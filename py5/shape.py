# *****************************************************************************
#
#   Part of the py5 library
#   Copyright (C) 2020-2021 Jim Schmitz
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
from __future__ import annotations

import functools
from pathlib import Path
from typing import overload, List  # noqa
from nptyping import NDArray, Float  # noqa

from jpype import JException
from jpype.types import JBoolean, JInt, JFloat

from .pmath import _get_pvector_wrapper  # noqa


def _return_list_py5shapes(f):
    @functools.wraps(f)
    def decorated(self_, *args):
        return [Py5Shape(s) for s in f(self_, *args)]
    return decorated


def _return_py5shape(f):
    @functools.wraps(f)
    def decorated(self_, *args):
        return Py5Shape(f(self_, *args))
    return decorated


def _py5shape_type_fixer(f):
    @functools.wraps(f)
    def decorated(self_, *args):
        def fix_type(arg):
            if isinstance(arg, bool):
                return JBoolean(arg)
            elif isinstance(arg, int):
                return JInt(arg)
            elif isinstance(arg, float):
                return JFloat(arg)
            else:
                return arg
        args = [fix_type(a) for a in args]
        return f(self_, *args)
    return decorated


def _load_py5shape(f):
    @functools.wraps(f)
    def decorated(self_, *args):
        try:
            return Py5Shape(f(self_, *args))
        except JException as e:
            msg = e.message()
            if msg == 'None':
                msg = 'shape file cannot be found'
        raise RuntimeError('cannot load shape ' +
                           str(args[0]) + '. error message: ' + msg)
    return decorated


class Py5Shape:
    """Datatype for storing shapes.

    Underlying Java class: PShape.PShape

    Notes
    -----

    Datatype for storing shapes. Before a shape is used, it must be loaded with the
    ``load_shape()`` or created with the ``create_shape()``. The ``shape()``
    function is used to draw the shape to the display window. Processing can
    currently load and display SVG (Scalable Vector Graphics) and OBJ shapes. OBJ
    files can only be opened using the ``P3D`` renderer. The ``load_shape()``
    function supports SVG files created with Inkscape and Adobe Illustrator. It is
    not a full SVG implementation, but offers some straightforward support for
    handling vector data.

    The ``Py5Shape`` object contains a group of methods that can operate on the
    shape data. Some of the methods are listed below, but the full list used for
    creating and modifying shapes is available here in the Processing Javadoc.

    To create a new shape, use the ``create_shape()`` function. Do not use the
    syntax ``new Py5Shape()``.
    """

    def __init__(self, pshape):
        self._instance = pshape

    def _get_depth(self) -> float:
        """The documentation for this field or method has not yet been written.

        Underlying Java field: PShape.depth

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.depth
    depth: float = property(fget=_get_depth)

    def _get_height(self) -> float:
        """The height of the PShape document.

        Underlying Java field: PShape.height

        Notes
        -----

        The height of the PShape document.
        """
        return self._instance.height
    height: float = property(fget=_get_height)

    def _get_width(self) -> float:
        """The width of the PShape document.

        Underlying Java field: PShape.width

        Notes
        -----

        The width of the PShape document.
        """
        return self._instance.width
    width: float = property(fget=_get_width)

    @overload
    def add_child(self, who: Py5Shape, /) -> None:
        """Adds a child PShape to a parent PShape that is defined as a GROUP.

        Underlying Java method: PShape.addChild

        Methods
        -------

        You can use any of the following signatures:

         * add_child(who: Py5Shape, /) -> None
         * add_child(who: Py5Shape, idx: int, /) -> None

        Parameters
        ----------

        idx: int
            the layer position in which to insert the new child

        who: Py5Shape
            any variable of type PShape

        Notes
        -----

        Adds a child PShape to a parent PShape that is defined as a GROUP. In the
        example, the three shapes ``path``, ``rectangle``, and ``circle`` are added to a
        parent PShape variable named ``house`` that is a GROUP.
        """
        pass

    @overload
    def add_child(self, who: Py5Shape, idx: int, /) -> None:
        """Adds a child PShape to a parent PShape that is defined as a GROUP.

        Underlying Java method: PShape.addChild

        Methods
        -------

        You can use any of the following signatures:

         * add_child(who: Py5Shape, /) -> None
         * add_child(who: Py5Shape, idx: int, /) -> None

        Parameters
        ----------

        idx: int
            the layer position in which to insert the new child

        who: Py5Shape
            any variable of type PShape

        Notes
        -----

        Adds a child PShape to a parent PShape that is defined as a GROUP. In the
        example, the three shapes ``path``, ``rectangle``, and ``circle`` are added to a
        parent PShape variable named ``house`` that is a GROUP.
        """
        pass

    def add_child(self, *args):
        """Adds a child PShape to a parent PShape that is defined as a GROUP.

        Underlying Java method: PShape.addChild

        Methods
        -------

        You can use any of the following signatures:

         * add_child(who: Py5Shape, /) -> None
         * add_child(who: Py5Shape, idx: int, /) -> None

        Parameters
        ----------

        idx: int
            the layer position in which to insert the new child

        who: Py5Shape
            any variable of type PShape

        Notes
        -----

        Adds a child PShape to a parent PShape that is defined as a GROUP. In the
        example, the three shapes ``path``, ``rectangle``, and ``circle`` are added to a
        parent PShape variable named ``house`` that is a GROUP.
        """
        return self._instance.addChild(*args)

    def add_name(self, nom: str, shape: Py5Shape, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.addName

        Parameters
        ----------

        nom: str
            missing variable description

        shape: Py5Shape
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.addName(nom, shape)

    @overload
    def ambient(self, gray: float, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.ambient

        Methods
        -------

        You can use any of the following signatures:

         * ambient(gray: float, /) -> None
         * ambient(rgb: int, /) -> None
         * ambient(x: float, y: float, z: float, /) -> None

        Parameters
        ----------

        gray: float
            missing variable description

        rgb: int
            missing variable description

        x: float
            missing variable description

        y: float
            missing variable description

        z: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    @overload
    def ambient(self, x: float, y: float, z: float, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.ambient

        Methods
        -------

        You can use any of the following signatures:

         * ambient(gray: float, /) -> None
         * ambient(rgb: int, /) -> None
         * ambient(x: float, y: float, z: float, /) -> None

        Parameters
        ----------

        gray: float
            missing variable description

        rgb: int
            missing variable description

        x: float
            missing variable description

        y: float
            missing variable description

        z: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    @overload
    def ambient(self, rgb: int, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.ambient

        Methods
        -------

        You can use any of the following signatures:

         * ambient(gray: float, /) -> None
         * ambient(rgb: int, /) -> None
         * ambient(x: float, y: float, z: float, /) -> None

        Parameters
        ----------

        gray: float
            missing variable description

        rgb: int
            missing variable description

        x: float
            missing variable description

        y: float
            missing variable description

        z: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    def ambient(self, *args):
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.ambient

        Methods
        -------

        You can use any of the following signatures:

         * ambient(gray: float, /) -> None
         * ambient(rgb: int, /) -> None
         * ambient(x: float, y: float, z: float, /) -> None

        Parameters
        ----------

        gray: float
            missing variable description

        rgb: int
            missing variable description

        x: float
            missing variable description

        y: float
            missing variable description

        z: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.ambient(*args)

    @overload
    def apply_matrix(self, n00: float, n01: float, n02: float,
                     n10: float, n11: float, n12: float, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.applyMatrix

        Methods
        -------

        You can use any of the following signatures:

         * apply_matrix(n00: float, n01: float, n02: float, n03: float, n10: float, n11: float, n12: float, n13: float, n20: float, n21: float, n22: float, n23: float, n30: float, n31: float, n32: float, n33: float, /) -> None
         * apply_matrix(n00: float, n01: float, n02: float, n10: float, n11: float, n12: float, /) -> None
         * apply_matrix(source: NDArray[(2, 3), Float], /) -> None
         * apply_matrix(source: NDArray[(4, 4), Float], /) -> None

        Parameters
        ----------

        n00: float
            missing variable description

        n01: float
            missing variable description

        n02: float
            missing variable description

        n03: float
            missing variable description

        n10: float
            missing variable description

        n11: float
            missing variable description

        n12: float
            missing variable description

        n13: float
            missing variable description

        n20: float
            missing variable description

        n21: float
            missing variable description

        n22: float
            missing variable description

        n23: float
            missing variable description

        n30: float
            missing variable description

        n31: float
            missing variable description

        n32: float
            missing variable description

        n33: float
            missing variable description

        source: NDArray[(2, 3), Float]
            missing variable description

        source: NDArray[(4, 4), Float]
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    @overload
    def apply_matrix(
            self,
            n00: float,
            n01: float,
            n02: float,
            n03: float,
            n10: float,
            n11: float,
            n12: float,
            n13: float,
            n20: float,
            n21: float,
            n22: float,
            n23: float,
            n30: float,
            n31: float,
            n32: float,
            n33: float,
            /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.applyMatrix

        Methods
        -------

        You can use any of the following signatures:

         * apply_matrix(n00: float, n01: float, n02: float, n03: float, n10: float, n11: float, n12: float, n13: float, n20: float, n21: float, n22: float, n23: float, n30: float, n31: float, n32: float, n33: float, /) -> None
         * apply_matrix(n00: float, n01: float, n02: float, n10: float, n11: float, n12: float, /) -> None
         * apply_matrix(source: NDArray[(2, 3), Float], /) -> None
         * apply_matrix(source: NDArray[(4, 4), Float], /) -> None

        Parameters
        ----------

        n00: float
            missing variable description

        n01: float
            missing variable description

        n02: float
            missing variable description

        n03: float
            missing variable description

        n10: float
            missing variable description

        n11: float
            missing variable description

        n12: float
            missing variable description

        n13: float
            missing variable description

        n20: float
            missing variable description

        n21: float
            missing variable description

        n22: float
            missing variable description

        n23: float
            missing variable description

        n30: float
            missing variable description

        n31: float
            missing variable description

        n32: float
            missing variable description

        n33: float
            missing variable description

        source: NDArray[(2, 3), Float]
            missing variable description

        source: NDArray[(4, 4), Float]
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    @overload
    def apply_matrix(self, source: NDArray[(2, 3), Float], /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.applyMatrix

        Methods
        -------

        You can use any of the following signatures:

         * apply_matrix(n00: float, n01: float, n02: float, n03: float, n10: float, n11: float, n12: float, n13: float, n20: float, n21: float, n22: float, n23: float, n30: float, n31: float, n32: float, n33: float, /) -> None
         * apply_matrix(n00: float, n01: float, n02: float, n10: float, n11: float, n12: float, /) -> None
         * apply_matrix(source: NDArray[(2, 3), Float], /) -> None
         * apply_matrix(source: NDArray[(4, 4), Float], /) -> None

        Parameters
        ----------

        n00: float
            missing variable description

        n01: float
            missing variable description

        n02: float
            missing variable description

        n03: float
            missing variable description

        n10: float
            missing variable description

        n11: float
            missing variable description

        n12: float
            missing variable description

        n13: float
            missing variable description

        n20: float
            missing variable description

        n21: float
            missing variable description

        n22: float
            missing variable description

        n23: float
            missing variable description

        n30: float
            missing variable description

        n31: float
            missing variable description

        n32: float
            missing variable description

        n33: float
            missing variable description

        source: NDArray[(2, 3), Float]
            missing variable description

        source: NDArray[(4, 4), Float]
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    @overload
    def apply_matrix(self, source: NDArray[(4, 4), Float], /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.applyMatrix

        Methods
        -------

        You can use any of the following signatures:

         * apply_matrix(n00: float, n01: float, n02: float, n03: float, n10: float, n11: float, n12: float, n13: float, n20: float, n21: float, n22: float, n23: float, n30: float, n31: float, n32: float, n33: float, /) -> None
         * apply_matrix(n00: float, n01: float, n02: float, n10: float, n11: float, n12: float, /) -> None
         * apply_matrix(source: NDArray[(2, 3), Float], /) -> None
         * apply_matrix(source: NDArray[(4, 4), Float], /) -> None

        Parameters
        ----------

        n00: float
            missing variable description

        n01: float
            missing variable description

        n02: float
            missing variable description

        n03: float
            missing variable description

        n10: float
            missing variable description

        n11: float
            missing variable description

        n12: float
            missing variable description

        n13: float
            missing variable description

        n20: float
            missing variable description

        n21: float
            missing variable description

        n22: float
            missing variable description

        n23: float
            missing variable description

        n30: float
            missing variable description

        n31: float
            missing variable description

        n32: float
            missing variable description

        n33: float
            missing variable description

        source: NDArray[(2, 3), Float]
            missing variable description

        source: NDArray[(4, 4), Float]
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    def apply_matrix(self, *args):
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.applyMatrix

        Methods
        -------

        You can use any of the following signatures:

         * apply_matrix(n00: float, n01: float, n02: float, n03: float, n10: float, n11: float, n12: float, n13: float, n20: float, n21: float, n22: float, n23: float, n30: float, n31: float, n32: float, n33: float, /) -> None
         * apply_matrix(n00: float, n01: float, n02: float, n10: float, n11: float, n12: float, /) -> None
         * apply_matrix(source: NDArray[(2, 3), Float], /) -> None
         * apply_matrix(source: NDArray[(4, 4), Float], /) -> None

        Parameters
        ----------

        n00: float
            missing variable description

        n01: float
            missing variable description

        n02: float
            missing variable description

        n03: float
            missing variable description

        n10: float
            missing variable description

        n11: float
            missing variable description

        n12: float
            missing variable description

        n13: float
            missing variable description

        n20: float
            missing variable description

        n21: float
            missing variable description

        n22: float
            missing variable description

        n23: float
            missing variable description

        n30: float
            missing variable description

        n31: float
            missing variable description

        n32: float
            missing variable description

        n33: float
            missing variable description

        source: NDArray[(2, 3), Float]
            missing variable description

        source: NDArray[(4, 4), Float]
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.applyMatrix(*args)

    @overload
    def attrib(self, name: str, /, *values: bool) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.attrib

        Methods
        -------

        You can use any of the following signatures:

         * attrib(name: str, /, *values: bool) -> None
         * attrib(name: str, /, *values: float) -> None
         * attrib(name: str, /, *values: int) -> None

        Parameters
        ----------

        name: str
            missing variable description

        values: bool
            missing variable description

        values: float
            missing variable description

        values: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    @overload
    def attrib(self, name: str, /, *values: float) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.attrib

        Methods
        -------

        You can use any of the following signatures:

         * attrib(name: str, /, *values: bool) -> None
         * attrib(name: str, /, *values: float) -> None
         * attrib(name: str, /, *values: int) -> None

        Parameters
        ----------

        name: str
            missing variable description

        values: bool
            missing variable description

        values: float
            missing variable description

        values: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    @overload
    def attrib(self, name: str, /, *values: int) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.attrib

        Methods
        -------

        You can use any of the following signatures:

         * attrib(name: str, /, *values: bool) -> None
         * attrib(name: str, /, *values: float) -> None
         * attrib(name: str, /, *values: int) -> None

        Parameters
        ----------

        name: str
            missing variable description

        values: bool
            missing variable description

        values: float
            missing variable description

        values: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    @_py5shape_type_fixer
    def attrib(self, *args):
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.attrib

        Methods
        -------

        You can use any of the following signatures:

         * attrib(name: str, /, *values: bool) -> None
         * attrib(name: str, /, *values: float) -> None
         * attrib(name: str, /, *values: int) -> None

        Parameters
        ----------

        name: str
            missing variable description

        values: bool
            missing variable description

        values: float
            missing variable description

        values: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.attrib(*args)

    def attrib_color(self, name: str, color: int, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.attribColor

        Parameters
        ----------

        color: int
            missing variable description

        name: str
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.attribColor(name, color)

    def attrib_normal(self, name: str, nx: float,
                      ny: float, nz: float, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.attribNormal

        Parameters
        ----------

        name: str
            missing variable description

        nx: float
            missing variable description

        ny: float
            missing variable description

        nz: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.attribNormal(name, nx, ny, nz)

    def attrib_position(self, name: str, x: float,
                        y: float, z: float, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.attribPosition

        Parameters
        ----------

        name: str
            missing variable description

        x: float
            missing variable description

        y: float
            missing variable description

        z: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.attribPosition(name, x, y, z)

    def begin_contour(self) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.beginContour

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.beginContour()

    @overload
    def begin_shape(self) -> None:
        """This method is used to start a custom shape created with the ``create_shape()``
        function.

        Underlying Java method: PShape.beginShape

        Methods
        -------

        You can use any of the following signatures:

         * begin_shape() -> None
         * begin_shape(kind: int, /) -> None

        Parameters
        ----------

        kind: int
            missing variable description

        Notes
        -----

        This method is used to start a custom shape created with the ``create_shape()``
        function. It's always and only used with ``create_shape()``.
        """
        pass

    @overload
    def begin_shape(self, kind: int, /) -> None:
        """This method is used to start a custom shape created with the ``create_shape()``
        function.

        Underlying Java method: PShape.beginShape

        Methods
        -------

        You can use any of the following signatures:

         * begin_shape() -> None
         * begin_shape(kind: int, /) -> None

        Parameters
        ----------

        kind: int
            missing variable description

        Notes
        -----

        This method is used to start a custom shape created with the ``create_shape()``
        function. It's always and only used with ``create_shape()``.
        """
        pass

    def begin_shape(self, *args):
        """This method is used to start a custom shape created with the ``create_shape()``
        function.

        Underlying Java method: PShape.beginShape

        Methods
        -------

        You can use any of the following signatures:

         * begin_shape() -> None
         * begin_shape(kind: int, /) -> None

        Parameters
        ----------

        kind: int
            missing variable description

        Notes
        -----

        This method is used to start a custom shape created with the ``create_shape()``
        function. It's always and only used with ``create_shape()``.
        """
        return self._instance.beginShape(*args)

    def bezier_detail(self, detail: int, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.bezierDetail

        Parameters
        ----------

        detail: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.bezierDetail(detail)

    @overload
    def bezier_vertex(self, x2: float, y2: float, x3: float,
                      y3: float, x4: float, y4: float, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.bezierVertex

        Methods
        -------

        You can use any of the following signatures:

         * bezier_vertex(x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, /) -> None
         * bezier_vertex(x2: float, y2: float, z2: float, x3: float, y3: float, z3: float, x4: float, y4: float, z4: float, /) -> None

        Parameters
        ----------

        x2: float
            missing variable description

        x3: float
            missing variable description

        x4: float
            missing variable description

        y2: float
            missing variable description

        y3: float
            missing variable description

        y4: float
            missing variable description

        z2: float
            missing variable description

        z3: float
            missing variable description

        z4: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    @overload
    def bezier_vertex(self, x2: float, y2: float, z2: float, x3: float,
                      y3: float, z3: float, x4: float, y4: float, z4: float, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.bezierVertex

        Methods
        -------

        You can use any of the following signatures:

         * bezier_vertex(x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, /) -> None
         * bezier_vertex(x2: float, y2: float, z2: float, x3: float, y3: float, z3: float, x4: float, y4: float, z4: float, /) -> None

        Parameters
        ----------

        x2: float
            missing variable description

        x3: float
            missing variable description

        x4: float
            missing variable description

        y2: float
            missing variable description

        y3: float
            missing variable description

        y4: float
            missing variable description

        z2: float
            missing variable description

        z3: float
            missing variable description

        z4: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    def bezier_vertex(self, *args):
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.bezierVertex

        Methods
        -------

        You can use any of the following signatures:

         * bezier_vertex(x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, /) -> None
         * bezier_vertex(x2: float, y2: float, z2: float, x3: float, y3: float, z3: float, x4: float, y4: float, z4: float, /) -> None

        Parameters
        ----------

        x2: float
            missing variable description

        x3: float
            missing variable description

        x4: float
            missing variable description

        y2: float
            missing variable description

        y3: float
            missing variable description

        y4: float
            missing variable description

        z2: float
            missing variable description

        z3: float
            missing variable description

        z4: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.bezierVertex(*args)

    @overload
    def color_mode(self, mode: int, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.colorMode

        Methods
        -------

        You can use any of the following signatures:

         * color_mode(mode: int, /) -> None
         * color_mode(mode: int, max: float, /) -> None
         * color_mode(mode: int, max_x: float, max_y: float, max_z: float, /) -> None
         * color_mode(mode: int, max_x: float, max_y: float, max_z: float, max_a: float, /) -> None

        Parameters
        ----------

        max: float
            missing variable description

        max_a: float
            missing variable description

        max_x: float
            missing variable description

        max_y: float
            missing variable description

        max_z: float
            missing variable description

        mode: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    @overload
    def color_mode(self, mode: int, max: float, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.colorMode

        Methods
        -------

        You can use any of the following signatures:

         * color_mode(mode: int, /) -> None
         * color_mode(mode: int, max: float, /) -> None
         * color_mode(mode: int, max_x: float, max_y: float, max_z: float, /) -> None
         * color_mode(mode: int, max_x: float, max_y: float, max_z: float, max_a: float, /) -> None

        Parameters
        ----------

        max: float
            missing variable description

        max_a: float
            missing variable description

        max_x: float
            missing variable description

        max_y: float
            missing variable description

        max_z: float
            missing variable description

        mode: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    @overload
    def color_mode(self, mode: int, max_x: float,
                   max_y: float, max_z: float, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.colorMode

        Methods
        -------

        You can use any of the following signatures:

         * color_mode(mode: int, /) -> None
         * color_mode(mode: int, max: float, /) -> None
         * color_mode(mode: int, max_x: float, max_y: float, max_z: float, /) -> None
         * color_mode(mode: int, max_x: float, max_y: float, max_z: float, max_a: float, /) -> None

        Parameters
        ----------

        max: float
            missing variable description

        max_a: float
            missing variable description

        max_x: float
            missing variable description

        max_y: float
            missing variable description

        max_z: float
            missing variable description

        mode: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    @overload
    def color_mode(self, mode: int, max_x: float, max_y: float,
                   max_z: float, max_a: float, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.colorMode

        Methods
        -------

        You can use any of the following signatures:

         * color_mode(mode: int, /) -> None
         * color_mode(mode: int, max: float, /) -> None
         * color_mode(mode: int, max_x: float, max_y: float, max_z: float, /) -> None
         * color_mode(mode: int, max_x: float, max_y: float, max_z: float, max_a: float, /) -> None

        Parameters
        ----------

        max: float
            missing variable description

        max_a: float
            missing variable description

        max_x: float
            missing variable description

        max_y: float
            missing variable description

        max_z: float
            missing variable description

        mode: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    def color_mode(self, *args):
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.colorMode

        Methods
        -------

        You can use any of the following signatures:

         * color_mode(mode: int, /) -> None
         * color_mode(mode: int, max: float, /) -> None
         * color_mode(mode: int, max_x: float, max_y: float, max_z: float, /) -> None
         * color_mode(mode: int, max_x: float, max_y: float, max_z: float, max_a: float, /) -> None

        Parameters
        ----------

        max: float
            missing variable description

        max_a: float
            missing variable description

        max_x: float
            missing variable description

        max_y: float
            missing variable description

        max_z: float
            missing variable description

        mode: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.colorMode(*args)

    def contains(self, x: float, y: float, /) -> bool:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.contains

        Parameters
        ----------

        x: float
            missing variable description

        y: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.contains(x, y)

    def curve_detail(self, detail: int, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.curveDetail

        Parameters
        ----------

        detail: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.curveDetail(detail)

    def curve_tightness(self, tightness: float, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.curveTightness

        Parameters
        ----------

        tightness: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.curveTightness(tightness)

    @overload
    def curve_vertex(self, x: float, y: float, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.curveVertex

        Methods
        -------

        You can use any of the following signatures:

         * curve_vertex(x: float, y: float, /) -> None
         * curve_vertex(x: float, y: float, z: float, /) -> None

        Parameters
        ----------

        x: float
            missing variable description

        y: float
            missing variable description

        z: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    @overload
    def curve_vertex(self, x: float, y: float, z: float, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.curveVertex

        Methods
        -------

        You can use any of the following signatures:

         * curve_vertex(x: float, y: float, /) -> None
         * curve_vertex(x: float, y: float, z: float, /) -> None

        Parameters
        ----------

        x: float
            missing variable description

        y: float
            missing variable description

        z: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    def curve_vertex(self, *args):
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.curveVertex

        Methods
        -------

        You can use any of the following signatures:

         * curve_vertex(x: float, y: float, /) -> None
         * curve_vertex(x: float, y: float, z: float, /) -> None

        Parameters
        ----------

        x: float
            missing variable description

        y: float
            missing variable description

        z: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.curveVertex(*args)

    def disable_style(self) -> None:
        """Disables the shape's style data and uses Processing's current styles.

        Underlying Java method: PShape.disableStyle

        Notes
        -----

        Disables the shape's style data and uses Processing's current styles. Styles
        include attributes such as colors, stroke weight, and stroke joints.
        """
        return self._instance.disableStyle()

    @overload
    def emissive(self, gray: float, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.emissive

        Methods
        -------

        You can use any of the following signatures:

         * emissive(gray: float, /) -> None
         * emissive(rgb: int, /) -> None
         * emissive(x: float, y: float, z: float, /) -> None

        Parameters
        ----------

        gray: float
            missing variable description

        rgb: int
            missing variable description

        x: float
            missing variable description

        y: float
            missing variable description

        z: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    @overload
    def emissive(self, x: float, y: float, z: float, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.emissive

        Methods
        -------

        You can use any of the following signatures:

         * emissive(gray: float, /) -> None
         * emissive(rgb: int, /) -> None
         * emissive(x: float, y: float, z: float, /) -> None

        Parameters
        ----------

        gray: float
            missing variable description

        rgb: int
            missing variable description

        x: float
            missing variable description

        y: float
            missing variable description

        z: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    @overload
    def emissive(self, rgb: int, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.emissive

        Methods
        -------

        You can use any of the following signatures:

         * emissive(gray: float, /) -> None
         * emissive(rgb: int, /) -> None
         * emissive(x: float, y: float, z: float, /) -> None

        Parameters
        ----------

        gray: float
            missing variable description

        rgb: int
            missing variable description

        x: float
            missing variable description

        y: float
            missing variable description

        z: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    def emissive(self, *args):
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.emissive

        Methods
        -------

        You can use any of the following signatures:

         * emissive(gray: float, /) -> None
         * emissive(rgb: int, /) -> None
         * emissive(x: float, y: float, z: float, /) -> None

        Parameters
        ----------

        gray: float
            missing variable description

        rgb: int
            missing variable description

        x: float
            missing variable description

        y: float
            missing variable description

        z: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.emissive(*args)

    def enable_style(self) -> None:
        """Enables the shape's style data and ignores Processing's current styles.

        Underlying Java method: PShape.enableStyle

        Notes
        -----

        Enables the shape's style data and ignores Processing's current styles. Styles
        include attributes such as colors, stroke weight, and stroke joints.
        """
        return self._instance.enableStyle()

    def end_contour(self) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.endContour

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.endContour()

    @overload
    def end_shape(self) -> None:
        """This method is used to complete a custom shape created with the
        ``create_shape()`` function.

        Underlying Java method: PShape.endShape

        Methods
        -------

        You can use any of the following signatures:

         * end_shape() -> None
         * end_shape(mode: int, /) -> None

        Parameters
        ----------

        mode: int
            missing variable description

        Notes
        -----

        This method is used to complete a custom shape created with the
        ``create_shape()`` function. It's always and only used with ``create_shape()``.
        """
        pass

    @overload
    def end_shape(self, mode: int, /) -> None:
        """This method is used to complete a custom shape created with the
        ``create_shape()`` function.

        Underlying Java method: PShape.endShape

        Methods
        -------

        You can use any of the following signatures:

         * end_shape() -> None
         * end_shape(mode: int, /) -> None

        Parameters
        ----------

        mode: int
            missing variable description

        Notes
        -----

        This method is used to complete a custom shape created with the
        ``create_shape()`` function. It's always and only used with ``create_shape()``.
        """
        pass

    def end_shape(self, *args):
        """This method is used to complete a custom shape created with the
        ``create_shape()`` function.

        Underlying Java method: PShape.endShape

        Methods
        -------

        You can use any of the following signatures:

         * end_shape() -> None
         * end_shape(mode: int, /) -> None

        Parameters
        ----------

        mode: int
            missing variable description

        Notes
        -----

        This method is used to complete a custom shape created with the
        ``create_shape()`` function. It's always and only used with ``create_shape()``.
        """
        return self._instance.endShape(*args)

    @overload
    def fill(self, gray: float, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.fill

        Methods
        -------

        You can use any of the following signatures:

         * fill(gray: float, /) -> None
         * fill(gray: float, alpha: float, /) -> None
         * fill(rgb: int, /) -> None
         * fill(rgb: int, alpha: float, /) -> None
         * fill(x: float, y: float, z: float, /) -> None
         * fill(x: float, y: float, z: float, a: float, /) -> None

        Parameters
        ----------

        a: float
            missing variable description

        alpha: float
            missing variable description

        gray: float
            missing variable description

        rgb: int
            missing variable description

        x: float
            missing variable description

        y: float
            missing variable description

        z: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    @overload
    def fill(self, gray: float, alpha: float, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.fill

        Methods
        -------

        You can use any of the following signatures:

         * fill(gray: float, /) -> None
         * fill(gray: float, alpha: float, /) -> None
         * fill(rgb: int, /) -> None
         * fill(rgb: int, alpha: float, /) -> None
         * fill(x: float, y: float, z: float, /) -> None
         * fill(x: float, y: float, z: float, a: float, /) -> None

        Parameters
        ----------

        a: float
            missing variable description

        alpha: float
            missing variable description

        gray: float
            missing variable description

        rgb: int
            missing variable description

        x: float
            missing variable description

        y: float
            missing variable description

        z: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    @overload
    def fill(self, x: float, y: float, z: float, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.fill

        Methods
        -------

        You can use any of the following signatures:

         * fill(gray: float, /) -> None
         * fill(gray: float, alpha: float, /) -> None
         * fill(rgb: int, /) -> None
         * fill(rgb: int, alpha: float, /) -> None
         * fill(x: float, y: float, z: float, /) -> None
         * fill(x: float, y: float, z: float, a: float, /) -> None

        Parameters
        ----------

        a: float
            missing variable description

        alpha: float
            missing variable description

        gray: float
            missing variable description

        rgb: int
            missing variable description

        x: float
            missing variable description

        y: float
            missing variable description

        z: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    @overload
    def fill(self, x: float, y: float, z: float, a: float, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.fill

        Methods
        -------

        You can use any of the following signatures:

         * fill(gray: float, /) -> None
         * fill(gray: float, alpha: float, /) -> None
         * fill(rgb: int, /) -> None
         * fill(rgb: int, alpha: float, /) -> None
         * fill(x: float, y: float, z: float, /) -> None
         * fill(x: float, y: float, z: float, a: float, /) -> None

        Parameters
        ----------

        a: float
            missing variable description

        alpha: float
            missing variable description

        gray: float
            missing variable description

        rgb: int
            missing variable description

        x: float
            missing variable description

        y: float
            missing variable description

        z: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    @overload
    def fill(self, rgb: int, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.fill

        Methods
        -------

        You can use any of the following signatures:

         * fill(gray: float, /) -> None
         * fill(gray: float, alpha: float, /) -> None
         * fill(rgb: int, /) -> None
         * fill(rgb: int, alpha: float, /) -> None
         * fill(x: float, y: float, z: float, /) -> None
         * fill(x: float, y: float, z: float, a: float, /) -> None

        Parameters
        ----------

        a: float
            missing variable description

        alpha: float
            missing variable description

        gray: float
            missing variable description

        rgb: int
            missing variable description

        x: float
            missing variable description

        y: float
            missing variable description

        z: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    @overload
    def fill(self, rgb: int, alpha: float, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.fill

        Methods
        -------

        You can use any of the following signatures:

         * fill(gray: float, /) -> None
         * fill(gray: float, alpha: float, /) -> None
         * fill(rgb: int, /) -> None
         * fill(rgb: int, alpha: float, /) -> None
         * fill(x: float, y: float, z: float, /) -> None
         * fill(x: float, y: float, z: float, a: float, /) -> None

        Parameters
        ----------

        a: float
            missing variable description

        alpha: float
            missing variable description

        gray: float
            missing variable description

        rgb: int
            missing variable description

        x: float
            missing variable description

        y: float
            missing variable description

        z: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    def fill(self, *args):
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.fill

        Methods
        -------

        You can use any of the following signatures:

         * fill(gray: float, /) -> None
         * fill(gray: float, alpha: float, /) -> None
         * fill(rgb: int, /) -> None
         * fill(rgb: int, alpha: float, /) -> None
         * fill(x: float, y: float, z: float, /) -> None
         * fill(x: float, y: float, z: float, a: float, /) -> None

        Parameters
        ----------

        a: float
            missing variable description

        alpha: float
            missing variable description

        gray: float
            missing variable description

        rgb: int
            missing variable description

        x: float
            missing variable description

        y: float
            missing variable description

        z: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.fill(*args)

    @_return_py5shape
    def find_child(self, target: str, /) -> Py5Shape:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.findChild

        Parameters
        ----------

        target: str
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.findChild(target)

    def get_ambient(self, index: int, /) -> int:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.getAmbient

        Parameters
        ----------

        index: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.getAmbient(index)

    @overload
    def get_child(self, index: int, /) -> Py5Shape:
        """Extracts a child shape from a parent shape.

        Underlying Java method: PShape.getChild

        Methods
        -------

        You can use any of the following signatures:

         * get_child(index: int, /) -> Py5Shape
         * get_child(target: str, /) -> Py5Shape

        Parameters
        ----------

        index: int
            the layer position of the shape to get

        target: str
            the name of the shape to get

        Notes
        -----

        Extracts a child shape from a parent shape. Specify the name of the shape with
        the ``target`` parameter. The shape is returned as a ``Py5Shape`` object, or
        ``None`` is returned if there is an error.
        """
        pass

    @overload
    def get_child(self, target: str, /) -> Py5Shape:
        """Extracts a child shape from a parent shape.

        Underlying Java method: PShape.getChild

        Methods
        -------

        You can use any of the following signatures:

         * get_child(index: int, /) -> Py5Shape
         * get_child(target: str, /) -> Py5Shape

        Parameters
        ----------

        index: int
            the layer position of the shape to get

        target: str
            the name of the shape to get

        Notes
        -----

        Extracts a child shape from a parent shape. Specify the name of the shape with
        the ``target`` parameter. The shape is returned as a ``Py5Shape`` object, or
        ``None`` is returned if there is an error.
        """
        pass

    @_return_py5shape
    def get_child(self, *args):
        """Extracts a child shape from a parent shape.

        Underlying Java method: PShape.getChild

        Methods
        -------

        You can use any of the following signatures:

         * get_child(index: int, /) -> Py5Shape
         * get_child(target: str, /) -> Py5Shape

        Parameters
        ----------

        index: int
            the layer position of the shape to get

        target: str
            the name of the shape to get

        Notes
        -----

        Extracts a child shape from a parent shape. Specify the name of the shape with
        the ``target`` parameter. The shape is returned as a ``Py5Shape`` object, or
        ``None`` is returned if there is an error.
        """
        return self._instance.getChild(*args)

    def get_child_count(self) -> int:
        """Returns the number of children within the PShape.

        Underlying Java method: PShape.getChildCount

        Notes
        -----

        Returns the number of children within the PShape.
        """
        return self._instance.getChildCount()

    def get_child_index(self, who: Py5Shape, /) -> int:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.getChildIndex

        Parameters
        ----------

        who: Py5Shape
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.getChildIndex(who)

    @_return_list_py5shapes
    def get_children(self) -> List[Py5Shape]:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.getChildren

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.getChildren()

    def get_depth(self) -> float:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.getDepth

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.getDepth()

    def get_emissive(self, index: int, /) -> int:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.getEmissive

        Parameters
        ----------

        index: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.getEmissive(index)

    def get_family(self) -> int:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.getFamily

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.getFamily()

    def get_fill(self, index: int, /) -> int:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.getFill

        Parameters
        ----------

        index: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.getFill(index)

    def get_height(self) -> float:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.getHeight

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.getHeight()

    def get_kind(self) -> int:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.getKind

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.getKind()

    def get_name(self) -> str:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.getName

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.getName()

    @overload
    def get_normal(self, index: int, /) -> NDArray[(Any,), Float]:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.getNormal

        Methods
        -------

        You can use any of the following signatures:

         * get_normal(index: int, /) -> NDArray[(Any,), Float]
         * get_normal(index: int, vec: NDArray[(Any,), Float], /) -> NDArray[(Any,), Float]

        Parameters
        ----------

        index: int
            missing variable description

        vec: NDArray[(Any,), Float]
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    @overload
    def get_normal(self, index: int, vec: NDArray[(
            Any,), Float], /) -> NDArray[(Any,), Float]:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.getNormal

        Methods
        -------

        You can use any of the following signatures:

         * get_normal(index: int, /) -> NDArray[(Any,), Float]
         * get_normal(index: int, vec: NDArray[(Any,), Float], /) -> NDArray[(Any,), Float]

        Parameters
        ----------

        index: int
            missing variable description

        vec: NDArray[(Any,), Float]
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    @_get_pvector_wrapper
    def get_normal(self, *args):
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.getNormal

        Methods
        -------

        You can use any of the following signatures:

         * get_normal(index: int, /) -> NDArray[(Any,), Float]
         * get_normal(index: int, vec: NDArray[(Any,), Float], /) -> NDArray[(Any,), Float]

        Parameters
        ----------

        index: int
            missing variable description

        vec: NDArray[(Any,), Float]
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.getNormal(*args)

    def get_normal_x(self, index: int, /) -> float:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.getNormalX

        Parameters
        ----------

        index: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.getNormalX(index)

    def get_normal_y(self, index: int, /) -> float:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.getNormalY

        Parameters
        ----------

        index: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.getNormalY(index)

    def get_normal_z(self, index: int, /) -> float:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.getNormalZ

        Parameters
        ----------

        index: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.getNormalZ(index)

    def get_param(self, index: int, /) -> float:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.getParam

        Parameters
        ----------

        index: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.getParam(index)

    @overload
    def get_params(self) -> NDArray[(Any,), Float]:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.getParams

        Methods
        -------

        You can use any of the following signatures:

         * get_params() -> NDArray[(Any,), Float]
         * get_params(target: NDArray[(Any,), Float], /) -> NDArray[(Any,), Float]

        Parameters
        ----------

        target: NDArray[(Any,), Float]
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    @overload
    def get_params(self, target: NDArray[(
            Any,), Float], /) -> NDArray[(Any,), Float]:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.getParams

        Methods
        -------

        You can use any of the following signatures:

         * get_params() -> NDArray[(Any,), Float]
         * get_params(target: NDArray[(Any,), Float], /) -> NDArray[(Any,), Float]

        Parameters
        ----------

        target: NDArray[(Any,), Float]
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    def get_params(self, *args):
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.getParams

        Methods
        -------

        You can use any of the following signatures:

         * get_params() -> NDArray[(Any,), Float]
         * get_params(target: NDArray[(Any,), Float], /) -> NDArray[(Any,), Float]

        Parameters
        ----------

        target: NDArray[(Any,), Float]
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.getParams(*args)

    @_return_py5shape
    def get_parent(self) -> Py5Shape:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.getParent

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.getParent()

    def get_shininess(self, index: int, /) -> float:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.getShininess

        Parameters
        ----------

        index: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.getShininess(index)

    def get_specular(self, index: int, /) -> int:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.getSpecular

        Parameters
        ----------

        index: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.getSpecular(index)

    def get_stroke(self, index: int, /) -> int:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.getStroke

        Parameters
        ----------

        index: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.getStroke(index)

    def get_stroke_weight(self, index: int, /) -> float:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.getStrokeWeight

        Parameters
        ----------

        index: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.getStrokeWeight(index)

    @_return_py5shape
    def get_tessellation(self) -> Py5Shape:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.getTessellation

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.getTessellation()

    def get_texture_u(self, index: int, /) -> float:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.getTextureU

        Parameters
        ----------

        index: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.getTextureU(index)

    def get_texture_v(self, index: int, /) -> float:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.getTextureV

        Parameters
        ----------

        index: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.getTextureV(index)

    def get_tint(self, index: int, /) -> int:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.getTint

        Parameters
        ----------

        index: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.getTint(index)

    @overload
    def get_vertex(self, index: int, /) -> NDArray[(Any,), Float]:
        """The ``get_vertex()`` method returns a PVector with the coordinates of the vertex
        point located at the position defined by the ``index`` parameter.

        Underlying Java method: PShape.getVertex

        Methods
        -------

        You can use any of the following signatures:

         * get_vertex(index: int, /) -> NDArray[(Any,), Float]
         * get_vertex(index: int, vec: NDArray[(Any,), Float], /) -> NDArray[(Any,), Float]

        Parameters
        ----------

        index: int
            the location of the vertex

        vec: NDArray[(Any,), Float]
            PVector to assign the data to

        Notes
        -----

        The ``get_vertex()`` method returns a PVector with the coordinates of the vertex
        point located at the position defined by the ``index`` parameter. This method
        works when shapes are created as shown in the example above, but won't work
        properly when a shape is defined explicitly (e.g. ``create_shape(RECT, 20, 20,
        80, 80)``.
        """
        pass

    @overload
    def get_vertex(self, index: int, vec: NDArray[(
            Any,), Float], /) -> NDArray[(Any,), Float]:
        """The ``get_vertex()`` method returns a PVector with the coordinates of the vertex
        point located at the position defined by the ``index`` parameter.

        Underlying Java method: PShape.getVertex

        Methods
        -------

        You can use any of the following signatures:

         * get_vertex(index: int, /) -> NDArray[(Any,), Float]
         * get_vertex(index: int, vec: NDArray[(Any,), Float], /) -> NDArray[(Any,), Float]

        Parameters
        ----------

        index: int
            the location of the vertex

        vec: NDArray[(Any,), Float]
            PVector to assign the data to

        Notes
        -----

        The ``get_vertex()`` method returns a PVector with the coordinates of the vertex
        point located at the position defined by the ``index`` parameter. This method
        works when shapes are created as shown in the example above, but won't work
        properly when a shape is defined explicitly (e.g. ``create_shape(RECT, 20, 20,
        80, 80)``.
        """
        pass

    @_get_pvector_wrapper
    def get_vertex(self, *args):
        """The ``get_vertex()`` method returns a PVector with the coordinates of the vertex
        point located at the position defined by the ``index`` parameter.

        Underlying Java method: PShape.getVertex

        Methods
        -------

        You can use any of the following signatures:

         * get_vertex(index: int, /) -> NDArray[(Any,), Float]
         * get_vertex(index: int, vec: NDArray[(Any,), Float], /) -> NDArray[(Any,), Float]

        Parameters
        ----------

        index: int
            the location of the vertex

        vec: NDArray[(Any,), Float]
            PVector to assign the data to

        Notes
        -----

        The ``get_vertex()`` method returns a PVector with the coordinates of the vertex
        point located at the position defined by the ``index`` parameter. This method
        works when shapes are created as shown in the example above, but won't work
        properly when a shape is defined explicitly (e.g. ``create_shape(RECT, 20, 20,
        80, 80)``.
        """
        return self._instance.getVertex(*args)

    def get_vertex_code(self, index: int, /) -> int:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.getVertexCode

        Parameters
        ----------

        index: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.getVertexCode(index)

    def get_vertex_code_count(self) -> int:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.getVertexCodeCount

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.getVertexCodeCount()

    def get_vertex_codes(self) -> JArray(JInt):
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.getVertexCodes

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.getVertexCodes()

    def get_vertex_count(self) -> int:
        """The ``get_vertex_count()`` method returns the number of vertices that make up a
        PShape.

        Underlying Java method: PShape.getVertexCount

        Notes
        -----

        The ``get_vertex_count()`` method returns the number of vertices that make up a
        PShape. In the above example, the value 4 is returned by the
        ``get_vertex_count()`` method because 4 vertices are defined in ``setup()``.
        """
        return self._instance.getVertexCount()

    def get_vertex_x(self, index: int, /) -> float:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.getVertexX

        Parameters
        ----------

        index: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.getVertexX(index)

    def get_vertex_y(self, index: int, /) -> float:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.getVertexY

        Parameters
        ----------

        index: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.getVertexY(index)

    def get_vertex_z(self, index: int, /) -> float:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.getVertexZ

        Parameters
        ----------

        index: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.getVertexZ(index)

    def get_width(self) -> float:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.getWidth

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.getWidth()

    def is2d(self) -> bool:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.is2D

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.is2D()

    def is3d(self) -> bool:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.is3D

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.is3D()

    def is_closed(self) -> bool:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.isClosed

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.isClosed()

    def is_visible(self) -> bool:
        """Returns a boolean value "true" if the image is set to be visible, "false" if
        not.

        Underlying Java method: PShape.isVisible

        Notes
        -----

        Returns a boolean value "true" if the image is set to be visible, "false" if
        not. This value can be modified with the ``set_visible()`` method.

        The default visibility of a shape is usually controlled by whatever program
        created the SVG file. For instance, this parameter is controlled by showing or
        hiding the shape in the layers palette in Adobe Illustrator.
        """
        return self._instance.isVisible()

    def no_fill(self) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.noFill

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.noFill()

    def no_stroke(self) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.noStroke

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.noStroke()

    def no_texture(self) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.noTexture

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.noTexture()

    def no_tint(self) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.noTint

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.noTint()

    def normal(self, nx: float, ny: float, nz: float, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.normal

        Parameters
        ----------

        nx: float
            missing variable description

        ny: float
            missing variable description

        nz: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.normal(nx, ny, nz)

    @overload
    def quadratic_vertex(self, cx: float, cy: float,
                         x3: float, y3: float, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.quadraticVertex

        Methods
        -------

        You can use any of the following signatures:

         * quadratic_vertex(cx: float, cy: float, cz: float, x3: float, y3: float, z3: float, /) -> None
         * quadratic_vertex(cx: float, cy: float, x3: float, y3: float, /) -> None

        Parameters
        ----------

        cx: float
            missing variable description

        cy: float
            missing variable description

        cz: float
            missing variable description

        x3: float
            missing variable description

        y3: float
            missing variable description

        z3: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    @overload
    def quadratic_vertex(self, cx: float, cy: float, cz: float,
                         x3: float, y3: float, z3: float, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.quadraticVertex

        Methods
        -------

        You can use any of the following signatures:

         * quadratic_vertex(cx: float, cy: float, cz: float, x3: float, y3: float, z3: float, /) -> None
         * quadratic_vertex(cx: float, cy: float, x3: float, y3: float, /) -> None

        Parameters
        ----------

        cx: float
            missing variable description

        cy: float
            missing variable description

        cz: float
            missing variable description

        x3: float
            missing variable description

        y3: float
            missing variable description

        z3: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    def quadratic_vertex(self, *args):
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.quadraticVertex

        Methods
        -------

        You can use any of the following signatures:

         * quadratic_vertex(cx: float, cy: float, cz: float, x3: float, y3: float, z3: float, /) -> None
         * quadratic_vertex(cx: float, cy: float, x3: float, y3: float, /) -> None

        Parameters
        ----------

        cx: float
            missing variable description

        cy: float
            missing variable description

        cz: float
            missing variable description

        x3: float
            missing variable description

        y3: float
            missing variable description

        z3: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.quadraticVertex(*args)

    def remove_child(self, idx: int, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.removeChild

        Parameters
        ----------

        idx: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.removeChild(idx)

    def reset_matrix(self) -> None:
        """Replaces the current matrix of a shape with the identity matrix.

        Underlying Java method: PShape.resetMatrix

        Notes
        -----

        Replaces the current matrix of a shape with the identity matrix. The equivalent
        function in OpenGL is ``gl_load_identity()``.
        """
        return self._instance.resetMatrix()

    @overload
    def rotate(self, angle: float, /) -> None:
        """Rotates the shape the amount specified by the ``angle`` parameter.

        Underlying Java method: PShape.rotate

        Methods
        -------

        You can use any of the following signatures:

         * rotate(angle: float, /) -> None
         * rotate(angle: float, v0: float, v1: float, v2: float, /) -> None

        Parameters
        ----------

        angle: float
            angle of rotation specified in radians

        v0: float
            missing variable description

        v1: float
            missing variable description

        v2: float
            missing variable description

        Notes
        -----

        Rotates the shape the amount specified by the ``angle`` parameter. Angles should
        be specified in radians (values from 0 to TWO_PI) or converted from degrees to
        radians with the ``radians()`` method.

        Shapes are always rotated around the upper-left corner of their bounding box.
        Positive numbers rotate objects in a clockwise direction. Transformations apply
        to everything that happens after and subsequent calls to the method accumulates
        the effect. For example, calling ``rotate(HALF_PI)`` and then
        ``rotate(HALF_PI)`` is the same as ``rotate(PI)``. This transformation is
        applied directly to the shape, it's not refreshed each time ``draw()`` is run.
        """
        pass

    @overload
    def rotate(self, angle: float, v0: float, v1: float, v2: float, /) -> None:
        """Rotates the shape the amount specified by the ``angle`` parameter.

        Underlying Java method: PShape.rotate

        Methods
        -------

        You can use any of the following signatures:

         * rotate(angle: float, /) -> None
         * rotate(angle: float, v0: float, v1: float, v2: float, /) -> None

        Parameters
        ----------

        angle: float
            angle of rotation specified in radians

        v0: float
            missing variable description

        v1: float
            missing variable description

        v2: float
            missing variable description

        Notes
        -----

        Rotates the shape the amount specified by the ``angle`` parameter. Angles should
        be specified in radians (values from 0 to TWO_PI) or converted from degrees to
        radians with the ``radians()`` method.

        Shapes are always rotated around the upper-left corner of their bounding box.
        Positive numbers rotate objects in a clockwise direction. Transformations apply
        to everything that happens after and subsequent calls to the method accumulates
        the effect. For example, calling ``rotate(HALF_PI)`` and then
        ``rotate(HALF_PI)`` is the same as ``rotate(PI)``. This transformation is
        applied directly to the shape, it's not refreshed each time ``draw()`` is run.
        """
        pass

    def rotate(self, *args):
        """Rotates the shape the amount specified by the ``angle`` parameter.

        Underlying Java method: PShape.rotate

        Methods
        -------

        You can use any of the following signatures:

         * rotate(angle: float, /) -> None
         * rotate(angle: float, v0: float, v1: float, v2: float, /) -> None

        Parameters
        ----------

        angle: float
            angle of rotation specified in radians

        v0: float
            missing variable description

        v1: float
            missing variable description

        v2: float
            missing variable description

        Notes
        -----

        Rotates the shape the amount specified by the ``angle`` parameter. Angles should
        be specified in radians (values from 0 to TWO_PI) or converted from degrees to
        radians with the ``radians()`` method.

        Shapes are always rotated around the upper-left corner of their bounding box.
        Positive numbers rotate objects in a clockwise direction. Transformations apply
        to everything that happens after and subsequent calls to the method accumulates
        the effect. For example, calling ``rotate(HALF_PI)`` and then
        ``rotate(HALF_PI)`` is the same as ``rotate(PI)``. This transformation is
        applied directly to the shape, it's not refreshed each time ``draw()`` is run.
        """
        return self._instance.rotate(*args)

    def rotate_x(self, angle: float, /) -> None:
        """Rotates the shape around the x-axis the amount specified by the ``angle``
        parameter.

        Underlying Java method: PShape.rotateX

        Parameters
        ----------

        angle: float
            angle of rotation specified in radians

        Notes
        -----

        Rotates the shape around the x-axis the amount specified by the ``angle``
        parameter. Angles should be specified in radians (values from 0 to TWO_PI) or
        converted from degrees to radians with the ``radians()`` method.

        Shapes are always rotated around the upper-left corner of their bounding box.
        Positive numbers rotate objects in a clockwise direction. Subsequent calls to
        the method accumulates the effect. For example, calling ``rotate_x(HALF_PI)``
        and then ``rotate_x(HALF_PI)`` is the same as ``rotate_x(PI)``. This
        transformation is applied directly to the shape, it's not refreshed each time
        ``draw()`` is run.

        This method requires a 3D renderer. You need to use P3D as a third parameter for
        the ``size()`` function as shown in the example above.
        """
        return self._instance.rotateX(angle)

    def rotate_y(self, angle: float, /) -> None:
        """Rotates the shape around the y-axis the amount specified by the ``angle``
        parameter.

        Underlying Java method: PShape.rotateY

        Parameters
        ----------

        angle: float
            angle of rotation specified in radians

        Notes
        -----

        Rotates the shape around the y-axis the amount specified by the ``angle``
        parameter. Angles should be specified in radians (values from 0 to TWO_PI) or
        converted from degrees to radians with the ``radians()`` method.

        Shapes are always rotated around the upper-left corner of their bounding box.
        Positive numbers rotate objects in a clockwise direction. Subsequent calls to
        the method accumulates the effect. For example, calling ``rotate_y(HALF_PI)``
        and then ``rotate_y(HALF_PI)`` is the same as ``rotate_y(PI)``. This
        transformation is applied directly to the shape, it's not refreshed each time
        ``draw()`` is run.

        This method requires a 3D renderer. You need to use P3D as a third parameter for
        the ``size()`` function as shown in the example above.
        """
        return self._instance.rotateY(angle)

    def rotate_z(self, angle: float, /) -> None:
        """Rotates the shape around the z-axis the amount specified by the ``angle``
        parameter.

        Underlying Java method: PShape.rotateZ

        Parameters
        ----------

        angle: float
            angle of rotation specified in radians

        Notes
        -----

        Rotates the shape around the z-axis the amount specified by the ``angle``
        parameter. Angles should be specified in radians (values from 0 to TWO_PI) or
        converted from degrees to radians with the ``radians()`` method.

        Shapes are always rotated around the upper-left corner of their bounding box.
        Positive numbers rotate objects in a clockwise direction. Subsequent calls to
        the method accumulates the effect. For example, calling ``rotate_z(HALF_PI)``
        and then ``rotate_z(HALF_PI)`` is the same as ``rotate_z(PI)``. This
        transformation is applied directly to the shape, it's not refreshed each time
        ``draw()`` is run.

        This method requires a 3D renderer. You need to use P3D as a third parameter for
        the ``size()`` function as shown in the example above.
        """
        return self._instance.rotateZ(angle)

    @overload
    def scale(self, s: float, /) -> None:
        """Increases or decreases the size of a shape by expanding and contracting
        vertices.

        Underlying Java method: PShape.scale

        Methods
        -------

        You can use any of the following signatures:

         * scale(s: float, /) -> None
         * scale(x: float, y: float, /) -> None
         * scale(x: float, y: float, z: float, /) -> None

        Parameters
        ----------

        s: float
            percentate to scale the object

        x: float
            percentage to scale the object in the x-axis

        y: float
            percentage to scale the object in the y-axis

        z: float
            percentage to scale the object in the z-axis

        Notes
        -----

        Increases or decreases the size of a shape by expanding and contracting
        vertices. Shapes always scale from the relative origin of their bounding box.
        Scale values are specified as decimal percentages. For example, the method call
        ``scale(2.0)`` increases the dimension of a shape by 200%. Subsequent calls to
        the method multiply the effect. For example, calling ``scale(2.0)`` and then
        ``scale(1.5)`` is the same as ``scale(3.0)``. This transformation is applied
        directly to the shape; it's not refreshed each time ``draw()`` is run.

        Using this method with the ``z`` parameter requires using the P3D parameter in
        combination with size.
        """
        pass

    @overload
    def scale(self, x: float, y: float, /) -> None:
        """Increases or decreases the size of a shape by expanding and contracting
        vertices.

        Underlying Java method: PShape.scale

        Methods
        -------

        You can use any of the following signatures:

         * scale(s: float, /) -> None
         * scale(x: float, y: float, /) -> None
         * scale(x: float, y: float, z: float, /) -> None

        Parameters
        ----------

        s: float
            percentate to scale the object

        x: float
            percentage to scale the object in the x-axis

        y: float
            percentage to scale the object in the y-axis

        z: float
            percentage to scale the object in the z-axis

        Notes
        -----

        Increases or decreases the size of a shape by expanding and contracting
        vertices. Shapes always scale from the relative origin of their bounding box.
        Scale values are specified as decimal percentages. For example, the method call
        ``scale(2.0)`` increases the dimension of a shape by 200%. Subsequent calls to
        the method multiply the effect. For example, calling ``scale(2.0)`` and then
        ``scale(1.5)`` is the same as ``scale(3.0)``. This transformation is applied
        directly to the shape; it's not refreshed each time ``draw()`` is run.

        Using this method with the ``z`` parameter requires using the P3D parameter in
        combination with size.
        """
        pass

    @overload
    def scale(self, x: float, y: float, z: float, /) -> None:
        """Increases or decreases the size of a shape by expanding and contracting
        vertices.

        Underlying Java method: PShape.scale

        Methods
        -------

        You can use any of the following signatures:

         * scale(s: float, /) -> None
         * scale(x: float, y: float, /) -> None
         * scale(x: float, y: float, z: float, /) -> None

        Parameters
        ----------

        s: float
            percentate to scale the object

        x: float
            percentage to scale the object in the x-axis

        y: float
            percentage to scale the object in the y-axis

        z: float
            percentage to scale the object in the z-axis

        Notes
        -----

        Increases or decreases the size of a shape by expanding and contracting
        vertices. Shapes always scale from the relative origin of their bounding box.
        Scale values are specified as decimal percentages. For example, the method call
        ``scale(2.0)`` increases the dimension of a shape by 200%. Subsequent calls to
        the method multiply the effect. For example, calling ``scale(2.0)`` and then
        ``scale(1.5)`` is the same as ``scale(3.0)``. This transformation is applied
        directly to the shape; it's not refreshed each time ``draw()`` is run.

        Using this method with the ``z`` parameter requires using the P3D parameter in
        combination with size.
        """
        pass

    def scale(self, *args):
        """Increases or decreases the size of a shape by expanding and contracting
        vertices.

        Underlying Java method: PShape.scale

        Methods
        -------

        You can use any of the following signatures:

         * scale(s: float, /) -> None
         * scale(x: float, y: float, /) -> None
         * scale(x: float, y: float, z: float, /) -> None

        Parameters
        ----------

        s: float
            percentate to scale the object

        x: float
            percentage to scale the object in the x-axis

        y: float
            percentage to scale the object in the y-axis

        z: float
            percentage to scale the object in the z-axis

        Notes
        -----

        Increases or decreases the size of a shape by expanding and contracting
        vertices. Shapes always scale from the relative origin of their bounding box.
        Scale values are specified as decimal percentages. For example, the method call
        ``scale(2.0)`` increases the dimension of a shape by 200%. Subsequent calls to
        the method multiply the effect. For example, calling ``scale(2.0)`` and then
        ``scale(1.5)`` is the same as ``scale(3.0)``. This transformation is applied
        directly to the shape; it's not refreshed each time ``draw()`` is run.

        Using this method with the ``z`` parameter requires using the P3D parameter in
        combination with size.
        """
        return self._instance.scale(*args)

    def set3d(self, val: bool, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.set3D

        Parameters
        ----------

        val: bool
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.set3D(val)

    @overload
    def set_ambient(self, ambient: int, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.setAmbient

        Methods
        -------

        You can use any of the following signatures:

         * set_ambient(ambient: int, /) -> None
         * set_ambient(index: int, ambient: int, /) -> None

        Parameters
        ----------

        ambient: int
            missing variable description

        index: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    @overload
    def set_ambient(self, index: int, ambient: int, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.setAmbient

        Methods
        -------

        You can use any of the following signatures:

         * set_ambient(ambient: int, /) -> None
         * set_ambient(index: int, ambient: int, /) -> None

        Parameters
        ----------

        ambient: int
            missing variable description

        index: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    def set_ambient(self, *args):
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.setAmbient

        Methods
        -------

        You can use any of the following signatures:

         * set_ambient(ambient: int, /) -> None
         * set_ambient(index: int, ambient: int, /) -> None

        Parameters
        ----------

        ambient: int
            missing variable description

        index: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.setAmbient(*args)

    @overload
    def set_attrib(self, name: str, index: int, /, *values: bool) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.setAttrib

        Methods
        -------

        You can use any of the following signatures:

         * set_attrib(name: str, index: int, /, *values: bool) -> None
         * set_attrib(name: str, index: int, /, *values: float) -> None
         * set_attrib(name: str, index: int, /, *values: int) -> None

        Parameters
        ----------

        index: int
            missing variable description

        name: str
            missing variable description

        values: bool
            missing variable description

        values: float
            missing variable description

        values: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    @overload
    def set_attrib(self, name: str, index: int, /, *values: float) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.setAttrib

        Methods
        -------

        You can use any of the following signatures:

         * set_attrib(name: str, index: int, /, *values: bool) -> None
         * set_attrib(name: str, index: int, /, *values: float) -> None
         * set_attrib(name: str, index: int, /, *values: int) -> None

        Parameters
        ----------

        index: int
            missing variable description

        name: str
            missing variable description

        values: bool
            missing variable description

        values: float
            missing variable description

        values: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    @overload
    def set_attrib(self, name: str, index: int, /, *values: int) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.setAttrib

        Methods
        -------

        You can use any of the following signatures:

         * set_attrib(name: str, index: int, /, *values: bool) -> None
         * set_attrib(name: str, index: int, /, *values: float) -> None
         * set_attrib(name: str, index: int, /, *values: int) -> None

        Parameters
        ----------

        index: int
            missing variable description

        name: str
            missing variable description

        values: bool
            missing variable description

        values: float
            missing variable description

        values: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    @_py5shape_type_fixer
    def set_attrib(self, *args):
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.setAttrib

        Methods
        -------

        You can use any of the following signatures:

         * set_attrib(name: str, index: int, /, *values: bool) -> None
         * set_attrib(name: str, index: int, /, *values: float) -> None
         * set_attrib(name: str, index: int, /, *values: int) -> None

        Parameters
        ----------

        index: int
            missing variable description

        name: str
            missing variable description

        values: bool
            missing variable description

        values: float
            missing variable description

        values: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.setAttrib(*args)

    @overload
    def set_emissive(self, emissive: int, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.setEmissive

        Methods
        -------

        You can use any of the following signatures:

         * set_emissive(emissive: int, /) -> None
         * set_emissive(index: int, emissive: int, /) -> None

        Parameters
        ----------

        emissive: int
            missing variable description

        index: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    @overload
    def set_emissive(self, index: int, emissive: int, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.setEmissive

        Methods
        -------

        You can use any of the following signatures:

         * set_emissive(emissive: int, /) -> None
         * set_emissive(index: int, emissive: int, /) -> None

        Parameters
        ----------

        emissive: int
            missing variable description

        index: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    def set_emissive(self, *args):
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.setEmissive

        Methods
        -------

        You can use any of the following signatures:

         * set_emissive(emissive: int, /) -> None
         * set_emissive(index: int, emissive: int, /) -> None

        Parameters
        ----------

        emissive: int
            missing variable description

        index: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.setEmissive(*args)

    def set_family(self, family: int, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.setFamily

        Parameters
        ----------

        family: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.setFamily(family)

    @overload
    def set_fill(self, fill: bool, /) -> None:
        """The ``set_fill()`` method defines the fill color of a ``Py5Shape``.

        Underlying Java method: PShape.setFill

        Methods
        -------

        You can use any of the following signatures:

         * set_fill(fill: bool, /) -> None
         * set_fill(fill: int, /) -> None
         * set_fill(index: int, fill: int, /) -> None

        Parameters
        ----------

        fill: bool
            missing variable description

        fill: int
            missing variable description

        index: int
            missing variable description

        Notes
        -----

        The ``set_fill()`` method defines the fill color of a ``Py5Shape``. This method
        is used after shapes are created or when a shape is defined explicitly (e.g.
        ``create_shape(RECT, 20, 20, 80, 80)``) as shown in the above example. When a
        shape is created with ``begin_shape()`` and ``end_shape()``, its attributes may
        be changed with ``fill()`` and ``stroke()`` within ``begin_shape()`` and
        ``end_shape()``. However, after the shape is created, only the ``set_fill()``
        method can define a new fill value for the ``Py5Shape``.
        """
        pass

    @overload
    def set_fill(self, fill: int, /) -> None:
        """The ``set_fill()`` method defines the fill color of a ``Py5Shape``.

        Underlying Java method: PShape.setFill

        Methods
        -------

        You can use any of the following signatures:

         * set_fill(fill: bool, /) -> None
         * set_fill(fill: int, /) -> None
         * set_fill(index: int, fill: int, /) -> None

        Parameters
        ----------

        fill: bool
            missing variable description

        fill: int
            missing variable description

        index: int
            missing variable description

        Notes
        -----

        The ``set_fill()`` method defines the fill color of a ``Py5Shape``. This method
        is used after shapes are created or when a shape is defined explicitly (e.g.
        ``create_shape(RECT, 20, 20, 80, 80)``) as shown in the above example. When a
        shape is created with ``begin_shape()`` and ``end_shape()``, its attributes may
        be changed with ``fill()`` and ``stroke()`` within ``begin_shape()`` and
        ``end_shape()``. However, after the shape is created, only the ``set_fill()``
        method can define a new fill value for the ``Py5Shape``.
        """
        pass

    @overload
    def set_fill(self, index: int, fill: int, /) -> None:
        """The ``set_fill()`` method defines the fill color of a ``Py5Shape``.

        Underlying Java method: PShape.setFill

        Methods
        -------

        You can use any of the following signatures:

         * set_fill(fill: bool, /) -> None
         * set_fill(fill: int, /) -> None
         * set_fill(index: int, fill: int, /) -> None

        Parameters
        ----------

        fill: bool
            missing variable description

        fill: int
            missing variable description

        index: int
            missing variable description

        Notes
        -----

        The ``set_fill()`` method defines the fill color of a ``Py5Shape``. This method
        is used after shapes are created or when a shape is defined explicitly (e.g.
        ``create_shape(RECT, 20, 20, 80, 80)``) as shown in the above example. When a
        shape is created with ``begin_shape()`` and ``end_shape()``, its attributes may
        be changed with ``fill()`` and ``stroke()`` within ``begin_shape()`` and
        ``end_shape()``. However, after the shape is created, only the ``set_fill()``
        method can define a new fill value for the ``Py5Shape``.
        """
        pass

    @_py5shape_type_fixer
    def set_fill(self, *args):
        """The ``set_fill()`` method defines the fill color of a ``Py5Shape``.

        Underlying Java method: PShape.setFill

        Methods
        -------

        You can use any of the following signatures:

         * set_fill(fill: bool, /) -> None
         * set_fill(fill: int, /) -> None
         * set_fill(index: int, fill: int, /) -> None

        Parameters
        ----------

        fill: bool
            missing variable description

        fill: int
            missing variable description

        index: int
            missing variable description

        Notes
        -----

        The ``set_fill()`` method defines the fill color of a ``Py5Shape``. This method
        is used after shapes are created or when a shape is defined explicitly (e.g.
        ``create_shape(RECT, 20, 20, 80, 80)``) as shown in the above example. When a
        shape is created with ``begin_shape()`` and ``end_shape()``, its attributes may
        be changed with ``fill()`` and ``stroke()`` within ``begin_shape()`` and
        ``end_shape()``. However, after the shape is created, only the ``set_fill()``
        method can define a new fill value for the ``Py5Shape``.
        """
        return self._instance.setFill(*args)

    def set_kind(self, kind: int, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.setKind

        Parameters
        ----------

        kind: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.setKind(kind)

    def set_name(self, name: str, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.setName

        Parameters
        ----------

        name: str
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.setName(name)

    def set_normal(self, index: int, nx: float,
                   ny: float, nz: float, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.setNormal

        Parameters
        ----------

        index: int
            missing variable description

        nx: float
            missing variable description

        ny: float
            missing variable description

        nz: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.setNormal(index, nx, ny, nz)

    def set_path(self, vcount: int,
                 verts: NDArray[(Any, Any), Float], /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.setPath

        Parameters
        ----------

        vcount: int
            missing variable description

        verts: NDArray[(Any, Any), Float]
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.setPath(vcount, verts)

    @overload
    def set_shininess(self, shine: float, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.setShininess

        Methods
        -------

        You can use any of the following signatures:

         * set_shininess(index: int, shine: float, /) -> None
         * set_shininess(shine: float, /) -> None

        Parameters
        ----------

        index: int
            missing variable description

        shine: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    @overload
    def set_shininess(self, index: int, shine: float, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.setShininess

        Methods
        -------

        You can use any of the following signatures:

         * set_shininess(index: int, shine: float, /) -> None
         * set_shininess(shine: float, /) -> None

        Parameters
        ----------

        index: int
            missing variable description

        shine: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    def set_shininess(self, *args):
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.setShininess

        Methods
        -------

        You can use any of the following signatures:

         * set_shininess(index: int, shine: float, /) -> None
         * set_shininess(shine: float, /) -> None

        Parameters
        ----------

        index: int
            missing variable description

        shine: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.setShininess(*args)

    @overload
    def set_specular(self, specular: int, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.setSpecular

        Methods
        -------

        You can use any of the following signatures:

         * set_specular(index: int, specular: int, /) -> None
         * set_specular(specular: int, /) -> None

        Parameters
        ----------

        index: int
            missing variable description

        specular: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    @overload
    def set_specular(self, index: int, specular: int, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.setSpecular

        Methods
        -------

        You can use any of the following signatures:

         * set_specular(index: int, specular: int, /) -> None
         * set_specular(specular: int, /) -> None

        Parameters
        ----------

        index: int
            missing variable description

        specular: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    def set_specular(self, *args):
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.setSpecular

        Methods
        -------

        You can use any of the following signatures:

         * set_specular(index: int, specular: int, /) -> None
         * set_specular(specular: int, /) -> None

        Parameters
        ----------

        index: int
            missing variable description

        specular: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.setSpecular(*args)

    @overload
    def set_stroke(self, stroke: bool, /) -> None:
        """The ``set_stroke()`` method defines the outline color of a ``Py5Shape``.

        Underlying Java method: PShape.setStroke

        Methods
        -------

        You can use any of the following signatures:

         * set_stroke(index: int, stroke: int, /) -> None
         * set_stroke(stroke: bool, /) -> None
         * set_stroke(stroke: int, /) -> None

        Parameters
        ----------

        index: int
            missing variable description

        stroke: bool
            missing variable description

        stroke: int
            missing variable description

        Notes
        -----

        The ``set_stroke()`` method defines the outline color of a ``Py5Shape``. This
        method is used after shapes are created or when a shape is defined explicitly
        (e.g. ``create_shape(RECT, 20, 20, 80, 80)``) as shown in the above example.
        When a shape is created with ``begin_shape()`` and ``end_shape()``, its
        attributes may be changed with ``fill()`` and ``stroke()`` within
        ``begin_shape()`` and ``end_shape()``. However, after the shape is created, only
        the ``set_stroke()`` method can define a new stroke value for the ``Py5Shape``.
        """
        pass

    @overload
    def set_stroke(self, stroke: int, /) -> None:
        """The ``set_stroke()`` method defines the outline color of a ``Py5Shape``.

        Underlying Java method: PShape.setStroke

        Methods
        -------

        You can use any of the following signatures:

         * set_stroke(index: int, stroke: int, /) -> None
         * set_stroke(stroke: bool, /) -> None
         * set_stroke(stroke: int, /) -> None

        Parameters
        ----------

        index: int
            missing variable description

        stroke: bool
            missing variable description

        stroke: int
            missing variable description

        Notes
        -----

        The ``set_stroke()`` method defines the outline color of a ``Py5Shape``. This
        method is used after shapes are created or when a shape is defined explicitly
        (e.g. ``create_shape(RECT, 20, 20, 80, 80)``) as shown in the above example.
        When a shape is created with ``begin_shape()`` and ``end_shape()``, its
        attributes may be changed with ``fill()`` and ``stroke()`` within
        ``begin_shape()`` and ``end_shape()``. However, after the shape is created, only
        the ``set_stroke()`` method can define a new stroke value for the ``Py5Shape``.
        """
        pass

    @overload
    def set_stroke(self, index: int, stroke: int, /) -> None:
        """The ``set_stroke()`` method defines the outline color of a ``Py5Shape``.

        Underlying Java method: PShape.setStroke

        Methods
        -------

        You can use any of the following signatures:

         * set_stroke(index: int, stroke: int, /) -> None
         * set_stroke(stroke: bool, /) -> None
         * set_stroke(stroke: int, /) -> None

        Parameters
        ----------

        index: int
            missing variable description

        stroke: bool
            missing variable description

        stroke: int
            missing variable description

        Notes
        -----

        The ``set_stroke()`` method defines the outline color of a ``Py5Shape``. This
        method is used after shapes are created or when a shape is defined explicitly
        (e.g. ``create_shape(RECT, 20, 20, 80, 80)``) as shown in the above example.
        When a shape is created with ``begin_shape()`` and ``end_shape()``, its
        attributes may be changed with ``fill()`` and ``stroke()`` within
        ``begin_shape()`` and ``end_shape()``. However, after the shape is created, only
        the ``set_stroke()`` method can define a new stroke value for the ``Py5Shape``.
        """
        pass

    @_py5shape_type_fixer
    def set_stroke(self, *args):
        """The ``set_stroke()`` method defines the outline color of a ``Py5Shape``.

        Underlying Java method: PShape.setStroke

        Methods
        -------

        You can use any of the following signatures:

         * set_stroke(index: int, stroke: int, /) -> None
         * set_stroke(stroke: bool, /) -> None
         * set_stroke(stroke: int, /) -> None

        Parameters
        ----------

        index: int
            missing variable description

        stroke: bool
            missing variable description

        stroke: int
            missing variable description

        Notes
        -----

        The ``set_stroke()`` method defines the outline color of a ``Py5Shape``. This
        method is used after shapes are created or when a shape is defined explicitly
        (e.g. ``create_shape(RECT, 20, 20, 80, 80)``) as shown in the above example.
        When a shape is created with ``begin_shape()`` and ``end_shape()``, its
        attributes may be changed with ``fill()`` and ``stroke()`` within
        ``begin_shape()`` and ``end_shape()``. However, after the shape is created, only
        the ``set_stroke()`` method can define a new stroke value for the ``Py5Shape``.
        """
        return self._instance.setStroke(*args)

    def set_stroke_cap(self, cap: int, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.setStrokeCap

        Parameters
        ----------

        cap: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.setStrokeCap(cap)

    def set_stroke_join(self, join: int, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.setStrokeJoin

        Parameters
        ----------

        join: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.setStrokeJoin(join)

    @overload
    def set_stroke_weight(self, weight: float, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.setStrokeWeight

        Methods
        -------

        You can use any of the following signatures:

         * set_stroke_weight(index: int, weight: float, /) -> None
         * set_stroke_weight(weight: float, /) -> None

        Parameters
        ----------

        index: int
            missing variable description

        weight: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    @overload
    def set_stroke_weight(self, index: int, weight: float, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.setStrokeWeight

        Methods
        -------

        You can use any of the following signatures:

         * set_stroke_weight(index: int, weight: float, /) -> None
         * set_stroke_weight(weight: float, /) -> None

        Parameters
        ----------

        index: int
            missing variable description

        weight: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    def set_stroke_weight(self, *args):
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.setStrokeWeight

        Methods
        -------

        You can use any of the following signatures:

         * set_stroke_weight(index: int, weight: float, /) -> None
         * set_stroke_weight(weight: float, /) -> None

        Parameters
        ----------

        index: int
            missing variable description

        weight: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.setStrokeWeight(*args)

    def set_texture(self, tex: Py5Image, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.setTexture

        Parameters
        ----------

        tex: Py5Image
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.setTexture(tex)

    def set_texture_mode(self, mode: int, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.setTextureMode

        Parameters
        ----------

        mode: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.setTextureMode(mode)

    def set_texture_uv(self, index: int, u: float, v: float, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.setTextureUV

        Parameters
        ----------

        index: int
            missing variable description

        u: float
            missing variable description

        v: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.setTextureUV(index, u, v)

    @overload
    def set_tint(self, tint: bool, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.setTint

        Methods
        -------

        You can use any of the following signatures:

         * set_tint(fill: int, /) -> None
         * set_tint(index: int, tint: int, /) -> None
         * set_tint(tint: bool, /) -> None

        Parameters
        ----------

        fill: int
            missing variable description

        index: int
            missing variable description

        tint: bool
            missing variable description

        tint: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    @overload
    def set_tint(self, fill: int, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.setTint

        Methods
        -------

        You can use any of the following signatures:

         * set_tint(fill: int, /) -> None
         * set_tint(index: int, tint: int, /) -> None
         * set_tint(tint: bool, /) -> None

        Parameters
        ----------

        fill: int
            missing variable description

        index: int
            missing variable description

        tint: bool
            missing variable description

        tint: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    @overload
    def set_tint(self, index: int, tint: int, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.setTint

        Methods
        -------

        You can use any of the following signatures:

         * set_tint(fill: int, /) -> None
         * set_tint(index: int, tint: int, /) -> None
         * set_tint(tint: bool, /) -> None

        Parameters
        ----------

        fill: int
            missing variable description

        index: int
            missing variable description

        tint: bool
            missing variable description

        tint: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    @_py5shape_type_fixer
    def set_tint(self, *args):
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.setTint

        Methods
        -------

        You can use any of the following signatures:

         * set_tint(fill: int, /) -> None
         * set_tint(index: int, tint: int, /) -> None
         * set_tint(tint: bool, /) -> None

        Parameters
        ----------

        fill: int
            missing variable description

        index: int
            missing variable description

        tint: bool
            missing variable description

        tint: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.setTint(*args)

    @overload
    def set_vertex(self, index: int, x: float, y: float, /) -> None:
        """The ``set_vertex()`` method defines the coordinates of the vertex point located
        at the position defined by the ``index`` parameter.

        Underlying Java method: PShape.setVertex

        Methods
        -------

        You can use any of the following signatures:

         * set_vertex(index: int, vec: NDArray[(Any,), Float], /) -> None
         * set_vertex(index: int, x: float, y: float, /) -> None
         * set_vertex(index: int, x: float, y: float, z: float, /) -> None

        Parameters
        ----------

        index: int
            the location of the vertex

        vec: NDArray[(Any,), Float]
            the PVector to define the x, y, z coordinates

        x: float
            the x value for the vertex

        y: float
            the y value for the vertex

        z: float
            the z value for the vertex

        Notes
        -----

        The ``set_vertex()`` method defines the coordinates of the vertex point located
        at the position defined by the ``index`` parameter. This method works when
        shapes are created as shown in the example above, but won't work properly when a
        shape is defined explicitly (e.g. ``create_shape(RECT, 20, 20, 80, 80)``.
        """
        pass

    @overload
    def set_vertex(self, index: int, x: float, y: float, z: float, /) -> None:
        """The ``set_vertex()`` method defines the coordinates of the vertex point located
        at the position defined by the ``index`` parameter.

        Underlying Java method: PShape.setVertex

        Methods
        -------

        You can use any of the following signatures:

         * set_vertex(index: int, vec: NDArray[(Any,), Float], /) -> None
         * set_vertex(index: int, x: float, y: float, /) -> None
         * set_vertex(index: int, x: float, y: float, z: float, /) -> None

        Parameters
        ----------

        index: int
            the location of the vertex

        vec: NDArray[(Any,), Float]
            the PVector to define the x, y, z coordinates

        x: float
            the x value for the vertex

        y: float
            the y value for the vertex

        z: float
            the z value for the vertex

        Notes
        -----

        The ``set_vertex()`` method defines the coordinates of the vertex point located
        at the position defined by the ``index`` parameter. This method works when
        shapes are created as shown in the example above, but won't work properly when a
        shape is defined explicitly (e.g. ``create_shape(RECT, 20, 20, 80, 80)``.
        """
        pass

    @overload
    def set_vertex(self, index: int, vec: NDArray[(Any,), Float], /) -> None:
        """The ``set_vertex()`` method defines the coordinates of the vertex point located
        at the position defined by the ``index`` parameter.

        Underlying Java method: PShape.setVertex

        Methods
        -------

        You can use any of the following signatures:

         * set_vertex(index: int, vec: NDArray[(Any,), Float], /) -> None
         * set_vertex(index: int, x: float, y: float, /) -> None
         * set_vertex(index: int, x: float, y: float, z: float, /) -> None

        Parameters
        ----------

        index: int
            the location of the vertex

        vec: NDArray[(Any,), Float]
            the PVector to define the x, y, z coordinates

        x: float
            the x value for the vertex

        y: float
            the y value for the vertex

        z: float
            the z value for the vertex

        Notes
        -----

        The ``set_vertex()`` method defines the coordinates of the vertex point located
        at the position defined by the ``index`` parameter. This method works when
        shapes are created as shown in the example above, but won't work properly when a
        shape is defined explicitly (e.g. ``create_shape(RECT, 20, 20, 80, 80)``.
        """
        pass

    def set_vertex(self, *args):
        """The ``set_vertex()`` method defines the coordinates of the vertex point located
        at the position defined by the ``index`` parameter.

        Underlying Java method: PShape.setVertex

        Methods
        -------

        You can use any of the following signatures:

         * set_vertex(index: int, vec: NDArray[(Any,), Float], /) -> None
         * set_vertex(index: int, x: float, y: float, /) -> None
         * set_vertex(index: int, x: float, y: float, z: float, /) -> None

        Parameters
        ----------

        index: int
            the location of the vertex

        vec: NDArray[(Any,), Float]
            the PVector to define the x, y, z coordinates

        x: float
            the x value for the vertex

        y: float
            the y value for the vertex

        z: float
            the z value for the vertex

        Notes
        -----

        The ``set_vertex()`` method defines the coordinates of the vertex point located
        at the position defined by the ``index`` parameter. This method works when
        shapes are created as shown in the example above, but won't work properly when a
        shape is defined explicitly (e.g. ``create_shape(RECT, 20, 20, 80, 80)``.
        """
        return self._instance.setVertex(*args)

    def set_visible(self, visible: bool, /) -> None:
        """Sets the shape to be visible or invisible.

        Underlying Java method: PShape.setVisible

        Parameters
        ----------

        visible: bool
            "false" makes the shape invisible and "true" makes it visible

        Notes
        -----

        Sets the shape to be visible or invisible. This is determined by the value of
        the ``visible`` parameter.

        The default visibility of a shape is usually controlled by whatever program
        created the SVG file. For instance, this parameter is controlled by showing or
        hiding the shape in the layers palette in Adobe Illustrator.
        """
        return self._instance.setVisible(visible)

    def shininess(self, shine: float, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.shininess

        Parameters
        ----------

        shine: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.shininess(shine)

    @overload
    def specular(self, gray: float, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.specular

        Methods
        -------

        You can use any of the following signatures:

         * specular(gray: float, /) -> None
         * specular(rgb: int, /) -> None
         * specular(x: float, y: float, z: float, /) -> None

        Parameters
        ----------

        gray: float
            missing variable description

        rgb: int
            missing variable description

        x: float
            missing variable description

        y: float
            missing variable description

        z: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    @overload
    def specular(self, x: float, y: float, z: float, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.specular

        Methods
        -------

        You can use any of the following signatures:

         * specular(gray: float, /) -> None
         * specular(rgb: int, /) -> None
         * specular(x: float, y: float, z: float, /) -> None

        Parameters
        ----------

        gray: float
            missing variable description

        rgb: int
            missing variable description

        x: float
            missing variable description

        y: float
            missing variable description

        z: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    @overload
    def specular(self, rgb: int, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.specular

        Methods
        -------

        You can use any of the following signatures:

         * specular(gray: float, /) -> None
         * specular(rgb: int, /) -> None
         * specular(x: float, y: float, z: float, /) -> None

        Parameters
        ----------

        gray: float
            missing variable description

        rgb: int
            missing variable description

        x: float
            missing variable description

        y: float
            missing variable description

        z: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    def specular(self, *args):
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.specular

        Methods
        -------

        You can use any of the following signatures:

         * specular(gray: float, /) -> None
         * specular(rgb: int, /) -> None
         * specular(x: float, y: float, z: float, /) -> None

        Parameters
        ----------

        gray: float
            missing variable description

        rgb: int
            missing variable description

        x: float
            missing variable description

        y: float
            missing variable description

        z: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.specular(*args)

    @overload
    def stroke(self, gray: float, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.stroke

        Methods
        -------

        You can use any of the following signatures:

         * stroke(gray: float, /) -> None
         * stroke(gray: float, alpha: float, /) -> None
         * stroke(rgb: int, /) -> None
         * stroke(rgb: int, alpha: float, /) -> None
         * stroke(x: float, y: float, z: float, /) -> None
         * stroke(x: float, y: float, z: float, alpha: float, /) -> None

        Parameters
        ----------

        alpha: float
            missing variable description

        gray: float
            missing variable description

        rgb: int
            missing variable description

        x: float
            missing variable description

        y: float
            missing variable description

        z: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    @overload
    def stroke(self, gray: float, alpha: float, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.stroke

        Methods
        -------

        You can use any of the following signatures:

         * stroke(gray: float, /) -> None
         * stroke(gray: float, alpha: float, /) -> None
         * stroke(rgb: int, /) -> None
         * stroke(rgb: int, alpha: float, /) -> None
         * stroke(x: float, y: float, z: float, /) -> None
         * stroke(x: float, y: float, z: float, alpha: float, /) -> None

        Parameters
        ----------

        alpha: float
            missing variable description

        gray: float
            missing variable description

        rgb: int
            missing variable description

        x: float
            missing variable description

        y: float
            missing variable description

        z: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    @overload
    def stroke(self, x: float, y: float, z: float, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.stroke

        Methods
        -------

        You can use any of the following signatures:

         * stroke(gray: float, /) -> None
         * stroke(gray: float, alpha: float, /) -> None
         * stroke(rgb: int, /) -> None
         * stroke(rgb: int, alpha: float, /) -> None
         * stroke(x: float, y: float, z: float, /) -> None
         * stroke(x: float, y: float, z: float, alpha: float, /) -> None

        Parameters
        ----------

        alpha: float
            missing variable description

        gray: float
            missing variable description

        rgb: int
            missing variable description

        x: float
            missing variable description

        y: float
            missing variable description

        z: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    @overload
    def stroke(self, x: float, y: float, z: float, alpha: float, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.stroke

        Methods
        -------

        You can use any of the following signatures:

         * stroke(gray: float, /) -> None
         * stroke(gray: float, alpha: float, /) -> None
         * stroke(rgb: int, /) -> None
         * stroke(rgb: int, alpha: float, /) -> None
         * stroke(x: float, y: float, z: float, /) -> None
         * stroke(x: float, y: float, z: float, alpha: float, /) -> None

        Parameters
        ----------

        alpha: float
            missing variable description

        gray: float
            missing variable description

        rgb: int
            missing variable description

        x: float
            missing variable description

        y: float
            missing variable description

        z: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    @overload
    def stroke(self, rgb: int, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.stroke

        Methods
        -------

        You can use any of the following signatures:

         * stroke(gray: float, /) -> None
         * stroke(gray: float, alpha: float, /) -> None
         * stroke(rgb: int, /) -> None
         * stroke(rgb: int, alpha: float, /) -> None
         * stroke(x: float, y: float, z: float, /) -> None
         * stroke(x: float, y: float, z: float, alpha: float, /) -> None

        Parameters
        ----------

        alpha: float
            missing variable description

        gray: float
            missing variable description

        rgb: int
            missing variable description

        x: float
            missing variable description

        y: float
            missing variable description

        z: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    @overload
    def stroke(self, rgb: int, alpha: float, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.stroke

        Methods
        -------

        You can use any of the following signatures:

         * stroke(gray: float, /) -> None
         * stroke(gray: float, alpha: float, /) -> None
         * stroke(rgb: int, /) -> None
         * stroke(rgb: int, alpha: float, /) -> None
         * stroke(x: float, y: float, z: float, /) -> None
         * stroke(x: float, y: float, z: float, alpha: float, /) -> None

        Parameters
        ----------

        alpha: float
            missing variable description

        gray: float
            missing variable description

        rgb: int
            missing variable description

        x: float
            missing variable description

        y: float
            missing variable description

        z: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    def stroke(self, *args):
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.stroke

        Methods
        -------

        You can use any of the following signatures:

         * stroke(gray: float, /) -> None
         * stroke(gray: float, alpha: float, /) -> None
         * stroke(rgb: int, /) -> None
         * stroke(rgb: int, alpha: float, /) -> None
         * stroke(x: float, y: float, z: float, /) -> None
         * stroke(x: float, y: float, z: float, alpha: float, /) -> None

        Parameters
        ----------

        alpha: float
            missing variable description

        gray: float
            missing variable description

        rgb: int
            missing variable description

        x: float
            missing variable description

        y: float
            missing variable description

        z: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.stroke(*args)

    def stroke_cap(self, cap: int, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.strokeCap

        Parameters
        ----------

        cap: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.strokeCap(cap)

    def stroke_join(self, join: int, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.strokeJoin

        Parameters
        ----------

        join: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.strokeJoin(join)

    def stroke_weight(self, weight: float, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.strokeWeight

        Parameters
        ----------

        weight: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.strokeWeight(weight)

    def texture(self, tex: Py5Image, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.texture

        Parameters
        ----------

        tex: Py5Image
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.texture(tex)

    def texture_mode(self, mode: int, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.textureMode

        Parameters
        ----------

        mode: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.textureMode(mode)

    @overload
    def tint(self, gray: float, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.tint

        Methods
        -------

        You can use any of the following signatures:

         * tint(gray: float, /) -> None
         * tint(gray: float, alpha: float, /) -> None
         * tint(rgb: int, /) -> None
         * tint(rgb: int, alpha: float, /) -> None
         * tint(x: float, y: float, z: float, /) -> None
         * tint(x: float, y: float, z: float, alpha: float, /) -> None

        Parameters
        ----------

        alpha: float
            missing variable description

        gray: float
            missing variable description

        rgb: int
            missing variable description

        x: float
            missing variable description

        y: float
            missing variable description

        z: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    @overload
    def tint(self, gray: float, alpha: float, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.tint

        Methods
        -------

        You can use any of the following signatures:

         * tint(gray: float, /) -> None
         * tint(gray: float, alpha: float, /) -> None
         * tint(rgb: int, /) -> None
         * tint(rgb: int, alpha: float, /) -> None
         * tint(x: float, y: float, z: float, /) -> None
         * tint(x: float, y: float, z: float, alpha: float, /) -> None

        Parameters
        ----------

        alpha: float
            missing variable description

        gray: float
            missing variable description

        rgb: int
            missing variable description

        x: float
            missing variable description

        y: float
            missing variable description

        z: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    @overload
    def tint(self, x: float, y: float, z: float, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.tint

        Methods
        -------

        You can use any of the following signatures:

         * tint(gray: float, /) -> None
         * tint(gray: float, alpha: float, /) -> None
         * tint(rgb: int, /) -> None
         * tint(rgb: int, alpha: float, /) -> None
         * tint(x: float, y: float, z: float, /) -> None
         * tint(x: float, y: float, z: float, alpha: float, /) -> None

        Parameters
        ----------

        alpha: float
            missing variable description

        gray: float
            missing variable description

        rgb: int
            missing variable description

        x: float
            missing variable description

        y: float
            missing variable description

        z: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    @overload
    def tint(self, x: float, y: float, z: float, alpha: float, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.tint

        Methods
        -------

        You can use any of the following signatures:

         * tint(gray: float, /) -> None
         * tint(gray: float, alpha: float, /) -> None
         * tint(rgb: int, /) -> None
         * tint(rgb: int, alpha: float, /) -> None
         * tint(x: float, y: float, z: float, /) -> None
         * tint(x: float, y: float, z: float, alpha: float, /) -> None

        Parameters
        ----------

        alpha: float
            missing variable description

        gray: float
            missing variable description

        rgb: int
            missing variable description

        x: float
            missing variable description

        y: float
            missing variable description

        z: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    @overload
    def tint(self, rgb: int, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.tint

        Methods
        -------

        You can use any of the following signatures:

         * tint(gray: float, /) -> None
         * tint(gray: float, alpha: float, /) -> None
         * tint(rgb: int, /) -> None
         * tint(rgb: int, alpha: float, /) -> None
         * tint(x: float, y: float, z: float, /) -> None
         * tint(x: float, y: float, z: float, alpha: float, /) -> None

        Parameters
        ----------

        alpha: float
            missing variable description

        gray: float
            missing variable description

        rgb: int
            missing variable description

        x: float
            missing variable description

        y: float
            missing variable description

        z: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    @overload
    def tint(self, rgb: int, alpha: float, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.tint

        Methods
        -------

        You can use any of the following signatures:

         * tint(gray: float, /) -> None
         * tint(gray: float, alpha: float, /) -> None
         * tint(rgb: int, /) -> None
         * tint(rgb: int, alpha: float, /) -> None
         * tint(x: float, y: float, z: float, /) -> None
         * tint(x: float, y: float, z: float, alpha: float, /) -> None

        Parameters
        ----------

        alpha: float
            missing variable description

        gray: float
            missing variable description

        rgb: int
            missing variable description

        x: float
            missing variable description

        y: float
            missing variable description

        z: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    def tint(self, *args):
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.tint

        Methods
        -------

        You can use any of the following signatures:

         * tint(gray: float, /) -> None
         * tint(gray: float, alpha: float, /) -> None
         * tint(rgb: int, /) -> None
         * tint(rgb: int, alpha: float, /) -> None
         * tint(x: float, y: float, z: float, /) -> None
         * tint(x: float, y: float, z: float, alpha: float, /) -> None

        Parameters
        ----------

        alpha: float
            missing variable description

        gray: float
            missing variable description

        rgb: int
            missing variable description

        x: float
            missing variable description

        y: float
            missing variable description

        z: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.tint(*args)

    @overload
    def translate(self, x: float, y: float, /) -> None:
        """Specifies an amount to displace the shape.

        Underlying Java method: PShape.translate

        Methods
        -------

        You can use any of the following signatures:

         * translate(x: float, y: float, /) -> None
         * translate(x: float, y: float, z: float, /) -> None

        Parameters
        ----------

        x: float
            left/right translation

        y: float
            up/down translation

        z: float
            forward/back translation

        Notes
        -----

        Specifies an amount to displace the shape. The ``x`` parameter specifies
        left/right translation, the ``y`` parameter specifies up/down translation, and
        the ``z`` parameter specifies translations toward/away from the screen.
        Subsequent calls to the method accumulates the effect. For example, calling
        ``translate(50, 0)`` and then ``translate(20, 0)`` is the same as
        ``translate(70, 0)``. This transformation is applied directly to the shape, it's
        not refreshed each time ``draw()`` is run.

        Using this method with the ``z`` parameter requires using the P3D parameter in
        combination with size.
        """
        pass

    @overload
    def translate(self, x: float, y: float, z: float, /) -> None:
        """Specifies an amount to displace the shape.

        Underlying Java method: PShape.translate

        Methods
        -------

        You can use any of the following signatures:

         * translate(x: float, y: float, /) -> None
         * translate(x: float, y: float, z: float, /) -> None

        Parameters
        ----------

        x: float
            left/right translation

        y: float
            up/down translation

        z: float
            forward/back translation

        Notes
        -----

        Specifies an amount to displace the shape. The ``x`` parameter specifies
        left/right translation, the ``y`` parameter specifies up/down translation, and
        the ``z`` parameter specifies translations toward/away from the screen.
        Subsequent calls to the method accumulates the effect. For example, calling
        ``translate(50, 0)`` and then ``translate(20, 0)`` is the same as
        ``translate(70, 0)``. This transformation is applied directly to the shape, it's
        not refreshed each time ``draw()`` is run.

        Using this method with the ``z`` parameter requires using the P3D parameter in
        combination with size.
        """
        pass

    def translate(self, *args):
        """Specifies an amount to displace the shape.

        Underlying Java method: PShape.translate

        Methods
        -------

        You can use any of the following signatures:

         * translate(x: float, y: float, /) -> None
         * translate(x: float, y: float, z: float, /) -> None

        Parameters
        ----------

        x: float
            left/right translation

        y: float
            up/down translation

        z: float
            forward/back translation

        Notes
        -----

        Specifies an amount to displace the shape. The ``x`` parameter specifies
        left/right translation, the ``y`` parameter specifies up/down translation, and
        the ``z`` parameter specifies translations toward/away from the screen.
        Subsequent calls to the method accumulates the effect. For example, calling
        ``translate(50, 0)`` and then ``translate(20, 0)`` is the same as
        ``translate(70, 0)``. This transformation is applied directly to the shape, it's
        not refreshed each time ``draw()`` is run.

        Using this method with the ``z`` parameter requires using the P3D parameter in
        combination with size.
        """
        return self._instance.translate(*args)

    @overload
    def vertex(self, x: float, y: float, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.vertex

        Methods
        -------

        You can use any of the following signatures:

         * vertex(x: float, y: float, /) -> None
         * vertex(x: float, y: float, u: float, v: float, /) -> None
         * vertex(x: float, y: float, z: float, /) -> None
         * vertex(x: float, y: float, z: float, u: float, v: float, /) -> None

        Parameters
        ----------

        u: float
            missing variable description

        v: float
            missing variable description

        x: float
            missing variable description

        y: float
            missing variable description

        z: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    @overload
    def vertex(self, x: float, y: float, z: float, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.vertex

        Methods
        -------

        You can use any of the following signatures:

         * vertex(x: float, y: float, /) -> None
         * vertex(x: float, y: float, u: float, v: float, /) -> None
         * vertex(x: float, y: float, z: float, /) -> None
         * vertex(x: float, y: float, z: float, u: float, v: float, /) -> None

        Parameters
        ----------

        u: float
            missing variable description

        v: float
            missing variable description

        x: float
            missing variable description

        y: float
            missing variable description

        z: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    @overload
    def vertex(self, x: float, y: float, u: float, v: float, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.vertex

        Methods
        -------

        You can use any of the following signatures:

         * vertex(x: float, y: float, /) -> None
         * vertex(x: float, y: float, u: float, v: float, /) -> None
         * vertex(x: float, y: float, z: float, /) -> None
         * vertex(x: float, y: float, z: float, u: float, v: float, /) -> None

        Parameters
        ----------

        u: float
            missing variable description

        v: float
            missing variable description

        x: float
            missing variable description

        y: float
            missing variable description

        z: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    @overload
    def vertex(self, x: float, y: float, z: float,
               u: float, v: float, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.vertex

        Methods
        -------

        You can use any of the following signatures:

         * vertex(x: float, y: float, /) -> None
         * vertex(x: float, y: float, u: float, v: float, /) -> None
         * vertex(x: float, y: float, z: float, /) -> None
         * vertex(x: float, y: float, z: float, u: float, v: float, /) -> None

        Parameters
        ----------

        u: float
            missing variable description

        v: float
            missing variable description

        x: float
            missing variable description

        y: float
            missing variable description

        z: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    def vertex(self, *args):
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PShape.vertex

        Methods
        -------

        You can use any of the following signatures:

         * vertex(x: float, y: float, /) -> None
         * vertex(x: float, y: float, u: float, v: float, /) -> None
         * vertex(x: float, y: float, z: float, /) -> None
         * vertex(x: float, y: float, z: float, u: float, v: float, /) -> None

        Parameters
        ----------

        u: float
            missing variable description

        v: float
            missing variable description

        x: float
            missing variable description

        y: float
            missing variable description

        z: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.vertex(*args)
