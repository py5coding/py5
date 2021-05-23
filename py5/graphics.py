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
from typing import overload, List  # noqa
from nptyping import NDArray, Float  # noqa

import numpy as np  # noqa

from jpype import JClass

from .base import Py5Base
from .mixins import PixelMixin
from .font import Py5Font  # noqa
from .shader import Py5Shader, _return_py5shader, _load_py5shader  # noqa
from .shape import Py5Shape, _return_py5shape, _load_py5shape  # noqa
from .image import Py5Image, _return_py5image  # noqa
from .type_decorators import _text_fix_str  # noqa
from .pmath import _get_matrix_wrapper  # noqa


def _return_py5graphics(f):
    @functools.wraps(f)
    def decorated(self_, *args):
        ret = f(self_, *args)
        if ret is not None:
            return Py5Graphics(ret)
    return decorated


_Py5GraphicsHelper = JClass('py5.core.Py5GraphicsHelper')


class Py5Graphics(PixelMixin, Py5Base):
    """Main graphics and rendering context, as well as the base ``API`` implementation
    for processing "core".

    Underlying Java class: PGraphics.PGraphics

    Notes
    -----

    Main graphics and rendering context, as well as the base ``API`` implementation
    for processing "core". Use this class if you need to draw into an off-screen
    graphics buffer. A Py5Graphics object can be constructed with the
    ``create_graphics()`` function. The ``Py5Graphics.begin_draw()`` and
    ``Py5Graphics.end_draw()`` methods (see example) are necessary to set up the
    buffer and to finalize it. The fields and methods for this class are extensive.

    To create a new graphics context, use the ``create_graphics()`` function. Do not
    use the syntax ``Py5Graphics()``.
    """

    def __init__(self, pgraphics):
        self._instance = pgraphics
        super().__init__(instance=pgraphics)

    def points(self, coordinates):
        _Py5GraphicsHelper.points(self._instance, coordinates)

    def lines(self, coordinates):
        _Py5GraphicsHelper.lines(self._instance, coordinates)

    def vertices(self, coordinates):
        _Py5GraphicsHelper.vertices(self._instance, coordinates)

    def bezier_vertices(self, coordinates):
        _Py5GraphicsHelper.bezierVertices(self._instance, coordinates)

    def curve_vertices(self, coordinates):
        _Py5GraphicsHelper.curveVertices(self._instance, coordinates)

    def quadratic_vertices(self, coordinates):
        _Py5GraphicsHelper.quadraticVertices(self._instance, coordinates)

    ADD = 2
    ALPHA = 4
    ALPHA_MASK = -16777216
    ALT = 18
    AMBIENT = 0
    ARC = 32
    ARGB = 2
    ARROW = 0
    BACKSPACE = '\b'
    BASELINE = 0
    BEVEL = 32
    BEZIER_VERTEX = 1
    BLEND = 1
    BLUE_MASK = 255
    BLUR = 11
    BOTTOM = 102
    BOX = 41
    BREAK = 4
    BURN = 8192
    CENTER = 3
    CHATTER = 0
    CHORD = 2
    CLAMP = 0
    CLOSE = 2
    CODED = '\uffff'
    COMPLAINT = 1
    CONTROL = 17
    CORNER = 0
    CORNERS = 1
    CROSS = 1
    CURVE_VERTEX = 3
    CUSTOM = 0
    DARKEST = 16
    DEG_TO_RAD = 0.017453292
    DELETE = '\u007f'
    DIAMETER = 3
    DIFFERENCE = 32
    DILATE = 18
    DIRECTIONAL = 1
    DISABLE_ASYNC_SAVEFRAME = 12
    DISABLE_BUFFER_READING = -10
    DISABLE_DEPTH_MASK = 5
    DISABLE_DEPTH_SORT = -3
    DISABLE_DEPTH_TEST = 2
    DISABLE_KEY_REPEAT = 11
    DISABLE_NATIVE_FONTS = -1
    DISABLE_OPENGL_ERRORS = 4
    DISABLE_OPTIMIZED_STROKE = 6
    DISABLE_STROKE_PERSPECTIVE = -7
    DISABLE_STROKE_PURE = -9
    DISABLE_TEXTURE_MIPMAPS = 8
    DODGE = 4096
    DOWN = 40
    DXF = "processing.dxf.RawDXF"
    ELLIPSE = 31
    ENABLE_ASYNC_SAVEFRAME = -12
    ENABLE_BUFFER_READING = 10
    ENABLE_DEPTH_MASK = -5
    ENABLE_DEPTH_SORT = 3
    ENABLE_DEPTH_TEST = -2
    ENABLE_KEY_REPEAT = -11
    ENABLE_NATIVE_FONTS = 1
    ENABLE_OPENGL_ERRORS = -4
    ENABLE_OPTIMIZED_STROKE = -6
    ENABLE_STROKE_PERSPECTIVE = 7
    ENABLE_STROKE_PURE = 9
    ENABLE_TEXTURE_MIPMAPS = -8
    ENTER = '\n'
    EPSILON = 1.0E-4
    ERODE = 17
    ESC = '\u001b'
    EXCLUSION = 64
    FX2D = "processing.javafx.PGraphicsFX2D"
    GIF = 3
    GRAY = 12
    GREEN_MASK = 65280
    GROUP = 0
    HALF_PI = 1.5707964
    HAND = 12
    HARD_LIGHT = 1024
    HINT_COUNT = 13
    HSB = 3
    IMAGE = 2
    INVERT = 13
    JAVA2D = "processing.awt.PGraphicsJava2D"
    JPEG = 2
    LANDSCAPE = 2
    LEFT = 37
    LIGHTEST = 8
    LINE = 4
    LINES = 5
    LINE_LOOP = 51
    LINE_STRIP = 50
    LINUX = 3
    MACOS = 2
    MAX_FLOAT = 3.4028235E38
    MAX_INT = 2147483647
    MIN_FLOAT = -3.4028235E38
    MIN_INT = -2147483648
    MITER = 8
    MODEL = 4
    MODELVIEW = 1
    MOVE = 13
    MULTIPLY = 128
    NORMAL = 1
    OPAQUE = 14
    OPEN = 1
    OPENGL = "processing.opengl.PGraphics3D"
    ORTHOGRAPHIC = 2
    OTHER = 0
    OVERLAY = 512
    P2D = "processing.opengl.PGraphics2D"
    P3D = "processing.opengl.PGraphics3D"
    PATH = 21
    PDF = "processing.pdf.PGraphicsPDF"
    PERSPECTIVE = 3
    PI = 3.1415927
    PIE = 3
    POINT = 2
    POINTS = 3
    POLYGON = 20
    PORTRAIT = 1
    POSTERIZE = 15
    PROBLEM = 2
    PROJECT = 4
    PROJECTION = 0
    QUAD = 16
    QUADRATIC_VERTEX = 2
    QUADS = 17
    QUAD_BEZIER_VERTEX = 2
    QUAD_STRIP = 18
    QUARTER_PI = 0.7853982
    RADIUS = 2
    RAD_TO_DEG = 57.295776
    RECT = 30
    RED_MASK = 16711680
    REPEAT = 1
    REPLACE = 0
    RETURN = '\r'
    RGB = 1
    RIGHT = 39
    ROUND = 2
    SCREEN = 256
    SHAPE = 5
    SHIFT = 16
    SOFT_LIGHT = 2048
    SPAN = 0
    SPHERE = 40
    SPOT = 3
    SQUARE = 1
    SUBTRACT = 4
    SVG = "processing.svg.PGraphicsSVG"
    TAB = '\t'
    TARGA = 1
    TAU = 6.2831855
    TEXT = 2
    THIRD_PI = 1.0471976
    THRESHOLD = 16
    TIFF = 0
    TOP = 101
    TRIANGLE = 8
    TRIANGLES = 9
    TRIANGLE_FAN = 11
    TRIANGLE_STRIP = 10
    TWO_PI = 6.2831855
    UP = 38
    VERTEX = 0
    WAIT = 3
    WHITESPACE = " \t\n\r\f\u00a0"
    WINDOWS = 1
    X = 0
    Y = 1
    Z = 2

    def _get_height(self) -> int:
        """System variable that stores the height of the Py5Graphics drawing surface.

        Underlying Java field: PGraphics.height

        Notes
        -----

        System variable that stores the height of the Py5Graphics drawing surface. This
        value is set when creating the ``Py5Graphics`` object with the
        ``create_graphics()`` method. For example, ``create_graphics(320, 240)`` sets
        the ``height`` variable to the value 240.

        This field is the same as ``height`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``height``.
        """
        return self._instance.height
    height: int = property(fget=_get_height)

    def _get_pixel_density(self) -> int:
        """Get the pixel density of the Py5Graphics drawing surface.

        Underlying Java field: PGraphics.pixelDensity

        Notes
        -----

        Get the pixel density of the Py5Graphics drawing surface. By default this is 1
        but it can be changed by calling ``pixel_density()`` in ``settings()``.

        When the pixel density has been set to more than 1, it changes all of the pixel
        operations including the way ``Py5Graphics.get()``, ``Py5Graphics.blend()``,
        ``Py5Graphics.copy()``, ``Py5Graphics.update_pixels()``, and
        ``Py5Graphics.update_np_pixels()`` all work. See the reference for
        ``Py5Graphics.pixel_width`` and ``Py5Graphics.pixel_height`` for more
        information.
        """
        return self._instance.pixelDensity
    pixel_density: int = property(fget=_get_pixel_density)

    def _get_pixel_height(self) -> int:
        """When ``pixel_density(2)`` was used in ``settings()`` to make use of a high
        resolution display (called a Retina display on OSX or high-dpi on Windows and
        Linux), the width and height of the Py5Graphics drawing surface does not change,
        but the number of pixels is doubled.

        Underlying Java field: PGraphics.pixelHeight

        Notes
        -----

        When ``pixel_density(2)`` was used in ``settings()`` to make use of a high
        resolution display (called a Retina display on OSX or high-dpi on Windows and
        Linux), the width and height of the Py5Graphics drawing surface does not change,
        but the number of pixels is doubled. As a result, all operations that use pixels
        (like ``Py5Graphics.load_pixels()``, ``Py5Graphics.get()``, etc.) happen in this
        doubled space. As a convenience, the variables ``Py5Graphics.pixel_width`` and
        ``pixel_height`` hold the actual width and height of the drawing surface in
        pixels. This is useful for any Py5Graphics objects that use the
        ``Py5Graphics.pixels[]`` or ``Py5Graphics.np_pixels[]`` arrays, for instance,
        because the number of elements in each array will be
        ``pixel_width*pixel_height``, not ``width*height``.

        This field is the same as ``pixel_height`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``pixel_height``.
        """
        return self._instance.pixelHeight
    pixel_height: int = property(fget=_get_pixel_height)

    def _get_pixel_width(self) -> int:
        """When ``pixel_density(2)`` was used in ``settings()`` to make use of a high
        resolution display (called a Retina display on OSX or high-dpi on Windows and
        Linux), the width and height of the Py5Graphics drawing surface does not change,
        but the number of pixels is doubled.

        Underlying Java field: PGraphics.pixelWidth

        Notes
        -----

        When ``pixel_density(2)`` was used in ``settings()`` to make use of a high
        resolution display (called a Retina display on OSX or high-dpi on Windows and
        Linux), the width and height of the Py5Graphics drawing surface does not change,
        but the number of pixels is doubled. As a result, all operations that use pixels
        (like ``Py5Graphics.load_pixels()``, ``Py5Graphics.get()``, etc.) happen in this
        doubled space. As a convenience, the variables ``pixel_width`` and
        ``Py5Graphics.pixel_height`` hold the actual width and height of the drawing
        surface in pixels. This is useful for any Py5Graphics objects that use the
        ``Py5Graphics.pixels[]`` or ``Py5Graphics.np_pixels[]`` arrays, for instance,
        because the number of elements in each array will be
        ``pixel_width*pixel_height``, not ``width*height``.

        This field is the same as ``pixel_width`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``pixel_width``.
        """
        return self._instance.pixelWidth
    pixel_width: int = property(fget=_get_pixel_width)

    def _get_pixels(self) -> NDArray[(Any,), Int]:
        """The ``pixels[]`` array contains the values for all the pixels in the Py5Graphics
        drawing surface.

        Underlying Java field: PGraphics.pixels

        Notes
        -----

        The ``pixels[]`` array contains the values for all the pixels in the Py5Graphics
        drawing surface. These values are of the color datatype. This array is defined
        by the size of the Py5Graphics drawing surface. For example, if the drawing
        surface is 100 x 100 pixels, there will be 10,000 values and if the drawing
        surface is 200 x 300 pixels, there will be 60,000 values. When the pixel density
        is set to higher than 1 with the ``Py5Graphics.pixel_density`` function, these
        values will change. See the reference for ``Py5Graphics.pixel_width`` or
        ``Py5Graphics.pixel_height`` for more information.

        Before accessing this array, the data must loaded with the
        ``Py5Graphics.load_pixels()`` function. Failure to do so may result in a Java
        ``NullPointerException``. Subsequent changes to the Py5Graphics drawing surface
        will not be reflected in ``pixels`` until ``Py5Graphics.load_pixels()`` is
        called again. After ``pixels`` has been modified, the
        ``Py5Graphics.update_pixels()`` function must be run to update the content of
        the Py5Graphics drawing surface.

        This field is the same as ``pixels[]`` but linked to a ``Py5Graphics`` object.
        """
        return self._instance.pixels
    pixels: NDArray[(Any,), Int] = property(fget=_get_pixels)

    def _get_width(self) -> int:
        """System variable that stores the width of the Py5Graphics drawing surface.

        Underlying Java field: PGraphics.width

        Notes
        -----

        System variable that stores the width of the Py5Graphics drawing surface. This
        value is set when creating the ``Py5Graphics`` object with the
        ``create_graphics()`` method. For example, ``create_graphics(320, 240)`` sets
        the ``width`` variable to the value 320.

        This field is the same as ``width`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``width``.
        """
        return self._instance.width
    width: int = property(fget=_get_width)

    def alpha(self, rgb: int, /) -> float:
        """Extracts the alpha value from a color, scaled to match current
        ``Py5Graphics.color_mode()``.

        Underlying Java method: PGraphics.alpha

        Parameters
        ----------

        rgb: int
            any value of the color datatype

        Notes
        -----

        Extracts the alpha value from a color, scaled to match current
        ``Py5Graphics.color_mode()``.

        The ``alpha()`` function is easy to use and understand, but it is slower than a
        technique called bit shifting. When working in ``color_mode(RGB, 255)``, you can
        achieve the same results as ``alpha()`` but with greater speed by using the
        right shift operator (``>>``) with a bit mask. For example, ``alpha(c)`` and ``c
        >> 24 & 0xFF`` both extract the alpha value from a color variable ``c`` but the
        later is faster.

        This method is the same as ``alpha()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``alpha()``.
        """
        return self._instance.alpha(rgb)

    @overload
    def ambient(self, gray: float, /) -> None:
        """Sets the ambient reflectance for shapes drawn to the screen.

        Underlying Java method: PGraphics.ambient

        Methods
        -------

        You can use any of the following signatures:

         * ambient(gray: float, /) -> None
         * ambient(rgb: int, /) -> None
         * ambient(v1: float, v2: float, v3: float, /) -> None

        Parameters
        ----------

        gray: float
            number specifying value between white and black

        rgb: int
            any value of the color datatype

        v1: float
            red or hue value (depending on current color mode)

        v2: float
            green or saturation value (depending on current color mode)

        v3: float
            blue or brightness value (depending on current color mode)

        Notes
        -----

        Sets the ambient reflectance for shapes drawn to the screen. This is combined
        with the ambient light component of the environment. The color components set
        through the parameters define the reflectance. For example in the default color
        mode, setting ``ambient(255, 127, 0)``, would cause all the red light to reflect
        and half of the green light to reflect. Use in combination with
        ``Py5Graphics.emissive()``, ``Py5Graphics.specular()``, and
        ``Py5Graphics.shininess()`` to set the material properties of shapes.

        This method is the same as ``ambient()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``ambient()``.
        """
        pass

    @overload
    def ambient(self, v1: float, v2: float, v3: float, /) -> None:
        """Sets the ambient reflectance for shapes drawn to the screen.

        Underlying Java method: PGraphics.ambient

        Methods
        -------

        You can use any of the following signatures:

         * ambient(gray: float, /) -> None
         * ambient(rgb: int, /) -> None
         * ambient(v1: float, v2: float, v3: float, /) -> None

        Parameters
        ----------

        gray: float
            number specifying value between white and black

        rgb: int
            any value of the color datatype

        v1: float
            red or hue value (depending on current color mode)

        v2: float
            green or saturation value (depending on current color mode)

        v3: float
            blue or brightness value (depending on current color mode)

        Notes
        -----

        Sets the ambient reflectance for shapes drawn to the screen. This is combined
        with the ambient light component of the environment. The color components set
        through the parameters define the reflectance. For example in the default color
        mode, setting ``ambient(255, 127, 0)``, would cause all the red light to reflect
        and half of the green light to reflect. Use in combination with
        ``Py5Graphics.emissive()``, ``Py5Graphics.specular()``, and
        ``Py5Graphics.shininess()`` to set the material properties of shapes.

        This method is the same as ``ambient()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``ambient()``.
        """
        pass

    @overload
    def ambient(self, rgb: int, /) -> None:
        """Sets the ambient reflectance for shapes drawn to the screen.

        Underlying Java method: PGraphics.ambient

        Methods
        -------

        You can use any of the following signatures:

         * ambient(gray: float, /) -> None
         * ambient(rgb: int, /) -> None
         * ambient(v1: float, v2: float, v3: float, /) -> None

        Parameters
        ----------

        gray: float
            number specifying value between white and black

        rgb: int
            any value of the color datatype

        v1: float
            red or hue value (depending on current color mode)

        v2: float
            green or saturation value (depending on current color mode)

        v3: float
            blue or brightness value (depending on current color mode)

        Notes
        -----

        Sets the ambient reflectance for shapes drawn to the screen. This is combined
        with the ambient light component of the environment. The color components set
        through the parameters define the reflectance. For example in the default color
        mode, setting ``ambient(255, 127, 0)``, would cause all the red light to reflect
        and half of the green light to reflect. Use in combination with
        ``Py5Graphics.emissive()``, ``Py5Graphics.specular()``, and
        ``Py5Graphics.shininess()`` to set the material properties of shapes.

        This method is the same as ``ambient()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``ambient()``.
        """
        pass

    def ambient(self, *args):
        """Sets the ambient reflectance for shapes drawn to the screen.

        Underlying Java method: PGraphics.ambient

        Methods
        -------

        You can use any of the following signatures:

         * ambient(gray: float, /) -> None
         * ambient(rgb: int, /) -> None
         * ambient(v1: float, v2: float, v3: float, /) -> None

        Parameters
        ----------

        gray: float
            number specifying value between white and black

        rgb: int
            any value of the color datatype

        v1: float
            red or hue value (depending on current color mode)

        v2: float
            green or saturation value (depending on current color mode)

        v3: float
            blue or brightness value (depending on current color mode)

        Notes
        -----

        Sets the ambient reflectance for shapes drawn to the screen. This is combined
        with the ambient light component of the environment. The color components set
        through the parameters define the reflectance. For example in the default color
        mode, setting ``ambient(255, 127, 0)``, would cause all the red light to reflect
        and half of the green light to reflect. Use in combination with
        ``Py5Graphics.emissive()``, ``Py5Graphics.specular()``, and
        ``Py5Graphics.shininess()`` to set the material properties of shapes.

        This method is the same as ``ambient()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``ambient()``.
        """
        return self._instance.ambient(*args)

    @overload
    def ambient_light(self, v1: float, v2: float, v3: float, /) -> None:
        """Adds an ambient light.

        Underlying Java method: PGraphics.ambientLight

        Methods
        -------

        You can use any of the following signatures:

         * ambient_light(v1: float, v2: float, v3: float, /) -> None
         * ambient_light(v1: float, v2: float, v3: float, x: float, y: float, z: float, /) -> None

        Parameters
        ----------

        v1: float
            red or hue value (depending on current color mode)

        v2: float
            green or saturation value (depending on current color mode)

        v3: float
            blue or brightness value (depending on current color mode)

        x: float
            x-coordinate of the light

        y: float
            y-coordinate of the light

        z: float
            z-coordinate of the light

        Notes
        -----

        Adds an ambient light. Ambient light doesn't come from a specific direction, the
        rays of light have bounced around so much that objects are evenly lit from all
        sides. Ambient lights are almost always used in combination with other types of
        lights. The ``v1``, ``v2``, and ``v3`` parameters are interpreted as either
        ``RGB`` or ``HSB`` values, depending on the current color mode.

        This method is the same as ``ambient_light()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``ambient_light()``.
        """
        pass

    @overload
    def ambient_light(self, v1: float, v2: float, v3: float,
                      x: float, y: float, z: float, /) -> None:
        """Adds an ambient light.

        Underlying Java method: PGraphics.ambientLight

        Methods
        -------

        You can use any of the following signatures:

         * ambient_light(v1: float, v2: float, v3: float, /) -> None
         * ambient_light(v1: float, v2: float, v3: float, x: float, y: float, z: float, /) -> None

        Parameters
        ----------

        v1: float
            red or hue value (depending on current color mode)

        v2: float
            green or saturation value (depending on current color mode)

        v3: float
            blue or brightness value (depending on current color mode)

        x: float
            x-coordinate of the light

        y: float
            y-coordinate of the light

        z: float
            z-coordinate of the light

        Notes
        -----

        Adds an ambient light. Ambient light doesn't come from a specific direction, the
        rays of light have bounced around so much that objects are evenly lit from all
        sides. Ambient lights are almost always used in combination with other types of
        lights. The ``v1``, ``v2``, and ``v3`` parameters are interpreted as either
        ``RGB`` or ``HSB`` values, depending on the current color mode.

        This method is the same as ``ambient_light()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``ambient_light()``.
        """
        pass

    def ambient_light(self, *args):
        """Adds an ambient light.

        Underlying Java method: PGraphics.ambientLight

        Methods
        -------

        You can use any of the following signatures:

         * ambient_light(v1: float, v2: float, v3: float, /) -> None
         * ambient_light(v1: float, v2: float, v3: float, x: float, y: float, z: float, /) -> None

        Parameters
        ----------

        v1: float
            red or hue value (depending on current color mode)

        v2: float
            green or saturation value (depending on current color mode)

        v3: float
            blue or brightness value (depending on current color mode)

        x: float
            x-coordinate of the light

        y: float
            y-coordinate of the light

        z: float
            z-coordinate of the light

        Notes
        -----

        Adds an ambient light. Ambient light doesn't come from a specific direction, the
        rays of light have bounced around so much that objects are evenly lit from all
        sides. Ambient lights are almost always used in combination with other types of
        lights. The ``v1``, ``v2``, and ``v3`` parameters are interpreted as either
        ``RGB`` or ``HSB`` values, depending on the current color mode.

        This method is the same as ``ambient_light()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``ambient_light()``.
        """
        return self._instance.ambientLight(*args)

    @overload
    def apply_matrix(self, n00: float, n01: float, n02: float,
                     n10: float, n11: float, n12: float, /) -> None:
        """Multiplies the current matrix by the one specified through the parameters.

        Underlying Java method: PGraphics.applyMatrix

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
            numbers which define the 4x4 matrix to be multiplied

        n01: float
            numbers which define the 4x4 matrix to be multiplied

        n02: float
            numbers which define the 4x4 matrix to be multiplied

        n03: float
            numbers which define the 4x4 matrix to be multiplied

        n10: float
            numbers which define the 4x4 matrix to be multiplied

        n11: float
            numbers which define the 4x4 matrix to be multiplied

        n12: float
            numbers which define the 4x4 matrix to be multiplied

        n13: float
            numbers which define the 4x4 matrix to be multiplied

        n20: float
            numbers which define the 4x4 matrix to be multiplied

        n21: float
            numbers which define the 4x4 matrix to be multiplied

        n22: float
            numbers which define the 4x4 matrix to be multiplied

        n23: float
            numbers which define the 4x4 matrix to be multiplied

        n30: float
            numbers which define the 4x4 matrix to be multiplied

        n31: float
            numbers which define the 4x4 matrix to be multiplied

        n32: float
            numbers which define the 4x4 matrix to be multiplied

        n33: float
            numbers which define the 4x4 matrix to be multiplied

        source: NDArray[(2, 3), Float]
            2D transformation matrix

        source: NDArray[(4, 4), Float]
            3D transformation matrix

        Notes
        -----

        Multiplies the current matrix by the one specified through the parameters. This
        is very slow because it will try to calculate the inverse of the transform, so
        avoid it whenever possible. The equivalent function in OpenGL is
        ``gl_mult_matrix()``.

        This method is the same as ``apply_matrix()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``apply_matrix()``.
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
        """Multiplies the current matrix by the one specified through the parameters.

        Underlying Java method: PGraphics.applyMatrix

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
            numbers which define the 4x4 matrix to be multiplied

        n01: float
            numbers which define the 4x4 matrix to be multiplied

        n02: float
            numbers which define the 4x4 matrix to be multiplied

        n03: float
            numbers which define the 4x4 matrix to be multiplied

        n10: float
            numbers which define the 4x4 matrix to be multiplied

        n11: float
            numbers which define the 4x4 matrix to be multiplied

        n12: float
            numbers which define the 4x4 matrix to be multiplied

        n13: float
            numbers which define the 4x4 matrix to be multiplied

        n20: float
            numbers which define the 4x4 matrix to be multiplied

        n21: float
            numbers which define the 4x4 matrix to be multiplied

        n22: float
            numbers which define the 4x4 matrix to be multiplied

        n23: float
            numbers which define the 4x4 matrix to be multiplied

        n30: float
            numbers which define the 4x4 matrix to be multiplied

        n31: float
            numbers which define the 4x4 matrix to be multiplied

        n32: float
            numbers which define the 4x4 matrix to be multiplied

        n33: float
            numbers which define the 4x4 matrix to be multiplied

        source: NDArray[(2, 3), Float]
            2D transformation matrix

        source: NDArray[(4, 4), Float]
            3D transformation matrix

        Notes
        -----

        Multiplies the current matrix by the one specified through the parameters. This
        is very slow because it will try to calculate the inverse of the transform, so
        avoid it whenever possible. The equivalent function in OpenGL is
        ``gl_mult_matrix()``.

        This method is the same as ``apply_matrix()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``apply_matrix()``.
        """
        pass

    @overload
    def apply_matrix(self, source: NDArray[(2, 3), Float], /) -> None:
        """Multiplies the current matrix by the one specified through the parameters.

        Underlying Java method: PGraphics.applyMatrix

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
            numbers which define the 4x4 matrix to be multiplied

        n01: float
            numbers which define the 4x4 matrix to be multiplied

        n02: float
            numbers which define the 4x4 matrix to be multiplied

        n03: float
            numbers which define the 4x4 matrix to be multiplied

        n10: float
            numbers which define the 4x4 matrix to be multiplied

        n11: float
            numbers which define the 4x4 matrix to be multiplied

        n12: float
            numbers which define the 4x4 matrix to be multiplied

        n13: float
            numbers which define the 4x4 matrix to be multiplied

        n20: float
            numbers which define the 4x4 matrix to be multiplied

        n21: float
            numbers which define the 4x4 matrix to be multiplied

        n22: float
            numbers which define the 4x4 matrix to be multiplied

        n23: float
            numbers which define the 4x4 matrix to be multiplied

        n30: float
            numbers which define the 4x4 matrix to be multiplied

        n31: float
            numbers which define the 4x4 matrix to be multiplied

        n32: float
            numbers which define the 4x4 matrix to be multiplied

        n33: float
            numbers which define the 4x4 matrix to be multiplied

        source: NDArray[(2, 3), Float]
            2D transformation matrix

        source: NDArray[(4, 4), Float]
            3D transformation matrix

        Notes
        -----

        Multiplies the current matrix by the one specified through the parameters. This
        is very slow because it will try to calculate the inverse of the transform, so
        avoid it whenever possible. The equivalent function in OpenGL is
        ``gl_mult_matrix()``.

        This method is the same as ``apply_matrix()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``apply_matrix()``.
        """
        pass

    @overload
    def apply_matrix(self, source: NDArray[(4, 4), Float], /) -> None:
        """Multiplies the current matrix by the one specified through the parameters.

        Underlying Java method: PGraphics.applyMatrix

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
            numbers which define the 4x4 matrix to be multiplied

        n01: float
            numbers which define the 4x4 matrix to be multiplied

        n02: float
            numbers which define the 4x4 matrix to be multiplied

        n03: float
            numbers which define the 4x4 matrix to be multiplied

        n10: float
            numbers which define the 4x4 matrix to be multiplied

        n11: float
            numbers which define the 4x4 matrix to be multiplied

        n12: float
            numbers which define the 4x4 matrix to be multiplied

        n13: float
            numbers which define the 4x4 matrix to be multiplied

        n20: float
            numbers which define the 4x4 matrix to be multiplied

        n21: float
            numbers which define the 4x4 matrix to be multiplied

        n22: float
            numbers which define the 4x4 matrix to be multiplied

        n23: float
            numbers which define the 4x4 matrix to be multiplied

        n30: float
            numbers which define the 4x4 matrix to be multiplied

        n31: float
            numbers which define the 4x4 matrix to be multiplied

        n32: float
            numbers which define the 4x4 matrix to be multiplied

        n33: float
            numbers which define the 4x4 matrix to be multiplied

        source: NDArray[(2, 3), Float]
            2D transformation matrix

        source: NDArray[(4, 4), Float]
            3D transformation matrix

        Notes
        -----

        Multiplies the current matrix by the one specified through the parameters. This
        is very slow because it will try to calculate the inverse of the transform, so
        avoid it whenever possible. The equivalent function in OpenGL is
        ``gl_mult_matrix()``.

        This method is the same as ``apply_matrix()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``apply_matrix()``.
        """
        pass

    def apply_matrix(self, *args):
        """Multiplies the current matrix by the one specified through the parameters.

        Underlying Java method: PGraphics.applyMatrix

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
            numbers which define the 4x4 matrix to be multiplied

        n01: float
            numbers which define the 4x4 matrix to be multiplied

        n02: float
            numbers which define the 4x4 matrix to be multiplied

        n03: float
            numbers which define the 4x4 matrix to be multiplied

        n10: float
            numbers which define the 4x4 matrix to be multiplied

        n11: float
            numbers which define the 4x4 matrix to be multiplied

        n12: float
            numbers which define the 4x4 matrix to be multiplied

        n13: float
            numbers which define the 4x4 matrix to be multiplied

        n20: float
            numbers which define the 4x4 matrix to be multiplied

        n21: float
            numbers which define the 4x4 matrix to be multiplied

        n22: float
            numbers which define the 4x4 matrix to be multiplied

        n23: float
            numbers which define the 4x4 matrix to be multiplied

        n30: float
            numbers which define the 4x4 matrix to be multiplied

        n31: float
            numbers which define the 4x4 matrix to be multiplied

        n32: float
            numbers which define the 4x4 matrix to be multiplied

        n33: float
            numbers which define the 4x4 matrix to be multiplied

        source: NDArray[(2, 3), Float]
            2D transformation matrix

        source: NDArray[(4, 4), Float]
            3D transformation matrix

        Notes
        -----

        Multiplies the current matrix by the one specified through the parameters. This
        is very slow because it will try to calculate the inverse of the transform, so
        avoid it whenever possible. The equivalent function in OpenGL is
        ``gl_mult_matrix()``.

        This method is the same as ``apply_matrix()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``apply_matrix()``.
        """
        return self._instance.applyMatrix(*args)

    @overload
    def arc(self, a: float, b: float, c: float, d: float,
            start: float, stop: float, /) -> None:
        """Draws an arc to the screen.

        Underlying Java method: PGraphics.arc

        Methods
        -------

        You can use any of the following signatures:

         * arc(a: float, b: float, c: float, d: float, start: float, stop: float, /) -> None
         * arc(a: float, b: float, c: float, d: float, start: float, stop: float, mode: int, /) -> None

        Parameters
        ----------

        a: float
            x-coordinate of the arc's ellipse

        b: float
            y-coordinate of the arc's ellipse

        c: float
            width of the arc's ellipse by default

        d: float
            height of the arc's ellipse by default

        mode: int
            arc drawing mode

        start: float
            angle to start the arc, specified in radians

        stop: float
            angle to stop the arc, specified in radians

        Notes
        -----

        Draws an arc to the screen. Arcs are drawn along the outer edge of an ellipse
        defined by the ``a``, ``b``, ``c``, and ``d`` parameters. The origin of the
        arc's ellipse may be changed with the ``Py5Graphics.ellipse_mode()`` function.
        Use the ``start`` and ``stop`` parameters to specify the angles (in radians) at
        which to draw the arc. The start/stop values must be in clockwise order.

        There are three ways to draw an arc; the rendering technique used is defined by
        the optional seventh parameter. The three options, depicted in the examples, are
        ``PIE``, ``OPEN``, and ``CHORD``. The default mode is the ``OPEN`` stroke with a
        ``PIE`` fill.

        In some cases, the ``arc()`` function isn't accurate enough for smooth drawing.
        For example, the shape may jitter on screen when rotating slowly. If you're
        having an issue with how arcs are rendered, you'll need to draw the arc yourself
        with ``Py5Graphics.begin_shape()`` & ``Py5Graphics.end_shape()`` or a
        ``Py5Shape``.

        This method is the same as ``arc()`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``arc()``.
        """
        pass

    @overload
    def arc(self, a: float, b: float, c: float, d: float,
            start: float, stop: float, mode: int, /) -> None:
        """Draws an arc to the screen.

        Underlying Java method: PGraphics.arc

        Methods
        -------

        You can use any of the following signatures:

         * arc(a: float, b: float, c: float, d: float, start: float, stop: float, /) -> None
         * arc(a: float, b: float, c: float, d: float, start: float, stop: float, mode: int, /) -> None

        Parameters
        ----------

        a: float
            x-coordinate of the arc's ellipse

        b: float
            y-coordinate of the arc's ellipse

        c: float
            width of the arc's ellipse by default

        d: float
            height of the arc's ellipse by default

        mode: int
            arc drawing mode

        start: float
            angle to start the arc, specified in radians

        stop: float
            angle to stop the arc, specified in radians

        Notes
        -----

        Draws an arc to the screen. Arcs are drawn along the outer edge of an ellipse
        defined by the ``a``, ``b``, ``c``, and ``d`` parameters. The origin of the
        arc's ellipse may be changed with the ``Py5Graphics.ellipse_mode()`` function.
        Use the ``start`` and ``stop`` parameters to specify the angles (in radians) at
        which to draw the arc. The start/stop values must be in clockwise order.

        There are three ways to draw an arc; the rendering technique used is defined by
        the optional seventh parameter. The three options, depicted in the examples, are
        ``PIE``, ``OPEN``, and ``CHORD``. The default mode is the ``OPEN`` stroke with a
        ``PIE`` fill.

        In some cases, the ``arc()`` function isn't accurate enough for smooth drawing.
        For example, the shape may jitter on screen when rotating slowly. If you're
        having an issue with how arcs are rendered, you'll need to draw the arc yourself
        with ``Py5Graphics.begin_shape()`` & ``Py5Graphics.end_shape()`` or a
        ``Py5Shape``.

        This method is the same as ``arc()`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``arc()``.
        """
        pass

    def arc(self, *args):
        """Draws an arc to the screen.

        Underlying Java method: PGraphics.arc

        Methods
        -------

        You can use any of the following signatures:

         * arc(a: float, b: float, c: float, d: float, start: float, stop: float, /) -> None
         * arc(a: float, b: float, c: float, d: float, start: float, stop: float, mode: int, /) -> None

        Parameters
        ----------

        a: float
            x-coordinate of the arc's ellipse

        b: float
            y-coordinate of the arc's ellipse

        c: float
            width of the arc's ellipse by default

        d: float
            height of the arc's ellipse by default

        mode: int
            arc drawing mode

        start: float
            angle to start the arc, specified in radians

        stop: float
            angle to stop the arc, specified in radians

        Notes
        -----

        Draws an arc to the screen. Arcs are drawn along the outer edge of an ellipse
        defined by the ``a``, ``b``, ``c``, and ``d`` parameters. The origin of the
        arc's ellipse may be changed with the ``Py5Graphics.ellipse_mode()`` function.
        Use the ``start`` and ``stop`` parameters to specify the angles (in radians) at
        which to draw the arc. The start/stop values must be in clockwise order.

        There are three ways to draw an arc; the rendering technique used is defined by
        the optional seventh parameter. The three options, depicted in the examples, are
        ``PIE``, ``OPEN``, and ``CHORD``. The default mode is the ``OPEN`` stroke with a
        ``PIE`` fill.

        In some cases, the ``arc()`` function isn't accurate enough for smooth drawing.
        For example, the shape may jitter on screen when rotating slowly. If you're
        having an issue with how arcs are rendered, you'll need to draw the arc yourself
        with ``Py5Graphics.begin_shape()`` & ``Py5Graphics.end_shape()`` or a
        ``Py5Shape``.

        This method is the same as ``arc()`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``arc()``.
        """
        return self._instance.arc(*args)

    @overload
    def background(self, gray: float, /) -> None:
        """The ``background()`` function sets the color used for the background of the
        ``Py5Graphics`` object.

        Underlying Java method: PGraphics.background

        Methods
        -------

        You can use any of the following signatures:

         * background(gray: float, /) -> None
         * background(gray: float, alpha: float, /) -> None
         * background(image: Py5Image, /) -> None
         * background(rgb: int, /) -> None
         * background(rgb: int, alpha: float, /) -> None
         * background(v1: float, v2: float, v3: float, /) -> None
         * background(v1: float, v2: float, v3: float, alpha: float, /) -> None

        Parameters
        ----------

        alpha: float
            opacity of the background

        gray: float
            specifies a value between white and black

        image: Py5Image
            Py5Image to set as background (must be same size as the Sketch window)

        rgb: int
            any value of the color datatype

        v1: float
            red or hue value (depending on the current color mode)

        v2: float
            green or saturation value (depending on the current color mode)

        v3: float
            blue or brightness value (depending on the current color mode)

        Notes
        -----

        The ``background()`` function sets the color used for the background of the
        ``Py5Graphics`` object. The default background is 100% transparent.

        An image can also be used as the background, although the image's width and
        height must match that of the ``Py5Graphics`` object. Images used with
        ``background()`` will ignore the current ``Py5Graphics.tint()`` setting. To
        resize an image to the size of the ``Py5Graphics`` object, use
        ``image.resize(width, height)``.

        This method is the same as ``background()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``background()``.
        """
        pass

    @overload
    def background(self, gray: float, alpha: float, /) -> None:
        """The ``background()`` function sets the color used for the background of the
        ``Py5Graphics`` object.

        Underlying Java method: PGraphics.background

        Methods
        -------

        You can use any of the following signatures:

         * background(gray: float, /) -> None
         * background(gray: float, alpha: float, /) -> None
         * background(image: Py5Image, /) -> None
         * background(rgb: int, /) -> None
         * background(rgb: int, alpha: float, /) -> None
         * background(v1: float, v2: float, v3: float, /) -> None
         * background(v1: float, v2: float, v3: float, alpha: float, /) -> None

        Parameters
        ----------

        alpha: float
            opacity of the background

        gray: float
            specifies a value between white and black

        image: Py5Image
            Py5Image to set as background (must be same size as the Sketch window)

        rgb: int
            any value of the color datatype

        v1: float
            red or hue value (depending on the current color mode)

        v2: float
            green or saturation value (depending on the current color mode)

        v3: float
            blue or brightness value (depending on the current color mode)

        Notes
        -----

        The ``background()`` function sets the color used for the background of the
        ``Py5Graphics`` object. The default background is 100% transparent.

        An image can also be used as the background, although the image's width and
        height must match that of the ``Py5Graphics`` object. Images used with
        ``background()`` will ignore the current ``Py5Graphics.tint()`` setting. To
        resize an image to the size of the ``Py5Graphics`` object, use
        ``image.resize(width, height)``.

        This method is the same as ``background()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``background()``.
        """
        pass

    @overload
    def background(self, v1: float, v2: float, v3: float, /) -> None:
        """The ``background()`` function sets the color used for the background of the
        ``Py5Graphics`` object.

        Underlying Java method: PGraphics.background

        Methods
        -------

        You can use any of the following signatures:

         * background(gray: float, /) -> None
         * background(gray: float, alpha: float, /) -> None
         * background(image: Py5Image, /) -> None
         * background(rgb: int, /) -> None
         * background(rgb: int, alpha: float, /) -> None
         * background(v1: float, v2: float, v3: float, /) -> None
         * background(v1: float, v2: float, v3: float, alpha: float, /) -> None

        Parameters
        ----------

        alpha: float
            opacity of the background

        gray: float
            specifies a value between white and black

        image: Py5Image
            Py5Image to set as background (must be same size as the Sketch window)

        rgb: int
            any value of the color datatype

        v1: float
            red or hue value (depending on the current color mode)

        v2: float
            green or saturation value (depending on the current color mode)

        v3: float
            blue or brightness value (depending on the current color mode)

        Notes
        -----

        The ``background()`` function sets the color used for the background of the
        ``Py5Graphics`` object. The default background is 100% transparent.

        An image can also be used as the background, although the image's width and
        height must match that of the ``Py5Graphics`` object. Images used with
        ``background()`` will ignore the current ``Py5Graphics.tint()`` setting. To
        resize an image to the size of the ``Py5Graphics`` object, use
        ``image.resize(width, height)``.

        This method is the same as ``background()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``background()``.
        """
        pass

    @overload
    def background(self, v1: float, v2: float,
                   v3: float, alpha: float, /) -> None:
        """The ``background()`` function sets the color used for the background of the
        ``Py5Graphics`` object.

        Underlying Java method: PGraphics.background

        Methods
        -------

        You can use any of the following signatures:

         * background(gray: float, /) -> None
         * background(gray: float, alpha: float, /) -> None
         * background(image: Py5Image, /) -> None
         * background(rgb: int, /) -> None
         * background(rgb: int, alpha: float, /) -> None
         * background(v1: float, v2: float, v3: float, /) -> None
         * background(v1: float, v2: float, v3: float, alpha: float, /) -> None

        Parameters
        ----------

        alpha: float
            opacity of the background

        gray: float
            specifies a value between white and black

        image: Py5Image
            Py5Image to set as background (must be same size as the Sketch window)

        rgb: int
            any value of the color datatype

        v1: float
            red or hue value (depending on the current color mode)

        v2: float
            green or saturation value (depending on the current color mode)

        v3: float
            blue or brightness value (depending on the current color mode)

        Notes
        -----

        The ``background()`` function sets the color used for the background of the
        ``Py5Graphics`` object. The default background is 100% transparent.

        An image can also be used as the background, although the image's width and
        height must match that of the ``Py5Graphics`` object. Images used with
        ``background()`` will ignore the current ``Py5Graphics.tint()`` setting. To
        resize an image to the size of the ``Py5Graphics`` object, use
        ``image.resize(width, height)``.

        This method is the same as ``background()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``background()``.
        """
        pass

    @overload
    def background(self, rgb: int, /) -> None:
        """The ``background()`` function sets the color used for the background of the
        ``Py5Graphics`` object.

        Underlying Java method: PGraphics.background

        Methods
        -------

        You can use any of the following signatures:

         * background(gray: float, /) -> None
         * background(gray: float, alpha: float, /) -> None
         * background(image: Py5Image, /) -> None
         * background(rgb: int, /) -> None
         * background(rgb: int, alpha: float, /) -> None
         * background(v1: float, v2: float, v3: float, /) -> None
         * background(v1: float, v2: float, v3: float, alpha: float, /) -> None

        Parameters
        ----------

        alpha: float
            opacity of the background

        gray: float
            specifies a value between white and black

        image: Py5Image
            Py5Image to set as background (must be same size as the Sketch window)

        rgb: int
            any value of the color datatype

        v1: float
            red or hue value (depending on the current color mode)

        v2: float
            green or saturation value (depending on the current color mode)

        v3: float
            blue or brightness value (depending on the current color mode)

        Notes
        -----

        The ``background()`` function sets the color used for the background of the
        ``Py5Graphics`` object. The default background is 100% transparent.

        An image can also be used as the background, although the image's width and
        height must match that of the ``Py5Graphics`` object. Images used with
        ``background()`` will ignore the current ``Py5Graphics.tint()`` setting. To
        resize an image to the size of the ``Py5Graphics`` object, use
        ``image.resize(width, height)``.

        This method is the same as ``background()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``background()``.
        """
        pass

    @overload
    def background(self, rgb: int, alpha: float, /) -> None:
        """The ``background()`` function sets the color used for the background of the
        ``Py5Graphics`` object.

        Underlying Java method: PGraphics.background

        Methods
        -------

        You can use any of the following signatures:

         * background(gray: float, /) -> None
         * background(gray: float, alpha: float, /) -> None
         * background(image: Py5Image, /) -> None
         * background(rgb: int, /) -> None
         * background(rgb: int, alpha: float, /) -> None
         * background(v1: float, v2: float, v3: float, /) -> None
         * background(v1: float, v2: float, v3: float, alpha: float, /) -> None

        Parameters
        ----------

        alpha: float
            opacity of the background

        gray: float
            specifies a value between white and black

        image: Py5Image
            Py5Image to set as background (must be same size as the Sketch window)

        rgb: int
            any value of the color datatype

        v1: float
            red or hue value (depending on the current color mode)

        v2: float
            green or saturation value (depending on the current color mode)

        v3: float
            blue or brightness value (depending on the current color mode)

        Notes
        -----

        The ``background()`` function sets the color used for the background of the
        ``Py5Graphics`` object. The default background is 100% transparent.

        An image can also be used as the background, although the image's width and
        height must match that of the ``Py5Graphics`` object. Images used with
        ``background()`` will ignore the current ``Py5Graphics.tint()`` setting. To
        resize an image to the size of the ``Py5Graphics`` object, use
        ``image.resize(width, height)``.

        This method is the same as ``background()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``background()``.
        """
        pass

    @overload
    def background(self, image: Py5Image, /) -> None:
        """The ``background()`` function sets the color used for the background of the
        ``Py5Graphics`` object.

        Underlying Java method: PGraphics.background

        Methods
        -------

        You can use any of the following signatures:

         * background(gray: float, /) -> None
         * background(gray: float, alpha: float, /) -> None
         * background(image: Py5Image, /) -> None
         * background(rgb: int, /) -> None
         * background(rgb: int, alpha: float, /) -> None
         * background(v1: float, v2: float, v3: float, /) -> None
         * background(v1: float, v2: float, v3: float, alpha: float, /) -> None

        Parameters
        ----------

        alpha: float
            opacity of the background

        gray: float
            specifies a value between white and black

        image: Py5Image
            Py5Image to set as background (must be same size as the Sketch window)

        rgb: int
            any value of the color datatype

        v1: float
            red or hue value (depending on the current color mode)

        v2: float
            green or saturation value (depending on the current color mode)

        v3: float
            blue or brightness value (depending on the current color mode)

        Notes
        -----

        The ``background()`` function sets the color used for the background of the
        ``Py5Graphics`` object. The default background is 100% transparent.

        An image can also be used as the background, although the image's width and
        height must match that of the ``Py5Graphics`` object. Images used with
        ``background()`` will ignore the current ``Py5Graphics.tint()`` setting. To
        resize an image to the size of the ``Py5Graphics`` object, use
        ``image.resize(width, height)``.

        This method is the same as ``background()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``background()``.
        """
        pass

    def background(self, *args):
        """The ``background()`` function sets the color used for the background of the
        ``Py5Graphics`` object.

        Underlying Java method: PGraphics.background

        Methods
        -------

        You can use any of the following signatures:

         * background(gray: float, /) -> None
         * background(gray: float, alpha: float, /) -> None
         * background(image: Py5Image, /) -> None
         * background(rgb: int, /) -> None
         * background(rgb: int, alpha: float, /) -> None
         * background(v1: float, v2: float, v3: float, /) -> None
         * background(v1: float, v2: float, v3: float, alpha: float, /) -> None

        Parameters
        ----------

        alpha: float
            opacity of the background

        gray: float
            specifies a value between white and black

        image: Py5Image
            Py5Image to set as background (must be same size as the Sketch window)

        rgb: int
            any value of the color datatype

        v1: float
            red or hue value (depending on the current color mode)

        v2: float
            green or saturation value (depending on the current color mode)

        v3: float
            blue or brightness value (depending on the current color mode)

        Notes
        -----

        The ``background()`` function sets the color used for the background of the
        ``Py5Graphics`` object. The default background is 100% transparent.

        An image can also be used as the background, although the image's width and
        height must match that of the ``Py5Graphics`` object. Images used with
        ``background()`` will ignore the current ``Py5Graphics.tint()`` setting. To
        resize an image to the size of the ``Py5Graphics`` object, use
        ``image.resize(width, height)``.

        This method is the same as ``background()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``background()``.
        """
        return self._instance.background(*args)

    def begin_camera(self) -> None:
        """The ``begin_camera()`` and ``Py5Graphics.end_camera()`` functions enable
        advanced customization of the camera space.

        Underlying Java method: PGraphics.beginCamera

        Notes
        -----

        The ``begin_camera()`` and ``Py5Graphics.end_camera()`` functions enable
        advanced customization of the camera space. The functions are useful if you want
        to more control over camera movement, however for most users, the
        ``Py5Graphics.camera()`` function will be sufficient. The camera functions will
        replace any transformations (such as ``Py5Graphics.rotate()`` or
        ``Py5Graphics.translate()``) that occur before them, but they will not
        automatically replace the camera transform itself. For this reason, camera
        functions should be placed right after the call to ``Py5Graphics.begin_draw()``
        (so that transformations happen afterwards), and the ``Py5Graphics.camera()``
        function can be used after ``begin_camera()`` if you want to reset the camera
        before applying transformations.

        This function sets the matrix mode to the camera matrix so calls such as
        ``Py5Graphics.translate()``, ``Py5Graphics.rotate()``,
        ``Py5Graphics.apply_matrix()`` and ``Py5Graphics.reset_matrix()`` affect the
        camera. ``begin_camera()`` should always be used with a following
        ``Py5Graphics.end_camera()`` and pairs of ``begin_camera()`` and
        ``Py5Graphics.end_camera()`` cannot be nested.

        This method is the same as ``begin_camera()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``begin_camera()``.
        """
        return self._instance.beginCamera()

    def begin_contour(self) -> None:
        """Use the ``begin_contour()`` and ``Py5Graphics.end_contour()`` methods to create
        negative shapes within shapes such as the center of the letter 'O'.

        Underlying Java method: PGraphics.beginContour

        Notes
        -----

        Use the ``begin_contour()`` and ``Py5Graphics.end_contour()`` methods to create
        negative shapes within shapes such as the center of the letter 'O'. The
        ``begin_contour()`` method begins recording vertices for the shape and
        ``Py5Graphics.end_contour()`` stops recording. The vertices that define a
        negative shape must "wind" in the opposite direction from the exterior shape.
        First draw vertices for the exterior shape in clockwise order, then for internal
        shapes, draw vertices counterclockwise.

        These methods can only be used within a ``Py5Graphics.begin_shape()`` &
        ``Py5Graphics.end_shape()`` pair and transformations such as
        ``Py5Graphics.translate()``, ``Py5Graphics.rotate()``, and
        ``Py5Graphics.scale()`` do not work within a ``begin_contour()`` &
        ``Py5Graphics.end_contour()`` pair. It is also not possible to use other shapes,
        such as ``Py5Graphics.ellipse()`` or ``Py5Graphics.rect()`` within.

        This method is the same as ``begin_contour()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``begin_contour()``.
        """
        return self._instance.beginContour()

    def begin_draw(self) -> None:
        """Sets the default properties for a ``Py5Graphics`` object.

        Underlying Java method: PGraphics.beginDraw

        Notes
        -----

        Sets the default properties for a ``Py5Graphics`` object. It should be called
        before anything is drawn into the object.
        """
        return self._instance.beginDraw()

    def begin_raw(self, raw_graphics: Py5Graphics, /) -> None:
        """To create vectors from 3D data, use the ``begin_raw()`` and
        ``Py5Graphics.end_raw()`` commands.

        Underlying Java method: PGraphics.beginRaw

        Parameters
        ----------

        raw_graphics: Py5Graphics
            Py5Graphics object to apply draw commands to

        Notes
        -----

        To create vectors from 3D data, use the ``begin_raw()`` and
        ``Py5Graphics.end_raw()`` commands. These commands will grab the shape data just
        before it is rendered to the ``Py5Graphics`` object. At this stage, the
        ``Py5Graphics`` object contains nothing but a long list of individual lines and
        triangles. This means that a shape created with ``Py5Graphics.sphere()``
        function will be made up of hundreds of triangles, rather than a single object.
        Or that a multi-segment line shape (such as a curve) will be rendered as
        individual segments.

        When using ``begin_raw()`` and ``Py5Graphics.end_raw()``, it's possible to write
        to either a 2D or 3D renderer. For instance, ``begin_raw()`` with the ``PDF``
        library will write the geometry as flattened triangles and lines, even if
        recording from the ``P3D`` renderer.

        If you want a background to show up in your files, use ``rect(0, 0, width,
        height)`` after setting the ``Py5Graphics.fill()`` to the background color.
        Otherwise the background will not be rendered to the file because the background
        is not shape.

        Using ``hint(ENABLE_DEPTH_SORT)`` can improve the appearance of 3D geometry
        drawn to 2D file formats.

        This method is the same as ``begin_raw()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``begin_raw()``.
        """
        return self._instance.beginRaw(raw_graphics)

    @overload
    def begin_shape(self) -> None:
        """Using the ``begin_shape()`` and ``Py5Graphics.end_shape()`` functions allow
        creating more complex forms.

        Underlying Java method: PGraphics.beginShape

        Methods
        -------

        You can use any of the following signatures:

         * begin_shape() -> None
         * begin_shape(kind: int, /) -> None

        Parameters
        ----------

        kind: int
            Either POINTS, LINES, TRIANGLES, TRIANGLE_FAN, TRIANGLE_STRIP, QUADS, or QUAD_STRIP

        Notes
        -----

        Using the ``begin_shape()`` and ``Py5Graphics.end_shape()`` functions allow
        creating more complex forms. ``begin_shape()`` begins recording vertices for a
        shape and ``Py5Graphics.end_shape()`` stops recording. The value of the ``kind``
        parameter tells it which types of shapes to create from the provided vertices.
        With no mode specified, the shape can be any irregular polygon. The parameters
        available for ``begin_shape()`` are ``POINTS``, ``LINES``, ``TRIANGLES``,
        ``TRIANGLE_FAN``, ``TRIANGLE_STRIP``, ``QUADS``, and ``QUAD_STRIP``. After
        calling the ``begin_shape()`` function, a series of ``Py5Graphics.vertex()``
        commands must follow. To stop drawing the shape, call
        ``Py5Graphics.end_shape()``. The ``Py5Graphics.vertex()`` function with two
        parameters specifies a position in 2D and the ``Py5Graphics.vertex()`` function
        with three parameters specifies a position in 3D. Each shape will be outlined
        with the current stroke color and filled with the fill color.

        Transformations such as ``Py5Graphics.translate()``, ``Py5Graphics.rotate()``,
        and ``Py5Graphics.scale()`` do not work within ``begin_shape()``. It is also not
        possible to use other shapes, such as ``Py5Graphics.ellipse()`` or
        ``Py5Graphics.rect()`` within ``begin_shape()``.

        The ``P2D`` and ``P3D`` renderers allow ``Py5Graphics.stroke()`` and
        ``Py5Graphics.fill()`` to be altered on a per-vertex basis, but the default
        renderer does not. Settings such as ``Py5Graphics.stroke_weight()``,
        ``Py5Graphics.stroke_cap()``, and ``Py5Graphics.stroke_join()`` cannot be
        changed while inside a ``begin_shape()`` & ``Py5Graphics.end_shape()`` block
        with any renderer.

        This method is the same as ``begin_shape()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``begin_shape()``.
        """
        pass

    @overload
    def begin_shape(self, kind: int, /) -> None:
        """Using the ``begin_shape()`` and ``Py5Graphics.end_shape()`` functions allow
        creating more complex forms.

        Underlying Java method: PGraphics.beginShape

        Methods
        -------

        You can use any of the following signatures:

         * begin_shape() -> None
         * begin_shape(kind: int, /) -> None

        Parameters
        ----------

        kind: int
            Either POINTS, LINES, TRIANGLES, TRIANGLE_FAN, TRIANGLE_STRIP, QUADS, or QUAD_STRIP

        Notes
        -----

        Using the ``begin_shape()`` and ``Py5Graphics.end_shape()`` functions allow
        creating more complex forms. ``begin_shape()`` begins recording vertices for a
        shape and ``Py5Graphics.end_shape()`` stops recording. The value of the ``kind``
        parameter tells it which types of shapes to create from the provided vertices.
        With no mode specified, the shape can be any irregular polygon. The parameters
        available for ``begin_shape()`` are ``POINTS``, ``LINES``, ``TRIANGLES``,
        ``TRIANGLE_FAN``, ``TRIANGLE_STRIP``, ``QUADS``, and ``QUAD_STRIP``. After
        calling the ``begin_shape()`` function, a series of ``Py5Graphics.vertex()``
        commands must follow. To stop drawing the shape, call
        ``Py5Graphics.end_shape()``. The ``Py5Graphics.vertex()`` function with two
        parameters specifies a position in 2D and the ``Py5Graphics.vertex()`` function
        with three parameters specifies a position in 3D. Each shape will be outlined
        with the current stroke color and filled with the fill color.

        Transformations such as ``Py5Graphics.translate()``, ``Py5Graphics.rotate()``,
        and ``Py5Graphics.scale()`` do not work within ``begin_shape()``. It is also not
        possible to use other shapes, such as ``Py5Graphics.ellipse()`` or
        ``Py5Graphics.rect()`` within ``begin_shape()``.

        The ``P2D`` and ``P3D`` renderers allow ``Py5Graphics.stroke()`` and
        ``Py5Graphics.fill()`` to be altered on a per-vertex basis, but the default
        renderer does not. Settings such as ``Py5Graphics.stroke_weight()``,
        ``Py5Graphics.stroke_cap()``, and ``Py5Graphics.stroke_join()`` cannot be
        changed while inside a ``begin_shape()`` & ``Py5Graphics.end_shape()`` block
        with any renderer.

        This method is the same as ``begin_shape()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``begin_shape()``.
        """
        pass

    def begin_shape(self, *args):
        """Using the ``begin_shape()`` and ``Py5Graphics.end_shape()`` functions allow
        creating more complex forms.

        Underlying Java method: PGraphics.beginShape

        Methods
        -------

        You can use any of the following signatures:

         * begin_shape() -> None
         * begin_shape(kind: int, /) -> None

        Parameters
        ----------

        kind: int
            Either POINTS, LINES, TRIANGLES, TRIANGLE_FAN, TRIANGLE_STRIP, QUADS, or QUAD_STRIP

        Notes
        -----

        Using the ``begin_shape()`` and ``Py5Graphics.end_shape()`` functions allow
        creating more complex forms. ``begin_shape()`` begins recording vertices for a
        shape and ``Py5Graphics.end_shape()`` stops recording. The value of the ``kind``
        parameter tells it which types of shapes to create from the provided vertices.
        With no mode specified, the shape can be any irregular polygon. The parameters
        available for ``begin_shape()`` are ``POINTS``, ``LINES``, ``TRIANGLES``,
        ``TRIANGLE_FAN``, ``TRIANGLE_STRIP``, ``QUADS``, and ``QUAD_STRIP``. After
        calling the ``begin_shape()`` function, a series of ``Py5Graphics.vertex()``
        commands must follow. To stop drawing the shape, call
        ``Py5Graphics.end_shape()``. The ``Py5Graphics.vertex()`` function with two
        parameters specifies a position in 2D and the ``Py5Graphics.vertex()`` function
        with three parameters specifies a position in 3D. Each shape will be outlined
        with the current stroke color and filled with the fill color.

        Transformations such as ``Py5Graphics.translate()``, ``Py5Graphics.rotate()``,
        and ``Py5Graphics.scale()`` do not work within ``begin_shape()``. It is also not
        possible to use other shapes, such as ``Py5Graphics.ellipse()`` or
        ``Py5Graphics.rect()`` within ``begin_shape()``.

        The ``P2D`` and ``P3D`` renderers allow ``Py5Graphics.stroke()`` and
        ``Py5Graphics.fill()`` to be altered on a per-vertex basis, but the default
        renderer does not. Settings such as ``Py5Graphics.stroke_weight()``,
        ``Py5Graphics.stroke_cap()``, and ``Py5Graphics.stroke_join()`` cannot be
        changed while inside a ``begin_shape()`` & ``Py5Graphics.end_shape()`` block
        with any renderer.

        This method is the same as ``begin_shape()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``begin_shape()``.
        """
        return self._instance.beginShape(*args)

    @overload
    def bezier(self, x1: float, y1: float, x2: float, y2: float,
               x3: float, y3: float, x4: float, y4: float, /) -> None:
        """Draws a Bezier curve on the ``Py5Graphics`` object.

        Underlying Java method: PGraphics.bezier

        Methods
        -------

        You can use any of the following signatures:

         * bezier(x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, /) -> None
         * bezier(x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, x3: float, y3: float, z3: float, x4: float, y4: float, z4: float, /) -> None

        Parameters
        ----------

        x1: float
            coordinates for the first anchor point

        x2: float
            coordinates for the first control point

        x3: float
            coordinates for the second control point

        x4: float
            coordinates for the second anchor point

        y1: float
            coordinates for the first anchor point

        y2: float
            coordinates for the first control point

        y3: float
            coordinates for the second control point

        y4: float
            coordinates for the second anchor point

        z1: float
            coordinates for the first anchor point

        z2: float
            coordinates for the first control point

        z3: float
            coordinates for the second control point

        z4: float
            coordinates for the second anchor point

        Notes
        -----

        Draws a Bezier curve on the ``Py5Graphics`` object. These curves are defined by
        a series of anchor and control points. The first two parameters specify the
        first anchor point and the last two parameters specify the other anchor point.
        The middle parameters specify the control points which define the shape of the
        curve. Bezier curves were developed by French engineer Pierre Bezier. Using the
        3D version requires rendering with ``P3D``.

        This method is the same as ``bezier()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``bezier()``.
        """
        pass

    @overload
    def bezier(self, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float,
               x3: float, y3: float, z3: float, x4: float, y4: float, z4: float, /) -> None:
        """Draws a Bezier curve on the ``Py5Graphics`` object.

        Underlying Java method: PGraphics.bezier

        Methods
        -------

        You can use any of the following signatures:

         * bezier(x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, /) -> None
         * bezier(x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, x3: float, y3: float, z3: float, x4: float, y4: float, z4: float, /) -> None

        Parameters
        ----------

        x1: float
            coordinates for the first anchor point

        x2: float
            coordinates for the first control point

        x3: float
            coordinates for the second control point

        x4: float
            coordinates for the second anchor point

        y1: float
            coordinates for the first anchor point

        y2: float
            coordinates for the first control point

        y3: float
            coordinates for the second control point

        y4: float
            coordinates for the second anchor point

        z1: float
            coordinates for the first anchor point

        z2: float
            coordinates for the first control point

        z3: float
            coordinates for the second control point

        z4: float
            coordinates for the second anchor point

        Notes
        -----

        Draws a Bezier curve on the ``Py5Graphics`` object. These curves are defined by
        a series of anchor and control points. The first two parameters specify the
        first anchor point and the last two parameters specify the other anchor point.
        The middle parameters specify the control points which define the shape of the
        curve. Bezier curves were developed by French engineer Pierre Bezier. Using the
        3D version requires rendering with ``P3D``.

        This method is the same as ``bezier()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``bezier()``.
        """
        pass

    def bezier(self, *args):
        """Draws a Bezier curve on the ``Py5Graphics`` object.

        Underlying Java method: PGraphics.bezier

        Methods
        -------

        You can use any of the following signatures:

         * bezier(x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, /) -> None
         * bezier(x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, x3: float, y3: float, z3: float, x4: float, y4: float, z4: float, /) -> None

        Parameters
        ----------

        x1: float
            coordinates for the first anchor point

        x2: float
            coordinates for the first control point

        x3: float
            coordinates for the second control point

        x4: float
            coordinates for the second anchor point

        y1: float
            coordinates for the first anchor point

        y2: float
            coordinates for the first control point

        y3: float
            coordinates for the second control point

        y4: float
            coordinates for the second anchor point

        z1: float
            coordinates for the first anchor point

        z2: float
            coordinates for the first control point

        z3: float
            coordinates for the second control point

        z4: float
            coordinates for the second anchor point

        Notes
        -----

        Draws a Bezier curve on the ``Py5Graphics`` object. These curves are defined by
        a series of anchor and control points. The first two parameters specify the
        first anchor point and the last two parameters specify the other anchor point.
        The middle parameters specify the control points which define the shape of the
        curve. Bezier curves were developed by French engineer Pierre Bezier. Using the
        3D version requires rendering with ``P3D``.

        This method is the same as ``bezier()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``bezier()``.
        """
        return self._instance.bezier(*args)

    def bezier_detail(self, detail: int, /) -> None:
        """Sets the resolution at which Beziers display.

        Underlying Java method: PGraphics.bezierDetail

        Parameters
        ----------

        detail: int
            resolution of the curves

        Notes
        -----

        Sets the resolution at which Beziers display. The default value is 20. This
        function is only useful when using the ``P3D`` renderer; the default ``P2D``
        renderer does not use this information.

        This method is the same as ``bezier_detail()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``bezier_detail()``.
        """
        return self._instance.bezierDetail(detail)

    def bezier_point(self, a: float, b: float, c: float,
                     d: float, t: float, /) -> float:
        """Evaluates the Bezier at point t for points a, b, c, d.

        Underlying Java method: PGraphics.bezierPoint

        Parameters
        ----------

        a: float
            coordinate of first point on the curve

        b: float
            coordinate of first control point

        c: float
            coordinate of second control point

        d: float
            coordinate of second point on the curve

        t: float
            value between 0 and 1

        Notes
        -----

        Evaluates the Bezier at point t for points a, b, c, d. The parameter t varies
        between 0 and 1, a and d are points on the curve, and b and c are the control
        points. This can be done once with the x coordinates and a second time with the
        y coordinates to get the location of a bezier curve at t.

        This method is the same as ``bezier_point()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``bezier_point()``.
        """
        return self._instance.bezierPoint(a, b, c, d, t)

    def bezier_tangent(self, a: float, b: float, c: float,
                       d: float, t: float, /) -> float:
        """Calculates the tangent of a point on a Bezier curve.

        Underlying Java method: PGraphics.bezierTangent

        Parameters
        ----------

        a: float
            coordinate of first point on the curve

        b: float
            coordinate of first control point

        c: float
            coordinate of second control point

        d: float
            coordinate of second point on the curve

        t: float
            value between 0 and 1

        Notes
        -----

        Calculates the tangent of a point on a Bezier curve. There is a good definition
        of *tangent* on Wikipedia.

        This method is the same as ``bezier_tangent()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``bezier_tangent()``.
        """
        return self._instance.bezierTangent(a, b, c, d, t)

    @overload
    def bezier_vertex(self, x2: float, y2: float, x3: float,
                      y3: float, x4: float, y4: float, /) -> None:
        """Specifies vertex coordinates for Bezier curves.

        Underlying Java method: PGraphics.bezierVertex

        Methods
        -------

        You can use any of the following signatures:

         * bezier_vertex(x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, /) -> None
         * bezier_vertex(x2: float, y2: float, z2: float, x3: float, y3: float, z3: float, x4: float, y4: float, z4: float, /) -> None

        Parameters
        ----------

        x2: float
            the x-coordinate of the 1st control point

        x3: float
            the x-coordinate of the 2nd control point

        x4: float
            the x-coordinate of the anchor point

        y2: float
            the y-coordinate of the 1st control point

        y3: float
            the y-coordinate of the 2nd control point

        y4: float
            the y-coordinate of the anchor point

        z2: float
            the z-coordinate of the 1st control point

        z3: float
            the z-coordinate of the 2nd control point

        z4: float
            the z-coordinate of the anchor point

        Notes
        -----

        Specifies vertex coordinates for Bezier curves. Each call to ``bezier_vertex()``
        defines the position of two control points and one anchor point of a Bezier
        curve, adding a new segment to a line or shape. The first time
        ``bezier_vertex()`` is used within a ``Py5Graphics.begin_shape()`` call, it must
        be prefaced with a call to ``Py5Graphics.vertex()`` to set the first anchor
        point. This function must be used between ``Py5Graphics.begin_shape()`` and
        ``Py5Graphics.end_shape()`` and only when there is no ``MODE`` parameter
        specified to ``Py5Graphics.begin_shape()``. Using the 3D version requires
        rendering with ``P3D``.

        This method is the same as ``bezier_vertex()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``bezier_vertex()``.
        """
        pass

    @overload
    def bezier_vertex(self, x2: float, y2: float, z2: float, x3: float,
                      y3: float, z3: float, x4: float, y4: float, z4: float, /) -> None:
        """Specifies vertex coordinates for Bezier curves.

        Underlying Java method: PGraphics.bezierVertex

        Methods
        -------

        You can use any of the following signatures:

         * bezier_vertex(x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, /) -> None
         * bezier_vertex(x2: float, y2: float, z2: float, x3: float, y3: float, z3: float, x4: float, y4: float, z4: float, /) -> None

        Parameters
        ----------

        x2: float
            the x-coordinate of the 1st control point

        x3: float
            the x-coordinate of the 2nd control point

        x4: float
            the x-coordinate of the anchor point

        y2: float
            the y-coordinate of the 1st control point

        y3: float
            the y-coordinate of the 2nd control point

        y4: float
            the y-coordinate of the anchor point

        z2: float
            the z-coordinate of the 1st control point

        z3: float
            the z-coordinate of the 2nd control point

        z4: float
            the z-coordinate of the anchor point

        Notes
        -----

        Specifies vertex coordinates for Bezier curves. Each call to ``bezier_vertex()``
        defines the position of two control points and one anchor point of a Bezier
        curve, adding a new segment to a line or shape. The first time
        ``bezier_vertex()`` is used within a ``Py5Graphics.begin_shape()`` call, it must
        be prefaced with a call to ``Py5Graphics.vertex()`` to set the first anchor
        point. This function must be used between ``Py5Graphics.begin_shape()`` and
        ``Py5Graphics.end_shape()`` and only when there is no ``MODE`` parameter
        specified to ``Py5Graphics.begin_shape()``. Using the 3D version requires
        rendering with ``P3D``.

        This method is the same as ``bezier_vertex()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``bezier_vertex()``.
        """
        pass

    def bezier_vertex(self, *args):
        """Specifies vertex coordinates for Bezier curves.

        Underlying Java method: PGraphics.bezierVertex

        Methods
        -------

        You can use any of the following signatures:

         * bezier_vertex(x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, /) -> None
         * bezier_vertex(x2: float, y2: float, z2: float, x3: float, y3: float, z3: float, x4: float, y4: float, z4: float, /) -> None

        Parameters
        ----------

        x2: float
            the x-coordinate of the 1st control point

        x3: float
            the x-coordinate of the 2nd control point

        x4: float
            the x-coordinate of the anchor point

        y2: float
            the y-coordinate of the 1st control point

        y3: float
            the y-coordinate of the 2nd control point

        y4: float
            the y-coordinate of the anchor point

        z2: float
            the z-coordinate of the 1st control point

        z3: float
            the z-coordinate of the 2nd control point

        z4: float
            the z-coordinate of the anchor point

        Notes
        -----

        Specifies vertex coordinates for Bezier curves. Each call to ``bezier_vertex()``
        defines the position of two control points and one anchor point of a Bezier
        curve, adding a new segment to a line or shape. The first time
        ``bezier_vertex()`` is used within a ``Py5Graphics.begin_shape()`` call, it must
        be prefaced with a call to ``Py5Graphics.vertex()`` to set the first anchor
        point. This function must be used between ``Py5Graphics.begin_shape()`` and
        ``Py5Graphics.end_shape()`` and only when there is no ``MODE`` parameter
        specified to ``Py5Graphics.begin_shape()``. Using the 3D version requires
        rendering with ``P3D``.

        This method is the same as ``bezier_vertex()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``bezier_vertex()``.
        """
        return self._instance.bezierVertex(*args)

    @overload
    def blend(self, sx: int, sy: int, sw: int, sh: int, dx: int,
              dy: int, dw: int, dh: int, mode: int, /) -> None:
        """Blends a region of pixels from one image into another (or in itself again) with
        full alpha channel support.

        Underlying Java method: PGraphics.blend

        Methods
        -------

        You can use any of the following signatures:

         * blend(src: Py5Image, sx: int, sy: int, sw: int, sh: int, dx: int, dy: int, dw: int, dh: int, mode: int, /) -> None
         * blend(sx: int, sy: int, sw: int, sh: int, dx: int, dy: int, dw: int, dh: int, mode: int, /) -> None

        Parameters
        ----------

        dh: int
            destination image height

        dw: int
            destination image width

        dx: int
            x-coordinate of the destinations's upper left corner

        dy: int
            y-coordinate of the destinations's upper left corner

        mode: int
            Either BLEND, ADD, SUBTRACT, LIGHTEST, DARKEST, DIFFERENCE, EXCLUSION, MULTIPLY, SCREEN, OVERLAY, HARD_LIGHT, SOFT_LIGHT, DODGE, BURN

        sh: int
            source image height

        src: Py5Image
            an image variable referring to the source image

        sw: int
            source image width

        sx: int
            x-coordinate of the source's upper left corner

        sy: int
            y-coordinate of the source's upper left corner

        Notes
        -----

        Blends a region of pixels from one image into another (or in itself again) with
        full alpha channel support. There is a choice of the following modes to blend
        the source pixels (A) with the ones of pixels in the destination image (B):

        * BLEND: linear interpolation of colors: ``C = A*factor + B``
        * ADD: additive blending with white clip: ``C = min(A*factor + B, 255)``
        * SUBTRACT: subtractive blending with black clip: ``C = max(B - A*factor, 0)``
        * DARKEST: only the darkest color succeeds: ``C = min(A*factor, B)``
        * LIGHTEST: only the lightest color succeeds: ``C = max(A*factor, B)``
        * DIFFERENCE: subtract colors from underlying image.
        * EXCLUSION: similar to ``DIFFERENCE``, but less extreme.
        * MULTIPLY: Multiply the colors, result will always be darker.
        * SCREEN: Opposite multiply, uses inverse values of the colors.
        * OVERLAY: A mix of ``MULTIPLY`` and SCREEN. Multiplies dark values, and screens
        light values.
        * HARD_LIGHT: ``SCREEN`` when greater than 50% gray, ``MULTIPLY`` when lower.
        * SOFT_LIGHT: Mix of ``DARKEST`` and LIGHTEST.  Works like ``OVERLAY``, but not
        as harsh.
        * DODGE: Lightens light tones and increases contrast, ignores darks. Called
        "Color Dodge" in Illustrator and Photoshop.
        * BURN: Darker areas are applied, increasing contrast, ignores lights. Called
        "Color Burn" in Illustrator and Photoshop.

        All modes use the alpha information (highest byte) of source image pixels as the
        blending factor. If the source and destination regions are different sizes, the
        image will be automatically resized to match the destination size. If the
        ``src`` parameter is not used, the Py5Graphics drawing surface is used as the
        source image.

        This function ignores ``Py5Graphics.image_mode()``.

        This method is the same as ``blend()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``blend()``.
        """
        pass

    @overload
    def blend(self, src: Py5Image, sx: int, sy: int, sw: int, sh: int,
              dx: int, dy: int, dw: int, dh: int, mode: int, /) -> None:
        """Blends a region of pixels from one image into another (or in itself again) with
        full alpha channel support.

        Underlying Java method: PGraphics.blend

        Methods
        -------

        You can use any of the following signatures:

         * blend(src: Py5Image, sx: int, sy: int, sw: int, sh: int, dx: int, dy: int, dw: int, dh: int, mode: int, /) -> None
         * blend(sx: int, sy: int, sw: int, sh: int, dx: int, dy: int, dw: int, dh: int, mode: int, /) -> None

        Parameters
        ----------

        dh: int
            destination image height

        dw: int
            destination image width

        dx: int
            x-coordinate of the destinations's upper left corner

        dy: int
            y-coordinate of the destinations's upper left corner

        mode: int
            Either BLEND, ADD, SUBTRACT, LIGHTEST, DARKEST, DIFFERENCE, EXCLUSION, MULTIPLY, SCREEN, OVERLAY, HARD_LIGHT, SOFT_LIGHT, DODGE, BURN

        sh: int
            source image height

        src: Py5Image
            an image variable referring to the source image

        sw: int
            source image width

        sx: int
            x-coordinate of the source's upper left corner

        sy: int
            y-coordinate of the source's upper left corner

        Notes
        -----

        Blends a region of pixels from one image into another (or in itself again) with
        full alpha channel support. There is a choice of the following modes to blend
        the source pixels (A) with the ones of pixels in the destination image (B):

        * BLEND: linear interpolation of colors: ``C = A*factor + B``
        * ADD: additive blending with white clip: ``C = min(A*factor + B, 255)``
        * SUBTRACT: subtractive blending with black clip: ``C = max(B - A*factor, 0)``
        * DARKEST: only the darkest color succeeds: ``C = min(A*factor, B)``
        * LIGHTEST: only the lightest color succeeds: ``C = max(A*factor, B)``
        * DIFFERENCE: subtract colors from underlying image.
        * EXCLUSION: similar to ``DIFFERENCE``, but less extreme.
        * MULTIPLY: Multiply the colors, result will always be darker.
        * SCREEN: Opposite multiply, uses inverse values of the colors.
        * OVERLAY: A mix of ``MULTIPLY`` and SCREEN. Multiplies dark values, and screens
        light values.
        * HARD_LIGHT: ``SCREEN`` when greater than 50% gray, ``MULTIPLY`` when lower.
        * SOFT_LIGHT: Mix of ``DARKEST`` and LIGHTEST.  Works like ``OVERLAY``, but not
        as harsh.
        * DODGE: Lightens light tones and increases contrast, ignores darks. Called
        "Color Dodge" in Illustrator and Photoshop.
        * BURN: Darker areas are applied, increasing contrast, ignores lights. Called
        "Color Burn" in Illustrator and Photoshop.

        All modes use the alpha information (highest byte) of source image pixels as the
        blending factor. If the source and destination regions are different sizes, the
        image will be automatically resized to match the destination size. If the
        ``src`` parameter is not used, the Py5Graphics drawing surface is used as the
        source image.

        This function ignores ``Py5Graphics.image_mode()``.

        This method is the same as ``blend()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``blend()``.
        """
        pass

    def blend(self, *args):
        """Blends a region of pixels from one image into another (or in itself again) with
        full alpha channel support.

        Underlying Java method: PGraphics.blend

        Methods
        -------

        You can use any of the following signatures:

         * blend(src: Py5Image, sx: int, sy: int, sw: int, sh: int, dx: int, dy: int, dw: int, dh: int, mode: int, /) -> None
         * blend(sx: int, sy: int, sw: int, sh: int, dx: int, dy: int, dw: int, dh: int, mode: int, /) -> None

        Parameters
        ----------

        dh: int
            destination image height

        dw: int
            destination image width

        dx: int
            x-coordinate of the destinations's upper left corner

        dy: int
            y-coordinate of the destinations's upper left corner

        mode: int
            Either BLEND, ADD, SUBTRACT, LIGHTEST, DARKEST, DIFFERENCE, EXCLUSION, MULTIPLY, SCREEN, OVERLAY, HARD_LIGHT, SOFT_LIGHT, DODGE, BURN

        sh: int
            source image height

        src: Py5Image
            an image variable referring to the source image

        sw: int
            source image width

        sx: int
            x-coordinate of the source's upper left corner

        sy: int
            y-coordinate of the source's upper left corner

        Notes
        -----

        Blends a region of pixels from one image into another (or in itself again) with
        full alpha channel support. There is a choice of the following modes to blend
        the source pixels (A) with the ones of pixels in the destination image (B):

        * BLEND: linear interpolation of colors: ``C = A*factor + B``
        * ADD: additive blending with white clip: ``C = min(A*factor + B, 255)``
        * SUBTRACT: subtractive blending with black clip: ``C = max(B - A*factor, 0)``
        * DARKEST: only the darkest color succeeds: ``C = min(A*factor, B)``
        * LIGHTEST: only the lightest color succeeds: ``C = max(A*factor, B)``
        * DIFFERENCE: subtract colors from underlying image.
        * EXCLUSION: similar to ``DIFFERENCE``, but less extreme.
        * MULTIPLY: Multiply the colors, result will always be darker.
        * SCREEN: Opposite multiply, uses inverse values of the colors.
        * OVERLAY: A mix of ``MULTIPLY`` and SCREEN. Multiplies dark values, and screens
        light values.
        * HARD_LIGHT: ``SCREEN`` when greater than 50% gray, ``MULTIPLY`` when lower.
        * SOFT_LIGHT: Mix of ``DARKEST`` and LIGHTEST.  Works like ``OVERLAY``, but not
        as harsh.
        * DODGE: Lightens light tones and increases contrast, ignores darks. Called
        "Color Dodge" in Illustrator and Photoshop.
        * BURN: Darker areas are applied, increasing contrast, ignores lights. Called
        "Color Burn" in Illustrator and Photoshop.

        All modes use the alpha information (highest byte) of source image pixels as the
        blending factor. If the source and destination regions are different sizes, the
        image will be automatically resized to match the destination size. If the
        ``src`` parameter is not used, the Py5Graphics drawing surface is used as the
        source image.

        This function ignores ``Py5Graphics.image_mode()``.

        This method is the same as ``blend()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``blend()``.
        """
        return self._instance.blend(*args)

    def blend_mode(self, mode: int, /) -> None:
        """Blends the pixels in the Py5Graphics drawing surface according to a defined
        mode.

        Underlying Java method: PGraphics.blendMode

        Parameters
        ----------

        mode: int
            the blending mode to use

        Notes
        -----

        Blends the pixels in the Py5Graphics drawing surface according to a defined
        mode. There is a choice of the following modes to blend the source pixels (A)
        with the ones of pixels already in the Py5Graphics drawing surface (B). Each
        pixel's final color is the result of applying one of the blend modes with each
        channel of (A) and (B) independently. The red channel is compared with red,
        green with green, and blue with blue.

        * BLEND: linear interpolation of colors: ``C = A*factor + B``. This is the
        default.
        * ADD: additive blending with white clip: ``C = min(A*factor + B, 255)``
        * SUBTRACT: subtractive blending with black clip: ``C = max(B - A*factor, 0)``
        * DARKEST: only the darkest color succeeds: ``C = min(A*factor, B)``
        * LIGHTEST: only the lightest color succeeds: ``C = max(A*factor, B)``
        * DIFFERENCE: subtract colors from underlying image.
        * EXCLUSION: similar to ``DIFFERENCE``, but less extreme.
        * MULTIPLY: multiply the colors, result will always be darker.
        * SCREEN: opposite multiply, uses inverse values of the colors.
        * REPLACE: the pixels entirely replace the others and don't utilize alpha
        (transparency) values

        We recommend using ``blend_mode()`` and not the previous ``Py5Graphics.blend()``
        function. However, unlike ``Py5Graphics.blend()``, the ``blend_mode()`` function
        does not support the following: ``HARD_LIGHT``, ``SOFT_LIGHT``, ``OVERLAY``,
        ``DODGE``, ``BURN``. On older hardware, the ``LIGHTEST``, ``DARKEST``, and
        ``DIFFERENCE`` modes might not be available as well.

        This method is the same as ``blend_mode()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``blend_mode()``.
        """
        return self._instance.blendMode(mode)

    def blue(self, rgb: int, /) -> float:
        """Extracts the blue value from a color, scaled to match current
        ``Py5Graphics.color_mode()``.

        Underlying Java method: PGraphics.blue

        Parameters
        ----------

        rgb: int
            any value of the color datatype

        Notes
        -----

        Extracts the blue value from a color, scaled to match current
        ``Py5Graphics.color_mode()``.

        The ``blue()`` function is easy to use and understand, but it is slower than a
        technique called bit masking. When working in ``color_mode(RGB, 255)``, you can
        achieve the same results as ``blue()`` but with greater speed by using a bit
        mask to remove the other color components. For example, ``blue(c)`` and ``c &
        0xFF`` both extract the blue value from a color variable ``c`` but the later is
        faster.

        This method is the same as ``blue()`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``blue()``.
        """
        return self._instance.blue(rgb)

    @overload
    def box(self, size: float, /) -> None:
        """A box is an extruded rectangle.

        Underlying Java method: PGraphics.box

        Methods
        -------

        You can use any of the following signatures:

         * box(size: float, /) -> None
         * box(w: float, h: float, d: float, /) -> None

        Parameters
        ----------

        d: float
            dimension of the box in the z-dimension

        h: float
            dimension of the box in the y-dimension

        size: float
            dimension of the box in all dimensions (creates a cube)

        w: float
            dimension of the box in the x-dimension

        Notes
        -----

        A box is an extruded rectangle. A box with equal dimensions on all sides is a
        cube.

        This method is the same as ``box()`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``box()``.
        """
        pass

    @overload
    def box(self, w: float, h: float, d: float, /) -> None:
        """A box is an extruded rectangle.

        Underlying Java method: PGraphics.box

        Methods
        -------

        You can use any of the following signatures:

         * box(size: float, /) -> None
         * box(w: float, h: float, d: float, /) -> None

        Parameters
        ----------

        d: float
            dimension of the box in the z-dimension

        h: float
            dimension of the box in the y-dimension

        size: float
            dimension of the box in all dimensions (creates a cube)

        w: float
            dimension of the box in the x-dimension

        Notes
        -----

        A box is an extruded rectangle. A box with equal dimensions on all sides is a
        cube.

        This method is the same as ``box()`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``box()``.
        """
        pass

    def box(self, *args):
        """A box is an extruded rectangle.

        Underlying Java method: PGraphics.box

        Methods
        -------

        You can use any of the following signatures:

         * box(size: float, /) -> None
         * box(w: float, h: float, d: float, /) -> None

        Parameters
        ----------

        d: float
            dimension of the box in the z-dimension

        h: float
            dimension of the box in the y-dimension

        size: float
            dimension of the box in all dimensions (creates a cube)

        w: float
            dimension of the box in the x-dimension

        Notes
        -----

        A box is an extruded rectangle. A box with equal dimensions on all sides is a
        cube.

        This method is the same as ``box()`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``box()``.
        """
        return self._instance.box(*args)

    def brightness(self, rgb: int, /) -> float:
        """Extracts the brightness value from a color.

        Underlying Java method: PGraphics.brightness

        Parameters
        ----------

        rgb: int
            any value of the color datatype

        Notes
        -----

        Extracts the brightness value from a color.

        This method is the same as ``brightness()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``brightness()``.
        """
        return self._instance.brightness(rgb)

    @overload
    def camera(self) -> None:
        """Sets the position of the camera through setting the eye position, the center of
        the scene, and which axis is facing upward.

        Underlying Java method: PGraphics.camera

        Methods
        -------

        You can use any of the following signatures:

         * camera() -> None
         * camera(eye_x: float, eye_y: float, eye_z: float, center_x: float, center_y: float, center_z: float, up_x: float, up_y: float, up_z: float, /) -> None

        Parameters
        ----------

        center_x: float
            x-coordinate for the center of the scene

        center_y: float
            y-coordinate for the center of the scene

        center_z: float
            z-coordinate for the center of the scene

        eye_x: float
            x-coordinate for the eye

        eye_y: float
            y-coordinate for the eye

        eye_z: float
            z-coordinate for the eye

        up_x: float
            usually 0.0, 1.0, or -1.0

        up_y: float
            usually 0.0, 1.0, or -1.0

        up_z: float
            usually 0.0, 1.0, or -1.0

        Notes
        -----

        Sets the position of the camera through setting the eye position, the center of
        the scene, and which axis is facing upward. Moving the eye position and the
        direction it is pointing (the center of the scene) allows the images to be seen
        from different angles. The version without any parameters sets the camera to the
        default position, pointing to the center of the Py5Graphics drawing surface with
        the Y axis as up. The default values are ``camera(width//2.0, height//2.0,
        (height//2.0) / tan(PI*30.0 / 180.0), width//2.0, height//2.0, 0, 0, 1, 0)``.
        This function is similar to ``glu_look_at()`` in OpenGL, but it first clears the
        current camera settings.

        This method is the same as ``camera()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``camera()``.
        """
        pass

    @overload
    def camera(
            self,
            eye_x: float,
            eye_y: float,
            eye_z: float,
            center_x: float,
            center_y: float,
            center_z: float,
            up_x: float,
            up_y: float,
            up_z: float,
            /) -> None:
        """Sets the position of the camera through setting the eye position, the center of
        the scene, and which axis is facing upward.

        Underlying Java method: PGraphics.camera

        Methods
        -------

        You can use any of the following signatures:

         * camera() -> None
         * camera(eye_x: float, eye_y: float, eye_z: float, center_x: float, center_y: float, center_z: float, up_x: float, up_y: float, up_z: float, /) -> None

        Parameters
        ----------

        center_x: float
            x-coordinate for the center of the scene

        center_y: float
            y-coordinate for the center of the scene

        center_z: float
            z-coordinate for the center of the scene

        eye_x: float
            x-coordinate for the eye

        eye_y: float
            y-coordinate for the eye

        eye_z: float
            z-coordinate for the eye

        up_x: float
            usually 0.0, 1.0, or -1.0

        up_y: float
            usually 0.0, 1.0, or -1.0

        up_z: float
            usually 0.0, 1.0, or -1.0

        Notes
        -----

        Sets the position of the camera through setting the eye position, the center of
        the scene, and which axis is facing upward. Moving the eye position and the
        direction it is pointing (the center of the scene) allows the images to be seen
        from different angles. The version without any parameters sets the camera to the
        default position, pointing to the center of the Py5Graphics drawing surface with
        the Y axis as up. The default values are ``camera(width//2.0, height//2.0,
        (height//2.0) / tan(PI*30.0 / 180.0), width//2.0, height//2.0, 0, 0, 1, 0)``.
        This function is similar to ``glu_look_at()`` in OpenGL, but it first clears the
        current camera settings.

        This method is the same as ``camera()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``camera()``.
        """
        pass

    def camera(self, *args):
        """Sets the position of the camera through setting the eye position, the center of
        the scene, and which axis is facing upward.

        Underlying Java method: PGraphics.camera

        Methods
        -------

        You can use any of the following signatures:

         * camera() -> None
         * camera(eye_x: float, eye_y: float, eye_z: float, center_x: float, center_y: float, center_z: float, up_x: float, up_y: float, up_z: float, /) -> None

        Parameters
        ----------

        center_x: float
            x-coordinate for the center of the scene

        center_y: float
            y-coordinate for the center of the scene

        center_z: float
            z-coordinate for the center of the scene

        eye_x: float
            x-coordinate for the eye

        eye_y: float
            y-coordinate for the eye

        eye_z: float
            z-coordinate for the eye

        up_x: float
            usually 0.0, 1.0, or -1.0

        up_y: float
            usually 0.0, 1.0, or -1.0

        up_z: float
            usually 0.0, 1.0, or -1.0

        Notes
        -----

        Sets the position of the camera through setting the eye position, the center of
        the scene, and which axis is facing upward. Moving the eye position and the
        direction it is pointing (the center of the scene) allows the images to be seen
        from different angles. The version without any parameters sets the camera to the
        default position, pointing to the center of the Py5Graphics drawing surface with
        the Y axis as up. The default values are ``camera(width//2.0, height//2.0,
        (height//2.0) / tan(PI*30.0 / 180.0), width//2.0, height//2.0, 0, 0, 1, 0)``.
        This function is similar to ``glu_look_at()`` in OpenGL, but it first clears the
        current camera settings.

        This method is the same as ``camera()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``camera()``.
        """
        return self._instance.camera(*args)

    def circle(self, x: float, y: float, extent: float, /) -> None:
        """Draws a circle to the screen.

        Underlying Java method: PGraphics.circle

        Parameters
        ----------

        extent: float
            width and height of the ellipse by default

        x: float
            x-coordinate of the ellipse

        y: float
            y-coordinate of the ellipse

        Notes
        -----

        Draws a circle to the screen. By default, the first two parameters set the
        location of the center, and the third sets the shape's width and height. The
        origin may be changed with the ``Py5Graphics.ellipse_mode()`` function.

        This method is the same as ``circle()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``circle()``.
        """
        return self._instance.circle(x, y, extent)

    def clear(self) -> None:
        """Clears the pixels within a buffer.

        Underlying Java method: PGraphics.clear

        Notes
        -----

        Clears the pixels within a buffer. Unlike the main graphics context (the display
        window), pixels in ``Py5Graphics`` objects created with ``create_graphics()``
        can be entirely or partially transparent. This function clears everything in a
        ``Py5Graphics`` object to make all of the pixels 100% transparent.
        """
        return self._instance.clear()

    def clip(self, a: float, b: float, c: float, d: float, /) -> None:
        """Limits the rendering to the boundaries of a rectangle defined by the parameters.

        Underlying Java method: PGraphics.clip

        Parameters
        ----------

        a: float
            x-coordinate of the rectangle, by default

        b: float
            y-coordinate of the rectangle, by default

        c: float
            width of the rectangle, by default

        d: float
            height of the rectangle, by default

        Notes
        -----

        Limits the rendering to the boundaries of a rectangle defined by the parameters.
        The boundaries are drawn based on the state of the ``Py5Graphics.image_mode()``
        fuction, either ``CORNER``, ``CORNERS``, or ``CENTER``.

        This method is the same as ``clip()`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``clip()``.
        """
        return self._instance.clip(a, b, c, d)

    @overload
    def color(self, gray: float, /) -> int:
        """Creates colors for storing in variables of the ``color`` datatype (a 32 bit
        integer).

        Underlying Java method: PGraphics.color

        Methods
        -------

        You can use any of the following signatures:

         * color(c: int, /) -> int
         * color(c: int, alpha: float, /) -> int
         * color(c: int, alpha: int, /) -> int
         * color(gray: float, /) -> int
         * color(gray: float, alpha: float, /) -> int
         * color(v1: float, v2: float, v3: float, /) -> int
         * color(v1: float, v2: float, v3: float, a: float, /) -> int
         * color(v1: int, v2: int, v3: int, /) -> int
         * color(v1: int, v2: int, v3: int, a: int, /) -> int

        Parameters
        ----------

        a: float
            alpha value relative to current color range

        a: int
            alpha value relative to current color range

        alpha: float
            alpha value relative to current color range

        alpha: int
            alpha value relative to current color range

        c: int
            color value

        gray: float
            gray value relative to current color range

        v1: float
            red or hue values relative to the current color range

        v1: int
            red or hue values relative to the current color range

        v2: float
            green or saturation values relative to the current color range

        v2: int
            green or saturation values relative to the current color range

        v3: float
            blue or brightness values relative to the current color range

        v3: int
            blue or brightness values relative to the current color range

        Notes
        -----

        Creates colors for storing in variables of the ``color`` datatype (a 32 bit
        integer). The parameters are interpreted as ``RGB`` or ``HSB`` values depending
        on the current ``Py5Graphics.color_mode()``. The default mode is ``RGB`` values
        from 0 to 255 and, therefore, ``color(255, 204, 0)`` will return a bright yellow
        color (see the first example).

        Note that if only one value is provided to ``color()``, it will be interpreted
        as a grayscale value. Add a second value, and it will be used for alpha
        transparency. When three values are specified, they are interpreted as either
        ``RGB`` or ``HSB`` values. Adding a fourth value applies alpha transparency.

        Note that when using hexadecimal notation, it is not necessary to use
        ``color()``, as in: ``c = 0x006699``

        This method is the same as ``color()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``color()``.
        """
        pass

    @overload
    def color(self, gray: float, alpha: float, /) -> int:
        """Creates colors for storing in variables of the ``color`` datatype (a 32 bit
        integer).

        Underlying Java method: PGraphics.color

        Methods
        -------

        You can use any of the following signatures:

         * color(c: int, /) -> int
         * color(c: int, alpha: float, /) -> int
         * color(c: int, alpha: int, /) -> int
         * color(gray: float, /) -> int
         * color(gray: float, alpha: float, /) -> int
         * color(v1: float, v2: float, v3: float, /) -> int
         * color(v1: float, v2: float, v3: float, a: float, /) -> int
         * color(v1: int, v2: int, v3: int, /) -> int
         * color(v1: int, v2: int, v3: int, a: int, /) -> int

        Parameters
        ----------

        a: float
            alpha value relative to current color range

        a: int
            alpha value relative to current color range

        alpha: float
            alpha value relative to current color range

        alpha: int
            alpha value relative to current color range

        c: int
            color value

        gray: float
            gray value relative to current color range

        v1: float
            red or hue values relative to the current color range

        v1: int
            red or hue values relative to the current color range

        v2: float
            green or saturation values relative to the current color range

        v2: int
            green or saturation values relative to the current color range

        v3: float
            blue or brightness values relative to the current color range

        v3: int
            blue or brightness values relative to the current color range

        Notes
        -----

        Creates colors for storing in variables of the ``color`` datatype (a 32 bit
        integer). The parameters are interpreted as ``RGB`` or ``HSB`` values depending
        on the current ``Py5Graphics.color_mode()``. The default mode is ``RGB`` values
        from 0 to 255 and, therefore, ``color(255, 204, 0)`` will return a bright yellow
        color (see the first example).

        Note that if only one value is provided to ``color()``, it will be interpreted
        as a grayscale value. Add a second value, and it will be used for alpha
        transparency. When three values are specified, they are interpreted as either
        ``RGB`` or ``HSB`` values. Adding a fourth value applies alpha transparency.

        Note that when using hexadecimal notation, it is not necessary to use
        ``color()``, as in: ``c = 0x006699``

        This method is the same as ``color()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``color()``.
        """
        pass

    @overload
    def color(self, v1: float, v2: float, v3: float, /) -> int:
        """Creates colors for storing in variables of the ``color`` datatype (a 32 bit
        integer).

        Underlying Java method: PGraphics.color

        Methods
        -------

        You can use any of the following signatures:

         * color(c: int, /) -> int
         * color(c: int, alpha: float, /) -> int
         * color(c: int, alpha: int, /) -> int
         * color(gray: float, /) -> int
         * color(gray: float, alpha: float, /) -> int
         * color(v1: float, v2: float, v3: float, /) -> int
         * color(v1: float, v2: float, v3: float, a: float, /) -> int
         * color(v1: int, v2: int, v3: int, /) -> int
         * color(v1: int, v2: int, v3: int, a: int, /) -> int

        Parameters
        ----------

        a: float
            alpha value relative to current color range

        a: int
            alpha value relative to current color range

        alpha: float
            alpha value relative to current color range

        alpha: int
            alpha value relative to current color range

        c: int
            color value

        gray: float
            gray value relative to current color range

        v1: float
            red or hue values relative to the current color range

        v1: int
            red or hue values relative to the current color range

        v2: float
            green or saturation values relative to the current color range

        v2: int
            green or saturation values relative to the current color range

        v3: float
            blue or brightness values relative to the current color range

        v3: int
            blue or brightness values relative to the current color range

        Notes
        -----

        Creates colors for storing in variables of the ``color`` datatype (a 32 bit
        integer). The parameters are interpreted as ``RGB`` or ``HSB`` values depending
        on the current ``Py5Graphics.color_mode()``. The default mode is ``RGB`` values
        from 0 to 255 and, therefore, ``color(255, 204, 0)`` will return a bright yellow
        color (see the first example).

        Note that if only one value is provided to ``color()``, it will be interpreted
        as a grayscale value. Add a second value, and it will be used for alpha
        transparency. When three values are specified, they are interpreted as either
        ``RGB`` or ``HSB`` values. Adding a fourth value applies alpha transparency.

        Note that when using hexadecimal notation, it is not necessary to use
        ``color()``, as in: ``c = 0x006699``

        This method is the same as ``color()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``color()``.
        """
        pass

    @overload
    def color(self, v1: float, v2: float, v3: float, a: float, /) -> int:
        """Creates colors for storing in variables of the ``color`` datatype (a 32 bit
        integer).

        Underlying Java method: PGraphics.color

        Methods
        -------

        You can use any of the following signatures:

         * color(c: int, /) -> int
         * color(c: int, alpha: float, /) -> int
         * color(c: int, alpha: int, /) -> int
         * color(gray: float, /) -> int
         * color(gray: float, alpha: float, /) -> int
         * color(v1: float, v2: float, v3: float, /) -> int
         * color(v1: float, v2: float, v3: float, a: float, /) -> int
         * color(v1: int, v2: int, v3: int, /) -> int
         * color(v1: int, v2: int, v3: int, a: int, /) -> int

        Parameters
        ----------

        a: float
            alpha value relative to current color range

        a: int
            alpha value relative to current color range

        alpha: float
            alpha value relative to current color range

        alpha: int
            alpha value relative to current color range

        c: int
            color value

        gray: float
            gray value relative to current color range

        v1: float
            red or hue values relative to the current color range

        v1: int
            red or hue values relative to the current color range

        v2: float
            green or saturation values relative to the current color range

        v2: int
            green or saturation values relative to the current color range

        v3: float
            blue or brightness values relative to the current color range

        v3: int
            blue or brightness values relative to the current color range

        Notes
        -----

        Creates colors for storing in variables of the ``color`` datatype (a 32 bit
        integer). The parameters are interpreted as ``RGB`` or ``HSB`` values depending
        on the current ``Py5Graphics.color_mode()``. The default mode is ``RGB`` values
        from 0 to 255 and, therefore, ``color(255, 204, 0)`` will return a bright yellow
        color (see the first example).

        Note that if only one value is provided to ``color()``, it will be interpreted
        as a grayscale value. Add a second value, and it will be used for alpha
        transparency. When three values are specified, they are interpreted as either
        ``RGB`` or ``HSB`` values. Adding a fourth value applies alpha transparency.

        Note that when using hexadecimal notation, it is not necessary to use
        ``color()``, as in: ``c = 0x006699``

        This method is the same as ``color()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``color()``.
        """
        pass

    @overload
    def color(self, c: int, /) -> int:
        """Creates colors for storing in variables of the ``color`` datatype (a 32 bit
        integer).

        Underlying Java method: PGraphics.color

        Methods
        -------

        You can use any of the following signatures:

         * color(c: int, /) -> int
         * color(c: int, alpha: float, /) -> int
         * color(c: int, alpha: int, /) -> int
         * color(gray: float, /) -> int
         * color(gray: float, alpha: float, /) -> int
         * color(v1: float, v2: float, v3: float, /) -> int
         * color(v1: float, v2: float, v3: float, a: float, /) -> int
         * color(v1: int, v2: int, v3: int, /) -> int
         * color(v1: int, v2: int, v3: int, a: int, /) -> int

        Parameters
        ----------

        a: float
            alpha value relative to current color range

        a: int
            alpha value relative to current color range

        alpha: float
            alpha value relative to current color range

        alpha: int
            alpha value relative to current color range

        c: int
            color value

        gray: float
            gray value relative to current color range

        v1: float
            red or hue values relative to the current color range

        v1: int
            red or hue values relative to the current color range

        v2: float
            green or saturation values relative to the current color range

        v2: int
            green or saturation values relative to the current color range

        v3: float
            blue or brightness values relative to the current color range

        v3: int
            blue or brightness values relative to the current color range

        Notes
        -----

        Creates colors for storing in variables of the ``color`` datatype (a 32 bit
        integer). The parameters are interpreted as ``RGB`` or ``HSB`` values depending
        on the current ``Py5Graphics.color_mode()``. The default mode is ``RGB`` values
        from 0 to 255 and, therefore, ``color(255, 204, 0)`` will return a bright yellow
        color (see the first example).

        Note that if only one value is provided to ``color()``, it will be interpreted
        as a grayscale value. Add a second value, and it will be used for alpha
        transparency. When three values are specified, they are interpreted as either
        ``RGB`` or ``HSB`` values. Adding a fourth value applies alpha transparency.

        Note that when using hexadecimal notation, it is not necessary to use
        ``color()``, as in: ``c = 0x006699``

        This method is the same as ``color()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``color()``.
        """
        pass

    @overload
    def color(self, c: int, alpha: float, /) -> int:
        """Creates colors for storing in variables of the ``color`` datatype (a 32 bit
        integer).

        Underlying Java method: PGraphics.color

        Methods
        -------

        You can use any of the following signatures:

         * color(c: int, /) -> int
         * color(c: int, alpha: float, /) -> int
         * color(c: int, alpha: int, /) -> int
         * color(gray: float, /) -> int
         * color(gray: float, alpha: float, /) -> int
         * color(v1: float, v2: float, v3: float, /) -> int
         * color(v1: float, v2: float, v3: float, a: float, /) -> int
         * color(v1: int, v2: int, v3: int, /) -> int
         * color(v1: int, v2: int, v3: int, a: int, /) -> int

        Parameters
        ----------

        a: float
            alpha value relative to current color range

        a: int
            alpha value relative to current color range

        alpha: float
            alpha value relative to current color range

        alpha: int
            alpha value relative to current color range

        c: int
            color value

        gray: float
            gray value relative to current color range

        v1: float
            red or hue values relative to the current color range

        v1: int
            red or hue values relative to the current color range

        v2: float
            green or saturation values relative to the current color range

        v2: int
            green or saturation values relative to the current color range

        v3: float
            blue or brightness values relative to the current color range

        v3: int
            blue or brightness values relative to the current color range

        Notes
        -----

        Creates colors for storing in variables of the ``color`` datatype (a 32 bit
        integer). The parameters are interpreted as ``RGB`` or ``HSB`` values depending
        on the current ``Py5Graphics.color_mode()``. The default mode is ``RGB`` values
        from 0 to 255 and, therefore, ``color(255, 204, 0)`` will return a bright yellow
        color (see the first example).

        Note that if only one value is provided to ``color()``, it will be interpreted
        as a grayscale value. Add a second value, and it will be used for alpha
        transparency. When three values are specified, they are interpreted as either
        ``RGB`` or ``HSB`` values. Adding a fourth value applies alpha transparency.

        Note that when using hexadecimal notation, it is not necessary to use
        ``color()``, as in: ``c = 0x006699``

        This method is the same as ``color()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``color()``.
        """
        pass

    @overload
    def color(self, c: int, alpha: int, /) -> int:
        """Creates colors for storing in variables of the ``color`` datatype (a 32 bit
        integer).

        Underlying Java method: PGraphics.color

        Methods
        -------

        You can use any of the following signatures:

         * color(c: int, /) -> int
         * color(c: int, alpha: float, /) -> int
         * color(c: int, alpha: int, /) -> int
         * color(gray: float, /) -> int
         * color(gray: float, alpha: float, /) -> int
         * color(v1: float, v2: float, v3: float, /) -> int
         * color(v1: float, v2: float, v3: float, a: float, /) -> int
         * color(v1: int, v2: int, v3: int, /) -> int
         * color(v1: int, v2: int, v3: int, a: int, /) -> int

        Parameters
        ----------

        a: float
            alpha value relative to current color range

        a: int
            alpha value relative to current color range

        alpha: float
            alpha value relative to current color range

        alpha: int
            alpha value relative to current color range

        c: int
            color value

        gray: float
            gray value relative to current color range

        v1: float
            red or hue values relative to the current color range

        v1: int
            red or hue values relative to the current color range

        v2: float
            green or saturation values relative to the current color range

        v2: int
            green or saturation values relative to the current color range

        v3: float
            blue or brightness values relative to the current color range

        v3: int
            blue or brightness values relative to the current color range

        Notes
        -----

        Creates colors for storing in variables of the ``color`` datatype (a 32 bit
        integer). The parameters are interpreted as ``RGB`` or ``HSB`` values depending
        on the current ``Py5Graphics.color_mode()``. The default mode is ``RGB`` values
        from 0 to 255 and, therefore, ``color(255, 204, 0)`` will return a bright yellow
        color (see the first example).

        Note that if only one value is provided to ``color()``, it will be interpreted
        as a grayscale value. Add a second value, and it will be used for alpha
        transparency. When three values are specified, they are interpreted as either
        ``RGB`` or ``HSB`` values. Adding a fourth value applies alpha transparency.

        Note that when using hexadecimal notation, it is not necessary to use
        ``color()``, as in: ``c = 0x006699``

        This method is the same as ``color()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``color()``.
        """
        pass

    @overload
    def color(self, v1: int, v2: int, v3: int, /) -> int:
        """Creates colors for storing in variables of the ``color`` datatype (a 32 bit
        integer).

        Underlying Java method: PGraphics.color

        Methods
        -------

        You can use any of the following signatures:

         * color(c: int, /) -> int
         * color(c: int, alpha: float, /) -> int
         * color(c: int, alpha: int, /) -> int
         * color(gray: float, /) -> int
         * color(gray: float, alpha: float, /) -> int
         * color(v1: float, v2: float, v3: float, /) -> int
         * color(v1: float, v2: float, v3: float, a: float, /) -> int
         * color(v1: int, v2: int, v3: int, /) -> int
         * color(v1: int, v2: int, v3: int, a: int, /) -> int

        Parameters
        ----------

        a: float
            alpha value relative to current color range

        a: int
            alpha value relative to current color range

        alpha: float
            alpha value relative to current color range

        alpha: int
            alpha value relative to current color range

        c: int
            color value

        gray: float
            gray value relative to current color range

        v1: float
            red or hue values relative to the current color range

        v1: int
            red or hue values relative to the current color range

        v2: float
            green or saturation values relative to the current color range

        v2: int
            green or saturation values relative to the current color range

        v3: float
            blue or brightness values relative to the current color range

        v3: int
            blue or brightness values relative to the current color range

        Notes
        -----

        Creates colors for storing in variables of the ``color`` datatype (a 32 bit
        integer). The parameters are interpreted as ``RGB`` or ``HSB`` values depending
        on the current ``Py5Graphics.color_mode()``. The default mode is ``RGB`` values
        from 0 to 255 and, therefore, ``color(255, 204, 0)`` will return a bright yellow
        color (see the first example).

        Note that if only one value is provided to ``color()``, it will be interpreted
        as a grayscale value. Add a second value, and it will be used for alpha
        transparency. When three values are specified, they are interpreted as either
        ``RGB`` or ``HSB`` values. Adding a fourth value applies alpha transparency.

        Note that when using hexadecimal notation, it is not necessary to use
        ``color()``, as in: ``c = 0x006699``

        This method is the same as ``color()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``color()``.
        """
        pass

    @overload
    def color(self, v1: int, v2: int, v3: int, a: int, /) -> int:
        """Creates colors for storing in variables of the ``color`` datatype (a 32 bit
        integer).

        Underlying Java method: PGraphics.color

        Methods
        -------

        You can use any of the following signatures:

         * color(c: int, /) -> int
         * color(c: int, alpha: float, /) -> int
         * color(c: int, alpha: int, /) -> int
         * color(gray: float, /) -> int
         * color(gray: float, alpha: float, /) -> int
         * color(v1: float, v2: float, v3: float, /) -> int
         * color(v1: float, v2: float, v3: float, a: float, /) -> int
         * color(v1: int, v2: int, v3: int, /) -> int
         * color(v1: int, v2: int, v3: int, a: int, /) -> int

        Parameters
        ----------

        a: float
            alpha value relative to current color range

        a: int
            alpha value relative to current color range

        alpha: float
            alpha value relative to current color range

        alpha: int
            alpha value relative to current color range

        c: int
            color value

        gray: float
            gray value relative to current color range

        v1: float
            red or hue values relative to the current color range

        v1: int
            red or hue values relative to the current color range

        v2: float
            green or saturation values relative to the current color range

        v2: int
            green or saturation values relative to the current color range

        v3: float
            blue or brightness values relative to the current color range

        v3: int
            blue or brightness values relative to the current color range

        Notes
        -----

        Creates colors for storing in variables of the ``color`` datatype (a 32 bit
        integer). The parameters are interpreted as ``RGB`` or ``HSB`` values depending
        on the current ``Py5Graphics.color_mode()``. The default mode is ``RGB`` values
        from 0 to 255 and, therefore, ``color(255, 204, 0)`` will return a bright yellow
        color (see the first example).

        Note that if only one value is provided to ``color()``, it will be interpreted
        as a grayscale value. Add a second value, and it will be used for alpha
        transparency. When three values are specified, they are interpreted as either
        ``RGB`` or ``HSB`` values. Adding a fourth value applies alpha transparency.

        Note that when using hexadecimal notation, it is not necessary to use
        ``color()``, as in: ``c = 0x006699``

        This method is the same as ``color()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``color()``.
        """
        pass

    def color(self, *args):
        """Creates colors for storing in variables of the ``color`` datatype (a 32 bit
        integer).

        Underlying Java method: PGraphics.color

        Methods
        -------

        You can use any of the following signatures:

         * color(c: int, /) -> int
         * color(c: int, alpha: float, /) -> int
         * color(c: int, alpha: int, /) -> int
         * color(gray: float, /) -> int
         * color(gray: float, alpha: float, /) -> int
         * color(v1: float, v2: float, v3: float, /) -> int
         * color(v1: float, v2: float, v3: float, a: float, /) -> int
         * color(v1: int, v2: int, v3: int, /) -> int
         * color(v1: int, v2: int, v3: int, a: int, /) -> int

        Parameters
        ----------

        a: float
            alpha value relative to current color range

        a: int
            alpha value relative to current color range

        alpha: float
            alpha value relative to current color range

        alpha: int
            alpha value relative to current color range

        c: int
            color value

        gray: float
            gray value relative to current color range

        v1: float
            red or hue values relative to the current color range

        v1: int
            red or hue values relative to the current color range

        v2: float
            green or saturation values relative to the current color range

        v2: int
            green or saturation values relative to the current color range

        v3: float
            blue or brightness values relative to the current color range

        v3: int
            blue or brightness values relative to the current color range

        Notes
        -----

        Creates colors for storing in variables of the ``color`` datatype (a 32 bit
        integer). The parameters are interpreted as ``RGB`` or ``HSB`` values depending
        on the current ``Py5Graphics.color_mode()``. The default mode is ``RGB`` values
        from 0 to 255 and, therefore, ``color(255, 204, 0)`` will return a bright yellow
        color (see the first example).

        Note that if only one value is provided to ``color()``, it will be interpreted
        as a grayscale value. Add a second value, and it will be used for alpha
        transparency. When three values are specified, they are interpreted as either
        ``RGB`` or ``HSB`` values. Adding a fourth value applies alpha transparency.

        Note that when using hexadecimal notation, it is not necessary to use
        ``color()``, as in: ``c = 0x006699``

        This method is the same as ``color()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``color()``.
        """
        return self._instance.color(*args)

    @overload
    def color_mode(self, mode: int, /) -> None:
        """Changes the way py5 interprets color data.

        Underlying Java method: PGraphics.colorMode

        Methods
        -------

        You can use any of the following signatures:

         * color_mode(mode: int, /) -> None
         * color_mode(mode: int, max1: float, max2: float, max3: float, /) -> None
         * color_mode(mode: int, max1: float, max2: float, max3: float, max_a: float, /) -> None
         * color_mode(mode: int, max: float, /) -> None

        Parameters
        ----------

        max1: float
            range for the red or hue depending on the current color mode

        max2: float
            range for the green or saturation depending on the current color mode

        max3: float
            range for the blue or brightness depending on the current color mode

        max: float
            range for all color elements

        max_a: float
            range for the alpha

        mode: int
            Either RGB or HSB, corresponding to Red/Green/Blue and Hue/Saturation/Brightness

        Notes
        -----

        Changes the way py5 interprets color data. By default, the parameters for
        ``Py5Graphics.fill()``, ``Py5Graphics.stroke()``, ``Py5Graphics.background()``,
        and ``Py5Graphics.color()`` are defined by values between 0 and 255 using the
        ``RGB`` color model. The ``color_mode()`` function is used to change the
        numerical range used for specifying colors and to switch color systems. For
        example, calling ``color_mode(RGB, 1.0)`` will specify that values are specified
        between 0 and 1. The limits for defining colors are altered by setting the
        parameters ``max``, ``max1``, ``max2``, ``max3``, and ``max_a``.

        After changing the range of values for colors with code like ``color_mode(HSB,
        360, 100, 100)``, those ranges remain in use until they are explicitly changed
        again. For example, after running ``color_mode(HSB, 360, 100, 100)`` and then
        changing back to ``color_mode(RGB)``, the range for R will be 0 to 360 and the
        range for G and B will be 0 to 100. To avoid this, be explicit about the ranges
        when changing the color mode. For instance, instead of ``color_mode(RGB)``,
        write ``color_mode(RGB, 255, 255, 255)``.

        This method is the same as ``color_mode()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``color_mode()``.
        """
        pass

    @overload
    def color_mode(self, mode: int, max: float, /) -> None:
        """Changes the way py5 interprets color data.

        Underlying Java method: PGraphics.colorMode

        Methods
        -------

        You can use any of the following signatures:

         * color_mode(mode: int, /) -> None
         * color_mode(mode: int, max1: float, max2: float, max3: float, /) -> None
         * color_mode(mode: int, max1: float, max2: float, max3: float, max_a: float, /) -> None
         * color_mode(mode: int, max: float, /) -> None

        Parameters
        ----------

        max1: float
            range for the red or hue depending on the current color mode

        max2: float
            range for the green or saturation depending on the current color mode

        max3: float
            range for the blue or brightness depending on the current color mode

        max: float
            range for all color elements

        max_a: float
            range for the alpha

        mode: int
            Either RGB or HSB, corresponding to Red/Green/Blue and Hue/Saturation/Brightness

        Notes
        -----

        Changes the way py5 interprets color data. By default, the parameters for
        ``Py5Graphics.fill()``, ``Py5Graphics.stroke()``, ``Py5Graphics.background()``,
        and ``Py5Graphics.color()`` are defined by values between 0 and 255 using the
        ``RGB`` color model. The ``color_mode()`` function is used to change the
        numerical range used for specifying colors and to switch color systems. For
        example, calling ``color_mode(RGB, 1.0)`` will specify that values are specified
        between 0 and 1. The limits for defining colors are altered by setting the
        parameters ``max``, ``max1``, ``max2``, ``max3``, and ``max_a``.

        After changing the range of values for colors with code like ``color_mode(HSB,
        360, 100, 100)``, those ranges remain in use until they are explicitly changed
        again. For example, after running ``color_mode(HSB, 360, 100, 100)`` and then
        changing back to ``color_mode(RGB)``, the range for R will be 0 to 360 and the
        range for G and B will be 0 to 100. To avoid this, be explicit about the ranges
        when changing the color mode. For instance, instead of ``color_mode(RGB)``,
        write ``color_mode(RGB, 255, 255, 255)``.

        This method is the same as ``color_mode()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``color_mode()``.
        """
        pass

    @overload
    def color_mode(self, mode: int, max1: float,
                   max2: float, max3: float, /) -> None:
        """Changes the way py5 interprets color data.

        Underlying Java method: PGraphics.colorMode

        Methods
        -------

        You can use any of the following signatures:

         * color_mode(mode: int, /) -> None
         * color_mode(mode: int, max1: float, max2: float, max3: float, /) -> None
         * color_mode(mode: int, max1: float, max2: float, max3: float, max_a: float, /) -> None
         * color_mode(mode: int, max: float, /) -> None

        Parameters
        ----------

        max1: float
            range for the red or hue depending on the current color mode

        max2: float
            range for the green or saturation depending on the current color mode

        max3: float
            range for the blue or brightness depending on the current color mode

        max: float
            range for all color elements

        max_a: float
            range for the alpha

        mode: int
            Either RGB or HSB, corresponding to Red/Green/Blue and Hue/Saturation/Brightness

        Notes
        -----

        Changes the way py5 interprets color data. By default, the parameters for
        ``Py5Graphics.fill()``, ``Py5Graphics.stroke()``, ``Py5Graphics.background()``,
        and ``Py5Graphics.color()`` are defined by values between 0 and 255 using the
        ``RGB`` color model. The ``color_mode()`` function is used to change the
        numerical range used for specifying colors and to switch color systems. For
        example, calling ``color_mode(RGB, 1.0)`` will specify that values are specified
        between 0 and 1. The limits for defining colors are altered by setting the
        parameters ``max``, ``max1``, ``max2``, ``max3``, and ``max_a``.

        After changing the range of values for colors with code like ``color_mode(HSB,
        360, 100, 100)``, those ranges remain in use until they are explicitly changed
        again. For example, after running ``color_mode(HSB, 360, 100, 100)`` and then
        changing back to ``color_mode(RGB)``, the range for R will be 0 to 360 and the
        range for G and B will be 0 to 100. To avoid this, be explicit about the ranges
        when changing the color mode. For instance, instead of ``color_mode(RGB)``,
        write ``color_mode(RGB, 255, 255, 255)``.

        This method is the same as ``color_mode()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``color_mode()``.
        """
        pass

    @overload
    def color_mode(self, mode: int, max1: float, max2: float,
                   max3: float, max_a: float, /) -> None:
        """Changes the way py5 interprets color data.

        Underlying Java method: PGraphics.colorMode

        Methods
        -------

        You can use any of the following signatures:

         * color_mode(mode: int, /) -> None
         * color_mode(mode: int, max1: float, max2: float, max3: float, /) -> None
         * color_mode(mode: int, max1: float, max2: float, max3: float, max_a: float, /) -> None
         * color_mode(mode: int, max: float, /) -> None

        Parameters
        ----------

        max1: float
            range for the red or hue depending on the current color mode

        max2: float
            range for the green or saturation depending on the current color mode

        max3: float
            range for the blue or brightness depending on the current color mode

        max: float
            range for all color elements

        max_a: float
            range for the alpha

        mode: int
            Either RGB or HSB, corresponding to Red/Green/Blue and Hue/Saturation/Brightness

        Notes
        -----

        Changes the way py5 interprets color data. By default, the parameters for
        ``Py5Graphics.fill()``, ``Py5Graphics.stroke()``, ``Py5Graphics.background()``,
        and ``Py5Graphics.color()`` are defined by values between 0 and 255 using the
        ``RGB`` color model. The ``color_mode()`` function is used to change the
        numerical range used for specifying colors and to switch color systems. For
        example, calling ``color_mode(RGB, 1.0)`` will specify that values are specified
        between 0 and 1. The limits for defining colors are altered by setting the
        parameters ``max``, ``max1``, ``max2``, ``max3``, and ``max_a``.

        After changing the range of values for colors with code like ``color_mode(HSB,
        360, 100, 100)``, those ranges remain in use until they are explicitly changed
        again. For example, after running ``color_mode(HSB, 360, 100, 100)`` and then
        changing back to ``color_mode(RGB)``, the range for R will be 0 to 360 and the
        range for G and B will be 0 to 100. To avoid this, be explicit about the ranges
        when changing the color mode. For instance, instead of ``color_mode(RGB)``,
        write ``color_mode(RGB, 255, 255, 255)``.

        This method is the same as ``color_mode()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``color_mode()``.
        """
        pass

    def color_mode(self, *args):
        """Changes the way py5 interprets color data.

        Underlying Java method: PGraphics.colorMode

        Methods
        -------

        You can use any of the following signatures:

         * color_mode(mode: int, /) -> None
         * color_mode(mode: int, max1: float, max2: float, max3: float, /) -> None
         * color_mode(mode: int, max1: float, max2: float, max3: float, max_a: float, /) -> None
         * color_mode(mode: int, max: float, /) -> None

        Parameters
        ----------

        max1: float
            range for the red or hue depending on the current color mode

        max2: float
            range for the green or saturation depending on the current color mode

        max3: float
            range for the blue or brightness depending on the current color mode

        max: float
            range for all color elements

        max_a: float
            range for the alpha

        mode: int
            Either RGB or HSB, corresponding to Red/Green/Blue and Hue/Saturation/Brightness

        Notes
        -----

        Changes the way py5 interprets color data. By default, the parameters for
        ``Py5Graphics.fill()``, ``Py5Graphics.stroke()``, ``Py5Graphics.background()``,
        and ``Py5Graphics.color()`` are defined by values between 0 and 255 using the
        ``RGB`` color model. The ``color_mode()`` function is used to change the
        numerical range used for specifying colors and to switch color systems. For
        example, calling ``color_mode(RGB, 1.0)`` will specify that values are specified
        between 0 and 1. The limits for defining colors are altered by setting the
        parameters ``max``, ``max1``, ``max2``, ``max3``, and ``max_a``.

        After changing the range of values for colors with code like ``color_mode(HSB,
        360, 100, 100)``, those ranges remain in use until they are explicitly changed
        again. For example, after running ``color_mode(HSB, 360, 100, 100)`` and then
        changing back to ``color_mode(RGB)``, the range for R will be 0 to 360 and the
        range for G and B will be 0 to 100. To avoid this, be explicit about the ranges
        when changing the color mode. For instance, instead of ``color_mode(RGB)``,
        write ``color_mode(RGB, 255, 255, 255)``.

        This method is the same as ``color_mode()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``color_mode()``.
        """
        return self._instance.colorMode(*args)

    @overload
    def copy(self) -> Py5Image:
        """Copies a region of pixels from the ``Py5Graphics`` object to another area of the
        canvas and copies a region of pixels from an image used as the ``src_img``
        parameter into the ``Py5Graphics`` object.

        Underlying Java method: PGraphics.copy

        Methods
        -------

        You can use any of the following signatures:

         * copy() -> Py5Image
         * copy(src: Py5Image, sx: int, sy: int, sw: int, sh: int, dx: int, dy: int, dw: int, dh: int, /) -> None
         * copy(sx: int, sy: int, sw: int, sh: int, dx: int, dy: int, dw: int, dh: int, /) -> None

        Parameters
        ----------

        dh: int
            destination image height

        dw: int
            destination image width

        dx: int
            x-coordinate of the destination's upper left corner

        dy: int
            y-coordinate of the destination's upper left corner

        sh: int
            source image height

        src: Py5Image
            an image variable referring to the source image

        sw: int
            source image width

        sx: int
            x-coordinate of the source's upper left corner

        sy: int
            y-coordinate of the source's upper left corner

        Notes
        -----

        Copies a region of pixels from the ``Py5Graphics`` object to another area of the
        canvas and copies a region of pixels from an image used as the ``src_img``
        parameter into the ``Py5Graphics`` object. If the source and destination regions
        aren't the same size, it will automatically resize the source pixels to fit the
        specified target region. No alpha information is used in the process, however if
        the source image has an alpha channel set, it will be copied as well.

        This function ignores ``Py5Graphics.image_mode()``.

        This method is the same as ``copy()`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``copy()``.
        """
        pass

    @overload
    def copy(self, sx: int, sy: int, sw: int, sh: int,
             dx: int, dy: int, dw: int, dh: int, /) -> None:
        """Copies a region of pixels from the ``Py5Graphics`` object to another area of the
        canvas and copies a region of pixels from an image used as the ``src_img``
        parameter into the ``Py5Graphics`` object.

        Underlying Java method: PGraphics.copy

        Methods
        -------

        You can use any of the following signatures:

         * copy() -> Py5Image
         * copy(src: Py5Image, sx: int, sy: int, sw: int, sh: int, dx: int, dy: int, dw: int, dh: int, /) -> None
         * copy(sx: int, sy: int, sw: int, sh: int, dx: int, dy: int, dw: int, dh: int, /) -> None

        Parameters
        ----------

        dh: int
            destination image height

        dw: int
            destination image width

        dx: int
            x-coordinate of the destination's upper left corner

        dy: int
            y-coordinate of the destination's upper left corner

        sh: int
            source image height

        src: Py5Image
            an image variable referring to the source image

        sw: int
            source image width

        sx: int
            x-coordinate of the source's upper left corner

        sy: int
            y-coordinate of the source's upper left corner

        Notes
        -----

        Copies a region of pixels from the ``Py5Graphics`` object to another area of the
        canvas and copies a region of pixels from an image used as the ``src_img``
        parameter into the ``Py5Graphics`` object. If the source and destination regions
        aren't the same size, it will automatically resize the source pixels to fit the
        specified target region. No alpha information is used in the process, however if
        the source image has an alpha channel set, it will be copied as well.

        This function ignores ``Py5Graphics.image_mode()``.

        This method is the same as ``copy()`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``copy()``.
        """
        pass

    @overload
    def copy(self, src: Py5Image, sx: int, sy: int, sw: int,
             sh: int, dx: int, dy: int, dw: int, dh: int, /) -> None:
        """Copies a region of pixels from the ``Py5Graphics`` object to another area of the
        canvas and copies a region of pixels from an image used as the ``src_img``
        parameter into the ``Py5Graphics`` object.

        Underlying Java method: PGraphics.copy

        Methods
        -------

        You can use any of the following signatures:

         * copy() -> Py5Image
         * copy(src: Py5Image, sx: int, sy: int, sw: int, sh: int, dx: int, dy: int, dw: int, dh: int, /) -> None
         * copy(sx: int, sy: int, sw: int, sh: int, dx: int, dy: int, dw: int, dh: int, /) -> None

        Parameters
        ----------

        dh: int
            destination image height

        dw: int
            destination image width

        dx: int
            x-coordinate of the destination's upper left corner

        dy: int
            y-coordinate of the destination's upper left corner

        sh: int
            source image height

        src: Py5Image
            an image variable referring to the source image

        sw: int
            source image width

        sx: int
            x-coordinate of the source's upper left corner

        sy: int
            y-coordinate of the source's upper left corner

        Notes
        -----

        Copies a region of pixels from the ``Py5Graphics`` object to another area of the
        canvas and copies a region of pixels from an image used as the ``src_img``
        parameter into the ``Py5Graphics`` object. If the source and destination regions
        aren't the same size, it will automatically resize the source pixels to fit the
        specified target region. No alpha information is used in the process, however if
        the source image has an alpha channel set, it will be copied as well.

        This function ignores ``Py5Graphics.image_mode()``.

        This method is the same as ``copy()`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``copy()``.
        """
        pass

    @_return_py5image
    def copy(self, *args):
        """Copies a region of pixels from the ``Py5Graphics`` object to another area of the
        canvas and copies a region of pixels from an image used as the ``src_img``
        parameter into the ``Py5Graphics`` object.

        Underlying Java method: PGraphics.copy

        Methods
        -------

        You can use any of the following signatures:

         * copy() -> Py5Image
         * copy(src: Py5Image, sx: int, sy: int, sw: int, sh: int, dx: int, dy: int, dw: int, dh: int, /) -> None
         * copy(sx: int, sy: int, sw: int, sh: int, dx: int, dy: int, dw: int, dh: int, /) -> None

        Parameters
        ----------

        dh: int
            destination image height

        dw: int
            destination image width

        dx: int
            x-coordinate of the destination's upper left corner

        dy: int
            y-coordinate of the destination's upper left corner

        sh: int
            source image height

        src: Py5Image
            an image variable referring to the source image

        sw: int
            source image width

        sx: int
            x-coordinate of the source's upper left corner

        sy: int
            y-coordinate of the source's upper left corner

        Notes
        -----

        Copies a region of pixels from the ``Py5Graphics`` object to another area of the
        canvas and copies a region of pixels from an image used as the ``src_img``
        parameter into the ``Py5Graphics`` object. If the source and destination regions
        aren't the same size, it will automatically resize the source pixels to fit the
        specified target region. No alpha information is used in the process, however if
        the source image has an alpha channel set, it will be copied as well.

        This function ignores ``Py5Graphics.image_mode()``.

        This method is the same as ``copy()`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``copy()``.
        """
        return self._instance.copy(*args)

    @overload
    def create_shape(self) -> Py5Shape:
        """The ``create_shape()`` function is used to define a new shape.

        Underlying Java method: PGraphics.createShape

        Methods
        -------

        You can use any of the following signatures:

         * create_shape() -> Py5Shape
         * create_shape(kind: int, /, *p: float) -> Py5Shape
         * create_shape(type: int, /) -> Py5Shape

        Parameters
        ----------

        kind: int
            either POINT, LINE, TRIANGLE, QUAD, RECT, ELLIPSE, ARC, BOX, SPHERE

        p: float
            parameters that match the kind of shape

        type: int
            either GROUP, PATH, or GEOMETRY

        Notes
        -----

        The ``create_shape()`` function is used to define a new shape. Once created,
        this shape can be drawn with the ``Py5Graphics.shape()`` function. The basic way
        to use the function defines new primitive shapes. One of the following
        parameters are used as the first parameter: ``ELLIPSE``, ``RECT``, ``ARC``,
        ``TRIANGLE``, ``SPHERE``, ``BOX``, ``QUAD``, or ``LINE``. The parameters for
        each of these different shapes are the same as their corresponding functions:
        ``Py5Graphics.ellipse()``, ``Py5Graphics.rect()``, ``Py5Graphics.arc()``,
        ``Py5Graphics.triangle()``, ``Py5Graphics.sphere()``, ``Py5Graphics.box()``,
        ``Py5Graphics.quad()``, and ``Py5Graphics.line()``.

        Custom, unique shapes can be made by using ``create_shape()`` without a
        parameter. After the shape is started, the drawing attributes and geometry can
        be set directly to the shape within the ``Py5Graphics.begin_shape()`` and
        ``Py5Graphics.end_shape()`` methods. See reference for
        ``Py5Graphics.begin_shape()`` for all of its options.

        The  ``create_shape()`` function can also be used to make a complex shape made
        of other shapes. This is called a "group" and it's created by using the
        parameter ``GROUP`` as the first parameter.

        After using ``create_shape()``, stroke and fill color can be set by calling
        methods like ``Py5Shape.set_fill()`` and ``Py5Shape.set_stroke()``, as seen in
        the examples. The complete list of methods and fields for the ``Py5Shape`` class
        are in the py5 documentation.

        This method is the same as ``create_shape()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``create_shape()``.
        """
        pass

    @overload
    def create_shape(self, type: int, /) -> Py5Shape:
        """The ``create_shape()`` function is used to define a new shape.

        Underlying Java method: PGraphics.createShape

        Methods
        -------

        You can use any of the following signatures:

         * create_shape() -> Py5Shape
         * create_shape(kind: int, /, *p: float) -> Py5Shape
         * create_shape(type: int, /) -> Py5Shape

        Parameters
        ----------

        kind: int
            either POINT, LINE, TRIANGLE, QUAD, RECT, ELLIPSE, ARC, BOX, SPHERE

        p: float
            parameters that match the kind of shape

        type: int
            either GROUP, PATH, or GEOMETRY

        Notes
        -----

        The ``create_shape()`` function is used to define a new shape. Once created,
        this shape can be drawn with the ``Py5Graphics.shape()`` function. The basic way
        to use the function defines new primitive shapes. One of the following
        parameters are used as the first parameter: ``ELLIPSE``, ``RECT``, ``ARC``,
        ``TRIANGLE``, ``SPHERE``, ``BOX``, ``QUAD``, or ``LINE``. The parameters for
        each of these different shapes are the same as their corresponding functions:
        ``Py5Graphics.ellipse()``, ``Py5Graphics.rect()``, ``Py5Graphics.arc()``,
        ``Py5Graphics.triangle()``, ``Py5Graphics.sphere()``, ``Py5Graphics.box()``,
        ``Py5Graphics.quad()``, and ``Py5Graphics.line()``.

        Custom, unique shapes can be made by using ``create_shape()`` without a
        parameter. After the shape is started, the drawing attributes and geometry can
        be set directly to the shape within the ``Py5Graphics.begin_shape()`` and
        ``Py5Graphics.end_shape()`` methods. See reference for
        ``Py5Graphics.begin_shape()`` for all of its options.

        The  ``create_shape()`` function can also be used to make a complex shape made
        of other shapes. This is called a "group" and it's created by using the
        parameter ``GROUP`` as the first parameter.

        After using ``create_shape()``, stroke and fill color can be set by calling
        methods like ``Py5Shape.set_fill()`` and ``Py5Shape.set_stroke()``, as seen in
        the examples. The complete list of methods and fields for the ``Py5Shape`` class
        are in the py5 documentation.

        This method is the same as ``create_shape()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``create_shape()``.
        """
        pass

    @overload
    def create_shape(self, kind: int, /, *p: float) -> Py5Shape:
        """The ``create_shape()`` function is used to define a new shape.

        Underlying Java method: PGraphics.createShape

        Methods
        -------

        You can use any of the following signatures:

         * create_shape() -> Py5Shape
         * create_shape(kind: int, /, *p: float) -> Py5Shape
         * create_shape(type: int, /) -> Py5Shape

        Parameters
        ----------

        kind: int
            either POINT, LINE, TRIANGLE, QUAD, RECT, ELLIPSE, ARC, BOX, SPHERE

        p: float
            parameters that match the kind of shape

        type: int
            either GROUP, PATH, or GEOMETRY

        Notes
        -----

        The ``create_shape()`` function is used to define a new shape. Once created,
        this shape can be drawn with the ``Py5Graphics.shape()`` function. The basic way
        to use the function defines new primitive shapes. One of the following
        parameters are used as the first parameter: ``ELLIPSE``, ``RECT``, ``ARC``,
        ``TRIANGLE``, ``SPHERE``, ``BOX``, ``QUAD``, or ``LINE``. The parameters for
        each of these different shapes are the same as their corresponding functions:
        ``Py5Graphics.ellipse()``, ``Py5Graphics.rect()``, ``Py5Graphics.arc()``,
        ``Py5Graphics.triangle()``, ``Py5Graphics.sphere()``, ``Py5Graphics.box()``,
        ``Py5Graphics.quad()``, and ``Py5Graphics.line()``.

        Custom, unique shapes can be made by using ``create_shape()`` without a
        parameter. After the shape is started, the drawing attributes and geometry can
        be set directly to the shape within the ``Py5Graphics.begin_shape()`` and
        ``Py5Graphics.end_shape()`` methods. See reference for
        ``Py5Graphics.begin_shape()`` for all of its options.

        The  ``create_shape()`` function can also be used to make a complex shape made
        of other shapes. This is called a "group" and it's created by using the
        parameter ``GROUP`` as the first parameter.

        After using ``create_shape()``, stroke and fill color can be set by calling
        methods like ``Py5Shape.set_fill()`` and ``Py5Shape.set_stroke()``, as seen in
        the examples. The complete list of methods and fields for the ``Py5Shape`` class
        are in the py5 documentation.

        This method is the same as ``create_shape()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``create_shape()``.
        """
        pass

    @_return_py5shape
    def create_shape(self, *args):
        """The ``create_shape()`` function is used to define a new shape.

        Underlying Java method: PGraphics.createShape

        Methods
        -------

        You can use any of the following signatures:

         * create_shape() -> Py5Shape
         * create_shape(kind: int, /, *p: float) -> Py5Shape
         * create_shape(type: int, /) -> Py5Shape

        Parameters
        ----------

        kind: int
            either POINT, LINE, TRIANGLE, QUAD, RECT, ELLIPSE, ARC, BOX, SPHERE

        p: float
            parameters that match the kind of shape

        type: int
            either GROUP, PATH, or GEOMETRY

        Notes
        -----

        The ``create_shape()`` function is used to define a new shape. Once created,
        this shape can be drawn with the ``Py5Graphics.shape()`` function. The basic way
        to use the function defines new primitive shapes. One of the following
        parameters are used as the first parameter: ``ELLIPSE``, ``RECT``, ``ARC``,
        ``TRIANGLE``, ``SPHERE``, ``BOX``, ``QUAD``, or ``LINE``. The parameters for
        each of these different shapes are the same as their corresponding functions:
        ``Py5Graphics.ellipse()``, ``Py5Graphics.rect()``, ``Py5Graphics.arc()``,
        ``Py5Graphics.triangle()``, ``Py5Graphics.sphere()``, ``Py5Graphics.box()``,
        ``Py5Graphics.quad()``, and ``Py5Graphics.line()``.

        Custom, unique shapes can be made by using ``create_shape()`` without a
        parameter. After the shape is started, the drawing attributes and geometry can
        be set directly to the shape within the ``Py5Graphics.begin_shape()`` and
        ``Py5Graphics.end_shape()`` methods. See reference for
        ``Py5Graphics.begin_shape()`` for all of its options.

        The  ``create_shape()`` function can also be used to make a complex shape made
        of other shapes. This is called a "group" and it's created by using the
        parameter ``GROUP`` as the first parameter.

        After using ``create_shape()``, stroke and fill color can be set by calling
        methods like ``Py5Shape.set_fill()`` and ``Py5Shape.set_stroke()``, as seen in
        the examples. The complete list of methods and fields for the ``Py5Shape`` class
        are in the py5 documentation.

        This method is the same as ``create_shape()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``create_shape()``.
        """
        return self._instance.createShape(*args)

    @overload
    def curve(self, x1: float, y1: float, x2: float, y2: float,
              x3: float, y3: float, x4: float, y4: float, /) -> None:
        """Draws a curved line on the ``Py5Graphics`` object.

        Underlying Java method: PGraphics.curve

        Methods
        -------

        You can use any of the following signatures:

         * curve(x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, /) -> None
         * curve(x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, x3: float, y3: float, z3: float, x4: float, y4: float, z4: float, /) -> None

        Parameters
        ----------

        x1: float
            coordinates for the beginning control point

        x2: float
            coordinates for the first point

        x3: float
            coordinates for the second point

        x4: float
            coordinates for the ending control point

        y1: float
            coordinates for the beginning control point

        y2: float
            coordinates for the first point

        y3: float
            coordinates for the second point

        y4: float
            coordinates for the ending control point

        z1: float
            coordinates for the beginning control point

        z2: float
            coordinates for the first point

        z3: float
            coordinates for the second point

        z4: float
            coordinates for the ending control point

        Notes
        -----

        Draws a curved line on the ``Py5Graphics`` object. The first and second
        parameters specify the beginning control point and the last two parameters
        specify the ending control point. The middle parameters specify the start and
        stop of the curve. Longer curves can be created by putting a series of
        ``curve()`` functions together or using ``Py5Graphics.curve_vertex()``. An
        additional function called ``Py5Graphics.curve_tightness()`` provides control
        for the visual quality of the curve. The ``curve()`` function is an
        implementation of Catmull-Rom splines. Using the 3D version requires rendering
        with ``P3D``.

        This method is the same as ``curve()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``curve()``.
        """
        pass

    @overload
    def curve(self, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float,
              x3: float, y3: float, z3: float, x4: float, y4: float, z4: float, /) -> None:
        """Draws a curved line on the ``Py5Graphics`` object.

        Underlying Java method: PGraphics.curve

        Methods
        -------

        You can use any of the following signatures:

         * curve(x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, /) -> None
         * curve(x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, x3: float, y3: float, z3: float, x4: float, y4: float, z4: float, /) -> None

        Parameters
        ----------

        x1: float
            coordinates for the beginning control point

        x2: float
            coordinates for the first point

        x3: float
            coordinates for the second point

        x4: float
            coordinates for the ending control point

        y1: float
            coordinates for the beginning control point

        y2: float
            coordinates for the first point

        y3: float
            coordinates for the second point

        y4: float
            coordinates for the ending control point

        z1: float
            coordinates for the beginning control point

        z2: float
            coordinates for the first point

        z3: float
            coordinates for the second point

        z4: float
            coordinates for the ending control point

        Notes
        -----

        Draws a curved line on the ``Py5Graphics`` object. The first and second
        parameters specify the beginning control point and the last two parameters
        specify the ending control point. The middle parameters specify the start and
        stop of the curve. Longer curves can be created by putting a series of
        ``curve()`` functions together or using ``Py5Graphics.curve_vertex()``. An
        additional function called ``Py5Graphics.curve_tightness()`` provides control
        for the visual quality of the curve. The ``curve()`` function is an
        implementation of Catmull-Rom splines. Using the 3D version requires rendering
        with ``P3D``.

        This method is the same as ``curve()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``curve()``.
        """
        pass

    def curve(self, *args):
        """Draws a curved line on the ``Py5Graphics`` object.

        Underlying Java method: PGraphics.curve

        Methods
        -------

        You can use any of the following signatures:

         * curve(x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, /) -> None
         * curve(x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, x3: float, y3: float, z3: float, x4: float, y4: float, z4: float, /) -> None

        Parameters
        ----------

        x1: float
            coordinates for the beginning control point

        x2: float
            coordinates for the first point

        x3: float
            coordinates for the second point

        x4: float
            coordinates for the ending control point

        y1: float
            coordinates for the beginning control point

        y2: float
            coordinates for the first point

        y3: float
            coordinates for the second point

        y4: float
            coordinates for the ending control point

        z1: float
            coordinates for the beginning control point

        z2: float
            coordinates for the first point

        z3: float
            coordinates for the second point

        z4: float
            coordinates for the ending control point

        Notes
        -----

        Draws a curved line on the ``Py5Graphics`` object. The first and second
        parameters specify the beginning control point and the last two parameters
        specify the ending control point. The middle parameters specify the start and
        stop of the curve. Longer curves can be created by putting a series of
        ``curve()`` functions together or using ``Py5Graphics.curve_vertex()``. An
        additional function called ``Py5Graphics.curve_tightness()`` provides control
        for the visual quality of the curve. The ``curve()`` function is an
        implementation of Catmull-Rom splines. Using the 3D version requires rendering
        with ``P3D``.

        This method is the same as ``curve()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``curve()``.
        """
        return self._instance.curve(*args)

    def curve_detail(self, detail: int, /) -> None:
        """Sets the resolution at which curves display.

        Underlying Java method: PGraphics.curveDetail

        Parameters
        ----------

        detail: int
            resolution of the curves

        Notes
        -----

        Sets the resolution at which curves display. The default value is 20. This
        function is only useful when using the ``P3D`` renderer as the default ``P2D``
        renderer does not use this information.

        This method is the same as ``curve_detail()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``curve_detail()``.
        """
        return self._instance.curveDetail(detail)

    def curve_point(self, a: float, b: float, c: float,
                    d: float, t: float, /) -> float:
        """Evaluates the curve at point ``t`` for points ``a``, ``b``, ``c``, ``d``.

        Underlying Java method: PGraphics.curvePoint

        Parameters
        ----------

        a: float
            coordinate of first control point

        b: float
            coordinate of first point on the curve

        c: float
            coordinate of second point on the curve

        d: float
            coordinate of second control point

        t: float
            value between 0 and 1

        Notes
        -----

        Evaluates the curve at point ``t`` for points ``a``, ``b``, ``c``, ``d``. The
        parameter ``t`` may range from 0 (the start of the curve) and 1 (the end of the
        curve). ``a`` and ``d`` are the control points, and ``b`` and ``c`` are points
        on the curve. As seen in the example, this can be used once with the ``x``
        coordinates and a second time with the ``y`` coordinates to get the location of
        a curve at ``t``.

        This method is the same as ``curve_point()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``curve_point()``.
        """
        return self._instance.curvePoint(a, b, c, d, t)

    def curve_tangent(self, a: float, b: float, c: float,
                      d: float, t: float, /) -> float:
        """Calculates the tangent of a point on a curve.

        Underlying Java method: PGraphics.curveTangent

        Parameters
        ----------

        a: float
            coordinate of first point on the curve

        b: float
            coordinate of first control point

        c: float
            coordinate of second control point

        d: float
            coordinate of second point on the curve

        t: float
            value between 0 and 1

        Notes
        -----

        Calculates the tangent of a point on a curve. There's a good definition of
        *tangent* on Wikipedia.

        This method is the same as ``curve_tangent()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``curve_tangent()``.
        """
        return self._instance.curveTangent(a, b, c, d, t)

    def curve_tightness(self, tightness: float, /) -> None:
        """Modifies the quality of forms created with ``Py5Graphics.curve()`` and
        ``Py5Graphics.curve_vertex()``.

        Underlying Java method: PGraphics.curveTightness

        Parameters
        ----------

        tightness: float
            amount of deformation from the original vertices

        Notes
        -----

        Modifies the quality of forms created with ``Py5Graphics.curve()`` and
        ``Py5Graphics.curve_vertex()``. The parameter ``tightness`` determines how the
        curve fits to the vertex points. The value 0.0 is the default value for
        ``tightness`` (this value defines the curves to be Catmull-Rom splines) and the
        value 1.0 connects all the points with straight lines. Values within the range
        -5.0 and 5.0 will deform the curves but will leave them recognizable and as
        values increase in magnitude, they will continue to deform.

        This method is the same as ``curve_tightness()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``curve_tightness()``.
        """
        return self._instance.curveTightness(tightness)

    @overload
    def curve_vertex(self, x: float, y: float, /) -> None:
        """Specifies vertex coordinates for curves.

        Underlying Java method: PGraphics.curveVertex

        Methods
        -------

        You can use any of the following signatures:

         * curve_vertex(x: float, y: float, /) -> None
         * curve_vertex(x: float, y: float, z: float, /) -> None

        Parameters
        ----------

        x: float
            the x-coordinate of the vertex

        y: float
            the y-coordinate of the vertex

        z: float
            the z-coordinate of the vertex

        Notes
        -----

        Specifies vertex coordinates for curves. This method may only be used between
        ``Py5Graphics.begin_shape()`` and ``Py5Graphics.end_shape()`` and only when
        there is no ``MODE`` parameter specified to ``Py5Graphics.begin_shape()``. The
        first and last points in a series of ``curve_vertex()`` lines will be used to
        guide the beginning and end of the curve. A minimum of four points is required
        to draw a tiny curve between the second and third points. Adding a fifth point
        with ``curve_vertex()`` will draw the curve between the second, third, and
        fourth points. The ``curve_vertex()`` method is an implementation of Catmull-Rom
        splines. Using the 3D version requires rendering with ``P3D``.

        This method is the same as ``curve_vertex()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``curve_vertex()``.
        """
        pass

    @overload
    def curve_vertex(self, x: float, y: float, z: float, /) -> None:
        """Specifies vertex coordinates for curves.

        Underlying Java method: PGraphics.curveVertex

        Methods
        -------

        You can use any of the following signatures:

         * curve_vertex(x: float, y: float, /) -> None
         * curve_vertex(x: float, y: float, z: float, /) -> None

        Parameters
        ----------

        x: float
            the x-coordinate of the vertex

        y: float
            the y-coordinate of the vertex

        z: float
            the z-coordinate of the vertex

        Notes
        -----

        Specifies vertex coordinates for curves. This method may only be used between
        ``Py5Graphics.begin_shape()`` and ``Py5Graphics.end_shape()`` and only when
        there is no ``MODE`` parameter specified to ``Py5Graphics.begin_shape()``. The
        first and last points in a series of ``curve_vertex()`` lines will be used to
        guide the beginning and end of the curve. A minimum of four points is required
        to draw a tiny curve between the second and third points. Adding a fifth point
        with ``curve_vertex()`` will draw the curve between the second, third, and
        fourth points. The ``curve_vertex()`` method is an implementation of Catmull-Rom
        splines. Using the 3D version requires rendering with ``P3D``.

        This method is the same as ``curve_vertex()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``curve_vertex()``.
        """
        pass

    def curve_vertex(self, *args):
        """Specifies vertex coordinates for curves.

        Underlying Java method: PGraphics.curveVertex

        Methods
        -------

        You can use any of the following signatures:

         * curve_vertex(x: float, y: float, /) -> None
         * curve_vertex(x: float, y: float, z: float, /) -> None

        Parameters
        ----------

        x: float
            the x-coordinate of the vertex

        y: float
            the y-coordinate of the vertex

        z: float
            the z-coordinate of the vertex

        Notes
        -----

        Specifies vertex coordinates for curves. This method may only be used between
        ``Py5Graphics.begin_shape()`` and ``Py5Graphics.end_shape()`` and only when
        there is no ``MODE`` parameter specified to ``Py5Graphics.begin_shape()``. The
        first and last points in a series of ``curve_vertex()`` lines will be used to
        guide the beginning and end of the curve. A minimum of four points is required
        to draw a tiny curve between the second and third points. Adding a fifth point
        with ``curve_vertex()`` will draw the curve between the second, third, and
        fourth points. The ``curve_vertex()`` method is an implementation of Catmull-Rom
        splines. Using the 3D version requires rendering with ``P3D``.

        This method is the same as ``curve_vertex()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``curve_vertex()``.
        """
        return self._instance.curveVertex(*args)

    def directional_light(self, v1: float, v2: float, v3: float,
                          nx: float, ny: float, nz: float, /) -> None:
        """Adds a directional light.

        Underlying Java method: PGraphics.directionalLight

        Parameters
        ----------

        nx: float
            direction along the x-axis

        ny: float
            direction along the y-axis

        nz: float
            direction along the z-axis

        v1: float
            red or hue value (depending on current color mode)

        v2: float
            green or saturation value (depending on current color mode)

        v3: float
            blue or brightness value (depending on current color mode)

        Notes
        -----

        Adds a directional light. Directional light comes from one direction: it is
        stronger when hitting a surface squarely, and weaker if it hits at a gentle
        angle. After hitting a surface, directional light scatters in all directions.
        Lights need to be included in the ``draw()`` to remain persistent in a looping
        program. Placing them in the ``setup()`` of a looping program will cause them to
        only have an effect the first time through the loop. The ``v1``, ``v2``, and
        ``v3`` parameters are interpreted as either ``RGB`` or ``HSB`` values, depending
        on the current color mode. The ``nx``, ``ny``, and ``nz`` parameters specify the
        direction the light is facing. For example, setting ``ny`` to -1 will cause the
        geometry to be lit from below (since the light would be facing directly upward).

        This method is the same as ``directional_light()`` but linked to a
        ``Py5Graphics`` object. To see example code for how it can be used, see
        ``directional_light()``.
        """
        return self._instance.directionalLight(v1, v2, v3, nx, ny, nz)

    def ellipse(self, a: float, b: float, c: float, d: float, /) -> None:
        """Draws an ellipse (oval) to the screen.

        Underlying Java method: PGraphics.ellipse

        Parameters
        ----------

        a: float
            x-coordinate of the ellipse

        b: float
            y-coordinate of the ellipse

        c: float
            width of the ellipse by default

        d: float
            height of the ellipse by default

        Notes
        -----

        Draws an ellipse (oval) to the screen. An ellipse with equal width and height is
        a circle. By default, the first two parameters set the location, and the third
        and fourth parameters set the shape's width and height. The origin may be
        changed with the ``Py5Graphics.ellipse_mode()`` function.

        This method is the same as ``ellipse()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``ellipse()``.
        """
        return self._instance.ellipse(a, b, c, d)

    def ellipse_mode(self, mode: int, /) -> None:
        """Modifies the location from which ellipses are drawn by changing the way in which
        parameters given to ``Py5Graphics.ellipse()`` are intepreted.

        Underlying Java method: PGraphics.ellipseMode

        Parameters
        ----------

        mode: int
            either CENTER, RADIUS, CORNER, or CORNERS

        Notes
        -----

        Modifies the location from which ellipses are drawn by changing the way in which
        parameters given to ``Py5Graphics.ellipse()`` are intepreted.

        The default mode is ``ellipse_mode(CENTER)``, which interprets the first two
        parameters of ``Py5Graphics.ellipse()`` as the shape's center point, while the
        third and fourth parameters are its width and height.

        ``ellipse_mode(RADIUS)`` also uses the first two parameters of
        ``Py5Graphics.ellipse()`` as the shape's center point, but uses the third and
        fourth parameters to specify half of the shapes's width and height.

        ``ellipse_mode(CORNER)`` interprets the first two parameters of
        ``Py5Graphics.ellipse()`` as the upper-left corner of the shape, while the third
        and fourth parameters are its width and height.

        ``ellipse_mode(CORNERS)`` interprets the first two parameters of
        ``Py5Graphics.ellipse()`` as the location of one corner of the ellipse's
        bounding box, and the third and fourth parameters as the location of the
        opposite corner.

        The parameter must be written in ALL CAPS because Python is a case-sensitive
        language.

        This method is the same as ``ellipse_mode()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``ellipse_mode()``.
        """
        return self._instance.ellipseMode(mode)

    @overload
    def emissive(self, gray: float, /) -> None:
        """Sets the emissive color of the material used for drawing shapes drawn to the
        screen.

        Underlying Java method: PGraphics.emissive

        Methods
        -------

        You can use any of the following signatures:

         * emissive(gray: float, /) -> None
         * emissive(rgb: int, /) -> None
         * emissive(v1: float, v2: float, v3: float, /) -> None

        Parameters
        ----------

        gray: float
            value between black and white, by default 0 to 255

        rgb: int
            color to set

        v1: float
            red or hue value (depending on current color mode)

        v2: float
            green or saturation value (depending on current color mode)

        v3: float
            blue or brightness value (depending on current color mode)

        Notes
        -----

        Sets the emissive color of the material used for drawing shapes drawn to the
        screen. Use in combination with ``Py5Graphics.ambient()``,
        ``Py5Graphics.specular()``, and ``Py5Graphics.shininess()`` to set the material
        properties of shapes.

        This method is the same as ``emissive()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``emissive()``.
        """
        pass

    @overload
    def emissive(self, v1: float, v2: float, v3: float, /) -> None:
        """Sets the emissive color of the material used for drawing shapes drawn to the
        screen.

        Underlying Java method: PGraphics.emissive

        Methods
        -------

        You can use any of the following signatures:

         * emissive(gray: float, /) -> None
         * emissive(rgb: int, /) -> None
         * emissive(v1: float, v2: float, v3: float, /) -> None

        Parameters
        ----------

        gray: float
            value between black and white, by default 0 to 255

        rgb: int
            color to set

        v1: float
            red or hue value (depending on current color mode)

        v2: float
            green or saturation value (depending on current color mode)

        v3: float
            blue or brightness value (depending on current color mode)

        Notes
        -----

        Sets the emissive color of the material used for drawing shapes drawn to the
        screen. Use in combination with ``Py5Graphics.ambient()``,
        ``Py5Graphics.specular()``, and ``Py5Graphics.shininess()`` to set the material
        properties of shapes.

        This method is the same as ``emissive()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``emissive()``.
        """
        pass

    @overload
    def emissive(self, rgb: int, /) -> None:
        """Sets the emissive color of the material used for drawing shapes drawn to the
        screen.

        Underlying Java method: PGraphics.emissive

        Methods
        -------

        You can use any of the following signatures:

         * emissive(gray: float, /) -> None
         * emissive(rgb: int, /) -> None
         * emissive(v1: float, v2: float, v3: float, /) -> None

        Parameters
        ----------

        gray: float
            value between black and white, by default 0 to 255

        rgb: int
            color to set

        v1: float
            red or hue value (depending on current color mode)

        v2: float
            green or saturation value (depending on current color mode)

        v3: float
            blue or brightness value (depending on current color mode)

        Notes
        -----

        Sets the emissive color of the material used for drawing shapes drawn to the
        screen. Use in combination with ``Py5Graphics.ambient()``,
        ``Py5Graphics.specular()``, and ``Py5Graphics.shininess()`` to set the material
        properties of shapes.

        This method is the same as ``emissive()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``emissive()``.
        """
        pass

    def emissive(self, *args):
        """Sets the emissive color of the material used for drawing shapes drawn to the
        screen.

        Underlying Java method: PGraphics.emissive

        Methods
        -------

        You can use any of the following signatures:

         * emissive(gray: float, /) -> None
         * emissive(rgb: int, /) -> None
         * emissive(v1: float, v2: float, v3: float, /) -> None

        Parameters
        ----------

        gray: float
            value between black and white, by default 0 to 255

        rgb: int
            color to set

        v1: float
            red or hue value (depending on current color mode)

        v2: float
            green or saturation value (depending on current color mode)

        v3: float
            blue or brightness value (depending on current color mode)

        Notes
        -----

        Sets the emissive color of the material used for drawing shapes drawn to the
        screen. Use in combination with ``Py5Graphics.ambient()``,
        ``Py5Graphics.specular()``, and ``Py5Graphics.shininess()`` to set the material
        properties of shapes.

        This method is the same as ``emissive()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``emissive()``.
        """
        return self._instance.emissive(*args)

    def end_camera(self) -> None:
        """The ``Py5Graphics.begin_camera()`` and ``end_camera()`` methods enable advanced
        customization of the camera space.

        Underlying Java method: PGraphics.endCamera

        Notes
        -----

        The ``Py5Graphics.begin_camera()`` and ``end_camera()`` methods enable advanced
        customization of the camera space. Please see the reference for
        ``Py5Graphics.begin_camera()`` for a description of how the methods are used.

        This method is the same as ``end_camera()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``end_camera()``.
        """
        return self._instance.endCamera()

    def end_contour(self) -> None:
        """Use the ``Py5Graphics.begin_contour()`` and ``end_contour()`` methods to create
        negative shapes within shapes such as the center of the letter 'O'.

        Underlying Java method: PGraphics.endContour

        Notes
        -----

        Use the ``Py5Graphics.begin_contour()`` and ``end_contour()`` methods to create
        negative shapes within shapes such as the center of the letter 'O'. The
        ``Py5Graphics.begin_contour()`` method begins recording vertices for the shape
        and ``end_contour()`` stops recording. The vertices that define a negative shape
        must "wind" in the opposite direction from the exterior shape. First draw
        vertices for the exterior shape in clockwise order, then for internal shapes,
        draw vertices counterclockwise.

        These methods can only be used within a ``Py5Graphics.begin_shape()`` &
        ``Py5Graphics.end_shape()`` pair and transformations such as
        ``Py5Graphics.translate()``, ``Py5Graphics.rotate()``, and
        ``Py5Graphics.scale()`` do not work within a ``Py5Graphics.begin_contour()`` &
        ``end_contour()`` pair. It is also not possible to use other shapes, such as
        ``Py5Graphics.ellipse()`` or ``Py5Graphics.rect()`` within.

        This method is the same as ``end_contour()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``end_contour()``.
        """
        return self._instance.endContour()

    def end_draw(self) -> None:
        """Finalizes the rendering of a ``Py5Graphics`` object so that it can be shown on
        screen.

        Underlying Java method: PGraphics.endDraw

        Notes
        -----

        Finalizes the rendering of a ``Py5Graphics`` object so that it can be shown on
        screen.
        """
        return self._instance.endDraw()

    def end_raw(self) -> None:
        """Complement to ``Py5Graphics.begin_raw()``; they must always be used together.

        Underlying Java method: PGraphics.endRaw

        Notes
        -----

        Complement to ``Py5Graphics.begin_raw()``; they must always be used together.
        See the ``Py5Graphics.begin_raw()`` reference for details.

        This method is the same as ``end_raw()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``end_raw()``.
        """
        return self._instance.endRaw()

    @overload
    def end_shape(self) -> None:
        """The ``end_shape()`` function is the companion to ``Py5Graphics.begin_shape()``
        and may only be called after ``Py5Graphics.begin_shape()``.

        Underlying Java method: PGraphics.endShape

        Methods
        -------

        You can use any of the following signatures:

         * end_shape() -> None
         * end_shape(mode: int, /) -> None

        Parameters
        ----------

        mode: int
            use CLOSE to close the shape

        Notes
        -----

        The ``end_shape()`` function is the companion to ``Py5Graphics.begin_shape()``
        and may only be called after ``Py5Graphics.begin_shape()``. When ``end_shape()``
        is called, all of image data defined since the previous call to
        ``Py5Graphics.begin_shape()`` is written into the image buffer. The constant
        ``CLOSE`` as the value for the ``MODE`` parameter to close the shape (to connect
        the beginning and the end).

        This method is the same as ``end_shape()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``end_shape()``.
        """
        pass

    @overload
    def end_shape(self, mode: int, /) -> None:
        """The ``end_shape()`` function is the companion to ``Py5Graphics.begin_shape()``
        and may only be called after ``Py5Graphics.begin_shape()``.

        Underlying Java method: PGraphics.endShape

        Methods
        -------

        You can use any of the following signatures:

         * end_shape() -> None
         * end_shape(mode: int, /) -> None

        Parameters
        ----------

        mode: int
            use CLOSE to close the shape

        Notes
        -----

        The ``end_shape()`` function is the companion to ``Py5Graphics.begin_shape()``
        and may only be called after ``Py5Graphics.begin_shape()``. When ``end_shape()``
        is called, all of image data defined since the previous call to
        ``Py5Graphics.begin_shape()`` is written into the image buffer. The constant
        ``CLOSE`` as the value for the ``MODE`` parameter to close the shape (to connect
        the beginning and the end).

        This method is the same as ``end_shape()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``end_shape()``.
        """
        pass

    def end_shape(self, *args):
        """The ``end_shape()`` function is the companion to ``Py5Graphics.begin_shape()``
        and may only be called after ``Py5Graphics.begin_shape()``.

        Underlying Java method: PGraphics.endShape

        Methods
        -------

        You can use any of the following signatures:

         * end_shape() -> None
         * end_shape(mode: int, /) -> None

        Parameters
        ----------

        mode: int
            use CLOSE to close the shape

        Notes
        -----

        The ``end_shape()`` function is the companion to ``Py5Graphics.begin_shape()``
        and may only be called after ``Py5Graphics.begin_shape()``. When ``end_shape()``
        is called, all of image data defined since the previous call to
        ``Py5Graphics.begin_shape()`` is written into the image buffer. The constant
        ``CLOSE`` as the value for the ``MODE`` parameter to close the shape (to connect
        the beginning and the end).

        This method is the same as ``end_shape()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``end_shape()``.
        """
        return self._instance.endShape(*args)

    @overload
    def fill(self, gray: float, /) -> None:
        """Sets the color used to fill shapes.

        Underlying Java method: PGraphics.fill

        Methods
        -------

        You can use any of the following signatures:

         * fill(gray: float, /) -> None
         * fill(gray: float, alpha: float, /) -> None
         * fill(rgb: int, /) -> None
         * fill(rgb: int, alpha: float, /) -> None
         * fill(v1: float, v2: float, v3: float, /) -> None
         * fill(v1: float, v2: float, v3: float, alpha: float, /) -> None

        Parameters
        ----------

        alpha: float
            opacity of the fill

        gray: float
            number specifying value between white and black

        rgb: int
            color variable or hex value

        v1: float
            red or hue value (depending on current color mode)

        v2: float
            green or saturation value (depending on current color mode)

        v3: float
            blue or brightness value (depending on current color mode)

        Notes
        -----

        Sets the color used to fill shapes. For example, if you run ``fill(204, 102,
        0)``, all subsequent shapes will be filled with orange. This color is either
        specified in terms of the ``RGB`` or ``HSB`` color depending on the current
        ``Py5Graphics.color_mode()``. The default color space is ``RGB``, with each
        value in the range from 0 to 255.

        When using hexadecimal notation to specify a color, use "``0x``" before the
        values (e.g., ``0xFFCCFFAA``). The hexadecimal value must be specified with
        eight characters; the first two characters define the alpha component, and the
        remainder define the red, green, and blue components.

        The value for the "gray" parameter must be less than or equal to the current
        maximum value as specified by ``Py5Graphics.color_mode()``. The default maximum
        value is 255.

        To change the color of an image or a texture, use ``Py5Graphics.tint()``.

        This method is the same as ``fill()`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``fill()``.
        """
        pass

    @overload
    def fill(self, gray: float, alpha: float, /) -> None:
        """Sets the color used to fill shapes.

        Underlying Java method: PGraphics.fill

        Methods
        -------

        You can use any of the following signatures:

         * fill(gray: float, /) -> None
         * fill(gray: float, alpha: float, /) -> None
         * fill(rgb: int, /) -> None
         * fill(rgb: int, alpha: float, /) -> None
         * fill(v1: float, v2: float, v3: float, /) -> None
         * fill(v1: float, v2: float, v3: float, alpha: float, /) -> None

        Parameters
        ----------

        alpha: float
            opacity of the fill

        gray: float
            number specifying value between white and black

        rgb: int
            color variable or hex value

        v1: float
            red or hue value (depending on current color mode)

        v2: float
            green or saturation value (depending on current color mode)

        v3: float
            blue or brightness value (depending on current color mode)

        Notes
        -----

        Sets the color used to fill shapes. For example, if you run ``fill(204, 102,
        0)``, all subsequent shapes will be filled with orange. This color is either
        specified in terms of the ``RGB`` or ``HSB`` color depending on the current
        ``Py5Graphics.color_mode()``. The default color space is ``RGB``, with each
        value in the range from 0 to 255.

        When using hexadecimal notation to specify a color, use "``0x``" before the
        values (e.g., ``0xFFCCFFAA``). The hexadecimal value must be specified with
        eight characters; the first two characters define the alpha component, and the
        remainder define the red, green, and blue components.

        The value for the "gray" parameter must be less than or equal to the current
        maximum value as specified by ``Py5Graphics.color_mode()``. The default maximum
        value is 255.

        To change the color of an image or a texture, use ``Py5Graphics.tint()``.

        This method is the same as ``fill()`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``fill()``.
        """
        pass

    @overload
    def fill(self, v1: float, v2: float, v3: float, /) -> None:
        """Sets the color used to fill shapes.

        Underlying Java method: PGraphics.fill

        Methods
        -------

        You can use any of the following signatures:

         * fill(gray: float, /) -> None
         * fill(gray: float, alpha: float, /) -> None
         * fill(rgb: int, /) -> None
         * fill(rgb: int, alpha: float, /) -> None
         * fill(v1: float, v2: float, v3: float, /) -> None
         * fill(v1: float, v2: float, v3: float, alpha: float, /) -> None

        Parameters
        ----------

        alpha: float
            opacity of the fill

        gray: float
            number specifying value between white and black

        rgb: int
            color variable or hex value

        v1: float
            red or hue value (depending on current color mode)

        v2: float
            green or saturation value (depending on current color mode)

        v3: float
            blue or brightness value (depending on current color mode)

        Notes
        -----

        Sets the color used to fill shapes. For example, if you run ``fill(204, 102,
        0)``, all subsequent shapes will be filled with orange. This color is either
        specified in terms of the ``RGB`` or ``HSB`` color depending on the current
        ``Py5Graphics.color_mode()``. The default color space is ``RGB``, with each
        value in the range from 0 to 255.

        When using hexadecimal notation to specify a color, use "``0x``" before the
        values (e.g., ``0xFFCCFFAA``). The hexadecimal value must be specified with
        eight characters; the first two characters define the alpha component, and the
        remainder define the red, green, and blue components.

        The value for the "gray" parameter must be less than or equal to the current
        maximum value as specified by ``Py5Graphics.color_mode()``. The default maximum
        value is 255.

        To change the color of an image or a texture, use ``Py5Graphics.tint()``.

        This method is the same as ``fill()`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``fill()``.
        """
        pass

    @overload
    def fill(self, v1: float, v2: float, v3: float, alpha: float, /) -> None:
        """Sets the color used to fill shapes.

        Underlying Java method: PGraphics.fill

        Methods
        -------

        You can use any of the following signatures:

         * fill(gray: float, /) -> None
         * fill(gray: float, alpha: float, /) -> None
         * fill(rgb: int, /) -> None
         * fill(rgb: int, alpha: float, /) -> None
         * fill(v1: float, v2: float, v3: float, /) -> None
         * fill(v1: float, v2: float, v3: float, alpha: float, /) -> None

        Parameters
        ----------

        alpha: float
            opacity of the fill

        gray: float
            number specifying value between white and black

        rgb: int
            color variable or hex value

        v1: float
            red or hue value (depending on current color mode)

        v2: float
            green or saturation value (depending on current color mode)

        v3: float
            blue or brightness value (depending on current color mode)

        Notes
        -----

        Sets the color used to fill shapes. For example, if you run ``fill(204, 102,
        0)``, all subsequent shapes will be filled with orange. This color is either
        specified in terms of the ``RGB`` or ``HSB`` color depending on the current
        ``Py5Graphics.color_mode()``. The default color space is ``RGB``, with each
        value in the range from 0 to 255.

        When using hexadecimal notation to specify a color, use "``0x``" before the
        values (e.g., ``0xFFCCFFAA``). The hexadecimal value must be specified with
        eight characters; the first two characters define the alpha component, and the
        remainder define the red, green, and blue components.

        The value for the "gray" parameter must be less than or equal to the current
        maximum value as specified by ``Py5Graphics.color_mode()``. The default maximum
        value is 255.

        To change the color of an image or a texture, use ``Py5Graphics.tint()``.

        This method is the same as ``fill()`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``fill()``.
        """
        pass

    @overload
    def fill(self, rgb: int, /) -> None:
        """Sets the color used to fill shapes.

        Underlying Java method: PGraphics.fill

        Methods
        -------

        You can use any of the following signatures:

         * fill(gray: float, /) -> None
         * fill(gray: float, alpha: float, /) -> None
         * fill(rgb: int, /) -> None
         * fill(rgb: int, alpha: float, /) -> None
         * fill(v1: float, v2: float, v3: float, /) -> None
         * fill(v1: float, v2: float, v3: float, alpha: float, /) -> None

        Parameters
        ----------

        alpha: float
            opacity of the fill

        gray: float
            number specifying value between white and black

        rgb: int
            color variable or hex value

        v1: float
            red or hue value (depending on current color mode)

        v2: float
            green or saturation value (depending on current color mode)

        v3: float
            blue or brightness value (depending on current color mode)

        Notes
        -----

        Sets the color used to fill shapes. For example, if you run ``fill(204, 102,
        0)``, all subsequent shapes will be filled with orange. This color is either
        specified in terms of the ``RGB`` or ``HSB`` color depending on the current
        ``Py5Graphics.color_mode()``. The default color space is ``RGB``, with each
        value in the range from 0 to 255.

        When using hexadecimal notation to specify a color, use "``0x``" before the
        values (e.g., ``0xFFCCFFAA``). The hexadecimal value must be specified with
        eight characters; the first two characters define the alpha component, and the
        remainder define the red, green, and blue components.

        The value for the "gray" parameter must be less than or equal to the current
        maximum value as specified by ``Py5Graphics.color_mode()``. The default maximum
        value is 255.

        To change the color of an image or a texture, use ``Py5Graphics.tint()``.

        This method is the same as ``fill()`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``fill()``.
        """
        pass

    @overload
    def fill(self, rgb: int, alpha: float, /) -> None:
        """Sets the color used to fill shapes.

        Underlying Java method: PGraphics.fill

        Methods
        -------

        You can use any of the following signatures:

         * fill(gray: float, /) -> None
         * fill(gray: float, alpha: float, /) -> None
         * fill(rgb: int, /) -> None
         * fill(rgb: int, alpha: float, /) -> None
         * fill(v1: float, v2: float, v3: float, /) -> None
         * fill(v1: float, v2: float, v3: float, alpha: float, /) -> None

        Parameters
        ----------

        alpha: float
            opacity of the fill

        gray: float
            number specifying value between white and black

        rgb: int
            color variable or hex value

        v1: float
            red or hue value (depending on current color mode)

        v2: float
            green or saturation value (depending on current color mode)

        v3: float
            blue or brightness value (depending on current color mode)

        Notes
        -----

        Sets the color used to fill shapes. For example, if you run ``fill(204, 102,
        0)``, all subsequent shapes will be filled with orange. This color is either
        specified in terms of the ``RGB`` or ``HSB`` color depending on the current
        ``Py5Graphics.color_mode()``. The default color space is ``RGB``, with each
        value in the range from 0 to 255.

        When using hexadecimal notation to specify a color, use "``0x``" before the
        values (e.g., ``0xFFCCFFAA``). The hexadecimal value must be specified with
        eight characters; the first two characters define the alpha component, and the
        remainder define the red, green, and blue components.

        The value for the "gray" parameter must be less than or equal to the current
        maximum value as specified by ``Py5Graphics.color_mode()``. The default maximum
        value is 255.

        To change the color of an image or a texture, use ``Py5Graphics.tint()``.

        This method is the same as ``fill()`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``fill()``.
        """
        pass

    def fill(self, *args):
        """Sets the color used to fill shapes.

        Underlying Java method: PGraphics.fill

        Methods
        -------

        You can use any of the following signatures:

         * fill(gray: float, /) -> None
         * fill(gray: float, alpha: float, /) -> None
         * fill(rgb: int, /) -> None
         * fill(rgb: int, alpha: float, /) -> None
         * fill(v1: float, v2: float, v3: float, /) -> None
         * fill(v1: float, v2: float, v3: float, alpha: float, /) -> None

        Parameters
        ----------

        alpha: float
            opacity of the fill

        gray: float
            number specifying value between white and black

        rgb: int
            color variable or hex value

        v1: float
            red or hue value (depending on current color mode)

        v2: float
            green or saturation value (depending on current color mode)

        v3: float
            blue or brightness value (depending on current color mode)

        Notes
        -----

        Sets the color used to fill shapes. For example, if you run ``fill(204, 102,
        0)``, all subsequent shapes will be filled with orange. This color is either
        specified in terms of the ``RGB`` or ``HSB`` color depending on the current
        ``Py5Graphics.color_mode()``. The default color space is ``RGB``, with each
        value in the range from 0 to 255.

        When using hexadecimal notation to specify a color, use "``0x``" before the
        values (e.g., ``0xFFCCFFAA``). The hexadecimal value must be specified with
        eight characters; the first two characters define the alpha component, and the
        remainder define the red, green, and blue components.

        The value for the "gray" parameter must be less than or equal to the current
        maximum value as specified by ``Py5Graphics.color_mode()``. The default maximum
        value is 255.

        To change the color of an image or a texture, use ``Py5Graphics.tint()``.

        This method is the same as ``fill()`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``fill()``.
        """
        return self._instance.fill(*args)

    @overload
    def apply_filter(self, kind: int, /) -> None:
        """Filters the Py5Graphics drawing surface using a preset filter or with a custom
        shader.

        Underlying Java method: PGraphics.filter

        Methods
        -------

        You can use any of the following signatures:

         * apply_filter(kind: int, /) -> None
         * apply_filter(kind: int, param: float, /) -> None
         * apply_filter(shader: Py5Shader, /) -> None

        Parameters
        ----------

        kind: int
            Either THRESHOLD, GRAY, OPAQUE, INVERT, POSTERIZE, BLUR, ERODE, or DILATE

        param: float
            unique for each, see above

        shader: Py5Shader
            the fragment shader to apply

        Notes
        -----

        Filters the Py5Graphics drawing surface using a preset filter or with a custom
        shader. Using a shader with ``apply_filter()`` is much faster than without.
        Shaders require the ``P2D`` or ``P3D`` renderer in ``size()``.

        The presets options are:

        * THRESHOLD: Converts the image to black and white pixels depending if they are
        above or below the threshold defined by the level parameter. The parameter must
        be between 0.0 (black) and 1.0 (white). If no level is specified, 0.5 is used.
        * GRAY: Converts any colors in the image to grayscale equivalents. No parameter
        is used.
        * OPAQUE: Sets the alpha channel to entirely opaque. No parameter is used.
        * INVERT: Sets each pixel to its inverse value. No parameter is used.
        * POSTERIZE: Limits each channel of the image to the number of colors specified
        as the parameter. The parameter can be set to values between 2 and 255, but
        results are most noticeable in the lower ranges.
        * BLUR: Executes a Guassian blur with the level parameter specifying the extent
        of the blurring. If no parameter is used, the blur is equivalent to Guassian
        blur of radius 1. Larger values increase the blur.
        * ERODE: Reduces the light areas. No parameter is used.
        * DILATE: Increases the light areas. No parameter is used.

        This method is the same as ``apply_filter()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``apply_filter()``.
        """
        pass

    @overload
    def apply_filter(self, kind: int, param: float, /) -> None:
        """Filters the Py5Graphics drawing surface using a preset filter or with a custom
        shader.

        Underlying Java method: PGraphics.filter

        Methods
        -------

        You can use any of the following signatures:

         * apply_filter(kind: int, /) -> None
         * apply_filter(kind: int, param: float, /) -> None
         * apply_filter(shader: Py5Shader, /) -> None

        Parameters
        ----------

        kind: int
            Either THRESHOLD, GRAY, OPAQUE, INVERT, POSTERIZE, BLUR, ERODE, or DILATE

        param: float
            unique for each, see above

        shader: Py5Shader
            the fragment shader to apply

        Notes
        -----

        Filters the Py5Graphics drawing surface using a preset filter or with a custom
        shader. Using a shader with ``apply_filter()`` is much faster than without.
        Shaders require the ``P2D`` or ``P3D`` renderer in ``size()``.

        The presets options are:

        * THRESHOLD: Converts the image to black and white pixels depending if they are
        above or below the threshold defined by the level parameter. The parameter must
        be between 0.0 (black) and 1.0 (white). If no level is specified, 0.5 is used.
        * GRAY: Converts any colors in the image to grayscale equivalents. No parameter
        is used.
        * OPAQUE: Sets the alpha channel to entirely opaque. No parameter is used.
        * INVERT: Sets each pixel to its inverse value. No parameter is used.
        * POSTERIZE: Limits each channel of the image to the number of colors specified
        as the parameter. The parameter can be set to values between 2 and 255, but
        results are most noticeable in the lower ranges.
        * BLUR: Executes a Guassian blur with the level parameter specifying the extent
        of the blurring. If no parameter is used, the blur is equivalent to Guassian
        blur of radius 1. Larger values increase the blur.
        * ERODE: Reduces the light areas. No parameter is used.
        * DILATE: Increases the light areas. No parameter is used.

        This method is the same as ``apply_filter()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``apply_filter()``.
        """
        pass

    @overload
    def apply_filter(self, shader: Py5Shader, /) -> None:
        """Filters the Py5Graphics drawing surface using a preset filter or with a custom
        shader.

        Underlying Java method: PGraphics.filter

        Methods
        -------

        You can use any of the following signatures:

         * apply_filter(kind: int, /) -> None
         * apply_filter(kind: int, param: float, /) -> None
         * apply_filter(shader: Py5Shader, /) -> None

        Parameters
        ----------

        kind: int
            Either THRESHOLD, GRAY, OPAQUE, INVERT, POSTERIZE, BLUR, ERODE, or DILATE

        param: float
            unique for each, see above

        shader: Py5Shader
            the fragment shader to apply

        Notes
        -----

        Filters the Py5Graphics drawing surface using a preset filter or with a custom
        shader. Using a shader with ``apply_filter()`` is much faster than without.
        Shaders require the ``P2D`` or ``P3D`` renderer in ``size()``.

        The presets options are:

        * THRESHOLD: Converts the image to black and white pixels depending if they are
        above or below the threshold defined by the level parameter. The parameter must
        be between 0.0 (black) and 1.0 (white). If no level is specified, 0.5 is used.
        * GRAY: Converts any colors in the image to grayscale equivalents. No parameter
        is used.
        * OPAQUE: Sets the alpha channel to entirely opaque. No parameter is used.
        * INVERT: Sets each pixel to its inverse value. No parameter is used.
        * POSTERIZE: Limits each channel of the image to the number of colors specified
        as the parameter. The parameter can be set to values between 2 and 255, but
        results are most noticeable in the lower ranges.
        * BLUR: Executes a Guassian blur with the level parameter specifying the extent
        of the blurring. If no parameter is used, the blur is equivalent to Guassian
        blur of radius 1. Larger values increase the blur.
        * ERODE: Reduces the light areas. No parameter is used.
        * DILATE: Increases the light areas. No parameter is used.

        This method is the same as ``apply_filter()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``apply_filter()``.
        """
        pass

    def apply_filter(self, *args):
        """Filters the Py5Graphics drawing surface using a preset filter or with a custom
        shader.

        Underlying Java method: PGraphics.filter

        Methods
        -------

        You can use any of the following signatures:

         * apply_filter(kind: int, /) -> None
         * apply_filter(kind: int, param: float, /) -> None
         * apply_filter(shader: Py5Shader, /) -> None

        Parameters
        ----------

        kind: int
            Either THRESHOLD, GRAY, OPAQUE, INVERT, POSTERIZE, BLUR, ERODE, or DILATE

        param: float
            unique for each, see above

        shader: Py5Shader
            the fragment shader to apply

        Notes
        -----

        Filters the Py5Graphics drawing surface using a preset filter or with a custom
        shader. Using a shader with ``apply_filter()`` is much faster than without.
        Shaders require the ``P2D`` or ``P3D`` renderer in ``size()``.

        The presets options are:

        * THRESHOLD: Converts the image to black and white pixels depending if they are
        above or below the threshold defined by the level parameter. The parameter must
        be between 0.0 (black) and 1.0 (white). If no level is specified, 0.5 is used.
        * GRAY: Converts any colors in the image to grayscale equivalents. No parameter
        is used.
        * OPAQUE: Sets the alpha channel to entirely opaque. No parameter is used.
        * INVERT: Sets each pixel to its inverse value. No parameter is used.
        * POSTERIZE: Limits each channel of the image to the number of colors specified
        as the parameter. The parameter can be set to values between 2 and 255, but
        results are most noticeable in the lower ranges.
        * BLUR: Executes a Guassian blur with the level parameter specifying the extent
        of the blurring. If no parameter is used, the blur is equivalent to Guassian
        blur of radius 1. Larger values increase the blur.
        * ERODE: Reduces the light areas. No parameter is used.
        * DILATE: Increases the light areas. No parameter is used.

        This method is the same as ``apply_filter()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``apply_filter()``.
        """
        return self._instance.filter(*args)

    def frustum(self, left: float, right: float, bottom: float,
                top: float, near: float, far: float, /) -> None:
        """Sets a perspective matrix as defined by the parameters.

        Underlying Java method: PGraphics.frustum

        Parameters
        ----------

        bottom: float
            bottom coordinate of the clipping plane

        far: float
            far component of the clipping plane; must be greater than the near value

        left: float
            left coordinate of the clipping plane

        near: float
            near component of the clipping plane; must be greater than zero

        right: float
            right coordinate of the clipping plane

        top: float
            top coordinate of the clipping plane

        Notes
        -----

        Sets a perspective matrix as defined by the parameters.

        A frustum is a geometric form: a pyramid with its top cut off.  With the
        viewer's eye at the imaginary top of the pyramid, the six planes of the frustum
        act as clipping planes when rendering a 3D view.  Thus, any form inside the
        clipping planes is rendered and visible; anything outside those planes is not
        visible.

        Setting the frustum has the effect of changing the *perspective* with which the
        scene is rendered.  This can be achieved more simply in many cases by using
        ``Py5Graphics.perspective()``.

        Note that the near value must be greater than zero (as the point of the frustum
        "pyramid" cannot converge "behind" the viewer).  Similarly, the far value must
        be greater than the near value (as the "far" plane of the frustum must be
        "farther away" from the viewer than the near plane).

        Works like glFrustum, except it wipes out the current perspective matrix rather
        than multiplying itself with it.

        This method is the same as ``frustum()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``frustum()``.
        """
        return self._instance.frustum(left, right, bottom, top, near, far)

    @overload
    def get(self) -> Py5Image:
        """Reads the color of any pixel or grabs a section of an ``Py5Graphics`` object
        canvas.

        Underlying Java method: PGraphics.get

        Methods
        -------

        You can use any of the following signatures:

         * get() -> Py5Image
         * get(x: int, y: int, /) -> int
         * get(x: int, y: int, w: int, h: int, /) -> Py5Image

        Parameters
        ----------

        h: int
            height of pixel rectangle to get

        w: int
            width of pixel rectangle to get

        x: int
            x-coordinate of the pixel

        y: int
            y-coordinate of the pixel

        Notes
        -----

        Reads the color of any pixel or grabs a section of an ``Py5Graphics`` object
        canvas. If no parameters are specified, the entire canvas is returned. Use the
        ``x`` and ``y`` parameters to get the value of one pixel. Get a section of the
        Py5Graphics drawing surface by specifying additional ``w`` and ``h`` parameters.
        When getting an image, the ``x`` and ``y`` parameters define the coordinates for
        the upper-left corner of the returned image, regardless of the current
        ``Py5Graphics.image_mode()``.

        If the pixel requested is outside of the ``Py5Graphics`` object canvas, black is
        returned. The numbers returned are scaled according to the current color ranges,
        but only ``RGB`` values are returned by this function. For example, even though
        you may have drawn a shape with ``color_mode(HSB)``, the numbers returned will
        be in ``RGB`` format.

        If a width and a height are specified, ``get(x, y, w, h)`` returns a Py5Image
        corresponding to the part of the original Py5Image where the top left pixel is
        at the ``(x, y)`` position with a width of ``w`` a height of ``h``.

        Getting the color of a single pixel with ``get(x, y)`` is easy, but not as fast
        as grabbing the data directly from ``Py5Graphics.pixels[]`` or
        ``Py5Graphics.np_pixels[]``. The equivalent statement to ``get(x, y)`` using
        ``Py5Graphics.pixels[]`` is ``pixels[y*width+x]``. Using
        ``Py5Graphics.np_pixels[]`` it is ``np_pixels[y, x]``. See the reference for
        ``Py5Graphics.pixels[]`` and ``Py5Graphics.np_pixels[]`` for more information.

        This method is the same as ``get()`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``get()``.
        """
        pass

    @overload
    def get(self, x: int, y: int, /) -> int:
        """Reads the color of any pixel or grabs a section of an ``Py5Graphics`` object
        canvas.

        Underlying Java method: PGraphics.get

        Methods
        -------

        You can use any of the following signatures:

         * get() -> Py5Image
         * get(x: int, y: int, /) -> int
         * get(x: int, y: int, w: int, h: int, /) -> Py5Image

        Parameters
        ----------

        h: int
            height of pixel rectangle to get

        w: int
            width of pixel rectangle to get

        x: int
            x-coordinate of the pixel

        y: int
            y-coordinate of the pixel

        Notes
        -----

        Reads the color of any pixel or grabs a section of an ``Py5Graphics`` object
        canvas. If no parameters are specified, the entire canvas is returned. Use the
        ``x`` and ``y`` parameters to get the value of one pixel. Get a section of the
        Py5Graphics drawing surface by specifying additional ``w`` and ``h`` parameters.
        When getting an image, the ``x`` and ``y`` parameters define the coordinates for
        the upper-left corner of the returned image, regardless of the current
        ``Py5Graphics.image_mode()``.

        If the pixel requested is outside of the ``Py5Graphics`` object canvas, black is
        returned. The numbers returned are scaled according to the current color ranges,
        but only ``RGB`` values are returned by this function. For example, even though
        you may have drawn a shape with ``color_mode(HSB)``, the numbers returned will
        be in ``RGB`` format.

        If a width and a height are specified, ``get(x, y, w, h)`` returns a Py5Image
        corresponding to the part of the original Py5Image where the top left pixel is
        at the ``(x, y)`` position with a width of ``w`` a height of ``h``.

        Getting the color of a single pixel with ``get(x, y)`` is easy, but not as fast
        as grabbing the data directly from ``Py5Graphics.pixels[]`` or
        ``Py5Graphics.np_pixels[]``. The equivalent statement to ``get(x, y)`` using
        ``Py5Graphics.pixels[]`` is ``pixels[y*width+x]``. Using
        ``Py5Graphics.np_pixels[]`` it is ``np_pixels[y, x]``. See the reference for
        ``Py5Graphics.pixels[]`` and ``Py5Graphics.np_pixels[]`` for more information.

        This method is the same as ``get()`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``get()``.
        """
        pass

    @overload
    def get(self, x: int, y: int, w: int, h: int, /) -> Py5Image:
        """Reads the color of any pixel or grabs a section of an ``Py5Graphics`` object
        canvas.

        Underlying Java method: PGraphics.get

        Methods
        -------

        You can use any of the following signatures:

         * get() -> Py5Image
         * get(x: int, y: int, /) -> int
         * get(x: int, y: int, w: int, h: int, /) -> Py5Image

        Parameters
        ----------

        h: int
            height of pixel rectangle to get

        w: int
            width of pixel rectangle to get

        x: int
            x-coordinate of the pixel

        y: int
            y-coordinate of the pixel

        Notes
        -----

        Reads the color of any pixel or grabs a section of an ``Py5Graphics`` object
        canvas. If no parameters are specified, the entire canvas is returned. Use the
        ``x`` and ``y`` parameters to get the value of one pixel. Get a section of the
        Py5Graphics drawing surface by specifying additional ``w`` and ``h`` parameters.
        When getting an image, the ``x`` and ``y`` parameters define the coordinates for
        the upper-left corner of the returned image, regardless of the current
        ``Py5Graphics.image_mode()``.

        If the pixel requested is outside of the ``Py5Graphics`` object canvas, black is
        returned. The numbers returned are scaled according to the current color ranges,
        but only ``RGB`` values are returned by this function. For example, even though
        you may have drawn a shape with ``color_mode(HSB)``, the numbers returned will
        be in ``RGB`` format.

        If a width and a height are specified, ``get(x, y, w, h)`` returns a Py5Image
        corresponding to the part of the original Py5Image where the top left pixel is
        at the ``(x, y)`` position with a width of ``w`` a height of ``h``.

        Getting the color of a single pixel with ``get(x, y)`` is easy, but not as fast
        as grabbing the data directly from ``Py5Graphics.pixels[]`` or
        ``Py5Graphics.np_pixels[]``. The equivalent statement to ``get(x, y)`` using
        ``Py5Graphics.pixels[]`` is ``pixels[y*width+x]``. Using
        ``Py5Graphics.np_pixels[]`` it is ``np_pixels[y, x]``. See the reference for
        ``Py5Graphics.pixels[]`` and ``Py5Graphics.np_pixels[]`` for more information.

        This method is the same as ``get()`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``get()``.
        """
        pass

    @_return_py5image
    def get(self, *args):
        """Reads the color of any pixel or grabs a section of an ``Py5Graphics`` object
        canvas.

        Underlying Java method: PGraphics.get

        Methods
        -------

        You can use any of the following signatures:

         * get() -> Py5Image
         * get(x: int, y: int, /) -> int
         * get(x: int, y: int, w: int, h: int, /) -> Py5Image

        Parameters
        ----------

        h: int
            height of pixel rectangle to get

        w: int
            width of pixel rectangle to get

        x: int
            x-coordinate of the pixel

        y: int
            y-coordinate of the pixel

        Notes
        -----

        Reads the color of any pixel or grabs a section of an ``Py5Graphics`` object
        canvas. If no parameters are specified, the entire canvas is returned. Use the
        ``x`` and ``y`` parameters to get the value of one pixel. Get a section of the
        Py5Graphics drawing surface by specifying additional ``w`` and ``h`` parameters.
        When getting an image, the ``x`` and ``y`` parameters define the coordinates for
        the upper-left corner of the returned image, regardless of the current
        ``Py5Graphics.image_mode()``.

        If the pixel requested is outside of the ``Py5Graphics`` object canvas, black is
        returned. The numbers returned are scaled according to the current color ranges,
        but only ``RGB`` values are returned by this function. For example, even though
        you may have drawn a shape with ``color_mode(HSB)``, the numbers returned will
        be in ``RGB`` format.

        If a width and a height are specified, ``get(x, y, w, h)`` returns a Py5Image
        corresponding to the part of the original Py5Image where the top left pixel is
        at the ``(x, y)`` position with a width of ``w`` a height of ``h``.

        Getting the color of a single pixel with ``get(x, y)`` is easy, but not as fast
        as grabbing the data directly from ``Py5Graphics.pixels[]`` or
        ``Py5Graphics.np_pixels[]``. The equivalent statement to ``get(x, y)`` using
        ``Py5Graphics.pixels[]`` is ``pixels[y*width+x]``. Using
        ``Py5Graphics.np_pixels[]`` it is ``np_pixels[y, x]``. See the reference for
        ``Py5Graphics.pixels[]`` and ``Py5Graphics.np_pixels[]`` for more information.

        This method is the same as ``get()`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``get()``.
        """
        return self._instance.get(*args)

    @overload
    def get_matrix(self) -> NDArray[(Any, Any), Float]:
        """Get the current matrix as a numpy array.

        Underlying Java method: PGraphics.getMatrix

        Methods
        -------

        You can use any of the following signatures:

         * get_matrix() -> NDArray[(Any, Any), Float]
         * get_matrix(target: NDArray[(2, 3), Float], /) -> NDArray[(2, 3), Float]
         * get_matrix(target: NDArray[(4, 4), Float], /) -> NDArray[(4, 4), Float]

        Parameters
        ----------

        target: NDArray[(2, 3), Float]
            transformation matrix data

        target: NDArray[(4, 4), Float]
            transformation matrix data

        Notes
        -----

        Get the current matrix as a numpy array. Use the ``target`` parameter to put the
        matrix data in a properly sized and typed numpy array.

        This method is the same as ``get_matrix()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``get_matrix()``.
        """
        pass

    @overload
    def get_matrix(self, target: NDArray[(
            2, 3), Float], /) -> NDArray[(2, 3), Float]:
        """Get the current matrix as a numpy array.

        Underlying Java method: PGraphics.getMatrix

        Methods
        -------

        You can use any of the following signatures:

         * get_matrix() -> NDArray[(Any, Any), Float]
         * get_matrix(target: NDArray[(2, 3), Float], /) -> NDArray[(2, 3), Float]
         * get_matrix(target: NDArray[(4, 4), Float], /) -> NDArray[(4, 4), Float]

        Parameters
        ----------

        target: NDArray[(2, 3), Float]
            transformation matrix data

        target: NDArray[(4, 4), Float]
            transformation matrix data

        Notes
        -----

        Get the current matrix as a numpy array. Use the ``target`` parameter to put the
        matrix data in a properly sized and typed numpy array.

        This method is the same as ``get_matrix()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``get_matrix()``.
        """
        pass

    @overload
    def get_matrix(self, target: NDArray[(
            4, 4), Float], /) -> NDArray[(4, 4), Float]:
        """Get the current matrix as a numpy array.

        Underlying Java method: PGraphics.getMatrix

        Methods
        -------

        You can use any of the following signatures:

         * get_matrix() -> NDArray[(Any, Any), Float]
         * get_matrix(target: NDArray[(2, 3), Float], /) -> NDArray[(2, 3), Float]
         * get_matrix(target: NDArray[(4, 4), Float], /) -> NDArray[(4, 4), Float]

        Parameters
        ----------

        target: NDArray[(2, 3), Float]
            transformation matrix data

        target: NDArray[(4, 4), Float]
            transformation matrix data

        Notes
        -----

        Get the current matrix as a numpy array. Use the ``target`` parameter to put the
        matrix data in a properly sized and typed numpy array.

        This method is the same as ``get_matrix()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``get_matrix()``.
        """
        pass

    @ _get_matrix_wrapper
    def get_matrix(self, *args):
        """Get the current matrix as a numpy array.

        Underlying Java method: PGraphics.getMatrix

        Methods
        -------

        You can use any of the following signatures:

         * get_matrix() -> NDArray[(Any, Any), Float]
         * get_matrix(target: NDArray[(2, 3), Float], /) -> NDArray[(2, 3), Float]
         * get_matrix(target: NDArray[(4, 4), Float], /) -> NDArray[(4, 4), Float]

        Parameters
        ----------

        target: NDArray[(2, 3), Float]
            transformation matrix data

        target: NDArray[(4, 4), Float]
            transformation matrix data

        Notes
        -----

        Get the current matrix as a numpy array. Use the ``target`` parameter to put the
        matrix data in a properly sized and typed numpy array.

        This method is the same as ``get_matrix()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``get_matrix()``.
        """
        return self._instance.getMatrix(*args)

    def green(self, rgb: int, /) -> float:
        """Extracts the green value from a color, scaled to match current
        ``Py5Graphics.color_mode()``.

        Underlying Java method: PGraphics.green

        Parameters
        ----------

        rgb: int
            any value of the color datatype

        Notes
        -----

        Extracts the green value from a color, scaled to match current
        ``Py5Graphics.color_mode()``.

        The ``green()`` function is easy to use and understand, but it is slower than a
        technique called bit shifting. When working in ``color_mode(RGB, 255)``, you can
        achieve the same results as ``green()`` but with greater speed by using the
        right shift operator (``>>``) with a bit mask. For example, ``green(c)`` and ``c
        >> 8 & 0xFF`` both extract the green value from a color variable ``c`` but the
        later is faster.

        This method is the same as ``green()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``green()``.
        """
        return self._instance.green(rgb)

    def hint(self, which: int, /) -> None:
        """This function is used to enable or disable special features that control how
        graphics are drawn.

        Underlying Java method: PGraphics.hint

        Parameters
        ----------

        which: int
            hint to use when rendering Sketch

        Notes
        -----

        This function is used to enable or disable special features that control how
        graphics are drawn. In the course of developing Processing, the developers had
        to make hard decisions about tradeoffs between performance and visual quality.
        They put significant effort into determining what makes most sense for the
        largest number of users, and then use functions like ``hint()`` to allow people
        to tune the settings for their particular Sketch. Implementing a ``hint()`` is a
        last resort that's used when a more elegant solution cannot be found. Some
        options might graduate to standard features instead of hints over time, or be
        added and removed between (major) releases.

        Hints used by the Default Renderer
        ----------------------------------

        * ``ENABLE_STROKE_PURE``: Fixes a problem with shapes that have a stroke and are
        rendered using small steps (for instance, using ``Py5Graphics.vertex()`` with
        points that are close to one another), or are drawn at small sizes.

        Hints for use with ``P2D`` and ``P3D``
        --------------------------------------

        * ``DISABLE_OPENGL_ERRORS``: Speeds up the ``P3D`` renderer setting by not
        checking for errors while running.
        * ``DISABLE_TEXTURE_MIPMAPS``: Disable generation of texture mipmaps in ``P2D``
        or ``P3D``. This results in lower quality - but faster - rendering of texture
        images when they appear smaller than their native resolutions (the mipmaps are
        scaled-down versions of a texture that make it look better when drawing it at a
        small size). However, the difference in performance is fairly minor on recent
        desktop video cards.


        Hints for use with ``P3D`` only
        -------------------------------

        * ``DISABLE_DEPTH_MASK``: Disables writing into the depth buffer. This means
        that a shape drawn with this hint can be hidden by another shape drawn later,
        irrespective of their distances to the camera. Note that this is different from
        disabling the depth test. The depth test is still applied, as long as the
        ``DISABLE_DEPTH_TEST`` hint is not called, but the depth values of the objects
        are not recorded. This is useful when drawing a semi-transparent 3D object
        without depth sorting, in order to avoid visual glitches due the faces of the
        object being at different distances from the camera, but still having the object
        properly occluded by the rest of the objects in the scene.
        * ``ENABLE_DEPTH_SORT``: Enable primitive z-sorting of triangles and lines in
        ``P3D``. This can slow performance considerably, and the algorithm is not yet
        perfect.
        * ``DISABLE_DEPTH_TEST``: Disable the zbuffer, allowing you to draw on top of
        everything at will. When depth testing is disabled, items will be drawn to the
        screen sequentially, like a painting. This hint is most often used to draw in
        3D, then draw in 2D on top of it (for instance, to draw GUI controls in 2D on
        top of a 3D interface). When called, this will also clear the depth buffer.
        Restore the default with ``hint(ENABLE_DEPTH_TEST)``, but note that with the
        depth buffer cleared, any 3D drawing that happens later in will ignore existing
        shapes on the screen.
        * ``DISABLE_OPTIMIZED_STROKE``: Forces the ``P3D`` renderer to draw each shape
        (including its strokes) separately, instead of batching them into larger groups
        for better performance. One consequence of this is that 2D items drawn with
        ``P3D`` are correctly stacked on the screen, depending on the order in which
        they were drawn. Otherwise, glitches such as the stroke lines being drawn on top
        of the interior of all the shapes will occur. However, this hint can make
        rendering substantially slower, so it is recommended to use it only when drawing
        a small amount of shapes. For drawing two-dimensional scenes, use the ``P2D``
        renderer instead, which doesn't need the hint to properly stack shapes and their
        strokes.
        * ``ENABLE_STROKE_PERSPECTIVE``: Enables stroke geometry (lines and points) to
        be affected by the perspective, meaning that they will look smaller as they move
        away from the camera.

        This method is the same as ``hint()`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``hint()``.
        """
        return self._instance.hint(which)

    def hue(self, rgb: int, /) -> float:
        """Extracts the hue value from a color.

        Underlying Java method: PGraphics.hue

        Parameters
        ----------

        rgb: int
            any value of the color datatype

        Notes
        -----

        Extracts the hue value from a color.

        This method is the same as ``hue()`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``hue()``.
        """
        return self._instance.hue(rgb)

    @overload
    def image(self, img: Py5Image, a: float, b: float, /) -> None:
        """The ``image()`` function draws an image to the Py5Graphics drawing surface.

        Underlying Java method: PGraphics.image

        Methods
        -------

        You can use any of the following signatures:

         * image(img: Py5Image, a: float, b: float, /) -> None
         * image(img: Py5Image, a: float, b: float, c: float, d: float, /) -> None
         * image(img: Py5Image, a: float, b: float, c: float, d: float, u1: int, v1: int, u2: int, v2: int, /) -> None

        Parameters
        ----------

        a: float
            x-coordinate of the image by default

        b: float
            y-coordinate of the image by default

        c: float
            width to display the image by default

        d: float
            height to display the image by default

        img: Py5Image
            the image to display

        u1: int
            x-coordinate of the upper left corner of image subset

        u2: int
            y-coordinate of the upper left corner of image subset

        v1: int
            x-coordinate of the lower right corner of image subset

        v2: int
            y-coordinate of the lower right corner of image subset

        Notes
        -----

        The ``image()`` function draws an image to the Py5Graphics drawing surface.
        Images must be in the Sketch's "data" directory to load correctly. Py5 currently
        works with GIF, JPEG, and PNG images.

        The ``img`` parameter specifies the image to display and by default the ``a``
        and ``b`` parameters define the location of its upper-left corner. The image is
        displayed at its original size unless the ``c`` and ``d`` parameters specify a
        different size. The ``Py5Graphics.image_mode()`` function can be used to change
        the way these parameters draw the image.

        Use the ``u1``, ``u2``, ``v1``, and ``v2`` parameters to use only a subset of
        the image. These values are always specified in image space location, regardless
        of the current ``Py5Graphics.texture_mode()`` setting.

        The color of an image may be modified with the ``Py5Graphics.tint()`` function.
        This function will maintain transparency for GIF and PNG images.

        This method is the same as ``image()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``image()``.
        """
        pass

    @overload
    def image(self, img: Py5Image, a: float, b: float,
              c: float, d: float, /) -> None:
        """The ``image()`` function draws an image to the Py5Graphics drawing surface.

        Underlying Java method: PGraphics.image

        Methods
        -------

        You can use any of the following signatures:

         * image(img: Py5Image, a: float, b: float, /) -> None
         * image(img: Py5Image, a: float, b: float, c: float, d: float, /) -> None
         * image(img: Py5Image, a: float, b: float, c: float, d: float, u1: int, v1: int, u2: int, v2: int, /) -> None

        Parameters
        ----------

        a: float
            x-coordinate of the image by default

        b: float
            y-coordinate of the image by default

        c: float
            width to display the image by default

        d: float
            height to display the image by default

        img: Py5Image
            the image to display

        u1: int
            x-coordinate of the upper left corner of image subset

        u2: int
            y-coordinate of the upper left corner of image subset

        v1: int
            x-coordinate of the lower right corner of image subset

        v2: int
            y-coordinate of the lower right corner of image subset

        Notes
        -----

        The ``image()`` function draws an image to the Py5Graphics drawing surface.
        Images must be in the Sketch's "data" directory to load correctly. Py5 currently
        works with GIF, JPEG, and PNG images.

        The ``img`` parameter specifies the image to display and by default the ``a``
        and ``b`` parameters define the location of its upper-left corner. The image is
        displayed at its original size unless the ``c`` and ``d`` parameters specify a
        different size. The ``Py5Graphics.image_mode()`` function can be used to change
        the way these parameters draw the image.

        Use the ``u1``, ``u2``, ``v1``, and ``v2`` parameters to use only a subset of
        the image. These values are always specified in image space location, regardless
        of the current ``Py5Graphics.texture_mode()`` setting.

        The color of an image may be modified with the ``Py5Graphics.tint()`` function.
        This function will maintain transparency for GIF and PNG images.

        This method is the same as ``image()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``image()``.
        """
        pass

    @overload
    def image(self, img: Py5Image, a: float, b: float, c: float,
              d: float, u1: int, v1: int, u2: int, v2: int, /) -> None:
        """The ``image()`` function draws an image to the Py5Graphics drawing surface.

        Underlying Java method: PGraphics.image

        Methods
        -------

        You can use any of the following signatures:

         * image(img: Py5Image, a: float, b: float, /) -> None
         * image(img: Py5Image, a: float, b: float, c: float, d: float, /) -> None
         * image(img: Py5Image, a: float, b: float, c: float, d: float, u1: int, v1: int, u2: int, v2: int, /) -> None

        Parameters
        ----------

        a: float
            x-coordinate of the image by default

        b: float
            y-coordinate of the image by default

        c: float
            width to display the image by default

        d: float
            height to display the image by default

        img: Py5Image
            the image to display

        u1: int
            x-coordinate of the upper left corner of image subset

        u2: int
            y-coordinate of the upper left corner of image subset

        v1: int
            x-coordinate of the lower right corner of image subset

        v2: int
            y-coordinate of the lower right corner of image subset

        Notes
        -----

        The ``image()`` function draws an image to the Py5Graphics drawing surface.
        Images must be in the Sketch's "data" directory to load correctly. Py5 currently
        works with GIF, JPEG, and PNG images.

        The ``img`` parameter specifies the image to display and by default the ``a``
        and ``b`` parameters define the location of its upper-left corner. The image is
        displayed at its original size unless the ``c`` and ``d`` parameters specify a
        different size. The ``Py5Graphics.image_mode()`` function can be used to change
        the way these parameters draw the image.

        Use the ``u1``, ``u2``, ``v1``, and ``v2`` parameters to use only a subset of
        the image. These values are always specified in image space location, regardless
        of the current ``Py5Graphics.texture_mode()`` setting.

        The color of an image may be modified with the ``Py5Graphics.tint()`` function.
        This function will maintain transparency for GIF and PNG images.

        This method is the same as ``image()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``image()``.
        """
        pass

    def image(self, *args):
        """The ``image()`` function draws an image to the Py5Graphics drawing surface.

        Underlying Java method: PGraphics.image

        Methods
        -------

        You can use any of the following signatures:

         * image(img: Py5Image, a: float, b: float, /) -> None
         * image(img: Py5Image, a: float, b: float, c: float, d: float, /) -> None
         * image(img: Py5Image, a: float, b: float, c: float, d: float, u1: int, v1: int, u2: int, v2: int, /) -> None

        Parameters
        ----------

        a: float
            x-coordinate of the image by default

        b: float
            y-coordinate of the image by default

        c: float
            width to display the image by default

        d: float
            height to display the image by default

        img: Py5Image
            the image to display

        u1: int
            x-coordinate of the upper left corner of image subset

        u2: int
            y-coordinate of the upper left corner of image subset

        v1: int
            x-coordinate of the lower right corner of image subset

        v2: int
            y-coordinate of the lower right corner of image subset

        Notes
        -----

        The ``image()`` function draws an image to the Py5Graphics drawing surface.
        Images must be in the Sketch's "data" directory to load correctly. Py5 currently
        works with GIF, JPEG, and PNG images.

        The ``img`` parameter specifies the image to display and by default the ``a``
        and ``b`` parameters define the location of its upper-left corner. The image is
        displayed at its original size unless the ``c`` and ``d`` parameters specify a
        different size. The ``Py5Graphics.image_mode()`` function can be used to change
        the way these parameters draw the image.

        Use the ``u1``, ``u2``, ``v1``, and ``v2`` parameters to use only a subset of
        the image. These values are always specified in image space location, regardless
        of the current ``Py5Graphics.texture_mode()`` setting.

        The color of an image may be modified with the ``Py5Graphics.tint()`` function.
        This function will maintain transparency for GIF and PNG images.

        This method is the same as ``image()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``image()``.
        """
        return self._instance.image(*args)

    def image_mode(self, mode: int, /) -> None:
        """Modifies the location from which images are drawn by changing the way in which
        parameters given to ``Py5Graphics.image()`` are intepreted.

        Underlying Java method: PGraphics.imageMode

        Parameters
        ----------

        mode: int
            either CORNER, CORNERS, or CENTER

        Notes
        -----

        Modifies the location from which images are drawn by changing the way in which
        parameters given to ``Py5Graphics.image()`` are intepreted.

        The default mode is ``image_mode(CORNER)``, which interprets the second and
        third parameters of ``Py5Graphics.image()`` as the upper-left corner of the
        image. If two additional parameters are specified, they are used to set the
        image's width and height.

        ``image_mode(CORNERS)`` interprets the second and third parameters of
        ``Py5Graphics.image()`` as the location of one corner, and the fourth and fifth
        parameters as the opposite corner.

        ``image_mode(CENTER)`` interprets the second and third parameters of
        ``Py5Graphics.image()`` as the image's center point. If two additional
        parameters are specified, they are used to set the image's width and height.

        The parameter must be written in ALL CAPS because Python is a case-sensitive
        language.

        This method is the same as ``image_mode()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``image_mode()``.
        """
        return self._instance.imageMode(mode)

    @overload
    def lerp_color(self, c1: int, c2: int, amt: float, /) -> int:
        """Calculates a color between two colors at a specific increment.

        Underlying Java method: PGraphics.lerpColor

        Methods
        -------

        You can use any of the following signatures:

         * lerp_color(c1: int, c2: int, amt: float, /) -> int
         * lerp_color(c1: int, c2: int, amt: float, mode: int, /) -> int

        Parameters
        ----------

        amt: float
            between 0.0 and 1.0

        c1: int
            interpolate from this color

        c2: int
            interpolate to this color

        mode: int
            either RGB or HSB

        Notes
        -----

        Calculates a color between two colors at a specific increment. The ``amt``
        parameter is the amount to interpolate between the two values where 0.0 is equal
        to the first point, 0.1 is very near the first point, 0.5 is halfway in between,
        etc.

        An amount below 0 will be treated as 0. Likewise, amounts above 1 will be capped
        at 1. This is different from the behavior of ``lerp()``, but necessary because
        otherwise numbers outside the range will produce strange and unexpected colors.

        This method is the same as ``lerp_color()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``lerp_color()``.
        """
        pass

    @overload
    def lerp_color(self, c1: int, c2: int, amt: float, mode: int, /) -> int:
        """Calculates a color between two colors at a specific increment.

        Underlying Java method: PGraphics.lerpColor

        Methods
        -------

        You can use any of the following signatures:

         * lerp_color(c1: int, c2: int, amt: float, /) -> int
         * lerp_color(c1: int, c2: int, amt: float, mode: int, /) -> int

        Parameters
        ----------

        amt: float
            between 0.0 and 1.0

        c1: int
            interpolate from this color

        c2: int
            interpolate to this color

        mode: int
            either RGB or HSB

        Notes
        -----

        Calculates a color between two colors at a specific increment. The ``amt``
        parameter is the amount to interpolate between the two values where 0.0 is equal
        to the first point, 0.1 is very near the first point, 0.5 is halfway in between,
        etc.

        An amount below 0 will be treated as 0. Likewise, amounts above 1 will be capped
        at 1. This is different from the behavior of ``lerp()``, but necessary because
        otherwise numbers outside the range will produce strange and unexpected colors.

        This method is the same as ``lerp_color()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``lerp_color()``.
        """
        pass

    def lerp_color(self, *args):
        """Calculates a color between two colors at a specific increment.

        Underlying Java method: PGraphics.lerpColor

        Methods
        -------

        You can use any of the following signatures:

         * lerp_color(c1: int, c2: int, amt: float, /) -> int
         * lerp_color(c1: int, c2: int, amt: float, mode: int, /) -> int

        Parameters
        ----------

        amt: float
            between 0.0 and 1.0

        c1: int
            interpolate from this color

        c2: int
            interpolate to this color

        mode: int
            either RGB or HSB

        Notes
        -----

        Calculates a color between two colors at a specific increment. The ``amt``
        parameter is the amount to interpolate between the two values where 0.0 is equal
        to the first point, 0.1 is very near the first point, 0.5 is halfway in between,
        etc.

        An amount below 0 will be treated as 0. Likewise, amounts above 1 will be capped
        at 1. This is different from the behavior of ``lerp()``, but necessary because
        otherwise numbers outside the range will produce strange and unexpected colors.

        This method is the same as ``lerp_color()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``lerp_color()``.
        """
        return self._instance.lerpColor(*args)

    def light_falloff(self, constant: float, linear: float,
                      quadratic: float, /) -> None:
        """Sets the falloff rates for point lights, spot lights, and ambient lights.

        Underlying Java method: PGraphics.lightFalloff

        Parameters
        ----------

        constant: float
            constant value or determining falloff

        linear: float
            linear value for determining falloff

        quadratic: float
            quadratic value for determining falloff

        Notes
        -----

        Sets the falloff rates for point lights, spot lights, and ambient lights. Like
        ``Py5Graphics.fill()``, it affects only the elements which are created after it
        in the code. The default value is ``light_falloff(1.0, 0.0, 0.0)``, and the
        parameters are used to calculate the falloff with the equation ``falloff = 1 /
        (CONSTANT + d * ``LINEAR`` + (d*d) * QUADRATIC)``, where ``d`` is the distance
        from light position to vertex position.

        Thinking about an ambient light with a falloff can be tricky. If you want a
        region of your scene to be lit ambiently with one color and another region to be
        lit ambiently with another color, you could use an ambient light with location
        and falloff. You can think of it as a point light that doesn't care which
        direction a surface is facing.

        This method is the same as ``light_falloff()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``light_falloff()``.
        """
        return self._instance.lightFalloff(constant, linear, quadratic)

    def light_specular(self, v1: float, v2: float, v3: float, /) -> None:
        """Sets the specular color for lights.

        Underlying Java method: PGraphics.lightSpecular

        Parameters
        ----------

        v1: float
            red or hue value (depending on current color mode)

        v2: float
            green or saturation value (depending on current color mode)

        v3: float
            blue or brightness value (depending on current color mode)

        Notes
        -----

        Sets the specular color for lights. Like ``Py5Graphics.fill()``, it affects only
        the elements which are created after it in the code. Specular refers to light
        which bounces off a surface in a preferred direction (rather than bouncing in
        all directions like a diffuse light) and is used for creating highlights. The
        specular quality of a light interacts with the specular material qualities set
        through the ``Py5Graphics.specular()`` and ``Py5Graphics.shininess()``
        functions.

        This method is the same as ``light_specular()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``light_specular()``.
        """
        return self._instance.lightSpecular(v1, v2, v3)

    def lights(self) -> None:
        """Sets the default ambient light, directional light, falloff, and specular values.

        Underlying Java method: PGraphics.lights

        Notes
        -----

        Sets the default ambient light, directional light, falloff, and specular values.
        The defaults are ``ambientLight(128, 128, 128)`` and ``directionalLight(128,
        128, 128, 0, 0, -1)``, ``lightFalloff(1, 0, 0)``, and ``lightSpecular(0, 0,
        0)``.

        This method is the same as ``lights()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``lights()``.
        """
        return self._instance.lights()

    @overload
    def line(self, x1: float, y1: float, x2: float, y2: float, /) -> None:
        """Draws a line (a direct path between two points) to the Py5Graphics drawing
        surface.

        Underlying Java method: PGraphics.line

        Methods
        -------

        You can use any of the following signatures:

         * line(x1: float, y1: float, x2: float, y2: float, /) -> None
         * line(x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, /) -> None

        Parameters
        ----------

        x1: float
            x-coordinate of the first point

        x2: float
            x-coordinate of the second point

        y1: float
            y-coordinate of the first point

        y2: float
            y-coordinate of the second point

        z1: float
            z-coordinate of the first point

        z2: float
            z-coordinate of the second point

        Notes
        -----

        Draws a line (a direct path between two points) to the Py5Graphics drawing
        surface. The version of ``line()`` with four parameters draws the line in 2D.
        To color a line, use the ``Py5Graphics.stroke()`` function. A line cannot be
        filled, therefore the ``Py5Graphics.fill()`` function will not affect the color
        of a line. 2D lines are drawn with a width of one pixel by default, but this can
        be changed with the ``Py5Graphics.stroke_weight()`` function. The version with
        six parameters allows the line to be placed anywhere within XYZ space. Drawing
        this shape in 3D with the ``z`` parameter requires the ``P3D`` renderer.

        This method is the same as ``line()`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``line()``.
        """
        pass

    @overload
    def line(self, x1: float, y1: float, z1: float,
             x2: float, y2: float, z2: float, /) -> None:
        """Draws a line (a direct path between two points) to the Py5Graphics drawing
        surface.

        Underlying Java method: PGraphics.line

        Methods
        -------

        You can use any of the following signatures:

         * line(x1: float, y1: float, x2: float, y2: float, /) -> None
         * line(x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, /) -> None

        Parameters
        ----------

        x1: float
            x-coordinate of the first point

        x2: float
            x-coordinate of the second point

        y1: float
            y-coordinate of the first point

        y2: float
            y-coordinate of the second point

        z1: float
            z-coordinate of the first point

        z2: float
            z-coordinate of the second point

        Notes
        -----

        Draws a line (a direct path between two points) to the Py5Graphics drawing
        surface. The version of ``line()`` with four parameters draws the line in 2D.
        To color a line, use the ``Py5Graphics.stroke()`` function. A line cannot be
        filled, therefore the ``Py5Graphics.fill()`` function will not affect the color
        of a line. 2D lines are drawn with a width of one pixel by default, but this can
        be changed with the ``Py5Graphics.stroke_weight()`` function. The version with
        six parameters allows the line to be placed anywhere within XYZ space. Drawing
        this shape in 3D with the ``z`` parameter requires the ``P3D`` renderer.

        This method is the same as ``line()`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``line()``.
        """
        pass

    def line(self, *args):
        """Draws a line (a direct path between two points) to the Py5Graphics drawing
        surface.

        Underlying Java method: PGraphics.line

        Methods
        -------

        You can use any of the following signatures:

         * line(x1: float, y1: float, x2: float, y2: float, /) -> None
         * line(x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, /) -> None

        Parameters
        ----------

        x1: float
            x-coordinate of the first point

        x2: float
            x-coordinate of the second point

        y1: float
            y-coordinate of the first point

        y2: float
            y-coordinate of the second point

        z1: float
            z-coordinate of the first point

        z2: float
            z-coordinate of the second point

        Notes
        -----

        Draws a line (a direct path between two points) to the Py5Graphics drawing
        surface. The version of ``line()`` with four parameters draws the line in 2D.
        To color a line, use the ``Py5Graphics.stroke()`` function. A line cannot be
        filled, therefore the ``Py5Graphics.fill()`` function will not affect the color
        of a line. 2D lines are drawn with a width of one pixel by default, but this can
        be changed with the ``Py5Graphics.stroke_weight()`` function. The version with
        six parameters allows the line to be placed anywhere within XYZ space. Drawing
        this shape in 3D with the ``z`` parameter requires the ``P3D`` renderer.

        This method is the same as ``line()`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``line()``.
        """
        return self._instance.line(*args)

    def load_pixels(self) -> None:
        """Loads the pixel data of the current Py5Graphics drawing surface into the
        ``Py5Graphics.pixels[]`` array.

        Underlying Java method: PGraphics.loadPixels

        Notes
        -----

        Loads the pixel data of the current Py5Graphics drawing surface into the
        ``Py5Graphics.pixels[]`` array. This function must always be called before
        reading from or writing to ``Py5Graphics.pixels[]``. Subsequent changes to the
        Py5Graphics drawing surface will not be reflected in ``Py5Graphics.pixels[]``
        until ``load_pixels()`` is called again.

        This method is the same as ``load_pixels()`` but linked to a ``Py5Graphics``
        object.
        """
        return self._instance.loadPixels()

    @overload
    def load_shader(self, frag_filename: str, /) -> Py5Shader:
        """Loads a shader into a ``Py5Shader`` object.

        Underlying Java method: PGraphics.loadShader

        Methods
        -------

        You can use any of the following signatures:

         * load_shader(frag_filename: str, /) -> Py5Shader
         * load_shader(frag_filename: str, vert_filename: str, /) -> Py5Shader

        Parameters
        ----------

        frag_filename: str
            name of fragment shader file

        vert_filename: str
            name of vertex shader file

        Notes
        -----

        Loads a shader into a ``Py5Shader`` object. The shader file must be loaded in
        the Sketch's "data" directory to load correctly. Shaders are compatible with the
        ``P2D`` and ``P3D`` renderers, but not with the default renderer.

        Alternatively, the file maybe be loaded from anywhere on the local computer
        using an absolute path (something that starts with / on Unix and Linux, or a
        drive letter on Windows), or the filename parameter can be a URL for a file
        found on a network.

        If the file is not available or an error occurs, ``None`` will be returned and
        an error message will be printed to the console. The error message does not halt
        the program, however the ``None`` value may cause an error if your code does not
        check whether the value returned is ``None``.

        This method is the same as ``load_shader()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``load_shader()``.
        """
        pass

    @overload
    def load_shader(self, frag_filename: str,
                    vert_filename: str, /) -> Py5Shader:
        """Loads a shader into a ``Py5Shader`` object.

        Underlying Java method: PGraphics.loadShader

        Methods
        -------

        You can use any of the following signatures:

         * load_shader(frag_filename: str, /) -> Py5Shader
         * load_shader(frag_filename: str, vert_filename: str, /) -> Py5Shader

        Parameters
        ----------

        frag_filename: str
            name of fragment shader file

        vert_filename: str
            name of vertex shader file

        Notes
        -----

        Loads a shader into a ``Py5Shader`` object. The shader file must be loaded in
        the Sketch's "data" directory to load correctly. Shaders are compatible with the
        ``P2D`` and ``P3D`` renderers, but not with the default renderer.

        Alternatively, the file maybe be loaded from anywhere on the local computer
        using an absolute path (something that starts with / on Unix and Linux, or a
        drive letter on Windows), or the filename parameter can be a URL for a file
        found on a network.

        If the file is not available or an error occurs, ``None`` will be returned and
        an error message will be printed to the console. The error message does not halt
        the program, however the ``None`` value may cause an error if your code does not
        check whether the value returned is ``None``.

        This method is the same as ``load_shader()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``load_shader()``.
        """
        pass

    @_load_py5shader
    def load_shader(self, *args):
        """Loads a shader into a ``Py5Shader`` object.

        Underlying Java method: PGraphics.loadShader

        Methods
        -------

        You can use any of the following signatures:

         * load_shader(frag_filename: str, /) -> Py5Shader
         * load_shader(frag_filename: str, vert_filename: str, /) -> Py5Shader

        Parameters
        ----------

        frag_filename: str
            name of fragment shader file

        vert_filename: str
            name of vertex shader file

        Notes
        -----

        Loads a shader into a ``Py5Shader`` object. The shader file must be loaded in
        the Sketch's "data" directory to load correctly. Shaders are compatible with the
        ``P2D`` and ``P3D`` renderers, but not with the default renderer.

        Alternatively, the file maybe be loaded from anywhere on the local computer
        using an absolute path (something that starts with / on Unix and Linux, or a
        drive letter on Windows), or the filename parameter can be a URL for a file
        found on a network.

        If the file is not available or an error occurs, ``None`` will be returned and
        an error message will be printed to the console. The error message does not halt
        the program, however the ``None`` value may cause an error if your code does not
        check whether the value returned is ``None``.

        This method is the same as ``load_shader()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``load_shader()``.
        """
        return self._instance.loadShader(*args)

    @overload
    def load_shape(self, filename: str, /) -> Py5Shape:
        """Loads geometry into a variable of type ``Py5Shape``.

        Underlying Java method: PGraphics.loadShape

        Methods
        -------

        You can use any of the following signatures:

         * load_shape(filename: str, /) -> Py5Shape
         * load_shape(filename: str, options: str, /) -> Py5Shape

        Parameters
        ----------

        filename: str
            name of file to load, can be .svg or .obj

        options: str
            unused parameter

        Notes
        -----

        Loads geometry into a variable of type ``Py5Shape``. SVG and OBJ files may be
        loaded. To load correctly, the file must be located in the data directory of the
        current Sketch. In most cases, ``load_shape()`` should be used inside
        ``setup()`` because loading shapes inside ``draw()`` will reduce the speed of a
        Sketch.

        Alternatively, the file maybe be loaded from anywhere on the local computer
        using an absolute path (something that starts with / on Unix and Linux, or a
        drive letter on Windows), or the filename parameter can be a URL for a file
        found on a network.

        If the file is not available or an error occurs, ``None`` will be returned and
        an error message will be printed to the console. The error message does not halt
        the program, however the ``None`` value may cause errors if your code does not
        check whether the value returned is ``None``.

        This method is the same as ``load_shape()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``load_shape()``.
        """
        pass

    @overload
    def load_shape(self, filename: str, options: str, /) -> Py5Shape:
        """Loads geometry into a variable of type ``Py5Shape``.

        Underlying Java method: PGraphics.loadShape

        Methods
        -------

        You can use any of the following signatures:

         * load_shape(filename: str, /) -> Py5Shape
         * load_shape(filename: str, options: str, /) -> Py5Shape

        Parameters
        ----------

        filename: str
            name of file to load, can be .svg or .obj

        options: str
            unused parameter

        Notes
        -----

        Loads geometry into a variable of type ``Py5Shape``. SVG and OBJ files may be
        loaded. To load correctly, the file must be located in the data directory of the
        current Sketch. In most cases, ``load_shape()`` should be used inside
        ``setup()`` because loading shapes inside ``draw()`` will reduce the speed of a
        Sketch.

        Alternatively, the file maybe be loaded from anywhere on the local computer
        using an absolute path (something that starts with / on Unix and Linux, or a
        drive letter on Windows), or the filename parameter can be a URL for a file
        found on a network.

        If the file is not available or an error occurs, ``None`` will be returned and
        an error message will be printed to the console. The error message does not halt
        the program, however the ``None`` value may cause errors if your code does not
        check whether the value returned is ``None``.

        This method is the same as ``load_shape()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``load_shape()``.
        """
        pass

    @_load_py5shape
    def load_shape(self, *args):
        """Loads geometry into a variable of type ``Py5Shape``.

        Underlying Java method: PGraphics.loadShape

        Methods
        -------

        You can use any of the following signatures:

         * load_shape(filename: str, /) -> Py5Shape
         * load_shape(filename: str, options: str, /) -> Py5Shape

        Parameters
        ----------

        filename: str
            name of file to load, can be .svg or .obj

        options: str
            unused parameter

        Notes
        -----

        Loads geometry into a variable of type ``Py5Shape``. SVG and OBJ files may be
        loaded. To load correctly, the file must be located in the data directory of the
        current Sketch. In most cases, ``load_shape()`` should be used inside
        ``setup()`` because loading shapes inside ``draw()`` will reduce the speed of a
        Sketch.

        Alternatively, the file maybe be loaded from anywhere on the local computer
        using an absolute path (something that starts with / on Unix and Linux, or a
        drive letter on Windows), or the filename parameter can be a URL for a file
        found on a network.

        If the file is not available or an error occurs, ``None`` will be returned and
        an error message will be printed to the console. The error message does not halt
        the program, however the ``None`` value may cause errors if your code does not
        check whether the value returned is ``None``.

        This method is the same as ``load_shape()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``load_shape()``.
        """
        return self._instance.loadShape(*args)

    @overload
    def mask(self, mask_array: NDArray[(Any,), Int], /) -> None:
        """Masks part of the Py5Graphics drawing surface from displaying by loading an
        image and using it as an alpha channel.

        Underlying Java method: PGraphics.mask

        Methods
        -------

        You can use any of the following signatures:

         * mask(img: Py5Image, /) -> None
         * mask(mask_array: NDArray[(Any,), Int], /) -> None

        Parameters
        ----------

        img: Py5Image
            image to use as the mask

        mask_array: NDArray[(Any,), Int]
            array of integers used as the alpha channel, needs to be the same length as the image's pixel array.

        Notes
        -----

        Masks part of the Py5Graphics drawing surface from displaying by loading an
        image and using it as an alpha channel. This mask image should only contain
        grayscale data, but only the blue color channel is used. The mask image needs to
        be the same size as the image to which it is applied.

        In addition to using a mask image, an integer array containing the alpha channel
        data can be specified directly. This method is useful for creating dynamically
        generated alpha masks. This array must be of the same length as the target
        image's pixels array and should contain only grayscale data of values between
        0-255.
        """
        pass

    @overload
    def mask(self, img: Py5Image, /) -> None:
        """Masks part of the Py5Graphics drawing surface from displaying by loading an
        image and using it as an alpha channel.

        Underlying Java method: PGraphics.mask

        Methods
        -------

        You can use any of the following signatures:

         * mask(img: Py5Image, /) -> None
         * mask(mask_array: NDArray[(Any,), Int], /) -> None

        Parameters
        ----------

        img: Py5Image
            image to use as the mask

        mask_array: NDArray[(Any,), Int]
            array of integers used as the alpha channel, needs to be the same length as the image's pixel array.

        Notes
        -----

        Masks part of the Py5Graphics drawing surface from displaying by loading an
        image and using it as an alpha channel. This mask image should only contain
        grayscale data, but only the blue color channel is used. The mask image needs to
        be the same size as the image to which it is applied.

        In addition to using a mask image, an integer array containing the alpha channel
        data can be specified directly. This method is useful for creating dynamically
        generated alpha masks. This array must be of the same length as the target
        image's pixels array and should contain only grayscale data of values between
        0-255.
        """
        pass

    def mask(self, *args):
        """Masks part of the Py5Graphics drawing surface from displaying by loading an
        image and using it as an alpha channel.

        Underlying Java method: PGraphics.mask

        Methods
        -------

        You can use any of the following signatures:

         * mask(img: Py5Image, /) -> None
         * mask(mask_array: NDArray[(Any,), Int], /) -> None

        Parameters
        ----------

        img: Py5Image
            image to use as the mask

        mask_array: NDArray[(Any,), Int]
            array of integers used as the alpha channel, needs to be the same length as the image's pixel array.

        Notes
        -----

        Masks part of the Py5Graphics drawing surface from displaying by loading an
        image and using it as an alpha channel. This mask image should only contain
        grayscale data, but only the blue color channel is used. The mask image needs to
        be the same size as the image to which it is applied.

        In addition to using a mask image, an integer array containing the alpha channel
        data can be specified directly. This method is useful for creating dynamically
        generated alpha masks. This array must be of the same length as the target
        image's pixels array and should contain only grayscale data of values between
        0-255.
        """
        return self._instance.mask(*args)

    def model_x(self, x: float, y: float, z: float, /) -> float:
        """Returns the three-dimensional X, Y, Z position in model space.

        Underlying Java method: PGraphics.modelX

        Parameters
        ----------

        x: float
            3D x-coordinate to be mapped

        y: float
            3D y-coordinate to be mapped

        z: float
            3D z-coordinate to be mapped

        Notes
        -----

        Returns the three-dimensional X, Y, Z position in model space. This returns the
        X value for a given coordinate based on the current set of transformations
        (scale, rotate, translate, etc.) The X value can be used to place an object in
        space relative to the location of the original point once the transformations
        are no longer in use.

        To see an example for how this can be used, see ``model_x()``. In that example,
        the ``model_x()``, ``model_y()``, and ``model_z()`` methods (which are analogous
        to the ``model_x()``, ``Py5Graphics.model_y()``, and ``Py5Graphics.model_z()``
        methods) record the location of a box in space after being placed using a series
        of translate and rotate commands. After ``pop_matrix()`` is called, those
        transformations no longer apply, but the (x, y, z) coordinate returned by the
        model functions is used to place another box in the same location.

        This method is the same as ``model_x()`` but linked to a ``Py5Graphics`` object.
        """
        return self._instance.modelX(x, y, z)

    def model_y(self, x: float, y: float, z: float, /) -> float:
        """Returns the three-dimensional X, Y, Z position in model space.

        Underlying Java method: PGraphics.modelY

        Parameters
        ----------

        x: float
            3D x-coordinate to be mapped

        y: float
            3D y-coordinate to be mapped

        z: float
            3D z-coordinate to be mapped

        Notes
        -----

        Returns the three-dimensional X, Y, Z position in model space. This returns the
        Y value for a given coordinate based on the current set of transformations
        (scale, rotate, translate, etc.) The Y value can be used to place an object in
        space relative to the location of the original point once the transformations
        are no longer in use.

        To see an example for how this can be used, see ``model_y()``. In that example,
        the ``model_x()``, ``model_y()``, and ``model_z()`` methods (which are analogous
        to the ``Py5Graphics.model_x()``, ``model_y()``, and ``Py5Graphics.model_z()``
        methods) record the location of a box in space after being placed using a series
        of translate and rotate commands. After ``pop_matrix()`` is called, those
        transformations no longer apply, but the (x, y, z) coordinate returned by the
        model functions is used to place another box in the same location.

        This method is the same as ``model_y()`` but linked to a ``Py5Graphics`` object.
        """
        return self._instance.modelY(x, y, z)

    def model_z(self, x: float, y: float, z: float, /) -> float:
        """Returns the three-dimensional X, Y, Z position in model space.

        Underlying Java method: PGraphics.modelZ

        Parameters
        ----------

        x: float
            3D x-coordinate to be mapped

        y: float
            3D y-coordinate to be mapped

        z: float
            3D z-coordinate to be mapped

        Notes
        -----

        Returns the three-dimensional X, Y, Z position in model space. This returns the
        Z value for a given coordinate based on the current set of transformations
        (scale, rotate, translate, etc.) The Z value can be used to place an object in
        space relative to the location of the original point once the transformations
        are no longer in use.

        To see an example for how this can be used, see ``model_y()``. In that example,
        the ``model_x()``, ``model_y()``, and ``model_z()`` methods (which are analogous
        to the ``Py5Graphics.model_x()``, ``Py5Graphics.model_y()``, and ``model_z()``
        methods) record the location of a box in space after being placed using a series
        of translate and rotate commands. After ``pop_matrix()`` is called, those
        transformations no longer apply, but the (x, y, z) coordinate returned by the
        model functions is used to place another box in the same location.

        This method is the same as ``model_z()`` but linked to a ``Py5Graphics`` object.
        """
        return self._instance.modelZ(x, y, z)

    def no_clip(self) -> None:
        """Disables the clipping previously started by the ``Py5Graphics.clip()`` function.

        Underlying Java method: PGraphics.noClip

        Notes
        -----

        Disables the clipping previously started by the ``Py5Graphics.clip()`` function.

        This method is the same as ``no_clip()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``no_clip()``.
        """
        return self._instance.noClip()

    def no_fill(self) -> None:
        """Disables filling geometry.

        Underlying Java method: PGraphics.noFill

        Notes
        -----

        Disables filling geometry. If both ``Py5Graphics.no_stroke()`` and ``no_fill()``
        are called, nothing will be drawn to the screen.

        This method is the same as ``no_fill()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``no_fill()``.
        """
        return self._instance.noFill()

    def no_lights(self) -> None:
        """Disable all lighting.

        Underlying Java method: PGraphics.noLights

        Notes
        -----

        Disable all lighting. Lighting is turned off by default and enabled with the
        ``Py5Graphics.lights()`` function. This function can be used to disable lighting
        so that 2D geometry (which does not require lighting) can be drawn after a set
        of lighted 3D geometry.

        This method is the same as ``no_lights()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``no_lights()``.
        """
        return self._instance.noLights()

    def no_smooth(self) -> None:
        """Draws all geometry and fonts with jagged (aliased) edges and images with hard
        edges between the pixels when enlarged rather than interpolating pixels.

        Underlying Java method: PGraphics.noSmooth

        Notes
        -----

        Draws all geometry and fonts with jagged (aliased) edges and images with hard
        edges between the pixels when enlarged rather than interpolating pixels.  Note
        that ``Py5Graphics.smooth()`` is active by default, so it is necessary to call
        ``no_smooth()`` to disable smoothing of geometry, fonts, and images. The
        ``no_smooth()`` method can only be run once for a ``Py5Graphics`` object and it
        must be called before ``Py5Graphics.begin_draw()``.

        This method is the same as ``no_smooth()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``no_smooth()``.
        """
        return self._instance.noSmooth()

    def no_stroke(self) -> None:
        """Disables drawing the stroke (outline).

        Underlying Java method: PGraphics.noStroke

        Notes
        -----

        Disables drawing the stroke (outline). If both ``no_stroke()`` and
        ``Py5Graphics.no_fill()`` are called, nothing will be drawn to the screen.

        This method is the same as ``no_stroke()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``no_stroke()``.
        """
        return self._instance.noStroke()

    def no_tint(self) -> None:
        """Removes the current fill value for displaying images and reverts to displaying
        images with their original hues.

        Underlying Java method: PGraphics.noTint

        Notes
        -----

        Removes the current fill value for displaying images and reverts to displaying
        images with their original hues.

        This method is the same as ``no_tint()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``no_tint()``.
        """
        return self._instance.noTint()

    def normal(self, nx: float, ny: float, nz: float, /) -> None:
        """Sets the current normal vector.

        Underlying Java method: PGraphics.normal

        Parameters
        ----------

        nx: float
            x direction

        ny: float
            y direction

        nz: float
            z direction

        Notes
        -----

        Sets the current normal vector. Used for drawing three dimensional shapes and
        surfaces, ``normal()`` specifies a vector perpendicular to a shape's surface
        which, in turn, determines how lighting affects it. Py5 attempts to
        automatically assign normals to shapes, but since that's imperfect, this is a
        better option when you want more control. This function is identical to
        ``gl_normal3f()`` in OpenGL.

        This method is the same as ``normal()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``normal()``.
        """
        return self._instance.normal(nx, ny, nz)

    @overload
    def ortho(self) -> None:
        """Sets an orthographic projection and defines a parallel clipping volume.

        Underlying Java method: PGraphics.ortho

        Methods
        -------

        You can use any of the following signatures:

         * ortho() -> None
         * ortho(left: float, right: float, bottom: float, top: float, /) -> None
         * ortho(left: float, right: float, bottom: float, top: float, near: float, far: float, /) -> None

        Parameters
        ----------

        bottom: float
            bottom plane of the clipping volume

        far: float
            maximum distance from the origin away from the viewer

        left: float
            left plane of the clipping volume

        near: float
            maximum distance from the origin to the viewer

        right: float
            right plane of the clipping volume

        top: float
            top plane of the clipping volume

        Notes
        -----

        Sets an orthographic projection and defines a parallel clipping volume. All
        objects with the same dimension appear the same size, regardless of whether they
        are near or far from the camera. The parameters to this function specify the
        clipping volume where left and right are the minimum and maximum x values, top
        and bottom are the minimum and maximum y values, and near and far are the
        minimum and maximum z values. If no parameters are given, the default is used:
        ``ortho(-width/2, width/2, -height/2, height/2)``.

        This method is the same as ``ortho()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``ortho()``.
        """
        pass

    @overload
    def ortho(self, left: float, right: float,
              bottom: float, top: float, /) -> None:
        """Sets an orthographic projection and defines a parallel clipping volume.

        Underlying Java method: PGraphics.ortho

        Methods
        -------

        You can use any of the following signatures:

         * ortho() -> None
         * ortho(left: float, right: float, bottom: float, top: float, /) -> None
         * ortho(left: float, right: float, bottom: float, top: float, near: float, far: float, /) -> None

        Parameters
        ----------

        bottom: float
            bottom plane of the clipping volume

        far: float
            maximum distance from the origin away from the viewer

        left: float
            left plane of the clipping volume

        near: float
            maximum distance from the origin to the viewer

        right: float
            right plane of the clipping volume

        top: float
            top plane of the clipping volume

        Notes
        -----

        Sets an orthographic projection and defines a parallel clipping volume. All
        objects with the same dimension appear the same size, regardless of whether they
        are near or far from the camera. The parameters to this function specify the
        clipping volume where left and right are the minimum and maximum x values, top
        and bottom are the minimum and maximum y values, and near and far are the
        minimum and maximum z values. If no parameters are given, the default is used:
        ``ortho(-width/2, width/2, -height/2, height/2)``.

        This method is the same as ``ortho()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``ortho()``.
        """
        pass

    @overload
    def ortho(self, left: float, right: float, bottom: float,
              top: float, near: float, far: float, /) -> None:
        """Sets an orthographic projection and defines a parallel clipping volume.

        Underlying Java method: PGraphics.ortho

        Methods
        -------

        You can use any of the following signatures:

         * ortho() -> None
         * ortho(left: float, right: float, bottom: float, top: float, /) -> None
         * ortho(left: float, right: float, bottom: float, top: float, near: float, far: float, /) -> None

        Parameters
        ----------

        bottom: float
            bottom plane of the clipping volume

        far: float
            maximum distance from the origin away from the viewer

        left: float
            left plane of the clipping volume

        near: float
            maximum distance from the origin to the viewer

        right: float
            right plane of the clipping volume

        top: float
            top plane of the clipping volume

        Notes
        -----

        Sets an orthographic projection and defines a parallel clipping volume. All
        objects with the same dimension appear the same size, regardless of whether they
        are near or far from the camera. The parameters to this function specify the
        clipping volume where left and right are the minimum and maximum x values, top
        and bottom are the minimum and maximum y values, and near and far are the
        minimum and maximum z values. If no parameters are given, the default is used:
        ``ortho(-width/2, width/2, -height/2, height/2)``.

        This method is the same as ``ortho()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``ortho()``.
        """
        pass

    def ortho(self, *args):
        """Sets an orthographic projection and defines a parallel clipping volume.

        Underlying Java method: PGraphics.ortho

        Methods
        -------

        You can use any of the following signatures:

         * ortho() -> None
         * ortho(left: float, right: float, bottom: float, top: float, /) -> None
         * ortho(left: float, right: float, bottom: float, top: float, near: float, far: float, /) -> None

        Parameters
        ----------

        bottom: float
            bottom plane of the clipping volume

        far: float
            maximum distance from the origin away from the viewer

        left: float
            left plane of the clipping volume

        near: float
            maximum distance from the origin to the viewer

        right: float
            right plane of the clipping volume

        top: float
            top plane of the clipping volume

        Notes
        -----

        Sets an orthographic projection and defines a parallel clipping volume. All
        objects with the same dimension appear the same size, regardless of whether they
        are near or far from the camera. The parameters to this function specify the
        clipping volume where left and right are the minimum and maximum x values, top
        and bottom are the minimum and maximum y values, and near and far are the
        minimum and maximum z values. If no parameters are given, the default is used:
        ``ortho(-width/2, width/2, -height/2, height/2)``.

        This method is the same as ``ortho()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``ortho()``.
        """
        return self._instance.ortho(*args)

    @overload
    def perspective(self) -> None:
        """Sets a perspective projection applying foreshortening, making distant objects
        appear smaller than closer ones.

        Underlying Java method: PGraphics.perspective

        Methods
        -------

        You can use any of the following signatures:

         * perspective() -> None
         * perspective(fovy: float, aspect: float, z_near: float, z_far: float, /) -> None

        Parameters
        ----------

        aspect: float
            ratio of width to height

        fovy: float
            field-of-view angle (in radians) for vertical direction

        z_far: float
            z-position of farthest clipping plane

        z_near: float
            z-position of nearest clipping plane

        Notes
        -----

        Sets a perspective projection applying foreshortening, making distant objects
        appear smaller than closer ones. The parameters define a viewing volume with the
        shape of truncated pyramid. Objects near to the front of the volume appear their
        actual size, while farther objects appear smaller. This projection simulates the
        perspective of the world more accurately than orthographic projection. The
        version of perspective without parameters sets the default perspective and the
        version with four parameters allows the programmer to set the area precisely.
        The default values are: ``perspective(PI/3.0, width/height, cameraZ/10.0,
        cameraZ*10.0)`` where cameraZ is ``((height/2.0) / tan(PI*60.0/360.0))``.

        This method is the same as ``perspective()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``perspective()``.
        """
        pass

    @overload
    def perspective(self, fovy: float, aspect: float,
                    z_near: float, z_far: float, /) -> None:
        """Sets a perspective projection applying foreshortening, making distant objects
        appear smaller than closer ones.

        Underlying Java method: PGraphics.perspective

        Methods
        -------

        You can use any of the following signatures:

         * perspective() -> None
         * perspective(fovy: float, aspect: float, z_near: float, z_far: float, /) -> None

        Parameters
        ----------

        aspect: float
            ratio of width to height

        fovy: float
            field-of-view angle (in radians) for vertical direction

        z_far: float
            z-position of farthest clipping plane

        z_near: float
            z-position of nearest clipping plane

        Notes
        -----

        Sets a perspective projection applying foreshortening, making distant objects
        appear smaller than closer ones. The parameters define a viewing volume with the
        shape of truncated pyramid. Objects near to the front of the volume appear their
        actual size, while farther objects appear smaller. This projection simulates the
        perspective of the world more accurately than orthographic projection. The
        version of perspective without parameters sets the default perspective and the
        version with four parameters allows the programmer to set the area precisely.
        The default values are: ``perspective(PI/3.0, width/height, cameraZ/10.0,
        cameraZ*10.0)`` where cameraZ is ``((height/2.0) / tan(PI*60.0/360.0))``.

        This method is the same as ``perspective()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``perspective()``.
        """
        pass

    def perspective(self, *args):
        """Sets a perspective projection applying foreshortening, making distant objects
        appear smaller than closer ones.

        Underlying Java method: PGraphics.perspective

        Methods
        -------

        You can use any of the following signatures:

         * perspective() -> None
         * perspective(fovy: float, aspect: float, z_near: float, z_far: float, /) -> None

        Parameters
        ----------

        aspect: float
            ratio of width to height

        fovy: float
            field-of-view angle (in radians) for vertical direction

        z_far: float
            z-position of farthest clipping plane

        z_near: float
            z-position of nearest clipping plane

        Notes
        -----

        Sets a perspective projection applying foreshortening, making distant objects
        appear smaller than closer ones. The parameters define a viewing volume with the
        shape of truncated pyramid. Objects near to the front of the volume appear their
        actual size, while farther objects appear smaller. This projection simulates the
        perspective of the world more accurately than orthographic projection. The
        version of perspective without parameters sets the default perspective and the
        version with four parameters allows the programmer to set the area precisely.
        The default values are: ``perspective(PI/3.0, width/height, cameraZ/10.0,
        cameraZ*10.0)`` where cameraZ is ``((height/2.0) / tan(PI*60.0/360.0))``.

        This method is the same as ``perspective()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``perspective()``.
        """
        return self._instance.perspective(*args)

    @overload
    def point(self, x: float, y: float, /) -> None:
        """Draws a point, a coordinate in space at the dimension of one pixel.

        Underlying Java method: PGraphics.point

        Methods
        -------

        You can use any of the following signatures:

         * point(x: float, y: float, /) -> None
         * point(x: float, y: float, z: float, /) -> None

        Parameters
        ----------

        x: float
            x-coordinate of the point

        y: float
            y-coordinate of the point

        z: float
            z-coordinate of the point

        Notes
        -----

        Draws a point, a coordinate in space at the dimension of one pixel. The first
        parameter is the horizontal value for the point, the second value is the
        vertical value for the point, and the optional third value is the depth value.
        Drawing this shape in 3D with the ``z`` parameter requires the ``P3D`` renderer.

        Use ``Py5Graphics.stroke()`` to set the color of a ``point()``.

        Point appears round with the default ``stroke_cap(ROUND)`` and square with
        ``stroke_cap(PROJECT)``. Points are invisible with ``stroke_cap(SQUARE)`` (no
        cap).

        Using ``point()`` with ``strokeWeight(1)`` or smaller may draw nothing to the
        Py5Graphics drawing surface, depending on the graphics settings of the computer.
        Workarounds include setting the pixel using the ``Py5Graphics.pixels[]`` or
        ``Py5Graphics.np_pixels[]`` arrays or drawing the point using either
        ``Py5Graphics.circle()`` or ``Py5Graphics.square()``.

        This method is the same as ``point()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``point()``.
        """
        pass

    @overload
    def point(self, x: float, y: float, z: float, /) -> None:
        """Draws a point, a coordinate in space at the dimension of one pixel.

        Underlying Java method: PGraphics.point

        Methods
        -------

        You can use any of the following signatures:

         * point(x: float, y: float, /) -> None
         * point(x: float, y: float, z: float, /) -> None

        Parameters
        ----------

        x: float
            x-coordinate of the point

        y: float
            y-coordinate of the point

        z: float
            z-coordinate of the point

        Notes
        -----

        Draws a point, a coordinate in space at the dimension of one pixel. The first
        parameter is the horizontal value for the point, the second value is the
        vertical value for the point, and the optional third value is the depth value.
        Drawing this shape in 3D with the ``z`` parameter requires the ``P3D`` renderer.

        Use ``Py5Graphics.stroke()`` to set the color of a ``point()``.

        Point appears round with the default ``stroke_cap(ROUND)`` and square with
        ``stroke_cap(PROJECT)``. Points are invisible with ``stroke_cap(SQUARE)`` (no
        cap).

        Using ``point()`` with ``strokeWeight(1)`` or smaller may draw nothing to the
        Py5Graphics drawing surface, depending on the graphics settings of the computer.
        Workarounds include setting the pixel using the ``Py5Graphics.pixels[]`` or
        ``Py5Graphics.np_pixels[]`` arrays or drawing the point using either
        ``Py5Graphics.circle()`` or ``Py5Graphics.square()``.

        This method is the same as ``point()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``point()``.
        """
        pass

    def point(self, *args):
        """Draws a point, a coordinate in space at the dimension of one pixel.

        Underlying Java method: PGraphics.point

        Methods
        -------

        You can use any of the following signatures:

         * point(x: float, y: float, /) -> None
         * point(x: float, y: float, z: float, /) -> None

        Parameters
        ----------

        x: float
            x-coordinate of the point

        y: float
            y-coordinate of the point

        z: float
            z-coordinate of the point

        Notes
        -----

        Draws a point, a coordinate in space at the dimension of one pixel. The first
        parameter is the horizontal value for the point, the second value is the
        vertical value for the point, and the optional third value is the depth value.
        Drawing this shape in 3D with the ``z`` parameter requires the ``P3D`` renderer.

        Use ``Py5Graphics.stroke()`` to set the color of a ``point()``.

        Point appears round with the default ``stroke_cap(ROUND)`` and square with
        ``stroke_cap(PROJECT)``. Points are invisible with ``stroke_cap(SQUARE)`` (no
        cap).

        Using ``point()`` with ``strokeWeight(1)`` or smaller may draw nothing to the
        Py5Graphics drawing surface, depending on the graphics settings of the computer.
        Workarounds include setting the pixel using the ``Py5Graphics.pixels[]`` or
        ``Py5Graphics.np_pixels[]`` arrays or drawing the point using either
        ``Py5Graphics.circle()`` or ``Py5Graphics.square()``.

        This method is the same as ``point()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``point()``.
        """
        return self._instance.point(*args)

    def point_light(self, v1: float, v2: float, v3: float,
                    x: float, y: float, z: float, /) -> None:
        """Adds a point light.

        Underlying Java method: PGraphics.pointLight

        Parameters
        ----------

        v1: float
            red or hue value (depending on current color mode)

        v2: float
            green or saturation value (depending on current color mode)

        v3: float
            blue or brightness value (depending on current color mode)

        x: float
            x-coordinate of the light

        y: float
            y-coordinate of the light

        z: float
            z-coordinate of the light

        Notes
        -----

        Adds a point light. The ``v1``, ``v2``, and ``v3`` parameters are interpreted as
        either RGB or HSB values, depending on the current color mode. The ``x``, ``y``,
        and ``z`` parameters set the position of the light.

        This method is the same as ``point_light()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``point_light()``.
        """
        return self._instance.pointLight(v1, v2, v3, x, y, z)

    def pop(self) -> None:
        """The ``pop()`` function restores the previous drawing style settings and
        transformations after ``Py5Graphics.push()`` has changed them.

        Underlying Java method: PGraphics.pop

        Notes
        -----

        The ``pop()`` function restores the previous drawing style settings and
        transformations after ``Py5Graphics.push()`` has changed them. Note that these
        functions are always used together. They allow you to change the style and
        transformation settings and later return to what you had. When a new state is
        started with ``Py5Graphics.push()``, it builds on the current style and
        transform information.

        ``Py5Graphics.push()`` stores information related to the current transformation
        state and style settings controlled by the following functions:
        ``Py5Graphics.rotate()``, ``Py5Graphics.translate()``, ``Py5Graphics.scale()``,
        ``Py5Graphics.fill()``, ``Py5Graphics.stroke()``, ``Py5Graphics.tint()``,
        ``Py5Graphics.stroke_weight()``, ``Py5Graphics.stroke_cap()``,
        ``Py5Graphics.stroke_join()``, ``Py5Graphics.image_mode()``,
        ``Py5Graphics.rect_mode()``, ``Py5Graphics.ellipse_mode()``,
        ``Py5Graphics.color_mode()``, ``Py5Graphics.text_align()``,
        ``Py5Graphics.text_font()``, ``Py5Graphics.text_mode()``,
        ``Py5Graphics.text_size()``, and ``Py5Graphics.text_leading()``.

        The ``Py5Graphics.push()`` and ``pop()`` functions can be used in place of
        ``Py5Graphics.push_matrix()``, ``Py5Graphics.pop_matrix()``, ``push_styles()``,
        and ``pop_styles()``. The difference is that ``Py5Graphics.push()`` and
        ``pop()`` control both the transformations (rotate, scale, translate) and the
        drawing styles at the same time.

        This method is the same as ``pop()`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``pop()``.
        """
        return self._instance.pop()

    def pop_matrix(self) -> None:
        """Pops the current transformation matrix off the matrix stack.

        Underlying Java method: PGraphics.popMatrix

        Notes
        -----

        Pops the current transformation matrix off the matrix stack. Understanding
        pushing and popping requires understanding the concept of a matrix stack. The
        ``Py5Graphics.push_matrix()`` function saves the current coordinate system to
        the stack and ``pop_matrix()`` restores the prior coordinate system.
        ``Py5Graphics.push_matrix()`` and ``pop_matrix()`` are used in conjuction with
        the other transformation functions and may be embedded to control the scope of
        the transformations.

        This method is the same as ``pop_matrix()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``pop_matrix()``.
        """
        return self._instance.popMatrix()

    def pop_style(self) -> None:
        """The ``Py5Graphics.push_style()`` function saves the current style settings and
        ``pop_style()`` restores the prior settings; these functions are always used
        together.

        Underlying Java method: PGraphics.popStyle

        Notes
        -----

        The ``Py5Graphics.push_style()`` function saves the current style settings and
        ``pop_style()`` restores the prior settings; these functions are always used
        together. They allow you to change the style settings and later return to what
        you had. When a new style is started with ``Py5Graphics.push_style()``, it
        builds on the current style information. The ``Py5Graphics.push_style()`` and
        ``pop_style()`` method pairs can be nested to provide more control.

        This method is the same as ``pop_style()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``pop_style()``.
        """
        return self._instance.popStyle()

    def print_camera(self) -> None:
        """Prints the current camera matrix to standard output.

        Underlying Java method: PGraphics.printCamera

        Notes
        -----

        Prints the current camera matrix to standard output.

        This method is the same as ``print_camera()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``print_camera()``.
        """
        return self._instance.printCamera()

    def print_matrix(self) -> None:
        """Prints the current matrix to standard output.

        Underlying Java method: PGraphics.printMatrix

        Notes
        -----

        Prints the current matrix to standard output.

        This method is the same as ``print_matrix()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``print_matrix()``.
        """
        return self._instance.printMatrix()

    def print_projection(self) -> None:
        """Prints the current projection matrix to standard output.

        Underlying Java method: PGraphics.printProjection

        Notes
        -----

        Prints the current projection matrix to standard output.

        This method is the same as ``print_projection()`` but linked to a
        ``Py5Graphics`` object. To see example code for how it can be used, see
        ``print_projection()``.
        """
        return self._instance.printProjection()

    def push(self) -> None:
        """The ``push()`` function saves the current drawing style settings and
        transformations, while ``Py5Graphics.pop()`` restores these settings.

        Underlying Java method: PGraphics.push

        Notes
        -----

        The ``push()`` function saves the current drawing style settings and
        transformations, while ``Py5Graphics.pop()`` restores these settings. Note that
        these functions are always used together. They allow you to change the style and
        transformation settings and later return to what you had. When a new state is
        started with ``push()``, it builds on the current style and transform
        information.

        ``push()`` stores information related to the current transformation state and
        style settings controlled by the following functions: ``Py5Graphics.rotate()``,
        ``Py5Graphics.translate()``, ``Py5Graphics.scale()``, ``Py5Graphics.fill()``,
        ``Py5Graphics.stroke()``, ``Py5Graphics.tint()``,
        ``Py5Graphics.stroke_weight()``, ``Py5Graphics.stroke_cap()``,
        ``Py5Graphics.stroke_join()``, ``Py5Graphics.image_mode()``,
        ``Py5Graphics.rect_mode()``, ``Py5Graphics.ellipse_mode()``,
        ``Py5Graphics.color_mode()``, ``Py5Graphics.text_align()``,
        ``Py5Graphics.text_font()``, ``Py5Graphics.text_mode()``,
        ``Py5Graphics.text_size()``, ``Py5Graphics.text_leading()``.

        The ``push()`` and ``Py5Graphics.pop()`` functions can be used in place of
        ``Py5Graphics.push_matrix()``, ``Py5Graphics.pop_matrix()``, ``push_styles()``,
        and ``pop_styles()``. The difference is that ``push()`` and
        ``Py5Graphics.pop()`` control both the transformations (rotate, scale,
        translate) and the drawing styles at the same time.

        This method is the same as ``push()`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``push()``.
        """
        return self._instance.push()

    def push_matrix(self) -> None:
        """Pushes the current transformation matrix onto the matrix stack.

        Underlying Java method: PGraphics.pushMatrix

        Notes
        -----

        Pushes the current transformation matrix onto the matrix stack. Understanding
        ``push_matrix()`` and ``Py5Graphics.pop_matrix()`` requires understanding the
        concept of a matrix stack. The ``push_matrix()`` function saves the current
        coordinate system to the stack and ``Py5Graphics.pop_matrix()`` restores the
        prior coordinate system. ``push_matrix()`` and ``Py5Graphics.pop_matrix()`` are
        used in conjuction with the other transformation functions and may be embedded
        to control the scope of the transformations.

        This method is the same as ``push_matrix()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``push_matrix()``.
        """
        return self._instance.pushMatrix()

    def push_style(self) -> None:
        """The ``push_style()`` function saves the current style settings and
        ``Py5Graphics.pop_style()`` restores the prior settings.

        Underlying Java method: PGraphics.pushStyle

        Notes
        -----

        The ``push_style()`` function saves the current style settings and
        ``Py5Graphics.pop_style()`` restores the prior settings. Note that these
        functions are always used together. They allow you to change the style settings
        and later return to what you had. When a new style is started with
        ``push_style()``, it builds on the current style information. The
        ``push_style()`` and ``Py5Graphics.pop_style()`` method pairs can be nested to
        provide more control. (See the second example for a demonstration.)

        The style information controlled by the following functions are included in the
        style: ``Py5Graphics.fill()``, ``Py5Graphics.stroke()``, ``Py5Graphics.tint()``,
        ``Py5Graphics.stroke_weight()``, ``Py5Graphics.stroke_cap()``,
        ``Py5Graphics.stroke_join()``, ``Py5Graphics.image_mode()``,
        ``Py5Graphics.rect_mode()``, ``Py5Graphics.ellipse_mode()``,
        ``Py5Graphics.shape_mode()``, ``Py5Graphics.color_mode()``,
        ``Py5Graphics.text_align()``, ``Py5Graphics.text_font()``,
        ``Py5Graphics.text_mode()``, ``Py5Graphics.text_size()``,
        ``Py5Graphics.text_leading()``, ``Py5Graphics.emissive()``,
        ``Py5Graphics.specular()``, ``Py5Graphics.shininess()``, and
        ``Py5Graphics.ambient()``.

        This method is the same as ``push_style()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``push_style()``.
        """
        return self._instance.pushStyle()

    def quad(self, x1: float, y1: float, x2: float, y2: float,
             x3: float, y3: float, x4: float, y4: float, /) -> None:
        """A quad is a quadrilateral, a four sided polygon.

        Underlying Java method: PGraphics.quad

        Parameters
        ----------

        x1: float
            x-coordinate of the first corner

        x2: float
            x-coordinate of the second corner

        x3: float
            x-coordinate of the third corner

        x4: float
            x-coordinate of the fourth corner

        y1: float
            y-coordinate of the first corner

        y2: float
            y-coordinate of the second corner

        y3: float
            y-coordinate of the third corner

        y4: float
            y-coordinate of the fourth corner

        Notes
        -----

        A quad is a quadrilateral, a four sided polygon. It is similar to a rectangle,
        but the angles between its edges are not constrained to ninety degrees. The
        first pair of parameters (x1,y1) sets the first vertex and the subsequent pairs
        should proceed clockwise or counter-clockwise around the defined shape.

        This method is the same as ``quad()`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``quad()``.
        """
        return self._instance.quad(x1, y1, x2, y2, x3, y3, x4, y4)

    @overload
    def quadratic_vertex(self, cx: float, cy: float,
                         x3: float, y3: float, /) -> None:
        """Specifies vertex coordinates for quadratic Bezier curves.

        Underlying Java method: PGraphics.quadraticVertex

        Methods
        -------

        You can use any of the following signatures:

         * quadratic_vertex(cx: float, cy: float, cz: float, x3: float, y3: float, z3: float, /) -> None
         * quadratic_vertex(cx: float, cy: float, x3: float, y3: float, /) -> None

        Parameters
        ----------

        cx: float
            the x-coordinate of the control point

        cy: float
            the y-coordinate of the control point

        cz: float
            the z-coordinate of the control point

        x3: float
            the x-coordinate of the anchor point

        y3: float
            the y-coordinate of the anchor point

        z3: float
            the z-coordinate of the anchor point

        Notes
        -----

        Specifies vertex coordinates for quadratic Bezier curves. Each call to
        ``quadratic_vertex()`` defines the position of one control point and one anchor
        point of a Bezier curve, adding a new segment to a line or shape. The first time
        ``quadratic_vertex()`` is used within a ``Py5Graphics.begin_shape()`` call, it
        must be prefaced with a call to ``Py5Graphics.vertex()`` to set the first anchor
        point. This method must be used between ``Py5Graphics.begin_shape()`` and
        ``Py5Graphics.end_shape()`` and only when there is no ``MODE`` parameter
        specified to ``Py5Graphics.begin_shape()``. Using the 3D version requires
        rendering with ``P3D``.

        This method is the same as ``quadratic_vertex()`` but linked to a
        ``Py5Graphics`` object. To see example code for how it can be used, see
        ``quadratic_vertex()``.
        """
        pass

    @overload
    def quadratic_vertex(self, cx: float, cy: float, cz: float,
                         x3: float, y3: float, z3: float, /) -> None:
        """Specifies vertex coordinates for quadratic Bezier curves.

        Underlying Java method: PGraphics.quadraticVertex

        Methods
        -------

        You can use any of the following signatures:

         * quadratic_vertex(cx: float, cy: float, cz: float, x3: float, y3: float, z3: float, /) -> None
         * quadratic_vertex(cx: float, cy: float, x3: float, y3: float, /) -> None

        Parameters
        ----------

        cx: float
            the x-coordinate of the control point

        cy: float
            the y-coordinate of the control point

        cz: float
            the z-coordinate of the control point

        x3: float
            the x-coordinate of the anchor point

        y3: float
            the y-coordinate of the anchor point

        z3: float
            the z-coordinate of the anchor point

        Notes
        -----

        Specifies vertex coordinates for quadratic Bezier curves. Each call to
        ``quadratic_vertex()`` defines the position of one control point and one anchor
        point of a Bezier curve, adding a new segment to a line or shape. The first time
        ``quadratic_vertex()`` is used within a ``Py5Graphics.begin_shape()`` call, it
        must be prefaced with a call to ``Py5Graphics.vertex()`` to set the first anchor
        point. This method must be used between ``Py5Graphics.begin_shape()`` and
        ``Py5Graphics.end_shape()`` and only when there is no ``MODE`` parameter
        specified to ``Py5Graphics.begin_shape()``. Using the 3D version requires
        rendering with ``P3D``.

        This method is the same as ``quadratic_vertex()`` but linked to a
        ``Py5Graphics`` object. To see example code for how it can be used, see
        ``quadratic_vertex()``.
        """
        pass

    def quadratic_vertex(self, *args):
        """Specifies vertex coordinates for quadratic Bezier curves.

        Underlying Java method: PGraphics.quadraticVertex

        Methods
        -------

        You can use any of the following signatures:

         * quadratic_vertex(cx: float, cy: float, cz: float, x3: float, y3: float, z3: float, /) -> None
         * quadratic_vertex(cx: float, cy: float, x3: float, y3: float, /) -> None

        Parameters
        ----------

        cx: float
            the x-coordinate of the control point

        cy: float
            the y-coordinate of the control point

        cz: float
            the z-coordinate of the control point

        x3: float
            the x-coordinate of the anchor point

        y3: float
            the y-coordinate of the anchor point

        z3: float
            the z-coordinate of the anchor point

        Notes
        -----

        Specifies vertex coordinates for quadratic Bezier curves. Each call to
        ``quadratic_vertex()`` defines the position of one control point and one anchor
        point of a Bezier curve, adding a new segment to a line or shape. The first time
        ``quadratic_vertex()`` is used within a ``Py5Graphics.begin_shape()`` call, it
        must be prefaced with a call to ``Py5Graphics.vertex()`` to set the first anchor
        point. This method must be used between ``Py5Graphics.begin_shape()`` and
        ``Py5Graphics.end_shape()`` and only when there is no ``MODE`` parameter
        specified to ``Py5Graphics.begin_shape()``. Using the 3D version requires
        rendering with ``P3D``.

        This method is the same as ``quadratic_vertex()`` but linked to a
        ``Py5Graphics`` object. To see example code for how it can be used, see
        ``quadratic_vertex()``.
        """
        return self._instance.quadraticVertex(*args)

    @overload
    def rect(self, a: float, b: float, c: float, d: float, /) -> None:
        """Draws a rectangle to the Py5Graphics drawing surface.

        Underlying Java method: PGraphics.rect

        Methods
        -------

        You can use any of the following signatures:

         * rect(a: float, b: float, c: float, d: float, /) -> None
         * rect(a: float, b: float, c: float, d: float, r: float, /) -> None
         * rect(a: float, b: float, c: float, d: float, tl: float, tr: float, br: float, bl: float, /) -> None

        Parameters
        ----------

        a: float
            x-coordinate of the rectangle by default

        b: float
            y-coordinate of the rectangle by default

        bl: float
            radius for bottom-left corner

        br: float
            radius for bottom-right corner

        c: float
            width of the rectangle by default

        d: float
            height of the rectangle by default

        r: float
            radii for all four corners

        tl: float
            radius for top-left corner

        tr: float
            radius for top-right corner

        Notes
        -----

        Draws a rectangle to the Py5Graphics drawing surface. A rectangle is a four-
        sided shape with every angle at ninety degrees. By default, the first two
        parameters set the location of the upper-left corner, the third sets the width,
        and the fourth sets the height. The way these parameters are interpreted,
        however, may be changed with the ``Py5Graphics.rect_mode()`` function.

        To draw a rounded rectangle, add a fifth parameter, which is used as the radius
        value for all four corners.

        To use a different radius value for each corner, include eight parameters. When
        using eight parameters, the latter four set the radius of the arc at each corner
        separately, starting with the top-left corner and moving clockwise around the
        rectangle.

        This method is the same as ``rect()`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``rect()``.
        """
        pass

    @overload
    def rect(self, a: float, b: float, c: float,
             d: float, r: float, /) -> None:
        """Draws a rectangle to the Py5Graphics drawing surface.

        Underlying Java method: PGraphics.rect

        Methods
        -------

        You can use any of the following signatures:

         * rect(a: float, b: float, c: float, d: float, /) -> None
         * rect(a: float, b: float, c: float, d: float, r: float, /) -> None
         * rect(a: float, b: float, c: float, d: float, tl: float, tr: float, br: float, bl: float, /) -> None

        Parameters
        ----------

        a: float
            x-coordinate of the rectangle by default

        b: float
            y-coordinate of the rectangle by default

        bl: float
            radius for bottom-left corner

        br: float
            radius for bottom-right corner

        c: float
            width of the rectangle by default

        d: float
            height of the rectangle by default

        r: float
            radii for all four corners

        tl: float
            radius for top-left corner

        tr: float
            radius for top-right corner

        Notes
        -----

        Draws a rectangle to the Py5Graphics drawing surface. A rectangle is a four-
        sided shape with every angle at ninety degrees. By default, the first two
        parameters set the location of the upper-left corner, the third sets the width,
        and the fourth sets the height. The way these parameters are interpreted,
        however, may be changed with the ``Py5Graphics.rect_mode()`` function.

        To draw a rounded rectangle, add a fifth parameter, which is used as the radius
        value for all four corners.

        To use a different radius value for each corner, include eight parameters. When
        using eight parameters, the latter four set the radius of the arc at each corner
        separately, starting with the top-left corner and moving clockwise around the
        rectangle.

        This method is the same as ``rect()`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``rect()``.
        """
        pass

    @overload
    def rect(self, a: float, b: float, c: float, d: float,
             tl: float, tr: float, br: float, bl: float, /) -> None:
        """Draws a rectangle to the Py5Graphics drawing surface.

        Underlying Java method: PGraphics.rect

        Methods
        -------

        You can use any of the following signatures:

         * rect(a: float, b: float, c: float, d: float, /) -> None
         * rect(a: float, b: float, c: float, d: float, r: float, /) -> None
         * rect(a: float, b: float, c: float, d: float, tl: float, tr: float, br: float, bl: float, /) -> None

        Parameters
        ----------

        a: float
            x-coordinate of the rectangle by default

        b: float
            y-coordinate of the rectangle by default

        bl: float
            radius for bottom-left corner

        br: float
            radius for bottom-right corner

        c: float
            width of the rectangle by default

        d: float
            height of the rectangle by default

        r: float
            radii for all four corners

        tl: float
            radius for top-left corner

        tr: float
            radius for top-right corner

        Notes
        -----

        Draws a rectangle to the Py5Graphics drawing surface. A rectangle is a four-
        sided shape with every angle at ninety degrees. By default, the first two
        parameters set the location of the upper-left corner, the third sets the width,
        and the fourth sets the height. The way these parameters are interpreted,
        however, may be changed with the ``Py5Graphics.rect_mode()`` function.

        To draw a rounded rectangle, add a fifth parameter, which is used as the radius
        value for all four corners.

        To use a different radius value for each corner, include eight parameters. When
        using eight parameters, the latter four set the radius of the arc at each corner
        separately, starting with the top-left corner and moving clockwise around the
        rectangle.

        This method is the same as ``rect()`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``rect()``.
        """
        pass

    def rect(self, *args):
        """Draws a rectangle to the Py5Graphics drawing surface.

        Underlying Java method: PGraphics.rect

        Methods
        -------

        You can use any of the following signatures:

         * rect(a: float, b: float, c: float, d: float, /) -> None
         * rect(a: float, b: float, c: float, d: float, r: float, /) -> None
         * rect(a: float, b: float, c: float, d: float, tl: float, tr: float, br: float, bl: float, /) -> None

        Parameters
        ----------

        a: float
            x-coordinate of the rectangle by default

        b: float
            y-coordinate of the rectangle by default

        bl: float
            radius for bottom-left corner

        br: float
            radius for bottom-right corner

        c: float
            width of the rectangle by default

        d: float
            height of the rectangle by default

        r: float
            radii for all four corners

        tl: float
            radius for top-left corner

        tr: float
            radius for top-right corner

        Notes
        -----

        Draws a rectangle to the Py5Graphics drawing surface. A rectangle is a four-
        sided shape with every angle at ninety degrees. By default, the first two
        parameters set the location of the upper-left corner, the third sets the width,
        and the fourth sets the height. The way these parameters are interpreted,
        however, may be changed with the ``Py5Graphics.rect_mode()`` function.

        To draw a rounded rectangle, add a fifth parameter, which is used as the radius
        value for all four corners.

        To use a different radius value for each corner, include eight parameters. When
        using eight parameters, the latter four set the radius of the arc at each corner
        separately, starting with the top-left corner and moving clockwise around the
        rectangle.

        This method is the same as ``rect()`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``rect()``.
        """
        return self._instance.rect(*args)

    def rect_mode(self, mode: int, /) -> None:
        """Modifies the location from which rectangles are drawn by changing the way in
        which parameters given to ``Py5Graphics.rect()`` are intepreted.

        Underlying Java method: PGraphics.rectMode

        Parameters
        ----------

        mode: int
            either CORNER, CORNERS, CENTER, or RADIUS

        Notes
        -----

        Modifies the location from which rectangles are drawn by changing the way in
        which parameters given to ``Py5Graphics.rect()`` are intepreted.

        The default mode is ``rect_mode(CORNER)``, which interprets the first two
        parameters of ``Py5Graphics.rect()`` as the upper-left corner of the shape,
        while the third and fourth parameters are its width and height.

        ``rect_mode(CORNERS)`` interprets the first two parameters of
        ``Py5Graphics.rect()`` as the location of one corner, and the third and fourth
        parameters as the location of the opposite corner.

        ``rect_mode(CENTER)`` interprets the first two parameters of
        ``Py5Graphics.rect()`` as the shape's center point, while the third and fourth
        parameters are its width and height.

        ``rect_mode(RADIUS)`` also uses the first two parameters of
        ``Py5Graphics.rect()`` as the shape's center point, but uses the third and
        fourth parameters to specify half of the shapes's width and height.

        The parameter must be written in ALL CAPS because Python is a case-sensitive
        language.

        This method is the same as ``rect_mode()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``rect_mode()``.
        """
        return self._instance.rectMode(mode)

    def red(self, rgb: int, /) -> float:
        """Extracts the red value from a color, scaled to match current
        ``Py5Graphics.color_mode()``.

        Underlying Java method: PGraphics.red

        Parameters
        ----------

        rgb: int
            any value of the color datatype

        Notes
        -----

        Extracts the red value from a color, scaled to match current
        ``Py5Graphics.color_mode()``.

        The ``red()`` function is easy to use and understand, but it is slower than a
        technique called bit shifting. When working in ``color_mode(RGB, 255)``, you can
        achieve the same results as ``red()`` but with greater speed by using the right
        shift operator (``>>``) with a bit mask. For example, ``red(c)`` and ``c >> 16 &
        0xFF`` both extract the red value from a color variable ``c`` but the later is
        faster.

        This method is the same as ``red()`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``red()``.
        """
        return self._instance.red(rgb)

    def reset_matrix(self) -> None:
        """Replaces the current matrix with the identity matrix.

        Underlying Java method: PGraphics.resetMatrix

        Notes
        -----

        Replaces the current matrix with the identity matrix. The equivalent function in
        OpenGL is ``gl_load_identity()``.

        This method is the same as ``reset_matrix()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``reset_matrix()``.
        """
        return self._instance.resetMatrix()

    @overload
    def reset_shader(self) -> None:
        """Restores the default shaders.

        Underlying Java method: PGraphics.resetShader

        Methods
        -------

        You can use any of the following signatures:

         * reset_shader() -> None
         * reset_shader(kind: int, /) -> None

        Parameters
        ----------

        kind: int
            type of shader, either POINTS, LINES, or TRIANGLES

        Notes
        -----

        Restores the default shaders. Code that runs after ``reset_shader()`` will not
        be affected by previously defined shaders.

        This method is the same as ``reset_shader()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``reset_shader()``.
        """
        pass

    @overload
    def reset_shader(self, kind: int, /) -> None:
        """Restores the default shaders.

        Underlying Java method: PGraphics.resetShader

        Methods
        -------

        You can use any of the following signatures:

         * reset_shader() -> None
         * reset_shader(kind: int, /) -> None

        Parameters
        ----------

        kind: int
            type of shader, either POINTS, LINES, or TRIANGLES

        Notes
        -----

        Restores the default shaders. Code that runs after ``reset_shader()`` will not
        be affected by previously defined shaders.

        This method is the same as ``reset_shader()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``reset_shader()``.
        """
        pass

    def reset_shader(self, *args):
        """Restores the default shaders.

        Underlying Java method: PGraphics.resetShader

        Methods
        -------

        You can use any of the following signatures:

         * reset_shader() -> None
         * reset_shader(kind: int, /) -> None

        Parameters
        ----------

        kind: int
            type of shader, either POINTS, LINES, or TRIANGLES

        Notes
        -----

        Restores the default shaders. Code that runs after ``reset_shader()`` will not
        be affected by previously defined shaders.

        This method is the same as ``reset_shader()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``reset_shader()``.
        """
        return self._instance.resetShader(*args)

    @overload
    def rotate(self, angle: float, /) -> None:
        """Rotates the amount specified by the ``angle`` parameter.

        Underlying Java method: PGraphics.rotate

        Methods
        -------

        You can use any of the following signatures:

         * rotate(angle: float, /) -> None
         * rotate(angle: float, x: float, y: float, z: float, /) -> None

        Parameters
        ----------

        angle: float
            angle of rotation specified in radians

        x: float
            x-coordinate of vector to rotate around

        y: float
            y-coordinate of vector to rotate around

        z: float
            z-coordinate of vector to rotate around

        Notes
        -----

        Rotates the amount specified by the ``angle`` parameter. Angles must be
        specified in radians (values from ``0`` to ``TWO_PI``), or they can be converted
        from degrees to radians with the ``radians()`` function.

        The coordinates are always rotated around their relative position to the origin.
        Positive numbers rotate objects in a clockwise direction and negative numbers
        rotate in the couterclockwise direction. Transformations apply to everything
        that happens afterward, and subsequent calls to the function compound the
        effect. For example, calling ``rotate(PI/2.0)`` once and then calling
        ``rotate(PI/2.0)`` a second time is the same as a single ``rotate(PI)``. All
        tranformations are reset when ``draw()`` begins again.

        Technically, ``rotate()`` multiplies the current transformation matrix by a
        rotation matrix. This function can be further controlled by
        ``Py5Graphics.push_matrix()`` and ``Py5Graphics.pop_matrix()``.

        This method is the same as ``rotate()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``rotate()``.
        """
        pass

    @overload
    def rotate(self, angle: float, x: float, y: float, z: float, /) -> None:
        """Rotates the amount specified by the ``angle`` parameter.

        Underlying Java method: PGraphics.rotate

        Methods
        -------

        You can use any of the following signatures:

         * rotate(angle: float, /) -> None
         * rotate(angle: float, x: float, y: float, z: float, /) -> None

        Parameters
        ----------

        angle: float
            angle of rotation specified in radians

        x: float
            x-coordinate of vector to rotate around

        y: float
            y-coordinate of vector to rotate around

        z: float
            z-coordinate of vector to rotate around

        Notes
        -----

        Rotates the amount specified by the ``angle`` parameter. Angles must be
        specified in radians (values from ``0`` to ``TWO_PI``), or they can be converted
        from degrees to radians with the ``radians()`` function.

        The coordinates are always rotated around their relative position to the origin.
        Positive numbers rotate objects in a clockwise direction and negative numbers
        rotate in the couterclockwise direction. Transformations apply to everything
        that happens afterward, and subsequent calls to the function compound the
        effect. For example, calling ``rotate(PI/2.0)`` once and then calling
        ``rotate(PI/2.0)`` a second time is the same as a single ``rotate(PI)``. All
        tranformations are reset when ``draw()`` begins again.

        Technically, ``rotate()`` multiplies the current transformation matrix by a
        rotation matrix. This function can be further controlled by
        ``Py5Graphics.push_matrix()`` and ``Py5Graphics.pop_matrix()``.

        This method is the same as ``rotate()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``rotate()``.
        """
        pass

    def rotate(self, *args):
        """Rotates the amount specified by the ``angle`` parameter.

        Underlying Java method: PGraphics.rotate

        Methods
        -------

        You can use any of the following signatures:

         * rotate(angle: float, /) -> None
         * rotate(angle: float, x: float, y: float, z: float, /) -> None

        Parameters
        ----------

        angle: float
            angle of rotation specified in radians

        x: float
            x-coordinate of vector to rotate around

        y: float
            y-coordinate of vector to rotate around

        z: float
            z-coordinate of vector to rotate around

        Notes
        -----

        Rotates the amount specified by the ``angle`` parameter. Angles must be
        specified in radians (values from ``0`` to ``TWO_PI``), or they can be converted
        from degrees to radians with the ``radians()`` function.

        The coordinates are always rotated around their relative position to the origin.
        Positive numbers rotate objects in a clockwise direction and negative numbers
        rotate in the couterclockwise direction. Transformations apply to everything
        that happens afterward, and subsequent calls to the function compound the
        effect. For example, calling ``rotate(PI/2.0)`` once and then calling
        ``rotate(PI/2.0)`` a second time is the same as a single ``rotate(PI)``. All
        tranformations are reset when ``draw()`` begins again.

        Technically, ``rotate()`` multiplies the current transformation matrix by a
        rotation matrix. This function can be further controlled by
        ``Py5Graphics.push_matrix()`` and ``Py5Graphics.pop_matrix()``.

        This method is the same as ``rotate()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``rotate()``.
        """
        return self._instance.rotate(*args)

    def rotate_x(self, angle: float, /) -> None:
        """Rotates around the x-axis the amount specified by the ``angle`` parameter.

        Underlying Java method: PGraphics.rotateX

        Parameters
        ----------

        angle: float
            angle of rotation specified in radians

        Notes
        -----

        Rotates around the x-axis the amount specified by the ``angle`` parameter.
        Angles should be specified in radians (values from ``0`` to ``TWO_PI``) or
        converted from degrees to radians with the ``radians()`` function. Coordinates
        are always rotated around their relative position to the origin. Positive
        numbers rotate in a clockwise direction and negative numbers rotate in a
        counterclockwise direction. Transformations apply to everything that happens
        after and subsequent calls to the function accumulates the effect. For example,
        calling ``rotate_x(PI/2)`` and then ``rotate_x(PI/2)`` is the same as
        ``rotate_x(PI)``. If ``rotate_x()`` is run within the ``draw()``, the
        transformation is reset when the loop begins again. This function requires using
        ``P3D`` as a third parameter to ``size()`` as shown in the example.

        This method is the same as ``rotate_x()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``rotate_x()``.
        """
        return self._instance.rotateX(angle)

    def rotate_y(self, angle: float, /) -> None:
        """Rotates around the y-axis the amount specified by the ``angle`` parameter.

        Underlying Java method: PGraphics.rotateY

        Parameters
        ----------

        angle: float
            angle of rotation specified in radians

        Notes
        -----

        Rotates around the y-axis the amount specified by the ``angle`` parameter.
        Angles should be specified in radians (values from ``0`` to ``TWO_PI``) or
        converted from degrees to radians with the ``radians()`` function. Coordinates
        are always rotated around their relative position to the origin. Positive
        numbers rotate in a clockwise direction and negative numbers rotate in a
        counterclockwise direction. Transformations apply to everything that happens
        after and subsequent calls to the function accumulates the effect. For example,
        calling ``rotate_y(PI/2)`` and then ``rotate_y(PI/2)`` is the same as
        ``rotate_y(PI)``. If ``rotate_y()`` is run within the ``draw()``, the
        transformation is reset when the loop begins again. This function requires using
        ``P3D`` as a third parameter to ``size()`` as shown in the example.

        This method is the same as ``rotate_y()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``rotate_y()``.
        """
        return self._instance.rotateY(angle)

    def rotate_z(self, angle: float, /) -> None:
        """Rotates around the z-axis the amount specified by the ``angle`` parameter.

        Underlying Java method: PGraphics.rotateZ

        Parameters
        ----------

        angle: float
            angle of rotation specified in radians

        Notes
        -----

        Rotates around the z-axis the amount specified by the ``angle`` parameter.
        Angles should be specified in radians (values from ``0`` to ``TWO_PI``) or
        converted from degrees to radians with the ``radians()`` function. Coordinates
        are always rotated around their relative position to the origin. Positive
        numbers rotate in a clockwise direction and negative numbers rotate in a
        counterclockwise direction. Transformations apply to everything that happens
        after and subsequent calls to the function accumulates the effect. For example,
        calling ``rotate_z(PI/2)`` and then ``rotate_z(PI/2)`` is the same as
        ``rotate_z(PI)``. If ``rotate_z()`` is run within the ``draw()``, the
        transformation is reset when the loop begins again. This function requires using
        ``P3D`` as a third parameter to ``size()`` as shown in the example.

        This method is the same as ``rotate_z()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``rotate_z()``.
        """
        return self._instance.rotateZ(angle)

    def saturation(self, rgb: int, /) -> float:
        """Extracts the saturation value from a color.

        Underlying Java method: PGraphics.saturation

        Parameters
        ----------

        rgb: int
            any value of the color datatype

        Notes
        -----

        Extracts the saturation value from a color.

        This method is the same as ``saturation()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``saturation()``.
        """
        return self._instance.saturation(rgb)

    @overload
    def scale(self, s: float, /) -> None:
        """Increases or decreases the size of a shape by expanding and contracting
        vertices.

        Underlying Java method: PGraphics.scale

        Methods
        -------

        You can use any of the following signatures:

         * scale(s: float, /) -> None
         * scale(x: float, y: float, /) -> None
         * scale(x: float, y: float, z: float, /) -> None

        Parameters
        ----------

        s: float
            percentage to scale the object

        x: float
            percentage to scale the object in the x-axis

        y: float
            percentage to scale the object in the y-axis

        z: float
            percentage to scale the object in the z-axis

        Notes
        -----

        Increases or decreases the size of a shape by expanding and contracting
        vertices. Objects always scale from their relative origin to the coordinate
        system. Scale values are specified as decimal percentages. For example, the
        function call ``scale(2.0)`` increases the dimension of a shape by 200%.

        Transformations apply to everything that happens after and subsequent calls to
        the function multiply the effect. For example, calling ``scale(2.0)`` and then
        ``scale(1.5)`` is the same as ``scale(3.0)``. Using this function with the ``z``
        parameter requires using ``P3D`` as the renderer. This function can be further
        controlled with ``Py5Graphics.push_matrix()`` and ``Py5Graphics.pop_matrix()``.

        This method is the same as ``scale()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``scale()``.
        """
        pass

    @overload
    def scale(self, x: float, y: float, /) -> None:
        """Increases or decreases the size of a shape by expanding and contracting
        vertices.

        Underlying Java method: PGraphics.scale

        Methods
        -------

        You can use any of the following signatures:

         * scale(s: float, /) -> None
         * scale(x: float, y: float, /) -> None
         * scale(x: float, y: float, z: float, /) -> None

        Parameters
        ----------

        s: float
            percentage to scale the object

        x: float
            percentage to scale the object in the x-axis

        y: float
            percentage to scale the object in the y-axis

        z: float
            percentage to scale the object in the z-axis

        Notes
        -----

        Increases or decreases the size of a shape by expanding and contracting
        vertices. Objects always scale from their relative origin to the coordinate
        system. Scale values are specified as decimal percentages. For example, the
        function call ``scale(2.0)`` increases the dimension of a shape by 200%.

        Transformations apply to everything that happens after and subsequent calls to
        the function multiply the effect. For example, calling ``scale(2.0)`` and then
        ``scale(1.5)`` is the same as ``scale(3.0)``. Using this function with the ``z``
        parameter requires using ``P3D`` as the renderer. This function can be further
        controlled with ``Py5Graphics.push_matrix()`` and ``Py5Graphics.pop_matrix()``.

        This method is the same as ``scale()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``scale()``.
        """
        pass

    @overload
    def scale(self, x: float, y: float, z: float, /) -> None:
        """Increases or decreases the size of a shape by expanding and contracting
        vertices.

        Underlying Java method: PGraphics.scale

        Methods
        -------

        You can use any of the following signatures:

         * scale(s: float, /) -> None
         * scale(x: float, y: float, /) -> None
         * scale(x: float, y: float, z: float, /) -> None

        Parameters
        ----------

        s: float
            percentage to scale the object

        x: float
            percentage to scale the object in the x-axis

        y: float
            percentage to scale the object in the y-axis

        z: float
            percentage to scale the object in the z-axis

        Notes
        -----

        Increases or decreases the size of a shape by expanding and contracting
        vertices. Objects always scale from their relative origin to the coordinate
        system. Scale values are specified as decimal percentages. For example, the
        function call ``scale(2.0)`` increases the dimension of a shape by 200%.

        Transformations apply to everything that happens after and subsequent calls to
        the function multiply the effect. For example, calling ``scale(2.0)`` and then
        ``scale(1.5)`` is the same as ``scale(3.0)``. Using this function with the ``z``
        parameter requires using ``P3D`` as the renderer. This function can be further
        controlled with ``Py5Graphics.push_matrix()`` and ``Py5Graphics.pop_matrix()``.

        This method is the same as ``scale()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``scale()``.
        """
        pass

    def scale(self, *args):
        """Increases or decreases the size of a shape by expanding and contracting
        vertices.

        Underlying Java method: PGraphics.scale

        Methods
        -------

        You can use any of the following signatures:

         * scale(s: float, /) -> None
         * scale(x: float, y: float, /) -> None
         * scale(x: float, y: float, z: float, /) -> None

        Parameters
        ----------

        s: float
            percentage to scale the object

        x: float
            percentage to scale the object in the x-axis

        y: float
            percentage to scale the object in the y-axis

        z: float
            percentage to scale the object in the z-axis

        Notes
        -----

        Increases or decreases the size of a shape by expanding and contracting
        vertices. Objects always scale from their relative origin to the coordinate
        system. Scale values are specified as decimal percentages. For example, the
        function call ``scale(2.0)`` increases the dimension of a shape by 200%.

        Transformations apply to everything that happens after and subsequent calls to
        the function multiply the effect. For example, calling ``scale(2.0)`` and then
        ``scale(1.5)`` is the same as ``scale(3.0)``. Using this function with the ``z``
        parameter requires using ``P3D`` as the renderer. This function can be further
        controlled with ``Py5Graphics.push_matrix()`` and ``Py5Graphics.pop_matrix()``.

        This method is the same as ``scale()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``scale()``.
        """
        return self._instance.scale(*args)

    @overload
    def screen_x(self, x: float, y: float, /) -> float:
        """Takes a three-dimensional X, Y, Z position and returns the X value for where it
        will appear on a (two-dimensional) screen.

        Underlying Java method: PGraphics.screenX

        Methods
        -------

        You can use any of the following signatures:

         * screen_x(x: float, y: float, /) -> float
         * screen_x(x: float, y: float, z: float, /) -> float

        Parameters
        ----------

        x: float
            3D x-coordinate to be mapped

        y: float
            3D y-coordinate to be mapped

        z: float
            3D z-coordinate to be mapped

        Notes
        -----

        Takes a three-dimensional X, Y, Z position and returns the X value for where it
        will appear on a (two-dimensional) screen.

        This method is the same as ``screen_x()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``screen_x()``.
        """
        pass

    @overload
    def screen_x(self, x: float, y: float, z: float, /) -> float:
        """Takes a three-dimensional X, Y, Z position and returns the X value for where it
        will appear on a (two-dimensional) screen.

        Underlying Java method: PGraphics.screenX

        Methods
        -------

        You can use any of the following signatures:

         * screen_x(x: float, y: float, /) -> float
         * screen_x(x: float, y: float, z: float, /) -> float

        Parameters
        ----------

        x: float
            3D x-coordinate to be mapped

        y: float
            3D y-coordinate to be mapped

        z: float
            3D z-coordinate to be mapped

        Notes
        -----

        Takes a three-dimensional X, Y, Z position and returns the X value for where it
        will appear on a (two-dimensional) screen.

        This method is the same as ``screen_x()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``screen_x()``.
        """
        pass

    def screen_x(self, *args):
        """Takes a three-dimensional X, Y, Z position and returns the X value for where it
        will appear on a (two-dimensional) screen.

        Underlying Java method: PGraphics.screenX

        Methods
        -------

        You can use any of the following signatures:

         * screen_x(x: float, y: float, /) -> float
         * screen_x(x: float, y: float, z: float, /) -> float

        Parameters
        ----------

        x: float
            3D x-coordinate to be mapped

        y: float
            3D y-coordinate to be mapped

        z: float
            3D z-coordinate to be mapped

        Notes
        -----

        Takes a three-dimensional X, Y, Z position and returns the X value for where it
        will appear on a (two-dimensional) screen.

        This method is the same as ``screen_x()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``screen_x()``.
        """
        return self._instance.screenX(*args)

    @overload
    def screen_y(self, x: float, y: float, /) -> float:
        """Takes a three-dimensional X, Y, Z position and returns the Y value for where it
        will appear on a (two-dimensional) screen.

        Underlying Java method: PGraphics.screenY

        Methods
        -------

        You can use any of the following signatures:

         * screen_y(x: float, y: float, /) -> float
         * screen_y(x: float, y: float, z: float, /) -> float

        Parameters
        ----------

        x: float
            3D x-coordinate to be mapped

        y: float
            3D y-coordinate to be mapped

        z: float
            3D z-coordinate to be mapped

        Notes
        -----

        Takes a three-dimensional X, Y, Z position and returns the Y value for where it
        will appear on a (two-dimensional) screen.

        This method is the same as ``screen_y()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``screen_y()``.
        """
        pass

    @overload
    def screen_y(self, x: float, y: float, z: float, /) -> float:
        """Takes a three-dimensional X, Y, Z position and returns the Y value for where it
        will appear on a (two-dimensional) screen.

        Underlying Java method: PGraphics.screenY

        Methods
        -------

        You can use any of the following signatures:

         * screen_y(x: float, y: float, /) -> float
         * screen_y(x: float, y: float, z: float, /) -> float

        Parameters
        ----------

        x: float
            3D x-coordinate to be mapped

        y: float
            3D y-coordinate to be mapped

        z: float
            3D z-coordinate to be mapped

        Notes
        -----

        Takes a three-dimensional X, Y, Z position and returns the Y value for where it
        will appear on a (two-dimensional) screen.

        This method is the same as ``screen_y()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``screen_y()``.
        """
        pass

    def screen_y(self, *args):
        """Takes a three-dimensional X, Y, Z position and returns the Y value for where it
        will appear on a (two-dimensional) screen.

        Underlying Java method: PGraphics.screenY

        Methods
        -------

        You can use any of the following signatures:

         * screen_y(x: float, y: float, /) -> float
         * screen_y(x: float, y: float, z: float, /) -> float

        Parameters
        ----------

        x: float
            3D x-coordinate to be mapped

        y: float
            3D y-coordinate to be mapped

        z: float
            3D z-coordinate to be mapped

        Notes
        -----

        Takes a three-dimensional X, Y, Z position and returns the Y value for where it
        will appear on a (two-dimensional) screen.

        This method is the same as ``screen_y()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``screen_y()``.
        """
        return self._instance.screenY(*args)

    def screen_z(self, x: float, y: float, z: float, /) -> float:
        """Takes a three-dimensional X, Y, Z position and returns the Z value for where it
        will appear on a (two-dimensional) screen.

        Underlying Java method: PGraphics.screenZ

        Parameters
        ----------

        x: float
            3D x-coordinate to be mapped

        y: float
            3D y-coordinate to be mapped

        z: float
            3D z-coordinate to be mapped

        Notes
        -----

        Takes a three-dimensional X, Y, Z position and returns the Z value for where it
        will appear on a (two-dimensional) screen.

        This method is the same as ``screen_z()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``screen_z()``.
        """
        return self._instance.screenZ(x, y, z)

    @overload
    def set_matrix(self, source: NDArray[(2, 3), Float], /) -> None:
        """Set the current matrix to the one specified through the parameter ``source``.

        Underlying Java method: PGraphics.setMatrix

        Methods
        -------

        You can use any of the following signatures:

         * set_matrix(source: NDArray[(2, 3), Float], /) -> None
         * set_matrix(source: NDArray[(4, 4), Float], /) -> None

        Parameters
        ----------

        source: NDArray[(2, 3), Float]
            transformation matrix data

        source: NDArray[(4, 4), Float]
            transformation matrix data

        Notes
        -----

        Set the current matrix to the one specified through the parameter ``source``.
        Inside the Processing code it will call ``Py5Graphics.reset_matrix()`` followed
        by ``Py5Graphics.apply_matrix()``. This will be very slow because
        ``Py5Graphics.apply_matrix()`` will try to calculate the inverse of the
        transform, so avoid it whenever possible.

        This method is the same as ``set_matrix()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``set_matrix()``.
        """
        pass

    @overload
    def set_matrix(self, source: NDArray[(4, 4), Float], /) -> None:
        """Set the current matrix to the one specified through the parameter ``source``.

        Underlying Java method: PGraphics.setMatrix

        Methods
        -------

        You can use any of the following signatures:

         * set_matrix(source: NDArray[(2, 3), Float], /) -> None
         * set_matrix(source: NDArray[(4, 4), Float], /) -> None

        Parameters
        ----------

        source: NDArray[(2, 3), Float]
            transformation matrix data

        source: NDArray[(4, 4), Float]
            transformation matrix data

        Notes
        -----

        Set the current matrix to the one specified through the parameter ``source``.
        Inside the Processing code it will call ``Py5Graphics.reset_matrix()`` followed
        by ``Py5Graphics.apply_matrix()``. This will be very slow because
        ``Py5Graphics.apply_matrix()`` will try to calculate the inverse of the
        transform, so avoid it whenever possible.

        This method is the same as ``set_matrix()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``set_matrix()``.
        """
        pass

    def set_matrix(self, *args):
        """Set the current matrix to the one specified through the parameter ``source``.

        Underlying Java method: PGraphics.setMatrix

        Methods
        -------

        You can use any of the following signatures:

         * set_matrix(source: NDArray[(2, 3), Float], /) -> None
         * set_matrix(source: NDArray[(4, 4), Float], /) -> None

        Parameters
        ----------

        source: NDArray[(2, 3), Float]
            transformation matrix data

        source: NDArray[(4, 4), Float]
            transformation matrix data

        Notes
        -----

        Set the current matrix to the one specified through the parameter ``source``.
        Inside the Processing code it will call ``Py5Graphics.reset_matrix()`` followed
        by ``Py5Graphics.apply_matrix()``. This will be very slow because
        ``Py5Graphics.apply_matrix()`` will try to calculate the inverse of the
        transform, so avoid it whenever possible.

        This method is the same as ``set_matrix()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``set_matrix()``.
        """
        return self._instance.setMatrix(*args)

    @overload
    def shader(self, shader: Py5Shader, /) -> None:
        """Applies the shader specified by the parameters.

        Underlying Java method: PGraphics.shader

        Methods
        -------

        You can use any of the following signatures:

         * shader(shader: Py5Shader, /) -> None
         * shader(shader: Py5Shader, kind: int, /) -> None

        Parameters
        ----------

        kind: int
            type of shader, either POINTS, LINES, or TRIANGLES

        shader: Py5Shader
            name of shader file

        Notes
        -----

        Applies the shader specified by the parameters. It's compatible with the ``P2D``
        and ``P3D`` renderers, but not with the default renderer.

        This method is the same as ``shader()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``shader()``.
        """
        pass

    @overload
    def shader(self, shader: Py5Shader, kind: int, /) -> None:
        """Applies the shader specified by the parameters.

        Underlying Java method: PGraphics.shader

        Methods
        -------

        You can use any of the following signatures:

         * shader(shader: Py5Shader, /) -> None
         * shader(shader: Py5Shader, kind: int, /) -> None

        Parameters
        ----------

        kind: int
            type of shader, either POINTS, LINES, or TRIANGLES

        shader: Py5Shader
            name of shader file

        Notes
        -----

        Applies the shader specified by the parameters. It's compatible with the ``P2D``
        and ``P3D`` renderers, but not with the default renderer.

        This method is the same as ``shader()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``shader()``.
        """
        pass

    def shader(self, *args):
        """Applies the shader specified by the parameters.

        Underlying Java method: PGraphics.shader

        Methods
        -------

        You can use any of the following signatures:

         * shader(shader: Py5Shader, /) -> None
         * shader(shader: Py5Shader, kind: int, /) -> None

        Parameters
        ----------

        kind: int
            type of shader, either POINTS, LINES, or TRIANGLES

        shader: Py5Shader
            name of shader file

        Notes
        -----

        Applies the shader specified by the parameters. It's compatible with the ``P2D``
        and ``P3D`` renderers, but not with the default renderer.

        This method is the same as ``shader()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``shader()``.
        """
        return self._instance.shader(*args)

    @overload
    def shape(self, shape: Py5Shape, /) -> None:
        """Draws shapes to the Py5Graphics drawing surface.

        Underlying Java method: PGraphics.shape

        Methods
        -------

        You can use any of the following signatures:

         * shape(shape: Py5Shape, /) -> None
         * shape(shape: Py5Shape, a: float, b: float, c: float, d: float, /) -> None
         * shape(shape: Py5Shape, x: float, y: float, /) -> None

        Parameters
        ----------

        a: float
            x-coordinate of the shape

        b: float
            y-coordinate of the shape

        c: float
            width to display the shape

        d: float
            height to display the shape

        shape: Py5Shape
            the shape to display

        x: float
            x-coordinate of the shape

        y: float
            y-coordinate of the shape

        Notes
        -----

        Draws shapes to the Py5Graphics drawing surface. Shapes must be in the Sketch's
        "data" directory to load correctly. Py5 currently works with SVG, OBJ, and
        custom-created shapes. The ``shape`` parameter specifies the shape to display
        and the coordinate parameters define the location of the shape from its upper-
        left corner. The shape is displayed at its original size unless the ``c`` and
        ``d`` parameters specify a different size. The ``Py5Graphics.shape_mode()``
        function can be used to change the way these parameters are interpreted.

        This method is the same as ``shape()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``shape()``.
        """
        pass

    @overload
    def shape(self, shape: Py5Shape, x: float, y: float, /) -> None:
        """Draws shapes to the Py5Graphics drawing surface.

        Underlying Java method: PGraphics.shape

        Methods
        -------

        You can use any of the following signatures:

         * shape(shape: Py5Shape, /) -> None
         * shape(shape: Py5Shape, a: float, b: float, c: float, d: float, /) -> None
         * shape(shape: Py5Shape, x: float, y: float, /) -> None

        Parameters
        ----------

        a: float
            x-coordinate of the shape

        b: float
            y-coordinate of the shape

        c: float
            width to display the shape

        d: float
            height to display the shape

        shape: Py5Shape
            the shape to display

        x: float
            x-coordinate of the shape

        y: float
            y-coordinate of the shape

        Notes
        -----

        Draws shapes to the Py5Graphics drawing surface. Shapes must be in the Sketch's
        "data" directory to load correctly. Py5 currently works with SVG, OBJ, and
        custom-created shapes. The ``shape`` parameter specifies the shape to display
        and the coordinate parameters define the location of the shape from its upper-
        left corner. The shape is displayed at its original size unless the ``c`` and
        ``d`` parameters specify a different size. The ``Py5Graphics.shape_mode()``
        function can be used to change the way these parameters are interpreted.

        This method is the same as ``shape()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``shape()``.
        """
        pass

    @overload
    def shape(self, shape: Py5Shape, a: float,
              b: float, c: float, d: float, /) -> None:
        """Draws shapes to the Py5Graphics drawing surface.

        Underlying Java method: PGraphics.shape

        Methods
        -------

        You can use any of the following signatures:

         * shape(shape: Py5Shape, /) -> None
         * shape(shape: Py5Shape, a: float, b: float, c: float, d: float, /) -> None
         * shape(shape: Py5Shape, x: float, y: float, /) -> None

        Parameters
        ----------

        a: float
            x-coordinate of the shape

        b: float
            y-coordinate of the shape

        c: float
            width to display the shape

        d: float
            height to display the shape

        shape: Py5Shape
            the shape to display

        x: float
            x-coordinate of the shape

        y: float
            y-coordinate of the shape

        Notes
        -----

        Draws shapes to the Py5Graphics drawing surface. Shapes must be in the Sketch's
        "data" directory to load correctly. Py5 currently works with SVG, OBJ, and
        custom-created shapes. The ``shape`` parameter specifies the shape to display
        and the coordinate parameters define the location of the shape from its upper-
        left corner. The shape is displayed at its original size unless the ``c`` and
        ``d`` parameters specify a different size. The ``Py5Graphics.shape_mode()``
        function can be used to change the way these parameters are interpreted.

        This method is the same as ``shape()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``shape()``.
        """
        pass

    def shape(self, *args):
        """Draws shapes to the Py5Graphics drawing surface.

        Underlying Java method: PGraphics.shape

        Methods
        -------

        You can use any of the following signatures:

         * shape(shape: Py5Shape, /) -> None
         * shape(shape: Py5Shape, a: float, b: float, c: float, d: float, /) -> None
         * shape(shape: Py5Shape, x: float, y: float, /) -> None

        Parameters
        ----------

        a: float
            x-coordinate of the shape

        b: float
            y-coordinate of the shape

        c: float
            width to display the shape

        d: float
            height to display the shape

        shape: Py5Shape
            the shape to display

        x: float
            x-coordinate of the shape

        y: float
            y-coordinate of the shape

        Notes
        -----

        Draws shapes to the Py5Graphics drawing surface. Shapes must be in the Sketch's
        "data" directory to load correctly. Py5 currently works with SVG, OBJ, and
        custom-created shapes. The ``shape`` parameter specifies the shape to display
        and the coordinate parameters define the location of the shape from its upper-
        left corner. The shape is displayed at its original size unless the ``c`` and
        ``d`` parameters specify a different size. The ``Py5Graphics.shape_mode()``
        function can be used to change the way these parameters are interpreted.

        This method is the same as ``shape()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``shape()``.
        """
        return self._instance.shape(*args)

    def shape_mode(self, mode: int, /) -> None:
        """Modifies the location from which shapes draw.

        Underlying Java method: PGraphics.shapeMode

        Parameters
        ----------

        mode: int
            either CORNER, CORNERS, CENTER

        Notes
        -----

        Modifies the location from which shapes draw. The default mode is
        ``shape_mode(CORNER)``, which specifies the location to be the upper left corner
        of the shape and uses the third and fourth parameters of ``Py5Graphics.shape()``
        to specify the width and height. The syntax ``shape_mode(CORNERS)`` uses the
        first and second parameters of ``Py5Graphics.shape()`` to set the location of
        one corner and uses the third and fourth parameters to set the opposite corner.
        The syntax ``shape_mode(CENTER)`` draws the shape from its center point and uses
        the third and forth parameters of ``Py5Graphics.shape()`` to specify the width
        and height. The parameter must be written in ALL CAPS because Python is a case
        sensitive language.

        This method is the same as ``shape_mode()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``shape_mode()``.
        """
        return self._instance.shapeMode(mode)

    def shear_x(self, angle: float, /) -> None:
        """Shears a shape around the x-axis the amount specified by the ``angle``
        parameter.

        Underlying Java method: PGraphics.shearX

        Parameters
        ----------

        angle: float
            angle of shear specified in radians

        Notes
        -----

        Shears a shape around the x-axis the amount specified by the ``angle``
        parameter. Angles should be specified in radians (values from ``0`` to
        ``TWO_PI``) or converted to radians with the ``radians()`` function. Objects are
        always sheared around their relative position to the origin and positive numbers
        shear objects in a clockwise direction. Transformations apply to everything that
        happens after and subsequent calls to the function accumulates the effect. For
        example, calling ``shear_x(PI/2)`` and then ``shear_x(PI/2)`` is the same as
        ``shear_x(PI)``.

        Technically, ``shear_x()`` multiplies the current transformation matrix by a
        rotation matrix. This function can be further controlled by the
        ``Py5Graphics.push_matrix()`` and ``Py5Graphics.pop_matrix()`` functions.

        This method is the same as ``shear_x()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``shear_x()``.
        """
        return self._instance.shearX(angle)

    def shear_y(self, angle: float, /) -> None:
        """Shears a shape around the y-axis the amount specified by the ``angle``
        parameter.

        Underlying Java method: PGraphics.shearY

        Parameters
        ----------

        angle: float
            angle of shear specified in radians

        Notes
        -----

        Shears a shape around the y-axis the amount specified by the ``angle``
        parameter. Angles should be specified in radians (values from ``0`` to
        ``TWO_PI``) or converted to radians with the ``radians()`` function. Objects are
        always sheared around their relative position to the origin and positive numbers
        shear objects in a clockwise direction. Transformations apply to everything that
        happens after and subsequent calls to the function accumulates the effect. For
        example, calling ``shear_y(PI/2)`` and then ``shear_y(PI/2)`` is the same as
        ``shear_y(PI)``.

        Technically, ``shear_y()`` multiplies the current transformation matrix by a
        rotation matrix. This function can be further controlled by the
        ``Py5Graphics.push_matrix()`` and ``Py5Graphics.pop_matrix()`` functions.

        This method is the same as ``shear_y()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``shear_y()``.
        """
        return self._instance.shearY(angle)

    def shininess(self, shine: float, /) -> None:
        """Sets the amount of gloss in the surface of shapes.

        Underlying Java method: PGraphics.shininess

        Parameters
        ----------

        shine: float
            degree of shininess

        Notes
        -----

        Sets the amount of gloss in the surface of shapes. Use in combination with
        ``Py5Graphics.ambient()``, ``Py5Graphics.specular()``, and
        ``Py5Graphics.emissive()`` to set the material properties of shapes.

        This method is the same as ``shininess()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``shininess()``.
        """
        return self._instance.shininess(shine)

    @overload
    def smooth(self) -> None:
        """Draws all geometry with smooth (anti-aliased) edges.

        Underlying Java method: PGraphics.smooth

        Methods
        -------

        You can use any of the following signatures:

         * smooth() -> None
         * smooth(quality: int, /) -> None

        Parameters
        ----------

        quality: int
            either 2, 3, 4, or 8 depending on the renderer

        Notes
        -----

        Draws all geometry with smooth (anti-aliased) edges. This behavior is the
        default, so ``smooth()`` only needs to be used when a program needs to set the
        smoothing in a different way. The ``level`` parameter increases the amount of
        smoothness. This is the level of over sampling applied to the graphics buffer.

        With the ``P2D`` and ``P3D`` renderers, ``smooth(2)`` is the default, this is
        called "2x anti-aliasing." The code ``smooth(4)`` is used for 4x anti-aliasing
        and ``smooth(8)`` is specified for "8x anti-aliasing." The maximum anti-aliasing
        level is determined by the hardware of the machine that is running the software,
        so ``smooth(4)`` and ``smooth(8)`` will not work with every computer.

        The default renderer uses ``smooth(3)`` by default. This is bicubic smoothing.
        The other option for the default renderer is ``smooth(2)``, which is bilinear
        smoothing.

        The ``smooth()`` method can only be run once for a ``Py5Graphics`` object and it
        must be called right after the object is created with ``create_graphics()`` and
        before ``Py5Graphics.begin_draw()``.

        This method is the same as ``smooth()`` but linked to a ``Py5Graphics`` object.
        """
        pass

    @overload
    def smooth(self, quality: int, /) -> None:
        """Draws all geometry with smooth (anti-aliased) edges.

        Underlying Java method: PGraphics.smooth

        Methods
        -------

        You can use any of the following signatures:

         * smooth() -> None
         * smooth(quality: int, /) -> None

        Parameters
        ----------

        quality: int
            either 2, 3, 4, or 8 depending on the renderer

        Notes
        -----

        Draws all geometry with smooth (anti-aliased) edges. This behavior is the
        default, so ``smooth()`` only needs to be used when a program needs to set the
        smoothing in a different way. The ``level`` parameter increases the amount of
        smoothness. This is the level of over sampling applied to the graphics buffer.

        With the ``P2D`` and ``P3D`` renderers, ``smooth(2)`` is the default, this is
        called "2x anti-aliasing." The code ``smooth(4)`` is used for 4x anti-aliasing
        and ``smooth(8)`` is specified for "8x anti-aliasing." The maximum anti-aliasing
        level is determined by the hardware of the machine that is running the software,
        so ``smooth(4)`` and ``smooth(8)`` will not work with every computer.

        The default renderer uses ``smooth(3)`` by default. This is bicubic smoothing.
        The other option for the default renderer is ``smooth(2)``, which is bilinear
        smoothing.

        The ``smooth()`` method can only be run once for a ``Py5Graphics`` object and it
        must be called right after the object is created with ``create_graphics()`` and
        before ``Py5Graphics.begin_draw()``.

        This method is the same as ``smooth()`` but linked to a ``Py5Graphics`` object.
        """
        pass

    def smooth(self, *args):
        """Draws all geometry with smooth (anti-aliased) edges.

        Underlying Java method: PGraphics.smooth

        Methods
        -------

        You can use any of the following signatures:

         * smooth() -> None
         * smooth(quality: int, /) -> None

        Parameters
        ----------

        quality: int
            either 2, 3, 4, or 8 depending on the renderer

        Notes
        -----

        Draws all geometry with smooth (anti-aliased) edges. This behavior is the
        default, so ``smooth()`` only needs to be used when a program needs to set the
        smoothing in a different way. The ``level`` parameter increases the amount of
        smoothness. This is the level of over sampling applied to the graphics buffer.

        With the ``P2D`` and ``P3D`` renderers, ``smooth(2)`` is the default, this is
        called "2x anti-aliasing." The code ``smooth(4)`` is used for 4x anti-aliasing
        and ``smooth(8)`` is specified for "8x anti-aliasing." The maximum anti-aliasing
        level is determined by the hardware of the machine that is running the software,
        so ``smooth(4)`` and ``smooth(8)`` will not work with every computer.

        The default renderer uses ``smooth(3)`` by default. This is bicubic smoothing.
        The other option for the default renderer is ``smooth(2)``, which is bilinear
        smoothing.

        The ``smooth()`` method can only be run once for a ``Py5Graphics`` object and it
        must be called right after the object is created with ``create_graphics()`` and
        before ``Py5Graphics.begin_draw()``.

        This method is the same as ``smooth()`` but linked to a ``Py5Graphics`` object.
        """
        return self._instance.smooth(*args)

    @overload
    def specular(self, gray: float, /) -> None:
        """Sets the specular color of the materials used for shapes drawn to the
        Py5Graphics drawing surface, which sets the color of highlights.

        Underlying Java method: PGraphics.specular

        Methods
        -------

        You can use any of the following signatures:

         * specular(gray: float, /) -> None
         * specular(rgb: int, /) -> None
         * specular(v1: float, v2: float, v3: float, /) -> None

        Parameters
        ----------

        gray: float
            value between black and white, by default 0 to 255

        rgb: int
            color to set

        v1: float
            red or hue value (depending on current color mode)

        v2: float
            green or saturation value (depending on current color mode)

        v3: float
            blue or brightness value (depending on current color mode)

        Notes
        -----

        Sets the specular color of the materials used for shapes drawn to the
        Py5Graphics drawing surface, which sets the color of highlights. Specular refers
        to light which bounces off a surface in a preferred direction (rather than
        bouncing in all directions like a diffuse light). Use in combination with
        ``Py5Graphics.emissive()``, ``Py5Graphics.ambient()``, and
        ``Py5Graphics.shininess()`` to set the material properties of shapes.

        This method is the same as ``specular()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``specular()``.
        """
        pass

    @overload
    def specular(self, v1: float, v2: float, v3: float, /) -> None:
        """Sets the specular color of the materials used for shapes drawn to the
        Py5Graphics drawing surface, which sets the color of highlights.

        Underlying Java method: PGraphics.specular

        Methods
        -------

        You can use any of the following signatures:

         * specular(gray: float, /) -> None
         * specular(rgb: int, /) -> None
         * specular(v1: float, v2: float, v3: float, /) -> None

        Parameters
        ----------

        gray: float
            value between black and white, by default 0 to 255

        rgb: int
            color to set

        v1: float
            red or hue value (depending on current color mode)

        v2: float
            green or saturation value (depending on current color mode)

        v3: float
            blue or brightness value (depending on current color mode)

        Notes
        -----

        Sets the specular color of the materials used for shapes drawn to the
        Py5Graphics drawing surface, which sets the color of highlights. Specular refers
        to light which bounces off a surface in a preferred direction (rather than
        bouncing in all directions like a diffuse light). Use in combination with
        ``Py5Graphics.emissive()``, ``Py5Graphics.ambient()``, and
        ``Py5Graphics.shininess()`` to set the material properties of shapes.

        This method is the same as ``specular()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``specular()``.
        """
        pass

    @overload
    def specular(self, rgb: int, /) -> None:
        """Sets the specular color of the materials used for shapes drawn to the
        Py5Graphics drawing surface, which sets the color of highlights.

        Underlying Java method: PGraphics.specular

        Methods
        -------

        You can use any of the following signatures:

         * specular(gray: float, /) -> None
         * specular(rgb: int, /) -> None
         * specular(v1: float, v2: float, v3: float, /) -> None

        Parameters
        ----------

        gray: float
            value between black and white, by default 0 to 255

        rgb: int
            color to set

        v1: float
            red or hue value (depending on current color mode)

        v2: float
            green or saturation value (depending on current color mode)

        v3: float
            blue or brightness value (depending on current color mode)

        Notes
        -----

        Sets the specular color of the materials used for shapes drawn to the
        Py5Graphics drawing surface, which sets the color of highlights. Specular refers
        to light which bounces off a surface in a preferred direction (rather than
        bouncing in all directions like a diffuse light). Use in combination with
        ``Py5Graphics.emissive()``, ``Py5Graphics.ambient()``, and
        ``Py5Graphics.shininess()`` to set the material properties of shapes.

        This method is the same as ``specular()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``specular()``.
        """
        pass

    def specular(self, *args):
        """Sets the specular color of the materials used for shapes drawn to the
        Py5Graphics drawing surface, which sets the color of highlights.

        Underlying Java method: PGraphics.specular

        Methods
        -------

        You can use any of the following signatures:

         * specular(gray: float, /) -> None
         * specular(rgb: int, /) -> None
         * specular(v1: float, v2: float, v3: float, /) -> None

        Parameters
        ----------

        gray: float
            value between black and white, by default 0 to 255

        rgb: int
            color to set

        v1: float
            red or hue value (depending on current color mode)

        v2: float
            green or saturation value (depending on current color mode)

        v3: float
            blue or brightness value (depending on current color mode)

        Notes
        -----

        Sets the specular color of the materials used for shapes drawn to the
        Py5Graphics drawing surface, which sets the color of highlights. Specular refers
        to light which bounces off a surface in a preferred direction (rather than
        bouncing in all directions like a diffuse light). Use in combination with
        ``Py5Graphics.emissive()``, ``Py5Graphics.ambient()``, and
        ``Py5Graphics.shininess()`` to set the material properties of shapes.

        This method is the same as ``specular()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``specular()``.
        """
        return self._instance.specular(*args)

    def sphere(self, r: float, /) -> None:
        """A sphere is a hollow ball made from tessellated triangles.

        Underlying Java method: PGraphics.sphere

        Parameters
        ----------

        r: float
            the radius of the sphere

        Notes
        -----

        A sphere is a hollow ball made from tessellated triangles.

        This method is the same as ``sphere()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``sphere()``.
        """
        return self._instance.sphere(r)

    @overload
    def sphere_detail(self, res: int, /) -> None:
        """Controls the detail used to render a sphere by adjusting the number of vertices
        of the sphere mesh.

        Underlying Java method: PGraphics.sphereDetail

        Methods
        -------

        You can use any of the following signatures:

         * sphere_detail(res: int, /) -> None
         * sphere_detail(ures: int, vres: int, /) -> None

        Parameters
        ----------

        res: int
            number of segments (minimum 3) used per full circle revolution

        ures: int
            number of segments used longitudinally per full circle revolutoin

        vres: int
            number of segments used latitudinally from top to bottom

        Notes
        -----

        Controls the detail used to render a sphere by adjusting the number of vertices
        of the sphere mesh. The default resolution is 30, which creates a fairly
        detailed sphere definition with vertices every ``360/30 = 12`` degrees. If
        you're going to render a great number of spheres per frame, it is advised to
        reduce the level of detail using this function. The setting stays active until
        ``sphere_detail()`` is called again with a new parameter and so should *not* be
        called prior to every ``Py5Graphics.sphere()`` statement, unless you wish to
        render spheres with different settings, e.g. using less detail for smaller
        spheres or ones further away from the camera. To control the detail of the
        horizontal and vertical resolution independently, use the version of the
        functions with two parameters.

        This method is the same as ``sphere_detail()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``sphere_detail()``.
        """
        pass

    @overload
    def sphere_detail(self, ures: int, vres: int, /) -> None:
        """Controls the detail used to render a sphere by adjusting the number of vertices
        of the sphere mesh.

        Underlying Java method: PGraphics.sphereDetail

        Methods
        -------

        You can use any of the following signatures:

         * sphere_detail(res: int, /) -> None
         * sphere_detail(ures: int, vres: int, /) -> None

        Parameters
        ----------

        res: int
            number of segments (minimum 3) used per full circle revolution

        ures: int
            number of segments used longitudinally per full circle revolutoin

        vres: int
            number of segments used latitudinally from top to bottom

        Notes
        -----

        Controls the detail used to render a sphere by adjusting the number of vertices
        of the sphere mesh. The default resolution is 30, which creates a fairly
        detailed sphere definition with vertices every ``360/30 = 12`` degrees. If
        you're going to render a great number of spheres per frame, it is advised to
        reduce the level of detail using this function. The setting stays active until
        ``sphere_detail()`` is called again with a new parameter and so should *not* be
        called prior to every ``Py5Graphics.sphere()`` statement, unless you wish to
        render spheres with different settings, e.g. using less detail for smaller
        spheres or ones further away from the camera. To control the detail of the
        horizontal and vertical resolution independently, use the version of the
        functions with two parameters.

        This method is the same as ``sphere_detail()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``sphere_detail()``.
        """
        pass

    def sphere_detail(self, *args):
        """Controls the detail used to render a sphere by adjusting the number of vertices
        of the sphere mesh.

        Underlying Java method: PGraphics.sphereDetail

        Methods
        -------

        You can use any of the following signatures:

         * sphere_detail(res: int, /) -> None
         * sphere_detail(ures: int, vres: int, /) -> None

        Parameters
        ----------

        res: int
            number of segments (minimum 3) used per full circle revolution

        ures: int
            number of segments used longitudinally per full circle revolutoin

        vres: int
            number of segments used latitudinally from top to bottom

        Notes
        -----

        Controls the detail used to render a sphere by adjusting the number of vertices
        of the sphere mesh. The default resolution is 30, which creates a fairly
        detailed sphere definition with vertices every ``360/30 = 12`` degrees. If
        you're going to render a great number of spheres per frame, it is advised to
        reduce the level of detail using this function. The setting stays active until
        ``sphere_detail()`` is called again with a new parameter and so should *not* be
        called prior to every ``Py5Graphics.sphere()`` statement, unless you wish to
        render spheres with different settings, e.g. using less detail for smaller
        spheres or ones further away from the camera. To control the detail of the
        horizontal and vertical resolution independently, use the version of the
        functions with two parameters.

        This method is the same as ``sphere_detail()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``sphere_detail()``.
        """
        return self._instance.sphereDetail(*args)

    def spot_light(
            self,
            v1: float,
            v2: float,
            v3: float,
            x: float,
            y: float,
            z: float,
            nx: float,
            ny: float,
            nz: float,
            angle: float,
            concentration: float,
            /) -> None:
        """Adds a spot light.

        Underlying Java method: PGraphics.spotLight

        Parameters
        ----------

        angle: float
            angle of the spotlight cone

        concentration: float
            exponent determining the center bias of the cone

        nx: float
            direction along the x axis

        ny: float
            direction along the y axis

        nz: float
            direction along the z axis

        v1: float
            red or hue value (depending on current color mode)

        v2: float
            green or saturation value (depending on current color mode)

        v3: float
            blue or brightness value (depending on current color mode)

        x: float
            x-coordinate of the light

        y: float
            y-coordinate of the light

        z: float
            z-coordinate of the light

        Notes
        -----

        Adds a spot light. The ``v1``, ``v2``, and ``v3`` parameters are interpreted as
        either RGB or HSB values, depending on the current color mode. The ``x``, ``y``,
        and ``z`` parameters specify the position of the light and ``nx``, ``ny``,
        ``nz`` specify the direction of light. The ``angle`` parameter affects angle of
        the spotlight cone, while ``concentration`` sets the bias of light focusing
        toward the center of that cone.

        This method is the same as ``spot_light()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``spot_light()``.
        """
        return self._instance.spotLight(
            v1, v2, v3, x, y, z, nx, ny, nz, angle, concentration)

    def square(self, x: float, y: float, extent: float, /) -> None:
        """Draws a square to the Py5Graphics drawing surface.

        Underlying Java method: PGraphics.square

        Parameters
        ----------

        extent: float
            width and height of the rectangle by default

        x: float
            x-coordinate of the rectangle by default

        y: float
            y-coordinate of the rectangle by default

        Notes
        -----

        Draws a square to the Py5Graphics drawing surface. A square is a four-sided
        shape with every angle at ninety degrees and each side is the same length. By
        default, the first two parameters set the location of the upper-left corner, the
        third sets the width and height. The way these parameters are interpreted,
        however, may be changed with the ``Py5Graphics.rect_mode()`` function.

        This method is the same as ``square()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``square()``.
        """
        return self._instance.square(x, y, extent)

    @overload
    def stroke(self, gray: float, /) -> None:
        """Sets the color used to draw lines and borders around shapes.

        Underlying Java method: PGraphics.stroke

        Methods
        -------

        You can use any of the following signatures:

         * stroke(gray: float, /) -> None
         * stroke(gray: float, alpha: float, /) -> None
         * stroke(rgb: int, /) -> None
         * stroke(rgb: int, alpha: float, /) -> None
         * stroke(v1: float, v2: float, v3: float, /) -> None
         * stroke(v1: float, v2: float, v3: float, alpha: float, /) -> None

        Parameters
        ----------

        alpha: float
            opacity of the stroke

        gray: float
            specifies a value between white and black

        rgb: int
            color value in hexadecimal notation

        v1: float
            red or hue value (depending on current color mode)

        v2: float
            green or saturation value (depending on current color mode)

        v3: float
            blue or brightness value (depending on current color mode)

        Notes
        -----

        Sets the color used to draw lines and borders around shapes. This color is
        either specified in terms of the RGB or HSB color depending on the current
        ``Py5Graphics.color_mode()``. The default color space is RGB, with each value in
        the range from 0 to 255.

        When using hexadecimal notation to specify a color, use "``0x``" before the
        values (e.g., ``0xFFCCFFAA``). The hexadecimal value must be specified with
        eight characters; the first two characters define the alpha component, and the
        remainder define the red, green, and blue components.

        The value for the gray parameter must be less than or equal to the current
        maximum value as specified by ``Py5Graphics.color_mode()``. The default maximum
        value is 255.

        When drawing in 2D with the default renderer, you may need
        ``hint(ENABLE_STROKE_PURE)`` to improve drawing quality (at the expense of
        performance). See the ``Py5Graphics.hint()`` documentation for more details.

        This method is the same as ``stroke()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``stroke()``.
        """
        pass

    @overload
    def stroke(self, gray: float, alpha: float, /) -> None:
        """Sets the color used to draw lines and borders around shapes.

        Underlying Java method: PGraphics.stroke

        Methods
        -------

        You can use any of the following signatures:

         * stroke(gray: float, /) -> None
         * stroke(gray: float, alpha: float, /) -> None
         * stroke(rgb: int, /) -> None
         * stroke(rgb: int, alpha: float, /) -> None
         * stroke(v1: float, v2: float, v3: float, /) -> None
         * stroke(v1: float, v2: float, v3: float, alpha: float, /) -> None

        Parameters
        ----------

        alpha: float
            opacity of the stroke

        gray: float
            specifies a value between white and black

        rgb: int
            color value in hexadecimal notation

        v1: float
            red or hue value (depending on current color mode)

        v2: float
            green or saturation value (depending on current color mode)

        v3: float
            blue or brightness value (depending on current color mode)

        Notes
        -----

        Sets the color used to draw lines and borders around shapes. This color is
        either specified in terms of the RGB or HSB color depending on the current
        ``Py5Graphics.color_mode()``. The default color space is RGB, with each value in
        the range from 0 to 255.

        When using hexadecimal notation to specify a color, use "``0x``" before the
        values (e.g., ``0xFFCCFFAA``). The hexadecimal value must be specified with
        eight characters; the first two characters define the alpha component, and the
        remainder define the red, green, and blue components.

        The value for the gray parameter must be less than or equal to the current
        maximum value as specified by ``Py5Graphics.color_mode()``. The default maximum
        value is 255.

        When drawing in 2D with the default renderer, you may need
        ``hint(ENABLE_STROKE_PURE)`` to improve drawing quality (at the expense of
        performance). See the ``Py5Graphics.hint()`` documentation for more details.

        This method is the same as ``stroke()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``stroke()``.
        """
        pass

    @overload
    def stroke(self, v1: float, v2: float, v3: float, /) -> None:
        """Sets the color used to draw lines and borders around shapes.

        Underlying Java method: PGraphics.stroke

        Methods
        -------

        You can use any of the following signatures:

         * stroke(gray: float, /) -> None
         * stroke(gray: float, alpha: float, /) -> None
         * stroke(rgb: int, /) -> None
         * stroke(rgb: int, alpha: float, /) -> None
         * stroke(v1: float, v2: float, v3: float, /) -> None
         * stroke(v1: float, v2: float, v3: float, alpha: float, /) -> None

        Parameters
        ----------

        alpha: float
            opacity of the stroke

        gray: float
            specifies a value between white and black

        rgb: int
            color value in hexadecimal notation

        v1: float
            red or hue value (depending on current color mode)

        v2: float
            green or saturation value (depending on current color mode)

        v3: float
            blue or brightness value (depending on current color mode)

        Notes
        -----

        Sets the color used to draw lines and borders around shapes. This color is
        either specified in terms of the RGB or HSB color depending on the current
        ``Py5Graphics.color_mode()``. The default color space is RGB, with each value in
        the range from 0 to 255.

        When using hexadecimal notation to specify a color, use "``0x``" before the
        values (e.g., ``0xFFCCFFAA``). The hexadecimal value must be specified with
        eight characters; the first two characters define the alpha component, and the
        remainder define the red, green, and blue components.

        The value for the gray parameter must be less than or equal to the current
        maximum value as specified by ``Py5Graphics.color_mode()``. The default maximum
        value is 255.

        When drawing in 2D with the default renderer, you may need
        ``hint(ENABLE_STROKE_PURE)`` to improve drawing quality (at the expense of
        performance). See the ``Py5Graphics.hint()`` documentation for more details.

        This method is the same as ``stroke()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``stroke()``.
        """
        pass

    @overload
    def stroke(self, v1: float, v2: float, v3: float, alpha: float, /) -> None:
        """Sets the color used to draw lines and borders around shapes.

        Underlying Java method: PGraphics.stroke

        Methods
        -------

        You can use any of the following signatures:

         * stroke(gray: float, /) -> None
         * stroke(gray: float, alpha: float, /) -> None
         * stroke(rgb: int, /) -> None
         * stroke(rgb: int, alpha: float, /) -> None
         * stroke(v1: float, v2: float, v3: float, /) -> None
         * stroke(v1: float, v2: float, v3: float, alpha: float, /) -> None

        Parameters
        ----------

        alpha: float
            opacity of the stroke

        gray: float
            specifies a value between white and black

        rgb: int
            color value in hexadecimal notation

        v1: float
            red or hue value (depending on current color mode)

        v2: float
            green or saturation value (depending on current color mode)

        v3: float
            blue or brightness value (depending on current color mode)

        Notes
        -----

        Sets the color used to draw lines and borders around shapes. This color is
        either specified in terms of the RGB or HSB color depending on the current
        ``Py5Graphics.color_mode()``. The default color space is RGB, with each value in
        the range from 0 to 255.

        When using hexadecimal notation to specify a color, use "``0x``" before the
        values (e.g., ``0xFFCCFFAA``). The hexadecimal value must be specified with
        eight characters; the first two characters define the alpha component, and the
        remainder define the red, green, and blue components.

        The value for the gray parameter must be less than or equal to the current
        maximum value as specified by ``Py5Graphics.color_mode()``. The default maximum
        value is 255.

        When drawing in 2D with the default renderer, you may need
        ``hint(ENABLE_STROKE_PURE)`` to improve drawing quality (at the expense of
        performance). See the ``Py5Graphics.hint()`` documentation for more details.

        This method is the same as ``stroke()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``stroke()``.
        """
        pass

    @overload
    def stroke(self, rgb: int, /) -> None:
        """Sets the color used to draw lines and borders around shapes.

        Underlying Java method: PGraphics.stroke

        Methods
        -------

        You can use any of the following signatures:

         * stroke(gray: float, /) -> None
         * stroke(gray: float, alpha: float, /) -> None
         * stroke(rgb: int, /) -> None
         * stroke(rgb: int, alpha: float, /) -> None
         * stroke(v1: float, v2: float, v3: float, /) -> None
         * stroke(v1: float, v2: float, v3: float, alpha: float, /) -> None

        Parameters
        ----------

        alpha: float
            opacity of the stroke

        gray: float
            specifies a value between white and black

        rgb: int
            color value in hexadecimal notation

        v1: float
            red or hue value (depending on current color mode)

        v2: float
            green or saturation value (depending on current color mode)

        v3: float
            blue or brightness value (depending on current color mode)

        Notes
        -----

        Sets the color used to draw lines and borders around shapes. This color is
        either specified in terms of the RGB or HSB color depending on the current
        ``Py5Graphics.color_mode()``. The default color space is RGB, with each value in
        the range from 0 to 255.

        When using hexadecimal notation to specify a color, use "``0x``" before the
        values (e.g., ``0xFFCCFFAA``). The hexadecimal value must be specified with
        eight characters; the first two characters define the alpha component, and the
        remainder define the red, green, and blue components.

        The value for the gray parameter must be less than or equal to the current
        maximum value as specified by ``Py5Graphics.color_mode()``. The default maximum
        value is 255.

        When drawing in 2D with the default renderer, you may need
        ``hint(ENABLE_STROKE_PURE)`` to improve drawing quality (at the expense of
        performance). See the ``Py5Graphics.hint()`` documentation for more details.

        This method is the same as ``stroke()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``stroke()``.
        """
        pass

    @overload
    def stroke(self, rgb: int, alpha: float, /) -> None:
        """Sets the color used to draw lines and borders around shapes.

        Underlying Java method: PGraphics.stroke

        Methods
        -------

        You can use any of the following signatures:

         * stroke(gray: float, /) -> None
         * stroke(gray: float, alpha: float, /) -> None
         * stroke(rgb: int, /) -> None
         * stroke(rgb: int, alpha: float, /) -> None
         * stroke(v1: float, v2: float, v3: float, /) -> None
         * stroke(v1: float, v2: float, v3: float, alpha: float, /) -> None

        Parameters
        ----------

        alpha: float
            opacity of the stroke

        gray: float
            specifies a value between white and black

        rgb: int
            color value in hexadecimal notation

        v1: float
            red or hue value (depending on current color mode)

        v2: float
            green or saturation value (depending on current color mode)

        v3: float
            blue or brightness value (depending on current color mode)

        Notes
        -----

        Sets the color used to draw lines and borders around shapes. This color is
        either specified in terms of the RGB or HSB color depending on the current
        ``Py5Graphics.color_mode()``. The default color space is RGB, with each value in
        the range from 0 to 255.

        When using hexadecimal notation to specify a color, use "``0x``" before the
        values (e.g., ``0xFFCCFFAA``). The hexadecimal value must be specified with
        eight characters; the first two characters define the alpha component, and the
        remainder define the red, green, and blue components.

        The value for the gray parameter must be less than or equal to the current
        maximum value as specified by ``Py5Graphics.color_mode()``. The default maximum
        value is 255.

        When drawing in 2D with the default renderer, you may need
        ``hint(ENABLE_STROKE_PURE)`` to improve drawing quality (at the expense of
        performance). See the ``Py5Graphics.hint()`` documentation for more details.

        This method is the same as ``stroke()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``stroke()``.
        """
        pass

    def stroke(self, *args):
        """Sets the color used to draw lines and borders around shapes.

        Underlying Java method: PGraphics.stroke

        Methods
        -------

        You can use any of the following signatures:

         * stroke(gray: float, /) -> None
         * stroke(gray: float, alpha: float, /) -> None
         * stroke(rgb: int, /) -> None
         * stroke(rgb: int, alpha: float, /) -> None
         * stroke(v1: float, v2: float, v3: float, /) -> None
         * stroke(v1: float, v2: float, v3: float, alpha: float, /) -> None

        Parameters
        ----------

        alpha: float
            opacity of the stroke

        gray: float
            specifies a value between white and black

        rgb: int
            color value in hexadecimal notation

        v1: float
            red or hue value (depending on current color mode)

        v2: float
            green or saturation value (depending on current color mode)

        v3: float
            blue or brightness value (depending on current color mode)

        Notes
        -----

        Sets the color used to draw lines and borders around shapes. This color is
        either specified in terms of the RGB or HSB color depending on the current
        ``Py5Graphics.color_mode()``. The default color space is RGB, with each value in
        the range from 0 to 255.

        When using hexadecimal notation to specify a color, use "``0x``" before the
        values (e.g., ``0xFFCCFFAA``). The hexadecimal value must be specified with
        eight characters; the first two characters define the alpha component, and the
        remainder define the red, green, and blue components.

        The value for the gray parameter must be less than or equal to the current
        maximum value as specified by ``Py5Graphics.color_mode()``. The default maximum
        value is 255.

        When drawing in 2D with the default renderer, you may need
        ``hint(ENABLE_STROKE_PURE)`` to improve drawing quality (at the expense of
        performance). See the ``Py5Graphics.hint()`` documentation for more details.

        This method is the same as ``stroke()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``stroke()``.
        """
        return self._instance.stroke(*args)

    def stroke_cap(self, cap: int, /) -> None:
        """Sets the style for rendering line endings.

        Underlying Java method: PGraphics.strokeCap

        Parameters
        ----------

        cap: int
            either SQUARE, PROJECT, or ROUND

        Notes
        -----

        Sets the style for rendering line endings. These ends are either squared,
        extended, or rounded, each of which specified with the corresponding parameters:
        ``SQUARE``, ``PROJECT``, and ``ROUND``. The default cap is ``ROUND``.

        To make ``Py5Graphics.point()`` appear square, use ``stroke_cap(PROJECT)``.
        Using ``stroke_cap(SQUARE)`` (no cap) causes points to become invisible.

        This method is the same as ``stroke_cap()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``stroke_cap()``.
        """
        return self._instance.strokeCap(cap)

    def stroke_join(self, join: int, /) -> None:
        """Sets the style of the joints which connect line segments.

        Underlying Java method: PGraphics.strokeJoin

        Parameters
        ----------

        join: int
            either MITER, BEVEL, ROUND

        Notes
        -----

        Sets the style of the joints which connect line segments. These joints are
        either mitered, beveled, or rounded and specified with the corresponding
        parameters ``MITER``, ``BEVEL``, and ``ROUND``. The default joint is ``MITER``.

        This method is the same as ``stroke_join()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``stroke_join()``.
        """
        return self._instance.strokeJoin(join)

    def stroke_weight(self, weight: float, /) -> None:
        """Sets the width of the stroke used for lines, points, and the border around
        shapes.

        Underlying Java method: PGraphics.strokeWeight

        Parameters
        ----------

        weight: float
            the weight (in pixels) of the stroke

        Notes
        -----

        Sets the width of the stroke used for lines, points, and the border around
        shapes. All widths are set in units of pixels.

        Using ``Py5Graphics.point()`` with ``strokeWeight(1)`` or smaller may draw
        nothing to the Py5Graphics drawing surface, depending on the graphics settings
        of the computer. Workarounds include setting the pixel using the
        ``Py5Graphics.pixels[]`` or ``Py5Graphics.np_pixels[]`` arrays or drawing the
        point using either ``Py5Graphics.circle()`` or ``Py5Graphics.square()``.

        This method is the same as ``stroke_weight()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``stroke_weight()``.
        """
        return self._instance.strokeWeight(weight)

    @overload
    def text(self, c: chr, x: float, y: float, /) -> None:
        """Draws text to the Py5Graphics drawing surface.

        Underlying Java method: PGraphics.text

        Methods
        -------

        You can use any of the following signatures:

         * text(c: chr, x: float, y: float, /) -> None
         * text(c: chr, x: float, y: float, z: float, /) -> None
         * text(chars: List[chr], start: int, stop: int, x: float, y: float, /) -> None
         * text(chars: List[chr], start: int, stop: int, x: float, y: float, z: float, /) -> None
         * text(num: float, x: float, y: float, /) -> None
         * text(num: float, x: float, y: float, z: float, /) -> None
         * text(num: int, x: float, y: float, /) -> None
         * text(num: int, x: float, y: float, z: float, /) -> None
         * text(str: str, x1: float, y1: float, x2: float, y2: float, /) -> None
         * text(str: str, x: float, y: float, /) -> None
         * text(str: str, x: float, y: float, z: float, /) -> None

        Parameters
        ----------

        c: chr
            the alphanumeric character to be displayed

        chars: List[chr]
            the alphanumberic symbols to be displayed

        num: float
            the numeric value to be displayed

        num: int
            the numeric value to be displayed

        start: int
            array index at which to start writing characters

        stop: int
            array index at which to stop writing characters

        str: str
            string to be displayed

        x1: float
            by default, the x-coordinate of text, see rectMode() for more info

        x2: float
            by default, the width of the text box, see rectMode() for more info

        x: float
            x-coordinate of text

        y1: float
            by default, the y-coordinate of text, see rectMode() for more info

        y2: float
            by default, the height of the text box, see rectMode() for more info

        y: float
            y-coordinate of text

        z: float
            z-coordinate of text

        Notes
        -----

        Draws text to the Py5Graphics drawing surface. Displays the information
        specified in the first parameter on the drawing surface in the position
        specified by the additional parameters. A default font will be used unless a
        font is set with the ``Py5Graphics.text_font()`` function and a default size
        will be used unless a font is set with ``Py5Graphics.text_size()``. Change the
        color of the text with the ``Py5Graphics.fill()`` function. The text displays in
        relation to the ``Py5Graphics.text_align()`` function, which gives the option to
        draw to the left, right, and center of the coordinates.

        The ``x2`` and ``y2`` parameters define a rectangular area to display within and
        may only be used with string data. When these parameters are specified, they are
        interpreted based on the current ``Py5Graphics.rect_mode()`` setting. Text that
        does not fit completely within the rectangle specified will not be drawn.

        Note that py5 lets you call ``text()`` without first specifying a Py5Font with
        ``Py5Graphics.text_font()``. In that case, a generic sans-serif font will be
        used instead.

        This method is the same as ``text()`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``text()``.
        """
        pass

    @overload
    def text(self, c: chr, x: float, y: float, z: float, /) -> None:
        """Draws text to the Py5Graphics drawing surface.

        Underlying Java method: PGraphics.text

        Methods
        -------

        You can use any of the following signatures:

         * text(c: chr, x: float, y: float, /) -> None
         * text(c: chr, x: float, y: float, z: float, /) -> None
         * text(chars: List[chr], start: int, stop: int, x: float, y: float, /) -> None
         * text(chars: List[chr], start: int, stop: int, x: float, y: float, z: float, /) -> None
         * text(num: float, x: float, y: float, /) -> None
         * text(num: float, x: float, y: float, z: float, /) -> None
         * text(num: int, x: float, y: float, /) -> None
         * text(num: int, x: float, y: float, z: float, /) -> None
         * text(str: str, x1: float, y1: float, x2: float, y2: float, /) -> None
         * text(str: str, x: float, y: float, /) -> None
         * text(str: str, x: float, y: float, z: float, /) -> None

        Parameters
        ----------

        c: chr
            the alphanumeric character to be displayed

        chars: List[chr]
            the alphanumberic symbols to be displayed

        num: float
            the numeric value to be displayed

        num: int
            the numeric value to be displayed

        start: int
            array index at which to start writing characters

        stop: int
            array index at which to stop writing characters

        str: str
            string to be displayed

        x1: float
            by default, the x-coordinate of text, see rectMode() for more info

        x2: float
            by default, the width of the text box, see rectMode() for more info

        x: float
            x-coordinate of text

        y1: float
            by default, the y-coordinate of text, see rectMode() for more info

        y2: float
            by default, the height of the text box, see rectMode() for more info

        y: float
            y-coordinate of text

        z: float
            z-coordinate of text

        Notes
        -----

        Draws text to the Py5Graphics drawing surface. Displays the information
        specified in the first parameter on the drawing surface in the position
        specified by the additional parameters. A default font will be used unless a
        font is set with the ``Py5Graphics.text_font()`` function and a default size
        will be used unless a font is set with ``Py5Graphics.text_size()``. Change the
        color of the text with the ``Py5Graphics.fill()`` function. The text displays in
        relation to the ``Py5Graphics.text_align()`` function, which gives the option to
        draw to the left, right, and center of the coordinates.

        The ``x2`` and ``y2`` parameters define a rectangular area to display within and
        may only be used with string data. When these parameters are specified, they are
        interpreted based on the current ``Py5Graphics.rect_mode()`` setting. Text that
        does not fit completely within the rectangle specified will not be drawn.

        Note that py5 lets you call ``text()`` without first specifying a Py5Font with
        ``Py5Graphics.text_font()``. In that case, a generic sans-serif font will be
        used instead.

        This method is the same as ``text()`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``text()``.
        """
        pass

    @overload
    def text(self, chars: List[chr], start: int,
             stop: int, x: float, y: float, /) -> None:
        """Draws text to the Py5Graphics drawing surface.

        Underlying Java method: PGraphics.text

        Methods
        -------

        You can use any of the following signatures:

         * text(c: chr, x: float, y: float, /) -> None
         * text(c: chr, x: float, y: float, z: float, /) -> None
         * text(chars: List[chr], start: int, stop: int, x: float, y: float, /) -> None
         * text(chars: List[chr], start: int, stop: int, x: float, y: float, z: float, /) -> None
         * text(num: float, x: float, y: float, /) -> None
         * text(num: float, x: float, y: float, z: float, /) -> None
         * text(num: int, x: float, y: float, /) -> None
         * text(num: int, x: float, y: float, z: float, /) -> None
         * text(str: str, x1: float, y1: float, x2: float, y2: float, /) -> None
         * text(str: str, x: float, y: float, /) -> None
         * text(str: str, x: float, y: float, z: float, /) -> None

        Parameters
        ----------

        c: chr
            the alphanumeric character to be displayed

        chars: List[chr]
            the alphanumberic symbols to be displayed

        num: float
            the numeric value to be displayed

        num: int
            the numeric value to be displayed

        start: int
            array index at which to start writing characters

        stop: int
            array index at which to stop writing characters

        str: str
            string to be displayed

        x1: float
            by default, the x-coordinate of text, see rectMode() for more info

        x2: float
            by default, the width of the text box, see rectMode() for more info

        x: float
            x-coordinate of text

        y1: float
            by default, the y-coordinate of text, see rectMode() for more info

        y2: float
            by default, the height of the text box, see rectMode() for more info

        y: float
            y-coordinate of text

        z: float
            z-coordinate of text

        Notes
        -----

        Draws text to the Py5Graphics drawing surface. Displays the information
        specified in the first parameter on the drawing surface in the position
        specified by the additional parameters. A default font will be used unless a
        font is set with the ``Py5Graphics.text_font()`` function and a default size
        will be used unless a font is set with ``Py5Graphics.text_size()``. Change the
        color of the text with the ``Py5Graphics.fill()`` function. The text displays in
        relation to the ``Py5Graphics.text_align()`` function, which gives the option to
        draw to the left, right, and center of the coordinates.

        The ``x2`` and ``y2`` parameters define a rectangular area to display within and
        may only be used with string data. When these parameters are specified, they are
        interpreted based on the current ``Py5Graphics.rect_mode()`` setting. Text that
        does not fit completely within the rectangle specified will not be drawn.

        Note that py5 lets you call ``text()`` without first specifying a Py5Font with
        ``Py5Graphics.text_font()``. In that case, a generic sans-serif font will be
        used instead.

        This method is the same as ``text()`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``text()``.
        """
        pass

    @overload
    def text(self, chars: List[chr], start: int,
             stop: int, x: float, y: float, z: float, /) -> None:
        """Draws text to the Py5Graphics drawing surface.

        Underlying Java method: PGraphics.text

        Methods
        -------

        You can use any of the following signatures:

         * text(c: chr, x: float, y: float, /) -> None
         * text(c: chr, x: float, y: float, z: float, /) -> None
         * text(chars: List[chr], start: int, stop: int, x: float, y: float, /) -> None
         * text(chars: List[chr], start: int, stop: int, x: float, y: float, z: float, /) -> None
         * text(num: float, x: float, y: float, /) -> None
         * text(num: float, x: float, y: float, z: float, /) -> None
         * text(num: int, x: float, y: float, /) -> None
         * text(num: int, x: float, y: float, z: float, /) -> None
         * text(str: str, x1: float, y1: float, x2: float, y2: float, /) -> None
         * text(str: str, x: float, y: float, /) -> None
         * text(str: str, x: float, y: float, z: float, /) -> None

        Parameters
        ----------

        c: chr
            the alphanumeric character to be displayed

        chars: List[chr]
            the alphanumberic symbols to be displayed

        num: float
            the numeric value to be displayed

        num: int
            the numeric value to be displayed

        start: int
            array index at which to start writing characters

        stop: int
            array index at which to stop writing characters

        str: str
            string to be displayed

        x1: float
            by default, the x-coordinate of text, see rectMode() for more info

        x2: float
            by default, the width of the text box, see rectMode() for more info

        x: float
            x-coordinate of text

        y1: float
            by default, the y-coordinate of text, see rectMode() for more info

        y2: float
            by default, the height of the text box, see rectMode() for more info

        y: float
            y-coordinate of text

        z: float
            z-coordinate of text

        Notes
        -----

        Draws text to the Py5Graphics drawing surface. Displays the information
        specified in the first parameter on the drawing surface in the position
        specified by the additional parameters. A default font will be used unless a
        font is set with the ``Py5Graphics.text_font()`` function and a default size
        will be used unless a font is set with ``Py5Graphics.text_size()``. Change the
        color of the text with the ``Py5Graphics.fill()`` function. The text displays in
        relation to the ``Py5Graphics.text_align()`` function, which gives the option to
        draw to the left, right, and center of the coordinates.

        The ``x2`` and ``y2`` parameters define a rectangular area to display within and
        may only be used with string data. When these parameters are specified, they are
        interpreted based on the current ``Py5Graphics.rect_mode()`` setting. Text that
        does not fit completely within the rectangle specified will not be drawn.

        Note that py5 lets you call ``text()`` without first specifying a Py5Font with
        ``Py5Graphics.text_font()``. In that case, a generic sans-serif font will be
        used instead.

        This method is the same as ``text()`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``text()``.
        """
        pass

    @overload
    def text(self, num: float, x: float, y: float, /) -> None:
        """Draws text to the Py5Graphics drawing surface.

        Underlying Java method: PGraphics.text

        Methods
        -------

        You can use any of the following signatures:

         * text(c: chr, x: float, y: float, /) -> None
         * text(c: chr, x: float, y: float, z: float, /) -> None
         * text(chars: List[chr], start: int, stop: int, x: float, y: float, /) -> None
         * text(chars: List[chr], start: int, stop: int, x: float, y: float, z: float, /) -> None
         * text(num: float, x: float, y: float, /) -> None
         * text(num: float, x: float, y: float, z: float, /) -> None
         * text(num: int, x: float, y: float, /) -> None
         * text(num: int, x: float, y: float, z: float, /) -> None
         * text(str: str, x1: float, y1: float, x2: float, y2: float, /) -> None
         * text(str: str, x: float, y: float, /) -> None
         * text(str: str, x: float, y: float, z: float, /) -> None

        Parameters
        ----------

        c: chr
            the alphanumeric character to be displayed

        chars: List[chr]
            the alphanumberic symbols to be displayed

        num: float
            the numeric value to be displayed

        num: int
            the numeric value to be displayed

        start: int
            array index at which to start writing characters

        stop: int
            array index at which to stop writing characters

        str: str
            string to be displayed

        x1: float
            by default, the x-coordinate of text, see rectMode() for more info

        x2: float
            by default, the width of the text box, see rectMode() for more info

        x: float
            x-coordinate of text

        y1: float
            by default, the y-coordinate of text, see rectMode() for more info

        y2: float
            by default, the height of the text box, see rectMode() for more info

        y: float
            y-coordinate of text

        z: float
            z-coordinate of text

        Notes
        -----

        Draws text to the Py5Graphics drawing surface. Displays the information
        specified in the first parameter on the drawing surface in the position
        specified by the additional parameters. A default font will be used unless a
        font is set with the ``Py5Graphics.text_font()`` function and a default size
        will be used unless a font is set with ``Py5Graphics.text_size()``. Change the
        color of the text with the ``Py5Graphics.fill()`` function. The text displays in
        relation to the ``Py5Graphics.text_align()`` function, which gives the option to
        draw to the left, right, and center of the coordinates.

        The ``x2`` and ``y2`` parameters define a rectangular area to display within and
        may only be used with string data. When these parameters are specified, they are
        interpreted based on the current ``Py5Graphics.rect_mode()`` setting. Text that
        does not fit completely within the rectangle specified will not be drawn.

        Note that py5 lets you call ``text()`` without first specifying a Py5Font with
        ``Py5Graphics.text_font()``. In that case, a generic sans-serif font will be
        used instead.

        This method is the same as ``text()`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``text()``.
        """
        pass

    @overload
    def text(self, num: float, x: float, y: float, z: float, /) -> None:
        """Draws text to the Py5Graphics drawing surface.

        Underlying Java method: PGraphics.text

        Methods
        -------

        You can use any of the following signatures:

         * text(c: chr, x: float, y: float, /) -> None
         * text(c: chr, x: float, y: float, z: float, /) -> None
         * text(chars: List[chr], start: int, stop: int, x: float, y: float, /) -> None
         * text(chars: List[chr], start: int, stop: int, x: float, y: float, z: float, /) -> None
         * text(num: float, x: float, y: float, /) -> None
         * text(num: float, x: float, y: float, z: float, /) -> None
         * text(num: int, x: float, y: float, /) -> None
         * text(num: int, x: float, y: float, z: float, /) -> None
         * text(str: str, x1: float, y1: float, x2: float, y2: float, /) -> None
         * text(str: str, x: float, y: float, /) -> None
         * text(str: str, x: float, y: float, z: float, /) -> None

        Parameters
        ----------

        c: chr
            the alphanumeric character to be displayed

        chars: List[chr]
            the alphanumberic symbols to be displayed

        num: float
            the numeric value to be displayed

        num: int
            the numeric value to be displayed

        start: int
            array index at which to start writing characters

        stop: int
            array index at which to stop writing characters

        str: str
            string to be displayed

        x1: float
            by default, the x-coordinate of text, see rectMode() for more info

        x2: float
            by default, the width of the text box, see rectMode() for more info

        x: float
            x-coordinate of text

        y1: float
            by default, the y-coordinate of text, see rectMode() for more info

        y2: float
            by default, the height of the text box, see rectMode() for more info

        y: float
            y-coordinate of text

        z: float
            z-coordinate of text

        Notes
        -----

        Draws text to the Py5Graphics drawing surface. Displays the information
        specified in the first parameter on the drawing surface in the position
        specified by the additional parameters. A default font will be used unless a
        font is set with the ``Py5Graphics.text_font()`` function and a default size
        will be used unless a font is set with ``Py5Graphics.text_size()``. Change the
        color of the text with the ``Py5Graphics.fill()`` function. The text displays in
        relation to the ``Py5Graphics.text_align()`` function, which gives the option to
        draw to the left, right, and center of the coordinates.

        The ``x2`` and ``y2`` parameters define a rectangular area to display within and
        may only be used with string data. When these parameters are specified, they are
        interpreted based on the current ``Py5Graphics.rect_mode()`` setting. Text that
        does not fit completely within the rectangle specified will not be drawn.

        Note that py5 lets you call ``text()`` without first specifying a Py5Font with
        ``Py5Graphics.text_font()``. In that case, a generic sans-serif font will be
        used instead.

        This method is the same as ``text()`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``text()``.
        """
        pass

    @overload
    def text(self, num: int, x: float, y: float, /) -> None:
        """Draws text to the Py5Graphics drawing surface.

        Underlying Java method: PGraphics.text

        Methods
        -------

        You can use any of the following signatures:

         * text(c: chr, x: float, y: float, /) -> None
         * text(c: chr, x: float, y: float, z: float, /) -> None
         * text(chars: List[chr], start: int, stop: int, x: float, y: float, /) -> None
         * text(chars: List[chr], start: int, stop: int, x: float, y: float, z: float, /) -> None
         * text(num: float, x: float, y: float, /) -> None
         * text(num: float, x: float, y: float, z: float, /) -> None
         * text(num: int, x: float, y: float, /) -> None
         * text(num: int, x: float, y: float, z: float, /) -> None
         * text(str: str, x1: float, y1: float, x2: float, y2: float, /) -> None
         * text(str: str, x: float, y: float, /) -> None
         * text(str: str, x: float, y: float, z: float, /) -> None

        Parameters
        ----------

        c: chr
            the alphanumeric character to be displayed

        chars: List[chr]
            the alphanumberic symbols to be displayed

        num: float
            the numeric value to be displayed

        num: int
            the numeric value to be displayed

        start: int
            array index at which to start writing characters

        stop: int
            array index at which to stop writing characters

        str: str
            string to be displayed

        x1: float
            by default, the x-coordinate of text, see rectMode() for more info

        x2: float
            by default, the width of the text box, see rectMode() for more info

        x: float
            x-coordinate of text

        y1: float
            by default, the y-coordinate of text, see rectMode() for more info

        y2: float
            by default, the height of the text box, see rectMode() for more info

        y: float
            y-coordinate of text

        z: float
            z-coordinate of text

        Notes
        -----

        Draws text to the Py5Graphics drawing surface. Displays the information
        specified in the first parameter on the drawing surface in the position
        specified by the additional parameters. A default font will be used unless a
        font is set with the ``Py5Graphics.text_font()`` function and a default size
        will be used unless a font is set with ``Py5Graphics.text_size()``. Change the
        color of the text with the ``Py5Graphics.fill()`` function. The text displays in
        relation to the ``Py5Graphics.text_align()`` function, which gives the option to
        draw to the left, right, and center of the coordinates.

        The ``x2`` and ``y2`` parameters define a rectangular area to display within and
        may only be used with string data. When these parameters are specified, they are
        interpreted based on the current ``Py5Graphics.rect_mode()`` setting. Text that
        does not fit completely within the rectangle specified will not be drawn.

        Note that py5 lets you call ``text()`` without first specifying a Py5Font with
        ``Py5Graphics.text_font()``. In that case, a generic sans-serif font will be
        used instead.

        This method is the same as ``text()`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``text()``.
        """
        pass

    @overload
    def text(self, num: int, x: float, y: float, z: float, /) -> None:
        """Draws text to the Py5Graphics drawing surface.

        Underlying Java method: PGraphics.text

        Methods
        -------

        You can use any of the following signatures:

         * text(c: chr, x: float, y: float, /) -> None
         * text(c: chr, x: float, y: float, z: float, /) -> None
         * text(chars: List[chr], start: int, stop: int, x: float, y: float, /) -> None
         * text(chars: List[chr], start: int, stop: int, x: float, y: float, z: float, /) -> None
         * text(num: float, x: float, y: float, /) -> None
         * text(num: float, x: float, y: float, z: float, /) -> None
         * text(num: int, x: float, y: float, /) -> None
         * text(num: int, x: float, y: float, z: float, /) -> None
         * text(str: str, x1: float, y1: float, x2: float, y2: float, /) -> None
         * text(str: str, x: float, y: float, /) -> None
         * text(str: str, x: float, y: float, z: float, /) -> None

        Parameters
        ----------

        c: chr
            the alphanumeric character to be displayed

        chars: List[chr]
            the alphanumberic symbols to be displayed

        num: float
            the numeric value to be displayed

        num: int
            the numeric value to be displayed

        start: int
            array index at which to start writing characters

        stop: int
            array index at which to stop writing characters

        str: str
            string to be displayed

        x1: float
            by default, the x-coordinate of text, see rectMode() for more info

        x2: float
            by default, the width of the text box, see rectMode() for more info

        x: float
            x-coordinate of text

        y1: float
            by default, the y-coordinate of text, see rectMode() for more info

        y2: float
            by default, the height of the text box, see rectMode() for more info

        y: float
            y-coordinate of text

        z: float
            z-coordinate of text

        Notes
        -----

        Draws text to the Py5Graphics drawing surface. Displays the information
        specified in the first parameter on the drawing surface in the position
        specified by the additional parameters. A default font will be used unless a
        font is set with the ``Py5Graphics.text_font()`` function and a default size
        will be used unless a font is set with ``Py5Graphics.text_size()``. Change the
        color of the text with the ``Py5Graphics.fill()`` function. The text displays in
        relation to the ``Py5Graphics.text_align()`` function, which gives the option to
        draw to the left, right, and center of the coordinates.

        The ``x2`` and ``y2`` parameters define a rectangular area to display within and
        may only be used with string data. When these parameters are specified, they are
        interpreted based on the current ``Py5Graphics.rect_mode()`` setting. Text that
        does not fit completely within the rectangle specified will not be drawn.

        Note that py5 lets you call ``text()`` without first specifying a Py5Font with
        ``Py5Graphics.text_font()``. In that case, a generic sans-serif font will be
        used instead.

        This method is the same as ``text()`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``text()``.
        """
        pass

    @overload
    def text(self, str: str, x: float, y: float, /) -> None:
        """Draws text to the Py5Graphics drawing surface.

        Underlying Java method: PGraphics.text

        Methods
        -------

        You can use any of the following signatures:

         * text(c: chr, x: float, y: float, /) -> None
         * text(c: chr, x: float, y: float, z: float, /) -> None
         * text(chars: List[chr], start: int, stop: int, x: float, y: float, /) -> None
         * text(chars: List[chr], start: int, stop: int, x: float, y: float, z: float, /) -> None
         * text(num: float, x: float, y: float, /) -> None
         * text(num: float, x: float, y: float, z: float, /) -> None
         * text(num: int, x: float, y: float, /) -> None
         * text(num: int, x: float, y: float, z: float, /) -> None
         * text(str: str, x1: float, y1: float, x2: float, y2: float, /) -> None
         * text(str: str, x: float, y: float, /) -> None
         * text(str: str, x: float, y: float, z: float, /) -> None

        Parameters
        ----------

        c: chr
            the alphanumeric character to be displayed

        chars: List[chr]
            the alphanumberic symbols to be displayed

        num: float
            the numeric value to be displayed

        num: int
            the numeric value to be displayed

        start: int
            array index at which to start writing characters

        stop: int
            array index at which to stop writing characters

        str: str
            string to be displayed

        x1: float
            by default, the x-coordinate of text, see rectMode() for more info

        x2: float
            by default, the width of the text box, see rectMode() for more info

        x: float
            x-coordinate of text

        y1: float
            by default, the y-coordinate of text, see rectMode() for more info

        y2: float
            by default, the height of the text box, see rectMode() for more info

        y: float
            y-coordinate of text

        z: float
            z-coordinate of text

        Notes
        -----

        Draws text to the Py5Graphics drawing surface. Displays the information
        specified in the first parameter on the drawing surface in the position
        specified by the additional parameters. A default font will be used unless a
        font is set with the ``Py5Graphics.text_font()`` function and a default size
        will be used unless a font is set with ``Py5Graphics.text_size()``. Change the
        color of the text with the ``Py5Graphics.fill()`` function. The text displays in
        relation to the ``Py5Graphics.text_align()`` function, which gives the option to
        draw to the left, right, and center of the coordinates.

        The ``x2`` and ``y2`` parameters define a rectangular area to display within and
        may only be used with string data. When these parameters are specified, they are
        interpreted based on the current ``Py5Graphics.rect_mode()`` setting. Text that
        does not fit completely within the rectangle specified will not be drawn.

        Note that py5 lets you call ``text()`` without first specifying a Py5Font with
        ``Py5Graphics.text_font()``. In that case, a generic sans-serif font will be
        used instead.

        This method is the same as ``text()`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``text()``.
        """
        pass

    @overload
    def text(self, str: str, x: float, y: float, z: float, /) -> None:
        """Draws text to the Py5Graphics drawing surface.

        Underlying Java method: PGraphics.text

        Methods
        -------

        You can use any of the following signatures:

         * text(c: chr, x: float, y: float, /) -> None
         * text(c: chr, x: float, y: float, z: float, /) -> None
         * text(chars: List[chr], start: int, stop: int, x: float, y: float, /) -> None
         * text(chars: List[chr], start: int, stop: int, x: float, y: float, z: float, /) -> None
         * text(num: float, x: float, y: float, /) -> None
         * text(num: float, x: float, y: float, z: float, /) -> None
         * text(num: int, x: float, y: float, /) -> None
         * text(num: int, x: float, y: float, z: float, /) -> None
         * text(str: str, x1: float, y1: float, x2: float, y2: float, /) -> None
         * text(str: str, x: float, y: float, /) -> None
         * text(str: str, x: float, y: float, z: float, /) -> None

        Parameters
        ----------

        c: chr
            the alphanumeric character to be displayed

        chars: List[chr]
            the alphanumberic symbols to be displayed

        num: float
            the numeric value to be displayed

        num: int
            the numeric value to be displayed

        start: int
            array index at which to start writing characters

        stop: int
            array index at which to stop writing characters

        str: str
            string to be displayed

        x1: float
            by default, the x-coordinate of text, see rectMode() for more info

        x2: float
            by default, the width of the text box, see rectMode() for more info

        x: float
            x-coordinate of text

        y1: float
            by default, the y-coordinate of text, see rectMode() for more info

        y2: float
            by default, the height of the text box, see rectMode() for more info

        y: float
            y-coordinate of text

        z: float
            z-coordinate of text

        Notes
        -----

        Draws text to the Py5Graphics drawing surface. Displays the information
        specified in the first parameter on the drawing surface in the position
        specified by the additional parameters. A default font will be used unless a
        font is set with the ``Py5Graphics.text_font()`` function and a default size
        will be used unless a font is set with ``Py5Graphics.text_size()``. Change the
        color of the text with the ``Py5Graphics.fill()`` function. The text displays in
        relation to the ``Py5Graphics.text_align()`` function, which gives the option to
        draw to the left, right, and center of the coordinates.

        The ``x2`` and ``y2`` parameters define a rectangular area to display within and
        may only be used with string data. When these parameters are specified, they are
        interpreted based on the current ``Py5Graphics.rect_mode()`` setting. Text that
        does not fit completely within the rectangle specified will not be drawn.

        Note that py5 lets you call ``text()`` without first specifying a Py5Font with
        ``Py5Graphics.text_font()``. In that case, a generic sans-serif font will be
        used instead.

        This method is the same as ``text()`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``text()``.
        """
        pass

    @overload
    def text(self, str: str, x1: float, y1: float,
             x2: float, y2: float, /) -> None:
        """Draws text to the Py5Graphics drawing surface.

        Underlying Java method: PGraphics.text

        Methods
        -------

        You can use any of the following signatures:

         * text(c: chr, x: float, y: float, /) -> None
         * text(c: chr, x: float, y: float, z: float, /) -> None
         * text(chars: List[chr], start: int, stop: int, x: float, y: float, /) -> None
         * text(chars: List[chr], start: int, stop: int, x: float, y: float, z: float, /) -> None
         * text(num: float, x: float, y: float, /) -> None
         * text(num: float, x: float, y: float, z: float, /) -> None
         * text(num: int, x: float, y: float, /) -> None
         * text(num: int, x: float, y: float, z: float, /) -> None
         * text(str: str, x1: float, y1: float, x2: float, y2: float, /) -> None
         * text(str: str, x: float, y: float, /) -> None
         * text(str: str, x: float, y: float, z: float, /) -> None

        Parameters
        ----------

        c: chr
            the alphanumeric character to be displayed

        chars: List[chr]
            the alphanumberic symbols to be displayed

        num: float
            the numeric value to be displayed

        num: int
            the numeric value to be displayed

        start: int
            array index at which to start writing characters

        stop: int
            array index at which to stop writing characters

        str: str
            string to be displayed

        x1: float
            by default, the x-coordinate of text, see rectMode() for more info

        x2: float
            by default, the width of the text box, see rectMode() for more info

        x: float
            x-coordinate of text

        y1: float
            by default, the y-coordinate of text, see rectMode() for more info

        y2: float
            by default, the height of the text box, see rectMode() for more info

        y: float
            y-coordinate of text

        z: float
            z-coordinate of text

        Notes
        -----

        Draws text to the Py5Graphics drawing surface. Displays the information
        specified in the first parameter on the drawing surface in the position
        specified by the additional parameters. A default font will be used unless a
        font is set with the ``Py5Graphics.text_font()`` function and a default size
        will be used unless a font is set with ``Py5Graphics.text_size()``. Change the
        color of the text with the ``Py5Graphics.fill()`` function. The text displays in
        relation to the ``Py5Graphics.text_align()`` function, which gives the option to
        draw to the left, right, and center of the coordinates.

        The ``x2`` and ``y2`` parameters define a rectangular area to display within and
        may only be used with string data. When these parameters are specified, they are
        interpreted based on the current ``Py5Graphics.rect_mode()`` setting. Text that
        does not fit completely within the rectangle specified will not be drawn.

        Note that py5 lets you call ``text()`` without first specifying a Py5Font with
        ``Py5Graphics.text_font()``. In that case, a generic sans-serif font will be
        used instead.

        This method is the same as ``text()`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``text()``.
        """
        pass

    @_text_fix_str
    def text(self, *args):
        """Draws text to the Py5Graphics drawing surface.

        Underlying Java method: PGraphics.text

        Methods
        -------

        You can use any of the following signatures:

         * text(c: chr, x: float, y: float, /) -> None
         * text(c: chr, x: float, y: float, z: float, /) -> None
         * text(chars: List[chr], start: int, stop: int, x: float, y: float, /) -> None
         * text(chars: List[chr], start: int, stop: int, x: float, y: float, z: float, /) -> None
         * text(num: float, x: float, y: float, /) -> None
         * text(num: float, x: float, y: float, z: float, /) -> None
         * text(num: int, x: float, y: float, /) -> None
         * text(num: int, x: float, y: float, z: float, /) -> None
         * text(str: str, x1: float, y1: float, x2: float, y2: float, /) -> None
         * text(str: str, x: float, y: float, /) -> None
         * text(str: str, x: float, y: float, z: float, /) -> None

        Parameters
        ----------

        c: chr
            the alphanumeric character to be displayed

        chars: List[chr]
            the alphanumberic symbols to be displayed

        num: float
            the numeric value to be displayed

        num: int
            the numeric value to be displayed

        start: int
            array index at which to start writing characters

        stop: int
            array index at which to stop writing characters

        str: str
            string to be displayed

        x1: float
            by default, the x-coordinate of text, see rectMode() for more info

        x2: float
            by default, the width of the text box, see rectMode() for more info

        x: float
            x-coordinate of text

        y1: float
            by default, the y-coordinate of text, see rectMode() for more info

        y2: float
            by default, the height of the text box, see rectMode() for more info

        y: float
            y-coordinate of text

        z: float
            z-coordinate of text

        Notes
        -----

        Draws text to the Py5Graphics drawing surface. Displays the information
        specified in the first parameter on the drawing surface in the position
        specified by the additional parameters. A default font will be used unless a
        font is set with the ``Py5Graphics.text_font()`` function and a default size
        will be used unless a font is set with ``Py5Graphics.text_size()``. Change the
        color of the text with the ``Py5Graphics.fill()`` function. The text displays in
        relation to the ``Py5Graphics.text_align()`` function, which gives the option to
        draw to the left, right, and center of the coordinates.

        The ``x2`` and ``y2`` parameters define a rectangular area to display within and
        may only be used with string data. When these parameters are specified, they are
        interpreted based on the current ``Py5Graphics.rect_mode()`` setting. Text that
        does not fit completely within the rectangle specified will not be drawn.

        Note that py5 lets you call ``text()`` without first specifying a Py5Font with
        ``Py5Graphics.text_font()``. In that case, a generic sans-serif font will be
        used instead.

        This method is the same as ``text()`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``text()``.
        """
        return self._instance.text(*args)

    @overload
    def text_align(self, align_x: int, /) -> None:
        """Sets the current alignment for drawing text.

        Underlying Java method: PGraphics.textAlign

        Methods
        -------

        You can use any of the following signatures:

         * text_align(align_x: int, /) -> None
         * text_align(align_x: int, align_y: int, /) -> None

        Parameters
        ----------

        align_x: int
            horizontal alignment, either LEFT, CENTER, or RIGHT

        align_y: int
            vertical alignment, either TOP, BOTTOM, CENTER, or BASELINE

        Notes
        -----

        Sets the current alignment for drawing text. The parameters ``LEFT``,
        ``CENTER``, and ``RIGHT`` set the display characteristics of the letters in
        relation to the values for the ``x`` and ``y`` parameters of the
        ``Py5Graphics.text()`` function.

        An optional second parameter can be used to vertically align the text.
        ``BASELINE`` is the default, and the vertical alignment will be reset to
        ``BASELINE`` if the second parameter is not used. The ``TOP`` and ``CENTER``
        parameters are straightforward. The ``BOTTOM`` parameter offsets the line based
        on the current ``Py5Graphics.text_descent()``. For multiple lines, the final
        line will be aligned to the bottom, with the previous lines appearing above it.

        When using ``Py5Graphics.text()`` with width and height parameters, ``BASELINE``
        is ignored, and treated as ``TOP``. (Otherwise, text would by default draw
        outside the box, since ``BASELINE`` is the default setting. ``BASELINE`` is not
        a useful drawing mode for text drawn in a rectangle.)

        The vertical alignment is based on the value of ``Py5Graphics.text_ascent()``,
        which many fonts do not specify correctly. It may be necessary to use a hack and
        offset by a few pixels by hand so that the offset looks correct. To do this as
        less of a hack, use some percentage of ``Py5Graphics.text_ascent()`` or
        ``Py5Graphics.text_descent()`` so that the hack works even if you change the
        size of the font.

        This method is the same as ``text_align()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``text_align()``.
        """
        pass

    @overload
    def text_align(self, align_x: int, align_y: int, /) -> None:
        """Sets the current alignment for drawing text.

        Underlying Java method: PGraphics.textAlign

        Methods
        -------

        You can use any of the following signatures:

         * text_align(align_x: int, /) -> None
         * text_align(align_x: int, align_y: int, /) -> None

        Parameters
        ----------

        align_x: int
            horizontal alignment, either LEFT, CENTER, or RIGHT

        align_y: int
            vertical alignment, either TOP, BOTTOM, CENTER, or BASELINE

        Notes
        -----

        Sets the current alignment for drawing text. The parameters ``LEFT``,
        ``CENTER``, and ``RIGHT`` set the display characteristics of the letters in
        relation to the values for the ``x`` and ``y`` parameters of the
        ``Py5Graphics.text()`` function.

        An optional second parameter can be used to vertically align the text.
        ``BASELINE`` is the default, and the vertical alignment will be reset to
        ``BASELINE`` if the second parameter is not used. The ``TOP`` and ``CENTER``
        parameters are straightforward. The ``BOTTOM`` parameter offsets the line based
        on the current ``Py5Graphics.text_descent()``. For multiple lines, the final
        line will be aligned to the bottom, with the previous lines appearing above it.

        When using ``Py5Graphics.text()`` with width and height parameters, ``BASELINE``
        is ignored, and treated as ``TOP``. (Otherwise, text would by default draw
        outside the box, since ``BASELINE`` is the default setting. ``BASELINE`` is not
        a useful drawing mode for text drawn in a rectangle.)

        The vertical alignment is based on the value of ``Py5Graphics.text_ascent()``,
        which many fonts do not specify correctly. It may be necessary to use a hack and
        offset by a few pixels by hand so that the offset looks correct. To do this as
        less of a hack, use some percentage of ``Py5Graphics.text_ascent()`` or
        ``Py5Graphics.text_descent()`` so that the hack works even if you change the
        size of the font.

        This method is the same as ``text_align()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``text_align()``.
        """
        pass

    def text_align(self, *args):
        """Sets the current alignment for drawing text.

        Underlying Java method: PGraphics.textAlign

        Methods
        -------

        You can use any of the following signatures:

         * text_align(align_x: int, /) -> None
         * text_align(align_x: int, align_y: int, /) -> None

        Parameters
        ----------

        align_x: int
            horizontal alignment, either LEFT, CENTER, or RIGHT

        align_y: int
            vertical alignment, either TOP, BOTTOM, CENTER, or BASELINE

        Notes
        -----

        Sets the current alignment for drawing text. The parameters ``LEFT``,
        ``CENTER``, and ``RIGHT`` set the display characteristics of the letters in
        relation to the values for the ``x`` and ``y`` parameters of the
        ``Py5Graphics.text()`` function.

        An optional second parameter can be used to vertically align the text.
        ``BASELINE`` is the default, and the vertical alignment will be reset to
        ``BASELINE`` if the second parameter is not used. The ``TOP`` and ``CENTER``
        parameters are straightforward. The ``BOTTOM`` parameter offsets the line based
        on the current ``Py5Graphics.text_descent()``. For multiple lines, the final
        line will be aligned to the bottom, with the previous lines appearing above it.

        When using ``Py5Graphics.text()`` with width and height parameters, ``BASELINE``
        is ignored, and treated as ``TOP``. (Otherwise, text would by default draw
        outside the box, since ``BASELINE`` is the default setting. ``BASELINE`` is not
        a useful drawing mode for text drawn in a rectangle.)

        The vertical alignment is based on the value of ``Py5Graphics.text_ascent()``,
        which many fonts do not specify correctly. It may be necessary to use a hack and
        offset by a few pixels by hand so that the offset looks correct. To do this as
        less of a hack, use some percentage of ``Py5Graphics.text_ascent()`` or
        ``Py5Graphics.text_descent()`` so that the hack works even if you change the
        size of the font.

        This method is the same as ``text_align()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``text_align()``.
        """
        return self._instance.textAlign(*args)

    def text_ascent(self) -> float:
        """Returns ascent of the current font at its current size.

        Underlying Java method: PGraphics.textAscent

        Notes
        -----

        Returns ascent of the current font at its current size. This information is
        useful for determining the height of the font above the baseline.

        This method is the same as ``text_ascent()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``text_ascent()``.
        """
        return self._instance.textAscent()

    def text_descent(self) -> float:
        """Returns descent of the current font at its current size.

        Underlying Java method: PGraphics.textDescent

        Notes
        -----

        Returns descent of the current font at its current size. This information is
        useful for determining the height of the font below the baseline.

        This method is the same as ``text_descent()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``text_descent()``.
        """
        return self._instance.textDescent()

    @overload
    def text_font(self, which: Py5Font, /) -> None:
        """Sets the current font that will be drawn with the ``Py5Graphics.text()``
        function.

        Underlying Java method: PGraphics.textFont

        Methods
        -------

        You can use any of the following signatures:

         * text_font(which: Py5Font, /) -> None
         * text_font(which: Py5Font, size: float, /) -> None

        Parameters
        ----------

        size: float
            the size of the letters in units of pixels

        which: Py5Font
            any variable of the type Py5Font

        Notes
        -----

        Sets the current font that will be drawn with the ``Py5Graphics.text()``
        function. Fonts must be created for py5 with ``create_font()`` or loaded with
        ``load_font()`` before they can be used. The font set through ``text_font()``
        will be used in all subsequent calls to the ``Py5Graphics.text()`` function. If
        no ``size`` parameter is specified, the font size defaults to the original size
        (the size in which it was created with ``create_font_file()``) overriding any
        previous calls to ``text_font()`` or ``Py5Graphics.text_size()``.

        When fonts are rendered as an image texture (as is the case with the ``P2D`` and
        ``P3D`` renderers as well as with ``load_font()`` and vlw files), you should
        create fonts at the sizes that will be used most commonly. Using ``text_font()``
        without the size parameter will result in the cleanest type.

        This method is the same as ``text_font()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``text_font()``.
        """
        pass

    @overload
    def text_font(self, which: Py5Font, size: float, /) -> None:
        """Sets the current font that will be drawn with the ``Py5Graphics.text()``
        function.

        Underlying Java method: PGraphics.textFont

        Methods
        -------

        You can use any of the following signatures:

         * text_font(which: Py5Font, /) -> None
         * text_font(which: Py5Font, size: float, /) -> None

        Parameters
        ----------

        size: float
            the size of the letters in units of pixels

        which: Py5Font
            any variable of the type Py5Font

        Notes
        -----

        Sets the current font that will be drawn with the ``Py5Graphics.text()``
        function. Fonts must be created for py5 with ``create_font()`` or loaded with
        ``load_font()`` before they can be used. The font set through ``text_font()``
        will be used in all subsequent calls to the ``Py5Graphics.text()`` function. If
        no ``size`` parameter is specified, the font size defaults to the original size
        (the size in which it was created with ``create_font_file()``) overriding any
        previous calls to ``text_font()`` or ``Py5Graphics.text_size()``.

        When fonts are rendered as an image texture (as is the case with the ``P2D`` and
        ``P3D`` renderers as well as with ``load_font()`` and vlw files), you should
        create fonts at the sizes that will be used most commonly. Using ``text_font()``
        without the size parameter will result in the cleanest type.

        This method is the same as ``text_font()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``text_font()``.
        """
        pass

    def text_font(self, *args):
        """Sets the current font that will be drawn with the ``Py5Graphics.text()``
        function.

        Underlying Java method: PGraphics.textFont

        Methods
        -------

        You can use any of the following signatures:

         * text_font(which: Py5Font, /) -> None
         * text_font(which: Py5Font, size: float, /) -> None

        Parameters
        ----------

        size: float
            the size of the letters in units of pixels

        which: Py5Font
            any variable of the type Py5Font

        Notes
        -----

        Sets the current font that will be drawn with the ``Py5Graphics.text()``
        function. Fonts must be created for py5 with ``create_font()`` or loaded with
        ``load_font()`` before they can be used. The font set through ``text_font()``
        will be used in all subsequent calls to the ``Py5Graphics.text()`` function. If
        no ``size`` parameter is specified, the font size defaults to the original size
        (the size in which it was created with ``create_font_file()``) overriding any
        previous calls to ``text_font()`` or ``Py5Graphics.text_size()``.

        When fonts are rendered as an image texture (as is the case with the ``P2D`` and
        ``P3D`` renderers as well as with ``load_font()`` and vlw files), you should
        create fonts at the sizes that will be used most commonly. Using ``text_font()``
        without the size parameter will result in the cleanest type.

        This method is the same as ``text_font()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``text_font()``.
        """
        return self._instance.textFont(*args)

    def text_leading(self, leading: float, /) -> None:
        """Sets the spacing between lines of text in units of pixels.

        Underlying Java method: PGraphics.textLeading

        Parameters
        ----------

        leading: float
            the size in pixels for spacing between lines

        Notes
        -----

        Sets the spacing between lines of text in units of pixels. This setting will be
        used in all subsequent calls to the ``Py5Graphics.text()`` function.  Note,
        however, that the leading is reset by ``Py5Graphics.text_size()``. For example,
        if the leading is set to 20 with ``text_leading(20)``, then if ``text_size(48)``
        is run at a later point, the leading will be reset to the default for the text
        size of 48.

        This method is the same as ``text_leading()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``text_leading()``.
        """
        return self._instance.textLeading(leading)

    def text_mode(self, mode: int, /) -> None:
        """Sets the way text draws to the Py5Graphics drawing surface, either as texture
        maps or as vector geometry.

        Underlying Java method: PGraphics.textMode

        Parameters
        ----------

        mode: int
            either MODEL or SHAPE

        Notes
        -----

        Sets the way text draws to the Py5Graphics drawing surface, either as texture
        maps or as vector geometry. The default ``text_mode(MODEL)``, uses textures to
        render the fonts. The ``text_mode(SHAPE)`` mode draws text using the glyph
        outlines of individual characters rather than as textures. This mode is only
        supported with the ``PDF`` and ``P3D`` renderer settings. With the ``PDF``
        renderer, you must call ``text_mode(SHAPE)`` before any other drawing occurs. If
        the outlines are not available, then ``text_mode(SHAPE)`` will be ignored and
        ``text_mode(MODEL)`` will be used instead.

        The ``text_mode(SHAPE)`` option in ``P3D`` can be combined with
        ``Py5Graphics.begin_raw()`` to write vector-accurate text to 2D and 3D output
        files, for instance ``DXF`` or ``PDF``. The ``SHAPE`` mode is not currently
        optimized for ``P3D``, so if recording shape data, use ``text_mode(MODEL)``
        until you're ready to capture the geometry with ``Py5Graphics.begin_raw()``.

        This method is the same as ``text_mode()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``text_mode()``.
        """
        return self._instance.textMode(mode)

    def text_size(self, size: float, /) -> None:
        """Sets the current font size.

        Underlying Java method: PGraphics.textSize

        Parameters
        ----------

        size: float
            the size of the letters in units of pixels

        Notes
        -----

        Sets the current font size. This size will be used in all subsequent calls to
        the ``Py5Graphics.text()`` function. Font size is measured in units of pixels.

        This method is the same as ``text_size()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``text_size()``.
        """
        return self._instance.textSize(size)

    @overload
    def text_width(self, c: chr, /) -> float:
        """Calculates and returns the width of any character or text string.

        Underlying Java method: PGraphics.textWidth

        Methods
        -------

        You can use any of the following signatures:

         * text_width(c: chr, /) -> float
         * text_width(chars: List[chr], start: int, length: int, /) -> float
         * text_width(str: str, /) -> float

        Parameters
        ----------

        c: chr
            the character to measure

        chars: List[chr]
            the character to measure

        length: int
            number of characters to measure

        start: int
            first character to measure

        str: str
            the String of characters to measure

        Notes
        -----

        Calculates and returns the width of any character or text string.

        This method is the same as ``text_width()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``text_width()``.
        """
        pass

    @overload
    def text_width(self, chars: List[chr],
                   start: int, length: int, /) -> float:
        """Calculates and returns the width of any character or text string.

        Underlying Java method: PGraphics.textWidth

        Methods
        -------

        You can use any of the following signatures:

         * text_width(c: chr, /) -> float
         * text_width(chars: List[chr], start: int, length: int, /) -> float
         * text_width(str: str, /) -> float

        Parameters
        ----------

        c: chr
            the character to measure

        chars: List[chr]
            the character to measure

        length: int
            number of characters to measure

        start: int
            first character to measure

        str: str
            the String of characters to measure

        Notes
        -----

        Calculates and returns the width of any character or text string.

        This method is the same as ``text_width()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``text_width()``.
        """
        pass

    @overload
    def text_width(self, str: str, /) -> float:
        """Calculates and returns the width of any character or text string.

        Underlying Java method: PGraphics.textWidth

        Methods
        -------

        You can use any of the following signatures:

         * text_width(c: chr, /) -> float
         * text_width(chars: List[chr], start: int, length: int, /) -> float
         * text_width(str: str, /) -> float

        Parameters
        ----------

        c: chr
            the character to measure

        chars: List[chr]
            the character to measure

        length: int
            number of characters to measure

        start: int
            first character to measure

        str: str
            the String of characters to measure

        Notes
        -----

        Calculates and returns the width of any character or text string.

        This method is the same as ``text_width()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``text_width()``.
        """
        pass

    @_text_fix_str
    def text_width(self, *args):
        """Calculates and returns the width of any character or text string.

        Underlying Java method: PGraphics.textWidth

        Methods
        -------

        You can use any of the following signatures:

         * text_width(c: chr, /) -> float
         * text_width(chars: List[chr], start: int, length: int, /) -> float
         * text_width(str: str, /) -> float

        Parameters
        ----------

        c: chr
            the character to measure

        chars: List[chr]
            the character to measure

        length: int
            number of characters to measure

        start: int
            first character to measure

        str: str
            the String of characters to measure

        Notes
        -----

        Calculates and returns the width of any character or text string.

        This method is the same as ``text_width()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``text_width()``.
        """
        return self._instance.textWidth(*args)

    def texture(self, image: Py5Image, /) -> None:
        """Sets a texture to be applied to vertex points.

        Underlying Java method: PGraphics.texture

        Parameters
        ----------

        image: Py5Image
            reference to a Py5Image object

        Notes
        -----

        Sets a texture to be applied to vertex points. The ``texture()`` method must be
        called between ``Py5Graphics.begin_shape()`` and ``Py5Graphics.end_shape()`` and
        before any calls to ``Py5Graphics.vertex()``. This method only works with the
        ``P2D`` and ``P3D`` renderers.

        When textures are in use, the fill color is ignored. Instead, use
        ``Py5Graphics.tint()`` to specify the color of the texture as it is applied to
        the shape.

        This method is the same as ``texture()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``texture()``.
        """
        return self._instance.texture(image)

    def texture_mode(self, mode: int, /) -> None:
        """Sets the coordinate space for texture mapping.

        Underlying Java method: PGraphics.textureMode

        Parameters
        ----------

        mode: int
            either IMAGE or NORMAL

        Notes
        -----

        Sets the coordinate space for texture mapping. The default mode is ``IMAGE``,
        which refers to the actual pixel coordinates of the image. ``NORMAL`` refers to
        a normalized space of values ranging from 0 to 1. This function only works with
        the ``P2D`` and ``P3D`` renderers.

        With ``IMAGE``, if an image is 100 x 200 pixels, mapping the image onto the
        entire size of a quad would require the points (0,0) (100,0) (100,200) (0,200).
        The same mapping in ``NORMAL`` is (0,0) (1,0) (1,1) (0,1).

        This method is the same as ``texture_mode()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``texture_mode()``.
        """
        return self._instance.textureMode(mode)

    def texture_wrap(self, wrap: int, /) -> None:
        """Defines if textures repeat or draw once within a texture map.

        Underlying Java method: PGraphics.textureWrap

        Parameters
        ----------

        wrap: int
            Either CLAMP (default) or REPEAT

        Notes
        -----

        Defines if textures repeat or draw once within a texture map. The two parameters
        are ``CLAMP`` (the default behavior) and ``REPEAT``. This function only works
        with the ``P2D`` and ``P3D`` renderers.

        This method is the same as ``texture_wrap()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``texture_wrap()``.
        """
        return self._instance.textureWrap(wrap)

    @overload
    def tint(self, gray: float, /) -> None:
        """Sets the fill value for displaying images.

        Underlying Java method: PGraphics.tint

        Methods
        -------

        You can use any of the following signatures:

         * tint(gray: float, /) -> None
         * tint(gray: float, alpha: float, /) -> None
         * tint(rgb: int, /) -> None
         * tint(rgb: int, alpha: float, /) -> None
         * tint(v1: float, v2: float, v3: float, /) -> None
         * tint(v1: float, v2: float, v3: float, alpha: float, /) -> None

        Parameters
        ----------

        alpha: float
            opacity of the image

        gray: float
            specifies a value between white and black

        rgb: int
            color value in hexadecimal notation

        v1: float
            red or hue value (depending on current color mode)

        v2: float
            green or saturation value (depending on current color mode)

        v3: float
            blue or brightness value (depending on current color mode)

        Notes
        -----

        Sets the fill value for displaying images. Images can be tinted to specified
        colors or made transparent by including an alpha value.

        To apply transparency to an image without affecting its color, use white as the
        tint color and specify an alpha value. For instance, ``tint(255, 128)`` will
        make an image 50% transparent (assuming the default alpha range of 0-255, which
        can be changed with ``Py5Graphics.color_mode()``).

        When using hexadecimal notation to specify a color, use "``0x``" before the
        values (e.g., ``0xFFCCFFAA``). The hexadecimal value must be specified with
        eight characters; the first two characters define the alpha component, and the
        remainder define the red, green, and blue components.

        The value for the gray parameter must be less than or equal to the current
        maximum value as specified by ``Py5Graphics.color_mode()``. The default maximum
        value is 255.

        The ``tint()`` function is also used to control the coloring of textures in 3D.

        This method is the same as ``tint()`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``tint()``.
        """
        pass

    @overload
    def tint(self, gray: float, alpha: float, /) -> None:
        """Sets the fill value for displaying images.

        Underlying Java method: PGraphics.tint

        Methods
        -------

        You can use any of the following signatures:

         * tint(gray: float, /) -> None
         * tint(gray: float, alpha: float, /) -> None
         * tint(rgb: int, /) -> None
         * tint(rgb: int, alpha: float, /) -> None
         * tint(v1: float, v2: float, v3: float, /) -> None
         * tint(v1: float, v2: float, v3: float, alpha: float, /) -> None

        Parameters
        ----------

        alpha: float
            opacity of the image

        gray: float
            specifies a value between white and black

        rgb: int
            color value in hexadecimal notation

        v1: float
            red or hue value (depending on current color mode)

        v2: float
            green or saturation value (depending on current color mode)

        v3: float
            blue or brightness value (depending on current color mode)

        Notes
        -----

        Sets the fill value for displaying images. Images can be tinted to specified
        colors or made transparent by including an alpha value.

        To apply transparency to an image without affecting its color, use white as the
        tint color and specify an alpha value. For instance, ``tint(255, 128)`` will
        make an image 50% transparent (assuming the default alpha range of 0-255, which
        can be changed with ``Py5Graphics.color_mode()``).

        When using hexadecimal notation to specify a color, use "``0x``" before the
        values (e.g., ``0xFFCCFFAA``). The hexadecimal value must be specified with
        eight characters; the first two characters define the alpha component, and the
        remainder define the red, green, and blue components.

        The value for the gray parameter must be less than or equal to the current
        maximum value as specified by ``Py5Graphics.color_mode()``. The default maximum
        value is 255.

        The ``tint()`` function is also used to control the coloring of textures in 3D.

        This method is the same as ``tint()`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``tint()``.
        """
        pass

    @overload
    def tint(self, v1: float, v2: float, v3: float, /) -> None:
        """Sets the fill value for displaying images.

        Underlying Java method: PGraphics.tint

        Methods
        -------

        You can use any of the following signatures:

         * tint(gray: float, /) -> None
         * tint(gray: float, alpha: float, /) -> None
         * tint(rgb: int, /) -> None
         * tint(rgb: int, alpha: float, /) -> None
         * tint(v1: float, v2: float, v3: float, /) -> None
         * tint(v1: float, v2: float, v3: float, alpha: float, /) -> None

        Parameters
        ----------

        alpha: float
            opacity of the image

        gray: float
            specifies a value between white and black

        rgb: int
            color value in hexadecimal notation

        v1: float
            red or hue value (depending on current color mode)

        v2: float
            green or saturation value (depending on current color mode)

        v3: float
            blue or brightness value (depending on current color mode)

        Notes
        -----

        Sets the fill value for displaying images. Images can be tinted to specified
        colors or made transparent by including an alpha value.

        To apply transparency to an image without affecting its color, use white as the
        tint color and specify an alpha value. For instance, ``tint(255, 128)`` will
        make an image 50% transparent (assuming the default alpha range of 0-255, which
        can be changed with ``Py5Graphics.color_mode()``).

        When using hexadecimal notation to specify a color, use "``0x``" before the
        values (e.g., ``0xFFCCFFAA``). The hexadecimal value must be specified with
        eight characters; the first two characters define the alpha component, and the
        remainder define the red, green, and blue components.

        The value for the gray parameter must be less than or equal to the current
        maximum value as specified by ``Py5Graphics.color_mode()``. The default maximum
        value is 255.

        The ``tint()`` function is also used to control the coloring of textures in 3D.

        This method is the same as ``tint()`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``tint()``.
        """
        pass

    @overload
    def tint(self, v1: float, v2: float, v3: float, alpha: float, /) -> None:
        """Sets the fill value for displaying images.

        Underlying Java method: PGraphics.tint

        Methods
        -------

        You can use any of the following signatures:

         * tint(gray: float, /) -> None
         * tint(gray: float, alpha: float, /) -> None
         * tint(rgb: int, /) -> None
         * tint(rgb: int, alpha: float, /) -> None
         * tint(v1: float, v2: float, v3: float, /) -> None
         * tint(v1: float, v2: float, v3: float, alpha: float, /) -> None

        Parameters
        ----------

        alpha: float
            opacity of the image

        gray: float
            specifies a value between white and black

        rgb: int
            color value in hexadecimal notation

        v1: float
            red or hue value (depending on current color mode)

        v2: float
            green or saturation value (depending on current color mode)

        v3: float
            blue or brightness value (depending on current color mode)

        Notes
        -----

        Sets the fill value for displaying images. Images can be tinted to specified
        colors or made transparent by including an alpha value.

        To apply transparency to an image without affecting its color, use white as the
        tint color and specify an alpha value. For instance, ``tint(255, 128)`` will
        make an image 50% transparent (assuming the default alpha range of 0-255, which
        can be changed with ``Py5Graphics.color_mode()``).

        When using hexadecimal notation to specify a color, use "``0x``" before the
        values (e.g., ``0xFFCCFFAA``). The hexadecimal value must be specified with
        eight characters; the first two characters define the alpha component, and the
        remainder define the red, green, and blue components.

        The value for the gray parameter must be less than or equal to the current
        maximum value as specified by ``Py5Graphics.color_mode()``. The default maximum
        value is 255.

        The ``tint()`` function is also used to control the coloring of textures in 3D.

        This method is the same as ``tint()`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``tint()``.
        """
        pass

    @overload
    def tint(self, rgb: int, /) -> None:
        """Sets the fill value for displaying images.

        Underlying Java method: PGraphics.tint

        Methods
        -------

        You can use any of the following signatures:

         * tint(gray: float, /) -> None
         * tint(gray: float, alpha: float, /) -> None
         * tint(rgb: int, /) -> None
         * tint(rgb: int, alpha: float, /) -> None
         * tint(v1: float, v2: float, v3: float, /) -> None
         * tint(v1: float, v2: float, v3: float, alpha: float, /) -> None

        Parameters
        ----------

        alpha: float
            opacity of the image

        gray: float
            specifies a value between white and black

        rgb: int
            color value in hexadecimal notation

        v1: float
            red or hue value (depending on current color mode)

        v2: float
            green or saturation value (depending on current color mode)

        v3: float
            blue or brightness value (depending on current color mode)

        Notes
        -----

        Sets the fill value for displaying images. Images can be tinted to specified
        colors or made transparent by including an alpha value.

        To apply transparency to an image without affecting its color, use white as the
        tint color and specify an alpha value. For instance, ``tint(255, 128)`` will
        make an image 50% transparent (assuming the default alpha range of 0-255, which
        can be changed with ``Py5Graphics.color_mode()``).

        When using hexadecimal notation to specify a color, use "``0x``" before the
        values (e.g., ``0xFFCCFFAA``). The hexadecimal value must be specified with
        eight characters; the first two characters define the alpha component, and the
        remainder define the red, green, and blue components.

        The value for the gray parameter must be less than or equal to the current
        maximum value as specified by ``Py5Graphics.color_mode()``. The default maximum
        value is 255.

        The ``tint()`` function is also used to control the coloring of textures in 3D.

        This method is the same as ``tint()`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``tint()``.
        """
        pass

    @overload
    def tint(self, rgb: int, alpha: float, /) -> None:
        """Sets the fill value for displaying images.

        Underlying Java method: PGraphics.tint

        Methods
        -------

        You can use any of the following signatures:

         * tint(gray: float, /) -> None
         * tint(gray: float, alpha: float, /) -> None
         * tint(rgb: int, /) -> None
         * tint(rgb: int, alpha: float, /) -> None
         * tint(v1: float, v2: float, v3: float, /) -> None
         * tint(v1: float, v2: float, v3: float, alpha: float, /) -> None

        Parameters
        ----------

        alpha: float
            opacity of the image

        gray: float
            specifies a value between white and black

        rgb: int
            color value in hexadecimal notation

        v1: float
            red or hue value (depending on current color mode)

        v2: float
            green or saturation value (depending on current color mode)

        v3: float
            blue or brightness value (depending on current color mode)

        Notes
        -----

        Sets the fill value for displaying images. Images can be tinted to specified
        colors or made transparent by including an alpha value.

        To apply transparency to an image without affecting its color, use white as the
        tint color and specify an alpha value. For instance, ``tint(255, 128)`` will
        make an image 50% transparent (assuming the default alpha range of 0-255, which
        can be changed with ``Py5Graphics.color_mode()``).

        When using hexadecimal notation to specify a color, use "``0x``" before the
        values (e.g., ``0xFFCCFFAA``). The hexadecimal value must be specified with
        eight characters; the first two characters define the alpha component, and the
        remainder define the red, green, and blue components.

        The value for the gray parameter must be less than or equal to the current
        maximum value as specified by ``Py5Graphics.color_mode()``. The default maximum
        value is 255.

        The ``tint()`` function is also used to control the coloring of textures in 3D.

        This method is the same as ``tint()`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``tint()``.
        """
        pass

    def tint(self, *args):
        """Sets the fill value for displaying images.

        Underlying Java method: PGraphics.tint

        Methods
        -------

        You can use any of the following signatures:

         * tint(gray: float, /) -> None
         * tint(gray: float, alpha: float, /) -> None
         * tint(rgb: int, /) -> None
         * tint(rgb: int, alpha: float, /) -> None
         * tint(v1: float, v2: float, v3: float, /) -> None
         * tint(v1: float, v2: float, v3: float, alpha: float, /) -> None

        Parameters
        ----------

        alpha: float
            opacity of the image

        gray: float
            specifies a value between white and black

        rgb: int
            color value in hexadecimal notation

        v1: float
            red or hue value (depending on current color mode)

        v2: float
            green or saturation value (depending on current color mode)

        v3: float
            blue or brightness value (depending on current color mode)

        Notes
        -----

        Sets the fill value for displaying images. Images can be tinted to specified
        colors or made transparent by including an alpha value.

        To apply transparency to an image without affecting its color, use white as the
        tint color and specify an alpha value. For instance, ``tint(255, 128)`` will
        make an image 50% transparent (assuming the default alpha range of 0-255, which
        can be changed with ``Py5Graphics.color_mode()``).

        When using hexadecimal notation to specify a color, use "``0x``" before the
        values (e.g., ``0xFFCCFFAA``). The hexadecimal value must be specified with
        eight characters; the first two characters define the alpha component, and the
        remainder define the red, green, and blue components.

        The value for the gray parameter must be less than or equal to the current
        maximum value as specified by ``Py5Graphics.color_mode()``. The default maximum
        value is 255.

        The ``tint()`` function is also used to control the coloring of textures in 3D.

        This method is the same as ``tint()`` but linked to a ``Py5Graphics`` object. To
        see example code for how it can be used, see ``tint()``.
        """
        return self._instance.tint(*args)

    @overload
    def translate(self, x: float, y: float, /) -> None:
        """Specifies an amount to displace objects within the Py5Graphics drawing surface.

        Underlying Java method: PGraphics.translate

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
            forward/backward translation

        Notes
        -----

        Specifies an amount to displace objects within the Py5Graphics drawing surface.
        The ``x`` parameter specifies left/right translation, the ``y`` parameter
        specifies up/down translation, and the ``z`` parameter specifies translations
        toward/away from the screen. Using this function with the ``z`` parameter
        requires using the ``P3D`` renderer.

        Transformations are cumulative and apply to everything that happens after and
        subsequent calls to the function accumulates the effect. For example, calling
        ``translate(50, 0)`` and then ``translate(20, 0)`` is the same as
        ``translate(70, 0)``. This function can be further controlled by using
        ``Py5Graphics.push_matrix()`` and ``Py5Graphics.pop_matrix()``.

        This method is the same as ``translate()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``translate()``.
        """
        pass

    @overload
    def translate(self, x: float, y: float, z: float, /) -> None:
        """Specifies an amount to displace objects within the Py5Graphics drawing surface.

        Underlying Java method: PGraphics.translate

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
            forward/backward translation

        Notes
        -----

        Specifies an amount to displace objects within the Py5Graphics drawing surface.
        The ``x`` parameter specifies left/right translation, the ``y`` parameter
        specifies up/down translation, and the ``z`` parameter specifies translations
        toward/away from the screen. Using this function with the ``z`` parameter
        requires using the ``P3D`` renderer.

        Transformations are cumulative and apply to everything that happens after and
        subsequent calls to the function accumulates the effect. For example, calling
        ``translate(50, 0)`` and then ``translate(20, 0)`` is the same as
        ``translate(70, 0)``. This function can be further controlled by using
        ``Py5Graphics.push_matrix()`` and ``Py5Graphics.pop_matrix()``.

        This method is the same as ``translate()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``translate()``.
        """
        pass

    def translate(self, *args):
        """Specifies an amount to displace objects within the Py5Graphics drawing surface.

        Underlying Java method: PGraphics.translate

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
            forward/backward translation

        Notes
        -----

        Specifies an amount to displace objects within the Py5Graphics drawing surface.
        The ``x`` parameter specifies left/right translation, the ``y`` parameter
        specifies up/down translation, and the ``z`` parameter specifies translations
        toward/away from the screen. Using this function with the ``z`` parameter
        requires using the ``P3D`` renderer.

        Transformations are cumulative and apply to everything that happens after and
        subsequent calls to the function accumulates the effect. For example, calling
        ``translate(50, 0)`` and then ``translate(20, 0)`` is the same as
        ``translate(70, 0)``. This function can be further controlled by using
        ``Py5Graphics.push_matrix()`` and ``Py5Graphics.pop_matrix()``.

        This method is the same as ``translate()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``translate()``.
        """
        return self._instance.translate(*args)

    def triangle(self, x1: float, y1: float, x2: float,
                 y2: float, x3: float, y3: float, /) -> None:
        """A triangle is a plane created by connecting three points.

        Underlying Java method: PGraphics.triangle

        Parameters
        ----------

        x1: float
            x-coordinate of the first point

        x2: float
            x-coordinate of the second point

        x3: float
            x-coordinate of the third point

        y1: float
            y-coordinate of the first point

        y2: float
            y-coordinate of the second point

        y3: float
            y-coordinate of the third point

        Notes
        -----

        A triangle is a plane created by connecting three points. The first two
        arguments specify the first point, the middle two arguments specify the second
        point, and the last two arguments specify the third point.

        This method is the same as ``triangle()`` but linked to a ``Py5Graphics``
        object. To see example code for how it can be used, see ``triangle()``.
        """
        return self._instance.triangle(x1, y1, x2, y2, x3, y3)

    @overload
    def update_pixels(self) -> None:
        """Updates the Py5Graphics drawing surface with the data in the
        ``Py5Graphics.pixels[]`` array.

        Underlying Java method: PGraphics.updatePixels

        Methods
        -------

        You can use any of the following signatures:

         * update_pixels() -> None
         * update_pixels(x: int, y: int, w: int, h: int, /) -> None

        Parameters
        ----------

        h: int
            height of pixel rectangle to update

        w: int
            width of pixel rectangle to update

        x: int
            x-coordinate of the upper left hand corner of rectangle to update

        y: int
            y-coordinate of the upper left hand corner of rectangle to update

        Notes
        -----

        Updates the Py5Graphics drawing surface with the data in the
        ``Py5Graphics.pixels[]`` array. Use in conjunction with
        ``Py5Graphics.load_pixels()``. If you're only reading pixels from the array,
        there's no need to call ``update_pixels()`` — updating is only necessary to
        apply changes.

        Use the ``update_pixels(x, y, w, h)`` syntax to update only a subset of the
        pixel array. This can be faster if only some of the pixels have been changed.

        This method is the same as ``update_pixels()`` but linked to a ``Py5Graphics``
        object.
        """
        pass

    @overload
    def update_pixels(self, x: int, y: int, w: int, h: int, /) -> None:
        """Updates the Py5Graphics drawing surface with the data in the
        ``Py5Graphics.pixels[]`` array.

        Underlying Java method: PGraphics.updatePixels

        Methods
        -------

        You can use any of the following signatures:

         * update_pixels() -> None
         * update_pixels(x: int, y: int, w: int, h: int, /) -> None

        Parameters
        ----------

        h: int
            height of pixel rectangle to update

        w: int
            width of pixel rectangle to update

        x: int
            x-coordinate of the upper left hand corner of rectangle to update

        y: int
            y-coordinate of the upper left hand corner of rectangle to update

        Notes
        -----

        Updates the Py5Graphics drawing surface with the data in the
        ``Py5Graphics.pixels[]`` array. Use in conjunction with
        ``Py5Graphics.load_pixels()``. If you're only reading pixels from the array,
        there's no need to call ``update_pixels()`` — updating is only necessary to
        apply changes.

        Use the ``update_pixels(x, y, w, h)`` syntax to update only a subset of the
        pixel array. This can be faster if only some of the pixels have been changed.

        This method is the same as ``update_pixels()`` but linked to a ``Py5Graphics``
        object.
        """
        pass

    def update_pixels(self, *args):
        """Updates the Py5Graphics drawing surface with the data in the
        ``Py5Graphics.pixels[]`` array.

        Underlying Java method: PGraphics.updatePixels

        Methods
        -------

        You can use any of the following signatures:

         * update_pixels() -> None
         * update_pixels(x: int, y: int, w: int, h: int, /) -> None

        Parameters
        ----------

        h: int
            height of pixel rectangle to update

        w: int
            width of pixel rectangle to update

        x: int
            x-coordinate of the upper left hand corner of rectangle to update

        y: int
            y-coordinate of the upper left hand corner of rectangle to update

        Notes
        -----

        Updates the Py5Graphics drawing surface with the data in the
        ``Py5Graphics.pixels[]`` array. Use in conjunction with
        ``Py5Graphics.load_pixels()``. If you're only reading pixels from the array,
        there's no need to call ``update_pixels()`` — updating is only necessary to
        apply changes.

        Use the ``update_pixels(x, y, w, h)`` syntax to update only a subset of the
        pixel array. This can be faster if only some of the pixels have been changed.

        This method is the same as ``update_pixels()`` but linked to a ``Py5Graphics``
        object.
        """
        return self._instance.updatePixels(*args)

    @overload
    def vertex(self, x: float, y: float, /) -> None:
        """Add a new vertex to a shape.

        Underlying Java method: PGraphics.vertex

        Methods
        -------

        You can use any of the following signatures:

         * vertex(v: NDArray[(Any,), Float], /) -> None
         * vertex(x: float, y: float, /) -> None
         * vertex(x: float, y: float, u: float, v: float, /) -> None
         * vertex(x: float, y: float, z: float, /) -> None
         * vertex(x: float, y: float, z: float, u: float, v: float, /) -> None

        Parameters
        ----------

        u: float
            horizontal coordinate for the texture mapping

        v: NDArray[(Any,), Float]
            vertical coordinate for the texture mapping

        v: float
            vertical coordinate for the texture mapping

        x: float
            x-coordinate of the vertex

        y: float
            y-coordinate of the vertex

        z: float
            z-coordinate of the vertex

        Notes
        -----

        Add a new vertex to a shape. All shapes are constructed by connecting a series
        of vertices. The ``vertex()`` method is used to specify the vertex coordinates
        for points, lines, triangles, quads, and polygons. It is used exclusively within
        the ``Py5Graphics.begin_shape()`` and ``Py5Graphics.end_shape()`` functions.

        Drawing a vertex in 3D using the ``z`` parameter requires the ``P3D`` renderer.

        This method is also used to map a texture onto geometry. The
        ``Py5Graphics.texture()`` function declares the texture to apply to the geometry
        and the ``u`` and ``v`` coordinates define the mapping of this texture to the
        form. By default, the coordinates used for ``u`` and ``v`` are specified in
        relation to the image's size in pixels, but this relation can be changed with
        the ``Py5Graphics.texture_mode()`` method.

        This method is the same as ``vertex()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``vertex()``.
        """
        pass

    @overload
    def vertex(self, x: float, y: float, z: float, /) -> None:
        """Add a new vertex to a shape.

        Underlying Java method: PGraphics.vertex

        Methods
        -------

        You can use any of the following signatures:

         * vertex(v: NDArray[(Any,), Float], /) -> None
         * vertex(x: float, y: float, /) -> None
         * vertex(x: float, y: float, u: float, v: float, /) -> None
         * vertex(x: float, y: float, z: float, /) -> None
         * vertex(x: float, y: float, z: float, u: float, v: float, /) -> None

        Parameters
        ----------

        u: float
            horizontal coordinate for the texture mapping

        v: NDArray[(Any,), Float]
            vertical coordinate for the texture mapping

        v: float
            vertical coordinate for the texture mapping

        x: float
            x-coordinate of the vertex

        y: float
            y-coordinate of the vertex

        z: float
            z-coordinate of the vertex

        Notes
        -----

        Add a new vertex to a shape. All shapes are constructed by connecting a series
        of vertices. The ``vertex()`` method is used to specify the vertex coordinates
        for points, lines, triangles, quads, and polygons. It is used exclusively within
        the ``Py5Graphics.begin_shape()`` and ``Py5Graphics.end_shape()`` functions.

        Drawing a vertex in 3D using the ``z`` parameter requires the ``P3D`` renderer.

        This method is also used to map a texture onto geometry. The
        ``Py5Graphics.texture()`` function declares the texture to apply to the geometry
        and the ``u`` and ``v`` coordinates define the mapping of this texture to the
        form. By default, the coordinates used for ``u`` and ``v`` are specified in
        relation to the image's size in pixels, but this relation can be changed with
        the ``Py5Graphics.texture_mode()`` method.

        This method is the same as ``vertex()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``vertex()``.
        """
        pass

    @overload
    def vertex(self, x: float, y: float, u: float, v: float, /) -> None:
        """Add a new vertex to a shape.

        Underlying Java method: PGraphics.vertex

        Methods
        -------

        You can use any of the following signatures:

         * vertex(v: NDArray[(Any,), Float], /) -> None
         * vertex(x: float, y: float, /) -> None
         * vertex(x: float, y: float, u: float, v: float, /) -> None
         * vertex(x: float, y: float, z: float, /) -> None
         * vertex(x: float, y: float, z: float, u: float, v: float, /) -> None

        Parameters
        ----------

        u: float
            horizontal coordinate for the texture mapping

        v: NDArray[(Any,), Float]
            vertical coordinate for the texture mapping

        v: float
            vertical coordinate for the texture mapping

        x: float
            x-coordinate of the vertex

        y: float
            y-coordinate of the vertex

        z: float
            z-coordinate of the vertex

        Notes
        -----

        Add a new vertex to a shape. All shapes are constructed by connecting a series
        of vertices. The ``vertex()`` method is used to specify the vertex coordinates
        for points, lines, triangles, quads, and polygons. It is used exclusively within
        the ``Py5Graphics.begin_shape()`` and ``Py5Graphics.end_shape()`` functions.

        Drawing a vertex in 3D using the ``z`` parameter requires the ``P3D`` renderer.

        This method is also used to map a texture onto geometry. The
        ``Py5Graphics.texture()`` function declares the texture to apply to the geometry
        and the ``u`` and ``v`` coordinates define the mapping of this texture to the
        form. By default, the coordinates used for ``u`` and ``v`` are specified in
        relation to the image's size in pixels, but this relation can be changed with
        the ``Py5Graphics.texture_mode()`` method.

        This method is the same as ``vertex()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``vertex()``.
        """
        pass

    @overload
    def vertex(self, x: float, y: float, z: float,
               u: float, v: float, /) -> None:
        """Add a new vertex to a shape.

        Underlying Java method: PGraphics.vertex

        Methods
        -------

        You can use any of the following signatures:

         * vertex(v: NDArray[(Any,), Float], /) -> None
         * vertex(x: float, y: float, /) -> None
         * vertex(x: float, y: float, u: float, v: float, /) -> None
         * vertex(x: float, y: float, z: float, /) -> None
         * vertex(x: float, y: float, z: float, u: float, v: float, /) -> None

        Parameters
        ----------

        u: float
            horizontal coordinate for the texture mapping

        v: NDArray[(Any,), Float]
            vertical coordinate for the texture mapping

        v: float
            vertical coordinate for the texture mapping

        x: float
            x-coordinate of the vertex

        y: float
            y-coordinate of the vertex

        z: float
            z-coordinate of the vertex

        Notes
        -----

        Add a new vertex to a shape. All shapes are constructed by connecting a series
        of vertices. The ``vertex()`` method is used to specify the vertex coordinates
        for points, lines, triangles, quads, and polygons. It is used exclusively within
        the ``Py5Graphics.begin_shape()`` and ``Py5Graphics.end_shape()`` functions.

        Drawing a vertex in 3D using the ``z`` parameter requires the ``P3D`` renderer.

        This method is also used to map a texture onto geometry. The
        ``Py5Graphics.texture()`` function declares the texture to apply to the geometry
        and the ``u`` and ``v`` coordinates define the mapping of this texture to the
        form. By default, the coordinates used for ``u`` and ``v`` are specified in
        relation to the image's size in pixels, but this relation can be changed with
        the ``Py5Graphics.texture_mode()`` method.

        This method is the same as ``vertex()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``vertex()``.
        """
        pass

    @overload
    def vertex(self, v: NDArray[(Any,), Float], /) -> None:
        """Add a new vertex to a shape.

        Underlying Java method: PGraphics.vertex

        Methods
        -------

        You can use any of the following signatures:

         * vertex(v: NDArray[(Any,), Float], /) -> None
         * vertex(x: float, y: float, /) -> None
         * vertex(x: float, y: float, u: float, v: float, /) -> None
         * vertex(x: float, y: float, z: float, /) -> None
         * vertex(x: float, y: float, z: float, u: float, v: float, /) -> None

        Parameters
        ----------

        u: float
            horizontal coordinate for the texture mapping

        v: NDArray[(Any,), Float]
            vertical coordinate for the texture mapping

        v: float
            vertical coordinate for the texture mapping

        x: float
            x-coordinate of the vertex

        y: float
            y-coordinate of the vertex

        z: float
            z-coordinate of the vertex

        Notes
        -----

        Add a new vertex to a shape. All shapes are constructed by connecting a series
        of vertices. The ``vertex()`` method is used to specify the vertex coordinates
        for points, lines, triangles, quads, and polygons. It is used exclusively within
        the ``Py5Graphics.begin_shape()`` and ``Py5Graphics.end_shape()`` functions.

        Drawing a vertex in 3D using the ``z`` parameter requires the ``P3D`` renderer.

        This method is also used to map a texture onto geometry. The
        ``Py5Graphics.texture()`` function declares the texture to apply to the geometry
        and the ``u`` and ``v`` coordinates define the mapping of this texture to the
        form. By default, the coordinates used for ``u`` and ``v`` are specified in
        relation to the image's size in pixels, but this relation can be changed with
        the ``Py5Graphics.texture_mode()`` method.

        This method is the same as ``vertex()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``vertex()``.
        """
        pass

    def vertex(self, *args):
        """Add a new vertex to a shape.

        Underlying Java method: PGraphics.vertex

        Methods
        -------

        You can use any of the following signatures:

         * vertex(v: NDArray[(Any,), Float], /) -> None
         * vertex(x: float, y: float, /) -> None
         * vertex(x: float, y: float, u: float, v: float, /) -> None
         * vertex(x: float, y: float, z: float, /) -> None
         * vertex(x: float, y: float, z: float, u: float, v: float, /) -> None

        Parameters
        ----------

        u: float
            horizontal coordinate for the texture mapping

        v: NDArray[(Any,), Float]
            vertical coordinate for the texture mapping

        v: float
            vertical coordinate for the texture mapping

        x: float
            x-coordinate of the vertex

        y: float
            y-coordinate of the vertex

        z: float
            z-coordinate of the vertex

        Notes
        -----

        Add a new vertex to a shape. All shapes are constructed by connecting a series
        of vertices. The ``vertex()`` method is used to specify the vertex coordinates
        for points, lines, triangles, quads, and polygons. It is used exclusively within
        the ``Py5Graphics.begin_shape()`` and ``Py5Graphics.end_shape()`` functions.

        Drawing a vertex in 3D using the ``z`` parameter requires the ``P3D`` renderer.

        This method is also used to map a texture onto geometry. The
        ``Py5Graphics.texture()`` function declares the texture to apply to the geometry
        and the ``u`` and ``v`` coordinates define the mapping of this texture to the
        form. By default, the coordinates used for ``u`` and ``v`` are specified in
        relation to the image's size in pixels, but this relation can be changed with
        the ``Py5Graphics.texture_mode()`` method.

        This method is the same as ``vertex()`` but linked to a ``Py5Graphics`` object.
        To see example code for how it can be used, see ``vertex()``.
        """
        return self._instance.vertex(*args)
