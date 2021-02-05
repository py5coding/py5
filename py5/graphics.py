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
    """Main graphics and rendering context, as well as the base API implementation for
    processing "core".

    Underlying Java class: PGraphics.PGraphics

    Notes
    -----

    Main graphics and rendering context, as well as the base API implementation for
    processing "core". Use this class if you need to draw into an off-screen
    graphics buffer. A PGraphics object can be constructed with the
    ``create_graphics()`` function. The ``begin_draw()`` and ``end_draw()`` methods
    (see above example) are necessary to set up the buffer and to finalize it. The
    fields and methods for this class are extensive. For a complete list, visit the
    developer's reference.

    To create a new graphics context, use the ``create_graphics()`` function. Do not
    use the syntax ``new Py5Graphics()``.
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

    A = 6
    AB = 27
    ADD = 2
    AG = 26
    ALPHA = 4
    ALPHA_MASK = -16777216
    ALT = 18
    AMBIENT = 0
    AR = 25
    ARC = 32
    ARGB = 2
    ARROW = 0
    B = 5
    BACKSPACE = '\b'
    BASELINE = 0
    BEEN_LIT = 35
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
    DA = 6
    DARKEST = 16
    DB = 5
    DEG_TO_RAD = 0.017453292
    DELETE = '\u007f'
    DG = 4
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
    DR = 3
    DXF = "processing.dxf.RawDXF"
    EB = 34
    EDGE = 12
    EG = 33
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
    ER = 32
    ERODE = 17
    ESC = '\u001b'
    EXCLUSION = 64
    FX2D = "processing.javafx.PGraphicsFX2D"
    G = 4
    GIF = 3
    GRAY = 12
    GREEN_MASK = 65280
    GROUP = 0
    HALF_PI = 1.5707964
    HAND = 12
    HARD_LIGHT = 1024
    HAS_NORMAL = 36
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
    NX = 9
    NY = 10
    NZ = 11
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
    R = 3
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
    SA = 16
    SB = 15
    SCREEN = 256
    SG = 14
    SHAPE = 5
    SHIFT = 16
    SHINE = 31
    SOFT_LIGHT = 2048
    SPAN = 0
    SPB = 30
    SPG = 29
    SPHERE = 40
    SPOT = 3
    SPR = 28
    SQUARE = 1
    SR = 13
    SUBTRACT = 4
    SVG = "processing.svg.PGraphicsSVG"
    SW = 17
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
    TX = 18
    TY = 19
    TZ = 20
    U = 7
    UP = 38
    V = 8
    VERTEX = 0
    VERTEX_FIELD_COUNT = 37
    VW = 24
    VX = 21
    VY = 22
    VZ = 23
    WAIT = 3
    WHITESPACE = " \t\n\r\f\u00a0"
    WINDOWS = 1
    X = 0
    Y = 1
    Z = 2

    def _get_height(self) -> int:
        """System variable that stores the height of the display window.

        Underlying Java field: PApplet.height

        Notes
        -----

        System variable that stores the height of the display window. This value is set
        by the second parameter of the ``size()`` function. For example, the function
        call ``size(320, 240)`` sets the ``height`` variable to the value 240. The value
        of ``height`` defaults to 100 if ``size()`` is not used in a program.
        """
        return self._instance.height
    height: int = property(fget=_get_height)

    def _get_pixel_density(self) -> int:
        """This function is new with Processing 3.0.

        Underlying Java method: PApplet.pixelDensity

        Parameters
        ----------

        density: int
            1 or 2

        Notes
        -----

        This function is new with Processing 3.0. It makes it possible for Processing to
        render using all of the pixels on high resolutions screens like Apple Retina
        displays and Windows High-DPI displays. This function can only be run once
        within a program and it must be used right after ``size()`` in a program without
        a ``setup()`` and used within ``setup()`` when a program has one.  The
        ``pixel_density()`` should only be used with hardcoded numbers (in almost all
        cases this number will be 2) or in combination with ``display_density()`` as in
        the third example above.

        When the pixel density is set to more than 1, it changes all of the pixel
        operations including the way ``get()``, ``set()``, ``blend()``, ``copy()``, and
        ``update_pixels()`` all work. See the reference for ``pixel_width`` and
        ``pixel_height`` for more information.

        To use variables as the arguments to ``pixel_density()`` function, place the
        ``pixel_density()`` function within the ``settings()`` function. There is more
        information about this on the ``settings()`` reference page.
        """
        return self._instance.pixelDensity
    pixel_density: int = property(fget=_get_pixel_density)

    def _get_pixel_height(self) -> int:
        """When ``pixel_density(2)`` is used to make use of a high resolution display
        (called a Retina display on OS X or high-dpi on Windows and Linux), the width
        and height of the sketch do not change, but the number of pixels is doubled.

        Underlying Java field: PApplet.pixelHeight

        Notes
        -----

        When ``pixel_density(2)`` is used to make use of a high resolution display
        (called a Retina display on OS X or high-dpi on Windows and Linux), the width
        and height of the sketch do not change, but the number of pixels is doubled. As
        a result, all operations that use pixels (like ``load_pixels()``, ``get()``,
        ``set()``, etc.) happen in this doubled space. As a convenience, the variables
        ``pixel_width`` and ``pixel_height`` hold the actual width and height of the
        sketch in pixels. This is useful for any sketch that uses the ``pixels[]``
        array, for instance, because the number of elements in the array will be
        ``pixel_width*pixel_height``, not ``width*height``.
        """
        return self._instance.pixelHeight
    pixel_height: int = property(fget=_get_pixel_height)

    def _get_pixel_width(self) -> int:
        """When ``pixel_density(2)`` is used to make use of a high resolution display
        (called a Retina display on OS X or high-dpi on Windows and Linux), the width
        and height of the sketch do not change, but the number of pixels is doubled.

        Underlying Java field: PApplet.pixelWidth

        Notes
        -----

        When ``pixel_density(2)`` is used to make use of a high resolution display
        (called a Retina display on OS X or high-dpi on Windows and Linux), the width
        and height of the sketch do not change, but the number of pixels is doubled. As
        a result, all operations that use pixels (like ``load_pixels()``, ``get()``,
        ``set()``, etc.) happen in this doubled space. As a convenience, the variables
        ``pixel_width`` and ``pixel_height`` hold the actual width and height of the
        sketch in pixels. This is useful for any sketch that uses the ``pixels[]``
        array, for instance, because the number of elements in the array will be
        ``pixel_width*pixel_height``, not ``width*height``.
        """
        return self._instance.pixelWidth
    pixel_width: int = property(fget=_get_pixel_width)

    def _get_pixels(self) -> JArray(JInt):
        """The ``pixels[]`` array contains the values for all the pixels in the display
        window.

        Underlying Java field: PApplet.pixels

        Notes
        -----

        The ``pixels[]`` array contains the values for all the pixels in the display
        window. These values are of the color datatype. This array is defined by the
        size of the display window. For example, if the window is 100 x 100 pixels,
        there will be 10,000 values and if the window is 200 x 300 pixels, there will be
        60,000 values. When the pixel density is set to higher than 1 with the
        ``pixel_density()`` function, these values will change. See the reference for
        ``pixel_width`` or ``pixel_height`` for more information.

        Before accessing this array, the data must loaded with the ``load_pixels()``
        function. Failure to do so may result in a NullPointerException. Subsequent
        changes to the display window will not be reflected in ``pixels`` until
        ``load_pixels()`` is called again. After ``pixels`` has been modified, the
        ``update_pixels()`` function must be run to update the content of the display
        window.
        """
        return self._instance.pixels
    pixels: JArray(JInt) = property(fget=_get_pixels)

    def _get_width(self) -> int:
        """System variable that stores the width of the display window.

        Underlying Java field: PApplet.width

        Notes
        -----

        System variable that stores the width of the display window. This value is set
        by the first parameter of the ``size()`` function. For example, the function
        call ``size(320, 240)`` sets the ``width`` variable to the value 320. The value
        of ``width`` defaults to 100 if ``size()`` is not used in a program.
        """
        return self._instance.width
    width: int = property(fget=_get_width)

    def alpha(self, rgb: int, /) -> float:
        """Extracts the alpha value from a color.

        Underlying Java method: PApplet.alpha

        Parameters
        ----------

        rgb: int
            any value of the color datatype

        Notes
        -----

        Extracts the alpha value from a color.
        """
        return self._instance.alpha(rgb)

    @overload
    def ambient(self, gray: float, /) -> None:
        """Sets the ambient reflectance for shapes drawn to the screen.

        Underlying Java method: PApplet.ambient

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
        with the ambient light component of environment. The color components set
        through the parameters define the reflectance. For example in the default color
        mode, setting v1=255, v2=127, v3=0, would cause all the red light to reflect and
        half of the green light to reflect. Used in combination with ``emissive()``,
        ``specular()``, and ``shininess()`` in setting the material properties of
        shapes.
        """
        pass

    @overload
    def ambient(self, v1: float, v2: float, v3: float, /) -> None:
        """Sets the ambient reflectance for shapes drawn to the screen.

        Underlying Java method: PApplet.ambient

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
        with the ambient light component of environment. The color components set
        through the parameters define the reflectance. For example in the default color
        mode, setting v1=255, v2=127, v3=0, would cause all the red light to reflect and
        half of the green light to reflect. Used in combination with ``emissive()``,
        ``specular()``, and ``shininess()`` in setting the material properties of
        shapes.
        """
        pass

    @overload
    def ambient(self, rgb: int, /) -> None:
        """Sets the ambient reflectance for shapes drawn to the screen.

        Underlying Java method: PApplet.ambient

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
        with the ambient light component of environment. The color components set
        through the parameters define the reflectance. For example in the default color
        mode, setting v1=255, v2=127, v3=0, would cause all the red light to reflect and
        half of the green light to reflect. Used in combination with ``emissive()``,
        ``specular()``, and ``shininess()`` in setting the material properties of
        shapes.
        """
        pass

    def ambient(self, *args):
        """Sets the ambient reflectance for shapes drawn to the screen.

        Underlying Java method: PApplet.ambient

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
        with the ambient light component of environment. The color components set
        through the parameters define the reflectance. For example in the default color
        mode, setting v1=255, v2=127, v3=0, would cause all the red light to reflect and
        half of the green light to reflect. Used in combination with ``emissive()``,
        ``specular()``, and ``shininess()`` in setting the material properties of
        shapes.
        """
        return self._instance.ambient(*args)

    @overload
    def ambient_light(self, v1: float, v2: float, v3: float, /) -> None:
        """Adds an ambient light.

        Underlying Java method: PApplet.ambientLight

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
        lights. Lights need to be included in the ``draw()`` to remain persistent in a
        looping program. Placing them in the ``setup()`` of a looping program will cause
        them to only have an effect the first time through the loop. The ``v1``, ``v2``,
        and ``v3`` parameters are interpreted as either RGB or HSB values, depending on
        the current color mode.
        """
        pass

    @overload
    def ambient_light(self, v1: float, v2: float, v3: float,
                      x: float, y: float, z: float, /) -> None:
        """Adds an ambient light.

        Underlying Java method: PApplet.ambientLight

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
        lights. Lights need to be included in the ``draw()`` to remain persistent in a
        looping program. Placing them in the ``setup()`` of a looping program will cause
        them to only have an effect the first time through the loop. The ``v1``, ``v2``,
        and ``v3`` parameters are interpreted as either RGB or HSB values, depending on
        the current color mode.
        """
        pass

    def ambient_light(self, *args):
        """Adds an ambient light.

        Underlying Java method: PApplet.ambientLight

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
        lights. Lights need to be included in the ``draw()`` to remain persistent in a
        looping program. Placing them in the ``setup()`` of a looping program will cause
        them to only have an effect the first time through the loop. The ``v1``, ``v2``,
        and ``v3`` parameters are interpreted as either RGB or HSB values, depending on
        the current color mode.
        """
        return self._instance.ambientLight(*args)

    @overload
    def apply_matrix(self, n00: float, n01: float, n02: float,
                     n10: float, n11: float, n12: float, /) -> None:
        """Multiplies the current matrix by the one specified through the parameters.

        Underlying Java method: PApplet.applyMatrix

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
            missing variable description

        source: NDArray[(4, 4), Float]
            missing variable description

        Notes
        -----

        Multiplies the current matrix by the one specified through the parameters. This
        is very slow because it will try to calculate the inverse of the transform, so
        avoid it whenever possible. The equivalent function in OpenGL is
        ``gl_mult_matrix()``.
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

        Underlying Java method: PApplet.applyMatrix

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
            missing variable description

        source: NDArray[(4, 4), Float]
            missing variable description

        Notes
        -----

        Multiplies the current matrix by the one specified through the parameters. This
        is very slow because it will try to calculate the inverse of the transform, so
        avoid it whenever possible. The equivalent function in OpenGL is
        ``gl_mult_matrix()``.
        """
        pass

    @overload
    def apply_matrix(self, source: NDArray[(2, 3), Float], /) -> None:
        """Multiplies the current matrix by the one specified through the parameters.

        Underlying Java method: PApplet.applyMatrix

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
            missing variable description

        source: NDArray[(4, 4), Float]
            missing variable description

        Notes
        -----

        Multiplies the current matrix by the one specified through the parameters. This
        is very slow because it will try to calculate the inverse of the transform, so
        avoid it whenever possible. The equivalent function in OpenGL is
        ``gl_mult_matrix()``.
        """
        pass

    @overload
    def apply_matrix(self, source: NDArray[(4, 4), Float], /) -> None:
        """Multiplies the current matrix by the one specified through the parameters.

        Underlying Java method: PApplet.applyMatrix

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
            missing variable description

        source: NDArray[(4, 4), Float]
            missing variable description

        Notes
        -----

        Multiplies the current matrix by the one specified through the parameters. This
        is very slow because it will try to calculate the inverse of the transform, so
        avoid it whenever possible. The equivalent function in OpenGL is
        ``gl_mult_matrix()``.
        """
        pass

    def apply_matrix(self, *args):
        """Multiplies the current matrix by the one specified through the parameters.

        Underlying Java method: PApplet.applyMatrix

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
            missing variable description

        source: NDArray[(4, 4), Float]
            missing variable description

        Notes
        -----

        Multiplies the current matrix by the one specified through the parameters. This
        is very slow because it will try to calculate the inverse of the transform, so
        avoid it whenever possible. The equivalent function in OpenGL is
        ``gl_mult_matrix()``.
        """
        return self._instance.applyMatrix(*args)

    @overload
    def arc(self, a: float, b: float, c: float, d: float,
            start: float, stop: float, /) -> None:
        """Draws an arc to the screen.

        Underlying Java method: PApplet.arc

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
            missing variable description

        start: float
            angle to start the arc, specified in radians

        stop: float
            angle to stop the arc, specified in radians

        Notes
        -----

        Draws an arc to the screen. Arcs are drawn along the outer edge of an ellipse
        defined by the ``a``, ``b``, ``c``, and ``d`` parameters. The origin of the
        arc's ellipse may be changed with the ``ellipse_mode()`` function. Use the
        ``start`` and ``stop`` parameters to specify the angles (in radians) at which to
        draw the arc. The start/stop values must be in clockwise order.

        There are three ways to draw an arc; the rendering technique used is defined by
        the optional seventh parameter. The three options, depicted in the above
        examples, are PIE, OPEN, and CHORD. The default mode is the OPEN stroke with a
        PIE fill.

        In some cases, the ``arc()`` function isn't accurate enough for smooth drawing.
        For example, the shape may jitter on screen when rotating slowly. If you're
        having an issue with how arcs are rendered, you'll need to draw the arc yourself
        with ``begin_shape()``/``end_shape()`` or a ``Py5Shape``.
        """
        pass

    @overload
    def arc(self, a: float, b: float, c: float, d: float,
            start: float, stop: float, mode: int, /) -> None:
        """Draws an arc to the screen.

        Underlying Java method: PApplet.arc

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
            missing variable description

        start: float
            angle to start the arc, specified in radians

        stop: float
            angle to stop the arc, specified in radians

        Notes
        -----

        Draws an arc to the screen. Arcs are drawn along the outer edge of an ellipse
        defined by the ``a``, ``b``, ``c``, and ``d`` parameters. The origin of the
        arc's ellipse may be changed with the ``ellipse_mode()`` function. Use the
        ``start`` and ``stop`` parameters to specify the angles (in radians) at which to
        draw the arc. The start/stop values must be in clockwise order.

        There are three ways to draw an arc; the rendering technique used is defined by
        the optional seventh parameter. The three options, depicted in the above
        examples, are PIE, OPEN, and CHORD. The default mode is the OPEN stroke with a
        PIE fill.

        In some cases, the ``arc()`` function isn't accurate enough for smooth drawing.
        For example, the shape may jitter on screen when rotating slowly. If you're
        having an issue with how arcs are rendered, you'll need to draw the arc yourself
        with ``begin_shape()``/``end_shape()`` or a ``Py5Shape``.
        """
        pass

    def arc(self, *args):
        """Draws an arc to the screen.

        Underlying Java method: PApplet.arc

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
            missing variable description

        start: float
            angle to start the arc, specified in radians

        stop: float
            angle to stop the arc, specified in radians

        Notes
        -----

        Draws an arc to the screen. Arcs are drawn along the outer edge of an ellipse
        defined by the ``a``, ``b``, ``c``, and ``d`` parameters. The origin of the
        arc's ellipse may be changed with the ``ellipse_mode()`` function. Use the
        ``start`` and ``stop`` parameters to specify the angles (in radians) at which to
        draw the arc. The start/stop values must be in clockwise order.

        There are three ways to draw an arc; the rendering technique used is defined by
        the optional seventh parameter. The three options, depicted in the above
        examples, are PIE, OPEN, and CHORD. The default mode is the OPEN stroke with a
        PIE fill.

        In some cases, the ``arc()`` function isn't accurate enough for smooth drawing.
        For example, the shape may jitter on screen when rotating slowly. If you're
        having an issue with how arcs are rendered, you'll need to draw the arc yourself
        with ``begin_shape()``/``end_shape()`` or a ``Py5Shape``.
        """
        return self._instance.arc(*args)

    @overload
    def background(self, gray: float, /) -> None:
        """The ``background()`` function sets the color used for the background of the
        Processing window.

        Underlying Java method: PApplet.background

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
            PImage to set as background (must be same size as the sketch window)

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
        Processing window. The default background is light gray. This function is
        typically used within ``draw()`` to clear the display window at the beginning of
        each frame, but it can be used inside ``setup()`` to set the background on the
        first frame of animation or if the backgound need only be set once.

        An image can also be used as the background for a sketch, although the image's
        width and height must match that of the sketch window. Images used with
        ``background()`` will ignore the current ``tint()`` setting. To resize an image
        to the size of the sketch window, use image.resize(width, height).

        It is not possible to use the transparency ``alpha`` parameter with background
        colors on the main drawing surface. It can only be used along with a
        ``Py5Graphics`` object and ``create_graphics()``.
        """
        pass

    @overload
    def background(self, gray: float, alpha: float, /) -> None:
        """The ``background()`` function sets the color used for the background of the
        Processing window.

        Underlying Java method: PApplet.background

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
            PImage to set as background (must be same size as the sketch window)

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
        Processing window. The default background is light gray. This function is
        typically used within ``draw()`` to clear the display window at the beginning of
        each frame, but it can be used inside ``setup()`` to set the background on the
        first frame of animation or if the backgound need only be set once.

        An image can also be used as the background for a sketch, although the image's
        width and height must match that of the sketch window. Images used with
        ``background()`` will ignore the current ``tint()`` setting. To resize an image
        to the size of the sketch window, use image.resize(width, height).

        It is not possible to use the transparency ``alpha`` parameter with background
        colors on the main drawing surface. It can only be used along with a
        ``Py5Graphics`` object and ``create_graphics()``.
        """
        pass

    @overload
    def background(self, v1: float, v2: float, v3: float, /) -> None:
        """The ``background()`` function sets the color used for the background of the
        Processing window.

        Underlying Java method: PApplet.background

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
            PImage to set as background (must be same size as the sketch window)

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
        Processing window. The default background is light gray. This function is
        typically used within ``draw()`` to clear the display window at the beginning of
        each frame, but it can be used inside ``setup()`` to set the background on the
        first frame of animation or if the backgound need only be set once.

        An image can also be used as the background for a sketch, although the image's
        width and height must match that of the sketch window. Images used with
        ``background()`` will ignore the current ``tint()`` setting. To resize an image
        to the size of the sketch window, use image.resize(width, height).

        It is not possible to use the transparency ``alpha`` parameter with background
        colors on the main drawing surface. It can only be used along with a
        ``Py5Graphics`` object and ``create_graphics()``.
        """
        pass

    @overload
    def background(self, v1: float, v2: float,
                   v3: float, alpha: float, /) -> None:
        """The ``background()`` function sets the color used for the background of the
        Processing window.

        Underlying Java method: PApplet.background

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
            PImage to set as background (must be same size as the sketch window)

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
        Processing window. The default background is light gray. This function is
        typically used within ``draw()`` to clear the display window at the beginning of
        each frame, but it can be used inside ``setup()`` to set the background on the
        first frame of animation or if the backgound need only be set once.

        An image can also be used as the background for a sketch, although the image's
        width and height must match that of the sketch window. Images used with
        ``background()`` will ignore the current ``tint()`` setting. To resize an image
        to the size of the sketch window, use image.resize(width, height).

        It is not possible to use the transparency ``alpha`` parameter with background
        colors on the main drawing surface. It can only be used along with a
        ``Py5Graphics`` object and ``create_graphics()``.
        """
        pass

    @overload
    def background(self, rgb: int, /) -> None:
        """The ``background()`` function sets the color used for the background of the
        Processing window.

        Underlying Java method: PApplet.background

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
            PImage to set as background (must be same size as the sketch window)

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
        Processing window. The default background is light gray. This function is
        typically used within ``draw()`` to clear the display window at the beginning of
        each frame, but it can be used inside ``setup()`` to set the background on the
        first frame of animation or if the backgound need only be set once.

        An image can also be used as the background for a sketch, although the image's
        width and height must match that of the sketch window. Images used with
        ``background()`` will ignore the current ``tint()`` setting. To resize an image
        to the size of the sketch window, use image.resize(width, height).

        It is not possible to use the transparency ``alpha`` parameter with background
        colors on the main drawing surface. It can only be used along with a
        ``Py5Graphics`` object and ``create_graphics()``.
        """
        pass

    @overload
    def background(self, rgb: int, alpha: float, /) -> None:
        """The ``background()`` function sets the color used for the background of the
        Processing window.

        Underlying Java method: PApplet.background

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
            PImage to set as background (must be same size as the sketch window)

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
        Processing window. The default background is light gray. This function is
        typically used within ``draw()`` to clear the display window at the beginning of
        each frame, but it can be used inside ``setup()`` to set the background on the
        first frame of animation or if the backgound need only be set once.

        An image can also be used as the background for a sketch, although the image's
        width and height must match that of the sketch window. Images used with
        ``background()`` will ignore the current ``tint()`` setting. To resize an image
        to the size of the sketch window, use image.resize(width, height).

        It is not possible to use the transparency ``alpha`` parameter with background
        colors on the main drawing surface. It can only be used along with a
        ``Py5Graphics`` object and ``create_graphics()``.
        """
        pass

    @overload
    def background(self, image: Py5Image, /) -> None:
        """The ``background()`` function sets the color used for the background of the
        Processing window.

        Underlying Java method: PApplet.background

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
            PImage to set as background (must be same size as the sketch window)

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
        Processing window. The default background is light gray. This function is
        typically used within ``draw()`` to clear the display window at the beginning of
        each frame, but it can be used inside ``setup()`` to set the background on the
        first frame of animation or if the backgound need only be set once.

        An image can also be used as the background for a sketch, although the image's
        width and height must match that of the sketch window. Images used with
        ``background()`` will ignore the current ``tint()`` setting. To resize an image
        to the size of the sketch window, use image.resize(width, height).

        It is not possible to use the transparency ``alpha`` parameter with background
        colors on the main drawing surface. It can only be used along with a
        ``Py5Graphics`` object and ``create_graphics()``.
        """
        pass

    def background(self, *args):
        """The ``background()`` function sets the color used for the background of the
        Processing window.

        Underlying Java method: PApplet.background

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
            PImage to set as background (must be same size as the sketch window)

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
        Processing window. The default background is light gray. This function is
        typically used within ``draw()`` to clear the display window at the beginning of
        each frame, but it can be used inside ``setup()`` to set the background on the
        first frame of animation or if the backgound need only be set once.

        An image can also be used as the background for a sketch, although the image's
        width and height must match that of the sketch window. Images used with
        ``background()`` will ignore the current ``tint()`` setting. To resize an image
        to the size of the sketch window, use image.resize(width, height).

        It is not possible to use the transparency ``alpha`` parameter with background
        colors on the main drawing surface. It can only be used along with a
        ``Py5Graphics`` object and ``create_graphics()``.
        """
        return self._instance.background(*args)

    def begin_camera(self) -> None:
        """The ``begin_camera()`` and ``end_camera()`` functions enable advanced
        customization of the camera space.

        Underlying Java method: PApplet.beginCamera

        Notes
        -----

        The ``begin_camera()`` and ``end_camera()`` functions enable advanced
        customization of the camera space. The functions are useful if you want to more
        control over camera movement, however for most users, the ``camera()`` function
        will be sufficient.The camera functions will replace any transformations (such
        as ``rotate()`` or ``translate()``) that occur before them in ``draw()``, but
        they will not automatically replace the camera transform itself. For this
        reason, camera functions should be placed at the beginning of ``draw()`` (so
        that transformations happen afterwards), and the ``camera()`` function can be
        used after ``begin_camera()`` if you want to reset the camera before applying
        transformations.This function sets the matrix mode to the camera matrix so calls
        such as ``translate()``, ``rotate()``, ``apply_matrix()`` and ``reset_matrix()``
        affect the camera. ``begin_camera()`` should always be used with a following
        ``end_camera()`` and pairs of ``begin_camera()`` and ``end_camera()`` cannot be
        nested.
        """
        return self._instance.beginCamera()

    def begin_contour(self) -> None:
        """Use the ``begin_contour()`` and ``end_contour()`` function to create negative
        shapes within shapes such as the center of the letter 'O'.

        Underlying Java method: PApplet.beginContour

        Notes
        -----

        Use the ``begin_contour()`` and ``end_contour()`` function to create negative
        shapes within shapes such as the center of the letter 'O'. ``begin_contour()``
        begins recording vertices for the shape and ``end_contour()`` stops recording.
        The vertices that define a negative shape must "wind" in the opposite direction
        from the exterior shape. First draw vertices for the exterior shape in clockwise
        order, then for internal shapes, draw vertices counterclockwise.

        These functions can only be used within a ``begin_shape()``/``end_shape()`` pair
        and transformations such as ``translate()``, ``rotate()``, and ``scale()`` do
        not work within a ``begin_contour()``/``end_contour()`` pair. It is also not
        possible to use other shapes, such as ``ellipse()`` or ``rect()`` within.
        """
        return self._instance.beginContour()

    def begin_draw(self) -> None:
        """Sets the default properties for a PGraphics object.

        Underlying Java method: PGraphics.beginDraw

        Notes
        -----

        Sets the default properties for a PGraphics object. It should be called before
        anything is drawn into the object.
        """
        return self._instance.beginDraw()

    def begin_raw(self, raw_graphics: Py5Graphics, /) -> None:
        """To create vectors from 3D data, use the ``begin_raw()`` and ``end_raw()``
        commands.

        Underlying Java method: PApplet.beginRaw

        Methods
        -------

        You can use any of the following signatures:

         * begin_raw(raw_graphics: Py5Graphics, /) -> None
         * begin_raw(renderer: str, filename: str, /) -> Py5Graphics

        Parameters
        ----------

        filename: str
            filename for output

        raw_graphics: Py5Graphics
            ???

        renderer: str
            for example, PDF or DXF

        Notes
        -----

        To create vectors from 3D data, use the ``begin_raw()`` and ``end_raw()``
        commands. These commands will grab the shape data just before it is rendered to
        the screen. At this stage, your entire scene is nothing but a long list of
        individual lines and triangles. This means that a shape created with
        ``sphere()`` function will be made up of hundreds of triangles, rather than a
        single object. Or that a multi-segment line shape (such as a curve) will be
        rendered as individual segments.

        When using ``begin_raw()`` and ``end_raw()``, it's possible to write to either a
        2D or 3D renderer. For instance, ``begin_raw()`` with the PDF library will write
        the geometry as flattened triangles and lines, even if recording from the
        ``P3D`` renderer.

        If you want a background to show up in your files, use ``rect(0, 0, width,
        height)`` after setting the ``fill()`` to the background color. Otherwise the
        background will not be rendered to the file because the background is not shape.

        Using ``hint(ENABLE_DEPTH_SORT)`` can improve the appearance of 3D geometry
        drawn to 2D file formats.

        See examples in the reference for the ``PDF`` and ``DXF`` libraries for more
        information.
        """
        return self._instance.beginRaw(raw_graphics)

    @overload
    def begin_shape(self) -> None:
        """Using the ``begin_shape()`` and ``end_shape()`` functions allow creating more
        complex forms.

        Underlying Java method: PApplet.beginShape

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

        Using the ``begin_shape()`` and ``end_shape()`` functions allow creating more
        complex forms. ``begin_shape()`` begins recording vertices for a shape and
        ``end_shape()`` stops recording. The value of the ``kind`` parameter tells it
        which types of shapes to create from the provided vertices. With no mode
        specified, the shape can be any irregular polygon. The parameters available for
        ``begin_shape()`` are POINTS, LINES, TRIANGLES, TRIANGLE_FAN, TRIANGLE_STRIP,
        QUADS, and QUAD_STRIP. After calling the ``begin_shape()`` function, a series of
        ``vertex()`` commands must follow. To stop drawing the shape, call
        ``end_shape()``. The ``vertex()`` function with two parameters specifies a
        position in 2D and the ``vertex()`` function with three parameters specifies a
        position in 3D. Each shape will be outlined with the current stroke color and
        filled with the fill color.

        Transformations such as ``translate()``, ``rotate()``, and ``scale()`` do not
        work within ``begin_shape()``. It is also not possible to use other shapes, such
        as ``ellipse()`` or ``rect()`` within ``begin_shape()``.

        The P2D and P3D renderers allow ``stroke()`` and ``fill()`` to be altered on a
        per-vertex basis, but the default renderer does not. Settings such as
        ``stroke_weight()``, ``stroke_cap()``, and ``stroke_join()`` cannot be changed
        while inside a ``begin_shape()``/``end_shape()`` block with any renderer.
        """
        pass

    @overload
    def begin_shape(self, kind: int, /) -> None:
        """Using the ``begin_shape()`` and ``end_shape()`` functions allow creating more
        complex forms.

        Underlying Java method: PApplet.beginShape

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

        Using the ``begin_shape()`` and ``end_shape()`` functions allow creating more
        complex forms. ``begin_shape()`` begins recording vertices for a shape and
        ``end_shape()`` stops recording. The value of the ``kind`` parameter tells it
        which types of shapes to create from the provided vertices. With no mode
        specified, the shape can be any irregular polygon. The parameters available for
        ``begin_shape()`` are POINTS, LINES, TRIANGLES, TRIANGLE_FAN, TRIANGLE_STRIP,
        QUADS, and QUAD_STRIP. After calling the ``begin_shape()`` function, a series of
        ``vertex()`` commands must follow. To stop drawing the shape, call
        ``end_shape()``. The ``vertex()`` function with two parameters specifies a
        position in 2D and the ``vertex()`` function with three parameters specifies a
        position in 3D. Each shape will be outlined with the current stroke color and
        filled with the fill color.

        Transformations such as ``translate()``, ``rotate()``, and ``scale()`` do not
        work within ``begin_shape()``. It is also not possible to use other shapes, such
        as ``ellipse()`` or ``rect()`` within ``begin_shape()``.

        The P2D and P3D renderers allow ``stroke()`` and ``fill()`` to be altered on a
        per-vertex basis, but the default renderer does not. Settings such as
        ``stroke_weight()``, ``stroke_cap()``, and ``stroke_join()`` cannot be changed
        while inside a ``begin_shape()``/``end_shape()`` block with any renderer.
        """
        pass

    def begin_shape(self, *args):
        """Using the ``begin_shape()`` and ``end_shape()`` functions allow creating more
        complex forms.

        Underlying Java method: PApplet.beginShape

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

        Using the ``begin_shape()`` and ``end_shape()`` functions allow creating more
        complex forms. ``begin_shape()`` begins recording vertices for a shape and
        ``end_shape()`` stops recording. The value of the ``kind`` parameter tells it
        which types of shapes to create from the provided vertices. With no mode
        specified, the shape can be any irregular polygon. The parameters available for
        ``begin_shape()`` are POINTS, LINES, TRIANGLES, TRIANGLE_FAN, TRIANGLE_STRIP,
        QUADS, and QUAD_STRIP. After calling the ``begin_shape()`` function, a series of
        ``vertex()`` commands must follow. To stop drawing the shape, call
        ``end_shape()``. The ``vertex()`` function with two parameters specifies a
        position in 2D and the ``vertex()`` function with three parameters specifies a
        position in 3D. Each shape will be outlined with the current stroke color and
        filled with the fill color.

        Transformations such as ``translate()``, ``rotate()``, and ``scale()`` do not
        work within ``begin_shape()``. It is also not possible to use other shapes, such
        as ``ellipse()`` or ``rect()`` within ``begin_shape()``.

        The P2D and P3D renderers allow ``stroke()`` and ``fill()`` to be altered on a
        per-vertex basis, but the default renderer does not. Settings such as
        ``stroke_weight()``, ``stroke_cap()``, and ``stroke_join()`` cannot be changed
        while inside a ``begin_shape()``/``end_shape()`` block with any renderer.
        """
        return self._instance.beginShape(*args)

    @overload
    def bezier(self, x1: float, y1: float, x2: float, y2: float,
               x3: float, y3: float, x4: float, y4: float, /) -> None:
        """Draws a Bezier curve on the screen.

        Underlying Java method: PApplet.bezier

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

        Draws a Bezier curve on the screen. These curves are defined by a series of
        anchor and control points. The first two parameters specify the first anchor
        point and the last two parameters specify the other anchor point. The middle
        parameters specify the control points which define the shape of the curve.
        Bezier curves were developed by French engineer Pierre Bezier. Using the 3D
        version requires rendering with P3D (see the Environment reference for more
        information).
        """
        pass

    @overload
    def bezier(self, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float,
               x3: float, y3: float, z3: float, x4: float, y4: float, z4: float, /) -> None:
        """Draws a Bezier curve on the screen.

        Underlying Java method: PApplet.bezier

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

        Draws a Bezier curve on the screen. These curves are defined by a series of
        anchor and control points. The first two parameters specify the first anchor
        point and the last two parameters specify the other anchor point. The middle
        parameters specify the control points which define the shape of the curve.
        Bezier curves were developed by French engineer Pierre Bezier. Using the 3D
        version requires rendering with P3D (see the Environment reference for more
        information).
        """
        pass

    def bezier(self, *args):
        """Draws a Bezier curve on the screen.

        Underlying Java method: PApplet.bezier

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

        Draws a Bezier curve on the screen. These curves are defined by a series of
        anchor and control points. The first two parameters specify the first anchor
        point and the last two parameters specify the other anchor point. The middle
        parameters specify the control points which define the shape of the curve.
        Bezier curves were developed by French engineer Pierre Bezier. Using the 3D
        version requires rendering with P3D (see the Environment reference for more
        information).
        """
        return self._instance.bezier(*args)

    def bezier_detail(self, detail: int, /) -> None:
        """Sets the resolution at which Beziers display.

        Underlying Java method: PApplet.bezierDetail

        Parameters
        ----------

        detail: int
            resolution of the curves

        Notes
        -----

        Sets the resolution at which Beziers display. The default value is 20. This
        function is only useful when using the ``P3D`` renderer; the default ``P2D``
        renderer does not use this information.
        """
        return self._instance.bezierDetail(detail)

    def bezier_point(self, a: float, b: float, c: float,
                     d: float, t: float, /) -> float:
        """Evaluates the Bezier at point t for points a, b, c, d.

        Underlying Java method: PApplet.bezierPoint

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
        """
        return self._instance.bezierPoint(a, b, c, d, t)

    def bezier_tangent(self, a: float, b: float, c: float,
                       d: float, t: float, /) -> float:
        """Calculates the tangent of a point on a Bezier curve.

        Underlying Java method: PApplet.bezierTangent

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
        """
        return self._instance.bezierTangent(a, b, c, d, t)

    @overload
    def bezier_vertex(self, x2: float, y2: float, x3: float,
                      y3: float, x4: float, y4: float, /) -> None:
        """Specifies vertex coordinates for Bezier curves.

        Underlying Java method: PApplet.bezierVertex

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
        ``bezier_vertex()`` is used within a ``begin_shape()`` call, it must be prefaced
        with a call to ``vertex()`` to set the first anchor point. This function must be
        used between ``begin_shape()`` and ``end_shape()`` and only when there is no
        MODE parameter specified to ``begin_shape()``. Using the 3D version requires
        rendering with P3D (see the Environment reference for more information).
        """
        pass

    @overload
    def bezier_vertex(self, x2: float, y2: float, z2: float, x3: float,
                      y3: float, z3: float, x4: float, y4: float, z4: float, /) -> None:
        """Specifies vertex coordinates for Bezier curves.

        Underlying Java method: PApplet.bezierVertex

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
        ``bezier_vertex()`` is used within a ``begin_shape()`` call, it must be prefaced
        with a call to ``vertex()`` to set the first anchor point. This function must be
        used between ``begin_shape()`` and ``end_shape()`` and only when there is no
        MODE parameter specified to ``begin_shape()``. Using the 3D version requires
        rendering with P3D (see the Environment reference for more information).
        """
        pass

    def bezier_vertex(self, *args):
        """Specifies vertex coordinates for Bezier curves.

        Underlying Java method: PApplet.bezierVertex

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
        ``bezier_vertex()`` is used within a ``begin_shape()`` call, it must be prefaced
        with a call to ``vertex()`` to set the first anchor point. This function must be
        used between ``begin_shape()`` and ``end_shape()`` and only when there is no
        MODE parameter specified to ``begin_shape()``. Using the 3D version requires
        rendering with P3D (see the Environment reference for more information).
        """
        return self._instance.bezierVertex(*args)

    @overload
    def blend(self, sx: int, sy: int, sw: int, sh: int, dx: int,
              dy: int, dw: int, dh: int, mode: int, /) -> None:
        """Blends a region of pixels from one image into another (or in itself again) with
        full alpha channel support.

        Underlying Java method: PApplet.blend

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
            X coordinate of the destinations's upper left corner

        dy: int
            Y coordinate of the destinations's upper left corner

        mode: int
            Either BLEND, ADD, SUBTRACT, LIGHTEST, DARKEST, DIFFERENCE, EXCLUSION, MULTIPLY, SCREEN, OVERLAY, HARD_LIGHT, SOFT_LIGHT, DODGE, BURN

        sh: int
            source image height

        src: Py5Image
            an image variable referring to the source image

        sw: int
            source image width

        sx: int
            X coordinate of the source's upper left corner

        sy: int
            Y coordinate of the source's upper left corner

        Notes
        -----

        Blends a region of pixels from one image into another (or in itself again) with
        full alpha channel support. There is a choice of the following modes to blend
        the source pixels (A) with the ones of pixels in the destination image (B):

        BLEND - linear interpolation of colors: C = A*factor + B

        ADD - additive blending with white clip: C = min(A*factor + B, 255)

        SUBTRACT - subtractive blending with black clip: C = max(B - A*factor, 0)

        DARKEST - only the darkest color succeeds: C = min(A*factor, B)

        LIGHTEST - only the lightest color succeeds: C = max(A*factor, B)

        DIFFERENCE - subtract colors from underlying image.

        EXCLUSION - similar to DIFFERENCE, but less extreme.

        MULTIPLY - Multiply the colors, result will always be darker.

        SCREEN - Opposite multiply, uses inverse values of the colors.

        OVERLAY - A mix of MULTIPLY and SCREEN. Multiplies dark values,
        and screens light values.

        HARD_LIGHT - SCREEN when greater than 50% gray, MULTIPLY when lower.

        SOFT_LIGHT - Mix of DARKEST and LIGHTEST.
        Works like OVERLAY, but not as harsh.

        DODGE - Lightens light tones and increases contrast, ignores darks.
        Called "Color Dodge" in Illustrator and Photoshop.

        BURN - Darker areas are applied, increasing contrast, ignores lights.
        Called "Color Burn" in Illustrator and Photoshop.

        All modes use the alpha information (highest byte) of source image pixels as the
        blending factor. If the source and destination regions are different sizes, the
        image will be automatically resized to match the destination size. If the
        ``src`` parameter is not used, the display window is used as the source image.

        As of release 0149, this function ignores ``image_mode()``.
        """
        pass

    @overload
    def blend(self, src: Py5Image, sx: int, sy: int, sw: int, sh: int,
              dx: int, dy: int, dw: int, dh: int, mode: int, /) -> None:
        """Blends a region of pixels from one image into another (or in itself again) with
        full alpha channel support.

        Underlying Java method: PApplet.blend

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
            X coordinate of the destinations's upper left corner

        dy: int
            Y coordinate of the destinations's upper left corner

        mode: int
            Either BLEND, ADD, SUBTRACT, LIGHTEST, DARKEST, DIFFERENCE, EXCLUSION, MULTIPLY, SCREEN, OVERLAY, HARD_LIGHT, SOFT_LIGHT, DODGE, BURN

        sh: int
            source image height

        src: Py5Image
            an image variable referring to the source image

        sw: int
            source image width

        sx: int
            X coordinate of the source's upper left corner

        sy: int
            Y coordinate of the source's upper left corner

        Notes
        -----

        Blends a region of pixels from one image into another (or in itself again) with
        full alpha channel support. There is a choice of the following modes to blend
        the source pixels (A) with the ones of pixels in the destination image (B):

        BLEND - linear interpolation of colors: C = A*factor + B

        ADD - additive blending with white clip: C = min(A*factor + B, 255)

        SUBTRACT - subtractive blending with black clip: C = max(B - A*factor, 0)

        DARKEST - only the darkest color succeeds: C = min(A*factor, B)

        LIGHTEST - only the lightest color succeeds: C = max(A*factor, B)

        DIFFERENCE - subtract colors from underlying image.

        EXCLUSION - similar to DIFFERENCE, but less extreme.

        MULTIPLY - Multiply the colors, result will always be darker.

        SCREEN - Opposite multiply, uses inverse values of the colors.

        OVERLAY - A mix of MULTIPLY and SCREEN. Multiplies dark values,
        and screens light values.

        HARD_LIGHT - SCREEN when greater than 50% gray, MULTIPLY when lower.

        SOFT_LIGHT - Mix of DARKEST and LIGHTEST.
        Works like OVERLAY, but not as harsh.

        DODGE - Lightens light tones and increases contrast, ignores darks.
        Called "Color Dodge" in Illustrator and Photoshop.

        BURN - Darker areas are applied, increasing contrast, ignores lights.
        Called "Color Burn" in Illustrator and Photoshop.

        All modes use the alpha information (highest byte) of source image pixels as the
        blending factor. If the source and destination regions are different sizes, the
        image will be automatically resized to match the destination size. If the
        ``src`` parameter is not used, the display window is used as the source image.

        As of release 0149, this function ignores ``image_mode()``.
        """
        pass

    def blend(self, *args):
        """Blends a region of pixels from one image into another (or in itself again) with
        full alpha channel support.

        Underlying Java method: PApplet.blend

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
            X coordinate of the destinations's upper left corner

        dy: int
            Y coordinate of the destinations's upper left corner

        mode: int
            Either BLEND, ADD, SUBTRACT, LIGHTEST, DARKEST, DIFFERENCE, EXCLUSION, MULTIPLY, SCREEN, OVERLAY, HARD_LIGHT, SOFT_LIGHT, DODGE, BURN

        sh: int
            source image height

        src: Py5Image
            an image variable referring to the source image

        sw: int
            source image width

        sx: int
            X coordinate of the source's upper left corner

        sy: int
            Y coordinate of the source's upper left corner

        Notes
        -----

        Blends a region of pixels from one image into another (or in itself again) with
        full alpha channel support. There is a choice of the following modes to blend
        the source pixels (A) with the ones of pixels in the destination image (B):

        BLEND - linear interpolation of colors: C = A*factor + B

        ADD - additive blending with white clip: C = min(A*factor + B, 255)

        SUBTRACT - subtractive blending with black clip: C = max(B - A*factor, 0)

        DARKEST - only the darkest color succeeds: C = min(A*factor, B)

        LIGHTEST - only the lightest color succeeds: C = max(A*factor, B)

        DIFFERENCE - subtract colors from underlying image.

        EXCLUSION - similar to DIFFERENCE, but less extreme.

        MULTIPLY - Multiply the colors, result will always be darker.

        SCREEN - Opposite multiply, uses inverse values of the colors.

        OVERLAY - A mix of MULTIPLY and SCREEN. Multiplies dark values,
        and screens light values.

        HARD_LIGHT - SCREEN when greater than 50% gray, MULTIPLY when lower.

        SOFT_LIGHT - Mix of DARKEST and LIGHTEST.
        Works like OVERLAY, but not as harsh.

        DODGE - Lightens light tones and increases contrast, ignores darks.
        Called "Color Dodge" in Illustrator and Photoshop.

        BURN - Darker areas are applied, increasing contrast, ignores lights.
        Called "Color Burn" in Illustrator and Photoshop.

        All modes use the alpha information (highest byte) of source image pixels as the
        blending factor. If the source and destination regions are different sizes, the
        image will be automatically resized to match the destination size. If the
        ``src`` parameter is not used, the display window is used as the source image.

        As of release 0149, this function ignores ``image_mode()``.
        """
        return self._instance.blend(*args)

    def blend_mode(self, mode: int, /) -> None:
        """Blends the pixels in the display window according to a defined mode.

        Underlying Java method: PApplet.blendMode

        Parameters
        ----------

        mode: int
            the blending mode to use

        Notes
        -----

        Blends the pixels in the display window according to a defined mode. There is a
        choice of the following modes to blend the source pixels (A) with the ones of
        pixels already in the display window (B). Each pixel's final color is the result
        of applying one of the blend modes with each channel of (A) and (B)
        independently. The red channel is compared with red, green with green, and blue
        with blue.

        BLEND - linear interpolation of colors: C = A*factor + B. This is the default.

        ADD - additive blending with white clip: C = min(A*factor + B, 255)

        SUBTRACT - subtractive blending with black clip: C = max(B - A*factor, 0)

        DARKEST - only the darkest color succeeds: C = min(A*factor, B)

        LIGHTEST - only the lightest color succeeds: C = max(A*factor, B)

        DIFFERENCE - subtract colors from underlying image.

        EXCLUSION - similar to DIFFERENCE, but less extreme.

        MULTIPLY - multiply the colors, result will always be darker.

        SCREEN - opposite multiply, uses inverse values of the colors.

        REPLACE - the pixels entirely replace the others and don't utilize alpha
        (transparency) values

        We recommend using ``blend_mode()`` and not the previous ``blend()`` function.
        However, unlike ``blend()``, the ``blend_mode()`` function does not support the
        following: HARD_LIGHT, SOFT_LIGHT, OVERLAY, DODGE, BURN. On older hardware, the
        LIGHTEST, DARKEST, and DIFFERENCE modes might not be available as well.
        """
        return self._instance.blendMode(mode)

    def blue(self, rgb: int, /) -> float:
        """Extracts the blue value from a color, scaled to match current ``color_mode()``.

        Underlying Java method: PApplet.blue

        Parameters
        ----------

        rgb: int
            any value of the color datatype

        Notes
        -----

        Extracts the blue value from a color, scaled to match current ``color_mode()``.
        The value is always returned as a float, so be careful not to assign it to an
        int value.

        The ``blue()`` function is easy to use and understand, but it is slower than a
        technique called bit masking. When working in ``color_mode(RGB, 255)``, you can
        acheive the same results as ``blue()`` but with greater speed by using a bit
        mask to remove the other color components. For example, the following two lines
        of code are equivalent means of getting the blue value of the color value ``c``:

        ``b1 = blue(c)   # simpler, but slower to calculate
        b2 = c & 0xFF  # very fast to calculate``
        """
        return self._instance.blue(rgb)

    @overload
    def box(self, size: float, /) -> None:
        """A box is an extruded rectangle.

        Underlying Java method: PApplet.box

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
        """
        pass

    @overload
    def box(self, w: float, h: float, d: float, /) -> None:
        """A box is an extruded rectangle.

        Underlying Java method: PApplet.box

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
        """
        pass

    def box(self, *args):
        """A box is an extruded rectangle.

        Underlying Java method: PApplet.box

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
        """
        return self._instance.box(*args)

    def brightness(self, rgb: int, /) -> float:
        """Extracts the brightness value from a color.

        Underlying Java method: PApplet.brightness

        Parameters
        ----------

        rgb: int
            any value of the color datatype

        Notes
        -----

        Extracts the brightness value from a color.
        """
        return self._instance.brightness(rgb)

    @overload
    def camera(self) -> None:
        """Sets the position of the camera through setting the eye position, the center of
        the scene, and which axis is facing upward.

        Underlying Java method: PApplet.camera

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
        default position, pointing to the center of the display window with the Y axis
        as up. The default values are ``camera(width//2.0, height//2.0, (height//2.0) /
        tan(PI*30.0 / 180.0), width//2.0, height//2.0, 0, 0, 1, 0)``. This function is
        similar to ``glu_look_at()`` in OpenGL, but it first clears the current camera
        settings.
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

        Underlying Java method: PApplet.camera

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
        default position, pointing to the center of the display window with the Y axis
        as up. The default values are ``camera(width//2.0, height//2.0, (height//2.0) /
        tan(PI*30.0 / 180.0), width//2.0, height//2.0, 0, 0, 1, 0)``. This function is
        similar to ``glu_look_at()`` in OpenGL, but it first clears the current camera
        settings.
        """
        pass

    def camera(self, *args):
        """Sets the position of the camera through setting the eye position, the center of
        the scene, and which axis is facing upward.

        Underlying Java method: PApplet.camera

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
        default position, pointing to the center of the display window with the Y axis
        as up. The default values are ``camera(width//2.0, height//2.0, (height//2.0) /
        tan(PI*30.0 / 180.0), width//2.0, height//2.0, 0, 0, 1, 0)``. This function is
        similar to ``glu_look_at()`` in OpenGL, but it first clears the current camera
        settings.
        """
        return self._instance.camera(*args)

    def circle(self, x: float, y: float, extent: float, /) -> None:
        """Draws a circle to the screen.

        Underlying Java method: PApplet.circle

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
        origin may be changed with the ``ellipse_mode()`` function.
        """
        return self._instance.circle(x, y, extent)

    def clear(self) -> None:
        """Clears the pixels within a buffer.

        Underlying Java method: PApplet.clear

        Notes
        -----

        Clears the pixels within a buffer. This function only works on ``Py5Graphics``
        objects created with the ``create_graphics()`` function. Unlike the main
        graphics context (the display window), pixels in additional graphics areas
        created with ``create_graphics()`` can be entirely or partially transparent.
        This function clears everything in a ``Py5Graphics`` object to make all of the
        pixels 100% transparent.
        """
        return self._instance.clear()

    def clip(self, a: float, b: float, c: float, d: float, /) -> None:
        """Limits the rendering to the boundaries of a rectangle defined by the parameters.

        Underlying Java method: PApplet.clip

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
        The boundaries are drawn based on the state of the ``image_mode()`` fuction,
        either CORNER, CORNERS, or CENTER.
        """
        return self._instance.clip(a, b, c, d)

    @overload
    def color(self, gray: float, /) -> int:
        """Creates colors for storing in variables of the ``color`` datatype.

        Underlying Java method: PApplet.color

        Methods
        -------

        You can use any of the following signatures:

         * color(fgray: float, /) -> int
         * color(fgray: float, falpha: float, /) -> int
         * color(gray: int, /) -> int
         * color(gray: int, alpha: int, /) -> int
         * color(v1: float, v2: float, v3: float, /) -> int
         * color(v1: float, v2: float, v3: float, alpha: float, /) -> int
         * color(v1: int, v2: int, v3: int, /) -> int
         * color(v1: int, v2: int, v3: int, alpha: int, /) -> int

        Parameters
        ----------

        alpha: float
            relative to current color range

        alpha: int
            relative to current color range

        falpha: float
            missing variable description

        fgray: float
            number specifying value between white and black

        gray: int
            number specifying value between white and black

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

        Creates colors for storing in variables of the ``color`` datatype. The
        parameters are interpreted as RGB or HSB values depending on the current
        ``color_mode()``. The default mode is RGB values from 0 to 255 and, therefore,
        ``color(255, 204, 0)`` will return a bright yellow color (see the first example
        above).

        Note that if only one value is provided to ``color()``, it will be interpreted
        as a grayscale value. Add a second value, and it will be used for alpha
        transparency. When three values are specified, they are interpreted as either
        RGB or HSB values. Adding a fourth value applies alpha transparency.

        Note that when using hexadecimal notation, it is not necessary to use
        ``color()``, as in: ``c = 0x006699``

        More about how colors are stored can be found in the reference for the color
        datatype.
        """
        pass

    @overload
    def color(self, gray: float, alpha: float, /) -> int:
        """Creates colors for storing in variables of the ``color`` datatype.

        Underlying Java method: PApplet.color

        Methods
        -------

        You can use any of the following signatures:

         * color(fgray: float, /) -> int
         * color(fgray: float, falpha: float, /) -> int
         * color(gray: int, /) -> int
         * color(gray: int, alpha: int, /) -> int
         * color(v1: float, v2: float, v3: float, /) -> int
         * color(v1: float, v2: float, v3: float, alpha: float, /) -> int
         * color(v1: int, v2: int, v3: int, /) -> int
         * color(v1: int, v2: int, v3: int, alpha: int, /) -> int

        Parameters
        ----------

        alpha: float
            relative to current color range

        alpha: int
            relative to current color range

        falpha: float
            missing variable description

        fgray: float
            number specifying value between white and black

        gray: int
            number specifying value between white and black

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

        Creates colors for storing in variables of the ``color`` datatype. The
        parameters are interpreted as RGB or HSB values depending on the current
        ``color_mode()``. The default mode is RGB values from 0 to 255 and, therefore,
        ``color(255, 204, 0)`` will return a bright yellow color (see the first example
        above).

        Note that if only one value is provided to ``color()``, it will be interpreted
        as a grayscale value. Add a second value, and it will be used for alpha
        transparency. When three values are specified, they are interpreted as either
        RGB or HSB values. Adding a fourth value applies alpha transparency.

        Note that when using hexadecimal notation, it is not necessary to use
        ``color()``, as in: ``c = 0x006699``

        More about how colors are stored can be found in the reference for the color
        datatype.
        """
        pass

    @overload
    def color(self, v1: float, v2: float, v3: float, /) -> int:
        """Creates colors for storing in variables of the ``color`` datatype.

        Underlying Java method: PApplet.color

        Methods
        -------

        You can use any of the following signatures:

         * color(fgray: float, /) -> int
         * color(fgray: float, falpha: float, /) -> int
         * color(gray: int, /) -> int
         * color(gray: int, alpha: int, /) -> int
         * color(v1: float, v2: float, v3: float, /) -> int
         * color(v1: float, v2: float, v3: float, alpha: float, /) -> int
         * color(v1: int, v2: int, v3: int, /) -> int
         * color(v1: int, v2: int, v3: int, alpha: int, /) -> int

        Parameters
        ----------

        alpha: float
            relative to current color range

        alpha: int
            relative to current color range

        falpha: float
            missing variable description

        fgray: float
            number specifying value between white and black

        gray: int
            number specifying value between white and black

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

        Creates colors for storing in variables of the ``color`` datatype. The
        parameters are interpreted as RGB or HSB values depending on the current
        ``color_mode()``. The default mode is RGB values from 0 to 255 and, therefore,
        ``color(255, 204, 0)`` will return a bright yellow color (see the first example
        above).

        Note that if only one value is provided to ``color()``, it will be interpreted
        as a grayscale value. Add a second value, and it will be used for alpha
        transparency. When three values are specified, they are interpreted as either
        RGB or HSB values. Adding a fourth value applies alpha transparency.

        Note that when using hexadecimal notation, it is not necessary to use
        ``color()``, as in: ``c = 0x006699``

        More about how colors are stored can be found in the reference for the color
        datatype.
        """
        pass

    @overload
    def color(self, v1: float, v2: float, v3: float, a: float, /) -> int:
        """Creates colors for storing in variables of the ``color`` datatype.

        Underlying Java method: PApplet.color

        Methods
        -------

        You can use any of the following signatures:

         * color(fgray: float, /) -> int
         * color(fgray: float, falpha: float, /) -> int
         * color(gray: int, /) -> int
         * color(gray: int, alpha: int, /) -> int
         * color(v1: float, v2: float, v3: float, /) -> int
         * color(v1: float, v2: float, v3: float, alpha: float, /) -> int
         * color(v1: int, v2: int, v3: int, /) -> int
         * color(v1: int, v2: int, v3: int, alpha: int, /) -> int

        Parameters
        ----------

        alpha: float
            relative to current color range

        alpha: int
            relative to current color range

        falpha: float
            missing variable description

        fgray: float
            number specifying value between white and black

        gray: int
            number specifying value between white and black

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

        Creates colors for storing in variables of the ``color`` datatype. The
        parameters are interpreted as RGB or HSB values depending on the current
        ``color_mode()``. The default mode is RGB values from 0 to 255 and, therefore,
        ``color(255, 204, 0)`` will return a bright yellow color (see the first example
        above).

        Note that if only one value is provided to ``color()``, it will be interpreted
        as a grayscale value. Add a second value, and it will be used for alpha
        transparency. When three values are specified, they are interpreted as either
        RGB or HSB values. Adding a fourth value applies alpha transparency.

        Note that when using hexadecimal notation, it is not necessary to use
        ``color()``, as in: ``c = 0x006699``

        More about how colors are stored can be found in the reference for the color
        datatype.
        """
        pass

    @overload
    def color(self, c: int, /) -> int:
        """Creates colors for storing in variables of the ``color`` datatype.

        Underlying Java method: PApplet.color

        Methods
        -------

        You can use any of the following signatures:

         * color(fgray: float, /) -> int
         * color(fgray: float, falpha: float, /) -> int
         * color(gray: int, /) -> int
         * color(gray: int, alpha: int, /) -> int
         * color(v1: float, v2: float, v3: float, /) -> int
         * color(v1: float, v2: float, v3: float, alpha: float, /) -> int
         * color(v1: int, v2: int, v3: int, /) -> int
         * color(v1: int, v2: int, v3: int, alpha: int, /) -> int

        Parameters
        ----------

        alpha: float
            relative to current color range

        alpha: int
            relative to current color range

        falpha: float
            missing variable description

        fgray: float
            number specifying value between white and black

        gray: int
            number specifying value between white and black

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

        Creates colors for storing in variables of the ``color`` datatype. The
        parameters are interpreted as RGB or HSB values depending on the current
        ``color_mode()``. The default mode is RGB values from 0 to 255 and, therefore,
        ``color(255, 204, 0)`` will return a bright yellow color (see the first example
        above).

        Note that if only one value is provided to ``color()``, it will be interpreted
        as a grayscale value. Add a second value, and it will be used for alpha
        transparency. When three values are specified, they are interpreted as either
        RGB or HSB values. Adding a fourth value applies alpha transparency.

        Note that when using hexadecimal notation, it is not necessary to use
        ``color()``, as in: ``c = 0x006699``

        More about how colors are stored can be found in the reference for the color
        datatype.
        """
        pass

    @overload
    def color(self, c: int, alpha: float, /) -> int:
        """Creates colors for storing in variables of the ``color`` datatype.

        Underlying Java method: PApplet.color

        Methods
        -------

        You can use any of the following signatures:

         * color(fgray: float, /) -> int
         * color(fgray: float, falpha: float, /) -> int
         * color(gray: int, /) -> int
         * color(gray: int, alpha: int, /) -> int
         * color(v1: float, v2: float, v3: float, /) -> int
         * color(v1: float, v2: float, v3: float, alpha: float, /) -> int
         * color(v1: int, v2: int, v3: int, /) -> int
         * color(v1: int, v2: int, v3: int, alpha: int, /) -> int

        Parameters
        ----------

        alpha: float
            relative to current color range

        alpha: int
            relative to current color range

        falpha: float
            missing variable description

        fgray: float
            number specifying value between white and black

        gray: int
            number specifying value between white and black

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

        Creates colors for storing in variables of the ``color`` datatype. The
        parameters are interpreted as RGB or HSB values depending on the current
        ``color_mode()``. The default mode is RGB values from 0 to 255 and, therefore,
        ``color(255, 204, 0)`` will return a bright yellow color (see the first example
        above).

        Note that if only one value is provided to ``color()``, it will be interpreted
        as a grayscale value. Add a second value, and it will be used for alpha
        transparency. When three values are specified, they are interpreted as either
        RGB or HSB values. Adding a fourth value applies alpha transparency.

        Note that when using hexadecimal notation, it is not necessary to use
        ``color()``, as in: ``c = 0x006699``

        More about how colors are stored can be found in the reference for the color
        datatype.
        """
        pass

    @overload
    def color(self, c: int, alpha: int, /) -> int:
        """Creates colors for storing in variables of the ``color`` datatype.

        Underlying Java method: PApplet.color

        Methods
        -------

        You can use any of the following signatures:

         * color(fgray: float, /) -> int
         * color(fgray: float, falpha: float, /) -> int
         * color(gray: int, /) -> int
         * color(gray: int, alpha: int, /) -> int
         * color(v1: float, v2: float, v3: float, /) -> int
         * color(v1: float, v2: float, v3: float, alpha: float, /) -> int
         * color(v1: int, v2: int, v3: int, /) -> int
         * color(v1: int, v2: int, v3: int, alpha: int, /) -> int

        Parameters
        ----------

        alpha: float
            relative to current color range

        alpha: int
            relative to current color range

        falpha: float
            missing variable description

        fgray: float
            number specifying value between white and black

        gray: int
            number specifying value between white and black

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

        Creates colors for storing in variables of the ``color`` datatype. The
        parameters are interpreted as RGB or HSB values depending on the current
        ``color_mode()``. The default mode is RGB values from 0 to 255 and, therefore,
        ``color(255, 204, 0)`` will return a bright yellow color (see the first example
        above).

        Note that if only one value is provided to ``color()``, it will be interpreted
        as a grayscale value. Add a second value, and it will be used for alpha
        transparency. When three values are specified, they are interpreted as either
        RGB or HSB values. Adding a fourth value applies alpha transparency.

        Note that when using hexadecimal notation, it is not necessary to use
        ``color()``, as in: ``c = 0x006699``

        More about how colors are stored can be found in the reference for the color
        datatype.
        """
        pass

    @overload
    def color(self, v1: int, v2: int, v3: int, /) -> int:
        """Creates colors for storing in variables of the ``color`` datatype.

        Underlying Java method: PApplet.color

        Methods
        -------

        You can use any of the following signatures:

         * color(fgray: float, /) -> int
         * color(fgray: float, falpha: float, /) -> int
         * color(gray: int, /) -> int
         * color(gray: int, alpha: int, /) -> int
         * color(v1: float, v2: float, v3: float, /) -> int
         * color(v1: float, v2: float, v3: float, alpha: float, /) -> int
         * color(v1: int, v2: int, v3: int, /) -> int
         * color(v1: int, v2: int, v3: int, alpha: int, /) -> int

        Parameters
        ----------

        alpha: float
            relative to current color range

        alpha: int
            relative to current color range

        falpha: float
            missing variable description

        fgray: float
            number specifying value between white and black

        gray: int
            number specifying value between white and black

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

        Creates colors for storing in variables of the ``color`` datatype. The
        parameters are interpreted as RGB or HSB values depending on the current
        ``color_mode()``. The default mode is RGB values from 0 to 255 and, therefore,
        ``color(255, 204, 0)`` will return a bright yellow color (see the first example
        above).

        Note that if only one value is provided to ``color()``, it will be interpreted
        as a grayscale value. Add a second value, and it will be used for alpha
        transparency. When three values are specified, they are interpreted as either
        RGB or HSB values. Adding a fourth value applies alpha transparency.

        Note that when using hexadecimal notation, it is not necessary to use
        ``color()``, as in: ``c = 0x006699``

        More about how colors are stored can be found in the reference for the color
        datatype.
        """
        pass

    @overload
    def color(self, v1: int, v2: int, v3: int, a: int, /) -> int:
        """Creates colors for storing in variables of the ``color`` datatype.

        Underlying Java method: PApplet.color

        Methods
        -------

        You can use any of the following signatures:

         * color(fgray: float, /) -> int
         * color(fgray: float, falpha: float, /) -> int
         * color(gray: int, /) -> int
         * color(gray: int, alpha: int, /) -> int
         * color(v1: float, v2: float, v3: float, /) -> int
         * color(v1: float, v2: float, v3: float, alpha: float, /) -> int
         * color(v1: int, v2: int, v3: int, /) -> int
         * color(v1: int, v2: int, v3: int, alpha: int, /) -> int

        Parameters
        ----------

        alpha: float
            relative to current color range

        alpha: int
            relative to current color range

        falpha: float
            missing variable description

        fgray: float
            number specifying value between white and black

        gray: int
            number specifying value between white and black

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

        Creates colors for storing in variables of the ``color`` datatype. The
        parameters are interpreted as RGB or HSB values depending on the current
        ``color_mode()``. The default mode is RGB values from 0 to 255 and, therefore,
        ``color(255, 204, 0)`` will return a bright yellow color (see the first example
        above).

        Note that if only one value is provided to ``color()``, it will be interpreted
        as a grayscale value. Add a second value, and it will be used for alpha
        transparency. When three values are specified, they are interpreted as either
        RGB or HSB values. Adding a fourth value applies alpha transparency.

        Note that when using hexadecimal notation, it is not necessary to use
        ``color()``, as in: ``c = 0x006699``

        More about how colors are stored can be found in the reference for the color
        datatype.
        """
        pass

    def color(self, *args):
        """Creates colors for storing in variables of the ``color`` datatype.

        Underlying Java method: PApplet.color

        Methods
        -------

        You can use any of the following signatures:

         * color(fgray: float, /) -> int
         * color(fgray: float, falpha: float, /) -> int
         * color(gray: int, /) -> int
         * color(gray: int, alpha: int, /) -> int
         * color(v1: float, v2: float, v3: float, /) -> int
         * color(v1: float, v2: float, v3: float, alpha: float, /) -> int
         * color(v1: int, v2: int, v3: int, /) -> int
         * color(v1: int, v2: int, v3: int, alpha: int, /) -> int

        Parameters
        ----------

        alpha: float
            relative to current color range

        alpha: int
            relative to current color range

        falpha: float
            missing variable description

        fgray: float
            number specifying value between white and black

        gray: int
            number specifying value between white and black

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

        Creates colors for storing in variables of the ``color`` datatype. The
        parameters are interpreted as RGB or HSB values depending on the current
        ``color_mode()``. The default mode is RGB values from 0 to 255 and, therefore,
        ``color(255, 204, 0)`` will return a bright yellow color (see the first example
        above).

        Note that if only one value is provided to ``color()``, it will be interpreted
        as a grayscale value. Add a second value, and it will be used for alpha
        transparency. When three values are specified, they are interpreted as either
        RGB or HSB values. Adding a fourth value applies alpha transparency.

        Note that when using hexadecimal notation, it is not necessary to use
        ``color()``, as in: ``c = 0x006699``

        More about how colors are stored can be found in the reference for the color
        datatype.
        """
        return self._instance.color(*args)

    @overload
    def color_mode(self, mode: int, /) -> None:
        """Changes the way Processing interprets color data.

        Underlying Java method: PApplet.colorMode

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

        Changes the way Processing interprets color data. By default, the parameters for
        ``fill()``, ``stroke()``, ``background()``, and ``color()`` are defined by
        values between 0 and 255 using the RGB color model. The ``color_mode()``
        function is used to change the numerical range used for specifying colors and to
        switch color systems. For example, calling ``color_mode(RGB, 1.0)`` will specify
        that values are specified between 0 and 1. The limits for defining colors are
        altered by setting the parameters ``max``, ``max1``, ``max2``, ``max3``, and
        ``max_a``.

        After changing the range of values for colors with code like ``color_mode(HSB,
        360, 100, 100)``, those ranges remain in use until they are explicitly changed
        again. For example, after running ``color_mode(HSB, 360, 100, 100)`` and then
        changing back to ``color_mode(RGB)``, the range for R will be 0 to 360 and the
        range for G and B will be 0 to 100. To avoid this, be explicit about the ranges
        when changing the color mode. For instance, instead of ``color_mode(RGB)``,
        write ``color_mode(RGB, 255, 255, 255)``.
        """
        pass

    @overload
    def color_mode(self, mode: int, max: float, /) -> None:
        """Changes the way Processing interprets color data.

        Underlying Java method: PApplet.colorMode

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

        Changes the way Processing interprets color data. By default, the parameters for
        ``fill()``, ``stroke()``, ``background()``, and ``color()`` are defined by
        values between 0 and 255 using the RGB color model. The ``color_mode()``
        function is used to change the numerical range used for specifying colors and to
        switch color systems. For example, calling ``color_mode(RGB, 1.0)`` will specify
        that values are specified between 0 and 1. The limits for defining colors are
        altered by setting the parameters ``max``, ``max1``, ``max2``, ``max3``, and
        ``max_a``.

        After changing the range of values for colors with code like ``color_mode(HSB,
        360, 100, 100)``, those ranges remain in use until they are explicitly changed
        again. For example, after running ``color_mode(HSB, 360, 100, 100)`` and then
        changing back to ``color_mode(RGB)``, the range for R will be 0 to 360 and the
        range for G and B will be 0 to 100. To avoid this, be explicit about the ranges
        when changing the color mode. For instance, instead of ``color_mode(RGB)``,
        write ``color_mode(RGB, 255, 255, 255)``.
        """
        pass

    @overload
    def color_mode(self, mode: int, max1: float,
                   max2: float, max3: float, /) -> None:
        """Changes the way Processing interprets color data.

        Underlying Java method: PApplet.colorMode

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

        Changes the way Processing interprets color data. By default, the parameters for
        ``fill()``, ``stroke()``, ``background()``, and ``color()`` are defined by
        values between 0 and 255 using the RGB color model. The ``color_mode()``
        function is used to change the numerical range used for specifying colors and to
        switch color systems. For example, calling ``color_mode(RGB, 1.0)`` will specify
        that values are specified between 0 and 1. The limits for defining colors are
        altered by setting the parameters ``max``, ``max1``, ``max2``, ``max3``, and
        ``max_a``.

        After changing the range of values for colors with code like ``color_mode(HSB,
        360, 100, 100)``, those ranges remain in use until they are explicitly changed
        again. For example, after running ``color_mode(HSB, 360, 100, 100)`` and then
        changing back to ``color_mode(RGB)``, the range for R will be 0 to 360 and the
        range for G and B will be 0 to 100. To avoid this, be explicit about the ranges
        when changing the color mode. For instance, instead of ``color_mode(RGB)``,
        write ``color_mode(RGB, 255, 255, 255)``.
        """
        pass

    @overload
    def color_mode(self, mode: int, max1: float, max2: float,
                   max3: float, max_a: float, /) -> None:
        """Changes the way Processing interprets color data.

        Underlying Java method: PApplet.colorMode

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

        Changes the way Processing interprets color data. By default, the parameters for
        ``fill()``, ``stroke()``, ``background()``, and ``color()`` are defined by
        values between 0 and 255 using the RGB color model. The ``color_mode()``
        function is used to change the numerical range used for specifying colors and to
        switch color systems. For example, calling ``color_mode(RGB, 1.0)`` will specify
        that values are specified between 0 and 1. The limits for defining colors are
        altered by setting the parameters ``max``, ``max1``, ``max2``, ``max3``, and
        ``max_a``.

        After changing the range of values for colors with code like ``color_mode(HSB,
        360, 100, 100)``, those ranges remain in use until they are explicitly changed
        again. For example, after running ``color_mode(HSB, 360, 100, 100)`` and then
        changing back to ``color_mode(RGB)``, the range for R will be 0 to 360 and the
        range for G and B will be 0 to 100. To avoid this, be explicit about the ranges
        when changing the color mode. For instance, instead of ``color_mode(RGB)``,
        write ``color_mode(RGB, 255, 255, 255)``.
        """
        pass

    def color_mode(self, *args):
        """Changes the way Processing interprets color data.

        Underlying Java method: PApplet.colorMode

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

        Changes the way Processing interprets color data. By default, the parameters for
        ``fill()``, ``stroke()``, ``background()``, and ``color()`` are defined by
        values between 0 and 255 using the RGB color model. The ``color_mode()``
        function is used to change the numerical range used for specifying colors and to
        switch color systems. For example, calling ``color_mode(RGB, 1.0)`` will specify
        that values are specified between 0 and 1. The limits for defining colors are
        altered by setting the parameters ``max``, ``max1``, ``max2``, ``max3``, and
        ``max_a``.

        After changing the range of values for colors with code like ``color_mode(HSB,
        360, 100, 100)``, those ranges remain in use until they are explicitly changed
        again. For example, after running ``color_mode(HSB, 360, 100, 100)`` and then
        changing back to ``color_mode(RGB)``, the range for R will be 0 to 360 and the
        range for G and B will be 0 to 100. To avoid this, be explicit about the ranges
        when changing the color mode. For instance, instead of ``color_mode(RGB)``,
        write ``color_mode(RGB, 255, 255, 255)``.
        """
        return self._instance.colorMode(*args)

    @overload
    def copy(self) -> Py5Image:
        """Copies a region of pixels from the display window to another area of the display
        window and copies a region of pixels from an image used as the ``src_img``
        parameter into the display window.

        Underlying Java method: PApplet.copy

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
            X coordinate of the destination's upper left corner

        dy: int
            Y coordinate of the destination's upper left corner

        sh: int
            source image height

        src: Py5Image
            an image variable referring to the source image.

        sw: int
            source image width

        sx: int
            X coordinate of the source's upper left corner

        sy: int
            Y coordinate of the source's upper left corner

        Notes
        -----

        Copies a region of pixels from the display window to another area of the display
        window and copies a region of pixels from an image used as the ``src_img``
        parameter into the display window. If the source and destination regions aren't
        the same size, it will automatically resize the source pixels to fit the
        specified target region. No alpha information is used in the process, however if
        the source image has an alpha channel set, it will be copied as well.

        As of release 0149, this function ignores ``image_mode()``.
        """
        pass

    @overload
    def copy(self, sx: int, sy: int, sw: int, sh: int,
             dx: int, dy: int, dw: int, dh: int, /) -> None:
        """Copies a region of pixels from the display window to another area of the display
        window and copies a region of pixels from an image used as the ``src_img``
        parameter into the display window.

        Underlying Java method: PApplet.copy

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
            X coordinate of the destination's upper left corner

        dy: int
            Y coordinate of the destination's upper left corner

        sh: int
            source image height

        src: Py5Image
            an image variable referring to the source image.

        sw: int
            source image width

        sx: int
            X coordinate of the source's upper left corner

        sy: int
            Y coordinate of the source's upper left corner

        Notes
        -----

        Copies a region of pixels from the display window to another area of the display
        window and copies a region of pixels from an image used as the ``src_img``
        parameter into the display window. If the source and destination regions aren't
        the same size, it will automatically resize the source pixels to fit the
        specified target region. No alpha information is used in the process, however if
        the source image has an alpha channel set, it will be copied as well.

        As of release 0149, this function ignores ``image_mode()``.
        """
        pass

    @overload
    def copy(self, src: Py5Image, sx: int, sy: int, sw: int,
             sh: int, dx: int, dy: int, dw: int, dh: int, /) -> None:
        """Copies a region of pixels from the display window to another area of the display
        window and copies a region of pixels from an image used as the ``src_img``
        parameter into the display window.

        Underlying Java method: PApplet.copy

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
            X coordinate of the destination's upper left corner

        dy: int
            Y coordinate of the destination's upper left corner

        sh: int
            source image height

        src: Py5Image
            an image variable referring to the source image.

        sw: int
            source image width

        sx: int
            X coordinate of the source's upper left corner

        sy: int
            Y coordinate of the source's upper left corner

        Notes
        -----

        Copies a region of pixels from the display window to another area of the display
        window and copies a region of pixels from an image used as the ``src_img``
        parameter into the display window. If the source and destination regions aren't
        the same size, it will automatically resize the source pixels to fit the
        specified target region. No alpha information is used in the process, however if
        the source image has an alpha channel set, it will be copied as well.

        As of release 0149, this function ignores ``image_mode()``.
        """
        pass

    @_return_py5image
    def copy(self, *args):
        """Copies a region of pixels from the display window to another area of the display
        window and copies a region of pixels from an image used as the ``src_img``
        parameter into the display window.

        Underlying Java method: PApplet.copy

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
            X coordinate of the destination's upper left corner

        dy: int
            Y coordinate of the destination's upper left corner

        sh: int
            source image height

        src: Py5Image
            an image variable referring to the source image.

        sw: int
            source image width

        sx: int
            X coordinate of the source's upper left corner

        sy: int
            Y coordinate of the source's upper left corner

        Notes
        -----

        Copies a region of pixels from the display window to another area of the display
        window and copies a region of pixels from an image used as the ``src_img``
        parameter into the display window. If the source and destination regions aren't
        the same size, it will automatically resize the source pixels to fit the
        specified target region. No alpha information is used in the process, however if
        the source image has an alpha channel set, it will be copied as well.

        As of release 0149, this function ignores ``image_mode()``.
        """
        return self._instance.copy(*args)

    @overload
    def create_shape(self) -> Py5Shape:
        """The ``create_shape()`` function is used to define a new shape.

        Underlying Java method: PApplet.createShape

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
            missing variable description

        Notes
        -----

        The ``create_shape()`` function is used to define a new shape. Once created,
        this shape can be drawn with the ``shape()`` function. The basic way to use the
        function defines new primitive shapes. One of the following parameters are used
        as the first parameter: ``ELLIPSE``, ``RECT``, ``ARC``, ``TRIANGLE``,
        ``SPHERE``, ``BOX``, ``QUAD``, or ``LINE``. The parameters for each of these
        different shapes are the same as their corresponding functions: ``ellipse()``,
        ``rect()``, ``arc()``, ``triangle()``, ``sphere()``, ``box()``, ``quad()``, and
        ``line()``. The first example above clarifies how this works.

        Custom, unique shapes can be made by using ``create_shape()`` without a
        parameter. After the shape is started, the drawing attributes and geometry can
        be set directly to the shape within the ``begin_shape()`` and ``end_shape()``
        methods. See the second example above for specifics, and the reference for
        ``begin_shape()`` for all of its options.

        The  ``create_shape()`` function can also be used to make a complex shape made
        of other shapes. This is called a "group" and it's created by using the
        parameter ``GROUP`` as the first parameter. See the fourth example above to see
        how it works.

        After using ``create_shape()``, stroke and fill color can be set by calling
        methods like ``set_fill()`` and ``set_stroke()``, as seen in the examples above.
        The complete list of methods and fields for the PShape class are in the
        Processing Javadoc.
        """
        pass

    @overload
    def create_shape(self, type: int, /) -> Py5Shape:
        """The ``create_shape()`` function is used to define a new shape.

        Underlying Java method: PApplet.createShape

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
            missing variable description

        Notes
        -----

        The ``create_shape()`` function is used to define a new shape. Once created,
        this shape can be drawn with the ``shape()`` function. The basic way to use the
        function defines new primitive shapes. One of the following parameters are used
        as the first parameter: ``ELLIPSE``, ``RECT``, ``ARC``, ``TRIANGLE``,
        ``SPHERE``, ``BOX``, ``QUAD``, or ``LINE``. The parameters for each of these
        different shapes are the same as their corresponding functions: ``ellipse()``,
        ``rect()``, ``arc()``, ``triangle()``, ``sphere()``, ``box()``, ``quad()``, and
        ``line()``. The first example above clarifies how this works.

        Custom, unique shapes can be made by using ``create_shape()`` without a
        parameter. After the shape is started, the drawing attributes and geometry can
        be set directly to the shape within the ``begin_shape()`` and ``end_shape()``
        methods. See the second example above for specifics, and the reference for
        ``begin_shape()`` for all of its options.

        The  ``create_shape()`` function can also be used to make a complex shape made
        of other shapes. This is called a "group" and it's created by using the
        parameter ``GROUP`` as the first parameter. See the fourth example above to see
        how it works.

        After using ``create_shape()``, stroke and fill color can be set by calling
        methods like ``set_fill()`` and ``set_stroke()``, as seen in the examples above.
        The complete list of methods and fields for the PShape class are in the
        Processing Javadoc.
        """
        pass

    @overload
    def create_shape(self, kind: int, /, *p: float) -> Py5Shape:
        """The ``create_shape()`` function is used to define a new shape.

        Underlying Java method: PApplet.createShape

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
            missing variable description

        Notes
        -----

        The ``create_shape()`` function is used to define a new shape. Once created,
        this shape can be drawn with the ``shape()`` function. The basic way to use the
        function defines new primitive shapes. One of the following parameters are used
        as the first parameter: ``ELLIPSE``, ``RECT``, ``ARC``, ``TRIANGLE``,
        ``SPHERE``, ``BOX``, ``QUAD``, or ``LINE``. The parameters for each of these
        different shapes are the same as their corresponding functions: ``ellipse()``,
        ``rect()``, ``arc()``, ``triangle()``, ``sphere()``, ``box()``, ``quad()``, and
        ``line()``. The first example above clarifies how this works.

        Custom, unique shapes can be made by using ``create_shape()`` without a
        parameter. After the shape is started, the drawing attributes and geometry can
        be set directly to the shape within the ``begin_shape()`` and ``end_shape()``
        methods. See the second example above for specifics, and the reference for
        ``begin_shape()`` for all of its options.

        The  ``create_shape()`` function can also be used to make a complex shape made
        of other shapes. This is called a "group" and it's created by using the
        parameter ``GROUP`` as the first parameter. See the fourth example above to see
        how it works.

        After using ``create_shape()``, stroke and fill color can be set by calling
        methods like ``set_fill()`` and ``set_stroke()``, as seen in the examples above.
        The complete list of methods and fields for the PShape class are in the
        Processing Javadoc.
        """
        pass

    @_return_py5shape
    def create_shape(self, *args):
        """The ``create_shape()`` function is used to define a new shape.

        Underlying Java method: PApplet.createShape

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
            missing variable description

        Notes
        -----

        The ``create_shape()`` function is used to define a new shape. Once created,
        this shape can be drawn with the ``shape()`` function. The basic way to use the
        function defines new primitive shapes. One of the following parameters are used
        as the first parameter: ``ELLIPSE``, ``RECT``, ``ARC``, ``TRIANGLE``,
        ``SPHERE``, ``BOX``, ``QUAD``, or ``LINE``. The parameters for each of these
        different shapes are the same as their corresponding functions: ``ellipse()``,
        ``rect()``, ``arc()``, ``triangle()``, ``sphere()``, ``box()``, ``quad()``, and
        ``line()``. The first example above clarifies how this works.

        Custom, unique shapes can be made by using ``create_shape()`` without a
        parameter. After the shape is started, the drawing attributes and geometry can
        be set directly to the shape within the ``begin_shape()`` and ``end_shape()``
        methods. See the second example above for specifics, and the reference for
        ``begin_shape()`` for all of its options.

        The  ``create_shape()`` function can also be used to make a complex shape made
        of other shapes. This is called a "group" and it's created by using the
        parameter ``GROUP`` as the first parameter. See the fourth example above to see
        how it works.

        After using ``create_shape()``, stroke and fill color can be set by calling
        methods like ``set_fill()`` and ``set_stroke()``, as seen in the examples above.
        The complete list of methods and fields for the PShape class are in the
        Processing Javadoc.
        """
        return self._instance.createShape(*args)

    @overload
    def curve(self, x1: float, y1: float, x2: float, y2: float,
              x3: float, y3: float, x4: float, y4: float, /) -> None:
        """Draws a curved line on the screen.

        Underlying Java method: PApplet.curve

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

        Draws a curved line on the screen. The first and second parameters specify the
        beginning control point and the last two parameters specify the ending control
        point. The middle parameters specify the start and stop of the curve. Longer
        curves can be created by putting a series of ``curve()`` functions together or
        using ``curve_vertex()``. An additional function called ``curve_tightness()``
        provides control for the visual quality of the curve. The ``curve()`` function
        is an implementation of Catmull-Rom splines. Using the 3D version requires
        rendering with P3D (see the Environment reference for more information).
        """
        pass

    @overload
    def curve(self, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float,
              x3: float, y3: float, z3: float, x4: float, y4: float, z4: float, /) -> None:
        """Draws a curved line on the screen.

        Underlying Java method: PApplet.curve

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

        Draws a curved line on the screen. The first and second parameters specify the
        beginning control point and the last two parameters specify the ending control
        point. The middle parameters specify the start and stop of the curve. Longer
        curves can be created by putting a series of ``curve()`` functions together or
        using ``curve_vertex()``. An additional function called ``curve_tightness()``
        provides control for the visual quality of the curve. The ``curve()`` function
        is an implementation of Catmull-Rom splines. Using the 3D version requires
        rendering with P3D (see the Environment reference for more information).
        """
        pass

    def curve(self, *args):
        """Draws a curved line on the screen.

        Underlying Java method: PApplet.curve

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

        Draws a curved line on the screen. The first and second parameters specify the
        beginning control point and the last two parameters specify the ending control
        point. The middle parameters specify the start and stop of the curve. Longer
        curves can be created by putting a series of ``curve()`` functions together or
        using ``curve_vertex()``. An additional function called ``curve_tightness()``
        provides control for the visual quality of the curve. The ``curve()`` function
        is an implementation of Catmull-Rom splines. Using the 3D version requires
        rendering with P3D (see the Environment reference for more information).
        """
        return self._instance.curve(*args)

    def curve_detail(self, detail: int, /) -> None:
        """Sets the resolution at which curves display.

        Underlying Java method: PApplet.curveDetail

        Parameters
        ----------

        detail: int
            resolution of the curves

        Notes
        -----

        Sets the resolution at which curves display. The default value is 20. This
        function is only useful when using the P3D renderer as the default P2D renderer
        does not use this information.
        """
        return self._instance.curveDetail(detail)

    def curve_point(self, a: float, b: float, c: float,
                    d: float, t: float, /) -> float:
        """Evaluates the curve at point ``t`` for points ``a``, ``b``, ``c``, ``d``.

        Underlying Java method: PApplet.curvePoint

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
        on the curve. As seen in the example above, this can be used once with the ``x``
        coordinates and a second time with the ``y`` coordinates to get the location of
        a curve at ``t``.
        """
        return self._instance.curvePoint(a, b, c, d, t)

    def curve_tangent(self, a: float, b: float, c: float,
                      d: float, t: float, /) -> float:
        """Calculates the tangent of a point on a curve.

        Underlying Java method: PApplet.curveTangent

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
        """
        return self._instance.curveTangent(a, b, c, d, t)

    def curve_tightness(self, tightness: float, /) -> None:
        """Modifies the quality of forms created with ``curve()`` and ``curve_vertex()``.

        Underlying Java method: PApplet.curveTightness

        Parameters
        ----------

        tightness: float
            amount of deformation from the original vertices

        Notes
        -----

        Modifies the quality of forms created with ``curve()`` and ``curve_vertex()``.
        The parameter ``tightness`` determines how the curve fits to the vertex points.
        The value 0.0 is the default value for ``tightness`` (this value defines the
        curves to be Catmull-Rom splines) and the value 1.0 connects all the points with
        straight lines. Values within the range -5.0 and 5.0 will deform the curves but
        will leave them recognizable and as values increase in magnitude, they will
        continue to deform.
        """
        return self._instance.curveTightness(tightness)

    @overload
    def curve_vertex(self, x: float, y: float, /) -> None:
        """Specifies vertex coordinates for curves.

        Underlying Java method: PApplet.curveVertex

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

        Specifies vertex coordinates for curves. This function may only be used between
        ``begin_shape()`` and ``end_shape()`` and only when there is no MODE parameter
        specified to ``begin_shape()``. The first and last points in a series of
        ``curve_vertex()`` lines will be used to guide the beginning and end of a the
        curve. A minimum of four points is required to draw a tiny curve between the
        second and third points. Adding a fifth point with ``curve_vertex()`` will draw
        the curve between the second, third, and fourth points. The ``curve_vertex()``
        function is an implementation of Catmull-Rom splines. Using the 3D version
        requires rendering with P3D (see the Environment reference for more
        information).
        """
        pass

    @overload
    def curve_vertex(self, x: float, y: float, z: float, /) -> None:
        """Specifies vertex coordinates for curves.

        Underlying Java method: PApplet.curveVertex

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

        Specifies vertex coordinates for curves. This function may only be used between
        ``begin_shape()`` and ``end_shape()`` and only when there is no MODE parameter
        specified to ``begin_shape()``. The first and last points in a series of
        ``curve_vertex()`` lines will be used to guide the beginning and end of a the
        curve. A minimum of four points is required to draw a tiny curve between the
        second and third points. Adding a fifth point with ``curve_vertex()`` will draw
        the curve between the second, third, and fourth points. The ``curve_vertex()``
        function is an implementation of Catmull-Rom splines. Using the 3D version
        requires rendering with P3D (see the Environment reference for more
        information).
        """
        pass

    def curve_vertex(self, *args):
        """Specifies vertex coordinates for curves.

        Underlying Java method: PApplet.curveVertex

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

        Specifies vertex coordinates for curves. This function may only be used between
        ``begin_shape()`` and ``end_shape()`` and only when there is no MODE parameter
        specified to ``begin_shape()``. The first and last points in a series of
        ``curve_vertex()`` lines will be used to guide the beginning and end of a the
        curve. A minimum of four points is required to draw a tiny curve between the
        second and third points. Adding a fifth point with ``curve_vertex()`` will draw
        the curve between the second, third, and fourth points. The ``curve_vertex()``
        function is an implementation of Catmull-Rom splines. Using the 3D version
        requires rendering with P3D (see the Environment reference for more
        information).
        """
        return self._instance.curveVertex(*args)

    def directional_light(self, v1: float, v2: float, v3: float,
                          nx: float, ny: float, nz: float, /) -> None:
        """Adds a directional light.

        Underlying Java method: PApplet.directionalLight

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
        ``v3`` parameters are interpreted as either RGB or HSB values, depending on the
        current color mode. The ``nx``, ``ny``, and ``nz`` parameters specify the
        direction the light is facing. For example, setting ``ny`` to -1 will cause the
        geometry to be lit from below (since the light would be facing directly upward).
        """
        return self._instance.directionalLight(v1, v2, v3, nx, ny, nz)

    def ellipse(self, a: float, b: float, c: float, d: float, /) -> None:
        """Draws an ellipse (oval) to the screen.

        Underlying Java method: PApplet.ellipse

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
        changed with the ``ellipse_mode()`` function.
        """
        return self._instance.ellipse(a, b, c, d)

    def ellipse_mode(self, mode: int, /) -> None:
        """Modifies the location from which ellipses are drawn by changing the way in which
        parameters given to ``ellipse()`` are intepreted.

        Underlying Java method: PApplet.ellipseMode

        Parameters
        ----------

        mode: int
            either CENTER, RADIUS, CORNER, or CORNERS

        Notes
        -----

        Modifies the location from which ellipses are drawn by changing the way in which
        parameters given to ``ellipse()`` are intepreted.

        The default mode is ``ellipse_mode(CENTER)``, which interprets the first two
        parameters of ``ellipse()`` as the shape's center point, while the third and
        fourth parameters are its width and height.

        ``ellipse_mode(RADIUS)`` also uses the first two parameters of ``ellipse()`` as
        the shape's center point, but uses the third and fourth parameters to specify
        half of the shapes's width and height.

        ``ellipse_mode(CORNER)`` interprets the first two parameters of ``ellipse()`` as
        the upper-left corner of the shape, while the third and fourth parameters are
        its width and height.

        ``ellipse_mode(CORNERS)`` interprets the first two parameters of ``ellipse()``
        as the location of one corner of the ellipse's bounding box, and the third and
        fourth parameters as the location of the opposite corner.

        The parameter must be written in ALL CAPS because Processing is a case-sensitive
        language.
        """
        return self._instance.ellipseMode(mode)

    @overload
    def emissive(self, gray: float, /) -> None:
        """Sets the emissive color of the material used for drawing shapes drawn to the
        screen.

        Underlying Java method: PApplet.emissive

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
        screen. Used in combination with ``ambient()``, ``specular()``, and
        ``shininess()`` in setting the material properties of shapes.
        """
        pass

    @overload
    def emissive(self, v1: float, v2: float, v3: float, /) -> None:
        """Sets the emissive color of the material used for drawing shapes drawn to the
        screen.

        Underlying Java method: PApplet.emissive

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
        screen. Used in combination with ``ambient()``, ``specular()``, and
        ``shininess()`` in setting the material properties of shapes.
        """
        pass

    @overload
    def emissive(self, rgb: int, /) -> None:
        """Sets the emissive color of the material used for drawing shapes drawn to the
        screen.

        Underlying Java method: PApplet.emissive

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
        screen. Used in combination with ``ambient()``, ``specular()``, and
        ``shininess()`` in setting the material properties of shapes.
        """
        pass

    def emissive(self, *args):
        """Sets the emissive color of the material used for drawing shapes drawn to the
        screen.

        Underlying Java method: PApplet.emissive

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
        screen. Used in combination with ``ambient()``, ``specular()``, and
        ``shininess()`` in setting the material properties of shapes.
        """
        return self._instance.emissive(*args)

    def end_camera(self) -> None:
        """The ``begin_camera()`` and ``end_camera()`` functions enable advanced
        customization of the camera space.

        Underlying Java method: PApplet.endCamera

        Notes
        -----

        The ``begin_camera()`` and ``end_camera()`` functions enable advanced
        customization of the camera space. Please see the reference for
        ``begin_camera()`` for a description of how the functions are used.
        """
        return self._instance.endCamera()

    def end_contour(self) -> None:
        """Use the ``begin_contour()`` and ``end_contour()`` function to create negative
        shapes within shapes such as the center of the letter 'O'.

        Underlying Java method: PApplet.endContour

        Notes
        -----

        Use the ``begin_contour()`` and ``end_contour()`` function to create negative
        shapes within shapes such as the center of the letter 'O'. ``begin_contour()``
        begins recording vertices for the shape and ``end_contour()`` stops recording.
        The vertices that define a negative shape must "wind" in the opposite direction
        from the exterior shape. First draw vertices for the exterior shape in clockwise
        order, then for internal shapes, draw vertices counterclockwise.

        These functions can only be used within a ``begin_shape()``/``end_shape()`` pair
        and transformations such as ``translate()``, ``rotate()``, and ``scale()`` do
        not work within a ``begin_contour()``/``end_contour()`` pair. It is also not
        possible to use other shapes, such as ``ellipse()`` or ``rect()`` within.
        """
        return self._instance.endContour()

    def end_draw(self) -> None:
        """Finalizes the rendering of a PGraphics object so that it can be shown on screen.

        Underlying Java method: PGraphics.endDraw

        Notes
        -----

        Finalizes the rendering of a PGraphics object so that it can be shown on screen.
        """
        return self._instance.endDraw()

    def end_raw(self) -> None:
        """Complement to ``begin_raw()``; they must always be used together.

        Underlying Java method: PApplet.endRaw

        Notes
        -----

        Complement to ``begin_raw()``; they must always be used together. See the
        ``begin_raw()`` reference for details.
        """
        return self._instance.endRaw()

    @overload
    def end_shape(self) -> None:
        """The ``end_shape()`` function is the companion to ``begin_shape()`` and may only
        be called after ``begin_shape()``.

        Underlying Java method: PApplet.endShape

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

        The ``end_shape()`` function is the companion to ``begin_shape()`` and may only
        be called after ``begin_shape()``. When ``end_shape()`` is called, all of image
        data defined since the previous call to ``begin_shape()`` is written into the
        image buffer. The constant CLOSE as the value for the MODE parameter to close
        the shape (to connect the beginning and the end).
        """
        pass

    @overload
    def end_shape(self, mode: int, /) -> None:
        """The ``end_shape()`` function is the companion to ``begin_shape()`` and may only
        be called after ``begin_shape()``.

        Underlying Java method: PApplet.endShape

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

        The ``end_shape()`` function is the companion to ``begin_shape()`` and may only
        be called after ``begin_shape()``. When ``end_shape()`` is called, all of image
        data defined since the previous call to ``begin_shape()`` is written into the
        image buffer. The constant CLOSE as the value for the MODE parameter to close
        the shape (to connect the beginning and the end).
        """
        pass

    def end_shape(self, *args):
        """The ``end_shape()`` function is the companion to ``begin_shape()`` and may only
        be called after ``begin_shape()``.

        Underlying Java method: PApplet.endShape

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

        The ``end_shape()`` function is the companion to ``begin_shape()`` and may only
        be called after ``begin_shape()``. When ``end_shape()`` is called, all of image
        data defined since the previous call to ``begin_shape()`` is written into the
        image buffer. The constant CLOSE as the value for the MODE parameter to close
        the shape (to connect the beginning and the end).
        """
        return self._instance.endShape(*args)

    @overload
    def fill(self, gray: float, /) -> None:
        """Sets the color used to fill shapes.

        Underlying Java method: PApplet.fill

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
        specified in terms of the RGB or HSB color depending on the current
        ``color_mode()``. The default color space is RGB, with each value in the range
        from 0 to 255.

        When using hexadecimal notation to specify a color, use "``#``" or "``0x``"
        before the values (e.g., ``0xCCFFAA`` or ``0xFFCCFFAA``). The ``#`` syntax uses
        six digits to specify a color (just as colors are typically specified in HTML
        and CSS). When using the hexadecimal notation starting with "``0x``", the
        hexadecimal value must be specified with eight characters; the first two
        characters define the alpha component, and the remainder define the red, green,
        and blue components.

        The value for the "gray" parameter must be less than or equal to the current
        maximum value as specified by ``color_mode()``. The default maximum value is
        255.

        To change the color of an image or a texture, use ``tint()``.
        """
        pass

    @overload
    def fill(self, gray: float, alpha: float, /) -> None:
        """Sets the color used to fill shapes.

        Underlying Java method: PApplet.fill

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
        specified in terms of the RGB or HSB color depending on the current
        ``color_mode()``. The default color space is RGB, with each value in the range
        from 0 to 255.

        When using hexadecimal notation to specify a color, use "``#``" or "``0x``"
        before the values (e.g., ``0xCCFFAA`` or ``0xFFCCFFAA``). The ``#`` syntax uses
        six digits to specify a color (just as colors are typically specified in HTML
        and CSS). When using the hexadecimal notation starting with "``0x``", the
        hexadecimal value must be specified with eight characters; the first two
        characters define the alpha component, and the remainder define the red, green,
        and blue components.

        The value for the "gray" parameter must be less than or equal to the current
        maximum value as specified by ``color_mode()``. The default maximum value is
        255.

        To change the color of an image or a texture, use ``tint()``.
        """
        pass

    @overload
    def fill(self, v1: float, v2: float, v3: float, /) -> None:
        """Sets the color used to fill shapes.

        Underlying Java method: PApplet.fill

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
        specified in terms of the RGB or HSB color depending on the current
        ``color_mode()``. The default color space is RGB, with each value in the range
        from 0 to 255.

        When using hexadecimal notation to specify a color, use "``#``" or "``0x``"
        before the values (e.g., ``0xCCFFAA`` or ``0xFFCCFFAA``). The ``#`` syntax uses
        six digits to specify a color (just as colors are typically specified in HTML
        and CSS). When using the hexadecimal notation starting with "``0x``", the
        hexadecimal value must be specified with eight characters; the first two
        characters define the alpha component, and the remainder define the red, green,
        and blue components.

        The value for the "gray" parameter must be less than or equal to the current
        maximum value as specified by ``color_mode()``. The default maximum value is
        255.

        To change the color of an image or a texture, use ``tint()``.
        """
        pass

    @overload
    def fill(self, v1: float, v2: float, v3: float, alpha: float, /) -> None:
        """Sets the color used to fill shapes.

        Underlying Java method: PApplet.fill

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
        specified in terms of the RGB or HSB color depending on the current
        ``color_mode()``. The default color space is RGB, with each value in the range
        from 0 to 255.

        When using hexadecimal notation to specify a color, use "``#``" or "``0x``"
        before the values (e.g., ``0xCCFFAA`` or ``0xFFCCFFAA``). The ``#`` syntax uses
        six digits to specify a color (just as colors are typically specified in HTML
        and CSS). When using the hexadecimal notation starting with "``0x``", the
        hexadecimal value must be specified with eight characters; the first two
        characters define the alpha component, and the remainder define the red, green,
        and blue components.

        The value for the "gray" parameter must be less than or equal to the current
        maximum value as specified by ``color_mode()``. The default maximum value is
        255.

        To change the color of an image or a texture, use ``tint()``.
        """
        pass

    @overload
    def fill(self, rgb: int, /) -> None:
        """Sets the color used to fill shapes.

        Underlying Java method: PApplet.fill

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
        specified in terms of the RGB or HSB color depending on the current
        ``color_mode()``. The default color space is RGB, with each value in the range
        from 0 to 255.

        When using hexadecimal notation to specify a color, use "``#``" or "``0x``"
        before the values (e.g., ``0xCCFFAA`` or ``0xFFCCFFAA``). The ``#`` syntax uses
        six digits to specify a color (just as colors are typically specified in HTML
        and CSS). When using the hexadecimal notation starting with "``0x``", the
        hexadecimal value must be specified with eight characters; the first two
        characters define the alpha component, and the remainder define the red, green,
        and blue components.

        The value for the "gray" parameter must be less than or equal to the current
        maximum value as specified by ``color_mode()``. The default maximum value is
        255.

        To change the color of an image or a texture, use ``tint()``.
        """
        pass

    @overload
    def fill(self, rgb: int, alpha: float, /) -> None:
        """Sets the color used to fill shapes.

        Underlying Java method: PApplet.fill

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
        specified in terms of the RGB or HSB color depending on the current
        ``color_mode()``. The default color space is RGB, with each value in the range
        from 0 to 255.

        When using hexadecimal notation to specify a color, use "``#``" or "``0x``"
        before the values (e.g., ``0xCCFFAA`` or ``0xFFCCFFAA``). The ``#`` syntax uses
        six digits to specify a color (just as colors are typically specified in HTML
        and CSS). When using the hexadecimal notation starting with "``0x``", the
        hexadecimal value must be specified with eight characters; the first two
        characters define the alpha component, and the remainder define the red, green,
        and blue components.

        The value for the "gray" parameter must be less than or equal to the current
        maximum value as specified by ``color_mode()``. The default maximum value is
        255.

        To change the color of an image or a texture, use ``tint()``.
        """
        pass

    def fill(self, *args):
        """Sets the color used to fill shapes.

        Underlying Java method: PApplet.fill

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
        specified in terms of the RGB or HSB color depending on the current
        ``color_mode()``. The default color space is RGB, with each value in the range
        from 0 to 255.

        When using hexadecimal notation to specify a color, use "``#``" or "``0x``"
        before the values (e.g., ``0xCCFFAA`` or ``0xFFCCFFAA``). The ``#`` syntax uses
        six digits to specify a color (just as colors are typically specified in HTML
        and CSS). When using the hexadecimal notation starting with "``0x``", the
        hexadecimal value must be specified with eight characters; the first two
        characters define the alpha component, and the remainder define the red, green,
        and blue components.

        The value for the "gray" parameter must be less than or equal to the current
        maximum value as specified by ``color_mode()``. The default maximum value is
        255.

        To change the color of an image or a texture, use ``tint()``.
        """
        return self._instance.fill(*args)

    @overload
    def apply_filter(self, kind: int, /) -> None:
        """Filters the display window using a preset filter or with a custom shader.

        Underlying Java method: PApplet.filter

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

        Filters the display window using a preset filter or with a custom shader. Using
        a shader with ``apply_filter()`` is much faster than without. Shaders require
        the P2D or P3D renderer in ``size()``.

        The presets options are:

        THRESHOLD
        Converts the image to black and white pixels depending if they are above or
        below the threshold defined by the level parameter. The parameter must be
        between 0.0 (black) and 1.0 (white). If no level is specified, 0.5 is used.

        GRAY
        Converts any colors in the image to grayscale equivalents. No parameter is used.

        OPAQUE
        Sets the alpha channel to entirely opaque. No parameter is used.

        INVERT
        Sets each pixel to its inverse value. No parameter is used.

        POSTERIZE
        Limits each channel of the image to the number of colors specified as the
        parameter. The parameter can be set to values between 2 and 255, but results are
        most noticeable in the lower ranges.

        BLUR
        Executes a Guassian blur with the level parameter specifying the extent of the
        blurring. If no parameter is used, the blur is equivalent to Guassian blur of
        radius 1. Larger values increase the blur.

        ERODE
        Reduces the light areas. No parameter is used.

        DILATE
        Increases the light areas. No parameter is used.
        """
        pass

    @overload
    def apply_filter(self, kind: int, param: float, /) -> None:
        """Filters the display window using a preset filter or with a custom shader.

        Underlying Java method: PApplet.filter

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

        Filters the display window using a preset filter or with a custom shader. Using
        a shader with ``apply_filter()`` is much faster than without. Shaders require
        the P2D or P3D renderer in ``size()``.

        The presets options are:

        THRESHOLD
        Converts the image to black and white pixels depending if they are above or
        below the threshold defined by the level parameter. The parameter must be
        between 0.0 (black) and 1.0 (white). If no level is specified, 0.5 is used.

        GRAY
        Converts any colors in the image to grayscale equivalents. No parameter is used.

        OPAQUE
        Sets the alpha channel to entirely opaque. No parameter is used.

        INVERT
        Sets each pixel to its inverse value. No parameter is used.

        POSTERIZE
        Limits each channel of the image to the number of colors specified as the
        parameter. The parameter can be set to values between 2 and 255, but results are
        most noticeable in the lower ranges.

        BLUR
        Executes a Guassian blur with the level parameter specifying the extent of the
        blurring. If no parameter is used, the blur is equivalent to Guassian blur of
        radius 1. Larger values increase the blur.

        ERODE
        Reduces the light areas. No parameter is used.

        DILATE
        Increases the light areas. No parameter is used.
        """
        pass

    @overload
    def apply_filter(self, shader: Py5Shader, /) -> None:
        """Filters the display window using a preset filter or with a custom shader.

        Underlying Java method: PApplet.filter

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

        Filters the display window using a preset filter or with a custom shader. Using
        a shader with ``apply_filter()`` is much faster than without. Shaders require
        the P2D or P3D renderer in ``size()``.

        The presets options are:

        THRESHOLD
        Converts the image to black and white pixels depending if they are above or
        below the threshold defined by the level parameter. The parameter must be
        between 0.0 (black) and 1.0 (white). If no level is specified, 0.5 is used.

        GRAY
        Converts any colors in the image to grayscale equivalents. No parameter is used.

        OPAQUE
        Sets the alpha channel to entirely opaque. No parameter is used.

        INVERT
        Sets each pixel to its inverse value. No parameter is used.

        POSTERIZE
        Limits each channel of the image to the number of colors specified as the
        parameter. The parameter can be set to values between 2 and 255, but results are
        most noticeable in the lower ranges.

        BLUR
        Executes a Guassian blur with the level parameter specifying the extent of the
        blurring. If no parameter is used, the blur is equivalent to Guassian blur of
        radius 1. Larger values increase the blur.

        ERODE
        Reduces the light areas. No parameter is used.

        DILATE
        Increases the light areas. No parameter is used.
        """
        pass

    def apply_filter(self, *args):
        """Filters the display window using a preset filter or with a custom shader.

        Underlying Java method: PApplet.filter

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

        Filters the display window using a preset filter or with a custom shader. Using
        a shader with ``apply_filter()`` is much faster than without. Shaders require
        the P2D or P3D renderer in ``size()``.

        The presets options are:

        THRESHOLD
        Converts the image to black and white pixels depending if they are above or
        below the threshold defined by the level parameter. The parameter must be
        between 0.0 (black) and 1.0 (white). If no level is specified, 0.5 is used.

        GRAY
        Converts any colors in the image to grayscale equivalents. No parameter is used.

        OPAQUE
        Sets the alpha channel to entirely opaque. No parameter is used.

        INVERT
        Sets each pixel to its inverse value. No parameter is used.

        POSTERIZE
        Limits each channel of the image to the number of colors specified as the
        parameter. The parameter can be set to values between 2 and 255, but results are
        most noticeable in the lower ranges.

        BLUR
        Executes a Guassian blur with the level parameter specifying the extent of the
        blurring. If no parameter is used, the blur is equivalent to Guassian blur of
        radius 1. Larger values increase the blur.

        ERODE
        Reduces the light areas. No parameter is used.

        DILATE
        Increases the light areas. No parameter is used.
        """
        return self._instance.filter(*args)

    def frustum(self, left: float, right: float, bottom: float,
                top: float, near: float, far: float, /) -> None:
        """Sets a perspective matrix as defined by the parameters.

        Underlying Java method: PApplet.frustum

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
        ``perspective()``.

        Note that the near value must be greater than zero (as the point of the frustum
        "pyramid" cannot converge "behind" the viewer).  Similarly, the far value must
        be greater than the near value (as the "far" plane of the frustum must be
        "farther away" from the viewer than the near plane).

        Works like glFrustum, except it wipes out the current perspective matrix rather
        than multiplying itself with it.
        """
        return self._instance.frustum(left, right, bottom, top, near, far)

    @overload
    def get(self) -> Py5Image:
        """Reads the color of any pixel or grabs a section of an image.

        Underlying Java method: PApplet.get

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

        Reads the color of any pixel or grabs a section of an image. If no parameters
        are specified, the entire image is returned. Use the ``x`` and ``y`` parameters
        to get the value of one pixel. Get a section of the display window by specifying
        additional ``w`` and ``h`` parameters. When getting an image, the ``x`` and
        ``y`` parameters define the coordinates for the upper-left corner of the image,
        regardless of the current ``image_mode()``.

        If the pixel requested is outside of the image window, black is returned. The
        numbers returned are scaled according to the current color ranges, but only RGB
        values are returned by this function. For example, even though you may have
        drawn a shape with ``color_mode(HSB)``, the numbers returned will be in RGB
        format.

        If a width and a height are specified, ``get(x, y, w, h)`` returns a PImage
        corresponding to the part of the original PImage where the top left pixel is at
        the ``(x, y)`` position with a width of ``w`` a height of ``h``.

        Getting the color of a single pixel with ``get(x, y)`` is easy, but not as fast
        as grabbing the data directly from ``pixels[]``. The equivalent statement to
        ``get(x, y)`` using ``pixels[]`` is ``pixels[y*width+x]``. See the reference for
        pixels[] for more information.
        """
        pass

    @overload
    def get(self, x: int, y: int, /) -> int:
        """Reads the color of any pixel or grabs a section of an image.

        Underlying Java method: PApplet.get

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

        Reads the color of any pixel or grabs a section of an image. If no parameters
        are specified, the entire image is returned. Use the ``x`` and ``y`` parameters
        to get the value of one pixel. Get a section of the display window by specifying
        additional ``w`` and ``h`` parameters. When getting an image, the ``x`` and
        ``y`` parameters define the coordinates for the upper-left corner of the image,
        regardless of the current ``image_mode()``.

        If the pixel requested is outside of the image window, black is returned. The
        numbers returned are scaled according to the current color ranges, but only RGB
        values are returned by this function. For example, even though you may have
        drawn a shape with ``color_mode(HSB)``, the numbers returned will be in RGB
        format.

        If a width and a height are specified, ``get(x, y, w, h)`` returns a PImage
        corresponding to the part of the original PImage where the top left pixel is at
        the ``(x, y)`` position with a width of ``w`` a height of ``h``.

        Getting the color of a single pixel with ``get(x, y)`` is easy, but not as fast
        as grabbing the data directly from ``pixels[]``. The equivalent statement to
        ``get(x, y)`` using ``pixels[]`` is ``pixels[y*width+x]``. See the reference for
        pixels[] for more information.
        """
        pass

    @overload
    def get(self, x: int, y: int, w: int, h: int, /) -> Py5Image:
        """Reads the color of any pixel or grabs a section of an image.

        Underlying Java method: PApplet.get

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

        Reads the color of any pixel or grabs a section of an image. If no parameters
        are specified, the entire image is returned. Use the ``x`` and ``y`` parameters
        to get the value of one pixel. Get a section of the display window by specifying
        additional ``w`` and ``h`` parameters. When getting an image, the ``x`` and
        ``y`` parameters define the coordinates for the upper-left corner of the image,
        regardless of the current ``image_mode()``.

        If the pixel requested is outside of the image window, black is returned. The
        numbers returned are scaled according to the current color ranges, but only RGB
        values are returned by this function. For example, even though you may have
        drawn a shape with ``color_mode(HSB)``, the numbers returned will be in RGB
        format.

        If a width and a height are specified, ``get(x, y, w, h)`` returns a PImage
        corresponding to the part of the original PImage where the top left pixel is at
        the ``(x, y)`` position with a width of ``w`` a height of ``h``.

        Getting the color of a single pixel with ``get(x, y)`` is easy, but not as fast
        as grabbing the data directly from ``pixels[]``. The equivalent statement to
        ``get(x, y)`` using ``pixels[]`` is ``pixels[y*width+x]``. See the reference for
        pixels[] for more information.
        """
        pass

    @_return_py5image
    def get(self, *args):
        """Reads the color of any pixel or grabs a section of an image.

        Underlying Java method: PApplet.get

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

        Reads the color of any pixel or grabs a section of an image. If no parameters
        are specified, the entire image is returned. Use the ``x`` and ``y`` parameters
        to get the value of one pixel. Get a section of the display window by specifying
        additional ``w`` and ``h`` parameters. When getting an image, the ``x`` and
        ``y`` parameters define the coordinates for the upper-left corner of the image,
        regardless of the current ``image_mode()``.

        If the pixel requested is outside of the image window, black is returned. The
        numbers returned are scaled according to the current color ranges, but only RGB
        values are returned by this function. For example, even though you may have
        drawn a shape with ``color_mode(HSB)``, the numbers returned will be in RGB
        format.

        If a width and a height are specified, ``get(x, y, w, h)`` returns a PImage
        corresponding to the part of the original PImage where the top left pixel is at
        the ``(x, y)`` position with a width of ``w`` a height of ``h``.

        Getting the color of a single pixel with ``get(x, y)`` is easy, but not as fast
        as grabbing the data directly from ``pixels[]``. The equivalent statement to
        ``get(x, y)`` using ``pixels[]`` is ``pixels[y*width+x]``. See the reference for
        pixels[] for more information.
        """
        return self._instance.get(*args)

    @overload
    def get_matrix(self) -> NDArray[(Any, Any), Float]:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PApplet.getMatrix

        Methods
        -------

        You can use any of the following signatures:

         * get_matrix() -> NDArray[(Any, Any), Float]
         * get_matrix(target: NDArray[(2, 3), Float], /) -> NDArray[(2, 3), Float]
         * get_matrix(target: NDArray[(4, 4), Float], /) -> NDArray[(4, 4), Float]

        Parameters
        ----------

        target: NDArray[(2, 3), Float]
            missing variable description

        target: NDArray[(4, 4), Float]
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    @overload
    def get_matrix(self, target: NDArray[(
            2, 3), Float], /) -> NDArray[(2, 3), Float]:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PApplet.getMatrix

        Methods
        -------

        You can use any of the following signatures:

         * get_matrix() -> NDArray[(Any, Any), Float]
         * get_matrix(target: NDArray[(2, 3), Float], /) -> NDArray[(2, 3), Float]
         * get_matrix(target: NDArray[(4, 4), Float], /) -> NDArray[(4, 4), Float]

        Parameters
        ----------

        target: NDArray[(2, 3), Float]
            missing variable description

        target: NDArray[(4, 4), Float]
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    @overload
    def get_matrix(self, target: NDArray[(
            4, 4), Float], /) -> NDArray[(4, 4), Float]:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PApplet.getMatrix

        Methods
        -------

        You can use any of the following signatures:

         * get_matrix() -> NDArray[(Any, Any), Float]
         * get_matrix(target: NDArray[(2, 3), Float], /) -> NDArray[(2, 3), Float]
         * get_matrix(target: NDArray[(4, 4), Float], /) -> NDArray[(4, 4), Float]

        Parameters
        ----------

        target: NDArray[(2, 3), Float]
            missing variable description

        target: NDArray[(4, 4), Float]
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        pass

    @ _get_matrix_wrapper
    def get_matrix(self, *args):
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PApplet.getMatrix

        Methods
        -------

        You can use any of the following signatures:

         * get_matrix() -> NDArray[(Any, Any), Float]
         * get_matrix(target: NDArray[(2, 3), Float], /) -> NDArray[(2, 3), Float]
         * get_matrix(target: NDArray[(4, 4), Float], /) -> NDArray[(4, 4), Float]

        Parameters
        ----------

        target: NDArray[(2, 3), Float]
            missing variable description

        target: NDArray[(4, 4), Float]
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.getMatrix(*args)

    def green(self, rgb: int, /) -> float:
        """Extracts the green value from a color, scaled to match current ``color_mode()``.

        Underlying Java method: PApplet.green

        Parameters
        ----------

        rgb: int
            any value of the color datatype

        Notes
        -----

        Extracts the green value from a color, scaled to match current ``color_mode()``.
        The value is always returned as a float, so be careful not to assign it to an
        int value.

        The ``green()`` function is easy to use and understand, but it is slower than a
        technique called bit shifting. When working in ``color_mode(RGB, 255)``, you can
        acheive the same results as ``green()`` but with greater speed by using the
        right shift operator (``>>``) with a bit mask. For example, the following two
        lines of code are equivalent means of getting the green value of the color value
        ``c``:

        ``g1 = green(c)  # simpler, but slower to calculate
        g2 = c >> 8 & 0xFF  # very fast to calculate``
        """
        return self._instance.green(rgb)

    def hint(self, which: int, /) -> None:
        """This function is used to enable or disable special features that control how
        graphics are drawn.

        Underlying Java method: PApplet.hint

        Parameters
        ----------

        which: int
            missing variable description

        Notes
        -----

        This function is used to enable or disable special features that control how
        graphics are drawn. In the course of developing Processing, we had to make hard
        decisions about tradeoffs between performance and visual quality. We put
        significant effort into determining what makes most sense for the largest number
        of users, and then use functions like ``hint()`` to allow people to tune the
        settings for their particular sketch. Implementing a ``hint()`` is a last resort
        that's used when a more elegant solution cannot be found. Some options might
        graduate to standard features instead of hints over time, or be added and
        removed between (major) releases.


        ``hints used by the default renderer:``

        ``ENABLE_STROKE_PURE``
        Fixes a problem with shapes that have a stroke and are rendered using small
        steps (for instance, using ``vertex()`` with points that are close to one
        another), or are drawn at small sizes.


        ``hints for use with P2D and P3D:``

        ``DISABLE_ASYNC_SAVEFRAME``
        ``save()`` and ``save_frame()`` will not use separate threads for saving and
        will block until the image is written to the drive. This was the default
        behavior in 3.0b7 and before. To enable, call hint(ENABLE_ASYNC_SAVEFRAME).

        ``DISABLE_OPENGL_ERRORS``
        Speeds up the P3D renderer setting by not checking for errors while running.

        ``DISABLE_TEXTURE_MIPMAPS``
        Disable generation of texture mipmaps in P2D or P3D. This results in lower
        quality - but faster - rendering of texture images when they appear smaller than
        their native resolutions (the mipmaps are scaled-down versions of a texture that
        make it look better when drawing it at a small size). However, the difference in
        performance is fairly minor on recent desktop video cards.


        ``hints for use with P3D only:``

        ``DISABLE_DEPTH_MASK``
        Disables writing into the depth buffer. This means that a shape drawn with this
        hint can be hidden by another shape drawn later, irrespective of their distances
        to the camera. Note that this is different from disabling the depth test. The
        depth test is still applied, as long as the DISABLE_DEPTH_TEST hint is not
        called, but the depth values of the objects are not recorded. This is useful
        when drawing a semi-transparent 3D object without depth sorting, in order to
        avoid visual glitches due the faces of the object being at different distances
        from the camera, but still having the object properly occluded by the rest of
        the objects in the scene.

        ``ENABLE_DEPTH_SORT``
        Enable primitive z-sorting of triangles and lines in P3D. This can slow
        performance considerably, and the algorithm is not yet perfect.

        ``DISABLE_DEPTH_TEST``
        Disable the zbuffer, allowing you to draw on top of everything at will. When
        depth testing is disabled, items will be drawn to the screen sequentially, like
        a painting. This hint is most often used to draw in 3D, then draw in 2D on top
        of it (for instance, to draw GUI controls in 2D on top of a 3D interface). When
        called, this will also clear the depth buffer. Restore the default with
        ``hint(ENABLE_DEPTH_TEST)``, but note that with the depth buffer cleared, any 3D
        drawing that happens later in will ignore existing shapes on the screen.

        ``DISABLE_OPTIMIZED_STROKE``
        Forces the P3D renderer to draw each shape (including its strokes) separately,
        instead of batching them into larger groups for better performance. One
        consequence of this is that 2D items drawn with P3D are correctly stacked on the
        screen, depending on the order in which they were drawn. Otherwise, glitches
        such as the stroke lines being drawn on top of the interior of all the shapes
        will occur. However, this hint can make rendering substantially slower, so it is
        recommended to use it only when drawing a small amount of shapes. For drawing
        two-dimensional scenes, use the P2D renderer instead, which doesn't need the
        hint to properly stack shapes and their strokes.

        ``ENABLE_STROKE_PERSPECTIVE``
        Enables stroke geometry (lines and points) to be affected by the perspective,
        meaning that they will look smaller as they move away from the camera.
        """
        return self._instance.hint(which)

    def hue(self, rgb: int, /) -> float:
        """Extracts the hue value from a color.

        Underlying Java method: PApplet.hue

        Parameters
        ----------

        rgb: int
            any value of the color datatype

        Notes
        -----

        Extracts the hue value from a color.
        """
        return self._instance.hue(rgb)

    @overload
    def image(self, img: Py5Image, a: float, b: float, /) -> None:
        """The ``image()`` function draws an image to the display window.

        Underlying Java method: PApplet.image

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
            missing variable description

        u2: int
            missing variable description

        v1: int
            missing variable description

        v2: int
            missing variable description

        Notes
        -----

        The ``image()`` function draws an image to the display window. Images must be in
        the sketch's "data" directory to load correctly. Select "Add file..." from the
        "Sketch" menu to add the image to the data directory, or just drag the image
        file onto the sketch window. Processing currently works with GIF, JPEG, and PNG
        images.

        The ``img`` parameter specifies the image to display and by default the ``a``
        and ``b`` parameters define the location of its upper-left corner. The image is
        displayed at its original size unless the ``c`` and ``d`` parameters specify a
        different size. The ``image_mode()`` function can be used to change the way
        these parameters draw the image.

        The color of an image may be modified with the ``tint()`` function. This
        function will maintain transparency for GIF and PNG images.
        """
        pass

    @overload
    def image(self, img: Py5Image, a: float, b: float,
              c: float, d: float, /) -> None:
        """The ``image()`` function draws an image to the display window.

        Underlying Java method: PApplet.image

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
            missing variable description

        u2: int
            missing variable description

        v1: int
            missing variable description

        v2: int
            missing variable description

        Notes
        -----

        The ``image()`` function draws an image to the display window. Images must be in
        the sketch's "data" directory to load correctly. Select "Add file..." from the
        "Sketch" menu to add the image to the data directory, or just drag the image
        file onto the sketch window. Processing currently works with GIF, JPEG, and PNG
        images.

        The ``img`` parameter specifies the image to display and by default the ``a``
        and ``b`` parameters define the location of its upper-left corner. The image is
        displayed at its original size unless the ``c`` and ``d`` parameters specify a
        different size. The ``image_mode()`` function can be used to change the way
        these parameters draw the image.

        The color of an image may be modified with the ``tint()`` function. This
        function will maintain transparency for GIF and PNG images.
        """
        pass

    @overload
    def image(self, img: Py5Image, a: float, b: float, c: float,
              d: float, u1: int, v1: int, u2: int, v2: int, /) -> None:
        """The ``image()`` function draws an image to the display window.

        Underlying Java method: PApplet.image

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
            missing variable description

        u2: int
            missing variable description

        v1: int
            missing variable description

        v2: int
            missing variable description

        Notes
        -----

        The ``image()`` function draws an image to the display window. Images must be in
        the sketch's "data" directory to load correctly. Select "Add file..." from the
        "Sketch" menu to add the image to the data directory, or just drag the image
        file onto the sketch window. Processing currently works with GIF, JPEG, and PNG
        images.

        The ``img`` parameter specifies the image to display and by default the ``a``
        and ``b`` parameters define the location of its upper-left corner. The image is
        displayed at its original size unless the ``c`` and ``d`` parameters specify a
        different size. The ``image_mode()`` function can be used to change the way
        these parameters draw the image.

        The color of an image may be modified with the ``tint()`` function. This
        function will maintain transparency for GIF and PNG images.
        """
        pass

    def image(self, *args):
        """The ``image()`` function draws an image to the display window.

        Underlying Java method: PApplet.image

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
            missing variable description

        u2: int
            missing variable description

        v1: int
            missing variable description

        v2: int
            missing variable description

        Notes
        -----

        The ``image()`` function draws an image to the display window. Images must be in
        the sketch's "data" directory to load correctly. Select "Add file..." from the
        "Sketch" menu to add the image to the data directory, or just drag the image
        file onto the sketch window. Processing currently works with GIF, JPEG, and PNG
        images.

        The ``img`` parameter specifies the image to display and by default the ``a``
        and ``b`` parameters define the location of its upper-left corner. The image is
        displayed at its original size unless the ``c`` and ``d`` parameters specify a
        different size. The ``image_mode()`` function can be used to change the way
        these parameters draw the image.

        The color of an image may be modified with the ``tint()`` function. This
        function will maintain transparency for GIF and PNG images.
        """
        return self._instance.image(*args)

    def image_mode(self, mode: int, /) -> None:
        """Modifies the location from which images are drawn by changing the way in which
        parameters given to ``image()`` are intepreted.

        Underlying Java method: PApplet.imageMode

        Parameters
        ----------

        mode: int
            either CORNER, CORNERS, or CENTER

        Notes
        -----

        Modifies the location from which images are drawn by changing the way in which
        parameters given to ``image()`` are intepreted.

        The default mode is ``image_mode(CORNER)``, which interprets the second and
        third parameters of ``image()`` as the upper-left corner of the image. If two
        additional parameters are specified, they are used to set the image's width and
        height.

        ``image_mode(CORNERS)`` interprets the second and third parameters of
        ``image()`` as the  location of one corner, and the fourth and fifth parameters
        as the opposite corner.

        ``image_mode(CENTER)`` interprets the second and third parameters of ``image()``
        as the image's center point. If two additional parameters are specified, they
        are used to set the image's width and height.

        The parameter must be written in ALL CAPS because Processing is a case-sensitive
        language.
        """
        return self._instance.imageMode(mode)

    @overload
    def lerp_color(self, c1: int, c2: int, amt: float, /) -> int:
        """Calculates a color between two colors at a specific increment.

        Underlying Java method: PApplet.lerpColor

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
            missing variable description

        Notes
        -----

        Calculates a color between two colors at a specific increment. The ``amt``
        parameter is the amount to interpolate between the two values where 0.0 is equal
        to the first point, 0.1 is very near the first point, 0.5 is halfway in between,
        etc.

        An amount below 0 will be treated as 0. Likewise, amounts above 1 will be capped
        at 1. This is different from the behavior of ``lerp()``, but necessary because
        otherwise numbers outside the range will produce strange and unexpected colors.
        """
        pass

    @overload
    def lerp_color(self, c1: int, c2: int, amt: float, mode: int, /) -> int:
        """Calculates a color between two colors at a specific increment.

        Underlying Java method: PApplet.lerpColor

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
            missing variable description

        Notes
        -----

        Calculates a color between two colors at a specific increment. The ``amt``
        parameter is the amount to interpolate between the two values where 0.0 is equal
        to the first point, 0.1 is very near the first point, 0.5 is halfway in between,
        etc.

        An amount below 0 will be treated as 0. Likewise, amounts above 1 will be capped
        at 1. This is different from the behavior of ``lerp()``, but necessary because
        otherwise numbers outside the range will produce strange and unexpected colors.
        """
        pass

    def lerp_color(self, *args):
        """Calculates a color between two colors at a specific increment.

        Underlying Java method: PApplet.lerpColor

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
            missing variable description

        Notes
        -----

        Calculates a color between two colors at a specific increment. The ``amt``
        parameter is the amount to interpolate between the two values where 0.0 is equal
        to the first point, 0.1 is very near the first point, 0.5 is halfway in between,
        etc.

        An amount below 0 will be treated as 0. Likewise, amounts above 1 will be capped
        at 1. This is different from the behavior of ``lerp()``, but necessary because
        otherwise numbers outside the range will produce strange and unexpected colors.
        """
        return self._instance.lerpColor(*args)

    def light_falloff(self, constant: float, linear: float,
                      quadratic: float, /) -> None:
        """Sets the falloff rates for point lights, spot lights, and ambient lights.

        Underlying Java method: PApplet.lightFalloff

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
        ``fill()``, it affects only the elements which are created after it in the code.
        The default value is ``light_falloff(1.0, 0.0, 0.0)``, and the parameters are
        used to calculate the falloff with the following equation:

        d = distance from light position to vertex position
        falloff = 1 / (CONSTANT + d * LINEAR + (d*d) * QUADRATIC)

        Thinking about an ambient light with a falloff can be tricky. If you want a
        region of your scene to be lit ambiently with one color and another region to be
        lit ambiently with another color, you could use an ambient light with location
        and falloff. You can think of it as a point light that doesn't care which
        direction a surface is facing.
        """
        return self._instance.lightFalloff(constant, linear, quadratic)

    def light_specular(self, v1: float, v2: float, v3: float, /) -> None:
        """Sets the specular color for lights.

        Underlying Java method: PApplet.lightSpecular

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

        Sets the specular color for lights. Like ``fill()``, it affects only the
        elements which are created after it in the code. Specular refers to light which
        bounces off a surface in a preferred direction (rather than bouncing in all
        directions like a diffuse light) and is used for creating highlights. The
        specular quality of a light interacts with the specular material qualities set
        through the ``specular()`` and ``shininess()`` functions.
        """
        return self._instance.lightSpecular(v1, v2, v3)

    def lights(self) -> None:
        """Sets the default ambient light, directional light, falloff, and specular values.

        Underlying Java method: PApplet.lights

        Notes
        -----

        Sets the default ambient light, directional light, falloff, and specular values.
        The defaults are ambientLight(128, 128, 128) and directionalLight(128, 128, 128,
        0, 0, -1), lightFalloff(1, 0, 0), and lightSpecular(0, 0, 0). Lights need to be
        included in the ``draw()`` to remain persistent in a looping program. Placing
        them in the ``setup()`` of a looping program will cause them to only have an
        effect the first time through the loop.
        """
        return self._instance.lights()

    @overload
    def line(self, x1: float, y1: float, x2: float, y2: float, /) -> None:
        """Draws a line (a direct path between two points) to the screen.

        Underlying Java method: PApplet.line

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

        Draws a line (a direct path between two points) to the screen. The version of
        ``line()`` with four parameters draws the line in 2D.  To color a line, use the
        ``stroke()`` function. A line cannot be filled, therefore the ``fill()``
        function will not affect the color of a line. 2D lines are drawn with a width of
        one pixel by default, but this can be changed with the ``stroke_weight()``
        function. The version with six parameters allows the line to be placed anywhere
        within XYZ space. Drawing this shape in 3D with the ``z`` parameter requires the
        P3D parameter in combination with ``size()`` as shown in the above example.
        """
        pass

    @overload
    def line(self, x1: float, y1: float, z1: float,
             x2: float, y2: float, z2: float, /) -> None:
        """Draws a line (a direct path between two points) to the screen.

        Underlying Java method: PApplet.line

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

        Draws a line (a direct path between two points) to the screen. The version of
        ``line()`` with four parameters draws the line in 2D.  To color a line, use the
        ``stroke()`` function. A line cannot be filled, therefore the ``fill()``
        function will not affect the color of a line. 2D lines are drawn with a width of
        one pixel by default, but this can be changed with the ``stroke_weight()``
        function. The version with six parameters allows the line to be placed anywhere
        within XYZ space. Drawing this shape in 3D with the ``z`` parameter requires the
        P3D parameter in combination with ``size()`` as shown in the above example.
        """
        pass

    def line(self, *args):
        """Draws a line (a direct path between two points) to the screen.

        Underlying Java method: PApplet.line

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

        Draws a line (a direct path between two points) to the screen. The version of
        ``line()`` with four parameters draws the line in 2D.  To color a line, use the
        ``stroke()`` function. A line cannot be filled, therefore the ``fill()``
        function will not affect the color of a line. 2D lines are drawn with a width of
        one pixel by default, but this can be changed with the ``stroke_weight()``
        function. The version with six parameters allows the line to be placed anywhere
        within XYZ space. Drawing this shape in 3D with the ``z`` parameter requires the
        P3D parameter in combination with ``size()`` as shown in the above example.
        """
        return self._instance.line(*args)

    def load_pixels(self) -> None:
        """Loads the pixel data of the current display window into the ``pixels[]`` array.

        Underlying Java method: PApplet.loadPixels

        Notes
        -----

        Loads the pixel data of the current display window into the ``pixels[]`` array.
        This function must always be called before reading from or writing to
        ``pixels[]``. Subsequent changes to the display window will not be reflected in
        ``pixels`` until ``load_pixels()`` is called again.
        """
        return self._instance.loadPixels()

    @overload
    def load_shader(self, frag_filename: str, /) -> Py5Shader:
        """Loads a shader into the PShader object.

        Underlying Java method: PApplet.loadShader

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

        Loads a shader into the PShader object. The shader file must be loaded in the
        sketch's "data" folder/directory to load correctly. Shaders are compatible with
        the P2D and P3D renderers, but not with the default renderer.

        Alternatively, the file maybe be loaded from anywhere on the local computer
        using an absolute path (something that starts with / on Unix and Linux, or a
        drive letter on Windows), or the filename parameter can be a URL for a file
        found on a network.

        If the file is not available or an error occurs, ``None`` will be returned and
        an error message will be printed to the console. The error message does not halt
        the program, however the null value may cause a NullPointerException if your
        code does not check whether the value returned is null.
        """
        pass

    @overload
    def load_shader(self, frag_filename: str,
                    vert_filename: str, /) -> Py5Shader:
        """Loads a shader into the PShader object.

        Underlying Java method: PApplet.loadShader

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

        Loads a shader into the PShader object. The shader file must be loaded in the
        sketch's "data" folder/directory to load correctly. Shaders are compatible with
        the P2D and P3D renderers, but not with the default renderer.

        Alternatively, the file maybe be loaded from anywhere on the local computer
        using an absolute path (something that starts with / on Unix and Linux, or a
        drive letter on Windows), or the filename parameter can be a URL for a file
        found on a network.

        If the file is not available or an error occurs, ``None`` will be returned and
        an error message will be printed to the console. The error message does not halt
        the program, however the null value may cause a NullPointerException if your
        code does not check whether the value returned is null.
        """
        pass

    @_load_py5shader
    def load_shader(self, *args):
        """Loads a shader into the PShader object.

        Underlying Java method: PApplet.loadShader

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

        Loads a shader into the PShader object. The shader file must be loaded in the
        sketch's "data" folder/directory to load correctly. Shaders are compatible with
        the P2D and P3D renderers, but not with the default renderer.

        Alternatively, the file maybe be loaded from anywhere on the local computer
        using an absolute path (something that starts with / on Unix and Linux, or a
        drive letter on Windows), or the filename parameter can be a URL for a file
        found on a network.

        If the file is not available or an error occurs, ``None`` will be returned and
        an error message will be printed to the console. The error message does not halt
        the program, however the null value may cause a NullPointerException if your
        code does not check whether the value returned is null.
        """
        return self._instance.loadShader(*args)

    @overload
    def load_shape(self, filename: str, /) -> Py5Shape:
        """Loads geometry into a variable of type ``Py5Shape``.

        Underlying Java method: PApplet.loadShape

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
            missing variable description

        Notes
        -----

        Loads geometry into a variable of type ``Py5Shape``. SVG and OBJ files may be
        loaded. To load correctly, the file must be located in the data directory of the
        current sketch. In most cases, ``load_shape()`` should be used inside
        ``setup()`` because loading shapes inside ``draw()`` will reduce the speed of a
        sketch.

        Alternatively, the file maybe be loaded from anywhere on the local computer
        using an absolute path (something that starts with / on Unix and Linux, or a
        drive letter on Windows), or the filename parameter can be a URL for a file
        found on a network.

        If the file is not available or an error occurs, ``None`` will be returned and
        an error message will be printed to the console. The error message does not halt
        the program, however the null value may cause a NullPointerException if your
        code does not check whether the value returned is null.
        """
        pass

    @overload
    def load_shape(self, filename: str, options: str, /) -> Py5Shape:
        """Loads geometry into a variable of type ``Py5Shape``.

        Underlying Java method: PApplet.loadShape

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
            missing variable description

        Notes
        -----

        Loads geometry into a variable of type ``Py5Shape``. SVG and OBJ files may be
        loaded. To load correctly, the file must be located in the data directory of the
        current sketch. In most cases, ``load_shape()`` should be used inside
        ``setup()`` because loading shapes inside ``draw()`` will reduce the speed of a
        sketch.

        Alternatively, the file maybe be loaded from anywhere on the local computer
        using an absolute path (something that starts with / on Unix and Linux, or a
        drive letter on Windows), or the filename parameter can be a URL for a file
        found on a network.

        If the file is not available or an error occurs, ``None`` will be returned and
        an error message will be printed to the console. The error message does not halt
        the program, however the null value may cause a NullPointerException if your
        code does not check whether the value returned is null.
        """
        pass

    @_load_py5shape
    def load_shape(self, *args):
        """Loads geometry into a variable of type ``Py5Shape``.

        Underlying Java method: PApplet.loadShape

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
            missing variable description

        Notes
        -----

        Loads geometry into a variable of type ``Py5Shape``. SVG and OBJ files may be
        loaded. To load correctly, the file must be located in the data directory of the
        current sketch. In most cases, ``load_shape()`` should be used inside
        ``setup()`` because loading shapes inside ``draw()`` will reduce the speed of a
        sketch.

        Alternatively, the file maybe be loaded from anywhere on the local computer
        using an absolute path (something that starts with / on Unix and Linux, or a
        drive letter on Windows), or the filename parameter can be a URL for a file
        found on a network.

        If the file is not available or an error occurs, ``None`` will be returned and
        an error message will be printed to the console. The error message does not halt
        the program, however the null value may cause a NullPointerException if your
        code does not check whether the value returned is null.
        """
        return self._instance.loadShape(*args)

    @overload
    def mask(self, mask_array: JArray(JInt), /) -> None:
        """Masks part of an image from displaying by loading another image and using it as
        an alpha channel.

        Underlying Java method: PImage.mask

        Methods
        -------

        You can use any of the following signatures:

         * mask(img: Py5Image, /) -> None
         * mask(mask_array: JArray(JInt), /) -> None

        Parameters
        ----------

        img: Py5Image
            image to use as the mask

        mask_array: JArray(JInt)
            array of integers used as the alpha channel, needs to be the same length as the image's pixel array.

        Notes
        -----

        Masks part of an image from displaying by loading another image and using it as
        an alpha channel. This mask image should only contain grayscale data, but only
        the blue color channel is used. The mask image needs to be the same size as the
        image to which it is applied.

        In addition to using a mask image, an integer array containing the alpha channel
        data can be specified directly. This method is useful for creating dynamically
        generated alpha masks. This array must be of the same length as the target
        image's pixels array and should contain only grayscale data of values between
        0-255.
        """
        pass

    @overload
    def mask(self, img: Py5Image, /) -> None:
        """Masks part of an image from displaying by loading another image and using it as
        an alpha channel.

        Underlying Java method: PImage.mask

        Methods
        -------

        You can use any of the following signatures:

         * mask(img: Py5Image, /) -> None
         * mask(mask_array: JArray(JInt), /) -> None

        Parameters
        ----------

        img: Py5Image
            image to use as the mask

        mask_array: JArray(JInt)
            array of integers used as the alpha channel, needs to be the same length as the image's pixel array.

        Notes
        -----

        Masks part of an image from displaying by loading another image and using it as
        an alpha channel. This mask image should only contain grayscale data, but only
        the blue color channel is used. The mask image needs to be the same size as the
        image to which it is applied.

        In addition to using a mask image, an integer array containing the alpha channel
        data can be specified directly. This method is useful for creating dynamically
        generated alpha masks. This array must be of the same length as the target
        image's pixels array and should contain only grayscale data of values between
        0-255.
        """
        pass

    def mask(self, *args):
        """Masks part of an image from displaying by loading another image and using it as
        an alpha channel.

        Underlying Java method: PImage.mask

        Methods
        -------

        You can use any of the following signatures:

         * mask(img: Py5Image, /) -> None
         * mask(mask_array: JArray(JInt), /) -> None

        Parameters
        ----------

        img: Py5Image
            image to use as the mask

        mask_array: JArray(JInt)
            array of integers used as the alpha channel, needs to be the same length as the image's pixel array.

        Notes
        -----

        Masks part of an image from displaying by loading another image and using it as
        an alpha channel. This mask image should only contain grayscale data, but only
        the blue color channel is used. The mask image needs to be the same size as the
        image to which it is applied.

        In addition to using a mask image, an integer array containing the alpha channel
        data can be specified directly. This method is useful for creating dynamically
        generated alpha masks. This array must be of the same length as the target
        image's pixels array and should contain only grayscale data of values between
        0-255.
        """
        return self._instance.mask(*args)

    def model_x(self, x: float, y: float, z: float, /) -> float:
        """Returns the three-dimensional X, Y, Z position in model space.

        Underlying Java method: PApplet.modelX

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

        In the example, the ``model_x()``, ``model_y()``, and ``model_z()`` functions
        record the location of a box in space after being placed using a series of
        translate and rotate commands. After ``pop_matrix()`` is called, those
        transformations no longer apply, but the (x, y, z) coordinate returned by the
        model functions is used to place another box in the same location.
        """
        return self._instance.modelX(x, y, z)

    def model_y(self, x: float, y: float, z: float, /) -> float:
        """Returns the three-dimensional X, Y, Z position in model space.

        Underlying Java method: PApplet.modelY

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

        In the example, the ``model_x()``, ``model_y()``, and ``model_z()`` functions
        record the location of a box in space after being placed using a series of
        translate and rotate commands. After ``pop_matrix()`` is called, those
        transformations no longer apply, but the (x, y, z) coordinate returned by the
        model functions is used to place another box in the same location.
        """
        return self._instance.modelY(x, y, z)

    def model_z(self, x: float, y: float, z: float, /) -> float:
        """Returns the three-dimensional X, Y, Z position in model space.

        Underlying Java method: PApplet.modelZ

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

        In the example, the ``model_x()``, ``model_y()``, and ``model_z()`` functions
        record the location of a box in space after being placed using a series of
        translate and rotate commands. After ``pop_matrix()`` is called, those
        transformations no longer apply, but the (x, y, z) coordinate returned by the
        model functions is used to place another box in the same location.
        """
        return self._instance.modelZ(x, y, z)

    def no_clip(self) -> None:
        """Disables the clipping previously started by the ``clip()`` function.

        Underlying Java method: PApplet.noClip

        Notes
        -----

        Disables the clipping previously started by the ``clip()`` function.
        """
        return self._instance.noClip()

    def no_fill(self) -> None:
        """Disables filling geometry.

        Underlying Java method: PApplet.noFill

        Notes
        -----

        Disables filling geometry. If both ``no_stroke()`` and ``no_fill()`` are called,
        nothing will be drawn to the screen.
        """
        return self._instance.noFill()

    def no_lights(self) -> None:
        """Disable all lighting.

        Underlying Java method: PApplet.noLights

        Notes
        -----

        Disable all lighting. Lighting is turned off by default and enabled with the
        ``lights()`` function. This function can be used to disable lighting so that 2D
        geometry (which does not require lighting) can be drawn after a set of lighted
        3D geometry.
        """
        return self._instance.noLights()

    def no_smooth(self) -> None:
        """Draws all geometry and fonts with jagged (aliased) edges and images with hard
        edges between the pixels when enlarged rather than interpolating pixels.

        Underlying Java method: PApplet.noSmooth

        Notes
        -----

        Draws all geometry and fonts with jagged (aliased) edges and images with hard
        edges between the pixels when enlarged rather than interpolating pixels.  Note
        that ``smooth()`` is active by default, so it is necessary to call
        ``no_smooth()`` to disable smoothing of geometry, fonts, and images. Since the
        release of Processing 3.0, the ``no_smooth()`` function can only be run once for
        each sketch, either at the top of a sketch without a ``setup()``, or after the
        ``size()`` function when used in a sketch with ``setup()``. See the examples
        above for both scenarios.
        """
        return self._instance.noSmooth()

    def no_stroke(self) -> None:
        """Disables drawing the stroke (outline).

        Underlying Java method: PApplet.noStroke

        Notes
        -----

        Disables drawing the stroke (outline). If both ``no_stroke()`` and ``no_fill()``
        are called, nothing will be drawn to the screen.
        """
        return self._instance.noStroke()

    def no_texture(self) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PApplet.noTexture

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.noTexture()

    def no_tint(self) -> None:
        """Removes the current fill value for displaying images and reverts to displaying
        images with their original hues.

        Underlying Java method: PApplet.noTint

        Notes
        -----

        Removes the current fill value for displaying images and reverts to displaying
        images with their original hues.
        """
        return self._instance.noTint()

    def normal(self, nx: float, ny: float, nz: float, /) -> None:
        """Sets the current normal vector.

        Underlying Java method: PApplet.normal

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
        which, in turn, determines how lighting affects it. Processing attempts to
        automatically assign normals to shapes, but since that's imperfect, this is a
        better option when you want more control. This function is identical to
        ``gl_normal3f()`` in OpenGL.
        """
        return self._instance.normal(nx, ny, nz)

    @overload
    def ortho(self) -> None:
        """Sets an orthographic projection and defines a parallel clipping volume.

        Underlying Java method: PApplet.ortho

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
        ortho(-width/2, width/2, -height/2, height/2).
        """
        pass

    @overload
    def ortho(self, left: float, right: float,
              bottom: float, top: float, /) -> None:
        """Sets an orthographic projection and defines a parallel clipping volume.

        Underlying Java method: PApplet.ortho

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
        ortho(-width/2, width/2, -height/2, height/2).
        """
        pass

    @overload
    def ortho(self, left: float, right: float, bottom: float,
              top: float, near: float, far: float, /) -> None:
        """Sets an orthographic projection and defines a parallel clipping volume.

        Underlying Java method: PApplet.ortho

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
        ortho(-width/2, width/2, -height/2, height/2).
        """
        pass

    def ortho(self, *args):
        """Sets an orthographic projection and defines a parallel clipping volume.

        Underlying Java method: PApplet.ortho

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
        ortho(-width/2, width/2, -height/2, height/2).
        """
        return self._instance.ortho(*args)

    @overload
    def perspective(self) -> None:
        """Sets a perspective projection applying foreshortening, making distant objects
        appear smaller than closer ones.

        Underlying Java method: PApplet.perspective

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
        The default values are: perspective(PI/3.0, width/height, cameraZ/10.0,
        cameraZ*10.0) where cameraZ is ((height/2.0) / tan(PI*60.0/360.0));
        """
        pass

    @overload
    def perspective(self, fovy: float, aspect: float,
                    z_near: float, z_far: float, /) -> None:
        """Sets a perspective projection applying foreshortening, making distant objects
        appear smaller than closer ones.

        Underlying Java method: PApplet.perspective

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
        The default values are: perspective(PI/3.0, width/height, cameraZ/10.0,
        cameraZ*10.0) where cameraZ is ((height/2.0) / tan(PI*60.0/360.0));
        """
        pass

    def perspective(self, *args):
        """Sets a perspective projection applying foreshortening, making distant objects
        appear smaller than closer ones.

        Underlying Java method: PApplet.perspective

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
        The default values are: perspective(PI/3.0, width/height, cameraZ/10.0,
        cameraZ*10.0) where cameraZ is ((height/2.0) / tan(PI*60.0/360.0));
        """
        return self._instance.perspective(*args)

    @overload
    def point(self, x: float, y: float, /) -> None:
        """Draws a point, a coordinate in space at the dimension of one pixel.

        Underlying Java method: PApplet.point

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
        Drawing this shape in 3D with the ``z`` parameter requires the P3D parameter in
        combination with ``size()`` as shown in the above example.

        Use ``stroke()`` to set the color of a ``point()``.

        Point appears round with the default ``stroke_cap(ROUND)`` and square with
        ``stroke_cap(PROJECT)``. Points are invisible with ``stroke_cap(SQUARE)`` (no
        cap).

        Using ``point()`` with strokeWeight(1) or smaller may draw nothing to the
        screen, depending on the graphics settings of the computer. Workarounds include
        setting the pixel using ``set()`` or drawing the point using either ``circle()``
        or ``square()``.
        """
        pass

    @overload
    def point(self, x: float, y: float, z: float, /) -> None:
        """Draws a point, a coordinate in space at the dimension of one pixel.

        Underlying Java method: PApplet.point

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
        Drawing this shape in 3D with the ``z`` parameter requires the P3D parameter in
        combination with ``size()`` as shown in the above example.

        Use ``stroke()`` to set the color of a ``point()``.

        Point appears round with the default ``stroke_cap(ROUND)`` and square with
        ``stroke_cap(PROJECT)``. Points are invisible with ``stroke_cap(SQUARE)`` (no
        cap).

        Using ``point()`` with strokeWeight(1) or smaller may draw nothing to the
        screen, depending on the graphics settings of the computer. Workarounds include
        setting the pixel using ``set()`` or drawing the point using either ``circle()``
        or ``square()``.
        """
        pass

    def point(self, *args):
        """Draws a point, a coordinate in space at the dimension of one pixel.

        Underlying Java method: PApplet.point

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
        Drawing this shape in 3D with the ``z`` parameter requires the P3D parameter in
        combination with ``size()`` as shown in the above example.

        Use ``stroke()`` to set the color of a ``point()``.

        Point appears round with the default ``stroke_cap(ROUND)`` and square with
        ``stroke_cap(PROJECT)``. Points are invisible with ``stroke_cap(SQUARE)`` (no
        cap).

        Using ``point()`` with strokeWeight(1) or smaller may draw nothing to the
        screen, depending on the graphics settings of the computer. Workarounds include
        setting the pixel using ``set()`` or drawing the point using either ``circle()``
        or ``square()``.
        """
        return self._instance.point(*args)

    def point_light(self, v1: float, v2: float, v3: float,
                    x: float, y: float, z: float, /) -> None:
        """Adds a point light.

        Underlying Java method: PApplet.pointLight

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

        Adds a point light. Lights need to be included in the ``draw()`` to remain
        persistent in a looping program. Placing them in the ``setup()`` of a looping
        program will cause them to only have an effect the first time through the loop.
        The ``v1``, ``v2``, and ``v3`` parameters are interpreted as either RGB or HSB
        values, depending on the current color mode. The ``x``, ``y``, and ``z``
        parameters set the position of the light.
        """
        return self._instance.pointLight(v1, v2, v3, x, y, z)

    def pop(self) -> None:
        """The ``pop()`` function restores the previous drawing style settings and
        transformations after ``push()`` has changed them.

        Underlying Java method: PApplet.pop

        Notes
        -----

        The ``pop()`` function restores the previous drawing style settings and
        transformations after ``push()`` has changed them. Note that these functions are
        always used together. They allow you to change the style and transformation
        settings and later return to what you had. When a new state is started with
        ``push()``, it builds on the current style and transform information.

        ``push()`` stores information related to the current transformation state and
        style settings controlled by the following functions: ``rotate()``,
        ``translate()``, ``scale()``, ``fill()``, ``stroke()``, ``tint()``,
        ``stroke_weight()``, ``stroke_cap()``, ``stroke_join()``, ``image_mode()``,
        ``rect_mode()``, ``ellipse_mode()``, ``color_mode()``, ``text_align()``,
        ``text_font()``, ``text_mode()``, ``text_size()``, ``text_leading()``.

        The ``push()`` and ``pop()`` functions were added with Processing 3.5. They can
        be used in place of ``push_matrix()``, ``pop_matrix()``, ``push_styles()``, and
        ``pop_styles()``. The difference is that ``push()`` and ``pop()`` control both
        the transformations (rotate, scale, translate) and the drawing styles at the
        same time.
        """
        return self._instance.pop()

    def pop_matrix(self) -> None:
        """Pops the current transformation matrix off the matrix stack.

        Underlying Java method: PApplet.popMatrix

        Notes
        -----

        Pops the current transformation matrix off the matrix stack. Understanding
        pushing and popping requires understanding the concept of a matrix stack. The
        ``push_matrix()`` function saves the current coordinate system to the stack and
        ``pop_matrix()`` restores the prior coordinate system. ``push_matrix()`` and
        ``pop_matrix()`` are used in conjuction with the other transformation functions
        and may be embedded to control the scope of the transformations.
        """
        return self._instance.popMatrix()

    def pop_style(self) -> None:
        """The ``push_style()`` function saves the current style settings and
        ``pop_style()`` restores the prior settings; these functions are always used
        together.

        Underlying Java method: PApplet.popStyle

        Notes
        -----

        The ``push_style()`` function saves the current style settings and
        ``pop_style()`` restores the prior settings; these functions are always used
        together. They allow you to change the style settings and later return to what
        you had. When a new style is started with ``push_style()``, it builds on the
        current style information. The ``push_style()`` and ``pop_style()`` functions
        can be embedded to provide more control (see the second example above for a
        demonstration.)
        """
        return self._instance.popStyle()

    def print_camera(self) -> None:
        """Prints the current camera matrix to the Console (the text window at the bottom
        of Processing).

        Underlying Java method: PApplet.printCamera

        Notes
        -----

        Prints the current camera matrix to the Console (the text window at the bottom
        of Processing).
        """
        return self._instance.printCamera()

    def print_matrix(self) -> None:
        """Prints the current matrix to the Console (the text window at the bottom of
        Processing).

        Underlying Java method: PApplet.printMatrix

        Notes
        -----

        Prints the current matrix to the Console (the text window at the bottom of
        Processing).
        """
        return self._instance.printMatrix()

    def print_projection(self) -> None:
        """Prints the current projection matrix to the Console (the text window at the
        bottom of Processing).

        Underlying Java method: PApplet.printProjection

        Notes
        -----

        Prints the current projection matrix to the Console (the text window at the
        bottom of Processing).
        """
        return self._instance.printProjection()

    def push(self) -> None:
        """The ``push()`` function saves the current drawing style settings and
        transformations, while ``pop()`` restores these settings.

        Underlying Java method: PApplet.push

        Notes
        -----

        The ``push()`` function saves the current drawing style settings and
        transformations, while ``pop()`` restores these settings. Note that these
        functions are always used together. They allow you to change the style and
        transformation settings and later return to what you had. When a new state is
        started with ``push()``, it builds on the current style and transform
        information.

        ``push()`` stores information related to the current transformation state and
        style settings controlled by the following functions: ``rotate()``,
        ``translate()``, ``scale()``, ``fill()``, ``stroke()``, ``tint()``,
        ``stroke_weight()``, ``stroke_cap()``, ``stroke_join()``, ``image_mode()``,
        ``rect_mode()``, ``ellipse_mode()``, ``color_mode()``, ``text_align()``,
        ``text_font()``, ``text_mode()``, ``text_size()``, ``text_leading()``.

        The ``push()`` and ``pop()`` functions were added with Processing 3.5. They can
        be used in place of ``push_matrix()``, ``pop_matrix()``, ``push_styles()``, and
        ``pop_styles()``. The difference is that ``push()`` and ``pop()`` control both
        the transformations (rotate, scale, translate) and the drawing styles at the
        same time.
        """
        return self._instance.push()

    def push_matrix(self) -> None:
        """Pushes the current transformation matrix onto the matrix stack.

        Underlying Java method: PApplet.pushMatrix

        Notes
        -----

        Pushes the current transformation matrix onto the matrix stack. Understanding
        ``push_matrix()`` and ``pop_matrix()`` requires understanding the concept of a
        matrix stack. The ``push_matrix()`` function saves the current coordinate system
        to the stack and ``pop_matrix()`` restores the prior coordinate system.
        ``push_matrix()`` and ``pop_matrix()`` are used in conjuction with the other
        transformation functions and may be embedded to control the scope of the
        transformations.
        """
        return self._instance.pushMatrix()

    def push_style(self) -> None:
        """The ``push_style()`` function saves the current style settings and
        ``pop_style()`` restores the prior settings.

        Underlying Java method: PApplet.pushStyle

        Notes
        -----

        The ``push_style()`` function saves the current style settings and
        ``pop_style()`` restores the prior settings. Note that these functions are
        always used together. They allow you to change the style settings and later
        return to what you had. When a new style is started with ``push_style()``, it
        builds on the current style information. The ``push_style()`` and
        ``pop_style()`` functions can be embedded to provide more control. (See the
        second example above for a demonstration.)

        The style information controlled by the following functions are included in the
        style:
        ``fill()``, ``stroke()``, ``tint()``, ``stroke_weight()``, ``stroke_cap()``,
        ``stroke_join()``, ``image_mode()``, ``rect_mode()``, ``ellipse_mode()``,
        ``shape_mode()``, ``color_mode()``, ``text_align()``, ``text_font()``,
        ``text_mode()``, ``text_size()``, ``text_leading()``, ``emissive()``,
        ``specular()``, ``shininess()``, ``ambient()``
        """
        return self._instance.pushStyle()

    def quad(self, x1: float, y1: float, x2: float, y2: float,
             x3: float, y3: float, x4: float, y4: float, /) -> None:
        """A quad is a quadrilateral, a four sided polygon.

        Underlying Java method: PApplet.quad

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
        """
        return self._instance.quad(x1, y1, x2, y2, x3, y3, x4, y4)

    @overload
    def quadratic_vertex(self, cx: float, cy: float,
                         x3: float, y3: float, /) -> None:
        """Specifies vertex coordinates for quadratic Bezier curves.

        Underlying Java method: PApplet.quadraticVertex

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
        ``quadratic_vertex()`` is used within a ``begin_shape()`` call, it must be
        prefaced with a call to ``vertex()`` to set the first anchor point. This
        function must be used between ``begin_shape()`` and ``end_shape()`` and only
        when there is no MODE parameter specified to ``begin_shape()``. Using the 3D
        version requires rendering with P3D (see the Environment reference for more
        information).
        """
        pass

    @overload
    def quadratic_vertex(self, cx: float, cy: float, cz: float,
                         x3: float, y3: float, z3: float, /) -> None:
        """Specifies vertex coordinates for quadratic Bezier curves.

        Underlying Java method: PApplet.quadraticVertex

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
        ``quadratic_vertex()`` is used within a ``begin_shape()`` call, it must be
        prefaced with a call to ``vertex()`` to set the first anchor point. This
        function must be used between ``begin_shape()`` and ``end_shape()`` and only
        when there is no MODE parameter specified to ``begin_shape()``. Using the 3D
        version requires rendering with P3D (see the Environment reference for more
        information).
        """
        pass

    def quadratic_vertex(self, *args):
        """Specifies vertex coordinates for quadratic Bezier curves.

        Underlying Java method: PApplet.quadraticVertex

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
        ``quadratic_vertex()`` is used within a ``begin_shape()`` call, it must be
        prefaced with a call to ``vertex()`` to set the first anchor point. This
        function must be used between ``begin_shape()`` and ``end_shape()`` and only
        when there is no MODE parameter specified to ``begin_shape()``. Using the 3D
        version requires rendering with P3D (see the Environment reference for more
        information).
        """
        return self._instance.quadraticVertex(*args)

    @overload
    def rect(self, a: float, b: float, c: float, d: float, /) -> None:
        """Draws a rectangle to the screen.

        Underlying Java method: PApplet.rect

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

        Draws a rectangle to the screen. A rectangle is a four-sided shape with every
        angle at ninety degrees. By default, the first two parameters set the location
        of the upper-left corner, the third sets the width, and the fourth sets the
        height. The way these parameters are interpreted, however, may be changed with
        the ``rect_mode()`` function.

        To draw a rounded rectangle, add a fifth parameter, which is used as the radius
        value for all four corners.

        To use a different radius value for each corner, include eight parameters. When
        using eight parameters, the latter four set the radius of the arc at each corner
        separately, starting with the top-left corner and moving clockwise around the
        rectangle.
        """
        pass

    @overload
    def rect(self, a: float, b: float, c: float,
             d: float, r: float, /) -> None:
        """Draws a rectangle to the screen.

        Underlying Java method: PApplet.rect

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

        Draws a rectangle to the screen. A rectangle is a four-sided shape with every
        angle at ninety degrees. By default, the first two parameters set the location
        of the upper-left corner, the third sets the width, and the fourth sets the
        height. The way these parameters are interpreted, however, may be changed with
        the ``rect_mode()`` function.

        To draw a rounded rectangle, add a fifth parameter, which is used as the radius
        value for all four corners.

        To use a different radius value for each corner, include eight parameters. When
        using eight parameters, the latter four set the radius of the arc at each corner
        separately, starting with the top-left corner and moving clockwise around the
        rectangle.
        """
        pass

    @overload
    def rect(self, a: float, b: float, c: float, d: float,
             tl: float, tr: float, br: float, bl: float, /) -> None:
        """Draws a rectangle to the screen.

        Underlying Java method: PApplet.rect

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

        Draws a rectangle to the screen. A rectangle is a four-sided shape with every
        angle at ninety degrees. By default, the first two parameters set the location
        of the upper-left corner, the third sets the width, and the fourth sets the
        height. The way these parameters are interpreted, however, may be changed with
        the ``rect_mode()`` function.

        To draw a rounded rectangle, add a fifth parameter, which is used as the radius
        value for all four corners.

        To use a different radius value for each corner, include eight parameters. When
        using eight parameters, the latter four set the radius of the arc at each corner
        separately, starting with the top-left corner and moving clockwise around the
        rectangle.
        """
        pass

    def rect(self, *args):
        """Draws a rectangle to the screen.

        Underlying Java method: PApplet.rect

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

        Draws a rectangle to the screen. A rectangle is a four-sided shape with every
        angle at ninety degrees. By default, the first two parameters set the location
        of the upper-left corner, the third sets the width, and the fourth sets the
        height. The way these parameters are interpreted, however, may be changed with
        the ``rect_mode()`` function.

        To draw a rounded rectangle, add a fifth parameter, which is used as the radius
        value for all four corners.

        To use a different radius value for each corner, include eight parameters. When
        using eight parameters, the latter four set the radius of the arc at each corner
        separately, starting with the top-left corner and moving clockwise around the
        rectangle.
        """
        return self._instance.rect(*args)

    def rect_mode(self, mode: int, /) -> None:
        """Modifies the location from which rectangles are drawn by changing the way in
        which parameters given to ``rect()`` are intepreted.

        Underlying Java method: PApplet.rectMode

        Parameters
        ----------

        mode: int
            either CORNER, CORNERS, CENTER, or RADIUS

        Notes
        -----

        Modifies the location from which rectangles are drawn by changing the way in
        which parameters given to ``rect()`` are intepreted.

        The default mode is ``rect_mode(CORNER)``, which interprets the first two
        parameters of ``rect()`` as the upper-left corner of the shape, while the third
        and fourth parameters are its width and height.

        ``rect_mode(CORNERS)`` interprets the first two parameters of ``rect()`` as the
        location of one corner, and the third and fourth parameters as the location of
        the opposite corner.

        ``rect_mode(CENTER)`` interprets the first two parameters of ``rect()`` as the
        shape's center point, while the third and fourth parameters are its width and
        height.

        ``rect_mode(RADIUS)`` also uses the first two parameters of ``rect()`` as the
        shape's center point, but uses the third and fourth parameters to specify half
        of the shapes's width and height.

        The parameter must be written in ALL CAPS because Processing is a case-sensitive
        language.
        """
        return self._instance.rectMode(mode)

    def red(self, rgb: int, /) -> float:
        """Extracts the red value from a color, scaled to match current ``color_mode()``.

        Underlying Java method: PApplet.red

        Parameters
        ----------

        rgb: int
            any value of the color datatype

        Notes
        -----

        Extracts the red value from a color, scaled to match current ``color_mode()``.
        The value is always returned as a float, so be careful not to assign it to an
        int value.

        The ``red()`` function is easy to use and understand, but it is slower than a
        technique called bit shifting. When working in ``color_mode(RGB, 255)``, you can
        acheive the same results as ``red()`` but with greater speed by using the right
        shift operator (``>>``) with a bit mask. For example, the following two lines of
        code are equivalent means of getting the red value of the color value ``c``:

        ``r1 = red(c)  # simpler, but slower to calculate
        r2 = c >> 16 & 0xFF  # very fast to calculate``
        """
        return self._instance.red(rgb)

    def reset_matrix(self) -> None:
        """Replaces the current matrix with the identity matrix.

        Underlying Java method: PApplet.resetMatrix

        Notes
        -----

        Replaces the current matrix with the identity matrix. The equivalent function in
        OpenGL is ``gl_load_identity()``.
        """
        return self._instance.resetMatrix()

    @overload
    def reset_shader(self) -> None:
        """Restores the default shaders.

        Underlying Java method: PApplet.resetShader

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
        """
        pass

    @overload
    def reset_shader(self, kind: int, /) -> None:
        """Restores the default shaders.

        Underlying Java method: PApplet.resetShader

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
        """
        pass

    def reset_shader(self, *args):
        """Restores the default shaders.

        Underlying Java method: PApplet.resetShader

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
        """
        return self._instance.resetShader(*args)

    @overload
    def rotate(self, angle: float, /) -> None:
        """Rotates the amount specified by the ``angle`` parameter.

        Underlying Java method: PApplet.rotate

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
            missing variable description

        y: float
            missing variable description

        z: float
            missing variable description

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
        rotation matrix. This function can be further controlled by ``push_matrix()``
        and ``pop_matrix()``.
        """
        pass

    @overload
    def rotate(self, angle: float, x: float, y: float, z: float, /) -> None:
        """Rotates the amount specified by the ``angle`` parameter.

        Underlying Java method: PApplet.rotate

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
            missing variable description

        y: float
            missing variable description

        z: float
            missing variable description

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
        rotation matrix. This function can be further controlled by ``push_matrix()``
        and ``pop_matrix()``.
        """
        pass

    def rotate(self, *args):
        """Rotates the amount specified by the ``angle`` parameter.

        Underlying Java method: PApplet.rotate

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
            missing variable description

        y: float
            missing variable description

        z: float
            missing variable description

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
        rotation matrix. This function can be further controlled by ``push_matrix()``
        and ``pop_matrix()``.
        """
        return self._instance.rotate(*args)

    def rotate_x(self, angle: float, /) -> None:
        """Rotates around the x-axis the amount specified by the ``angle`` parameter.

        Underlying Java method: PApplet.rotateX

        Parameters
        ----------

        angle: float
            angle of rotation specified in radians

        Notes
        -----

        Rotates around the x-axis the amount specified by the ``angle`` parameter.
        Angles should be specified in radians (values from 0 to TWO_PI) or converted
        from degrees to radians with the ``radians()`` function. Coordinates are always
        rotated around their relative position to the origin. Positive numbers rotate in
        a clockwise direction and negative numbers rotate in a counterclockwise
        direction. Transformations apply to everything that happens after and subsequent
        calls to the function accumulates the effect. For example, calling
        ``rotate_x(PI/2)`` and then ``rotate_x(PI/2)`` is the same as ``rotate_x(PI)``.
        If ``rotate_x()`` is run within the ``draw()``, the transformation is reset when
        the loop begins again. This function requires using P3D as a third parameter to
        ``size()`` as shown in the example above.
        """
        return self._instance.rotateX(angle)

    def rotate_y(self, angle: float, /) -> None:
        """Rotates around the y-axis the amount specified by the ``angle`` parameter.

        Underlying Java method: PApplet.rotateY

        Parameters
        ----------

        angle: float
            angle of rotation specified in radians

        Notes
        -----

        Rotates around the y-axis the amount specified by the ``angle`` parameter.
        Angles should be specified in radians (values from 0 to TWO_PI) or converted
        from degrees to radians with the ``radians()`` function. Coordinates are always
        rotated around their relative position to the origin. Positive numbers rotate in
        a clockwise direction and negative numbers rotate in a counterclockwise
        direction. Transformations apply to everything that happens after and subsequent
        calls to the function accumulates the effect. For example, calling
        ``rotate_y(PI/2)`` and then ``rotate_y(PI/2)`` is the same as ``rotate_y(PI)``.
        If ``rotate_y()`` is run within the ``draw()``, the transformation is reset when
        the loop begins again. This function requires using P3D as a third parameter to
        ``size()`` as shown in the example above.
        """
        return self._instance.rotateY(angle)

    def rotate_z(self, angle: float, /) -> None:
        """Rotates around the z-axis the amount specified by the ``angle`` parameter.

        Underlying Java method: PApplet.rotateZ

        Parameters
        ----------

        angle: float
            angle of rotation specified in radians

        Notes
        -----

        Rotates around the z-axis the amount specified by the ``angle`` parameter.
        Angles should be specified in radians (values from 0 to TWO_PI) or converted
        from degrees to radians with the ``radians()`` function. Coordinates are always
        rotated around their relative position to the origin. Positive numbers rotate in
        a clockwise direction and negative numbers rotate in a counterclockwise
        direction. Transformations apply to everything that happens after and subsequent
        calls to the function accumulates the effect. For example, calling
        ``rotate_z(PI/2)`` and then ``rotate_z(PI/2)`` is the same as ``rotate_z(PI)``.
        If ``rotate_z()`` is run within the ``draw()``, the transformation is reset when
        the loop begins again. This function requires using P3D as a third parameter to
        ``size()`` as shown in the example above.
        """
        return self._instance.rotateZ(angle)

    def saturation(self, rgb: int, /) -> float:
        """Extracts the saturation value from a color.

        Underlying Java method: PApplet.saturation

        Parameters
        ----------

        rgb: int
            any value of the color datatype

        Notes
        -----

        Extracts the saturation value from a color.
        """
        return self._instance.saturation(rgb)

    @overload
    def scale(self, s: float, /) -> None:
        """Increases or decreases the size of a shape by expanding and contracting
        vertices.

        Underlying Java method: PApplet.scale

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
        ``scale(1.5)`` is the same as ``scale(3.0)``. If ``scale()`` is called within
        ``draw()``, the transformation is reset when the loop begins again. Using this
        function with the ``z`` parameter requires using P3D as a parameter for
        ``size()``, as shown in the third example above. This function can be further
        controlled with ``push_matrix()`` and ``pop_matrix()``.
        """
        pass

    @overload
    def scale(self, x: float, y: float, /) -> None:
        """Increases or decreases the size of a shape by expanding and contracting
        vertices.

        Underlying Java method: PApplet.scale

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
        ``scale(1.5)`` is the same as ``scale(3.0)``. If ``scale()`` is called within
        ``draw()``, the transformation is reset when the loop begins again. Using this
        function with the ``z`` parameter requires using P3D as a parameter for
        ``size()``, as shown in the third example above. This function can be further
        controlled with ``push_matrix()`` and ``pop_matrix()``.
        """
        pass

    @overload
    def scale(self, x: float, y: float, z: float, /) -> None:
        """Increases or decreases the size of a shape by expanding and contracting
        vertices.

        Underlying Java method: PApplet.scale

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
        ``scale(1.5)`` is the same as ``scale(3.0)``. If ``scale()`` is called within
        ``draw()``, the transformation is reset when the loop begins again. Using this
        function with the ``z`` parameter requires using P3D as a parameter for
        ``size()``, as shown in the third example above. This function can be further
        controlled with ``push_matrix()`` and ``pop_matrix()``.
        """
        pass

    def scale(self, *args):
        """Increases or decreases the size of a shape by expanding and contracting
        vertices.

        Underlying Java method: PApplet.scale

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
        ``scale(1.5)`` is the same as ``scale(3.0)``. If ``scale()`` is called within
        ``draw()``, the transformation is reset when the loop begins again. Using this
        function with the ``z`` parameter requires using P3D as a parameter for
        ``size()``, as shown in the third example above. This function can be further
        controlled with ``push_matrix()`` and ``pop_matrix()``.
        """
        return self._instance.scale(*args)

    @overload
    def screen_x(self, x: float, y: float, /) -> float:
        """Takes a three-dimensional X, Y, Z position and returns the X value for where it
        will appear on a (two-dimensional) screen.

        Underlying Java method: PApplet.screenX

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
        """
        pass

    @overload
    def screen_x(self, x: float, y: float, z: float, /) -> float:
        """Takes a three-dimensional X, Y, Z position and returns the X value for where it
        will appear on a (two-dimensional) screen.

        Underlying Java method: PApplet.screenX

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
        """
        pass

    def screen_x(self, *args):
        """Takes a three-dimensional X, Y, Z position and returns the X value for where it
        will appear on a (two-dimensional) screen.

        Underlying Java method: PApplet.screenX

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
        """
        return self._instance.screenX(*args)

    @overload
    def screen_y(self, x: float, y: float, /) -> float:
        """Takes a three-dimensional X, Y, Z position and returns the Y value for where it
        will appear on a (two-dimensional) screen.

        Underlying Java method: PApplet.screenY

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
        """
        pass

    @overload
    def screen_y(self, x: float, y: float, z: float, /) -> float:
        """Takes a three-dimensional X, Y, Z position and returns the Y value for where it
        will appear on a (two-dimensional) screen.

        Underlying Java method: PApplet.screenY

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
        """
        pass

    def screen_y(self, *args):
        """Takes a three-dimensional X, Y, Z position and returns the Y value for where it
        will appear on a (two-dimensional) screen.

        Underlying Java method: PApplet.screenY

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
        """
        return self._instance.screenY(*args)

    def screen_z(self, x: float, y: float, z: float, /) -> float:
        """Takes a three-dimensional X, Y, Z position and returns the Z value for where it
        will appear on a (two-dimensional) screen.

        Underlying Java method: PApplet.screenZ

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
        """
        return self._instance.screenZ(x, y, z)

    @overload
    def set_matrix(self, source: NDArray[(2, 3), Float], /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PApplet.setMatrix

        Methods
        -------

        You can use any of the following signatures:

         * set_matrix(source: NDArray[(2, 3), Float], /) -> None
         * set_matrix(source: NDArray[(4, 4), Float], /) -> None

        Parameters
        ----------

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
    def set_matrix(self, source: NDArray[(4, 4), Float], /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PApplet.setMatrix

        Methods
        -------

        You can use any of the following signatures:

         * set_matrix(source: NDArray[(2, 3), Float], /) -> None
         * set_matrix(source: NDArray[(4, 4), Float], /) -> None

        Parameters
        ----------

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

    def set_matrix(self, *args):
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PApplet.setMatrix

        Methods
        -------

        You can use any of the following signatures:

         * set_matrix(source: NDArray[(2, 3), Float], /) -> None
         * set_matrix(source: NDArray[(4, 4), Float], /) -> None

        Parameters
        ----------

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
        return self._instance.setMatrix(*args)

    @overload
    def shader(self, shader: Py5Shader, /) -> None:
        """Applies the shader specified by the parameters.

        Underlying Java method: PApplet.shader

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

        Applies the shader specified by the parameters. It's compatible with the P2D and
        P3D renderers, but not with the default renderer.
        """
        pass

    @overload
    def shader(self, shader: Py5Shader, kind: int, /) -> None:
        """Applies the shader specified by the parameters.

        Underlying Java method: PApplet.shader

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

        Applies the shader specified by the parameters. It's compatible with the P2D and
        P3D renderers, but not with the default renderer.
        """
        pass

    def shader(self, *args):
        """Applies the shader specified by the parameters.

        Underlying Java method: PApplet.shader

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

        Applies the shader specified by the parameters. It's compatible with the P2D and
        P3D renderers, but not with the default renderer.
        """
        return self._instance.shader(*args)

    @overload
    def shape(self, shape: Py5Shape, /) -> None:
        """Draws shapes to the display window.

        Underlying Java method: PApplet.shape

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

        Draws shapes to the display window. Shapes must be in the sketch's "data"
        directory to load correctly. Select "Add file..." from the "Sketch" menu to add
        the shape. Processing currently works with SVG, OBJ, and custom-created shapes.
        The ``shape`` parameter specifies the shape to display and the coordinate
        parameters define the location of the shape from its upper-left corner. The
        shape is displayed at its original size unless the ``c`` and ``d`` parameters
        specify a different size. The ``shape_mode()`` function can be used to change
        the way these parameters are interpreted.
        """
        pass

    @overload
    def shape(self, shape: Py5Shape, x: float, y: float, /) -> None:
        """Draws shapes to the display window.

        Underlying Java method: PApplet.shape

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

        Draws shapes to the display window. Shapes must be in the sketch's "data"
        directory to load correctly. Select "Add file..." from the "Sketch" menu to add
        the shape. Processing currently works with SVG, OBJ, and custom-created shapes.
        The ``shape`` parameter specifies the shape to display and the coordinate
        parameters define the location of the shape from its upper-left corner. The
        shape is displayed at its original size unless the ``c`` and ``d`` parameters
        specify a different size. The ``shape_mode()`` function can be used to change
        the way these parameters are interpreted.
        """
        pass

    @overload
    def shape(self, shape: Py5Shape, a: float,
              b: float, c: float, d: float, /) -> None:
        """Draws shapes to the display window.

        Underlying Java method: PApplet.shape

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

        Draws shapes to the display window. Shapes must be in the sketch's "data"
        directory to load correctly. Select "Add file..." from the "Sketch" menu to add
        the shape. Processing currently works with SVG, OBJ, and custom-created shapes.
        The ``shape`` parameter specifies the shape to display and the coordinate
        parameters define the location of the shape from its upper-left corner. The
        shape is displayed at its original size unless the ``c`` and ``d`` parameters
        specify a different size. The ``shape_mode()`` function can be used to change
        the way these parameters are interpreted.
        """
        pass

    def shape(self, *args):
        """Draws shapes to the display window.

        Underlying Java method: PApplet.shape

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

        Draws shapes to the display window. Shapes must be in the sketch's "data"
        directory to load correctly. Select "Add file..." from the "Sketch" menu to add
        the shape. Processing currently works with SVG, OBJ, and custom-created shapes.
        The ``shape`` parameter specifies the shape to display and the coordinate
        parameters define the location of the shape from its upper-left corner. The
        shape is displayed at its original size unless the ``c`` and ``d`` parameters
        specify a different size. The ``shape_mode()`` function can be used to change
        the way these parameters are interpreted.
        """
        return self._instance.shape(*args)

    def shape_mode(self, mode: int, /) -> None:
        """Modifies the location from which shapes draw.

        Underlying Java method: PApplet.shapeMode

        Parameters
        ----------

        mode: int
            either CORNER, CORNERS, CENTER

        Notes
        -----

        Modifies the location from which shapes draw. The default mode is
        ``shape_mode(CORNER)``, which specifies the location to be the upper left corner
        of the shape and uses the third and fourth parameters of ``shape()`` to specify
        the width and height. The syntax ``shape_mode(CORNERS)`` uses the first and
        second parameters of ``shape()`` to set the location of one corner and uses the
        third and fourth parameters to set the opposite corner. The syntax
        ``shape_mode(CENTER)`` draws the shape from its center point and uses the third
        and forth parameters of ``shape()`` to specify the width and height. The
        parameter must be written in "ALL CAPS" because Processing is a case sensitive
        language.
        """
        return self._instance.shapeMode(mode)

    def shear_x(self, angle: float, /) -> None:
        """Shears a shape around the x-axis the amount specified by the ``angle``
        parameter.

        Underlying Java method: PApplet.shearX

        Parameters
        ----------

        angle: float
            angle of shear specified in radians

        Notes
        -----

        Shears a shape around the x-axis the amount specified by the ``angle``
        parameter. Angles should be specified in radians (values from 0 to PI*2) or
        converted to radians with the ``radians()`` function. Objects are always sheared
        around their relative position to the origin and positive numbers shear objects
        in a clockwise direction. Transformations apply to everything that happens after
        and subsequent calls to the function accumulates the effect. For example,
        calling ``shear_x(PI/2)`` and then ``shear_x(PI/2)`` is the same as
        ``shear_x(PI)``. If ``shear_x()`` is called within the ``draw()``, the
        transformation is reset when the loop begins again.

        Technically, ``shear_x()`` multiplies the current transformation matrix by a
        rotation matrix. This function can be further controlled by the
        ``push_matrix()`` and ``pop_matrix()`` functions.
        """
        return self._instance.shearX(angle)

    def shear_y(self, angle: float, /) -> None:
        """Shears a shape around the y-axis the amount specified by the ``angle``
        parameter.

        Underlying Java method: PApplet.shearY

        Parameters
        ----------

        angle: float
            angle of shear specified in radians

        Notes
        -----

        Shears a shape around the y-axis the amount specified by the ``angle``
        parameter. Angles should be specified in radians (values from 0 to PI*2) or
        converted to radians with the ``radians()`` function. Objects are always sheared
        around their relative position to the origin and positive numbers shear objects
        in a clockwise direction. Transformations apply to everything that happens after
        and subsequent calls to the function accumulates the effect. For example,
        calling ``shear_y(PI/2)`` and then ``shear_y(PI/2)`` is the same as
        ``shear_y(PI)``. If ``shear_y()`` is called within the ``draw()``, the
        transformation is reset when the loop begins again.

        Technically, ``shear_y()`` multiplies the current transformation matrix by a
        rotation matrix. This function can be further controlled by the
        ``push_matrix()`` and ``pop_matrix()`` functions.
        """
        return self._instance.shearY(angle)

    def shininess(self, shine: float, /) -> None:
        """Sets the amount of gloss in the surface of shapes.

        Underlying Java method: PApplet.shininess

        Parameters
        ----------

        shine: float
            degree of shininess

        Notes
        -----

        Sets the amount of gloss in the surface of shapes. Used in combination with
        ``ambient()``, ``specular()``, and ``emissive()`` in setting the material
        properties of shapes.
        """
        return self._instance.shininess(shine)

    @overload
    def smooth(self) -> None:
        """Draws all geometry with smooth (anti-aliased) edges.

        Underlying Java method: PApplet.smooth

        Methods
        -------

        You can use any of the following signatures:

         * smooth() -> None
         * smooth(level: int, /) -> None

        Parameters
        ----------

        level: int
            either 2, 3, 4, or 8 depending on the renderer

        Notes
        -----

        Draws all geometry with smooth (anti-aliased) edges. This behavior is the
        default, so ``smooth()`` only needs to be used when a program needs to set the
        smoothing in a different way. The ``level`` parameter increases the amount of
        smoothness. This is the level of over sampling applied to the graphics buffer.

        With the P2D and P3D renderers, ``smooth(2)`` is the default, this is called "2x
        anti-aliasing." The code ``smooth(4)`` is used for 4x anti-aliasing and
        ``smooth(8)`` is specified for "8x anti-aliasing." The maximum anti-aliasing
        level is determined by the hardware of the machine that is running the software,
        so ``smooth(4)`` and ``smooth(8)`` will not work with every computer.

        The default renderer uses ``smooth(3)`` by default. This is bicubic smoothing.
        The other option for the default renderer is ``smooth(2)``, which is bilinear
        smoothing.

        With Processing 3.0, ``smooth()`` is different than before. It was common to use
        ``smooth()`` and ``no_smooth()`` to turn on and off antialiasing within a
        sketch. Now, because of how the software has changed, ``smooth()`` can only be
        set once within a sketch. It can be used either at the top of a sketch without a
        ``setup()``, or after the ``size()`` function when used in a sketch with
        ``setup()``. The ``no_smooth()`` function also follows the same rules.

        When ``smooth()`` is used with a ``Py5Graphics`` object, it should be run right
        after the object is created with ``create_graphics()``, as shown in the
        Reference in the third example.
        """
        pass

    @overload
    def smooth(self, quality: int, /) -> None:
        """Draws all geometry with smooth (anti-aliased) edges.

        Underlying Java method: PApplet.smooth

        Methods
        -------

        You can use any of the following signatures:

         * smooth() -> None
         * smooth(level: int, /) -> None

        Parameters
        ----------

        level: int
            either 2, 3, 4, or 8 depending on the renderer

        Notes
        -----

        Draws all geometry with smooth (anti-aliased) edges. This behavior is the
        default, so ``smooth()`` only needs to be used when a program needs to set the
        smoothing in a different way. The ``level`` parameter increases the amount of
        smoothness. This is the level of over sampling applied to the graphics buffer.

        With the P2D and P3D renderers, ``smooth(2)`` is the default, this is called "2x
        anti-aliasing." The code ``smooth(4)`` is used for 4x anti-aliasing and
        ``smooth(8)`` is specified for "8x anti-aliasing." The maximum anti-aliasing
        level is determined by the hardware of the machine that is running the software,
        so ``smooth(4)`` and ``smooth(8)`` will not work with every computer.

        The default renderer uses ``smooth(3)`` by default. This is bicubic smoothing.
        The other option for the default renderer is ``smooth(2)``, which is bilinear
        smoothing.

        With Processing 3.0, ``smooth()`` is different than before. It was common to use
        ``smooth()`` and ``no_smooth()`` to turn on and off antialiasing within a
        sketch. Now, because of how the software has changed, ``smooth()`` can only be
        set once within a sketch. It can be used either at the top of a sketch without a
        ``setup()``, or after the ``size()`` function when used in a sketch with
        ``setup()``. The ``no_smooth()`` function also follows the same rules.

        When ``smooth()`` is used with a ``Py5Graphics`` object, it should be run right
        after the object is created with ``create_graphics()``, as shown in the
        Reference in the third example.
        """
        pass

    def smooth(self, *args):
        """Draws all geometry with smooth (anti-aliased) edges.

        Underlying Java method: PApplet.smooth

        Methods
        -------

        You can use any of the following signatures:

         * smooth() -> None
         * smooth(level: int, /) -> None

        Parameters
        ----------

        level: int
            either 2, 3, 4, or 8 depending on the renderer

        Notes
        -----

        Draws all geometry with smooth (anti-aliased) edges. This behavior is the
        default, so ``smooth()`` only needs to be used when a program needs to set the
        smoothing in a different way. The ``level`` parameter increases the amount of
        smoothness. This is the level of over sampling applied to the graphics buffer.

        With the P2D and P3D renderers, ``smooth(2)`` is the default, this is called "2x
        anti-aliasing." The code ``smooth(4)`` is used for 4x anti-aliasing and
        ``smooth(8)`` is specified for "8x anti-aliasing." The maximum anti-aliasing
        level is determined by the hardware of the machine that is running the software,
        so ``smooth(4)`` and ``smooth(8)`` will not work with every computer.

        The default renderer uses ``smooth(3)`` by default. This is bicubic smoothing.
        The other option for the default renderer is ``smooth(2)``, which is bilinear
        smoothing.

        With Processing 3.0, ``smooth()`` is different than before. It was common to use
        ``smooth()`` and ``no_smooth()`` to turn on and off antialiasing within a
        sketch. Now, because of how the software has changed, ``smooth()`` can only be
        set once within a sketch. It can be used either at the top of a sketch without a
        ``setup()``, or after the ``size()`` function when used in a sketch with
        ``setup()``. The ``no_smooth()`` function also follows the same rules.

        When ``smooth()`` is used with a ``Py5Graphics`` object, it should be run right
        after the object is created with ``create_graphics()``, as shown in the
        Reference in the third example.
        """
        return self._instance.smooth(*args)

    @overload
    def specular(self, gray: float, /) -> None:
        """Sets the specular color of the materials used for shapes drawn to the screen,
        which sets the color of highlights.

        Underlying Java method: PApplet.specular

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

        Sets the specular color of the materials used for shapes drawn to the screen,
        which sets the color of highlights. Specular refers to light which bounces off a
        surface in a preferred direction (rather than bouncing in all directions like a
        diffuse light). Used in combination with ``emissive()``, ``ambient()``, and
        ``shininess()`` in setting the material properties of shapes.
        """
        pass

    @overload
    def specular(self, v1: float, v2: float, v3: float, /) -> None:
        """Sets the specular color of the materials used for shapes drawn to the screen,
        which sets the color of highlights.

        Underlying Java method: PApplet.specular

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

        Sets the specular color of the materials used for shapes drawn to the screen,
        which sets the color of highlights. Specular refers to light which bounces off a
        surface in a preferred direction (rather than bouncing in all directions like a
        diffuse light). Used in combination with ``emissive()``, ``ambient()``, and
        ``shininess()`` in setting the material properties of shapes.
        """
        pass

    @overload
    def specular(self, rgb: int, /) -> None:
        """Sets the specular color of the materials used for shapes drawn to the screen,
        which sets the color of highlights.

        Underlying Java method: PApplet.specular

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

        Sets the specular color of the materials used for shapes drawn to the screen,
        which sets the color of highlights. Specular refers to light which bounces off a
        surface in a preferred direction (rather than bouncing in all directions like a
        diffuse light). Used in combination with ``emissive()``, ``ambient()``, and
        ``shininess()`` in setting the material properties of shapes.
        """
        pass

    def specular(self, *args):
        """Sets the specular color of the materials used for shapes drawn to the screen,
        which sets the color of highlights.

        Underlying Java method: PApplet.specular

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

        Sets the specular color of the materials used for shapes drawn to the screen,
        which sets the color of highlights. Specular refers to light which bounces off a
        surface in a preferred direction (rather than bouncing in all directions like a
        diffuse light). Used in combination with ``emissive()``, ``ambient()``, and
        ``shininess()`` in setting the material properties of shapes.
        """
        return self._instance.specular(*args)

    def sphere(self, r: float, /) -> None:
        """A sphere is a hollow ball made from tessellated triangles.

        Underlying Java method: PApplet.sphere

        Parameters
        ----------

        r: float
            the radius of the sphere

        Notes
        -----

        A sphere is a hollow ball made from tessellated triangles.
        """
        return self._instance.sphere(r)

    @overload
    def sphere_detail(self, res: int, /) -> None:
        """Controls the detail used to render a sphere by adjusting the number of vertices
        of the sphere mesh.

        Underlying Java method: PApplet.sphereDetail

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
        detailed sphere definition with vertices every 360/30 = 12 degrees. If you're
        going to render a great number of spheres per frame, it is advised to reduce the
        level of detail using this function. The setting stays active until
        ``sphere_detail()`` is called again with a new parameter and so should *not* be
        called prior to every ``sphere()`` statement, unless you wish to render spheres
        with different settings, e.g. using less detail for smaller spheres or ones
        further away from the camera. To control the detail of the horizontal and
        vertical resolution independently, use the version of the functions with two
        parameters.
        """
        pass

    @overload
    def sphere_detail(self, ures: int, vres: int, /) -> None:
        """Controls the detail used to render a sphere by adjusting the number of vertices
        of the sphere mesh.

        Underlying Java method: PApplet.sphereDetail

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
        detailed sphere definition with vertices every 360/30 = 12 degrees. If you're
        going to render a great number of spheres per frame, it is advised to reduce the
        level of detail using this function. The setting stays active until
        ``sphere_detail()`` is called again with a new parameter and so should *not* be
        called prior to every ``sphere()`` statement, unless you wish to render spheres
        with different settings, e.g. using less detail for smaller spheres or ones
        further away from the camera. To control the detail of the horizontal and
        vertical resolution independently, use the version of the functions with two
        parameters.
        """
        pass

    def sphere_detail(self, *args):
        """Controls the detail used to render a sphere by adjusting the number of vertices
        of the sphere mesh.

        Underlying Java method: PApplet.sphereDetail

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
        detailed sphere definition with vertices every 360/30 = 12 degrees. If you're
        going to render a great number of spheres per frame, it is advised to reduce the
        level of detail using this function. The setting stays active until
        ``sphere_detail()`` is called again with a new parameter and so should *not* be
        called prior to every ``sphere()`` statement, unless you wish to render spheres
        with different settings, e.g. using less detail for smaller spheres or ones
        further away from the camera. To control the detail of the horizontal and
        vertical resolution independently, use the version of the functions with two
        parameters.
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

        Underlying Java method: PApplet.spotLight

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

        Adds a spot light. Lights need to be included in the ``draw()`` to remain
        persistent in a looping program. Placing them in the ``setup()`` of a looping
        program will cause them to only have an effect the first time through the loop.
        The ``v1``, ``v2``, and ``v3`` parameters are interpreted as either RGB or HSB
        values, depending on the current color mode. The ``x``, ``y``, and ``z``
        parameters specify the position of the light and ``nx``, ``ny``, ``nz`` specify
        the direction of light. The ``angle`` parameter affects angle of the spotlight
        cone, while ``concentration`` sets the bias of light focusing toward the center
        of that cone.
        """
        return self._instance.spotLight(
            v1, v2, v3, x, y, z, nx, ny, nz, angle, concentration)

    def square(self, x: float, y: float, extent: float, /) -> None:
        """Draws a square to the screen.

        Underlying Java method: PApplet.square

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

        Draws a square to the screen. A square is a four-sided shape with every angle at
        ninety degrees and each side is the same length. By default, the first two
        parameters set the location of the upper-left corner, the third sets the width
        and height. The way these parameters are interpreted, however, may be changed
        with the ``rect_mode()`` function.
        """
        return self._instance.square(x, y, extent)

    @overload
    def stroke(self, gray: float, /) -> None:
        """Sets the color used to draw lines and borders around shapes.

        Underlying Java method: PApplet.stroke

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
        ``c``olor_mode()``.`` The default color space is RGB, with each value in the
        range from 0 to 255.

        When using hexadecimal notation to specify a color, use "``#``" or "``0x``"
        before the values (e.g., ``0xCCFFAA`` or ``0xFFCCFFAA``). The ``#`` syntax uses
        six digits to specify a color (just as colors are typically specified in HTML
        and CSS). When using the hexadecimal notation starting with "``0x``", the
        hexadecimal value must be specified with eight characters; the first two
        characters define the alpha component, and the remainder define the red, green,
        and blue components.

        The value for the gray parameter must be less than or equal to the current
        maximum value as specified by ``color_mode()``. The default maximum value is
        255.

        When drawing in 2D with the default renderer, you may need
        ``hint(ENABLE_STROKE_PURE)`` to improve drawing quality (at the expense of
        performance). See the ``hint()`` documentation for more details.
        """
        pass

    @overload
    def stroke(self, gray: float, alpha: float, /) -> None:
        """Sets the color used to draw lines and borders around shapes.

        Underlying Java method: PApplet.stroke

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
        ``c``olor_mode()``.`` The default color space is RGB, with each value in the
        range from 0 to 255.

        When using hexadecimal notation to specify a color, use "``#``" or "``0x``"
        before the values (e.g., ``0xCCFFAA`` or ``0xFFCCFFAA``). The ``#`` syntax uses
        six digits to specify a color (just as colors are typically specified in HTML
        and CSS). When using the hexadecimal notation starting with "``0x``", the
        hexadecimal value must be specified with eight characters; the first two
        characters define the alpha component, and the remainder define the red, green,
        and blue components.

        The value for the gray parameter must be less than or equal to the current
        maximum value as specified by ``color_mode()``. The default maximum value is
        255.

        When drawing in 2D with the default renderer, you may need
        ``hint(ENABLE_STROKE_PURE)`` to improve drawing quality (at the expense of
        performance). See the ``hint()`` documentation for more details.
        """
        pass

    @overload
    def stroke(self, v1: float, v2: float, v3: float, /) -> None:
        """Sets the color used to draw lines and borders around shapes.

        Underlying Java method: PApplet.stroke

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
        ``c``olor_mode()``.`` The default color space is RGB, with each value in the
        range from 0 to 255.

        When using hexadecimal notation to specify a color, use "``#``" or "``0x``"
        before the values (e.g., ``0xCCFFAA`` or ``0xFFCCFFAA``). The ``#`` syntax uses
        six digits to specify a color (just as colors are typically specified in HTML
        and CSS). When using the hexadecimal notation starting with "``0x``", the
        hexadecimal value must be specified with eight characters; the first two
        characters define the alpha component, and the remainder define the red, green,
        and blue components.

        The value for the gray parameter must be less than or equal to the current
        maximum value as specified by ``color_mode()``. The default maximum value is
        255.

        When drawing in 2D with the default renderer, you may need
        ``hint(ENABLE_STROKE_PURE)`` to improve drawing quality (at the expense of
        performance). See the ``hint()`` documentation for more details.
        """
        pass

    @overload
    def stroke(self, v1: float, v2: float, v3: float, alpha: float, /) -> None:
        """Sets the color used to draw lines and borders around shapes.

        Underlying Java method: PApplet.stroke

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
        ``c``olor_mode()``.`` The default color space is RGB, with each value in the
        range from 0 to 255.

        When using hexadecimal notation to specify a color, use "``#``" or "``0x``"
        before the values (e.g., ``0xCCFFAA`` or ``0xFFCCFFAA``). The ``#`` syntax uses
        six digits to specify a color (just as colors are typically specified in HTML
        and CSS). When using the hexadecimal notation starting with "``0x``", the
        hexadecimal value must be specified with eight characters; the first two
        characters define the alpha component, and the remainder define the red, green,
        and blue components.

        The value for the gray parameter must be less than or equal to the current
        maximum value as specified by ``color_mode()``. The default maximum value is
        255.

        When drawing in 2D with the default renderer, you may need
        ``hint(ENABLE_STROKE_PURE)`` to improve drawing quality (at the expense of
        performance). See the ``hint()`` documentation for more details.
        """
        pass

    @overload
    def stroke(self, rgb: int, /) -> None:
        """Sets the color used to draw lines and borders around shapes.

        Underlying Java method: PApplet.stroke

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
        ``c``olor_mode()``.`` The default color space is RGB, with each value in the
        range from 0 to 255.

        When using hexadecimal notation to specify a color, use "``#``" or "``0x``"
        before the values (e.g., ``0xCCFFAA`` or ``0xFFCCFFAA``). The ``#`` syntax uses
        six digits to specify a color (just as colors are typically specified in HTML
        and CSS). When using the hexadecimal notation starting with "``0x``", the
        hexadecimal value must be specified with eight characters; the first two
        characters define the alpha component, and the remainder define the red, green,
        and blue components.

        The value for the gray parameter must be less than or equal to the current
        maximum value as specified by ``color_mode()``. The default maximum value is
        255.

        When drawing in 2D with the default renderer, you may need
        ``hint(ENABLE_STROKE_PURE)`` to improve drawing quality (at the expense of
        performance). See the ``hint()`` documentation for more details.
        """
        pass

    @overload
    def stroke(self, rgb: int, alpha: float, /) -> None:
        """Sets the color used to draw lines and borders around shapes.

        Underlying Java method: PApplet.stroke

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
        ``c``olor_mode()``.`` The default color space is RGB, with each value in the
        range from 0 to 255.

        When using hexadecimal notation to specify a color, use "``#``" or "``0x``"
        before the values (e.g., ``0xCCFFAA`` or ``0xFFCCFFAA``). The ``#`` syntax uses
        six digits to specify a color (just as colors are typically specified in HTML
        and CSS). When using the hexadecimal notation starting with "``0x``", the
        hexadecimal value must be specified with eight characters; the first two
        characters define the alpha component, and the remainder define the red, green,
        and blue components.

        The value for the gray parameter must be less than or equal to the current
        maximum value as specified by ``color_mode()``. The default maximum value is
        255.

        When drawing in 2D with the default renderer, you may need
        ``hint(ENABLE_STROKE_PURE)`` to improve drawing quality (at the expense of
        performance). See the ``hint()`` documentation for more details.
        """
        pass

    def stroke(self, *args):
        """Sets the color used to draw lines and borders around shapes.

        Underlying Java method: PApplet.stroke

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
        ``c``olor_mode()``.`` The default color space is RGB, with each value in the
        range from 0 to 255.

        When using hexadecimal notation to specify a color, use "``#``" or "``0x``"
        before the values (e.g., ``0xCCFFAA`` or ``0xFFCCFFAA``). The ``#`` syntax uses
        six digits to specify a color (just as colors are typically specified in HTML
        and CSS). When using the hexadecimal notation starting with "``0x``", the
        hexadecimal value must be specified with eight characters; the first two
        characters define the alpha component, and the remainder define the red, green,
        and blue components.

        The value for the gray parameter must be less than or equal to the current
        maximum value as specified by ``color_mode()``. The default maximum value is
        255.

        When drawing in 2D with the default renderer, you may need
        ``hint(ENABLE_STROKE_PURE)`` to improve drawing quality (at the expense of
        performance). See the ``hint()`` documentation for more details.
        """
        return self._instance.stroke(*args)

    def stroke_cap(self, cap: int, /) -> None:
        """Sets the style for rendering line endings.

        Underlying Java method: PApplet.strokeCap

        Parameters
        ----------

        cap: int
            either SQUARE, PROJECT, or ROUND

        Notes
        -----

        Sets the style for rendering line endings. These ends are either squared,
        extended, or rounded, each of which specified with the corresponding parameters:
        SQUARE, PROJECT, and ROUND. The default cap is ROUND.

        To make ``point()`` appear square, use ``stroke_cap(PROJECT)``. Using
        ``stroke_cap(SQUARE)`` (no cap) causes points to become invisible.
        """
        return self._instance.strokeCap(cap)

    def stroke_join(self, join: int, /) -> None:
        """Sets the style of the joints which connect line segments.

        Underlying Java method: PApplet.strokeJoin

        Parameters
        ----------

        join: int
            either MITER, BEVEL, ROUND

        Notes
        -----

        Sets the style of the joints which connect line segments. These joints are
        either mitered, beveled, or rounded and specified with the corresponding
        parameters MITER, BEVEL, and ROUND. The default joint is MITER.
        """
        return self._instance.strokeJoin(join)

    def stroke_weight(self, weight: float, /) -> None:
        """Sets the width of the stroke used for lines, points, and the border around
        shapes.

        Underlying Java method: PApplet.strokeWeight

        Parameters
        ----------

        weight: float
            the weight (in pixels) of the stroke

        Notes
        -----

        Sets the width of the stroke used for lines, points, and the border around
        shapes. All widths are set in units of pixels.

        Using ``point()`` with strokeWeight(1) or smaller may draw nothing to the
        screen, depending on the graphics settings of the computer. Workarounds include
        setting the pixel using ``set()`` or drawing the point using either ``circle()``
        or ``square()``.
        """
        return self._instance.strokeWeight(weight)

    @overload
    def text(self, c: chr, x: float, y: float, /) -> None:
        """Draws text to the screen.

        Underlying Java method: PApplet.text

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
            missing variable description

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

        Draws text to the screen. Displays the information specified in the first
        parameter on the screen in the position specified by the additional parameters.
        A default font will be used unless a font is set with the ``text_font()``
        function and a default size will be used unless a font is set with
        ``text_size()``. Change the color of the text with the ``fill()`` function. The
        text displays in relation to the ``text_align()`` function, which gives the
        option to draw to the left, right, and center of the coordinates.

        The ``x2`` and ``y2`` parameters define a rectangular area to display within and
        may only be used with string data. When these parameters are specified, they are
        interpreted based on the current ``rect_mode()`` setting. Text that does not fit
        completely within the rectangle specified will not be drawn to the screen.

        Note that Processing now lets you call ``text()`` without first specifying a
        PFont with ``text_font()``. In that case, a generic sans-serif font will be used
        instead. (See the third example above.)
        """
        pass

    @overload
    def text(self, c: chr, x: float, y: float, z: float, /) -> None:
        """Draws text to the screen.

        Underlying Java method: PApplet.text

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
            missing variable description

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

        Draws text to the screen. Displays the information specified in the first
        parameter on the screen in the position specified by the additional parameters.
        A default font will be used unless a font is set with the ``text_font()``
        function and a default size will be used unless a font is set with
        ``text_size()``. Change the color of the text with the ``fill()`` function. The
        text displays in relation to the ``text_align()`` function, which gives the
        option to draw to the left, right, and center of the coordinates.

        The ``x2`` and ``y2`` parameters define a rectangular area to display within and
        may only be used with string data. When these parameters are specified, they are
        interpreted based on the current ``rect_mode()`` setting. Text that does not fit
        completely within the rectangle specified will not be drawn to the screen.

        Note that Processing now lets you call ``text()`` without first specifying a
        PFont with ``text_font()``. In that case, a generic sans-serif font will be used
        instead. (See the third example above.)
        """
        pass

    @overload
    def text(self, chars: List[chr], start: int,
             stop: int, x: float, y: float, /) -> None:
        """Draws text to the screen.

        Underlying Java method: PApplet.text

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
            missing variable description

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

        Draws text to the screen. Displays the information specified in the first
        parameter on the screen in the position specified by the additional parameters.
        A default font will be used unless a font is set with the ``text_font()``
        function and a default size will be used unless a font is set with
        ``text_size()``. Change the color of the text with the ``fill()`` function. The
        text displays in relation to the ``text_align()`` function, which gives the
        option to draw to the left, right, and center of the coordinates.

        The ``x2`` and ``y2`` parameters define a rectangular area to display within and
        may only be used with string data. When these parameters are specified, they are
        interpreted based on the current ``rect_mode()`` setting. Text that does not fit
        completely within the rectangle specified will not be drawn to the screen.

        Note that Processing now lets you call ``text()`` without first specifying a
        PFont with ``text_font()``. In that case, a generic sans-serif font will be used
        instead. (See the third example above.)
        """
        pass

    @overload
    def text(self, chars: List[chr], start: int,
             stop: int, x: float, y: float, z: float, /) -> None:
        """Draws text to the screen.

        Underlying Java method: PApplet.text

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
            missing variable description

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

        Draws text to the screen. Displays the information specified in the first
        parameter on the screen in the position specified by the additional parameters.
        A default font will be used unless a font is set with the ``text_font()``
        function and a default size will be used unless a font is set with
        ``text_size()``. Change the color of the text with the ``fill()`` function. The
        text displays in relation to the ``text_align()`` function, which gives the
        option to draw to the left, right, and center of the coordinates.

        The ``x2`` and ``y2`` parameters define a rectangular area to display within and
        may only be used with string data. When these parameters are specified, they are
        interpreted based on the current ``rect_mode()`` setting. Text that does not fit
        completely within the rectangle specified will not be drawn to the screen.

        Note that Processing now lets you call ``text()`` without first specifying a
        PFont with ``text_font()``. In that case, a generic sans-serif font will be used
        instead. (See the third example above.)
        """
        pass

    @overload
    def text(self, num: float, x: float, y: float, /) -> None:
        """Draws text to the screen.

        Underlying Java method: PApplet.text

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
            missing variable description

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

        Draws text to the screen. Displays the information specified in the first
        parameter on the screen in the position specified by the additional parameters.
        A default font will be used unless a font is set with the ``text_font()``
        function and a default size will be used unless a font is set with
        ``text_size()``. Change the color of the text with the ``fill()`` function. The
        text displays in relation to the ``text_align()`` function, which gives the
        option to draw to the left, right, and center of the coordinates.

        The ``x2`` and ``y2`` parameters define a rectangular area to display within and
        may only be used with string data. When these parameters are specified, they are
        interpreted based on the current ``rect_mode()`` setting. Text that does not fit
        completely within the rectangle specified will not be drawn to the screen.

        Note that Processing now lets you call ``text()`` without first specifying a
        PFont with ``text_font()``. In that case, a generic sans-serif font will be used
        instead. (See the third example above.)
        """
        pass

    @overload
    def text(self, num: float, x: float, y: float, z: float, /) -> None:
        """Draws text to the screen.

        Underlying Java method: PApplet.text

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
            missing variable description

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

        Draws text to the screen. Displays the information specified in the first
        parameter on the screen in the position specified by the additional parameters.
        A default font will be used unless a font is set with the ``text_font()``
        function and a default size will be used unless a font is set with
        ``text_size()``. Change the color of the text with the ``fill()`` function. The
        text displays in relation to the ``text_align()`` function, which gives the
        option to draw to the left, right, and center of the coordinates.

        The ``x2`` and ``y2`` parameters define a rectangular area to display within and
        may only be used with string data. When these parameters are specified, they are
        interpreted based on the current ``rect_mode()`` setting. Text that does not fit
        completely within the rectangle specified will not be drawn to the screen.

        Note that Processing now lets you call ``text()`` without first specifying a
        PFont with ``text_font()``. In that case, a generic sans-serif font will be used
        instead. (See the third example above.)
        """
        pass

    @overload
    def text(self, num: int, x: float, y: float, /) -> None:
        """Draws text to the screen.

        Underlying Java method: PApplet.text

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
            missing variable description

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

        Draws text to the screen. Displays the information specified in the first
        parameter on the screen in the position specified by the additional parameters.
        A default font will be used unless a font is set with the ``text_font()``
        function and a default size will be used unless a font is set with
        ``text_size()``. Change the color of the text with the ``fill()`` function. The
        text displays in relation to the ``text_align()`` function, which gives the
        option to draw to the left, right, and center of the coordinates.

        The ``x2`` and ``y2`` parameters define a rectangular area to display within and
        may only be used with string data. When these parameters are specified, they are
        interpreted based on the current ``rect_mode()`` setting. Text that does not fit
        completely within the rectangle specified will not be drawn to the screen.

        Note that Processing now lets you call ``text()`` without first specifying a
        PFont with ``text_font()``. In that case, a generic sans-serif font will be used
        instead. (See the third example above.)
        """
        pass

    @overload
    def text(self, num: int, x: float, y: float, z: float, /) -> None:
        """Draws text to the screen.

        Underlying Java method: PApplet.text

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
            missing variable description

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

        Draws text to the screen. Displays the information specified in the first
        parameter on the screen in the position specified by the additional parameters.
        A default font will be used unless a font is set with the ``text_font()``
        function and a default size will be used unless a font is set with
        ``text_size()``. Change the color of the text with the ``fill()`` function. The
        text displays in relation to the ``text_align()`` function, which gives the
        option to draw to the left, right, and center of the coordinates.

        The ``x2`` and ``y2`` parameters define a rectangular area to display within and
        may only be used with string data. When these parameters are specified, they are
        interpreted based on the current ``rect_mode()`` setting. Text that does not fit
        completely within the rectangle specified will not be drawn to the screen.

        Note that Processing now lets you call ``text()`` without first specifying a
        PFont with ``text_font()``. In that case, a generic sans-serif font will be used
        instead. (See the third example above.)
        """
        pass

    @overload
    def text(self, str: str, x: float, y: float, /) -> None:
        """Draws text to the screen.

        Underlying Java method: PApplet.text

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
            missing variable description

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

        Draws text to the screen. Displays the information specified in the first
        parameter on the screen in the position specified by the additional parameters.
        A default font will be used unless a font is set with the ``text_font()``
        function and a default size will be used unless a font is set with
        ``text_size()``. Change the color of the text with the ``fill()`` function. The
        text displays in relation to the ``text_align()`` function, which gives the
        option to draw to the left, right, and center of the coordinates.

        The ``x2`` and ``y2`` parameters define a rectangular area to display within and
        may only be used with string data. When these parameters are specified, they are
        interpreted based on the current ``rect_mode()`` setting. Text that does not fit
        completely within the rectangle specified will not be drawn to the screen.

        Note that Processing now lets you call ``text()`` without first specifying a
        PFont with ``text_font()``. In that case, a generic sans-serif font will be used
        instead. (See the third example above.)
        """
        pass

    @overload
    def text(self, str: str, x: float, y: float, z: float, /) -> None:
        """Draws text to the screen.

        Underlying Java method: PApplet.text

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
            missing variable description

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

        Draws text to the screen. Displays the information specified in the first
        parameter on the screen in the position specified by the additional parameters.
        A default font will be used unless a font is set with the ``text_font()``
        function and a default size will be used unless a font is set with
        ``text_size()``. Change the color of the text with the ``fill()`` function. The
        text displays in relation to the ``text_align()`` function, which gives the
        option to draw to the left, right, and center of the coordinates.

        The ``x2`` and ``y2`` parameters define a rectangular area to display within and
        may only be used with string data. When these parameters are specified, they are
        interpreted based on the current ``rect_mode()`` setting. Text that does not fit
        completely within the rectangle specified will not be drawn to the screen.

        Note that Processing now lets you call ``text()`` without first specifying a
        PFont with ``text_font()``. In that case, a generic sans-serif font will be used
        instead. (See the third example above.)
        """
        pass

    @overload
    def text(self, str: str, x1: float, y1: float,
             x2: float, y2: float, /) -> None:
        """Draws text to the screen.

        Underlying Java method: PApplet.text

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
            missing variable description

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

        Draws text to the screen. Displays the information specified in the first
        parameter on the screen in the position specified by the additional parameters.
        A default font will be used unless a font is set with the ``text_font()``
        function and a default size will be used unless a font is set with
        ``text_size()``. Change the color of the text with the ``fill()`` function. The
        text displays in relation to the ``text_align()`` function, which gives the
        option to draw to the left, right, and center of the coordinates.

        The ``x2`` and ``y2`` parameters define a rectangular area to display within and
        may only be used with string data. When these parameters are specified, they are
        interpreted based on the current ``rect_mode()`` setting. Text that does not fit
        completely within the rectangle specified will not be drawn to the screen.

        Note that Processing now lets you call ``text()`` without first specifying a
        PFont with ``text_font()``. In that case, a generic sans-serif font will be used
        instead. (See the third example above.)
        """
        pass

    @_text_fix_str
    def text(self, *args):
        """Draws text to the screen.

        Underlying Java method: PApplet.text

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
            missing variable description

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

        Draws text to the screen. Displays the information specified in the first
        parameter on the screen in the position specified by the additional parameters.
        A default font will be used unless a font is set with the ``text_font()``
        function and a default size will be used unless a font is set with
        ``text_size()``. Change the color of the text with the ``fill()`` function. The
        text displays in relation to the ``text_align()`` function, which gives the
        option to draw to the left, right, and center of the coordinates.

        The ``x2`` and ``y2`` parameters define a rectangular area to display within and
        may only be used with string data. When these parameters are specified, they are
        interpreted based on the current ``rect_mode()`` setting. Text that does not fit
        completely within the rectangle specified will not be drawn to the screen.

        Note that Processing now lets you call ``text()`` without first specifying a
        PFont with ``text_font()``. In that case, a generic sans-serif font will be used
        instead. (See the third example above.)
        """
        return self._instance.text(*args)

    @overload
    def text_align(self, align_x: int, /) -> None:
        """Sets the current alignment for drawing text.

        Underlying Java method: PApplet.textAlign

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

        Sets the current alignment for drawing text. The parameters LEFT, CENTER, and
        RIGHT set the display characteristics of the letters in relation to the values
        for the ``x`` and ``y`` parameters of the ``text()`` function.

        An optional second parameter can be used to vertically align the text. BASELINE
        is the default, and the vertical alignment will be reset to BASELINE if the
        second parameter is not used. The TOP and CENTER parameters are straightforward.
        The BOTTOM parameter offsets the line based on the current ``text_descent()``.
        For multiple lines, the final line will be aligned to the bottom, with the
        previous lines appearing above it.

        When using ``text()`` with width and height parameters, BASELINE is ignored, and
        treated as TOP. (Otherwise, text would by default draw outside the box, since
        BASELINE is the default setting. BASELINE is not a useful drawing mode for text
        drawn in a rectangle.)

        The vertical alignment is based on the value of ``text_ascent()``, which many
        fonts do not specify correctly. It may be necessary to use a hack and offset by
        a few pixels by hand so that the offset looks correct. To do this as less of a
        hack, use some percentage of ``text_ascent()`` or ``text_descent()`` so that the
        hack works even if you change the size of the font.
        """
        pass

    @overload
    def text_align(self, align_x: int, align_y: int, /) -> None:
        """Sets the current alignment for drawing text.

        Underlying Java method: PApplet.textAlign

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

        Sets the current alignment for drawing text. The parameters LEFT, CENTER, and
        RIGHT set the display characteristics of the letters in relation to the values
        for the ``x`` and ``y`` parameters of the ``text()`` function.

        An optional second parameter can be used to vertically align the text. BASELINE
        is the default, and the vertical alignment will be reset to BASELINE if the
        second parameter is not used. The TOP and CENTER parameters are straightforward.
        The BOTTOM parameter offsets the line based on the current ``text_descent()``.
        For multiple lines, the final line will be aligned to the bottom, with the
        previous lines appearing above it.

        When using ``text()`` with width and height parameters, BASELINE is ignored, and
        treated as TOP. (Otherwise, text would by default draw outside the box, since
        BASELINE is the default setting. BASELINE is not a useful drawing mode for text
        drawn in a rectangle.)

        The vertical alignment is based on the value of ``text_ascent()``, which many
        fonts do not specify correctly. It may be necessary to use a hack and offset by
        a few pixels by hand so that the offset looks correct. To do this as less of a
        hack, use some percentage of ``text_ascent()`` or ``text_descent()`` so that the
        hack works even if you change the size of the font.
        """
        pass

    def text_align(self, *args):
        """Sets the current alignment for drawing text.

        Underlying Java method: PApplet.textAlign

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

        Sets the current alignment for drawing text. The parameters LEFT, CENTER, and
        RIGHT set the display characteristics of the letters in relation to the values
        for the ``x`` and ``y`` parameters of the ``text()`` function.

        An optional second parameter can be used to vertically align the text. BASELINE
        is the default, and the vertical alignment will be reset to BASELINE if the
        second parameter is not used. The TOP and CENTER parameters are straightforward.
        The BOTTOM parameter offsets the line based on the current ``text_descent()``.
        For multiple lines, the final line will be aligned to the bottom, with the
        previous lines appearing above it.

        When using ``text()`` with width and height parameters, BASELINE is ignored, and
        treated as TOP. (Otherwise, text would by default draw outside the box, since
        BASELINE is the default setting. BASELINE is not a useful drawing mode for text
        drawn in a rectangle.)

        The vertical alignment is based on the value of ``text_ascent()``, which many
        fonts do not specify correctly. It may be necessary to use a hack and offset by
        a few pixels by hand so that the offset looks correct. To do this as less of a
        hack, use some percentage of ``text_ascent()`` or ``text_descent()`` so that the
        hack works even if you change the size of the font.
        """
        return self._instance.textAlign(*args)

    def text_ascent(self) -> float:
        """Returns ascent of the current font at its current size.

        Underlying Java method: PApplet.textAscent

        Notes
        -----

        Returns ascent of the current font at its current size. This information is
        useful for determining the height of the font above the baseline.
        """
        return self._instance.textAscent()

    def text_descent(self) -> float:
        """Returns descent of the current font at its current size.

        Underlying Java method: PApplet.textDescent

        Notes
        -----

        Returns descent of the current font at its current size. This information is
        useful for determining the height of the font below the baseline.
        """
        return self._instance.textDescent()

    @overload
    def text_font(self, which: Py5Font, /) -> None:
        """Sets the current font that will be drawn with the ``text()`` function.

        Underlying Java method: PApplet.textFont

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
            any variable of the type PFont

        Notes
        -----

        Sets the current font that will be drawn with the ``text()`` function. Fonts
        must be created for Processing with ``create_font()`` or loaded with
        ``load_font()`` before they can be used. The font set through ``text_font()``
        will be used in all subsequent calls to the ``text()`` function. If no ``size``
        parameter is specified, the font size defaults to the original size (the size in
        which it was created with the "Create Font..." tool) overriding any previous
        calls to ``text_font()`` or ``text_size()``.
         When fonts are rendered as an image texture (as is the case with the P2D and
        P3D renderers as well as with ``load_font()`` and vlw files), you should create
        fonts at the sizes that will be used most commonly. Using ``text_font()``
        without the size parameter will result in the cleanest type.
        """
        pass

    @overload
    def text_font(self, which: Py5Font, size: float, /) -> None:
        """Sets the current font that will be drawn with the ``text()`` function.

        Underlying Java method: PApplet.textFont

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
            any variable of the type PFont

        Notes
        -----

        Sets the current font that will be drawn with the ``text()`` function. Fonts
        must be created for Processing with ``create_font()`` or loaded with
        ``load_font()`` before they can be used. The font set through ``text_font()``
        will be used in all subsequent calls to the ``text()`` function. If no ``size``
        parameter is specified, the font size defaults to the original size (the size in
        which it was created with the "Create Font..." tool) overriding any previous
        calls to ``text_font()`` or ``text_size()``.
         When fonts are rendered as an image texture (as is the case with the P2D and
        P3D renderers as well as with ``load_font()`` and vlw files), you should create
        fonts at the sizes that will be used most commonly. Using ``text_font()``
        without the size parameter will result in the cleanest type.
        """
        pass

    def text_font(self, *args):
        """Sets the current font that will be drawn with the ``text()`` function.

        Underlying Java method: PApplet.textFont

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
            any variable of the type PFont

        Notes
        -----

        Sets the current font that will be drawn with the ``text()`` function. Fonts
        must be created for Processing with ``create_font()`` or loaded with
        ``load_font()`` before they can be used. The font set through ``text_font()``
        will be used in all subsequent calls to the ``text()`` function. If no ``size``
        parameter is specified, the font size defaults to the original size (the size in
        which it was created with the "Create Font..." tool) overriding any previous
        calls to ``text_font()`` or ``text_size()``.
         When fonts are rendered as an image texture (as is the case with the P2D and
        P3D renderers as well as with ``load_font()`` and vlw files), you should create
        fonts at the sizes that will be used most commonly. Using ``text_font()``
        without the size parameter will result in the cleanest type.
        """
        return self._instance.textFont(*args)

    def text_leading(self, leading: float, /) -> None:
        """Sets the spacing between lines of text in units of pixels.

        Underlying Java method: PApplet.textLeading

        Parameters
        ----------

        leading: float
            the size in pixels for spacing between lines

        Notes
        -----

        Sets the spacing between lines of text in units of pixels. This setting will be
        used in all subsequent calls to the ``text()`` function.  Note, however, that
        the leading is reset by ``text_size()``. For example, if the leading is set to
        20 with ``text_leading(20)``, then if ``text_size(48)`` is run at a later point,
        the leading will be reset to the default for the text size of 48.
        """
        return self._instance.textLeading(leading)

    def text_mode(self, mode: int, /) -> None:
        """Sets the way text draws to the screen, either as texture maps or as vector
        geometry.

        Underlying Java method: PApplet.textMode

        Parameters
        ----------

        mode: int
            either MODEL or SHAPE

        Notes
        -----

        Sets the way text draws to the screen, either as texture maps or as vector
        geometry. The default ``text_mode(MODEL)``, uses textures to render the fonts.
        The ``text_mode(SHAPE)`` mode draws text using the glyph outlines of individual
        characters rather than as textures. This mode is only supported with the ``PDF``
        and ``P3D`` renderer settings. With the ``PDF`` renderer, you must call
        ``text_mode(SHAPE)`` before any other drawing occurs. If the outlines are not
        available, then ``text_mode(SHAPE)`` will be ignored and ``text_mode(MODEL)``
        will be used instead.

        The ``text_mode(SHAPE)`` option in ``P3D`` can be combined with ``begin_raw()``
        to write vector-accurate text to 2D and 3D output files, for instance ``DXF`` or
        ``PDF``. The ``SHAPE`` mode is not currently optimized for ``P3D``, so if
        recording shape data, use ``text_mode(MODEL)`` until you're ready to capture the
        geometry with ``begin_raw()``.
        """
        return self._instance.textMode(mode)

    def text_size(self, size: float, /) -> None:
        """Sets the current font size.

        Underlying Java method: PApplet.textSize

        Parameters
        ----------

        size: float
            the size of the letters in units of pixels

        Notes
        -----

        Sets the current font size. This size will be used in all subsequent calls to
        the ``text()`` function. Font size is measured in units of pixels.
        """
        return self._instance.textSize(size)

    @overload
    def text_width(self, c: chr, /) -> float:
        """Calculates and returns the width of any character or text string.

        Underlying Java method: PApplet.textWidth

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
            missing variable description

        length: int
            missing variable description

        start: int
            missing variable description

        str: str
            the String of characters to measure

        Notes
        -----

        Calculates and returns the width of any character or text string.
        """
        pass

    @overload
    def text_width(self, chars: List[chr],
                   start: int, length: int, /) -> float:
        """Calculates and returns the width of any character or text string.

        Underlying Java method: PApplet.textWidth

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
            missing variable description

        length: int
            missing variable description

        start: int
            missing variable description

        str: str
            the String of characters to measure

        Notes
        -----

        Calculates and returns the width of any character or text string.
        """
        pass

    @overload
    def text_width(self, str: str, /) -> float:
        """Calculates and returns the width of any character or text string.

        Underlying Java method: PApplet.textWidth

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
            missing variable description

        length: int
            missing variable description

        start: int
            missing variable description

        str: str
            the String of characters to measure

        Notes
        -----

        Calculates and returns the width of any character or text string.
        """
        pass

    @_text_fix_str
    def text_width(self, *args):
        """Calculates and returns the width of any character or text string.

        Underlying Java method: PApplet.textWidth

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
            missing variable description

        length: int
            missing variable description

        start: int
            missing variable description

        str: str
            the String of characters to measure

        Notes
        -----

        Calculates and returns the width of any character or text string.
        """
        return self._instance.textWidth(*args)

    def texture(self, image: Py5Image, /) -> None:
        """Sets a texture to be applied to vertex points.

        Underlying Java method: PApplet.texture

        Parameters
        ----------

        image: Py5Image
            reference to a PImage object

        Notes
        -----

        Sets a texture to be applied to vertex points. The ``texture()`` function must
        be called between ``begin_shape()`` and ``end_shape()`` and before any calls to
        ``vertex()``. This function only works with the P2D and P3D renderers.

        When textures are in use, the fill color is ignored. Instead, use ``tint()`` to
        specify the color of the texture as it is applied to the shape.
        """
        return self._instance.texture(image)

    def texture_mode(self, mode: int, /) -> None:
        """Sets the coordinate space for texture mapping.

        Underlying Java method: PApplet.textureMode

        Parameters
        ----------

        mode: int
            either IMAGE or NORMAL

        Notes
        -----

        Sets the coordinate space for texture mapping. The default mode is ``IMAGE``,
        which refers to the actual coordinates of the image. ``NORMAL`` refers to a
        normalized space of values ranging from 0 to 1. This function only works with
        the P2D and P3D renderers.

        With ``IMAGE``, if an image is 100 x 200 pixels, mapping the image onto the
        entire size of a quad would require the points (0,0) (100, 0) (100,200) (0,200).
        The same mapping in ``NORMAL`` is (0,0) (1,0) (1,1) (0,1).
        """
        return self._instance.textureMode(mode)

    def texture_wrap(self, wrap: int, /) -> None:
        """Defines if textures repeat or draw once within a texture map.

        Underlying Java method: PApplet.textureWrap

        Parameters
        ----------

        wrap: int
            Either CLAMP (default) or REPEAT

        Notes
        -----

        Defines if textures repeat or draw once within a texture map. The two parameters
        are CLAMP (the default behavior) and REPEAT. This function only works with the
        P2D and P3D renderers.
        """
        return self._instance.textureWrap(wrap)

    @overload
    def tint(self, gray: float, /) -> None:
        """Sets the fill value for displaying images.

        Underlying Java method: PApplet.tint

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
        can be changed with ``color_mode()``).

        When using hexadecimal notation to specify a color, use "``#``" or "``0x``"
        before the values (e.g., ``0xCCFFAA`` or ``0xFFCCFFAA``). The ``#`` syntax uses
        six digits to specify a color (just as colors are typically specified in HTML
        and CSS). When using the hexadecimal notation starting with "``0x``", the
        hexadecimal value must be specified with eight characters; the first two
        characters define the alpha component, and the remainder define the red, green,
        and blue components.

        The value for the gray parameter must be less than or equal to the current
        maximum value as specified by ``color_mode()``. The default maximum value is
        255.

        The ``tint()`` function is also used to control the coloring of textures in 3D.
        """
        pass

    @overload
    def tint(self, gray: float, alpha: float, /) -> None:
        """Sets the fill value for displaying images.

        Underlying Java method: PApplet.tint

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
        can be changed with ``color_mode()``).

        When using hexadecimal notation to specify a color, use "``#``" or "``0x``"
        before the values (e.g., ``0xCCFFAA`` or ``0xFFCCFFAA``). The ``#`` syntax uses
        six digits to specify a color (just as colors are typically specified in HTML
        and CSS). When using the hexadecimal notation starting with "``0x``", the
        hexadecimal value must be specified with eight characters; the first two
        characters define the alpha component, and the remainder define the red, green,
        and blue components.

        The value for the gray parameter must be less than or equal to the current
        maximum value as specified by ``color_mode()``. The default maximum value is
        255.

        The ``tint()`` function is also used to control the coloring of textures in 3D.
        """
        pass

    @overload
    def tint(self, v1: float, v2: float, v3: float, /) -> None:
        """Sets the fill value for displaying images.

        Underlying Java method: PApplet.tint

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
        can be changed with ``color_mode()``).

        When using hexadecimal notation to specify a color, use "``#``" or "``0x``"
        before the values (e.g., ``0xCCFFAA`` or ``0xFFCCFFAA``). The ``#`` syntax uses
        six digits to specify a color (just as colors are typically specified in HTML
        and CSS). When using the hexadecimal notation starting with "``0x``", the
        hexadecimal value must be specified with eight characters; the first two
        characters define the alpha component, and the remainder define the red, green,
        and blue components.

        The value for the gray parameter must be less than or equal to the current
        maximum value as specified by ``color_mode()``. The default maximum value is
        255.

        The ``tint()`` function is also used to control the coloring of textures in 3D.
        """
        pass

    @overload
    def tint(self, v1: float, v2: float, v3: float, alpha: float, /) -> None:
        """Sets the fill value for displaying images.

        Underlying Java method: PApplet.tint

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
        can be changed with ``color_mode()``).

        When using hexadecimal notation to specify a color, use "``#``" or "``0x``"
        before the values (e.g., ``0xCCFFAA`` or ``0xFFCCFFAA``). The ``#`` syntax uses
        six digits to specify a color (just as colors are typically specified in HTML
        and CSS). When using the hexadecimal notation starting with "``0x``", the
        hexadecimal value must be specified with eight characters; the first two
        characters define the alpha component, and the remainder define the red, green,
        and blue components.

        The value for the gray parameter must be less than or equal to the current
        maximum value as specified by ``color_mode()``. The default maximum value is
        255.

        The ``tint()`` function is also used to control the coloring of textures in 3D.
        """
        pass

    @overload
    def tint(self, rgb: int, /) -> None:
        """Sets the fill value for displaying images.

        Underlying Java method: PApplet.tint

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
        can be changed with ``color_mode()``).

        When using hexadecimal notation to specify a color, use "``#``" or "``0x``"
        before the values (e.g., ``0xCCFFAA`` or ``0xFFCCFFAA``). The ``#`` syntax uses
        six digits to specify a color (just as colors are typically specified in HTML
        and CSS). When using the hexadecimal notation starting with "``0x``", the
        hexadecimal value must be specified with eight characters; the first two
        characters define the alpha component, and the remainder define the red, green,
        and blue components.

        The value for the gray parameter must be less than or equal to the current
        maximum value as specified by ``color_mode()``. The default maximum value is
        255.

        The ``tint()`` function is also used to control the coloring of textures in 3D.
        """
        pass

    @overload
    def tint(self, rgb: int, alpha: float, /) -> None:
        """Sets the fill value for displaying images.

        Underlying Java method: PApplet.tint

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
        can be changed with ``color_mode()``).

        When using hexadecimal notation to specify a color, use "``#``" or "``0x``"
        before the values (e.g., ``0xCCFFAA`` or ``0xFFCCFFAA``). The ``#`` syntax uses
        six digits to specify a color (just as colors are typically specified in HTML
        and CSS). When using the hexadecimal notation starting with "``0x``", the
        hexadecimal value must be specified with eight characters; the first two
        characters define the alpha component, and the remainder define the red, green,
        and blue components.

        The value for the gray parameter must be less than or equal to the current
        maximum value as specified by ``color_mode()``. The default maximum value is
        255.

        The ``tint()`` function is also used to control the coloring of textures in 3D.
        """
        pass

    def tint(self, *args):
        """Sets the fill value for displaying images.

        Underlying Java method: PApplet.tint

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
        can be changed with ``color_mode()``).

        When using hexadecimal notation to specify a color, use "``#``" or "``0x``"
        before the values (e.g., ``0xCCFFAA`` or ``0xFFCCFFAA``). The ``#`` syntax uses
        six digits to specify a color (just as colors are typically specified in HTML
        and CSS). When using the hexadecimal notation starting with "``0x``", the
        hexadecimal value must be specified with eight characters; the first two
        characters define the alpha component, and the remainder define the red, green,
        and blue components.

        The value for the gray parameter must be less than or equal to the current
        maximum value as specified by ``color_mode()``. The default maximum value is
        255.

        The ``tint()`` function is also used to control the coloring of textures in 3D.
        """
        return self._instance.tint(*args)

    @overload
    def translate(self, x: float, y: float, /) -> None:
        """Specifies an amount to displace objects within the display window.

        Underlying Java method: PApplet.translate

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

        Specifies an amount to displace objects within the display window. The ``x``
        parameter specifies left/right translation, the ``y`` parameter specifies
        up/down translation, and the ``z`` parameter specifies translations toward/away
        from the screen. Using this function with the ``z`` parameter requires using P3D
        as a parameter in combination with size as shown in the above example.

        Transformations are cumulative and apply to everything that happens after and
        subsequent calls to the function accumulates the effect. For example, calling
        ``translate(50, 0)`` and then ``translate(20, 0)`` is the same as
        ``translate(70, 0)``. If ``translate()`` is called within ``draw()``, the
        transformation is reset when the loop begins again. This function can be further
        controlled by using ``push_matrix()`` and ``pop_matrix()``.
        """
        pass

    @overload
    def translate(self, x: float, y: float, z: float, /) -> None:
        """Specifies an amount to displace objects within the display window.

        Underlying Java method: PApplet.translate

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

        Specifies an amount to displace objects within the display window. The ``x``
        parameter specifies left/right translation, the ``y`` parameter specifies
        up/down translation, and the ``z`` parameter specifies translations toward/away
        from the screen. Using this function with the ``z`` parameter requires using P3D
        as a parameter in combination with size as shown in the above example.

        Transformations are cumulative and apply to everything that happens after and
        subsequent calls to the function accumulates the effect. For example, calling
        ``translate(50, 0)`` and then ``translate(20, 0)`` is the same as
        ``translate(70, 0)``. If ``translate()`` is called within ``draw()``, the
        transformation is reset when the loop begins again. This function can be further
        controlled by using ``push_matrix()`` and ``pop_matrix()``.
        """
        pass

    def translate(self, *args):
        """Specifies an amount to displace objects within the display window.

        Underlying Java method: PApplet.translate

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

        Specifies an amount to displace objects within the display window. The ``x``
        parameter specifies left/right translation, the ``y`` parameter specifies
        up/down translation, and the ``z`` parameter specifies translations toward/away
        from the screen. Using this function with the ``z`` parameter requires using P3D
        as a parameter in combination with size as shown in the above example.

        Transformations are cumulative and apply to everything that happens after and
        subsequent calls to the function accumulates the effect. For example, calling
        ``translate(50, 0)`` and then ``translate(20, 0)`` is the same as
        ``translate(70, 0)``. If ``translate()`` is called within ``draw()``, the
        transformation is reset when the loop begins again. This function can be further
        controlled by using ``push_matrix()`` and ``pop_matrix()``.
        """
        return self._instance.translate(*args)

    def triangle(self, x1: float, y1: float, x2: float,
                 y2: float, x3: float, y3: float, /) -> None:
        """A triangle is a plane created by connecting three points.

        Underlying Java method: PApplet.triangle

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
        """
        return self._instance.triangle(x1, y1, x2, y2, x3, y3)

    @overload
    def update_pixels(self) -> None:
        """Updates the display window with the data in the ``pixels[]`` array.

        Underlying Java method: PApplet.updatePixels

        Methods
        -------

        You can use any of the following signatures:

         * update_pixels() -> None
         * update_pixels(x1: int, y1: int, x2: int, y2: int, /) -> None

        Parameters
        ----------

        x1: int
            x-coordinate of the upper-left corner

        x2: int
            width of the region

        y1: int
            y-coordinate of the upper-left corner

        y2: int
            height of the region

        Notes
        -----

        Updates the display window with the data in the ``pixels[]`` array. Use in
        conjunction with ``load_pixels()``. If you're only reading pixels from the
        array, there's no need to call ``update_pixels()`` — updating is only necessary
        to apply changes.
        """
        pass

    @overload
    def update_pixels(self, x: int, y: int, w: int, h: int, /) -> None:
        """Updates the display window with the data in the ``pixels[]`` array.

        Underlying Java method: PApplet.updatePixels

        Methods
        -------

        You can use any of the following signatures:

         * update_pixels() -> None
         * update_pixels(x1: int, y1: int, x2: int, y2: int, /) -> None

        Parameters
        ----------

        x1: int
            x-coordinate of the upper-left corner

        x2: int
            width of the region

        y1: int
            y-coordinate of the upper-left corner

        y2: int
            height of the region

        Notes
        -----

        Updates the display window with the data in the ``pixels[]`` array. Use in
        conjunction with ``load_pixels()``. If you're only reading pixels from the
        array, there's no need to call ``update_pixels()`` — updating is only necessary
        to apply changes.
        """
        pass

    def update_pixels(self, *args):
        """Updates the display window with the data in the ``pixels[]`` array.

        Underlying Java method: PApplet.updatePixels

        Methods
        -------

        You can use any of the following signatures:

         * update_pixels() -> None
         * update_pixels(x1: int, y1: int, x2: int, y2: int, /) -> None

        Parameters
        ----------

        x1: int
            x-coordinate of the upper-left corner

        x2: int
            width of the region

        y1: int
            y-coordinate of the upper-left corner

        y2: int
            height of the region

        Notes
        -----

        Updates the display window with the data in the ``pixels[]`` array. Use in
        conjunction with ``load_pixels()``. If you're only reading pixels from the
        array, there's no need to call ``update_pixels()`` — updating is only necessary
        to apply changes.
        """
        return self._instance.updatePixels(*args)

    @overload
    def vertex(self, x: float, y: float, /) -> None:
        """All shapes are constructed by connecting a series of vertices.

        Underlying Java method: PApplet.vertex

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

        All shapes are constructed by connecting a series of vertices. ``vertex()`` is
        used to specify the vertex coordinates for points, lines, triangles, quads, and
        polygons. It is used exclusively within the ``begin_shape()`` and
        ``end_shape()`` functions.

        Drawing a vertex in 3D using the ``z`` parameter requires the P3D parameter in
        combination with size, as shown in the above example.

        This function is also used to map a texture onto geometry. The ``texture()``
        function declares the texture to apply to the geometry and the ``u`` and ``v``
        coordinates set define the mapping of this texture to the form. By default, the
        coordinates used for ``u`` and ``v`` are specified in relation to the image's
        size in pixels, but this relation can be changed with ``texture_mode()``.
        """
        pass

    @overload
    def vertex(self, x: float, y: float, z: float, /) -> None:
        """All shapes are constructed by connecting a series of vertices.

        Underlying Java method: PApplet.vertex

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

        All shapes are constructed by connecting a series of vertices. ``vertex()`` is
        used to specify the vertex coordinates for points, lines, triangles, quads, and
        polygons. It is used exclusively within the ``begin_shape()`` and
        ``end_shape()`` functions.

        Drawing a vertex in 3D using the ``z`` parameter requires the P3D parameter in
        combination with size, as shown in the above example.

        This function is also used to map a texture onto geometry. The ``texture()``
        function declares the texture to apply to the geometry and the ``u`` and ``v``
        coordinates set define the mapping of this texture to the form. By default, the
        coordinates used for ``u`` and ``v`` are specified in relation to the image's
        size in pixels, but this relation can be changed with ``texture_mode()``.
        """
        pass

    @overload
    def vertex(self, x: float, y: float, u: float, v: float, /) -> None:
        """All shapes are constructed by connecting a series of vertices.

        Underlying Java method: PApplet.vertex

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

        All shapes are constructed by connecting a series of vertices. ``vertex()`` is
        used to specify the vertex coordinates for points, lines, triangles, quads, and
        polygons. It is used exclusively within the ``begin_shape()`` and
        ``end_shape()`` functions.

        Drawing a vertex in 3D using the ``z`` parameter requires the P3D parameter in
        combination with size, as shown in the above example.

        This function is also used to map a texture onto geometry. The ``texture()``
        function declares the texture to apply to the geometry and the ``u`` and ``v``
        coordinates set define the mapping of this texture to the form. By default, the
        coordinates used for ``u`` and ``v`` are specified in relation to the image's
        size in pixels, but this relation can be changed with ``texture_mode()``.
        """
        pass

    @overload
    def vertex(self, x: float, y: float, z: float,
               u: float, v: float, /) -> None:
        """All shapes are constructed by connecting a series of vertices.

        Underlying Java method: PApplet.vertex

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

        All shapes are constructed by connecting a series of vertices. ``vertex()`` is
        used to specify the vertex coordinates for points, lines, triangles, quads, and
        polygons. It is used exclusively within the ``begin_shape()`` and
        ``end_shape()`` functions.

        Drawing a vertex in 3D using the ``z`` parameter requires the P3D parameter in
        combination with size, as shown in the above example.

        This function is also used to map a texture onto geometry. The ``texture()``
        function declares the texture to apply to the geometry and the ``u`` and ``v``
        coordinates set define the mapping of this texture to the form. By default, the
        coordinates used for ``u`` and ``v`` are specified in relation to the image's
        size in pixels, but this relation can be changed with ``texture_mode()``.
        """
        pass

    @overload
    def vertex(self, v: NDArray[(Any,), Float], /) -> None:
        """All shapes are constructed by connecting a series of vertices.

        Underlying Java method: PApplet.vertex

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

        All shapes are constructed by connecting a series of vertices. ``vertex()`` is
        used to specify the vertex coordinates for points, lines, triangles, quads, and
        polygons. It is used exclusively within the ``begin_shape()`` and
        ``end_shape()`` functions.

        Drawing a vertex in 3D using the ``z`` parameter requires the P3D parameter in
        combination with size, as shown in the above example.

        This function is also used to map a texture onto geometry. The ``texture()``
        function declares the texture to apply to the geometry and the ``u`` and ``v``
        coordinates set define the mapping of this texture to the form. By default, the
        coordinates used for ``u`` and ``v`` are specified in relation to the image's
        size in pixels, but this relation can be changed with ``texture_mode()``.
        """
        pass

    def vertex(self, *args):
        """All shapes are constructed by connecting a series of vertices.

        Underlying Java method: PApplet.vertex

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

        All shapes are constructed by connecting a series of vertices. ``vertex()`` is
        used to specify the vertex coordinates for points, lines, triangles, quads, and
        polygons. It is used exclusively within the ``begin_shape()`` and
        ``end_shape()`` functions.

        Drawing a vertex in 3D using the ``z`` parameter requires the P3D parameter in
        combination with size, as shown in the above example.

        This function is also used to map a texture onto geometry. The ``texture()``
        function declares the texture to apply to the geometry and the ``u`` and ``v``
        coordinates set define the mapping of this texture to the form. By default, the
        coordinates used for ``u`` and ``v`` are specified in relation to the image's
        size in pixels, but this relation can be changed with ``texture_mode()``.
        """
        return self._instance.vertex(*args)
