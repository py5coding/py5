# *****************************************************************************
#
#   Part of the py5 library
#   Copyright (C) 2020-2024 Jim Schmitz
#
#   This library is free software: you can redistribute it and/or modify it
#   under the terms of the GNU Lesser General Public License as published by
#   the Free Software Foundation, either version 2.1 of the License, or (at
#   your option) any later version.
#
#   This library is distributed in the hope that it will be useful, but
#   WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser
#   General Public License for more details.
#
#   You should have received a copy of the GNU Lesser General Public License
#   along with this library. If not, see <https://www.gnu.org/licenses/>.
#
# *****************************************************************************
from typing import Callable, Union

import numpy as np
from PIL.Image import Image as PIL_Image

pshape_functions = []


def _convertable(obj):
    return any(pre(obj) for pre, _ in pshape_functions)


def _convert(sketch, obj, **kwargs):
    for precondition, convert_function in pshape_functions:
        if precondition(obj):
            obj = convert_function(sketch, obj, **kwargs)
            break
    else:
        classname = f"{obj.__class__.__module__}.{obj.__class__.__name__}"
        raise RuntimeError(
            f"py5 convert_shape() method is not able to convert objects of type {classname}"
        )

    return obj


def register_shape_conversion(
    precondition: Callable, convert_function: Callable
) -> None:
    """Register new shape conversion functionality to be used by `convert_shape()`.

    Parameters
    ----------

    convert_function: Callable
        function to convert object to Py5Shape object

    precondition: Callable
        predicate determining if an object can be converted

    Notes
    -----

    Register new shape conversion functionality to be used by `convert_shape()`.
    This will allow users to extend py5's capabilities and compatability within the
    Python ecosystem.

    The `precondition` parameter must be a function that accepts an object as a
    parameter and returns `True` if and only if the `convert_function` can
    successfully convert the object.

    The `convert_function` parameter must be a function that accepts an object as a
    parameter and returns a `Py5Shape` object."""
    pshape_functions.insert(0, (precondition, convert_function))


###############################################################################
# BUILT-IN CONVERSTION FUNCTIONS
###############################################################################


try:
    from shapely import affinity
    from shapely.geometry import (
        GeometryCollection,
        LinearRing,
        LineString,
        MultiLineString,
        MultiPoint,
        MultiPolygon,
        Point,
        Polygon,
    )

    def shapely_to_py5shape_precondition(obj):
        return isinstance(
            obj,
            (
                GeometryCollection,
                LinearRing,
                LineString,
                MultiLineString,
                MultiPoint,
                MultiPolygon,
                Point,
                Polygon,
            ),
        )

    def shapely_to_py5shape_converter(sketch, obj, _first_call=True, **kwargs):
        if _first_call and kwargs.get("flip_y_axis", False):
            obj = affinity.scale(obj, yfact=-1, origin="center")

        if isinstance(obj, Polygon):
            shape = sketch.create_shape()
            with shape.begin_closed_shape():
                if obj.exterior.coords:
                    coords = (
                        np.array(obj.exterior.coords)
                        if obj.exterior.is_ccw
                        else np.array(obj.exterior.coords[::-1])
                    )
                    shape.vertices(coords[:-1])
                for hole in obj.interiors:
                    with shape.begin_contour():
                        coords = (
                            np.array(hole.coords[::-1])
                            if hole.is_ccw
                            else np.array(hole.coords)
                        )
                        shape.vertices(coords[:-1])
            return shape
        elif isinstance(obj, LinearRing):
            shape = sketch.create_shape()
            with shape.begin_closed_shape():
                if not kwargs.get("lines_allow_fill", False):
                    shape.no_fill()
                coords = np.array(obj.coords)
                shape.vertices(coords[:-1])
            return shape
        elif isinstance(obj, LineString):
            shape = sketch.create_shape()
            with shape.begin_shape():
                if not kwargs.get("lines_allow_fill", False):
                    shape.no_fill()
                coords = np.array(obj.coords)
                shape.vertices(coords)
            return shape
        elif isinstance(obj, MultiPoint):
            shape = sketch.create_shape()
            with shape.begin_shape(sketch.POINTS):
                coords = np.array([p.coords for p in obj.geoms]).squeeze()
                shape.vertices(coords)
            return shape
        elif isinstance(obj, Point):
            shape = sketch.create_shape(sketch.POINT, obj.x, obj.y)
            return shape
        elif isinstance(obj, (GeometryCollection, MultiPolygon, MultiLineString)):
            shape = sketch.create_shape(sketch.GROUP)
            for p in obj.geoms:
                shape.add_child(
                    shapely_to_py5shape_converter(
                        sketch, p, _first_call=False, **kwargs
                    )
                )
            return shape
        else:
            raise RuntimeError(f"Py5 Converter is not able to convert {str(obj)}")

    register_shape_conversion(
        shapely_to_py5shape_precondition, shapely_to_py5shape_converter
    )

except Exception:
    pass


try:
    from trimesh import PointCloud, Scene, Trimesh
    from trimesh.path import Path2D, Path3D
    from trimesh.visual import ColorVisuals, TextureVisuals

    ##### Path2D and Path3D #####

    def trimesh_path2d_path3d_to_py5shape_precondition(obj):
        return isinstance(obj, (Path2D, Path3D))

    def trimesh_path2d_path3d_to_py5shape_converter(
        sketch, obj: Union[Path2D, Path3D], **kwargs
    ):
        def helper(entity, color):
            shape = sketch.create_shape()

            if entity.closed:
                with shape.begin_closed_shape():
                    if not kwargs.get("lines_allow_fill", False):
                        shape.no_fill()

                    if color is not None:
                        shape.stroke(
                            color[0] * 65536
                            + color[1] * 256
                            + color[2]
                            + color[3] * 16777216
                        )

                    shape.vertices(entity.discrete(obj.vertices)[:-1])
            else:
                with shape.begin_shape():
                    if not kwargs.get("lines_allow_fill", False):
                        shape.no_fill()

                    if color is not None:
                        shape.stroke(
                            color[0] * 65536
                            + color[1] * 256
                            + color[2]
                            + color[3] * 16777216
                        )

                    shape.vertices(entity.discrete(obj.vertices))

            return shape

        if len(obj.entities) == 1:
            color = None if obj.colors is None else obj.colors[0]
            shape = helper(obj.entities[0], color)
        else:
            shape = sketch.create_shape(sketch.GROUP)
            for i, entity in enumerate(obj.entities):
                color = None if obj.colors is None else obj.colors[i]
                shape.add_child(helper(entity, color))

        return shape

    register_shape_conversion(
        trimesh_path2d_path3d_to_py5shape_precondition,
        trimesh_path2d_path3d_to_py5shape_converter,
    )

    ##### PointCloud #####

    def trimesh_pointcloud_to_py5shape_precondition(obj):
        return isinstance(obj, PointCloud)

    def trimesh_pointcloud_to_py5shape_converter(sketch, obj: PointCloud, **kwargs):
        shape = sketch.create_shape()

        with shape.begin_shape(sketch.POINTS):
            if obj.colors.size > 0 and (color := obj.colors.squeeze()).shape == (4,):
                shape.stroke(*color)

            shape.vertices(obj.vertices)

        if obj.colors.size > 0 and obj.colors.shape == (obj.vertices.shape[0], 4):
            colors = (
                obj.colors[:, 0] * 65536
                + obj.colors[:, 1] * 256
                + obj.colors[:, 2]
                + obj.colors[:, 3] * 16777216
            )
            shape.set_strokes(colors)

        return shape

    register_shape_conversion(
        trimesh_pointcloud_to_py5shape_precondition,
        trimesh_pointcloud_to_py5shape_converter,
    )

    ##### Trimesh #####

    def trimesh_trimesh_to_py5shape_precondition(obj):
        return isinstance(obj, Trimesh)

    def trimesh_trimesh_to_py5shape_converter(sketch, obj: Trimesh, **kwargs):
        shape = sketch.create_shape()
        use_texture = False
        vertices_fill_colors = None
        shape_fill_color = None
        texture = None

        obj_faces_ravel = obj.faces.ravel()
        vertices = obj.vertices[obj_faces_ravel]

        if isinstance(obj.visual, TextureVisuals):
            use_texture = True
            uv = obj.visual.uv[obj_faces_ravel]
            uv[:, 1] = 1 - uv[:, 1]
            vertices = np.hstack([vertices, uv])

            if "texture" in kwargs:
                from . import Py5Graphics, Py5Image

                tex = kwargs["texture"]
                if isinstance(tex, (Py5Image, Py5Graphics)):
                    texture = tex
                elif isinstance(tex, PIL_Image):
                    texture = sketch.convert_image(tex)
            elif (
                hasattr(obj.visual.material, "baseColorTexture")
                and obj.visual.material.baseColorTexture is not None
            ):
                try:
                    texture = sketch.convert_image(obj.visual.material.baseColorTexture)
                except:
                    pass

        elif isinstance(obj.visual, ColorVisuals) and obj.visual.kind is not None:
            if obj.visual.kind == "vertex":
                if obj.visual.vertex_colors.shape == (obj.vertices.shape[0], 4):
                    vertices_fill_colors = (
                        obj.visual.vertex_colors[obj_faces_ravel, 0] * 65536
                        + obj.visual.vertex_colors[obj_faces_ravel, 1] * 256
                        + obj.visual.vertex_colors[obj_faces_ravel, 2]
                        + obj.visual.vertex_colors[obj_faces_ravel, 3] * 16777216
                    )
                elif (color := obj.visual.vertex_colors.squeeze()).shape == (4,):
                    shape_fill_color = color
            elif obj.visual.kind == "face":
                if obj.visual.face_colors.shape == (obj.faces.shape[0], 4):
                    vertices_fill_colors = np.repeat(
                        obj.visual.face_colors[:, 0] * 65536
                        + obj.visual.face_colors[:, 1] * 256
                        + obj.visual.face_colors[:, 2]
                        + obj.visual.face_colors[:, 3] * 16777216,
                        3,
                    )
                elif (color := obj.visual.face_colors.squeeze()).shape == (4,):
                    shape_fill_color = color

        with shape.begin_shape(sketch.TRIANGLES):
            if vertices_fill_colors is not None:
                shape.no_stroke()
            if use_texture:
                shape.no_stroke()
                shape.texture_mode(sketch.NORMAL)
                if texture is not None:
                    shape.texture(texture)
            if shape_fill_color is not None:
                shape.no_stroke()
                shape.fill(*shape_fill_color)

            shape.vertices(vertices)

        if vertices_fill_colors is not None:
            shape.set_fills(vertices_fill_colors)

        return shape

    register_shape_conversion(
        trimesh_trimesh_to_py5shape_precondition, trimesh_trimesh_to_py5shape_converter
    )

    def trimesh_scene_to_py5shape_precondition(obj):
        return isinstance(obj, Scene)

    ##### Scene #####

    def trimesh_scene_to_py5shape_converter(sketch, obj: Scene, **kwargs):
        def helper(geometry):
            if isinstance(geometry, (Path2D, Path3D, PointCloud, Trimesh)):
                return _convert(sketch, geometry, **kwargs)
            else:
                classname = (
                    f"{geometry.__class__.__module__}.{geometry.__class__.__name__}"
                )
                raise RuntimeError(
                    f"py5 convert_shape() method is not able to convert trimesh objects of type {classname}"
                )

        if len(obj.geometry) == 1:
            shape = helper(list(obj.geometry.values())[0])
        else:
            shape = sketch.create_shape(sketch.GROUP)

            for name, geometry in obj.geometry.items():
                child = helper(geometry)
                child.set_name(name)
                shape.add_child(child)

        return shape

    register_shape_conversion(
        trimesh_scene_to_py5shape_precondition, trimesh_scene_to_py5shape_converter
    )


except Exception:
    pass
