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
# -*- coding: utf-8 -*-
"""
py5 makes Processing available to the CPython interpreter using JPype.
"""
import sys
from pathlib import Path
import inspect
from typing import overload, Any, Callable, Union, Dict, List, Tuple  # noqa
from nptyping import NDArray, Float, Int  # noqa

# import json  # noqa
import numpy as np  # noqa
from PIL import Image  # noqa
from jpype import JClass  # noqa
from jpype.types import JArray, JString, JFloat, JInt, JChar  # noqa

import py5_tools

if not py5_tools.is_jvm_running():
    base_path = Path(
        getattr(
            sys,
            '_MEIPASS',
            Path(__file__).absolute().parent))
    # add py5 jars to the classpath first
    py5_tools.add_jars(str(base_path / 'jars'))
    # if the cwd has a jars subdirectory, add that next
    py5_tools.add_jars(Path('jars'))
    py5_tools.jvm._start_jvm()

from .methods import register_exception_msg  # noqa
from .sketch import Sketch, Py5Surface, Py5Graphics, Py5Image, Py5Shader, Py5Shape, Py5Font, Py5Promise, _in_ipython_session  # noqa
from .render_helper import render_frame, render_frame_sequence, render, render_sequence  # noqa
from .create_font_tool import create_font_file  # noqa
from .image_conversion import register_image_conversion, NumpyImageArray  # noqa
from . import reference
from . import java_conversion  # noqa
try:
    from py5_tools.magics import load_ipython_extension  # noqa
except ModuleNotFoundError:
    # IPython must not be installed
    pass


__version__ = '0.4a2'

_PY5_USE_IMPORTED_MODE = py5_tools.imported.get_imported_mode()

java_conversion.init_jpype_converters()


_py5sketch = Sketch()


ADD = 2
ALPHA = 4
ALT = 18
AMBIENT = 0
ARC = 32
ARGB = 2
ARGS_BGCOLOR = "--bgcolor"
ARGS_DENSITY = "--density"
ARGS_DISABLE_AWT = "--disable-awt"
ARGS_DISPLAY = "--display"
ARGS_EDITOR_LOCATION = "--editor-location"
ARGS_EXTERNAL = "--external"
ARGS_FULL_SCREEN = "--full-screen"
ARGS_HIDE_STOP = "--hide-stop"
ARGS_LOCATION = "--location"
ARGS_PRESENT = "--present"
ARGS_SKETCH_FOLDER = "--sketch-path"
ARGS_STOP_COLOR = "--stop-color"
ARGS_WINDOW_COLOR = "--window-color"
ARROW = 0
BACKSPACE = '\b'
BASELINE = 0
BEVEL = 32
BEZIER_VERTEX = 1
BLEND = 1
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
DEFAULT_HEIGHT = 100
DEFAULT_WIDTH = 100
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
EXTERNAL_MOVE = "__MOVE__"
EXTERNAL_STOP = "__STOP__"
FX2D = "processing.javafx.PGraphicsFX2D"
GIF = 3
GRAY = 12
GROUP = 0
HALF_PI = 1.5707964
HAND = 12
HARD_LIGHT = 1024
HIDDEN = "py5.core.graphics.HiddenPy5GraphicsJava2D"
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
args: List[str] = None
display_height: int = None
display_width: int = None
finished: bool = None
focused: bool = None
frame_count: int = None
height: int = None
java_platform: int = None
java_version_name: str = None
key: chr = None
key_code: int = None
mouse_button: int = None
mouse_x: int = None
mouse_y: int = None
pixel_height: int = None
pixel_width: int = None
pixels: NDArray[(Any,), Int] = None
pmouse_x: int = None
pmouse_y: int = None
width: int = None


def alpha(rgb: int, /) -> float:
    """Extracts the alpha value from a color, scaled to match current ``color_mode()``.

    Underlying Java method: PApplet.alpha

    Parameters
    ----------

    rgb: int
        any value of the color datatype

    Notes
    -----

    Extracts the alpha value from a color, scaled to match current ``color_mode()``.

    The ``alpha()`` function is easy to use and understand, but it is slower than a
    technique called bit shifting. When working in ``color_mode(RGB, 255)``, you can
    achieve the same results as ``alpha()`` but with greater speed by using the
    right shift operator (``>>``) with a bit mask. For example, ``alpha(c)`` and ``c
    >> 24 & 0xFF`` both extract the alpha value from a color variable ``c`` but the
    later is faster.
    """
    return _py5sketch.alpha(rgb)


@overload
def ambient(gray: float, /) -> None:
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
    with the ambient light component of the environment. The color components set
    through the parameters define the reflectance. For example in the default color
    mode, setting ``ambient(255, 127, 0)``, would cause all the red light to reflect
    and half of the green light to reflect. Use in combination with ``emissive()``,
    ``specular()``, and ``shininess()`` to set the material properties of shapes.
    """
    pass


@overload
def ambient(v1: float, v2: float, v3: float, /) -> None:
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
    with the ambient light component of the environment. The color components set
    through the parameters define the reflectance. For example in the default color
    mode, setting ``ambient(255, 127, 0)``, would cause all the red light to reflect
    and half of the green light to reflect. Use in combination with ``emissive()``,
    ``specular()``, and ``shininess()`` to set the material properties of shapes.
    """
    pass


@overload
def ambient(rgb: int, /) -> None:
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
    with the ambient light component of the environment. The color components set
    through the parameters define the reflectance. For example in the default color
    mode, setting ``ambient(255, 127, 0)``, would cause all the red light to reflect
    and half of the green light to reflect. Use in combination with ``emissive()``,
    ``specular()``, and ``shininess()`` to set the material properties of shapes.
    """
    pass


def ambient(*args):
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
    with the ambient light component of the environment. The color components set
    through the parameters define the reflectance. For example in the default color
    mode, setting ``ambient(255, 127, 0)``, would cause all the red light to reflect
    and half of the green light to reflect. Use in combination with ``emissive()``,
    ``specular()``, and ``shininess()`` to set the material properties of shapes.
    """
    return _py5sketch.ambient(*args)


@overload
def ambient_light(v1: float, v2: float, v3: float, /) -> None:
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
    and ``v3`` parameters are interpreted as either ``RGB`` or ``HSB`` values,
    depending on the current color mode.
    """
    pass


@overload
def ambient_light(v1: float, v2: float, v3: float,
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
    and ``v3`` parameters are interpreted as either ``RGB`` or ``HSB`` values,
    depending on the current color mode.
    """
    pass


def ambient_light(*args):
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
    and ``v3`` parameters are interpreted as either ``RGB`` or ``HSB`` values,
    depending on the current color mode.
    """
    return _py5sketch.ambient_light(*args)


@overload
def apply_matrix(n00: float, n01: float, n02: float,
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
        2D transformation matrix

    source: NDArray[(4, 4), Float]
        3D transformation matrix

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
        2D transformation matrix

    source: NDArray[(4, 4), Float]
        3D transformation matrix

    Notes
    -----

    Multiplies the current matrix by the one specified through the parameters. This
    is very slow because it will try to calculate the inverse of the transform, so
    avoid it whenever possible. The equivalent function in OpenGL is
    ``gl_mult_matrix()``.
    """
    pass


@overload
def apply_matrix(source: NDArray[(2, 3), Float], /) -> None:
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
        2D transformation matrix

    source: NDArray[(4, 4), Float]
        3D transformation matrix

    Notes
    -----

    Multiplies the current matrix by the one specified through the parameters. This
    is very slow because it will try to calculate the inverse of the transform, so
    avoid it whenever possible. The equivalent function in OpenGL is
    ``gl_mult_matrix()``.
    """
    pass


@overload
def apply_matrix(source: NDArray[(4, 4), Float], /) -> None:
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
        2D transformation matrix

    source: NDArray[(4, 4), Float]
        3D transformation matrix

    Notes
    -----

    Multiplies the current matrix by the one specified through the parameters. This
    is very slow because it will try to calculate the inverse of the transform, so
    avoid it whenever possible. The equivalent function in OpenGL is
    ``gl_mult_matrix()``.
    """
    pass


def apply_matrix(*args):
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
        2D transformation matrix

    source: NDArray[(4, 4), Float]
        3D transformation matrix

    Notes
    -----

    Multiplies the current matrix by the one specified through the parameters. This
    is very slow because it will try to calculate the inverse of the transform, so
    avoid it whenever possible. The equivalent function in OpenGL is
    ``gl_mult_matrix()``.
    """
    return _py5sketch.apply_matrix(*args)


@overload
def arc(a: float, b: float, c: float, d: float,
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
        arc drawing mode

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
    the optional seventh parameter. The three options, depicted in the examples, are
    ``PIE``, ``OPEN``, and ``CHORD``. The default mode is the ``OPEN`` stroke with a
    ``PIE`` fill.

    In some cases, the ``arc()`` function isn't accurate enough for smooth drawing.
    For example, the shape may jitter on screen when rotating slowly. If you're
    having an issue with how arcs are rendered, you'll need to draw the arc yourself
    with ``begin_shape()`` & ``end_shape()`` or a ``Py5Shape``.
    """
    pass


@overload
def arc(a: float, b: float, c: float, d: float,
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
        arc drawing mode

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
    the optional seventh parameter. The three options, depicted in the examples, are
    ``PIE``, ``OPEN``, and ``CHORD``. The default mode is the ``OPEN`` stroke with a
    ``PIE`` fill.

    In some cases, the ``arc()`` function isn't accurate enough for smooth drawing.
    For example, the shape may jitter on screen when rotating slowly. If you're
    having an issue with how arcs are rendered, you'll need to draw the arc yourself
    with ``begin_shape()`` & ``end_shape()`` or a ``Py5Shape``.
    """
    pass


def arc(*args):
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
        arc drawing mode

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
    the optional seventh parameter. The three options, depicted in the examples, are
    ``PIE``, ``OPEN``, and ``CHORD``. The default mode is the ``OPEN`` stroke with a
    ``PIE`` fill.

    In some cases, the ``arc()`` function isn't accurate enough for smooth drawing.
    For example, the shape may jitter on screen when rotating slowly. If you're
    having an issue with how arcs are rendered, you'll need to draw the arc yourself
    with ``begin_shape()`` & ``end_shape()`` or a ``Py5Shape``.
    """
    return _py5sketch.arc(*args)


@overload
def background(gray: float, /) -> None:
    """The ``background()`` function sets the color used for the background of the py5
    window.

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

    The ``background()`` function sets the color used for the background of the py5
    window. The default background is light gray. This function is typically used
    within ``draw()`` to clear the display window at the beginning of each frame,
    but it can be used inside ``setup()`` to set the background on the first frame
    of animation or if the backgound need only be set once.

    An image can also be used as the background for a Sketch, although the image's
    width and height must match that of the Sketch window. Images used with
    ``background()`` will ignore the current ``tint()`` setting. To resize an image
    to the size of the Sketch window, use ``image.resize(width, height)``.

    It is not possible to use the transparency ``alpha`` parameter with background
    colors on the main drawing surface. It can only be used along with a
    ``Py5Graphics`` object and ``create_graphics()``.
    """
    pass


@overload
def background(gray: float, alpha: float, /) -> None:
    """The ``background()`` function sets the color used for the background of the py5
    window.

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

    The ``background()`` function sets the color used for the background of the py5
    window. The default background is light gray. This function is typically used
    within ``draw()`` to clear the display window at the beginning of each frame,
    but it can be used inside ``setup()`` to set the background on the first frame
    of animation or if the backgound need only be set once.

    An image can also be used as the background for a Sketch, although the image's
    width and height must match that of the Sketch window. Images used with
    ``background()`` will ignore the current ``tint()`` setting. To resize an image
    to the size of the Sketch window, use ``image.resize(width, height)``.

    It is not possible to use the transparency ``alpha`` parameter with background
    colors on the main drawing surface. It can only be used along with a
    ``Py5Graphics`` object and ``create_graphics()``.
    """
    pass


@overload
def background(v1: float, v2: float, v3: float, /) -> None:
    """The ``background()`` function sets the color used for the background of the py5
    window.

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

    The ``background()`` function sets the color used for the background of the py5
    window. The default background is light gray. This function is typically used
    within ``draw()`` to clear the display window at the beginning of each frame,
    but it can be used inside ``setup()`` to set the background on the first frame
    of animation or if the backgound need only be set once.

    An image can also be used as the background for a Sketch, although the image's
    width and height must match that of the Sketch window. Images used with
    ``background()`` will ignore the current ``tint()`` setting. To resize an image
    to the size of the Sketch window, use ``image.resize(width, height)``.

    It is not possible to use the transparency ``alpha`` parameter with background
    colors on the main drawing surface. It can only be used along with a
    ``Py5Graphics`` object and ``create_graphics()``.
    """
    pass


@overload
def background(v1: float, v2: float, v3: float, alpha: float, /) -> None:
    """The ``background()`` function sets the color used for the background of the py5
    window.

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

    The ``background()`` function sets the color used for the background of the py5
    window. The default background is light gray. This function is typically used
    within ``draw()`` to clear the display window at the beginning of each frame,
    but it can be used inside ``setup()`` to set the background on the first frame
    of animation or if the backgound need only be set once.

    An image can also be used as the background for a Sketch, although the image's
    width and height must match that of the Sketch window. Images used with
    ``background()`` will ignore the current ``tint()`` setting. To resize an image
    to the size of the Sketch window, use ``image.resize(width, height)``.

    It is not possible to use the transparency ``alpha`` parameter with background
    colors on the main drawing surface. It can only be used along with a
    ``Py5Graphics`` object and ``create_graphics()``.
    """
    pass


@overload
def background(rgb: int, /) -> None:
    """The ``background()`` function sets the color used for the background of the py5
    window.

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

    The ``background()`` function sets the color used for the background of the py5
    window. The default background is light gray. This function is typically used
    within ``draw()`` to clear the display window at the beginning of each frame,
    but it can be used inside ``setup()`` to set the background on the first frame
    of animation or if the backgound need only be set once.

    An image can also be used as the background for a Sketch, although the image's
    width and height must match that of the Sketch window. Images used with
    ``background()`` will ignore the current ``tint()`` setting. To resize an image
    to the size of the Sketch window, use ``image.resize(width, height)``.

    It is not possible to use the transparency ``alpha`` parameter with background
    colors on the main drawing surface. It can only be used along with a
    ``Py5Graphics`` object and ``create_graphics()``.
    """
    pass


@overload
def background(rgb: int, alpha: float, /) -> None:
    """The ``background()`` function sets the color used for the background of the py5
    window.

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

    The ``background()`` function sets the color used for the background of the py5
    window. The default background is light gray. This function is typically used
    within ``draw()`` to clear the display window at the beginning of each frame,
    but it can be used inside ``setup()`` to set the background on the first frame
    of animation or if the backgound need only be set once.

    An image can also be used as the background for a Sketch, although the image's
    width and height must match that of the Sketch window. Images used with
    ``background()`` will ignore the current ``tint()`` setting. To resize an image
    to the size of the Sketch window, use ``image.resize(width, height)``.

    It is not possible to use the transparency ``alpha`` parameter with background
    colors on the main drawing surface. It can only be used along with a
    ``Py5Graphics`` object and ``create_graphics()``.
    """
    pass


@overload
def background(image: Py5Image, /) -> None:
    """The ``background()`` function sets the color used for the background of the py5
    window.

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

    The ``background()`` function sets the color used for the background of the py5
    window. The default background is light gray. This function is typically used
    within ``draw()`` to clear the display window at the beginning of each frame,
    but it can be used inside ``setup()`` to set the background on the first frame
    of animation or if the backgound need only be set once.

    An image can also be used as the background for a Sketch, although the image's
    width and height must match that of the Sketch window. Images used with
    ``background()`` will ignore the current ``tint()`` setting. To resize an image
    to the size of the Sketch window, use ``image.resize(width, height)``.

    It is not possible to use the transparency ``alpha`` parameter with background
    colors on the main drawing surface. It can only be used along with a
    ``Py5Graphics`` object and ``create_graphics()``.
    """
    pass


def background(*args):
    """The ``background()`` function sets the color used for the background of the py5
    window.

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

    The ``background()`` function sets the color used for the background of the py5
    window. The default background is light gray. This function is typically used
    within ``draw()`` to clear the display window at the beginning of each frame,
    but it can be used inside ``setup()`` to set the background on the first frame
    of animation or if the backgound need only be set once.

    An image can also be used as the background for a Sketch, although the image's
    width and height must match that of the Sketch window. Images used with
    ``background()`` will ignore the current ``tint()`` setting. To resize an image
    to the size of the Sketch window, use ``image.resize(width, height)``.

    It is not possible to use the transparency ``alpha`` parameter with background
    colors on the main drawing surface. It can only be used along with a
    ``Py5Graphics`` object and ``create_graphics()``.
    """
    return _py5sketch.background(*args)


def begin_camera() -> None:
    """The ``begin_camera()`` and ``end_camera()`` functions enable advanced
    customization of the camera space.

    Underlying Java method: PApplet.beginCamera

    Notes
    -----

    The ``begin_camera()`` and ``end_camera()`` functions enable advanced
    customization of the camera space. The functions are useful if you want to more
    control over camera movement, however for most users, the ``camera()`` function
    will be sufficient. The camera functions will replace any transformations (such
    as ``rotate()`` or ``translate()``) that occur before them in ``draw()``, but
    they will not automatically replace the camera transform itself. For this
    reason, camera functions should be placed at the beginning of ``draw()`` (so
    that transformations happen afterwards), and the ``camera()`` function can be
    used after ``begin_camera()`` if you want to reset the camera before applying
    transformations.

    This function sets the matrix mode to the camera matrix so calls such as
    ``translate()``, ``rotate()``, ``apply_matrix()`` and ``reset_matrix()`` affect
    the camera. ``begin_camera()`` should always be used with a following
    ``end_camera()`` and pairs of ``begin_camera()`` and ``end_camera()`` cannot be
    nested.
    """
    return _py5sketch.begin_camera()


def begin_contour() -> None:
    """Use the ``begin_contour()`` and ``end_contour()`` methods to create negative
    shapes within shapes such as the center of the letter 'O'.

    Underlying Java method: PApplet.beginContour

    Notes
    -----

    Use the ``begin_contour()`` and ``end_contour()`` methods to create negative
    shapes within shapes such as the center of the letter 'O'. The
    ``begin_contour()`` method begins recording vertices for the shape and
    ``end_contour()`` stops recording. The vertices that define a negative shape
    must "wind" in the opposite direction from the exterior shape. First draw
    vertices for the exterior shape in clockwise order, then for internal shapes,
    draw vertices counterclockwise.

    These methods can only be used within a ``begin_shape()`` & ``end_shape()`` pair
    and transformations such as ``translate()``, ``rotate()``, and ``scale()`` do
    not work within a ``begin_contour()`` & ``end_contour()`` pair. It is also not
    possible to use other shapes, such as ``ellipse()`` or ``rect()`` within.
    """
    return _py5sketch.begin_contour()


@overload
def begin_raw(renderer: str, filename: str, /) -> Py5Graphics:
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
        Py5Graphics object to apply draw commands to

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
    2D or 3D renderer. For instance, ``begin_raw()`` with the ``PDF`` library will
    write the geometry as flattened triangles and lines, even if recording from the
    ``P3D`` renderer.

    If you want a background to show up in your files, use ``rect(0, 0, width,
    height)`` after setting the ``fill()`` to the background color. Otherwise the
    background will not be rendered to the file because the background is not shape.

    Using ``hint(ENABLE_DEPTH_SORT)`` can improve the appearance of 3D geometry
    drawn to 2D file formats.
    """
    pass


@overload
def begin_raw(raw_graphics: Py5Graphics, /) -> None:
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
        Py5Graphics object to apply draw commands to

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
    2D or 3D renderer. For instance, ``begin_raw()`` with the ``PDF`` library will
    write the geometry as flattened triangles and lines, even if recording from the
    ``P3D`` renderer.

    If you want a background to show up in your files, use ``rect(0, 0, width,
    height)`` after setting the ``fill()`` to the background color. Otherwise the
    background will not be rendered to the file because the background is not shape.

    Using ``hint(ENABLE_DEPTH_SORT)`` can improve the appearance of 3D geometry
    drawn to 2D file formats.
    """
    pass


def begin_raw(*args):
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
        Py5Graphics object to apply draw commands to

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
    2D or 3D renderer. For instance, ``begin_raw()`` with the ``PDF`` library will
    write the geometry as flattened triangles and lines, even if recording from the
    ``P3D`` renderer.

    If you want a background to show up in your files, use ``rect(0, 0, width,
    height)`` after setting the ``fill()`` to the background color. Otherwise the
    background will not be rendered to the file because the background is not shape.

    Using ``hint(ENABLE_DEPTH_SORT)`` can improve the appearance of 3D geometry
    drawn to 2D file formats.
    """
    return _py5sketch.begin_raw(*args)


@overload
def begin_record(renderer: str, filename: str, /) -> Py5Graphics:
    """Opens a new file and all subsequent drawing functions are echoed to this file as
    well as the display window.

    Underlying Java method: PApplet.beginRecord

    Methods
    -------

    You can use any of the following signatures:

     * begin_record(recorder: Py5Graphics, /) -> None
     * begin_record(renderer: str, filename: str, /) -> Py5Graphics

    Parameters
    ----------

    filename: str
        filename for output

    recorder: Py5Graphics
        Py5Graphics object to record drawing commands to

    renderer: str
        PDF or SVG

    Notes
    -----

    Opens a new file and all subsequent drawing functions are echoed to this file as
    well as the display window. The ``begin_record()`` function requires two
    parameters, the first is the renderer and the second is the file name. This
    function is always used with ``end_record()`` to stop the recording process and
    close the file.

    Note that ``begin_record()`` will only pick up any settings that happen after it
    has been called. For instance, if you call ``text_font()`` before
    ``begin_record()``, then that font will not be set for the file that you're
    recording to.

    ``begin_record()`` works only with the ``PDF`` and ``SVG`` renderers.
    """
    pass


@overload
def begin_record(recorder: Py5Graphics, /) -> None:
    """Opens a new file and all subsequent drawing functions are echoed to this file as
    well as the display window.

    Underlying Java method: PApplet.beginRecord

    Methods
    -------

    You can use any of the following signatures:

     * begin_record(recorder: Py5Graphics, /) -> None
     * begin_record(renderer: str, filename: str, /) -> Py5Graphics

    Parameters
    ----------

    filename: str
        filename for output

    recorder: Py5Graphics
        Py5Graphics object to record drawing commands to

    renderer: str
        PDF or SVG

    Notes
    -----

    Opens a new file and all subsequent drawing functions are echoed to this file as
    well as the display window. The ``begin_record()`` function requires two
    parameters, the first is the renderer and the second is the file name. This
    function is always used with ``end_record()`` to stop the recording process and
    close the file.

    Note that ``begin_record()`` will only pick up any settings that happen after it
    has been called. For instance, if you call ``text_font()`` before
    ``begin_record()``, then that font will not be set for the file that you're
    recording to.

    ``begin_record()`` works only with the ``PDF`` and ``SVG`` renderers.
    """
    pass


def begin_record(*args):
    """Opens a new file and all subsequent drawing functions are echoed to this file as
    well as the display window.

    Underlying Java method: PApplet.beginRecord

    Methods
    -------

    You can use any of the following signatures:

     * begin_record(recorder: Py5Graphics, /) -> None
     * begin_record(renderer: str, filename: str, /) -> Py5Graphics

    Parameters
    ----------

    filename: str
        filename for output

    recorder: Py5Graphics
        Py5Graphics object to record drawing commands to

    renderer: str
        PDF or SVG

    Notes
    -----

    Opens a new file and all subsequent drawing functions are echoed to this file as
    well as the display window. The ``begin_record()`` function requires two
    parameters, the first is the renderer and the second is the file name. This
    function is always used with ``end_record()`` to stop the recording process and
    close the file.

    Note that ``begin_record()`` will only pick up any settings that happen after it
    has been called. For instance, if you call ``text_font()`` before
    ``begin_record()``, then that font will not be set for the file that you're
    recording to.

    ``begin_record()`` works only with the ``PDF`` and ``SVG`` renderers.
    """
    return _py5sketch.begin_record(*args)


@overload
def begin_shape() -> None:
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
    ``begin_shape()`` are ``POINTS``, ``LINES``, ``TRIANGLES``, ``TRIANGLE_FAN``,
    ``TRIANGLE_STRIP``, ``QUADS``, and ``QUAD_STRIP``. After calling the
    ``begin_shape()`` function, a series of ``vertex()`` commands must follow. To
    stop drawing the shape, call ``end_shape()``. The ``vertex()`` function with two
    parameters specifies a position in 2D and the ``vertex()`` function with three
    parameters specifies a position in 3D. Each shape will be outlined with the
    current stroke color and filled with the fill color.

    Transformations such as ``translate()``, ``rotate()``, and ``scale()`` do not
    work within ``begin_shape()``. It is also not possible to use other shapes, such
    as ``ellipse()`` or ``rect()`` within ``begin_shape()``.

    The ``P2D`` and ``P3D`` renderers allow ``stroke()`` and ``fill()`` to be
    altered on a per-vertex basis, but the default renderer does not. Settings such
    as ``stroke_weight()``, ``stroke_cap()``, and ``stroke_join()`` cannot be
    changed while inside a ``begin_shape()`` & ``end_shape()`` block with any
    renderer.
    """
    pass


@overload
def begin_shape(kind: int, /) -> None:
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
    ``begin_shape()`` are ``POINTS``, ``LINES``, ``TRIANGLES``, ``TRIANGLE_FAN``,
    ``TRIANGLE_STRIP``, ``QUADS``, and ``QUAD_STRIP``. After calling the
    ``begin_shape()`` function, a series of ``vertex()`` commands must follow. To
    stop drawing the shape, call ``end_shape()``. The ``vertex()`` function with two
    parameters specifies a position in 2D and the ``vertex()`` function with three
    parameters specifies a position in 3D. Each shape will be outlined with the
    current stroke color and filled with the fill color.

    Transformations such as ``translate()``, ``rotate()``, and ``scale()`` do not
    work within ``begin_shape()``. It is also not possible to use other shapes, such
    as ``ellipse()`` or ``rect()`` within ``begin_shape()``.

    The ``P2D`` and ``P3D`` renderers allow ``stroke()`` and ``fill()`` to be
    altered on a per-vertex basis, but the default renderer does not. Settings such
    as ``stroke_weight()``, ``stroke_cap()``, and ``stroke_join()`` cannot be
    changed while inside a ``begin_shape()`` & ``end_shape()`` block with any
    renderer.
    """
    pass


def begin_shape(*args):
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
    ``begin_shape()`` are ``POINTS``, ``LINES``, ``TRIANGLES``, ``TRIANGLE_FAN``,
    ``TRIANGLE_STRIP``, ``QUADS``, and ``QUAD_STRIP``. After calling the
    ``begin_shape()`` function, a series of ``vertex()`` commands must follow. To
    stop drawing the shape, call ``end_shape()``. The ``vertex()`` function with two
    parameters specifies a position in 2D and the ``vertex()`` function with three
    parameters specifies a position in 3D. Each shape will be outlined with the
    current stroke color and filled with the fill color.

    Transformations such as ``translate()``, ``rotate()``, and ``scale()`` do not
    work within ``begin_shape()``. It is also not possible to use other shapes, such
    as ``ellipse()`` or ``rect()`` within ``begin_shape()``.

    The ``P2D`` and ``P3D`` renderers allow ``stroke()`` and ``fill()`` to be
    altered on a per-vertex basis, but the default renderer does not. Settings such
    as ``stroke_weight()``, ``stroke_cap()``, and ``stroke_join()`` cannot be
    changed while inside a ``begin_shape()`` & ``end_shape()`` block with any
    renderer.
    """
    return _py5sketch.begin_shape(*args)


@overload
def bezier(x1: float, y1: float, x2: float, y2: float, x3: float,
           y3: float, x4: float, y4: float, /) -> None:
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
    version requires rendering with ``P3D``.
    """
    pass


@overload
def bezier(x1: float, y1: float, z1: float, x2: float, y2: float, z2: float,
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
    version requires rendering with ``P3D``.
    """
    pass


def bezier(*args):
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
    version requires rendering with ``P3D``.
    """
    return _py5sketch.bezier(*args)


def bezier_detail(detail: int, /) -> None:
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
    return _py5sketch.bezier_detail(detail)


def bezier_point(a: float, b: float, c: float, d: float, t: float, /) -> float:
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
    return _py5sketch.bezier_point(a, b, c, d, t)


def bezier_tangent(a: float, b: float, c: float,
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
    return _py5sketch.bezier_tangent(a, b, c, d, t)


@overload
def bezier_vertex(x2: float, y2: float, x3: float, y3: float,
                  x4: float, y4: float, /) -> None:
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
    ``MODE`` parameter specified to ``begin_shape()``. Using the 3D version requires
    rendering with ``P3D``.
    """
    pass


@overload
def bezier_vertex(x2: float, y2: float, z2: float, x3: float,
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
    ``MODE`` parameter specified to ``begin_shape()``. Using the 3D version requires
    rendering with ``P3D``.
    """
    pass


def bezier_vertex(*args):
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
    ``MODE`` parameter specified to ``begin_shape()``. Using the 3D version requires
    rendering with ``P3D``.
    """
    return _py5sketch.bezier_vertex(*args)


def bezier_vertices(coordinates: NDArray[(Any, Any), Float], /) -> None:
    """Create a collection of bezier vertices.

    Underlying Java method: PApplet.bezierVertices

    Parameters
    ----------

    coordinates: NDArray[(Any, Any), Float]
        array of bezier vertex coordinates

    Notes
    -----

    Create a collection of bezier vertices. The purpose of this method is to provide
    an alternative to repeatedly calling ``bezier_vertex()`` in a loop. For a large
    number of bezier vertices, the performance of ``bezier_vertices()`` will be much
    faster.

    The ``coordinates`` parameter should be a numpy array with one row for each
    bezier vertex. The first few columns are for the first control point, the next
    few columns are for the second control point, and the final few columns are for
    the anchor point. There should be six or nine columns for 2D or 3D points,
    respectively.
    """
    return _py5sketch.bezier_vertices(coordinates)


@overload
def blend(sx: int, sy: int, sw: int, sh: int, dx: int,
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
    ``src`` parameter is not used, the display window is used as the source image.

    This function ignores ``image_mode()``.
    """
    pass


@overload
def blend(src: Py5Image, sx: int, sy: int, sw: int, sh: int,
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
    ``src`` parameter is not used, the display window is used as the source image.

    This function ignores ``image_mode()``.
    """
    pass


def blend(*args):
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
    ``src`` parameter is not used, the display window is used as the source image.

    This function ignores ``image_mode()``.
    """
    return _py5sketch.blend(*args)


def blend_mode(mode: int, /) -> None:
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

    We recommend using ``blend_mode()`` and not the previous ``blend()`` function.
    However, unlike ``blend()``, the ``blend_mode()`` function does not support the
    following: ``HARD_LIGHT``, ``SOFT_LIGHT``, ``OVERLAY``, ``DODGE``, ``BURN``. On
    older hardware, the ``LIGHTEST``, ``DARKEST``, and ``DIFFERENCE`` modes might
    not be available as well.
    """
    return _py5sketch.blend_mode(mode)


def blue(rgb: int, /) -> float:
    """Extracts the blue value from a color, scaled to match current ``color_mode()``.

    Underlying Java method: PApplet.blue

    Parameters
    ----------

    rgb: int
        any value of the color datatype

    Notes
    -----

    Extracts the blue value from a color, scaled to match current ``color_mode()``.

    The ``blue()`` function is easy to use and understand, but it is slower than a
    technique called bit masking. When working in ``color_mode(RGB, 255)``, you can
    achieve the same results as ``blue()`` but with greater speed by using a bit
    mask to remove the other color components. For example, ``blue(c)`` and ``c &
    0xFF`` both extract the blue value from a color variable ``c`` but the later is
    faster.
    """
    return _py5sketch.blue(rgb)


@overload
def box(size: float, /) -> None:
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
def box(w: float, h: float, d: float, /) -> None:
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


def box(*args):
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
    return _py5sketch.box(*args)


def brightness(rgb: int, /) -> float:
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
    return _py5sketch.brightness(rgb)


@overload
def camera() -> None:
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
def camera(eye_x: float, eye_y: float, eye_z: float, center_x: float, center_y: float,
           center_z: float, up_x: float, up_y: float, up_z: float, /) -> None:
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


def camera(*args):
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
    return _py5sketch.camera(*args)


def circle(x: float, y: float, extent: float, /) -> None:
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
    return _py5sketch.circle(x, y, extent)


def clip(a: float, b: float, c: float, d: float, /) -> None:
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
    either ``CORNER``, ``CORNERS``, or ``CENTER``.
    """
    return _py5sketch.clip(a, b, c, d)


@overload
def color(fgray: float, /) -> int:
    """Creates colors for storing in variables of the ``color`` datatype (a 32 bit
    integer).

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
        alpha value relative to current color range

    alpha: int
        alpha value relative to current color range

    falpha: float
        alpha value relative to current color range

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

    Creates colors for storing in variables of the ``color`` datatype (a 32 bit
    integer). The parameters are interpreted as ``RGB`` or ``HSB`` values depending
    on the current ``color_mode()``. The default mode is ``RGB`` values from 0 to
    255 and, therefore, ``color(255, 204, 0)`` will return a bright yellow color
    (see the first example).

    Note that if only one value is provided to ``color()``, it will be interpreted
    as a grayscale value. Add a second value, and it will be used for alpha
    transparency. When three values are specified, they are interpreted as either
    ``RGB`` or ``HSB`` values. Adding a fourth value applies alpha transparency.

    Note that when using hexadecimal notation, it is not necessary to use
    ``color()``, as in: ``c = 0x006699``
    """
    pass


@overload
def color(fgray: float, falpha: float, /) -> int:
    """Creates colors for storing in variables of the ``color`` datatype (a 32 bit
    integer).

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
        alpha value relative to current color range

    alpha: int
        alpha value relative to current color range

    falpha: float
        alpha value relative to current color range

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

    Creates colors for storing in variables of the ``color`` datatype (a 32 bit
    integer). The parameters are interpreted as ``RGB`` or ``HSB`` values depending
    on the current ``color_mode()``. The default mode is ``RGB`` values from 0 to
    255 and, therefore, ``color(255, 204, 0)`` will return a bright yellow color
    (see the first example).

    Note that if only one value is provided to ``color()``, it will be interpreted
    as a grayscale value. Add a second value, and it will be used for alpha
    transparency. When three values are specified, they are interpreted as either
    ``RGB`` or ``HSB`` values. Adding a fourth value applies alpha transparency.

    Note that when using hexadecimal notation, it is not necessary to use
    ``color()``, as in: ``c = 0x006699``
    """
    pass


@overload
def color(v1: float, v2: float, v3: float, /) -> int:
    """Creates colors for storing in variables of the ``color`` datatype (a 32 bit
    integer).

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
        alpha value relative to current color range

    alpha: int
        alpha value relative to current color range

    falpha: float
        alpha value relative to current color range

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

    Creates colors for storing in variables of the ``color`` datatype (a 32 bit
    integer). The parameters are interpreted as ``RGB`` or ``HSB`` values depending
    on the current ``color_mode()``. The default mode is ``RGB`` values from 0 to
    255 and, therefore, ``color(255, 204, 0)`` will return a bright yellow color
    (see the first example).

    Note that if only one value is provided to ``color()``, it will be interpreted
    as a grayscale value. Add a second value, and it will be used for alpha
    transparency. When three values are specified, they are interpreted as either
    ``RGB`` or ``HSB`` values. Adding a fourth value applies alpha transparency.

    Note that when using hexadecimal notation, it is not necessary to use
    ``color()``, as in: ``c = 0x006699``
    """
    pass


@overload
def color(v1: float, v2: float, v3: float, alpha: float, /) -> int:
    """Creates colors for storing in variables of the ``color`` datatype (a 32 bit
    integer).

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
        alpha value relative to current color range

    alpha: int
        alpha value relative to current color range

    falpha: float
        alpha value relative to current color range

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

    Creates colors for storing in variables of the ``color`` datatype (a 32 bit
    integer). The parameters are interpreted as ``RGB`` or ``HSB`` values depending
    on the current ``color_mode()``. The default mode is ``RGB`` values from 0 to
    255 and, therefore, ``color(255, 204, 0)`` will return a bright yellow color
    (see the first example).

    Note that if only one value is provided to ``color()``, it will be interpreted
    as a grayscale value. Add a second value, and it will be used for alpha
    transparency. When three values are specified, they are interpreted as either
    ``RGB`` or ``HSB`` values. Adding a fourth value applies alpha transparency.

    Note that when using hexadecimal notation, it is not necessary to use
    ``color()``, as in: ``c = 0x006699``
    """
    pass


@overload
def color(gray: int, /) -> int:
    """Creates colors for storing in variables of the ``color`` datatype (a 32 bit
    integer).

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
        alpha value relative to current color range

    alpha: int
        alpha value relative to current color range

    falpha: float
        alpha value relative to current color range

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

    Creates colors for storing in variables of the ``color`` datatype (a 32 bit
    integer). The parameters are interpreted as ``RGB`` or ``HSB`` values depending
    on the current ``color_mode()``. The default mode is ``RGB`` values from 0 to
    255 and, therefore, ``color(255, 204, 0)`` will return a bright yellow color
    (see the first example).

    Note that if only one value is provided to ``color()``, it will be interpreted
    as a grayscale value. Add a second value, and it will be used for alpha
    transparency. When three values are specified, they are interpreted as either
    ``RGB`` or ``HSB`` values. Adding a fourth value applies alpha transparency.

    Note that when using hexadecimal notation, it is not necessary to use
    ``color()``, as in: ``c = 0x006699``
    """
    pass


@overload
def color(gray: int, alpha: int, /) -> int:
    """Creates colors for storing in variables of the ``color`` datatype (a 32 bit
    integer).

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
        alpha value relative to current color range

    alpha: int
        alpha value relative to current color range

    falpha: float
        alpha value relative to current color range

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

    Creates colors for storing in variables of the ``color`` datatype (a 32 bit
    integer). The parameters are interpreted as ``RGB`` or ``HSB`` values depending
    on the current ``color_mode()``. The default mode is ``RGB`` values from 0 to
    255 and, therefore, ``color(255, 204, 0)`` will return a bright yellow color
    (see the first example).

    Note that if only one value is provided to ``color()``, it will be interpreted
    as a grayscale value. Add a second value, and it will be used for alpha
    transparency. When three values are specified, they are interpreted as either
    ``RGB`` or ``HSB`` values. Adding a fourth value applies alpha transparency.

    Note that when using hexadecimal notation, it is not necessary to use
    ``color()``, as in: ``c = 0x006699``
    """
    pass


@overload
def color(v1: int, v2: int, v3: int, /) -> int:
    """Creates colors for storing in variables of the ``color`` datatype (a 32 bit
    integer).

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
        alpha value relative to current color range

    alpha: int
        alpha value relative to current color range

    falpha: float
        alpha value relative to current color range

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

    Creates colors for storing in variables of the ``color`` datatype (a 32 bit
    integer). The parameters are interpreted as ``RGB`` or ``HSB`` values depending
    on the current ``color_mode()``. The default mode is ``RGB`` values from 0 to
    255 and, therefore, ``color(255, 204, 0)`` will return a bright yellow color
    (see the first example).

    Note that if only one value is provided to ``color()``, it will be interpreted
    as a grayscale value. Add a second value, and it will be used for alpha
    transparency. When three values are specified, they are interpreted as either
    ``RGB`` or ``HSB`` values. Adding a fourth value applies alpha transparency.

    Note that when using hexadecimal notation, it is not necessary to use
    ``color()``, as in: ``c = 0x006699``
    """
    pass


@overload
def color(v1: int, v2: int, v3: int, alpha: int, /) -> int:
    """Creates colors for storing in variables of the ``color`` datatype (a 32 bit
    integer).

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
        alpha value relative to current color range

    alpha: int
        alpha value relative to current color range

    falpha: float
        alpha value relative to current color range

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

    Creates colors for storing in variables of the ``color`` datatype (a 32 bit
    integer). The parameters are interpreted as ``RGB`` or ``HSB`` values depending
    on the current ``color_mode()``. The default mode is ``RGB`` values from 0 to
    255 and, therefore, ``color(255, 204, 0)`` will return a bright yellow color
    (see the first example).

    Note that if only one value is provided to ``color()``, it will be interpreted
    as a grayscale value. Add a second value, and it will be used for alpha
    transparency. When three values are specified, they are interpreted as either
    ``RGB`` or ``HSB`` values. Adding a fourth value applies alpha transparency.

    Note that when using hexadecimal notation, it is not necessary to use
    ``color()``, as in: ``c = 0x006699``
    """
    pass


def color(*args):
    """Creates colors for storing in variables of the ``color`` datatype (a 32 bit
    integer).

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
        alpha value relative to current color range

    alpha: int
        alpha value relative to current color range

    falpha: float
        alpha value relative to current color range

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

    Creates colors for storing in variables of the ``color`` datatype (a 32 bit
    integer). The parameters are interpreted as ``RGB`` or ``HSB`` values depending
    on the current ``color_mode()``. The default mode is ``RGB`` values from 0 to
    255 and, therefore, ``color(255, 204, 0)`` will return a bright yellow color
    (see the first example).

    Note that if only one value is provided to ``color()``, it will be interpreted
    as a grayscale value. Add a second value, and it will be used for alpha
    transparency. When three values are specified, they are interpreted as either
    ``RGB`` or ``HSB`` values. Adding a fourth value applies alpha transparency.

    Note that when using hexadecimal notation, it is not necessary to use
    ``color()``, as in: ``c = 0x006699``
    """
    return _py5sketch.color(*args)


@overload
def color_mode(mode: int, /) -> None:
    """Changes the way py5 interprets color data.

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

    Changes the way py5 interprets color data. By default, the parameters for
    ``fill()``, ``stroke()``, ``background()``, and ``color()`` are defined by
    values between 0 and 255 using the ``RGB`` color model. The ``color_mode()``
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
def color_mode(mode: int, max: float, /) -> None:
    """Changes the way py5 interprets color data.

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

    Changes the way py5 interprets color data. By default, the parameters for
    ``fill()``, ``stroke()``, ``background()``, and ``color()`` are defined by
    values between 0 and 255 using the ``RGB`` color model. The ``color_mode()``
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
def color_mode(mode: int, max1: float, max2: float, max3: float, /) -> None:
    """Changes the way py5 interprets color data.

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

    Changes the way py5 interprets color data. By default, the parameters for
    ``fill()``, ``stroke()``, ``background()``, and ``color()`` are defined by
    values between 0 and 255 using the ``RGB`` color model. The ``color_mode()``
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
def color_mode(mode: int, max1: float, max2: float,
               max3: float, max_a: float, /) -> None:
    """Changes the way py5 interprets color data.

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

    Changes the way py5 interprets color data. By default, the parameters for
    ``fill()``, ``stroke()``, ``background()``, and ``color()`` are defined by
    values between 0 and 255 using the ``RGB`` color model. The ``color_mode()``
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


def color_mode(*args):
    """Changes the way py5 interprets color data.

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

    Changes the way py5 interprets color data. By default, the parameters for
    ``fill()``, ``stroke()``, ``background()``, and ``color()`` are defined by
    values between 0 and 255 using the ``RGB`` color model. The ``color_mode()``
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
    return _py5sketch.color_mode(*args)


@overload
def copy() -> Py5Image:
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

    Copies a region of pixels from the display window to another area of the display
    window and copies a region of pixels from an image used as the ``src_img``
    parameter into the display window. If the source and destination regions aren't
    the same size, it will automatically resize the source pixels to fit the
    specified target region. No alpha information is used in the process, however if
    the source image has an alpha channel set, it will be copied as well.

    This function ignores ``image_mode()``.
    """
    pass


@overload
def copy(sx: int, sy: int, sw: int, sh: int, dx: int,
         dy: int, dw: int, dh: int, /) -> None:
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

    Copies a region of pixels from the display window to another area of the display
    window and copies a region of pixels from an image used as the ``src_img``
    parameter into the display window. If the source and destination regions aren't
    the same size, it will automatically resize the source pixels to fit the
    specified target region. No alpha information is used in the process, however if
    the source image has an alpha channel set, it will be copied as well.

    This function ignores ``image_mode()``.
    """
    pass


@overload
def copy(src: Py5Image, sx: int, sy: int, sw: int, sh: int,
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

    Copies a region of pixels from the display window to another area of the display
    window and copies a region of pixels from an image used as the ``src_img``
    parameter into the display window. If the source and destination regions aren't
    the same size, it will automatically resize the source pixels to fit the
    specified target region. No alpha information is used in the process, however if
    the source image has an alpha channel set, it will be copied as well.

    This function ignores ``image_mode()``.
    """
    pass


def copy(*args):
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

    Copies a region of pixels from the display window to another area of the display
    window and copies a region of pixels from an image used as the ``src_img``
    parameter into the display window. If the source and destination regions aren't
    the same size, it will automatically resize the source pixels to fit the
    specified target region. No alpha information is used in the process, however if
    the source image has an alpha channel set, it will be copied as well.

    This function ignores ``image_mode()``.
    """
    return _py5sketch.copy(*args)


@overload
def create_font(name: str, size: float, /) -> Py5Font:
    """Dynamically converts a font to the format used by py5 from a .ttf or .otf file
    inside the Sketch's "data" folder or a font that's installed elsewhere on the
    computer.

    Underlying Java method: PApplet.createFont

    Methods
    -------

    You can use any of the following signatures:

     * create_font(name: str, size: float, /) -> Py5Font
     * create_font(name: str, size: float, smooth: bool, /) -> Py5Font
     * create_font(name: str, size: float, smooth: bool, charset: List[chr], /) -> Py5Font

    Parameters
    ----------

    charset: List[chr]
        array containing characters to be generated

    name: str
        name of the font to load

    size: float
        point size of the font

    smooth: bool
        true for an antialiased font, false for aliased

    Notes
    -----

    Dynamically converts a font to the format used by py5 from a .ttf or .otf file
    inside the Sketch's "data" folder or a font that's installed elsewhere on the
    computer. If you want to use a font installed on your computer, use the
    ``Py5Font.list()`` method to first determine the names for the fonts recognized
    by the computer and are compatible with this function. Not all fonts can be used
    and some might work with one operating system and not others. When sharing a
    Sketch with other people or posting it on the web, you may need to include a
    .ttf or .otf version of your font in the data directory of the Sketch because
    other people might not have the font installed on their computer. Only fonts
    that can legally be distributed should be included with a Sketch.

    The ``size`` parameter states the font size you want to generate. The ``smooth``
    parameter specifies if the font should be antialiased or not. The ``charset``
    parameter is an array of chars that specifies the characters to generate.

    This function allows py5 to work with the font natively in the default renderer,
    so the letters are defined by vector geometry and are rendered quickly. In the
    ``P2D`` and ``P3D`` renderers, the function sets the project to render the font
    as a series of small textures. For instance, when using the default renderer,
    the actual native version of the font will be employed by the Sketch, improving
    drawing quality and performance. With the ``P2D`` and ``P3D`` renderers, the
    bitmapped version will be used to improve speed and appearance, but the results
    are poor when exporting if the Sketch does not include the .otf or .ttf file,
    and the requested font is not available on the machine running the Sketch.
    """
    pass


@overload
def create_font(name: str, size: float, smooth: bool, /) -> Py5Font:
    """Dynamically converts a font to the format used by py5 from a .ttf or .otf file
    inside the Sketch's "data" folder or a font that's installed elsewhere on the
    computer.

    Underlying Java method: PApplet.createFont

    Methods
    -------

    You can use any of the following signatures:

     * create_font(name: str, size: float, /) -> Py5Font
     * create_font(name: str, size: float, smooth: bool, /) -> Py5Font
     * create_font(name: str, size: float, smooth: bool, charset: List[chr], /) -> Py5Font

    Parameters
    ----------

    charset: List[chr]
        array containing characters to be generated

    name: str
        name of the font to load

    size: float
        point size of the font

    smooth: bool
        true for an antialiased font, false for aliased

    Notes
    -----

    Dynamically converts a font to the format used by py5 from a .ttf or .otf file
    inside the Sketch's "data" folder or a font that's installed elsewhere on the
    computer. If you want to use a font installed on your computer, use the
    ``Py5Font.list()`` method to first determine the names for the fonts recognized
    by the computer and are compatible with this function. Not all fonts can be used
    and some might work with one operating system and not others. When sharing a
    Sketch with other people or posting it on the web, you may need to include a
    .ttf or .otf version of your font in the data directory of the Sketch because
    other people might not have the font installed on their computer. Only fonts
    that can legally be distributed should be included with a Sketch.

    The ``size`` parameter states the font size you want to generate. The ``smooth``
    parameter specifies if the font should be antialiased or not. The ``charset``
    parameter is an array of chars that specifies the characters to generate.

    This function allows py5 to work with the font natively in the default renderer,
    so the letters are defined by vector geometry and are rendered quickly. In the
    ``P2D`` and ``P3D`` renderers, the function sets the project to render the font
    as a series of small textures. For instance, when using the default renderer,
    the actual native version of the font will be employed by the Sketch, improving
    drawing quality and performance. With the ``P2D`` and ``P3D`` renderers, the
    bitmapped version will be used to improve speed and appearance, but the results
    are poor when exporting if the Sketch does not include the .otf or .ttf file,
    and the requested font is not available on the machine running the Sketch.
    """
    pass


@overload
def create_font(name: str, size: float, smooth: bool,
                charset: List[chr], /) -> Py5Font:
    """Dynamically converts a font to the format used by py5 from a .ttf or .otf file
    inside the Sketch's "data" folder or a font that's installed elsewhere on the
    computer.

    Underlying Java method: PApplet.createFont

    Methods
    -------

    You can use any of the following signatures:

     * create_font(name: str, size: float, /) -> Py5Font
     * create_font(name: str, size: float, smooth: bool, /) -> Py5Font
     * create_font(name: str, size: float, smooth: bool, charset: List[chr], /) -> Py5Font

    Parameters
    ----------

    charset: List[chr]
        array containing characters to be generated

    name: str
        name of the font to load

    size: float
        point size of the font

    smooth: bool
        true for an antialiased font, false for aliased

    Notes
    -----

    Dynamically converts a font to the format used by py5 from a .ttf or .otf file
    inside the Sketch's "data" folder or a font that's installed elsewhere on the
    computer. If you want to use a font installed on your computer, use the
    ``Py5Font.list()`` method to first determine the names for the fonts recognized
    by the computer and are compatible with this function. Not all fonts can be used
    and some might work with one operating system and not others. When sharing a
    Sketch with other people or posting it on the web, you may need to include a
    .ttf or .otf version of your font in the data directory of the Sketch because
    other people might not have the font installed on their computer. Only fonts
    that can legally be distributed should be included with a Sketch.

    The ``size`` parameter states the font size you want to generate. The ``smooth``
    parameter specifies if the font should be antialiased or not. The ``charset``
    parameter is an array of chars that specifies the characters to generate.

    This function allows py5 to work with the font natively in the default renderer,
    so the letters are defined by vector geometry and are rendered quickly. In the
    ``P2D`` and ``P3D`` renderers, the function sets the project to render the font
    as a series of small textures. For instance, when using the default renderer,
    the actual native version of the font will be employed by the Sketch, improving
    drawing quality and performance. With the ``P2D`` and ``P3D`` renderers, the
    bitmapped version will be used to improve speed and appearance, but the results
    are poor when exporting if the Sketch does not include the .otf or .ttf file,
    and the requested font is not available on the machine running the Sketch.
    """
    pass


def create_font(*args):
    """Dynamically converts a font to the format used by py5 from a .ttf or .otf file
    inside the Sketch's "data" folder or a font that's installed elsewhere on the
    computer.

    Underlying Java method: PApplet.createFont

    Methods
    -------

    You can use any of the following signatures:

     * create_font(name: str, size: float, /) -> Py5Font
     * create_font(name: str, size: float, smooth: bool, /) -> Py5Font
     * create_font(name: str, size: float, smooth: bool, charset: List[chr], /) -> Py5Font

    Parameters
    ----------

    charset: List[chr]
        array containing characters to be generated

    name: str
        name of the font to load

    size: float
        point size of the font

    smooth: bool
        true for an antialiased font, false for aliased

    Notes
    -----

    Dynamically converts a font to the format used by py5 from a .ttf or .otf file
    inside the Sketch's "data" folder or a font that's installed elsewhere on the
    computer. If you want to use a font installed on your computer, use the
    ``Py5Font.list()`` method to first determine the names for the fonts recognized
    by the computer and are compatible with this function. Not all fonts can be used
    and some might work with one operating system and not others. When sharing a
    Sketch with other people or posting it on the web, you may need to include a
    .ttf or .otf version of your font in the data directory of the Sketch because
    other people might not have the font installed on their computer. Only fonts
    that can legally be distributed should be included with a Sketch.

    The ``size`` parameter states the font size you want to generate. The ``smooth``
    parameter specifies if the font should be antialiased or not. The ``charset``
    parameter is an array of chars that specifies the characters to generate.

    This function allows py5 to work with the font natively in the default renderer,
    so the letters are defined by vector geometry and are rendered quickly. In the
    ``P2D`` and ``P3D`` renderers, the function sets the project to render the font
    as a series of small textures. For instance, when using the default renderer,
    the actual native version of the font will be employed by the Sketch, improving
    drawing quality and performance. With the ``P2D`` and ``P3D`` renderers, the
    bitmapped version will be used to improve speed and appearance, but the results
    are poor when exporting if the Sketch does not include the .otf or .ttf file,
    and the requested font is not available on the machine running the Sketch.
    """
    return _py5sketch.create_font(*args)


@overload
def create_graphics(w: int, h: int, /) -> Py5Graphics:
    """Creates and returns a new ``Py5Graphics`` object.

    Underlying Java method: PApplet.createGraphics

    Methods
    -------

    You can use any of the following signatures:

     * create_graphics(w: int, h: int, /) -> Py5Graphics
     * create_graphics(w: int, h: int, renderer: str, /) -> Py5Graphics
     * create_graphics(w: int, h: int, renderer: str, path: str, /) -> Py5Graphics

    Parameters
    ----------

    h: int
        height in pixels

    path: str
        the name of the file (can be an absolute or relative path)

    renderer: str
        Either P2D, P3D, or PDF

    w: int
        width in pixels

    Notes
    -----

    Creates and returns a new ``Py5Graphics`` object. Use this class if you need to
    draw into an off-screen graphics buffer. The first two parameters define the
    width and height in pixels. The third, optional parameter specifies the
    renderer. It can be defined as ``P2D``, ``P3D``, ``PDF``, or SVG. If the third
    parameter isn't used, the default renderer is set. The ``PDF`` and ``SVG``
    renderers require the filename parameter.

    It's important to consider the renderer used with ``create_graphics()`` in
    relation to the main renderer specified in ``size()``. For example, it's only
    possible to use ``P2D`` or ``P3D`` with ``create_graphics()`` when one of them
    is defined in ``size()``. ``P2D`` and ``P3D`` use OpenGL for drawing, and when
    using an OpenGL renderer it's necessary for the main drawing surface to be
    OpenGL-based. If ``P2D`` or ``P3D`` are used as the renderer in ``size()``, then
    any of the options can be used with ``create_graphics()``. If the default
    renderer is used in ``size()``, then only the default, ``PDF``, or ``SVG`` can
    be used with ``create_graphics()``.

    It's important to run all drawing functions between the
    ``Py5Graphics.begin_draw()`` and ``Py5Graphics.end_draw()``. As the exception to
    this rule, ``smooth()`` should be run on the Py5Graphics object before
    ``Py5Graphics.begin_draw()``. See the reference for ``smooth()`` for more
    detail.

    The ``create_graphics()`` function should almost never be used inside ``draw()``
    because of the memory and time needed to set up the graphics. One-time or
    occasional use during ``draw()`` might be acceptable, but code that calls
    ``create_graphics()`` at 60 frames per second might run out of memory or freeze
    your Sketch.

    Unlike the main drawing surface which is completely opaque, surfaces created
    with ``create_graphics()`` can have transparency. This makes it possible to draw
    into a graphics and maintain the alpha channel. By using ``save()`` to write a
    ``PNG`` or ``TGA`` file, the transparency of the graphics object will be
    honored.
    """
    pass


@overload
def create_graphics(w: int, h: int, renderer: str, /) -> Py5Graphics:
    """Creates and returns a new ``Py5Graphics`` object.

    Underlying Java method: PApplet.createGraphics

    Methods
    -------

    You can use any of the following signatures:

     * create_graphics(w: int, h: int, /) -> Py5Graphics
     * create_graphics(w: int, h: int, renderer: str, /) -> Py5Graphics
     * create_graphics(w: int, h: int, renderer: str, path: str, /) -> Py5Graphics

    Parameters
    ----------

    h: int
        height in pixels

    path: str
        the name of the file (can be an absolute or relative path)

    renderer: str
        Either P2D, P3D, or PDF

    w: int
        width in pixels

    Notes
    -----

    Creates and returns a new ``Py5Graphics`` object. Use this class if you need to
    draw into an off-screen graphics buffer. The first two parameters define the
    width and height in pixels. The third, optional parameter specifies the
    renderer. It can be defined as ``P2D``, ``P3D``, ``PDF``, or SVG. If the third
    parameter isn't used, the default renderer is set. The ``PDF`` and ``SVG``
    renderers require the filename parameter.

    It's important to consider the renderer used with ``create_graphics()`` in
    relation to the main renderer specified in ``size()``. For example, it's only
    possible to use ``P2D`` or ``P3D`` with ``create_graphics()`` when one of them
    is defined in ``size()``. ``P2D`` and ``P3D`` use OpenGL for drawing, and when
    using an OpenGL renderer it's necessary for the main drawing surface to be
    OpenGL-based. If ``P2D`` or ``P3D`` are used as the renderer in ``size()``, then
    any of the options can be used with ``create_graphics()``. If the default
    renderer is used in ``size()``, then only the default, ``PDF``, or ``SVG`` can
    be used with ``create_graphics()``.

    It's important to run all drawing functions between the
    ``Py5Graphics.begin_draw()`` and ``Py5Graphics.end_draw()``. As the exception to
    this rule, ``smooth()`` should be run on the Py5Graphics object before
    ``Py5Graphics.begin_draw()``. See the reference for ``smooth()`` for more
    detail.

    The ``create_graphics()`` function should almost never be used inside ``draw()``
    because of the memory and time needed to set up the graphics. One-time or
    occasional use during ``draw()`` might be acceptable, but code that calls
    ``create_graphics()`` at 60 frames per second might run out of memory or freeze
    your Sketch.

    Unlike the main drawing surface which is completely opaque, surfaces created
    with ``create_graphics()`` can have transparency. This makes it possible to draw
    into a graphics and maintain the alpha channel. By using ``save()`` to write a
    ``PNG`` or ``TGA`` file, the transparency of the graphics object will be
    honored.
    """
    pass


@overload
def create_graphics(w: int, h: int, renderer: str,
                    path: str, /) -> Py5Graphics:
    """Creates and returns a new ``Py5Graphics`` object.

    Underlying Java method: PApplet.createGraphics

    Methods
    -------

    You can use any of the following signatures:

     * create_graphics(w: int, h: int, /) -> Py5Graphics
     * create_graphics(w: int, h: int, renderer: str, /) -> Py5Graphics
     * create_graphics(w: int, h: int, renderer: str, path: str, /) -> Py5Graphics

    Parameters
    ----------

    h: int
        height in pixels

    path: str
        the name of the file (can be an absolute or relative path)

    renderer: str
        Either P2D, P3D, or PDF

    w: int
        width in pixels

    Notes
    -----

    Creates and returns a new ``Py5Graphics`` object. Use this class if you need to
    draw into an off-screen graphics buffer. The first two parameters define the
    width and height in pixels. The third, optional parameter specifies the
    renderer. It can be defined as ``P2D``, ``P3D``, ``PDF``, or SVG. If the third
    parameter isn't used, the default renderer is set. The ``PDF`` and ``SVG``
    renderers require the filename parameter.

    It's important to consider the renderer used with ``create_graphics()`` in
    relation to the main renderer specified in ``size()``. For example, it's only
    possible to use ``P2D`` or ``P3D`` with ``create_graphics()`` when one of them
    is defined in ``size()``. ``P2D`` and ``P3D`` use OpenGL for drawing, and when
    using an OpenGL renderer it's necessary for the main drawing surface to be
    OpenGL-based. If ``P2D`` or ``P3D`` are used as the renderer in ``size()``, then
    any of the options can be used with ``create_graphics()``. If the default
    renderer is used in ``size()``, then only the default, ``PDF``, or ``SVG`` can
    be used with ``create_graphics()``.

    It's important to run all drawing functions between the
    ``Py5Graphics.begin_draw()`` and ``Py5Graphics.end_draw()``. As the exception to
    this rule, ``smooth()`` should be run on the Py5Graphics object before
    ``Py5Graphics.begin_draw()``. See the reference for ``smooth()`` for more
    detail.

    The ``create_graphics()`` function should almost never be used inside ``draw()``
    because of the memory and time needed to set up the graphics. One-time or
    occasional use during ``draw()`` might be acceptable, but code that calls
    ``create_graphics()`` at 60 frames per second might run out of memory or freeze
    your Sketch.

    Unlike the main drawing surface which is completely opaque, surfaces created
    with ``create_graphics()`` can have transparency. This makes it possible to draw
    into a graphics and maintain the alpha channel. By using ``save()`` to write a
    ``PNG`` or ``TGA`` file, the transparency of the graphics object will be
    honored.
    """
    pass


def create_graphics(*args):
    """Creates and returns a new ``Py5Graphics`` object.

    Underlying Java method: PApplet.createGraphics

    Methods
    -------

    You can use any of the following signatures:

     * create_graphics(w: int, h: int, /) -> Py5Graphics
     * create_graphics(w: int, h: int, renderer: str, /) -> Py5Graphics
     * create_graphics(w: int, h: int, renderer: str, path: str, /) -> Py5Graphics

    Parameters
    ----------

    h: int
        height in pixels

    path: str
        the name of the file (can be an absolute or relative path)

    renderer: str
        Either P2D, P3D, or PDF

    w: int
        width in pixels

    Notes
    -----

    Creates and returns a new ``Py5Graphics`` object. Use this class if you need to
    draw into an off-screen graphics buffer. The first two parameters define the
    width and height in pixels. The third, optional parameter specifies the
    renderer. It can be defined as ``P2D``, ``P3D``, ``PDF``, or SVG. If the third
    parameter isn't used, the default renderer is set. The ``PDF`` and ``SVG``
    renderers require the filename parameter.

    It's important to consider the renderer used with ``create_graphics()`` in
    relation to the main renderer specified in ``size()``. For example, it's only
    possible to use ``P2D`` or ``P3D`` with ``create_graphics()`` when one of them
    is defined in ``size()``. ``P2D`` and ``P3D`` use OpenGL for drawing, and when
    using an OpenGL renderer it's necessary for the main drawing surface to be
    OpenGL-based. If ``P2D`` or ``P3D`` are used as the renderer in ``size()``, then
    any of the options can be used with ``create_graphics()``. If the default
    renderer is used in ``size()``, then only the default, ``PDF``, or ``SVG`` can
    be used with ``create_graphics()``.

    It's important to run all drawing functions between the
    ``Py5Graphics.begin_draw()`` and ``Py5Graphics.end_draw()``. As the exception to
    this rule, ``smooth()`` should be run on the Py5Graphics object before
    ``Py5Graphics.begin_draw()``. See the reference for ``smooth()`` for more
    detail.

    The ``create_graphics()`` function should almost never be used inside ``draw()``
    because of the memory and time needed to set up the graphics. One-time or
    occasional use during ``draw()`` might be acceptable, but code that calls
    ``create_graphics()`` at 60 frames per second might run out of memory or freeze
    your Sketch.

    Unlike the main drawing surface which is completely opaque, surfaces created
    with ``create_graphics()`` can have transparency. This makes it possible to draw
    into a graphics and maintain the alpha channel. By using ``save()`` to write a
    ``PNG`` or ``TGA`` file, the transparency of the graphics object will be
    honored.
    """
    return _py5sketch.create_graphics(*args)


def create_image(w: int, h: int, format: int, /) -> Py5Image:
    """Creates a new Py5Image (the datatype for storing images).

    Underlying Java method: PApplet.createImage

    Parameters
    ----------

    format: int
        Either RGB, ARGB, ALPHA (grayscale alpha channel)

    h: int
        height in pixels

    w: int
        width in pixels

    Notes
    -----

    Creates a new Py5Image (the datatype for storing images). This provides a fresh
    buffer of pixels to play with. Set the size of the buffer with the ``w`` and
    ``h`` parameters. The ``format`` parameter defines how the pixels are stored.
    See the ``Py5Image`` reference for more information.

    Be sure to include all three parameters, specifying only the width and height
    (but no format) will produce a strange error.

    Advanced users please note that ``create_image()`` should be used instead of the
    syntax ``Py5Image()``.
    """
    return _py5sketch.create_image(w, h, format)


@overload
def create_shape() -> Py5Shape:
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
        either GROUP, PATH, or GEOMETRY

    Notes
    -----

    The ``create_shape()`` function is used to define a new shape. Once created,
    this shape can be drawn with the ``shape()`` function. The basic way to use the
    function defines new primitive shapes. One of the following parameters are used
    as the first parameter: ``ELLIPSE``, ``RECT``, ``ARC``, ``TRIANGLE``,
    ``SPHERE``, ``BOX``, ``QUAD``, or ``LINE``. The parameters for each of these
    different shapes are the same as their corresponding functions: ``ellipse()``,
    ``rect()``, ``arc()``, ``triangle()``, ``sphere()``, ``box()``, ``quad()``, and
    ``line()``. The first example clarifies how this works.

    Custom, unique shapes can be made by using ``create_shape()`` without a
    parameter. After the shape is started, the drawing attributes and geometry can
    be set directly to the shape within the ``begin_shape()`` and ``end_shape()``
    methods. See the second example for specifics, and the reference for
    ``begin_shape()`` for all of its options.

    The  ``create_shape()`` function can also be used to make a complex shape made
    of other shapes. This is called a "group" and it's created by using the
    parameter ``GROUP`` as the first parameter. See the fourth example to see how it
    works.

    After using ``create_shape()``, stroke and fill color can be set by calling
    methods like ``Py5Shape.set_fill()`` and ``Py5Shape.set_stroke()``, as seen in
    the examples. The complete list of methods and fields for the ``Py5Shape`` class
    are in the py5 documentation.
    """
    pass


@overload
def create_shape(type: int, /) -> Py5Shape:
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
        either GROUP, PATH, or GEOMETRY

    Notes
    -----

    The ``create_shape()`` function is used to define a new shape. Once created,
    this shape can be drawn with the ``shape()`` function. The basic way to use the
    function defines new primitive shapes. One of the following parameters are used
    as the first parameter: ``ELLIPSE``, ``RECT``, ``ARC``, ``TRIANGLE``,
    ``SPHERE``, ``BOX``, ``QUAD``, or ``LINE``. The parameters for each of these
    different shapes are the same as their corresponding functions: ``ellipse()``,
    ``rect()``, ``arc()``, ``triangle()``, ``sphere()``, ``box()``, ``quad()``, and
    ``line()``. The first example clarifies how this works.

    Custom, unique shapes can be made by using ``create_shape()`` without a
    parameter. After the shape is started, the drawing attributes and geometry can
    be set directly to the shape within the ``begin_shape()`` and ``end_shape()``
    methods. See the second example for specifics, and the reference for
    ``begin_shape()`` for all of its options.

    The  ``create_shape()`` function can also be used to make a complex shape made
    of other shapes. This is called a "group" and it's created by using the
    parameter ``GROUP`` as the first parameter. See the fourth example to see how it
    works.

    After using ``create_shape()``, stroke and fill color can be set by calling
    methods like ``Py5Shape.set_fill()`` and ``Py5Shape.set_stroke()``, as seen in
    the examples. The complete list of methods and fields for the ``Py5Shape`` class
    are in the py5 documentation.
    """
    pass


@overload
def create_shape(kind: int, /, *p: float) -> Py5Shape:
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
        either GROUP, PATH, or GEOMETRY

    Notes
    -----

    The ``create_shape()`` function is used to define a new shape. Once created,
    this shape can be drawn with the ``shape()`` function. The basic way to use the
    function defines new primitive shapes. One of the following parameters are used
    as the first parameter: ``ELLIPSE``, ``RECT``, ``ARC``, ``TRIANGLE``,
    ``SPHERE``, ``BOX``, ``QUAD``, or ``LINE``. The parameters for each of these
    different shapes are the same as their corresponding functions: ``ellipse()``,
    ``rect()``, ``arc()``, ``triangle()``, ``sphere()``, ``box()``, ``quad()``, and
    ``line()``. The first example clarifies how this works.

    Custom, unique shapes can be made by using ``create_shape()`` without a
    parameter. After the shape is started, the drawing attributes and geometry can
    be set directly to the shape within the ``begin_shape()`` and ``end_shape()``
    methods. See the second example for specifics, and the reference for
    ``begin_shape()`` for all of its options.

    The  ``create_shape()`` function can also be used to make a complex shape made
    of other shapes. This is called a "group" and it's created by using the
    parameter ``GROUP`` as the first parameter. See the fourth example to see how it
    works.

    After using ``create_shape()``, stroke and fill color can be set by calling
    methods like ``Py5Shape.set_fill()`` and ``Py5Shape.set_stroke()``, as seen in
    the examples. The complete list of methods and fields for the ``Py5Shape`` class
    are in the py5 documentation.
    """
    pass


def create_shape(*args):
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
        either GROUP, PATH, or GEOMETRY

    Notes
    -----

    The ``create_shape()`` function is used to define a new shape. Once created,
    this shape can be drawn with the ``shape()`` function. The basic way to use the
    function defines new primitive shapes. One of the following parameters are used
    as the first parameter: ``ELLIPSE``, ``RECT``, ``ARC``, ``TRIANGLE``,
    ``SPHERE``, ``BOX``, ``QUAD``, or ``LINE``. The parameters for each of these
    different shapes are the same as their corresponding functions: ``ellipse()``,
    ``rect()``, ``arc()``, ``triangle()``, ``sphere()``, ``box()``, ``quad()``, and
    ``line()``. The first example clarifies how this works.

    Custom, unique shapes can be made by using ``create_shape()`` without a
    parameter. After the shape is started, the drawing attributes and geometry can
    be set directly to the shape within the ``begin_shape()`` and ``end_shape()``
    methods. See the second example for specifics, and the reference for
    ``begin_shape()`` for all of its options.

    The  ``create_shape()`` function can also be used to make a complex shape made
    of other shapes. This is called a "group" and it's created by using the
    parameter ``GROUP`` as the first parameter. See the fourth example to see how it
    works.

    After using ``create_shape()``, stroke and fill color can be set by calling
    methods like ``Py5Shape.set_fill()`` and ``Py5Shape.set_stroke()``, as seen in
    the examples. The complete list of methods and fields for the ``Py5Shape`` class
    are in the py5 documentation.
    """
    return _py5sketch.create_shape(*args)


@overload
def cursor() -> None:
    """Sets the cursor to a predefined symbol or an image, or makes it visible if
    already hidden.

    Underlying Java method: PApplet.cursor

    Methods
    -------

    You can use any of the following signatures:

     * cursor() -> None
     * cursor(img: Py5Image, /) -> None
     * cursor(img: Py5Image, x: int, y: int, /) -> None
     * cursor(kind: int, /) -> None

    Parameters
    ----------

    img: Py5Image
        any variable of type Py5Image

    kind: int
        either ARROW, CROSS, HAND, MOVE, TEXT, or WAIT

    x: int
        the horizontal active spot of the cursor

    y: int
        the vertical active spot of the cursor

    Notes
    -----

    Sets the cursor to a predefined symbol or an image, or makes it visible if
    already hidden. If you are trying to set an image as the cursor, the recommended
    size is 16x16 or 32x32 pixels. The values for parameters ``x`` and ``y`` must be
    less than the dimensions of the image.

    Setting or hiding the cursor does not generally work with "Present" mode (when
    running full-screen).

    With the ``P2D`` and ``P3D`` renderers, a generic set of cursors are used
    because the OpenGL renderer doesn't have access to the default cursor images for
    each platform (Processing Issue 3791).
    """
    pass


@overload
def cursor(kind: int, /) -> None:
    """Sets the cursor to a predefined symbol or an image, or makes it visible if
    already hidden.

    Underlying Java method: PApplet.cursor

    Methods
    -------

    You can use any of the following signatures:

     * cursor() -> None
     * cursor(img: Py5Image, /) -> None
     * cursor(img: Py5Image, x: int, y: int, /) -> None
     * cursor(kind: int, /) -> None

    Parameters
    ----------

    img: Py5Image
        any variable of type Py5Image

    kind: int
        either ARROW, CROSS, HAND, MOVE, TEXT, or WAIT

    x: int
        the horizontal active spot of the cursor

    y: int
        the vertical active spot of the cursor

    Notes
    -----

    Sets the cursor to a predefined symbol or an image, or makes it visible if
    already hidden. If you are trying to set an image as the cursor, the recommended
    size is 16x16 or 32x32 pixels. The values for parameters ``x`` and ``y`` must be
    less than the dimensions of the image.

    Setting or hiding the cursor does not generally work with "Present" mode (when
    running full-screen).

    With the ``P2D`` and ``P3D`` renderers, a generic set of cursors are used
    because the OpenGL renderer doesn't have access to the default cursor images for
    each platform (Processing Issue 3791).
    """
    pass


@overload
def cursor(img: Py5Image, /) -> None:
    """Sets the cursor to a predefined symbol or an image, or makes it visible if
    already hidden.

    Underlying Java method: PApplet.cursor

    Methods
    -------

    You can use any of the following signatures:

     * cursor() -> None
     * cursor(img: Py5Image, /) -> None
     * cursor(img: Py5Image, x: int, y: int, /) -> None
     * cursor(kind: int, /) -> None

    Parameters
    ----------

    img: Py5Image
        any variable of type Py5Image

    kind: int
        either ARROW, CROSS, HAND, MOVE, TEXT, or WAIT

    x: int
        the horizontal active spot of the cursor

    y: int
        the vertical active spot of the cursor

    Notes
    -----

    Sets the cursor to a predefined symbol or an image, or makes it visible if
    already hidden. If you are trying to set an image as the cursor, the recommended
    size is 16x16 or 32x32 pixels. The values for parameters ``x`` and ``y`` must be
    less than the dimensions of the image.

    Setting or hiding the cursor does not generally work with "Present" mode (when
    running full-screen).

    With the ``P2D`` and ``P3D`` renderers, a generic set of cursors are used
    because the OpenGL renderer doesn't have access to the default cursor images for
    each platform (Processing Issue 3791).
    """
    pass


@overload
def cursor(img: Py5Image, x: int, y: int, /) -> None:
    """Sets the cursor to a predefined symbol or an image, or makes it visible if
    already hidden.

    Underlying Java method: PApplet.cursor

    Methods
    -------

    You can use any of the following signatures:

     * cursor() -> None
     * cursor(img: Py5Image, /) -> None
     * cursor(img: Py5Image, x: int, y: int, /) -> None
     * cursor(kind: int, /) -> None

    Parameters
    ----------

    img: Py5Image
        any variable of type Py5Image

    kind: int
        either ARROW, CROSS, HAND, MOVE, TEXT, or WAIT

    x: int
        the horizontal active spot of the cursor

    y: int
        the vertical active spot of the cursor

    Notes
    -----

    Sets the cursor to a predefined symbol or an image, or makes it visible if
    already hidden. If you are trying to set an image as the cursor, the recommended
    size is 16x16 or 32x32 pixels. The values for parameters ``x`` and ``y`` must be
    less than the dimensions of the image.

    Setting or hiding the cursor does not generally work with "Present" mode (when
    running full-screen).

    With the ``P2D`` and ``P3D`` renderers, a generic set of cursors are used
    because the OpenGL renderer doesn't have access to the default cursor images for
    each platform (Processing Issue 3791).
    """
    pass


def cursor(*args):
    """Sets the cursor to a predefined symbol or an image, or makes it visible if
    already hidden.

    Underlying Java method: PApplet.cursor

    Methods
    -------

    You can use any of the following signatures:

     * cursor() -> None
     * cursor(img: Py5Image, /) -> None
     * cursor(img: Py5Image, x: int, y: int, /) -> None
     * cursor(kind: int, /) -> None

    Parameters
    ----------

    img: Py5Image
        any variable of type Py5Image

    kind: int
        either ARROW, CROSS, HAND, MOVE, TEXT, or WAIT

    x: int
        the horizontal active spot of the cursor

    y: int
        the vertical active spot of the cursor

    Notes
    -----

    Sets the cursor to a predefined symbol or an image, or makes it visible if
    already hidden. If you are trying to set an image as the cursor, the recommended
    size is 16x16 or 32x32 pixels. The values for parameters ``x`` and ``y`` must be
    less than the dimensions of the image.

    Setting or hiding the cursor does not generally work with "Present" mode (when
    running full-screen).

    With the ``P2D`` and ``P3D`` renderers, a generic set of cursors are used
    because the OpenGL renderer doesn't have access to the default cursor images for
    each platform (Processing Issue 3791).
    """
    return _py5sketch.cursor(*args)


@overload
def curve(x1: float, y1: float, x2: float, y2: float, x3: float,
          y3: float, x4: float, y4: float, /) -> None:
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
    rendering with ``P3D``.
    """
    pass


@overload
def curve(x1: float, y1: float, z1: float, x2: float, y2: float, z2: float,
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
    rendering with ``P3D``.
    """
    pass


def curve(*args):
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
    rendering with ``P3D``.
    """
    return _py5sketch.curve(*args)


def curve_detail(detail: int, /) -> None:
    """Sets the resolution at which curves display.

    Underlying Java method: PApplet.curveDetail

    Parameters
    ----------

    detail: int
        resolution of the curves

    Notes
    -----

    Sets the resolution at which curves display. The default value is 20. This
    function is only useful when using the ``P3D`` renderer as the default ``P2D``
    renderer does not use this information.
    """
    return _py5sketch.curve_detail(detail)


def curve_point(a: float, b: float, c: float, d: float, t: float, /) -> float:
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
    on the curve. As seen in the example, this can be used once with the ``x``
    coordinates and a second time with the ``y`` coordinates to get the location of
    a curve at ``t``.
    """
    return _py5sketch.curve_point(a, b, c, d, t)


def curve_tangent(a: float, b: float, c: float,
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
    return _py5sketch.curve_tangent(a, b, c, d, t)


def curve_tightness(tightness: float, /) -> None:
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
    return _py5sketch.curve_tightness(tightness)


@overload
def curve_vertex(x: float, y: float, /) -> None:
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

    Specifies vertex coordinates for curves. This method may only be used between
    ``begin_shape()`` and ``end_shape()`` and only when there is no ``MODE``
    parameter specified to ``begin_shape()``. The first and last points in a series
    of ``curve_vertex()`` lines will be used to guide the beginning and end of the
    curve. A minimum of four points is required to draw a tiny curve between the
    second and third points. Adding a fifth point with ``curve_vertex()`` will draw
    the curve between the second, third, and fourth points. The ``curve_vertex()``
    method is an implementation of Catmull-Rom splines. Using the 3D version
    requires rendering with ``P3D``.
    """
    pass


@overload
def curve_vertex(x: float, y: float, z: float, /) -> None:
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

    Specifies vertex coordinates for curves. This method may only be used between
    ``begin_shape()`` and ``end_shape()`` and only when there is no ``MODE``
    parameter specified to ``begin_shape()``. The first and last points in a series
    of ``curve_vertex()`` lines will be used to guide the beginning and end of the
    curve. A minimum of four points is required to draw a tiny curve between the
    second and third points. Adding a fifth point with ``curve_vertex()`` will draw
    the curve between the second, third, and fourth points. The ``curve_vertex()``
    method is an implementation of Catmull-Rom splines. Using the 3D version
    requires rendering with ``P3D``.
    """
    pass


def curve_vertex(*args):
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

    Specifies vertex coordinates for curves. This method may only be used between
    ``begin_shape()`` and ``end_shape()`` and only when there is no ``MODE``
    parameter specified to ``begin_shape()``. The first and last points in a series
    of ``curve_vertex()`` lines will be used to guide the beginning and end of the
    curve. A minimum of four points is required to draw a tiny curve between the
    second and third points. Adding a fifth point with ``curve_vertex()`` will draw
    the curve between the second, third, and fourth points. The ``curve_vertex()``
    method is an implementation of Catmull-Rom splines. Using the 3D version
    requires rendering with ``P3D``.
    """
    return _py5sketch.curve_vertex(*args)


def curve_vertices(coordinates: NDArray[(Any, Any), Float], /) -> None:
    """Create a collection of curve vertices.

    Underlying Java method: PApplet.curveVertices

    Parameters
    ----------

    coordinates: NDArray[(Any, Any), Float]
        array of curve vertex coordinates

    Notes
    -----

    Create a collection of curve vertices. The purpose of this method is to provide
    an alternative to repeatedly calling ``curve_vertex()`` in a loop. For a large
    number of curve vertices, the performance of ``curve_vertices()`` will be much
    faster.

    The ``coordinates`` parameter should be a numpy array with one row for each
    curve vertex.  There should be two or three columns for 2D or 3D points,
    respectively.
    """
    return _py5sketch.curve_vertices(coordinates)


def day() -> int:
    """Py5 communicates with the clock on your computer.

    Underlying Java method: PApplet.day

    Notes
    -----

    Py5 communicates with the clock on your computer. The ``day()`` function returns
    the current day as a value from 1 - 31.
    """
    return Sketch.day()


def directional_light(v1: float, v2: float, v3: float,
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
    ``v3`` parameters are interpreted as either ``RGB`` or ``HSB`` values, depending
    on the current color mode. The ``nx``, ``ny``, and ``nz`` parameters specify the
    direction the light is facing. For example, setting ``ny`` to -1 will cause the
    geometry to be lit from below (since the light would be facing directly upward).
    """
    return _py5sketch.directional_light(v1, v2, v3, nx, ny, nz)


@overload
def display_density() -> int:
    """This function returns the number "2" if the screen is a high-density screen
    (called a Retina display on OSX or high-dpi on Windows and Linux) and a "1" if
    not.

    Underlying Java method: PApplet.displayDensity

    Methods
    -------

    You can use any of the following signatures:

     * display_density() -> int
     * display_density(display: int, /) -> int

    Parameters
    ----------

    display: int
        the display number to check (1-indexed to match the Preferences dialog box)

    Notes
    -----

    This function returns the number "2" if the screen is a high-density screen
    (called a Retina display on OSX or high-dpi on Windows and Linux) and a "1" if
    not. This information is useful for a program to adapt to run at double the
    pixel density on a screen that supports it.
    """
    pass


@overload
def display_density(display: int, /) -> int:
    """This function returns the number "2" if the screen is a high-density screen
    (called a Retina display on OSX or high-dpi on Windows and Linux) and a "1" if
    not.

    Underlying Java method: PApplet.displayDensity

    Methods
    -------

    You can use any of the following signatures:

     * display_density() -> int
     * display_density(display: int, /) -> int

    Parameters
    ----------

    display: int
        the display number to check (1-indexed to match the Preferences dialog box)

    Notes
    -----

    This function returns the number "2" if the screen is a high-density screen
    (called a Retina display on OSX or high-dpi on Windows and Linux) and a "1" if
    not. This information is useful for a program to adapt to run at double the
    pixel density on a screen that supports it.
    """
    pass


def display_density(*args):
    """This function returns the number "2" if the screen is a high-density screen
    (called a Retina display on OSX or high-dpi on Windows and Linux) and a "1" if
    not.

    Underlying Java method: PApplet.displayDensity

    Methods
    -------

    You can use any of the following signatures:

     * display_density() -> int
     * display_density(display: int, /) -> int

    Parameters
    ----------

    display: int
        the display number to check (1-indexed to match the Preferences dialog box)

    Notes
    -----

    This function returns the number "2" if the screen is a high-density screen
    (called a Retina display on OSX or high-dpi on Windows and Linux) and a "1" if
    not. This information is useful for a program to adapt to run at double the
    pixel density on a screen that supports it.
    """
    return _py5sketch.display_density(*args)


def ellipse(a: float, b: float, c: float, d: float, /) -> None:
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
    return _py5sketch.ellipse(a, b, c, d)


def ellipse_mode(mode: int, /) -> None:
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

    The parameter must be written in ALL CAPS because Python is a case-sensitive
    language.
    """
    return _py5sketch.ellipse_mode(mode)


@overload
def emissive(gray: float, /) -> None:
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
    screen. Use in combination with ``ambient()``, ``specular()``, and
    ``shininess()`` to set the material properties of shapes.
    """
    pass


@overload
def emissive(v1: float, v2: float, v3: float, /) -> None:
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
    screen. Use in combination with ``ambient()``, ``specular()``, and
    ``shininess()`` to set the material properties of shapes.
    """
    pass


@overload
def emissive(rgb: int, /) -> None:
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
    screen. Use in combination with ``ambient()``, ``specular()``, and
    ``shininess()`` to set the material properties of shapes.
    """
    pass


def emissive(*args):
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
    screen. Use in combination with ``ambient()``, ``specular()``, and
    ``shininess()`` to set the material properties of shapes.
    """
    return _py5sketch.emissive(*args)


def end_camera() -> None:
    """The ``begin_camera()`` and ``end_camera()`` methods enable advanced
    customization of the camera space.

    Underlying Java method: PApplet.endCamera

    Notes
    -----

    The ``begin_camera()`` and ``end_camera()`` methods enable advanced
    customization of the camera space. Please see the reference for
    ``begin_camera()`` for a description of how the methods are used.
    """
    return _py5sketch.end_camera()


def end_contour() -> None:
    """Use the ``begin_contour()`` and ``end_contour()`` methods to create negative
    shapes within shapes such as the center of the letter 'O'.

    Underlying Java method: PApplet.endContour

    Notes
    -----

    Use the ``begin_contour()`` and ``end_contour()`` methods to create negative
    shapes within shapes such as the center of the letter 'O'. The
    ``begin_contour()`` method begins recording vertices for the shape and
    ``end_contour()`` stops recording. The vertices that define a negative shape
    must "wind" in the opposite direction from the exterior shape. First draw
    vertices for the exterior shape in clockwise order, then for internal shapes,
    draw vertices counterclockwise.

    These methods can only be used within a ``begin_shape()`` & ``end_shape()`` pair
    and transformations such as ``translate()``, ``rotate()``, and ``scale()`` do
    not work within a ``begin_contour()`` & ``end_contour()`` pair. It is also not
    possible to use other shapes, such as ``ellipse()`` or ``rect()`` within.
    """
    return _py5sketch.end_contour()


def end_raw() -> None:
    """Complement to ``begin_raw()``; they must always be used together.

    Underlying Java method: PApplet.endRaw

    Notes
    -----

    Complement to ``begin_raw()``; they must always be used together. See the
    ``begin_raw()`` reference for details.
    """
    return _py5sketch.end_raw()


def end_record() -> None:
    """Stops the recording process started by ``begin_record()`` and closes the file.

    Underlying Java method: PApplet.endRecord

    Notes
    -----

    Stops the recording process started by ``begin_record()`` and closes the file.
    """
    return _py5sketch.end_record()


@overload
def end_shape() -> None:
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
    image buffer. The constant ``CLOSE`` as the value for the ``MODE`` parameter to
    close the shape (to connect the beginning and the end).
    """
    pass


@overload
def end_shape(mode: int, /) -> None:
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
    image buffer. The constant ``CLOSE`` as the value for the ``MODE`` parameter to
    close the shape (to connect the beginning and the end).
    """
    pass


def end_shape(*args):
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
    image buffer. The constant ``CLOSE`` as the value for the ``MODE`` parameter to
    close the shape (to connect the beginning and the end).
    """
    return _py5sketch.end_shape(*args)


def exit_sketch() -> None:
    """Quits/stops/exits the program.

    Underlying Java method: PApplet.exit

    Notes
    -----

    Quits/stops/exits the program. Programs without a ``draw()`` function stop
    automatically after the last line has run, but programs with ``draw()`` run
    continuously until the program is manually stopped or ``exit_sketch()`` is run.

    Rather than terminating immediately, ``exit_sketch()`` will cause the Sketch to
    exit after ``draw()`` has completed (or after ``setup()`` completes if called
    during the ``setup()`` function).

    For Python programmers, this is *not* the same as ``sys.exit()``. Further,
    ``sys.exit()`` should not be used because closing out an application while
    ``draw()`` is running may cause a crash (particularly with ``P3D``).
    """
    return _py5sketch.exit_sketch()


@overload
def fill(gray: float, /) -> None:
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
    specified in terms of the ``RGB`` or ``HSB`` color depending on the current
    ``color_mode()``. The default color space is ``RGB``, with each value in the
    range from 0 to 255.

    When using hexadecimal notation to specify a color, use "``0x``" before the
    values (e.g., ``0xFFCCFFAA``). The hexadecimal value must be specified with
    eight characters; the first two characters define the alpha component, and the
    remainder define the red, green, and blue components.

    The value for the "gray" parameter must be less than or equal to the current
    maximum value as specified by ``color_mode()``. The default maximum value is
    255.

    To change the color of an image or a texture, use ``tint()``.
    """
    pass


@overload
def fill(gray: float, alpha: float, /) -> None:
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
    specified in terms of the ``RGB`` or ``HSB`` color depending on the current
    ``color_mode()``. The default color space is ``RGB``, with each value in the
    range from 0 to 255.

    When using hexadecimal notation to specify a color, use "``0x``" before the
    values (e.g., ``0xFFCCFFAA``). The hexadecimal value must be specified with
    eight characters; the first two characters define the alpha component, and the
    remainder define the red, green, and blue components.

    The value for the "gray" parameter must be less than or equal to the current
    maximum value as specified by ``color_mode()``. The default maximum value is
    255.

    To change the color of an image or a texture, use ``tint()``.
    """
    pass


@overload
def fill(v1: float, v2: float, v3: float, /) -> None:
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
    specified in terms of the ``RGB`` or ``HSB`` color depending on the current
    ``color_mode()``. The default color space is ``RGB``, with each value in the
    range from 0 to 255.

    When using hexadecimal notation to specify a color, use "``0x``" before the
    values (e.g., ``0xFFCCFFAA``). The hexadecimal value must be specified with
    eight characters; the first two characters define the alpha component, and the
    remainder define the red, green, and blue components.

    The value for the "gray" parameter must be less than or equal to the current
    maximum value as specified by ``color_mode()``. The default maximum value is
    255.

    To change the color of an image or a texture, use ``tint()``.
    """
    pass


@overload
def fill(v1: float, v2: float, v3: float, alpha: float, /) -> None:
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
    specified in terms of the ``RGB`` or ``HSB`` color depending on the current
    ``color_mode()``. The default color space is ``RGB``, with each value in the
    range from 0 to 255.

    When using hexadecimal notation to specify a color, use "``0x``" before the
    values (e.g., ``0xFFCCFFAA``). The hexadecimal value must be specified with
    eight characters; the first two characters define the alpha component, and the
    remainder define the red, green, and blue components.

    The value for the "gray" parameter must be less than or equal to the current
    maximum value as specified by ``color_mode()``. The default maximum value is
    255.

    To change the color of an image or a texture, use ``tint()``.
    """
    pass


@overload
def fill(rgb: int, /) -> None:
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
    specified in terms of the ``RGB`` or ``HSB`` color depending on the current
    ``color_mode()``. The default color space is ``RGB``, with each value in the
    range from 0 to 255.

    When using hexadecimal notation to specify a color, use "``0x``" before the
    values (e.g., ``0xFFCCFFAA``). The hexadecimal value must be specified with
    eight characters; the first two characters define the alpha component, and the
    remainder define the red, green, and blue components.

    The value for the "gray" parameter must be less than or equal to the current
    maximum value as specified by ``color_mode()``. The default maximum value is
    255.

    To change the color of an image or a texture, use ``tint()``.
    """
    pass


@overload
def fill(rgb: int, alpha: float, /) -> None:
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
    specified in terms of the ``RGB`` or ``HSB`` color depending on the current
    ``color_mode()``. The default color space is ``RGB``, with each value in the
    range from 0 to 255.

    When using hexadecimal notation to specify a color, use "``0x``" before the
    values (e.g., ``0xFFCCFFAA``). The hexadecimal value must be specified with
    eight characters; the first two characters define the alpha component, and the
    remainder define the red, green, and blue components.

    The value for the "gray" parameter must be less than or equal to the current
    maximum value as specified by ``color_mode()``. The default maximum value is
    255.

    To change the color of an image or a texture, use ``tint()``.
    """
    pass


def fill(*args):
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
    specified in terms of the ``RGB`` or ``HSB`` color depending on the current
    ``color_mode()``. The default color space is ``RGB``, with each value in the
    range from 0 to 255.

    When using hexadecimal notation to specify a color, use "``0x``" before the
    values (e.g., ``0xFFCCFFAA``). The hexadecimal value must be specified with
    eight characters; the first two characters define the alpha component, and the
    remainder define the red, green, and blue components.

    The value for the "gray" parameter must be less than or equal to the current
    maximum value as specified by ``color_mode()``. The default maximum value is
    255.

    To change the color of an image or a texture, use ``tint()``.
    """
    return _py5sketch.fill(*args)


@overload
def apply_filter(kind: int, /) -> None:
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
    the ``P2D`` or ``P3D`` renderer in ``size()``.

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
    """
    pass


@overload
def apply_filter(kind: int, param: float, /) -> None:
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
    the ``P2D`` or ``P3D`` renderer in ``size()``.

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
    """
    pass


@overload
def apply_filter(shader: Py5Shader, /) -> None:
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
    the ``P2D`` or ``P3D`` renderer in ``size()``.

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
    """
    pass


def apply_filter(*args):
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
    the ``P2D`` or ``P3D`` renderer in ``size()``.

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
    """
    return _py5sketch.apply_filter(*args)


def frame_rate(fps: float, /) -> None:
    """Specifies the number of frames to be displayed every second.

    Underlying Java method: PApplet.frameRate

    Parameters
    ----------

    fps: float
        number of desired frames per second

    Notes
    -----

    Specifies the number of frames to be displayed every second. For example, the
    function call ``frame_rate(30)`` will attempt to refresh 30 times a second. If
    the processor is not fast enough to maintain the specified rate, the frame rate
    will not be achieved. Setting the frame rate within ``setup()`` is recommended.
    The default rate is 60 frames per second.
    """
    return _py5sketch.frame_rate(fps)


def frustum(left: float, right: float, bottom: float,
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
    return _py5sketch.frustum(left, right, bottom, top, near, far)


@overload
def full_screen() -> None:
    """Open a Sketch using the full size of the computer's display.

    Underlying Java method: PApplet.fullScreen

    Methods
    -------

    You can use any of the following signatures:

     * full_screen() -> None
     * full_screen(display: int, /) -> None
     * full_screen(renderer: str, /) -> None
     * full_screen(renderer: str, display: int, /) -> None

    Parameters
    ----------

    display: int
        the screen to run the Sketch on (1, 2, 3, etc. or on multiple screens using SPAN)

    renderer: str
        the renderer to use, e.g. P2D, P3D, JAVA2D (default)

    Notes
    -----

    Open a Sketch using the full size of the computer's display. This function must
    be called in ``settings()``. The ``size()`` and ``full_screen()`` functions
    cannot both be used in the same program.

    When ``full_screen()`` is used without a parameter on a computer with multiple
    monitors, it will (probably) draw the Sketch to the primary display. When it is
    used with a single parameter, this number defines the screen to display to
    program on (e.g. 1, 2, 3...). When used with two parameters, the first defines
    the renderer to use (e.g. P2D) and the second defines the screen. The ``SPAN``
    parameter can be used in place of a screen number to draw the Sketch as a full-
    screen window across all of the attached displays if there are more than one.
    """
    pass


@overload
def full_screen(display: int, /) -> None:
    """Open a Sketch using the full size of the computer's display.

    Underlying Java method: PApplet.fullScreen

    Methods
    -------

    You can use any of the following signatures:

     * full_screen() -> None
     * full_screen(display: int, /) -> None
     * full_screen(renderer: str, /) -> None
     * full_screen(renderer: str, display: int, /) -> None

    Parameters
    ----------

    display: int
        the screen to run the Sketch on (1, 2, 3, etc. or on multiple screens using SPAN)

    renderer: str
        the renderer to use, e.g. P2D, P3D, JAVA2D (default)

    Notes
    -----

    Open a Sketch using the full size of the computer's display. This function must
    be called in ``settings()``. The ``size()`` and ``full_screen()`` functions
    cannot both be used in the same program.

    When ``full_screen()`` is used without a parameter on a computer with multiple
    monitors, it will (probably) draw the Sketch to the primary display. When it is
    used with a single parameter, this number defines the screen to display to
    program on (e.g. 1, 2, 3...). When used with two parameters, the first defines
    the renderer to use (e.g. P2D) and the second defines the screen. The ``SPAN``
    parameter can be used in place of a screen number to draw the Sketch as a full-
    screen window across all of the attached displays if there are more than one.
    """
    pass


@overload
def full_screen(renderer: str, /) -> None:
    """Open a Sketch using the full size of the computer's display.

    Underlying Java method: PApplet.fullScreen

    Methods
    -------

    You can use any of the following signatures:

     * full_screen() -> None
     * full_screen(display: int, /) -> None
     * full_screen(renderer: str, /) -> None
     * full_screen(renderer: str, display: int, /) -> None

    Parameters
    ----------

    display: int
        the screen to run the Sketch on (1, 2, 3, etc. or on multiple screens using SPAN)

    renderer: str
        the renderer to use, e.g. P2D, P3D, JAVA2D (default)

    Notes
    -----

    Open a Sketch using the full size of the computer's display. This function must
    be called in ``settings()``. The ``size()`` and ``full_screen()`` functions
    cannot both be used in the same program.

    When ``full_screen()`` is used without a parameter on a computer with multiple
    monitors, it will (probably) draw the Sketch to the primary display. When it is
    used with a single parameter, this number defines the screen to display to
    program on (e.g. 1, 2, 3...). When used with two parameters, the first defines
    the renderer to use (e.g. P2D) and the second defines the screen. The ``SPAN``
    parameter can be used in place of a screen number to draw the Sketch as a full-
    screen window across all of the attached displays if there are more than one.
    """
    pass


@overload
def full_screen(renderer: str, display: int, /) -> None:
    """Open a Sketch using the full size of the computer's display.

    Underlying Java method: PApplet.fullScreen

    Methods
    -------

    You can use any of the following signatures:

     * full_screen() -> None
     * full_screen(display: int, /) -> None
     * full_screen(renderer: str, /) -> None
     * full_screen(renderer: str, display: int, /) -> None

    Parameters
    ----------

    display: int
        the screen to run the Sketch on (1, 2, 3, etc. or on multiple screens using SPAN)

    renderer: str
        the renderer to use, e.g. P2D, P3D, JAVA2D (default)

    Notes
    -----

    Open a Sketch using the full size of the computer's display. This function must
    be called in ``settings()``. The ``size()`` and ``full_screen()`` functions
    cannot both be used in the same program.

    When ``full_screen()`` is used without a parameter on a computer with multiple
    monitors, it will (probably) draw the Sketch to the primary display. When it is
    used with a single parameter, this number defines the screen to display to
    program on (e.g. 1, 2, 3...). When used with two parameters, the first defines
    the renderer to use (e.g. P2D) and the second defines the screen. The ``SPAN``
    parameter can be used in place of a screen number to draw the Sketch as a full-
    screen window across all of the attached displays if there are more than one.
    """
    pass


def full_screen(*args):
    """Open a Sketch using the full size of the computer's display.

    Underlying Java method: PApplet.fullScreen

    Methods
    -------

    You can use any of the following signatures:

     * full_screen() -> None
     * full_screen(display: int, /) -> None
     * full_screen(renderer: str, /) -> None
     * full_screen(renderer: str, display: int, /) -> None

    Parameters
    ----------

    display: int
        the screen to run the Sketch on (1, 2, 3, etc. or on multiple screens using SPAN)

    renderer: str
        the renderer to use, e.g. P2D, P3D, JAVA2D (default)

    Notes
    -----

    Open a Sketch using the full size of the computer's display. This function must
    be called in ``settings()``. The ``size()`` and ``full_screen()`` functions
    cannot both be used in the same program.

    When ``full_screen()`` is used without a parameter on a computer with multiple
    monitors, it will (probably) draw the Sketch to the primary display. When it is
    used with a single parameter, this number defines the screen to display to
    program on (e.g. 1, 2, 3...). When used with two parameters, the first defines
    the renderer to use (e.g. P2D) and the second defines the screen. The ``SPAN``
    parameter can be used in place of a screen number to draw the Sketch as a full-
    screen window across all of the attached displays if there are more than one.
    """
    return _py5sketch.full_screen(*args)


@overload
def get() -> Py5Image:
    """Reads the color of any pixel or grabs a section of the drawing surface.

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

    Reads the color of any pixel or grabs a section of the drawing surface. If no
    parameters are specified, the entire drawing surface is returned. Use the ``x``
    and ``y`` parameters to get the value of one pixel. Get a section of the display
    window by specifying additional ``w`` and ``h`` parameters. When getting an
    image, the ``x`` and ``y`` parameters define the coordinates for the upper-left
    corner of the returned image, regardless of the current ``image_mode()``.

    If the pixel requested is outside of the image window, black is returned. The
    numbers returned are scaled according to the current color ranges, but only
    ``RGB`` values are returned by this function. For example, even though you may
    have drawn a shape with ``color_mode(HSB)``, the numbers returned will be in
    ``RGB`` format.

    If a width and a height are specified, ``get(x, y, w, h)`` returns a Py5Image
    corresponding to the part of the original Py5Image where the top left pixel is
    at the ``(x, y)`` position with a width of ``w`` a height of ``h``.

    Getting the color of a single pixel with ``get(x, y)`` is easy, but not as fast
    as grabbing the data directly from ``pixels[]`` or ``np_pixels[]``. The
    equivalent statement to ``get(x, y)`` using ``pixels[]`` is
    ``pixels[y*width+x]``. Using ``np_pixels[]`` it is ``np_pixels[y, x]``. See the
    reference for ``pixels[]`` and ``np_pixels[]`` for more information.
    """
    pass


@overload
def get(x: int, y: int, /) -> int:
    """Reads the color of any pixel or grabs a section of the drawing surface.

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

    Reads the color of any pixel or grabs a section of the drawing surface. If no
    parameters are specified, the entire drawing surface is returned. Use the ``x``
    and ``y`` parameters to get the value of one pixel. Get a section of the display
    window by specifying additional ``w`` and ``h`` parameters. When getting an
    image, the ``x`` and ``y`` parameters define the coordinates for the upper-left
    corner of the returned image, regardless of the current ``image_mode()``.

    If the pixel requested is outside of the image window, black is returned. The
    numbers returned are scaled according to the current color ranges, but only
    ``RGB`` values are returned by this function. For example, even though you may
    have drawn a shape with ``color_mode(HSB)``, the numbers returned will be in
    ``RGB`` format.

    If a width and a height are specified, ``get(x, y, w, h)`` returns a Py5Image
    corresponding to the part of the original Py5Image where the top left pixel is
    at the ``(x, y)`` position with a width of ``w`` a height of ``h``.

    Getting the color of a single pixel with ``get(x, y)`` is easy, but not as fast
    as grabbing the data directly from ``pixels[]`` or ``np_pixels[]``. The
    equivalent statement to ``get(x, y)`` using ``pixels[]`` is
    ``pixels[y*width+x]``. Using ``np_pixels[]`` it is ``np_pixels[y, x]``. See the
    reference for ``pixels[]`` and ``np_pixels[]`` for more information.
    """
    pass


@overload
def get(x: int, y: int, w: int, h: int, /) -> Py5Image:
    """Reads the color of any pixel or grabs a section of the drawing surface.

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

    Reads the color of any pixel or grabs a section of the drawing surface. If no
    parameters are specified, the entire drawing surface is returned. Use the ``x``
    and ``y`` parameters to get the value of one pixel. Get a section of the display
    window by specifying additional ``w`` and ``h`` parameters. When getting an
    image, the ``x`` and ``y`` parameters define the coordinates for the upper-left
    corner of the returned image, regardless of the current ``image_mode()``.

    If the pixel requested is outside of the image window, black is returned. The
    numbers returned are scaled according to the current color ranges, but only
    ``RGB`` values are returned by this function. For example, even though you may
    have drawn a shape with ``color_mode(HSB)``, the numbers returned will be in
    ``RGB`` format.

    If a width and a height are specified, ``get(x, y, w, h)`` returns a Py5Image
    corresponding to the part of the original Py5Image where the top left pixel is
    at the ``(x, y)`` position with a width of ``w`` a height of ``h``.

    Getting the color of a single pixel with ``get(x, y)`` is easy, but not as fast
    as grabbing the data directly from ``pixels[]`` or ``np_pixels[]``. The
    equivalent statement to ``get(x, y)`` using ``pixels[]`` is
    ``pixels[y*width+x]``. Using ``np_pixels[]`` it is ``np_pixels[y, x]``. See the
    reference for ``pixels[]`` and ``np_pixels[]`` for more information.
    """
    pass


def get(*args):
    """Reads the color of any pixel or grabs a section of the drawing surface.

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

    Reads the color of any pixel or grabs a section of the drawing surface. If no
    parameters are specified, the entire drawing surface is returned. Use the ``x``
    and ``y`` parameters to get the value of one pixel. Get a section of the display
    window by specifying additional ``w`` and ``h`` parameters. When getting an
    image, the ``x`` and ``y`` parameters define the coordinates for the upper-left
    corner of the returned image, regardless of the current ``image_mode()``.

    If the pixel requested is outside of the image window, black is returned. The
    numbers returned are scaled according to the current color ranges, but only
    ``RGB`` values are returned by this function. For example, even though you may
    have drawn a shape with ``color_mode(HSB)``, the numbers returned will be in
    ``RGB`` format.

    If a width and a height are specified, ``get(x, y, w, h)`` returns a Py5Image
    corresponding to the part of the original Py5Image where the top left pixel is
    at the ``(x, y)`` position with a width of ``w`` a height of ``h``.

    Getting the color of a single pixel with ``get(x, y)`` is easy, but not as fast
    as grabbing the data directly from ``pixels[]`` or ``np_pixels[]``. The
    equivalent statement to ``get(x, y)`` using ``pixels[]`` is
    ``pixels[y*width+x]``. Using ``np_pixels[]`` it is ``np_pixels[y, x]``. See the
    reference for ``pixels[]`` and ``np_pixels[]`` for more information.
    """
    return _py5sketch.get(*args)


def get_frame_rate() -> float:
    """Get the running Sketch's current frame rate.

    Underlying Java method: PApplet.getFrameRate

    Notes
    -----

    Get the running Sketch's current frame rate. This is measured in frames per
    second (fps) and uses an exponential moving average. The returned value will not
    be accurate until after the Sketch has run for a few seconds. You can set the
    target frame rate with ``frame_rate()``.

    This method provides the same information as Processing's ``frameRate``
    variable. Python can't have a variable and a method with the same name, so a new
    method was created to provide access to that variable.
    """
    return _py5sketch.get_frame_rate()


def get_graphics() -> Py5Graphics:
    """Get the ``Py5Graphics`` object used by the Sketch.

    Underlying Java method: PApplet.getGraphics

    Notes
    -----

    Get the ``Py5Graphics`` object used by the Sketch. Internally, all of
    Processing's drawing functionality comes from interaction with PGraphics
    objects, and this will provide direct access to the PGraphics object used by the
    Sketch.
    """
    return _py5sketch.get_graphics()


@overload
def get_matrix() -> NDArray[(Any, Any), Float]:
    """Get the current matrix as a numpy array.

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
        transformation matrix data

    target: NDArray[(4, 4), Float]
        transformation matrix data

    Notes
    -----

    Get the current matrix as a numpy array. Use the ``target`` parameter to put the
    matrix data in a properly sized and typed numpy array.
    """
    pass


@overload
def get_matrix(target: NDArray[(2, 3), Float], /) -> NDArray[(2, 3), Float]:
    """Get the current matrix as a numpy array.

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
        transformation matrix data

    target: NDArray[(4, 4), Float]
        transformation matrix data

    Notes
    -----

    Get the current matrix as a numpy array. Use the ``target`` parameter to put the
    matrix data in a properly sized and typed numpy array.
    """
    pass


@overload
def get_matrix(target: NDArray[(4, 4), Float], /) -> NDArray[(4, 4), Float]:
    """Get the current matrix as a numpy array.

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
        transformation matrix data

    target: NDArray[(4, 4), Float]
        transformation matrix data

    Notes
    -----

    Get the current matrix as a numpy array. Use the ``target`` parameter to put the
    matrix data in a properly sized and typed numpy array.
    """
    pass


def get_matrix(*args):
    """Get the current matrix as a numpy array.

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
        transformation matrix data

    target: NDArray[(4, 4), Float]
        transformation matrix data

    Notes
    -----

    Get the current matrix as a numpy array. Use the ``target`` parameter to put the
    matrix data in a properly sized and typed numpy array.
    """
    return _py5sketch.get_matrix(*args)


def get_surface() -> Py5Surface:
    """Get the Py5Surface object used for the Sketch.

    Underlying Java method: PApplet.getSurface

    Notes
    -----

    Get the Py5Surface object used for the Sketch.
    """
    return _py5sketch.get_surface()


def green(rgb: int, /) -> float:
    """Extracts the green value from a color, scaled to match current ``color_mode()``.

    Underlying Java method: PApplet.green

    Parameters
    ----------

    rgb: int
        any value of the color datatype

    Notes
    -----

    Extracts the green value from a color, scaled to match current ``color_mode()``.

    The ``green()`` function is easy to use and understand, but it is slower than a
    technique called bit shifting. When working in ``color_mode(RGB, 255)``, you can
    achieve the same results as ``green()`` but with greater speed by using the
    right shift operator (``>>``) with a bit mask. For example, ``green(c)`` and ``c
    >> 8 & 0xFF`` both extract the green value from a color variable ``c`` but the
    later is faster.
    """
    return _py5sketch.green(rgb)


def hint(which: int, /) -> None:
    """This function is used to enable or disable special features that control how
    graphics are drawn.

    Underlying Java method: PApplet.hint

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
    rendered using small steps (for instance, using ``vertex()`` with points that
    are close to one another), or are drawn at small sizes.

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
    """
    return _py5sketch.hint(which)


def hour() -> int:
    """Py5 communicates with the clock on your computer.

    Underlying Java method: PApplet.hour

    Notes
    -----

    Py5 communicates with the clock on your computer. The ``hour()`` function
    returns the current hour as a value from 0 - 23.
    """
    return Sketch.hour()


def hue(rgb: int, /) -> float:
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
    return _py5sketch.hue(rgb)


@overload
def image(img: Py5Image, a: float, b: float, /) -> None:
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
        x-coordinate of the upper left corner of image subset

    u2: int
        y-coordinate of the upper left corner of image subset

    v1: int
        x-coordinate of the lower right corner of image subset

    v2: int
        y-coordinate of the lower right corner of image subset

    Notes
    -----

    The ``image()`` function draws an image to the display window. Images must be in
    the Sketch's "data" directory to load correctly. Py5 currently works with GIF,
    JPEG, and PNG images.

    The ``img`` parameter specifies the image to display and by default the ``a``
    and ``b`` parameters define the location of its upper-left corner. The image is
    displayed at its original size unless the ``c`` and ``d`` parameters specify a
    different size. The ``image_mode()`` function can be used to change the way
    these parameters draw the image.

    Use the ``u1``, ``u2``, ``v1``, and ``v2`` parameters to use only a subset of
    the image. These values are always specified in image space location, regardless
    of the current ``texture_mode()`` setting.

    The color of an image may be modified with the ``tint()`` function. This
    function will maintain transparency for GIF and PNG images.
    """
    pass


@overload
def image(img: Py5Image, a: float, b: float, c: float, d: float, /) -> None:
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
        x-coordinate of the upper left corner of image subset

    u2: int
        y-coordinate of the upper left corner of image subset

    v1: int
        x-coordinate of the lower right corner of image subset

    v2: int
        y-coordinate of the lower right corner of image subset

    Notes
    -----

    The ``image()`` function draws an image to the display window. Images must be in
    the Sketch's "data" directory to load correctly. Py5 currently works with GIF,
    JPEG, and PNG images.

    The ``img`` parameter specifies the image to display and by default the ``a``
    and ``b`` parameters define the location of its upper-left corner. The image is
    displayed at its original size unless the ``c`` and ``d`` parameters specify a
    different size. The ``image_mode()`` function can be used to change the way
    these parameters draw the image.

    Use the ``u1``, ``u2``, ``v1``, and ``v2`` parameters to use only a subset of
    the image. These values are always specified in image space location, regardless
    of the current ``texture_mode()`` setting.

    The color of an image may be modified with the ``tint()`` function. This
    function will maintain transparency for GIF and PNG images.
    """
    pass


@overload
def image(img: Py5Image, a: float, b: float, c: float, d: float,
          u1: int, v1: int, u2: int, v2: int, /) -> None:
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
        x-coordinate of the upper left corner of image subset

    u2: int
        y-coordinate of the upper left corner of image subset

    v1: int
        x-coordinate of the lower right corner of image subset

    v2: int
        y-coordinate of the lower right corner of image subset

    Notes
    -----

    The ``image()`` function draws an image to the display window. Images must be in
    the Sketch's "data" directory to load correctly. Py5 currently works with GIF,
    JPEG, and PNG images.

    The ``img`` parameter specifies the image to display and by default the ``a``
    and ``b`` parameters define the location of its upper-left corner. The image is
    displayed at its original size unless the ``c`` and ``d`` parameters specify a
    different size. The ``image_mode()`` function can be used to change the way
    these parameters draw the image.

    Use the ``u1``, ``u2``, ``v1``, and ``v2`` parameters to use only a subset of
    the image. These values are always specified in image space location, regardless
    of the current ``texture_mode()`` setting.

    The color of an image may be modified with the ``tint()`` function. This
    function will maintain transparency for GIF and PNG images.
    """
    pass


def image(*args):
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
        x-coordinate of the upper left corner of image subset

    u2: int
        y-coordinate of the upper left corner of image subset

    v1: int
        x-coordinate of the lower right corner of image subset

    v2: int
        y-coordinate of the lower right corner of image subset

    Notes
    -----

    The ``image()`` function draws an image to the display window. Images must be in
    the Sketch's "data" directory to load correctly. Py5 currently works with GIF,
    JPEG, and PNG images.

    The ``img`` parameter specifies the image to display and by default the ``a``
    and ``b`` parameters define the location of its upper-left corner. The image is
    displayed at its original size unless the ``c`` and ``d`` parameters specify a
    different size. The ``image_mode()`` function can be used to change the way
    these parameters draw the image.

    Use the ``u1``, ``u2``, ``v1``, and ``v2`` parameters to use only a subset of
    the image. These values are always specified in image space location, regardless
    of the current ``texture_mode()`` setting.

    The color of an image may be modified with the ``tint()`` function. This
    function will maintain transparency for GIF and PNG images.
    """
    return _py5sketch.image(*args)


def image_mode(mode: int, /) -> None:
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
    ``image()`` as the location of one corner, and the fourth and fifth parameters
    as the opposite corner.

    ``image_mode(CENTER)`` interprets the second and third parameters of ``image()``
    as the image's center point. If two additional parameters are specified, they
    are used to set the image's width and height.

    The parameter must be written in ALL CAPS because Python is a case-sensitive
    language.
    """
    return _py5sketch.image_mode(mode)


@overload
def lerp_color(c1: int, c2: int, amt: float, /) -> int:
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
    """
    pass


@overload
def lerp_color(c1: int, c2: int, amt: float, mode: int, /) -> int:
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
    """
    pass


def lerp_color(*args):
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
    """
    return _py5sketch.lerp_color(*args)


def light_falloff(constant: float, linear: float, quadratic: float, /) -> None:
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
    used to calculate the falloff with the equation ``falloff = 1 / (CONSTANT + d *
    ``LINEAR`` + (d*d) * QUADRATIC)``, where ``d`` is the distance from light
    position to vertex position.

    Thinking about an ambient light with a falloff can be tricky. If you want a
    region of your scene to be lit ambiently with one color and another region to be
    lit ambiently with another color, you could use an ambient light with location
    and falloff. You can think of it as a point light that doesn't care which
    direction a surface is facing.
    """
    return _py5sketch.light_falloff(constant, linear, quadratic)


def light_specular(v1: float, v2: float, v3: float, /) -> None:
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
    return _py5sketch.light_specular(v1, v2, v3)


def lights() -> None:
    """Sets the default ambient light, directional light, falloff, and specular values.

    Underlying Java method: PApplet.lights

    Notes
    -----

    Sets the default ambient light, directional light, falloff, and specular values.
    The defaults are ``ambientLight(128, 128, 128)`` and ``directionalLight(128,
    128, 128, 0, 0, -1)``, ``lightFalloff(1, 0, 0)``, and ``lightSpecular(0, 0,
    0)``. Lights need to be included in the ``draw()`` to remain persistent in a
    looping program. Placing them in the ``setup()`` of a looping program will cause
    them to only have an effect the first time through the loop.
    """
    return _py5sketch.lights()


@overload
def line(x1: float, y1: float, x2: float, y2: float, /) -> None:
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
    ``P3D`` parameter in combination with ``size()`` as shown in the third example.
    """
    pass


@overload
def line(x1: float, y1: float, z1: float, x2: float,
         y2: float, z2: float, /) -> None:
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
    ``P3D`` parameter in combination with ``size()`` as shown in the third example.
    """
    pass


def line(*args):
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
    ``P3D`` parameter in combination with ``size()`` as shown in the third example.
    """
    return _py5sketch.line(*args)


def lines(coordinates: NDArray[(Any, Any), Float], /) -> None:
    """Draw a collection of lines to the screen.

    Underlying Java method: PApplet.lines

    Parameters
    ----------

    coordinates: NDArray[(Any, Any), Float]
        array of line coordinates

    Notes
    -----

    Draw a collection of lines to the screen. The purpose of this method is to
    provide an alternative to repeatedly calling ``line()`` in a loop. For a large
    number of lines, the performance of ``lines()`` will be much faster.

    The ``coordinates`` parameter should be a numpy array with one row for each
    line. The first few columns are for the first point of each line and the next
    few columns are for the second point of each line. There will be four or six
    columns for 2D or 3D points, respectively.
    """
    return _py5sketch.lines(coordinates)


def load_font(filename: str, /) -> Py5Font:
    """Loads a .vlw formatted font into a ``Py5Font`` object.

    Underlying Java method: PApplet.loadFont

    Parameters
    ----------

    filename: str
        name of the font to load

    Notes
    -----

    Loads a .vlw formatted font into a ``Py5Font`` object. Create a .vlw font with
    the ``create_font_file()`` function. This tool creates a texture for each
    alphanumeric character and then adds them as a .vlw file to the current Sketch's
    data folder. Because the letters are defined as textures (and not vector data)
    the size at which the fonts are created must be considered in relation to the
    size at which they are drawn. For example, load a 32pt font if the Sketch
    displays the font at 32 pixels or smaller. Conversely, if a 12pt font is loaded
    and displayed at 48pts, the letters will be distorted because the program will
    be stretching a small graphic to a large size.

    Like ``load_image()`` and other functions that load data, the ``load_font()``
    function should not be used inside ``draw()``, because it will slow down the
    Sketch considerably, as the font will be re-loaded from the disk (or network) on
    each frame. It's recommended to load files inside ``setup()``.

    To load correctly, fonts must be located in the "data" folder of the current
    Sketch. Alternatively, the file maybe be loaded from anywhere on the local
    computer using an absolute path (something that starts with / on Unix and Linux,
    or a drive letter on Windows), or the filename parameter can be a URL for a file
    found on a network.

    If the file is not available or an error occurs, ``None`` will be returned and
    an error message will be printed to the console. The error message does not halt
    the program, however the ``None`` value may cause an error if your code does not
    check whether the value returned is ``None``.

    Use ``create_font()`` (instead of ``load_font()``) to enable vector data to be
    used with the default renderer setting. This can be helpful when many font sizes
    are needed, or when using any renderer based on the default renderer, such as
    the ``PDF`` renderer.
    """
    return _py5sketch.load_font(filename)


def load_pixels() -> None:
    """Loads the pixel data of the current display window into the ``pixels[]`` array.

    Underlying Java method: PApplet.loadPixels

    Notes
    -----

    Loads the pixel data of the current display window into the ``pixels[]`` array.
    This function must always be called before reading from or writing to
    ``pixels[]``. Subsequent changes to the display window will not be reflected in
    ``pixels[]`` until ``load_pixels()`` is called again.
    """
    return _py5sketch.load_pixels()


@overload
def load_shader(frag_filename: str, /) -> Py5Shader:
    """Loads a shader into a ``Py5Shader`` object.

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
    """
    pass


@overload
def load_shader(frag_filename: str, vert_filename: str, /) -> Py5Shader:
    """Loads a shader into a ``Py5Shader`` object.

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
    """
    pass


def load_shader(*args):
    """Loads a shader into a ``Py5Shader`` object.

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
    """
    return _py5sketch.load_shader(*args)


@overload
def load_shape(filename: str, /) -> Py5Shape:
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
    """
    pass


@overload
def load_shape(filename: str, options: str, /) -> Py5Shape:
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
    """
    pass


def load_shape(*args):
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
    """
    return _py5sketch.load_shape(*args)


def loop() -> None:
    """By default, py5 loops through ``draw()`` continuously, executing the code within
    it.

    Underlying Java method: PApplet.loop

    Notes
    -----

    By default, py5 loops through ``draw()`` continuously, executing the code within
    it. However, the ``draw()`` loop may be stopped by calling ``no_loop()``. In
    that case, the ``draw()`` loop can be resumed with ``loop()``.
    """
    return _py5sketch.loop()


def millis() -> int:
    """Returns the number of milliseconds (thousandths of a second) since starting the
    program.

    Underlying Java method: PApplet.millis

    Notes
    -----

    Returns the number of milliseconds (thousandths of a second) since starting the
    program. This information is often used for timing events and animation
    sequences.
    """
    return _py5sketch.millis()


def minute() -> int:
    """Py5 communicates with the clock on your computer.

    Underlying Java method: PApplet.minute

    Notes
    -----

    Py5 communicates with the clock on your computer. The ``minute()`` function
    returns the current minute as a value from 0 - 59.
    """
    return Sketch.minute()


def model_x(x: float, y: float, z: float, /) -> float:
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
    return _py5sketch.model_x(x, y, z)


def model_y(x: float, y: float, z: float, /) -> float:
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
    return _py5sketch.model_y(x, y, z)


def model_z(x: float, y: float, z: float, /) -> float:
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
    return _py5sketch.model_z(x, y, z)


def month() -> int:
    """Py5 communicates with the clock on your computer.

    Underlying Java method: PApplet.month

    Notes
    -----

    Py5 communicates with the clock on your computer. The ``month()`` function
    returns the current month as a value from 1 - 12.
    """
    return Sketch.month()


def no_clip() -> None:
    """Disables the clipping previously started by the ``clip()`` function.

    Underlying Java method: PApplet.noClip

    Notes
    -----

    Disables the clipping previously started by the ``clip()`` function.
    """
    return _py5sketch.no_clip()


def no_cursor() -> None:
    """Hides the cursor from view.

    Underlying Java method: PApplet.noCursor

    Notes
    -----

    Hides the cursor from view. Will not work when running the program in full
    screen (Present) mode.
    """
    return _py5sketch.no_cursor()


def no_fill() -> None:
    """Disables filling geometry.

    Underlying Java method: PApplet.noFill

    Notes
    -----

    Disables filling geometry. If both ``no_stroke()`` and ``no_fill()`` are called,
    nothing will be drawn to the screen.
    """
    return _py5sketch.no_fill()


def no_lights() -> None:
    """Disable all lighting.

    Underlying Java method: PApplet.noLights

    Notes
    -----

    Disable all lighting. Lighting is turned off by default and enabled with the
    ``lights()`` function. This function can be used to disable lighting so that 2D
    geometry (which does not require lighting) can be drawn after a set of lighted
    3D geometry.
    """
    return _py5sketch.no_lights()


def no_loop() -> None:
    """Stops py5 from continuously executing the code within ``draw()``.

    Underlying Java method: PApplet.noLoop

    Notes
    -----

    Stops py5 from continuously executing the code within ``draw()``. If ``loop()``
    is called, the code in ``draw()`` begins to run continuously again. If using
    ``no_loop()`` in ``setup()``, it should be the last line inside the block.

    When ``no_loop()`` is used, it's not possible to manipulate or access the screen
    inside event handling functions such as ``mouse_pressed()`` or
    ``key_pressed()``. Instead, use those functions to call ``redraw()`` or
    ``loop()``, which will run ``draw()``, which can update the screen properly.
    This means that when ``no_loop()`` has been called, no drawing can happen, and
    functions like ``save_frame()`` or ``load_pixels()`` may not be used.

    Note that if the Sketch is resized, ``redraw()`` will be called to update the
    Sketch, even after ``no_loop()`` has been specified. Otherwise, the Sketch would
    enter an odd state until ``loop()`` was called.
    """
    return _py5sketch.no_loop()


def no_smooth() -> None:
    """Draws all geometry and fonts with jagged (aliased) edges and images with hard
    edges between the pixels when enlarged rather than interpolating pixels.

    Underlying Java method: PApplet.noSmooth

    Notes
    -----

    Draws all geometry and fonts with jagged (aliased) edges and images with hard
    edges between the pixels when enlarged rather than interpolating pixels.  Note
    that ``smooth()`` is active by default, so it is necessary to call
    ``no_smooth()`` to disable smoothing of geometry, fonts, and images. The
    ``no_smooth()`` method can only be run once for each Sketch and must be called
    in ``settings()``.
    """
    return _py5sketch.no_smooth()


def no_stroke() -> None:
    """Disables drawing the stroke (outline).

    Underlying Java method: PApplet.noStroke

    Notes
    -----

    Disables drawing the stroke (outline). If both ``no_stroke()`` and ``no_fill()``
    are called, nothing will be drawn to the screen.
    """
    return _py5sketch.no_stroke()


def no_tint() -> None:
    """Removes the current fill value for displaying images and reverts to displaying
    images with their original hues.

    Underlying Java method: PApplet.noTint

    Notes
    -----

    Removes the current fill value for displaying images and reverts to displaying
    images with their original hues.
    """
    return _py5sketch.no_tint()


def normal(nx: float, ny: float, nz: float, /) -> None:
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
    which, in turn, determines how lighting affects it. Py5 attempts to
    automatically assign normals to shapes, but since that's imperfect, this is a
    better option when you want more control. This function is identical to
    ``gl_normal3f()`` in OpenGL.
    """
    return _py5sketch.normal(nx, ny, nz)


@overload
def ortho() -> None:
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
    ``ortho(-width/2, width/2, -height/2, height/2)``.
    """
    pass


@overload
def ortho(left: float, right: float, bottom: float, top: float, /) -> None:
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
    ``ortho(-width/2, width/2, -height/2, height/2)``.
    """
    pass


@overload
def ortho(left: float, right: float, bottom: float,
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
    ``ortho(-width/2, width/2, -height/2, height/2)``.
    """
    pass


def ortho(*args):
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
    ``ortho(-width/2, width/2, -height/2, height/2)``.
    """
    return _py5sketch.ortho(*args)


@overload
def perspective() -> None:
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
    The default values are: ``perspective(PI/3.0, width/height, cameraZ/10.0,
    cameraZ*10.0)`` where cameraZ is ``((height/2.0) / tan(PI*60.0/360.0))``.
    """
    pass


@overload
def perspective(fovy: float, aspect: float,
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
    The default values are: ``perspective(PI/3.0, width/height, cameraZ/10.0,
    cameraZ*10.0)`` where cameraZ is ``((height/2.0) / tan(PI*60.0/360.0))``.
    """
    pass


def perspective(*args):
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
    The default values are: ``perspective(PI/3.0, width/height, cameraZ/10.0,
    cameraZ*10.0)`` where cameraZ is ``((height/2.0) / tan(PI*60.0/360.0))``.
    """
    return _py5sketch.perspective(*args)


def pixel_density(density: int, /) -> None:
    """This function makes it possible for py5 to render using all of the pixels on
    high resolutions screens like Apple Retina displays and Windows High-DPI
    displays.

    Underlying Java method: PApplet.pixelDensity

    Parameters
    ----------

    density: int
        1 or 2

    Notes
    -----

    This function makes it possible for py5 to render using all of the pixels on
    high resolutions screens like Apple Retina displays and Windows High-DPI
    displays. This function can only be run once within a program and it must be
    called in ``settings()``.  The ``pixel_density()`` should only be used with
    hardcoded numbers (in almost all cases this number will be 2) or in combination
    with ``display_density()`` as in the second example.

    When the pixel density is set to more than 1, it changes all of the pixel
    operations including the way ``get()``, ``blend()``, ``copy()``,
    ``update_pixels()``, and ``update_np_pixels()`` all work. See the reference for
    ``pixel_width`` and ``pixel_height`` for more information.

    To use variables as the arguments to ``pixel_density()`` function, place the
    ``pixel_density()`` function within the ``settings()`` function.
    """
    return _py5sketch.pixel_density(density)


@overload
def point(x: float, y: float, /) -> None:
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
    Drawing this shape in 3D with the ``z`` parameter requires the ``P3D`` parameter
    in combination with ``size()`` as shown in the second example.

    Use ``stroke()`` to set the color of a ``point()``.

    Point appears round with the default ``stroke_cap(ROUND)`` and square with
    ``stroke_cap(PROJECT)``. Points are invisible with ``stroke_cap(SQUARE)`` (no
    cap).

    Using ``point()`` with ``strokeWeight(1)`` or smaller may draw nothing to the
    screen, depending on the graphics settings of the computer. Workarounds include
    setting the pixel using the ``pixels[]`` or ``np_pixels[]`` arrays or drawing
    the point using either ``circle()`` or ``square()``.
    """
    pass


@overload
def point(x: float, y: float, z: float, /) -> None:
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
    Drawing this shape in 3D with the ``z`` parameter requires the ``P3D`` parameter
    in combination with ``size()`` as shown in the second example.

    Use ``stroke()`` to set the color of a ``point()``.

    Point appears round with the default ``stroke_cap(ROUND)`` and square with
    ``stroke_cap(PROJECT)``. Points are invisible with ``stroke_cap(SQUARE)`` (no
    cap).

    Using ``point()`` with ``strokeWeight(1)`` or smaller may draw nothing to the
    screen, depending on the graphics settings of the computer. Workarounds include
    setting the pixel using the ``pixels[]`` or ``np_pixels[]`` arrays or drawing
    the point using either ``circle()`` or ``square()``.
    """
    pass


def point(*args):
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
    Drawing this shape in 3D with the ``z`` parameter requires the ``P3D`` parameter
    in combination with ``size()`` as shown in the second example.

    Use ``stroke()`` to set the color of a ``point()``.

    Point appears round with the default ``stroke_cap(ROUND)`` and square with
    ``stroke_cap(PROJECT)``. Points are invisible with ``stroke_cap(SQUARE)`` (no
    cap).

    Using ``point()`` with ``strokeWeight(1)`` or smaller may draw nothing to the
    screen, depending on the graphics settings of the computer. Workarounds include
    setting the pixel using the ``pixels[]`` or ``np_pixels[]`` arrays or drawing
    the point using either ``circle()`` or ``square()``.
    """
    return _py5sketch.point(*args)


def point_light(v1: float, v2: float, v3: float,
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
    return _py5sketch.point_light(v1, v2, v3, x, y, z)


def points(coordinates: NDArray[(Any, Any), Float], /) -> None:
    """Draw a collection of points, each a coordinate in space at the dimension of one
    pixel.

    Underlying Java method: PApplet.points

    Parameters
    ----------

    coordinates: NDArray[(Any, Any), Float]
        array of point coordinates

    Notes
    -----

    Draw a collection of points, each a coordinate in space at the dimension of one
    pixel. The purpose of this method is to provide an alternative to repeatedly
    calling ``point()`` in a loop. For a large number of points, the performance of
    ``points()`` will be much faster.

    The ``coordinates`` parameter should be a numpy array with one row for each
    point. There should be two or three columns for 2D or 3D points, respectively.
    """
    return _py5sketch.points(coordinates)


def pop() -> None:
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
    ``text_font()``, ``text_mode()``, ``text_size()``, and ``text_leading()``.

    The ``push()`` and ``pop()`` functions can be used in place of
    ``push_matrix()``, ``pop_matrix()``, ``push_styles()``, and ``pop_styles()``.
    The difference is that ``push()`` and ``pop()`` control both the transformations
    (rotate, scale, translate) and the drawing styles at the same time.
    """
    return _py5sketch.pop()


def pop_matrix() -> None:
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
    return _py5sketch.pop_matrix()


def pop_style() -> None:
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
    current style information. The ``push_style()`` and ``pop_style()`` method pairs
    can be nested to provide more control (see the second example for a
    demonstration.)
    """
    return _py5sketch.pop_style()


def print_camera() -> None:
    """Prints the current camera matrix to standard output.

    Underlying Java method: PApplet.printCamera

    Notes
    -----

    Prints the current camera matrix to standard output.
    """
    return _py5sketch.print_camera()


def print_matrix() -> None:
    """Prints the current matrix to standard output.

    Underlying Java method: PApplet.printMatrix

    Notes
    -----

    Prints the current matrix to standard output.
    """
    return _py5sketch.print_matrix()


def print_projection() -> None:
    """Prints the current projection matrix to standard output.

    Underlying Java method: PApplet.printProjection

    Notes
    -----

    Prints the current projection matrix to standard output.
    """
    return _py5sketch.print_projection()


def push() -> None:
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

    The ``push()`` and ``pop()`` functions can be used in place of
    ``push_matrix()``, ``pop_matrix()``, ``push_styles()``, and ``pop_styles()``.
    The difference is that ``push()`` and ``pop()`` control both the transformations
    (rotate, scale, translate) and the drawing styles at the same time.
    """
    return _py5sketch.push()


def push_matrix() -> None:
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
    return _py5sketch.push_matrix()


def push_style() -> None:
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
    ``pop_style()`` method pairs can be nested to provide more control. (See the
    second example for a demonstration.)

    The style information controlled by the following functions are included in the
    style: ``fill()``, ``stroke()``, ``tint()``, ``stroke_weight()``,
    ``stroke_cap()``, ``stroke_join()``, ``image_mode()``, ``rect_mode()``,
    ``ellipse_mode()``, ``shape_mode()``, ``color_mode()``, ``text_align()``,
    ``text_font()``, ``text_mode()``, ``text_size()``, ``text_leading()``,
    ``emissive()``, ``specular()``, ``shininess()``, and ``ambient()``.
    """
    return _py5sketch.push_style()


def quad(x1: float, y1: float, x2: float, y2: float, x3: float,
         y3: float, x4: float, y4: float, /) -> None:
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
    return _py5sketch.quad(x1, y1, x2, y2, x3, y3, x4, y4)


@overload
def quadratic_vertex(cx: float, cy: float, x3: float, y3: float, /) -> None:
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
    prefaced with a call to ``vertex()`` to set the first anchor point. This method
    must be used between ``begin_shape()`` and ``end_shape()`` and only when there
    is no ``MODE`` parameter specified to ``begin_shape()``. Using the 3D version
    requires rendering with ``P3D``.
    """
    pass


@overload
def quadratic_vertex(cx: float, cy: float, cz: float,
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
    prefaced with a call to ``vertex()`` to set the first anchor point. This method
    must be used between ``begin_shape()`` and ``end_shape()`` and only when there
    is no ``MODE`` parameter specified to ``begin_shape()``. Using the 3D version
    requires rendering with ``P3D``.
    """
    pass


def quadratic_vertex(*args):
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
    prefaced with a call to ``vertex()`` to set the first anchor point. This method
    must be used between ``begin_shape()`` and ``end_shape()`` and only when there
    is no ``MODE`` parameter specified to ``begin_shape()``. Using the 3D version
    requires rendering with ``P3D``.
    """
    return _py5sketch.quadratic_vertex(*args)


def quadratic_vertices(coordinates: NDArray[(Any, Any), Float], /) -> None:
    """Create a collection of quadratic vertices.

    Underlying Java method: PApplet.quadraticVertices

    Parameters
    ----------

    coordinates: NDArray[(Any, Any), Float]
        array of quadratic vertex coordinates

    Notes
    -----

    Create a collection of quadratic vertices. The purpose of this method is to
    provide an alternative to repeatedly calling ``quadratic_vertex()`` in a loop.
    For a large number of quadratic vertices, the performance of
    ``quadratic_vertices()`` will be much faster.

    The ``coordinates`` parameter should be a numpy array with one row for each
    quadratic vertex. The first few columns are for the control point and the next
    few columns are for the anchor point. There should be four or six columns for 2D
    or 3D points, respectively.
    """
    return _py5sketch.quadratic_vertices(coordinates)


@overload
def rect(a: float, b: float, c: float, d: float, /) -> None:
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
def rect(a: float, b: float, c: float, d: float, r: float, /) -> None:
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
def rect(a: float, b: float, c: float, d: float, tl: float,
         tr: float, br: float, bl: float, /) -> None:
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


def rect(*args):
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
    return _py5sketch.rect(*args)


def rect_mode(mode: int, /) -> None:
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

    The parameter must be written in ALL CAPS because Python is a case-sensitive
    language.
    """
    return _py5sketch.rect_mode(mode)


def red(rgb: int, /) -> float:
    """Extracts the red value from a color, scaled to match current ``color_mode()``.

    Underlying Java method: PApplet.red

    Parameters
    ----------

    rgb: int
        any value of the color datatype

    Notes
    -----

    Extracts the red value from a color, scaled to match current ``color_mode()``.

    The ``red()`` function is easy to use and understand, but it is slower than a
    technique called bit shifting. When working in ``color_mode(RGB, 255)``, you can
    achieve the same results as ``red()`` but with greater speed by using the right
    shift operator (``>>``) with a bit mask. For example, ``red(c)`` and ``c >> 16 &
    0xFF`` both extract the red value from a color variable ``c`` but the later is
    faster.
    """
    return _py5sketch.red(rgb)


def redraw() -> None:
    """Executes the code within ``draw()`` one time.

    Underlying Java method: PApplet.redraw

    Notes
    -----

    Executes the code within ``draw()`` one time. This functions allows the program
    to update the display window only when necessary, for example when an event
    registered by ``mouse_pressed()`` or ``key_pressed()`` occurs.

    In structuring a program, it only makes sense to call ``redraw()`` within events
    such as ``mouse_pressed()``. This is because ``redraw()`` does not run
    ``draw()`` immediately (it only sets a flag that indicates an update is needed).

    The ``redraw()`` function does not work properly when called inside ``draw()``.
    To enable/disable animations, use ``loop()`` and ``no_loop()``.
    """
    return _py5sketch.redraw()


def reset_matrix() -> None:
    """Replaces the current matrix with the identity matrix.

    Underlying Java method: PApplet.resetMatrix

    Notes
    -----

    Replaces the current matrix with the identity matrix. The equivalent function in
    OpenGL is ``gl_load_identity()``.
    """
    return _py5sketch.reset_matrix()


@overload
def reset_shader() -> None:
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
def reset_shader(kind: int, /) -> None:
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


def reset_shader(*args):
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
    return _py5sketch.reset_shader(*args)


@overload
def rotate(angle: float, /) -> None:
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
    rotation matrix. This function can be further controlled by ``push_matrix()``
    and ``pop_matrix()``.
    """
    pass


@overload
def rotate(angle: float, x: float, y: float, z: float, /) -> None:
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
    rotation matrix. This function can be further controlled by ``push_matrix()``
    and ``pop_matrix()``.
    """
    pass


def rotate(*args):
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
    rotation matrix. This function can be further controlled by ``push_matrix()``
    and ``pop_matrix()``.
    """
    return _py5sketch.rotate(*args)


def rotate_x(angle: float, /) -> None:
    """Rotates around the x-axis the amount specified by the ``angle`` parameter.

    Underlying Java method: PApplet.rotateX

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
    """
    return _py5sketch.rotate_x(angle)


def rotate_y(angle: float, /) -> None:
    """Rotates around the y-axis the amount specified by the ``angle`` parameter.

    Underlying Java method: PApplet.rotateY

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
    """
    return _py5sketch.rotate_y(angle)


def rotate_z(angle: float, /) -> None:
    """Rotates around the z-axis the amount specified by the ``angle`` parameter.

    Underlying Java method: PApplet.rotateZ

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
    """
    return _py5sketch.rotate_z(angle)


def saturation(rgb: int, /) -> float:
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
    return _py5sketch.saturation(rgb)


@overload
def scale(s: float, /) -> None:
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
    function with the ``z`` parameter requires using ``P3D`` as a parameter for
    ``size()``, as shown in the third example. This function can be further
    controlled with ``push_matrix()`` and ``pop_matrix()``.
    """
    pass


@overload
def scale(x: float, y: float, /) -> None:
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
    function with the ``z`` parameter requires using ``P3D`` as a parameter for
    ``size()``, as shown in the third example. This function can be further
    controlled with ``push_matrix()`` and ``pop_matrix()``.
    """
    pass


@overload
def scale(x: float, y: float, z: float, /) -> None:
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
    function with the ``z`` parameter requires using ``P3D`` as a parameter for
    ``size()``, as shown in the third example. This function can be further
    controlled with ``push_matrix()`` and ``pop_matrix()``.
    """
    pass


def scale(*args):
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
    function with the ``z`` parameter requires using ``P3D`` as a parameter for
    ``size()``, as shown in the third example. This function can be further
    controlled with ``push_matrix()`` and ``pop_matrix()``.
    """
    return _py5sketch.scale(*args)


@overload
def screen_x(x: float, y: float, /) -> float:
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
def screen_x(x: float, y: float, z: float, /) -> float:
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


def screen_x(*args):
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
    return _py5sketch.screen_x(*args)


@overload
def screen_y(x: float, y: float, /) -> float:
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
def screen_y(x: float, y: float, z: float, /) -> float:
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


def screen_y(*args):
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
    return _py5sketch.screen_y(*args)


def screen_z(x: float, y: float, z: float, /) -> float:
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
    return _py5sketch.screen_z(x, y, z)


def second() -> int:
    """Py5 communicates with the clock on your computer.

    Underlying Java method: PApplet.second

    Notes
    -----

    Py5 communicates with the clock on your computer. The ``second()`` function
    returns the current second as a value from 0 - 59.
    """
    return Sketch.second()


@overload
def set_matrix(source: NDArray[(2, 3), Float], /) -> None:
    """Set the current matrix to the one specified through the parameter ``source``.

    Underlying Java method: PApplet.setMatrix

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
    Inside the Processing code it will call ``reset_matrix()`` followed by
    ``apply_matrix()``. This will be very slow because ``apply_matrix()`` will try
    to calculate the inverse of the transform, so avoid it whenever possible.
    """
    pass


@overload
def set_matrix(source: NDArray[(4, 4), Float], /) -> None:
    """Set the current matrix to the one specified through the parameter ``source``.

    Underlying Java method: PApplet.setMatrix

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
    Inside the Processing code it will call ``reset_matrix()`` followed by
    ``apply_matrix()``. This will be very slow because ``apply_matrix()`` will try
    to calculate the inverse of the transform, so avoid it whenever possible.
    """
    pass


def set_matrix(*args):
    """Set the current matrix to the one specified through the parameter ``source``.

    Underlying Java method: PApplet.setMatrix

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
    Inside the Processing code it will call ``reset_matrix()`` followed by
    ``apply_matrix()``. This will be very slow because ``apply_matrix()`` will try
    to calculate the inverse of the transform, so avoid it whenever possible.
    """
    return _py5sketch.set_matrix(*args)


@overload
def shader(shader: Py5Shader, /) -> None:
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

    Applies the shader specified by the parameters. It's compatible with the ``P2D``
    and ``P3D`` renderers, but not with the default renderer.
    """
    pass


@overload
def shader(shader: Py5Shader, kind: int, /) -> None:
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

    Applies the shader specified by the parameters. It's compatible with the ``P2D``
    and ``P3D`` renderers, but not with the default renderer.
    """
    pass


def shader(*args):
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

    Applies the shader specified by the parameters. It's compatible with the ``P2D``
    and ``P3D`` renderers, but not with the default renderer.
    """
    return _py5sketch.shader(*args)


@overload
def shape(shape: Py5Shape, /) -> None:
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

    Draws shapes to the display window. Shapes must be in the Sketch's "data"
    directory to load correctly. Py5 currently works with SVG, OBJ, and custom-
    created shapes. The ``shape`` parameter specifies the shape to display and the
    coordinate parameters define the location of the shape from its upper-left
    corner. The shape is displayed at its original size unless the ``c`` and ``d``
    parameters specify a different size. The ``shape_mode()`` function can be used
    to change the way these parameters are interpreted.
    """
    pass


@overload
def shape(shape: Py5Shape, x: float, y: float, /) -> None:
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

    Draws shapes to the display window. Shapes must be in the Sketch's "data"
    directory to load correctly. Py5 currently works with SVG, OBJ, and custom-
    created shapes. The ``shape`` parameter specifies the shape to display and the
    coordinate parameters define the location of the shape from its upper-left
    corner. The shape is displayed at its original size unless the ``c`` and ``d``
    parameters specify a different size. The ``shape_mode()`` function can be used
    to change the way these parameters are interpreted.
    """
    pass


@overload
def shape(shape: Py5Shape, a: float, b: float, c: float, d: float, /) -> None:
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

    Draws shapes to the display window. Shapes must be in the Sketch's "data"
    directory to load correctly. Py5 currently works with SVG, OBJ, and custom-
    created shapes. The ``shape`` parameter specifies the shape to display and the
    coordinate parameters define the location of the shape from its upper-left
    corner. The shape is displayed at its original size unless the ``c`` and ``d``
    parameters specify a different size. The ``shape_mode()`` function can be used
    to change the way these parameters are interpreted.
    """
    pass


def shape(*args):
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

    Draws shapes to the display window. Shapes must be in the Sketch's "data"
    directory to load correctly. Py5 currently works with SVG, OBJ, and custom-
    created shapes. The ``shape`` parameter specifies the shape to display and the
    coordinate parameters define the location of the shape from its upper-left
    corner. The shape is displayed at its original size unless the ``c`` and ``d``
    parameters specify a different size. The ``shape_mode()`` function can be used
    to change the way these parameters are interpreted.
    """
    return _py5sketch.shape(*args)


def shape_mode(mode: int, /) -> None:
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
    parameter must be written in ALL CAPS because Python is a case sensitive
    language.
    """
    return _py5sketch.shape_mode(mode)


def shear_x(angle: float, /) -> None:
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
    parameter. Angles should be specified in radians (values from ``0`` to
    ``TWO_PI``) or converted to radians with the ``radians()`` function. Objects are
    always sheared around their relative position to the origin and positive numbers
    shear objects in a clockwise direction. Transformations apply to everything that
    happens after and subsequent calls to the function accumulates the effect. For
    example, calling ``shear_x(PI/2)`` and then ``shear_x(PI/2)`` is the same as
    ``shear_x(PI)``. If ``shear_x()`` is called within the ``draw()``, the
    transformation is reset when the loop begins again.

    Technically, ``shear_x()`` multiplies the current transformation matrix by a
    rotation matrix. This function can be further controlled by the
    ``push_matrix()`` and ``pop_matrix()`` functions.
    """
    return _py5sketch.shear_x(angle)


def shear_y(angle: float, /) -> None:
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
    parameter. Angles should be specified in radians (values from ``0`` to
    ``TWO_PI``) or converted to radians with the ``radians()`` function. Objects are
    always sheared around their relative position to the origin and positive numbers
    shear objects in a clockwise direction. Transformations apply to everything that
    happens after and subsequent calls to the function accumulates the effect. For
    example, calling ``shear_y(PI/2)`` and then ``shear_y(PI/2)`` is the same as
    ``shear_y(PI)``. If ``shear_y()`` is called within the ``draw()``, the
    transformation is reset when the loop begins again.

    Technically, ``shear_y()`` multiplies the current transformation matrix by a
    rotation matrix. This function can be further controlled by the
    ``push_matrix()`` and ``pop_matrix()`` functions.
    """
    return _py5sketch.shear_y(angle)


def shininess(shine: float, /) -> None:
    """Sets the amount of gloss in the surface of shapes.

    Underlying Java method: PApplet.shininess

    Parameters
    ----------

    shine: float
        degree of shininess

    Notes
    -----

    Sets the amount of gloss in the surface of shapes. Use in combination with
    ``ambient()``, ``specular()``, and ``emissive()`` to set the material properties
    of shapes.
    """
    return _py5sketch.shininess(shine)


@overload
def size(width: int, height: int, /) -> None:
    """Defines the dimension of the display window width and height in units of pixels.

    Underlying Java method: PApplet.size

    Methods
    -------

    You can use any of the following signatures:

     * size(width: int, height: int, /) -> None
     * size(width: int, height: int, renderer: str, /) -> None
     * size(width: int, height: int, renderer: str, path: str, /) -> None

    Parameters
    ----------

    height: int
        height of the display window in units of pixels

    path: str
        filename to save rendering engine output to

    renderer: str
        rendering engine to use

    width: int
        width of the display window in units of pixels

    Notes
    -----

    Defines the dimension of the display window width and height in units of pixels.
    This must be called from the ``settings()`` function.

    The built-in variables ``width`` and ``height`` are set by the parameters passed
    to this function. For example, running ``size(640, 480)`` will assign 640 to the
    ``width`` variable and 480 to the height ``variable``. If ``size()`` is not
    used, the window will be given a default size of 100 x 100 pixels.

    The ``size()`` function can only be used once inside a Sketch, and it cannot be
    used for resizing.

    To run a Sketch at the full dimensions of a screen, use the ``full_screen()``
    function, rather than the older way of using ``size(display_width,
    display_height)``.

    The maximum width and height is limited by your operating system, and is usually
    the width and height of your actual screen. On some machines it may simply be
    the number of pixels on your current screen, meaning that a screen of 800 x 600
    could support ``size(1600, 300)``, since that is the same number of pixels. This
    varies widely, so you'll have to try different rendering modes and sizes until
    you get what you're looking for. If you need something larger, use
    ``create_graphics`` to create a non-visible drawing surface.

    The minimum width and height is around 100 pixels in each direction. This is the
    smallest that is supported across Windows, macOS, and Linux. We enforce the
    minimum size so that Sketches will run identically on different machines.

    The ``renderer`` parameter selects which rendering engine to use. For example,
    if you will be drawing 3D shapes, use ``P3D``. In addition to the default
    renderer, other renderers are:

    * ``P2D`` (Processing 2D): 2D graphics renderer that makes use of OpenGL-
    compatible graphics hardware.
    * ``P3D`` (Processing 3D): 3D graphics renderer that makes use of OpenGL-
    compatible graphics hardware.
    * ``FX2D`` (JavaFX 2D): A 2D renderer that uses JavaFX, which may be faster for
    some applications, but has some compatibility quirks.
    * ``PDF``: The ``PDF`` renderer draws 2D graphics directly to an Acrobat PDF
    file. This produces excellent results when you need vector shapes for high-
    resolution output or printing.
    * ``SVG``: The ``SVG`` renderer draws 2D graphics directly to an SVG file. This
    is great for importing into other vector programs or using for digital
    fabrication.
    """
    pass


@overload
def size(width: int, height: int, renderer: str, /) -> None:
    """Defines the dimension of the display window width and height in units of pixels.

    Underlying Java method: PApplet.size

    Methods
    -------

    You can use any of the following signatures:

     * size(width: int, height: int, /) -> None
     * size(width: int, height: int, renderer: str, /) -> None
     * size(width: int, height: int, renderer: str, path: str, /) -> None

    Parameters
    ----------

    height: int
        height of the display window in units of pixels

    path: str
        filename to save rendering engine output to

    renderer: str
        rendering engine to use

    width: int
        width of the display window in units of pixels

    Notes
    -----

    Defines the dimension of the display window width and height in units of pixels.
    This must be called from the ``settings()`` function.

    The built-in variables ``width`` and ``height`` are set by the parameters passed
    to this function. For example, running ``size(640, 480)`` will assign 640 to the
    ``width`` variable and 480 to the height ``variable``. If ``size()`` is not
    used, the window will be given a default size of 100 x 100 pixels.

    The ``size()`` function can only be used once inside a Sketch, and it cannot be
    used for resizing.

    To run a Sketch at the full dimensions of a screen, use the ``full_screen()``
    function, rather than the older way of using ``size(display_width,
    display_height)``.

    The maximum width and height is limited by your operating system, and is usually
    the width and height of your actual screen. On some machines it may simply be
    the number of pixels on your current screen, meaning that a screen of 800 x 600
    could support ``size(1600, 300)``, since that is the same number of pixels. This
    varies widely, so you'll have to try different rendering modes and sizes until
    you get what you're looking for. If you need something larger, use
    ``create_graphics`` to create a non-visible drawing surface.

    The minimum width and height is around 100 pixels in each direction. This is the
    smallest that is supported across Windows, macOS, and Linux. We enforce the
    minimum size so that Sketches will run identically on different machines.

    The ``renderer`` parameter selects which rendering engine to use. For example,
    if you will be drawing 3D shapes, use ``P3D``. In addition to the default
    renderer, other renderers are:

    * ``P2D`` (Processing 2D): 2D graphics renderer that makes use of OpenGL-
    compatible graphics hardware.
    * ``P3D`` (Processing 3D): 3D graphics renderer that makes use of OpenGL-
    compatible graphics hardware.
    * ``FX2D`` (JavaFX 2D): A 2D renderer that uses JavaFX, which may be faster for
    some applications, but has some compatibility quirks.
    * ``PDF``: The ``PDF`` renderer draws 2D graphics directly to an Acrobat PDF
    file. This produces excellent results when you need vector shapes for high-
    resolution output or printing.
    * ``SVG``: The ``SVG`` renderer draws 2D graphics directly to an SVG file. This
    is great for importing into other vector programs or using for digital
    fabrication.
    """
    pass


@overload
def size(width: int, height: int, renderer: str, path: str, /) -> None:
    """Defines the dimension of the display window width and height in units of pixels.

    Underlying Java method: PApplet.size

    Methods
    -------

    You can use any of the following signatures:

     * size(width: int, height: int, /) -> None
     * size(width: int, height: int, renderer: str, /) -> None
     * size(width: int, height: int, renderer: str, path: str, /) -> None

    Parameters
    ----------

    height: int
        height of the display window in units of pixels

    path: str
        filename to save rendering engine output to

    renderer: str
        rendering engine to use

    width: int
        width of the display window in units of pixels

    Notes
    -----

    Defines the dimension of the display window width and height in units of pixels.
    This must be called from the ``settings()`` function.

    The built-in variables ``width`` and ``height`` are set by the parameters passed
    to this function. For example, running ``size(640, 480)`` will assign 640 to the
    ``width`` variable and 480 to the height ``variable``. If ``size()`` is not
    used, the window will be given a default size of 100 x 100 pixels.

    The ``size()`` function can only be used once inside a Sketch, and it cannot be
    used for resizing.

    To run a Sketch at the full dimensions of a screen, use the ``full_screen()``
    function, rather than the older way of using ``size(display_width,
    display_height)``.

    The maximum width and height is limited by your operating system, and is usually
    the width and height of your actual screen. On some machines it may simply be
    the number of pixels on your current screen, meaning that a screen of 800 x 600
    could support ``size(1600, 300)``, since that is the same number of pixels. This
    varies widely, so you'll have to try different rendering modes and sizes until
    you get what you're looking for. If you need something larger, use
    ``create_graphics`` to create a non-visible drawing surface.

    The minimum width and height is around 100 pixels in each direction. This is the
    smallest that is supported across Windows, macOS, and Linux. We enforce the
    minimum size so that Sketches will run identically on different machines.

    The ``renderer`` parameter selects which rendering engine to use. For example,
    if you will be drawing 3D shapes, use ``P3D``. In addition to the default
    renderer, other renderers are:

    * ``P2D`` (Processing 2D): 2D graphics renderer that makes use of OpenGL-
    compatible graphics hardware.
    * ``P3D`` (Processing 3D): 3D graphics renderer that makes use of OpenGL-
    compatible graphics hardware.
    * ``FX2D`` (JavaFX 2D): A 2D renderer that uses JavaFX, which may be faster for
    some applications, but has some compatibility quirks.
    * ``PDF``: The ``PDF`` renderer draws 2D graphics directly to an Acrobat PDF
    file. This produces excellent results when you need vector shapes for high-
    resolution output or printing.
    * ``SVG``: The ``SVG`` renderer draws 2D graphics directly to an SVG file. This
    is great for importing into other vector programs or using for digital
    fabrication.
    """
    pass


def size(*args):
    """Defines the dimension of the display window width and height in units of pixels.

    Underlying Java method: PApplet.size

    Methods
    -------

    You can use any of the following signatures:

     * size(width: int, height: int, /) -> None
     * size(width: int, height: int, renderer: str, /) -> None
     * size(width: int, height: int, renderer: str, path: str, /) -> None

    Parameters
    ----------

    height: int
        height of the display window in units of pixels

    path: str
        filename to save rendering engine output to

    renderer: str
        rendering engine to use

    width: int
        width of the display window in units of pixels

    Notes
    -----

    Defines the dimension of the display window width and height in units of pixels.
    This must be called from the ``settings()`` function.

    The built-in variables ``width`` and ``height`` are set by the parameters passed
    to this function. For example, running ``size(640, 480)`` will assign 640 to the
    ``width`` variable and 480 to the height ``variable``. If ``size()`` is not
    used, the window will be given a default size of 100 x 100 pixels.

    The ``size()`` function can only be used once inside a Sketch, and it cannot be
    used for resizing.

    To run a Sketch at the full dimensions of a screen, use the ``full_screen()``
    function, rather than the older way of using ``size(display_width,
    display_height)``.

    The maximum width and height is limited by your operating system, and is usually
    the width and height of your actual screen. On some machines it may simply be
    the number of pixels on your current screen, meaning that a screen of 800 x 600
    could support ``size(1600, 300)``, since that is the same number of pixels. This
    varies widely, so you'll have to try different rendering modes and sizes until
    you get what you're looking for. If you need something larger, use
    ``create_graphics`` to create a non-visible drawing surface.

    The minimum width and height is around 100 pixels in each direction. This is the
    smallest that is supported across Windows, macOS, and Linux. We enforce the
    minimum size so that Sketches will run identically on different machines.

    The ``renderer`` parameter selects which rendering engine to use. For example,
    if you will be drawing 3D shapes, use ``P3D``. In addition to the default
    renderer, other renderers are:

    * ``P2D`` (Processing 2D): 2D graphics renderer that makes use of OpenGL-
    compatible graphics hardware.
    * ``P3D`` (Processing 3D): 3D graphics renderer that makes use of OpenGL-
    compatible graphics hardware.
    * ``FX2D`` (JavaFX 2D): A 2D renderer that uses JavaFX, which may be faster for
    some applications, but has some compatibility quirks.
    * ``PDF``: The ``PDF`` renderer draws 2D graphics directly to an Acrobat PDF
    file. This produces excellent results when you need vector shapes for high-
    resolution output or printing.
    * ``SVG``: The ``SVG`` renderer draws 2D graphics directly to an SVG file. This
    is great for importing into other vector programs or using for digital
    fabrication.
    """
    return _py5sketch.size(*args)


@overload
def smooth() -> None:
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

    With the ``P2D`` and ``P3D`` renderers, ``smooth(2)`` is the default, this is
    called "2x anti-aliasing." The code ``smooth(4)`` is used for 4x anti-aliasing
    and ``smooth(8)`` is specified for "8x anti-aliasing." The maximum anti-aliasing
    level is determined by the hardware of the machine that is running the software,
    so ``smooth(4)`` and ``smooth(8)`` will not work with every computer.

    The default renderer uses ``smooth(3)`` by default. This is bicubic smoothing.
    The other option for the default renderer is ``smooth(2)``, which is bilinear
    smoothing.

    The ``smooth()`` function can only be set once within a Sketch. It must be
    called from the `settings()`` function. The ``no_smooth()`` function also
    follows the same rules.
    """
    pass


@overload
def smooth(level: int, /) -> None:
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

    With the ``P2D`` and ``P3D`` renderers, ``smooth(2)`` is the default, this is
    called "2x anti-aliasing." The code ``smooth(4)`` is used for 4x anti-aliasing
    and ``smooth(8)`` is specified for "8x anti-aliasing." The maximum anti-aliasing
    level is determined by the hardware of the machine that is running the software,
    so ``smooth(4)`` and ``smooth(8)`` will not work with every computer.

    The default renderer uses ``smooth(3)`` by default. This is bicubic smoothing.
    The other option for the default renderer is ``smooth(2)``, which is bilinear
    smoothing.

    The ``smooth()`` function can only be set once within a Sketch. It must be
    called from the `settings()`` function. The ``no_smooth()`` function also
    follows the same rules.
    """
    pass


def smooth(*args):
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

    With the ``P2D`` and ``P3D`` renderers, ``smooth(2)`` is the default, this is
    called "2x anti-aliasing." The code ``smooth(4)`` is used for 4x anti-aliasing
    and ``smooth(8)`` is specified for "8x anti-aliasing." The maximum anti-aliasing
    level is determined by the hardware of the machine that is running the software,
    so ``smooth(4)`` and ``smooth(8)`` will not work with every computer.

    The default renderer uses ``smooth(3)`` by default. This is bicubic smoothing.
    The other option for the default renderer is ``smooth(2)``, which is bilinear
    smoothing.

    The ``smooth()`` function can only be set once within a Sketch. It must be
    called from the `settings()`` function. The ``no_smooth()`` function also
    follows the same rules.
    """
    return _py5sketch.smooth(*args)


@overload
def specular(gray: float, /) -> None:
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
    diffuse light). Use in combination with ``emissive()``, ``ambient()``, and
    ``shininess()`` to set the material properties of shapes.
    """
    pass


@overload
def specular(v1: float, v2: float, v3: float, /) -> None:
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
    diffuse light). Use in combination with ``emissive()``, ``ambient()``, and
    ``shininess()`` to set the material properties of shapes.
    """
    pass


@overload
def specular(rgb: int, /) -> None:
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
    diffuse light). Use in combination with ``emissive()``, ``ambient()``, and
    ``shininess()`` to set the material properties of shapes.
    """
    pass


def specular(*args):
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
    diffuse light). Use in combination with ``emissive()``, ``ambient()``, and
    ``shininess()`` to set the material properties of shapes.
    """
    return _py5sketch.specular(*args)


def sphere(r: float, /) -> None:
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
    return _py5sketch.sphere(r)


@overload
def sphere_detail(res: int, /) -> None:
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
    detailed sphere definition with vertices every ``360/30 = 12`` degrees. If
    you're going to render a great number of spheres per frame, it is advised to
    reduce the level of detail using this function. The setting stays active until
    ``sphere_detail()`` is called again with a new parameter and so should *not* be
    called prior to every ``sphere()`` statement, unless you wish to render spheres
    with different settings, e.g. using less detail for smaller spheres or ones
    further away from the camera. To control the detail of the horizontal and
    vertical resolution independently, use the version of the functions with two
    parameters.
    """
    pass


@overload
def sphere_detail(ures: int, vres: int, /) -> None:
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
    detailed sphere definition with vertices every ``360/30 = 12`` degrees. If
    you're going to render a great number of spheres per frame, it is advised to
    reduce the level of detail using this function. The setting stays active until
    ``sphere_detail()`` is called again with a new parameter and so should *not* be
    called prior to every ``sphere()`` statement, unless you wish to render spheres
    with different settings, e.g. using less detail for smaller spheres or ones
    further away from the camera. To control the detail of the horizontal and
    vertical resolution independently, use the version of the functions with two
    parameters.
    """
    pass


def sphere_detail(*args):
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
    detailed sphere definition with vertices every ``360/30 = 12`` degrees. If
    you're going to render a great number of spheres per frame, it is advised to
    reduce the level of detail using this function. The setting stays active until
    ``sphere_detail()`` is called again with a new parameter and so should *not* be
    called prior to every ``sphere()`` statement, unless you wish to render spheres
    with different settings, e.g. using less detail for smaller spheres or ones
    further away from the camera. To control the detail of the horizontal and
    vertical resolution independently, use the version of the functions with two
    parameters.
    """
    return _py5sketch.sphere_detail(*args)


def spot_light(v1: float, v2: float, v3: float, x: float, y: float, z: float,
               nx: float, ny: float, nz: float, angle: float, concentration: float, /) -> None:
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
    return _py5sketch.spot_light(
        v1, v2, v3, x, y, z, nx, ny, nz, angle, concentration)


def square(x: float, y: float, extent: float, /) -> None:
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
    return _py5sketch.square(x, y, extent)


@overload
def stroke(gray: float, /) -> None:
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
    ``color_mode()``. The default color space is RGB, with each value in the range
    from 0 to 255.

    When using hexadecimal notation to specify a color, use "``0x``" before the
    values (e.g., ``0xFFCCFFAA``). The hexadecimal value must be specified with
    eight characters; the first two characters define the alpha component, and the
    remainder define the red, green, and blue components.

    The value for the gray parameter must be less than or equal to the current
    maximum value as specified by ``color_mode()``. The default maximum value is
    255.

    When drawing in 2D with the default renderer, you may need
    ``hint(ENABLE_STROKE_PURE)`` to improve drawing quality (at the expense of
    performance). See the ``hint()`` documentation for more details.
    """
    pass


@overload
def stroke(gray: float, alpha: float, /) -> None:
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
    ``color_mode()``. The default color space is RGB, with each value in the range
    from 0 to 255.

    When using hexadecimal notation to specify a color, use "``0x``" before the
    values (e.g., ``0xFFCCFFAA``). The hexadecimal value must be specified with
    eight characters; the first two characters define the alpha component, and the
    remainder define the red, green, and blue components.

    The value for the gray parameter must be less than or equal to the current
    maximum value as specified by ``color_mode()``. The default maximum value is
    255.

    When drawing in 2D with the default renderer, you may need
    ``hint(ENABLE_STROKE_PURE)`` to improve drawing quality (at the expense of
    performance). See the ``hint()`` documentation for more details.
    """
    pass


@overload
def stroke(v1: float, v2: float, v3: float, /) -> None:
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
    ``color_mode()``. The default color space is RGB, with each value in the range
    from 0 to 255.

    When using hexadecimal notation to specify a color, use "``0x``" before the
    values (e.g., ``0xFFCCFFAA``). The hexadecimal value must be specified with
    eight characters; the first two characters define the alpha component, and the
    remainder define the red, green, and blue components.

    The value for the gray parameter must be less than or equal to the current
    maximum value as specified by ``color_mode()``. The default maximum value is
    255.

    When drawing in 2D with the default renderer, you may need
    ``hint(ENABLE_STROKE_PURE)`` to improve drawing quality (at the expense of
    performance). See the ``hint()`` documentation for more details.
    """
    pass


@overload
def stroke(v1: float, v2: float, v3: float, alpha: float, /) -> None:
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
    ``color_mode()``. The default color space is RGB, with each value in the range
    from 0 to 255.

    When using hexadecimal notation to specify a color, use "``0x``" before the
    values (e.g., ``0xFFCCFFAA``). The hexadecimal value must be specified with
    eight characters; the first two characters define the alpha component, and the
    remainder define the red, green, and blue components.

    The value for the gray parameter must be less than or equal to the current
    maximum value as specified by ``color_mode()``. The default maximum value is
    255.

    When drawing in 2D with the default renderer, you may need
    ``hint(ENABLE_STROKE_PURE)`` to improve drawing quality (at the expense of
    performance). See the ``hint()`` documentation for more details.
    """
    pass


@overload
def stroke(rgb: int, /) -> None:
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
    ``color_mode()``. The default color space is RGB, with each value in the range
    from 0 to 255.

    When using hexadecimal notation to specify a color, use "``0x``" before the
    values (e.g., ``0xFFCCFFAA``). The hexadecimal value must be specified with
    eight characters; the first two characters define the alpha component, and the
    remainder define the red, green, and blue components.

    The value for the gray parameter must be less than or equal to the current
    maximum value as specified by ``color_mode()``. The default maximum value is
    255.

    When drawing in 2D with the default renderer, you may need
    ``hint(ENABLE_STROKE_PURE)`` to improve drawing quality (at the expense of
    performance). See the ``hint()`` documentation for more details.
    """
    pass


@overload
def stroke(rgb: int, alpha: float, /) -> None:
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
    ``color_mode()``. The default color space is RGB, with each value in the range
    from 0 to 255.

    When using hexadecimal notation to specify a color, use "``0x``" before the
    values (e.g., ``0xFFCCFFAA``). The hexadecimal value must be specified with
    eight characters; the first two characters define the alpha component, and the
    remainder define the red, green, and blue components.

    The value for the gray parameter must be less than or equal to the current
    maximum value as specified by ``color_mode()``. The default maximum value is
    255.

    When drawing in 2D with the default renderer, you may need
    ``hint(ENABLE_STROKE_PURE)`` to improve drawing quality (at the expense of
    performance). See the ``hint()`` documentation for more details.
    """
    pass


def stroke(*args):
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
    ``color_mode()``. The default color space is RGB, with each value in the range
    from 0 to 255.

    When using hexadecimal notation to specify a color, use "``0x``" before the
    values (e.g., ``0xFFCCFFAA``). The hexadecimal value must be specified with
    eight characters; the first two characters define the alpha component, and the
    remainder define the red, green, and blue components.

    The value for the gray parameter must be less than or equal to the current
    maximum value as specified by ``color_mode()``. The default maximum value is
    255.

    When drawing in 2D with the default renderer, you may need
    ``hint(ENABLE_STROKE_PURE)`` to improve drawing quality (at the expense of
    performance). See the ``hint()`` documentation for more details.
    """
    return _py5sketch.stroke(*args)


def stroke_cap(cap: int, /) -> None:
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
    ``SQUARE``, ``PROJECT``, and ``ROUND``. The default cap is ``ROUND``.

    To make ``point()`` appear square, use ``stroke_cap(PROJECT)``. Using
    ``stroke_cap(SQUARE)`` (no cap) causes points to become invisible.
    """
    return _py5sketch.stroke_cap(cap)


def stroke_join(join: int, /) -> None:
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
    parameters ``MITER``, ``BEVEL``, and ``ROUND``. The default joint is ``MITER``.
    """
    return _py5sketch.stroke_join(join)


def stroke_weight(weight: float, /) -> None:
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

    Using ``point()`` with ``strokeWeight(1)`` or smaller may draw nothing to the
    screen, depending on the graphics settings of the computer. Workarounds include
    setting the pixel using the ``pixels[]`` or ``np_pixels[]`` arrays or drawing
    the point using either ``circle()`` or ``square()``.
    """
    return _py5sketch.stroke_weight(weight)


@overload
def text(c: chr, x: float, y: float, /) -> None:
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

    Note that py5 lets you call ``text()`` without first specifying a Py5Font with
    ``text_font()``. In that case, a generic sans-serif font will be used instead.
    (See the third example.)
    """
    pass


@overload
def text(c: chr, x: float, y: float, z: float, /) -> None:
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

    Note that py5 lets you call ``text()`` without first specifying a Py5Font with
    ``text_font()``. In that case, a generic sans-serif font will be used instead.
    (See the third example.)
    """
    pass


@overload
def text(chars: List[chr], start: int, stop: int,
         x: float, y: float, /) -> None:
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

    Note that py5 lets you call ``text()`` without first specifying a Py5Font with
    ``text_font()``. In that case, a generic sans-serif font will be used instead.
    (See the third example.)
    """
    pass


@overload
def text(chars: List[chr], start: int, stop: int,
         x: float, y: float, z: float, /) -> None:
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

    Note that py5 lets you call ``text()`` without first specifying a Py5Font with
    ``text_font()``. In that case, a generic sans-serif font will be used instead.
    (See the third example.)
    """
    pass


@overload
def text(num: float, x: float, y: float, /) -> None:
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

    Note that py5 lets you call ``text()`` without first specifying a Py5Font with
    ``text_font()``. In that case, a generic sans-serif font will be used instead.
    (See the third example.)
    """
    pass


@overload
def text(num: float, x: float, y: float, z: float, /) -> None:
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

    Note that py5 lets you call ``text()`` without first specifying a Py5Font with
    ``text_font()``. In that case, a generic sans-serif font will be used instead.
    (See the third example.)
    """
    pass


@overload
def text(num: int, x: float, y: float, /) -> None:
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

    Note that py5 lets you call ``text()`` without first specifying a Py5Font with
    ``text_font()``. In that case, a generic sans-serif font will be used instead.
    (See the third example.)
    """
    pass


@overload
def text(num: int, x: float, y: float, z: float, /) -> None:
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

    Note that py5 lets you call ``text()`` without first specifying a Py5Font with
    ``text_font()``. In that case, a generic sans-serif font will be used instead.
    (See the third example.)
    """
    pass


@overload
def text(str: str, x: float, y: float, /) -> None:
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

    Note that py5 lets you call ``text()`` without first specifying a Py5Font with
    ``text_font()``. In that case, a generic sans-serif font will be used instead.
    (See the third example.)
    """
    pass


@overload
def text(str: str, x: float, y: float, z: float, /) -> None:
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

    Note that py5 lets you call ``text()`` without first specifying a Py5Font with
    ``text_font()``. In that case, a generic sans-serif font will be used instead.
    (See the third example.)
    """
    pass


@overload
def text(str: str, x1: float, y1: float, x2: float, y2: float, /) -> None:
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

    Note that py5 lets you call ``text()`` without first specifying a Py5Font with
    ``text_font()``. In that case, a generic sans-serif font will be used instead.
    (See the third example.)
    """
    pass


def text(*args):
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

    Note that py5 lets you call ``text()`` without first specifying a Py5Font with
    ``text_font()``. In that case, a generic sans-serif font will be used instead.
    (See the third example.)
    """
    return _py5sketch.text(*args)


@overload
def text_align(align_x: int, /) -> None:
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

    Sets the current alignment for drawing text. The parameters ``LEFT``,
    ``CENTER``, and ``RIGHT`` set the display characteristics of the letters in
    relation to the values for the ``x`` and ``y`` parameters of the ``text()``
    function.

    An optional second parameter can be used to vertically align the text.
    ``BASELINE`` is the default, and the vertical alignment will be reset to
    ``BASELINE`` if the second parameter is not used. The ``TOP`` and ``CENTER``
    parameters are straightforward. The ``BOTTOM`` parameter offsets the line based
    on the current ``text_descent()``. For multiple lines, the final line will be
    aligned to the bottom, with the previous lines appearing above it.

    When using ``text()`` with width and height parameters, ``BASELINE`` is ignored,
    and treated as ``TOP``. (Otherwise, text would by default draw outside the box,
    since ``BASELINE`` is the default setting. ``BASELINE`` is not a useful drawing
    mode for text drawn in a rectangle.)

    The vertical alignment is based on the value of ``text_ascent()``, which many
    fonts do not specify correctly. It may be necessary to use a hack and offset by
    a few pixels by hand so that the offset looks correct. To do this as less of a
    hack, use some percentage of ``text_ascent()`` or ``text_descent()`` so that the
    hack works even if you change the size of the font.
    """
    pass


@overload
def text_align(align_x: int, align_y: int, /) -> None:
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

    Sets the current alignment for drawing text. The parameters ``LEFT``,
    ``CENTER``, and ``RIGHT`` set the display characteristics of the letters in
    relation to the values for the ``x`` and ``y`` parameters of the ``text()``
    function.

    An optional second parameter can be used to vertically align the text.
    ``BASELINE`` is the default, and the vertical alignment will be reset to
    ``BASELINE`` if the second parameter is not used. The ``TOP`` and ``CENTER``
    parameters are straightforward. The ``BOTTOM`` parameter offsets the line based
    on the current ``text_descent()``. For multiple lines, the final line will be
    aligned to the bottom, with the previous lines appearing above it.

    When using ``text()`` with width and height parameters, ``BASELINE`` is ignored,
    and treated as ``TOP``. (Otherwise, text would by default draw outside the box,
    since ``BASELINE`` is the default setting. ``BASELINE`` is not a useful drawing
    mode for text drawn in a rectangle.)

    The vertical alignment is based on the value of ``text_ascent()``, which many
    fonts do not specify correctly. It may be necessary to use a hack and offset by
    a few pixels by hand so that the offset looks correct. To do this as less of a
    hack, use some percentage of ``text_ascent()`` or ``text_descent()`` so that the
    hack works even if you change the size of the font.
    """
    pass


def text_align(*args):
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

    Sets the current alignment for drawing text. The parameters ``LEFT``,
    ``CENTER``, and ``RIGHT`` set the display characteristics of the letters in
    relation to the values for the ``x`` and ``y`` parameters of the ``text()``
    function.

    An optional second parameter can be used to vertically align the text.
    ``BASELINE`` is the default, and the vertical alignment will be reset to
    ``BASELINE`` if the second parameter is not used. The ``TOP`` and ``CENTER``
    parameters are straightforward. The ``BOTTOM`` parameter offsets the line based
    on the current ``text_descent()``. For multiple lines, the final line will be
    aligned to the bottom, with the previous lines appearing above it.

    When using ``text()`` with width and height parameters, ``BASELINE`` is ignored,
    and treated as ``TOP``. (Otherwise, text would by default draw outside the box,
    since ``BASELINE`` is the default setting. ``BASELINE`` is not a useful drawing
    mode for text drawn in a rectangle.)

    The vertical alignment is based on the value of ``text_ascent()``, which many
    fonts do not specify correctly. It may be necessary to use a hack and offset by
    a few pixels by hand so that the offset looks correct. To do this as less of a
    hack, use some percentage of ``text_ascent()`` or ``text_descent()`` so that the
    hack works even if you change the size of the font.
    """
    return _py5sketch.text_align(*args)


def text_ascent() -> float:
    """Returns ascent of the current font at its current size.

    Underlying Java method: PApplet.textAscent

    Notes
    -----

    Returns ascent of the current font at its current size. This information is
    useful for determining the height of the font above the baseline.
    """
    return _py5sketch.text_ascent()


def text_descent() -> float:
    """Returns descent of the current font at its current size.

    Underlying Java method: PApplet.textDescent

    Notes
    -----

    Returns descent of the current font at its current size. This information is
    useful for determining the height of the font below the baseline.
    """
    return _py5sketch.text_descent()


@overload
def text_font(which: Py5Font, /) -> None:
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
        any variable of the type Py5Font

    Notes
    -----

    Sets the current font that will be drawn with the ``text()`` function. Fonts
    must be created for py5 with ``create_font()`` or loaded with ``load_font()``
    before they can be used. The font set through ``text_font()`` will be used in
    all subsequent calls to the ``text()`` function. If no ``size`` parameter is
    specified, the font size defaults to the original size (the size in which it was
    created with ``create_font_file()``) overriding any previous calls to
    ``text_font()`` or ``text_size()``.

    When fonts are rendered as an image texture (as is the case with the ``P2D`` and
    ``P3D`` renderers as well as with ``load_font()`` and vlw files), you should
    create fonts at the sizes that will be used most commonly. Using ``text_font()``
    without the size parameter will result in the cleanest type.
    """
    pass


@overload
def text_font(which: Py5Font, size: float, /) -> None:
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
        any variable of the type Py5Font

    Notes
    -----

    Sets the current font that will be drawn with the ``text()`` function. Fonts
    must be created for py5 with ``create_font()`` or loaded with ``load_font()``
    before they can be used. The font set through ``text_font()`` will be used in
    all subsequent calls to the ``text()`` function. If no ``size`` parameter is
    specified, the font size defaults to the original size (the size in which it was
    created with ``create_font_file()``) overriding any previous calls to
    ``text_font()`` or ``text_size()``.

    When fonts are rendered as an image texture (as is the case with the ``P2D`` and
    ``P3D`` renderers as well as with ``load_font()`` and vlw files), you should
    create fonts at the sizes that will be used most commonly. Using ``text_font()``
    without the size parameter will result in the cleanest type.
    """
    pass


def text_font(*args):
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
        any variable of the type Py5Font

    Notes
    -----

    Sets the current font that will be drawn with the ``text()`` function. Fonts
    must be created for py5 with ``create_font()`` or loaded with ``load_font()``
    before they can be used. The font set through ``text_font()`` will be used in
    all subsequent calls to the ``text()`` function. If no ``size`` parameter is
    specified, the font size defaults to the original size (the size in which it was
    created with ``create_font_file()``) overriding any previous calls to
    ``text_font()`` or ``text_size()``.

    When fonts are rendered as an image texture (as is the case with the ``P2D`` and
    ``P3D`` renderers as well as with ``load_font()`` and vlw files), you should
    create fonts at the sizes that will be used most commonly. Using ``text_font()``
    without the size parameter will result in the cleanest type.
    """
    return _py5sketch.text_font(*args)


def text_leading(leading: float, /) -> None:
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
    return _py5sketch.text_leading(leading)


def text_mode(mode: int, /) -> None:
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
    return _py5sketch.text_mode(mode)


def text_size(size: float, /) -> None:
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
    return _py5sketch.text_size(size)


@overload
def text_width(c: chr, /) -> float:
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
    """
    pass


@overload
def text_width(chars: List[chr], start: int, length: int, /) -> float:
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
    """
    pass


@overload
def text_width(str: str, /) -> float:
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
    """
    pass


def text_width(*args):
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
    """
    return _py5sketch.text_width(*args)


def texture(image: Py5Image, /) -> None:
    """Sets a texture to be applied to vertex points.

    Underlying Java method: PApplet.texture

    Parameters
    ----------

    image: Py5Image
        reference to a Py5Image object

    Notes
    -----

    Sets a texture to be applied to vertex points. The ``texture()`` method must be
    called between ``begin_shape()`` and ``end_shape()`` and before any calls to
    ``vertex()``. This method only works with the ``P2D`` and ``P3D`` renderers.

    When textures are in use, the fill color is ignored. Instead, use ``tint()`` to
    specify the color of the texture as it is applied to the shape.
    """
    return _py5sketch.texture(image)


def texture_mode(mode: int, /) -> None:
    """Sets the coordinate space for texture mapping.

    Underlying Java method: PApplet.textureMode

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
    """
    return _py5sketch.texture_mode(mode)


def texture_wrap(wrap: int, /) -> None:
    """Defines if textures repeat or draw once within a texture map.

    Underlying Java method: PApplet.textureWrap

    Parameters
    ----------

    wrap: int
        Either CLAMP (default) or REPEAT

    Notes
    -----

    Defines if textures repeat or draw once within a texture map. The two parameters
    are ``CLAMP`` (the default behavior) and ``REPEAT``. This function only works
    with the ``P2D`` and ``P3D`` renderers.
    """
    return _py5sketch.texture_wrap(wrap)


@overload
def tint(gray: float, /) -> None:
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

    When using hexadecimal notation to specify a color, use "``0x``" before the
    values (e.g., ``0xFFCCFFAA``). The hexadecimal value must be specified with
    eight characters; the first two characters define the alpha component, and the
    remainder define the red, green, and blue components.

    The value for the gray parameter must be less than or equal to the current
    maximum value as specified by ``color_mode()``. The default maximum value is
    255.

    The ``tint()`` function is also used to control the coloring of textures in 3D.
    """
    pass


@overload
def tint(gray: float, alpha: float, /) -> None:
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

    When using hexadecimal notation to specify a color, use "``0x``" before the
    values (e.g., ``0xFFCCFFAA``). The hexadecimal value must be specified with
    eight characters; the first two characters define the alpha component, and the
    remainder define the red, green, and blue components.

    The value for the gray parameter must be less than or equal to the current
    maximum value as specified by ``color_mode()``. The default maximum value is
    255.

    The ``tint()`` function is also used to control the coloring of textures in 3D.
    """
    pass


@overload
def tint(v1: float, v2: float, v3: float, /) -> None:
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

    When using hexadecimal notation to specify a color, use "``0x``" before the
    values (e.g., ``0xFFCCFFAA``). The hexadecimal value must be specified with
    eight characters; the first two characters define the alpha component, and the
    remainder define the red, green, and blue components.

    The value for the gray parameter must be less than or equal to the current
    maximum value as specified by ``color_mode()``. The default maximum value is
    255.

    The ``tint()`` function is also used to control the coloring of textures in 3D.
    """
    pass


@overload
def tint(v1: float, v2: float, v3: float, alpha: float, /) -> None:
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

    When using hexadecimal notation to specify a color, use "``0x``" before the
    values (e.g., ``0xFFCCFFAA``). The hexadecimal value must be specified with
    eight characters; the first two characters define the alpha component, and the
    remainder define the red, green, and blue components.

    The value for the gray parameter must be less than or equal to the current
    maximum value as specified by ``color_mode()``. The default maximum value is
    255.

    The ``tint()`` function is also used to control the coloring of textures in 3D.
    """
    pass


@overload
def tint(rgb: int, /) -> None:
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

    When using hexadecimal notation to specify a color, use "``0x``" before the
    values (e.g., ``0xFFCCFFAA``). The hexadecimal value must be specified with
    eight characters; the first two characters define the alpha component, and the
    remainder define the red, green, and blue components.

    The value for the gray parameter must be less than or equal to the current
    maximum value as specified by ``color_mode()``. The default maximum value is
    255.

    The ``tint()`` function is also used to control the coloring of textures in 3D.
    """
    pass


@overload
def tint(rgb: int, alpha: float, /) -> None:
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

    When using hexadecimal notation to specify a color, use "``0x``" before the
    values (e.g., ``0xFFCCFFAA``). The hexadecimal value must be specified with
    eight characters; the first two characters define the alpha component, and the
    remainder define the red, green, and blue components.

    The value for the gray parameter must be less than or equal to the current
    maximum value as specified by ``color_mode()``. The default maximum value is
    255.

    The ``tint()`` function is also used to control the coloring of textures in 3D.
    """
    pass


def tint(*args):
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

    When using hexadecimal notation to specify a color, use "``0x``" before the
    values (e.g., ``0xFFCCFFAA``). The hexadecimal value must be specified with
    eight characters; the first two characters define the alpha component, and the
    remainder define the red, green, and blue components.

    The value for the gray parameter must be less than or equal to the current
    maximum value as specified by ``color_mode()``. The default maximum value is
    255.

    The ``tint()`` function is also used to control the coloring of textures in 3D.
    """
    return _py5sketch.tint(*args)


@overload
def translate(x: float, y: float, /) -> None:
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
    from the screen. Using this function with the ``z`` parameter requires using
    ``P3D`` as a parameter in combination with size as shown in the second example.

    Transformations are cumulative and apply to everything that happens after and
    subsequent calls to the function accumulates the effect. For example, calling
    ``translate(50, 0)`` and then ``translate(20, 0)`` is the same as
    ``translate(70, 0)``. If ``translate()`` is called within ``draw()``, the
    transformation is reset when the loop begins again. This function can be further
    controlled by using ``push_matrix()`` and ``pop_matrix()``.
    """
    pass


@overload
def translate(x: float, y: float, z: float, /) -> None:
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
    from the screen. Using this function with the ``z`` parameter requires using
    ``P3D`` as a parameter in combination with size as shown in the second example.

    Transformations are cumulative and apply to everything that happens after and
    subsequent calls to the function accumulates the effect. For example, calling
    ``translate(50, 0)`` and then ``translate(20, 0)`` is the same as
    ``translate(70, 0)``. If ``translate()`` is called within ``draw()``, the
    transformation is reset when the loop begins again. This function can be further
    controlled by using ``push_matrix()`` and ``pop_matrix()``.
    """
    pass


def translate(*args):
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
    from the screen. Using this function with the ``z`` parameter requires using
    ``P3D`` as a parameter in combination with size as shown in the second example.

    Transformations are cumulative and apply to everything that happens after and
    subsequent calls to the function accumulates the effect. For example, calling
    ``translate(50, 0)`` and then ``translate(20, 0)`` is the same as
    ``translate(70, 0)``. If ``translate()`` is called within ``draw()``, the
    transformation is reset when the loop begins again. This function can be further
    controlled by using ``push_matrix()`` and ``pop_matrix()``.
    """
    return _py5sketch.translate(*args)


def triangle(x1: float, y1: float, x2: float, y2: float,
             x3: float, y3: float, /) -> None:
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
    return _py5sketch.triangle(x1, y1, x2, y2, x3, y3)


@overload
def update_pixels() -> None:
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
def update_pixels(x1: int, y1: int, x2: int, y2: int, /) -> None:
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


def update_pixels(*args):
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
    return _py5sketch.update_pixels(*args)


@overload
def vertex(x: float, y: float, /) -> None:
    """Add a new vertex to a shape.

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

    Add a new vertex to a shape. All shapes are constructed by connecting a series
    of vertices. The ``vertex()`` method is used to specify the vertex coordinates
    for points, lines, triangles, quads, and polygons. It is used exclusively within
    the ``begin_shape()`` and ``end_shape()`` functions.

    Drawing a vertex in 3D using the ``z`` parameter requires the ``P3D`` renderer,
    as shown in the second example.

    This method is also used to map a texture onto geometry. The ``texture()``
    function declares the texture to apply to the geometry and the ``u`` and ``v``
    coordinates define the mapping of this texture to the form. By default, the
    coordinates used for ``u`` and ``v`` are specified in relation to the image's
    size in pixels, but this relation can be changed with the Sketch's
    ``texture_mode()`` method.
    """
    pass


@overload
def vertex(x: float, y: float, z: float, /) -> None:
    """Add a new vertex to a shape.

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

    Add a new vertex to a shape. All shapes are constructed by connecting a series
    of vertices. The ``vertex()`` method is used to specify the vertex coordinates
    for points, lines, triangles, quads, and polygons. It is used exclusively within
    the ``begin_shape()`` and ``end_shape()`` functions.

    Drawing a vertex in 3D using the ``z`` parameter requires the ``P3D`` renderer,
    as shown in the second example.

    This method is also used to map a texture onto geometry. The ``texture()``
    function declares the texture to apply to the geometry and the ``u`` and ``v``
    coordinates define the mapping of this texture to the form. By default, the
    coordinates used for ``u`` and ``v`` are specified in relation to the image's
    size in pixels, but this relation can be changed with the Sketch's
    ``texture_mode()`` method.
    """
    pass


@overload
def vertex(x: float, y: float, u: float, v: float, /) -> None:
    """Add a new vertex to a shape.

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

    Add a new vertex to a shape. All shapes are constructed by connecting a series
    of vertices. The ``vertex()`` method is used to specify the vertex coordinates
    for points, lines, triangles, quads, and polygons. It is used exclusively within
    the ``begin_shape()`` and ``end_shape()`` functions.

    Drawing a vertex in 3D using the ``z`` parameter requires the ``P3D`` renderer,
    as shown in the second example.

    This method is also used to map a texture onto geometry. The ``texture()``
    function declares the texture to apply to the geometry and the ``u`` and ``v``
    coordinates define the mapping of this texture to the form. By default, the
    coordinates used for ``u`` and ``v`` are specified in relation to the image's
    size in pixels, but this relation can be changed with the Sketch's
    ``texture_mode()`` method.
    """
    pass


@overload
def vertex(x: float, y: float, z: float, u: float, v: float, /) -> None:
    """Add a new vertex to a shape.

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

    Add a new vertex to a shape. All shapes are constructed by connecting a series
    of vertices. The ``vertex()`` method is used to specify the vertex coordinates
    for points, lines, triangles, quads, and polygons. It is used exclusively within
    the ``begin_shape()`` and ``end_shape()`` functions.

    Drawing a vertex in 3D using the ``z`` parameter requires the ``P3D`` renderer,
    as shown in the second example.

    This method is also used to map a texture onto geometry. The ``texture()``
    function declares the texture to apply to the geometry and the ``u`` and ``v``
    coordinates define the mapping of this texture to the form. By default, the
    coordinates used for ``u`` and ``v`` are specified in relation to the image's
    size in pixels, but this relation can be changed with the Sketch's
    ``texture_mode()`` method.
    """
    pass


@overload
def vertex(v: NDArray[(Any,), Float], /) -> None:
    """Add a new vertex to a shape.

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

    Add a new vertex to a shape. All shapes are constructed by connecting a series
    of vertices. The ``vertex()`` method is used to specify the vertex coordinates
    for points, lines, triangles, quads, and polygons. It is used exclusively within
    the ``begin_shape()`` and ``end_shape()`` functions.

    Drawing a vertex in 3D using the ``z`` parameter requires the ``P3D`` renderer,
    as shown in the second example.

    This method is also used to map a texture onto geometry. The ``texture()``
    function declares the texture to apply to the geometry and the ``u`` and ``v``
    coordinates define the mapping of this texture to the form. By default, the
    coordinates used for ``u`` and ``v`` are specified in relation to the image's
    size in pixels, but this relation can be changed with the Sketch's
    ``texture_mode()`` method.
    """
    pass


def vertex(*args):
    """Add a new vertex to a shape.

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

    Add a new vertex to a shape. All shapes are constructed by connecting a series
    of vertices. The ``vertex()`` method is used to specify the vertex coordinates
    for points, lines, triangles, quads, and polygons. It is used exclusively within
    the ``begin_shape()`` and ``end_shape()`` functions.

    Drawing a vertex in 3D using the ``z`` parameter requires the ``P3D`` renderer,
    as shown in the second example.

    This method is also used to map a texture onto geometry. The ``texture()``
    function declares the texture to apply to the geometry and the ``u`` and ``v``
    coordinates define the mapping of this texture to the form. By default, the
    coordinates used for ``u`` and ``v`` are specified in relation to the image's
    size in pixels, but this relation can be changed with the Sketch's
    ``texture_mode()`` method.
    """
    return _py5sketch.vertex(*args)


def vertices(coordinates: NDArray[(Any, Any), Float], /) -> None:
    """Create a collection of vertices.

    Underlying Java method: PApplet.vertices

    Parameters
    ----------

    coordinates: NDArray[(Any, Any), Float]
        array of vertex coordinates

    Notes
    -----

    Create a collection of vertices. The purpose of this method is to provide an
    alternative to repeatedly calling ``vertex()`` in a loop. For a large number of
    vertices, the performance of ``vertices()`` will be much faster.

    The ``coordinates`` parameter should be a numpy array with one row for each
    vertex. There should be two or three columns for 2D or 3D points, respectively.
    """
    return _py5sketch.vertices(coordinates)


def year() -> int:
    """Py5 communicates with the clock on your computer.

    Underlying Java method: PApplet.year

    Notes
    -----

    Py5 communicates with the clock on your computer. The ``year()`` function
    returns the current year as an integer (2003, 2004, 2005, etc).
    """
    return Sketch.year()

##############################################################################
# module functions from pixels.py
##############################################################################


def load_np_pixels() -> None:
    """Loads the pixel data of the current display window into the ``np_pixels[]``
    array.

    Notes
    -----

    Loads the pixel data of the current display window into the ``np_pixels[]``
    array. This method must always be called before reading from or writing to
    ``np_pixels[]``. Subsequent changes to the display window will not be reflected
    in ``np_pixels[]`` until ``load_np_pixels()`` is called again.

    The ``load_np_pixels()`` method is similar to ``load_pixels()`` in that
    ``load_np_pixels()`` must be called before reading from or writing to
    ``np_pixels[]`` just as ``load_pixels()`` must be called before reading from or
    writing to ``pixels[]``.

    Note that ``load_np_pixels()`` will as a side effect call ``load_pixels()``, so
    if your code needs to read ``np_pixels[]`` and ``pixels[]`` simultaneously,
    there is no need for a separate call to ``load_pixels()``. However, be aware
    that modifying both ``np_pixels[]`` and ``pixels[]`` simultaneously will likely
    result in the updates to ``pixels[]`` being discarded.
    """
    return _py5sketch.load_np_pixels()


def update_np_pixels() -> None:
    """Updates the display window with the data in the ``np_pixels[]`` array.

    Notes
    -----

    Updates the display window with the data in the ``np_pixels[]`` array. Use in
    conjunction with ``load_np_pixels()``. If you're only reading pixels from the
    array, there's no need to call ``update_np_pixels()`` — updating is only
    necessary to apply changes.

    The ``update_np_pixels()`` method is similar to ``update_pixels()`` in that
    ``update_np_pixels()`` must be called after modifying ``np_pixels[]`` just as
    ``update_pixels()`` must be called after modifying ``pixels[]``.
    """
    return _py5sketch.update_np_pixels()


np_pixels: np.ndarray = None


def set_np_pixels(array: np.ndarray, bands: str = 'ARGB') -> None:
    """Set the entire contents of ``np_pixels[]`` to the contents of another properly
    sized and typed numpy array.

    Parameters
    ----------

    array: np.ndarray
        properly sized numpy array to be copied to np_pixels[]

    bands: str = 'ARGB'
        color channels in the array's third dimension

    Notes
    -----

    Set the entire contents of ``np_pixels[]`` to the contents of another properly
    sized and typed numpy array. The size of ``array``'s first and second dimensions
    must match the height and width of the Sketch window, respectively. The array's
    ``dtype`` must be ``np.uint8``.

    The ``bands`` parameter is used to interpret the ``array``'s color channel
    dimension (the array's third dimension). It can be one of ``'L'`` (single-
    channel grayscale), ``'ARGB'``, ``'RGB'``, or ``'RGBA'``. If there is no alpha
    channel, ``array`` is assumed to have no transparency, but recall that the
    display window's pixels can never be transparent so any transparency in
    ``array`` will have no effect. If the ``bands`` parameter is ``'L'``,
    ``array``'s third dimension is optional.

    This method makes its own calls to ``load_np_pixels()`` and
    ``update_np_pixels()`` so there is no need to call either explicitly.

    This method exists because setting the array contents with the code
    ``py5.np_pixels = array`` will cause an error, while the correct syntax,
    ``py5.np_pixels[:] = array``, might also be unintuitive for beginners.
    """
    return _py5sketch.set_np_pixels(array, bands=bands)


def save(filename: Union[str,
                         Path],
         *,
         format: str = None,
         drop_alpha: bool = True,
         use_thread: bool = True,
         **params) -> None:
    """Save image data to a file.

    Parameters
    ----------

    drop_alpha: bool = True
        remove the alpha channel when saving the image

    filename: Union[str, Path]
        output filename

    format: str = None
        image format, if not determined from filename extension

    params
        keyword arguments to pass to the PIL.Image save method

    use_thread: bool = True
        write file in separate thread

    Notes
    -----

    Save image data to a file. This method uses the Python library Pillow to write
    the image, so it can save images in any format that that library supports.

    Use the ``drop_alpha`` parameter to drop the alpha channel from the image. This
    defaults to ``True``. Some image formats such as JPG do not support alpha
    channels, and Pillow will throw an error if you try to save an image with the
    alpha channel in that format.

    The ``use_thread`` parameter will save the image in a separate Python thread.
    This improves performance by returning before the image has actually been
    written to the file.
    """
    return _py5sketch.save(
        filename,
        format=format,
        drop_alpha=drop_alpha,
        use_thread=use_thread,
        **params)


SIMPLEX_NOISE = 1
PERLIN_NOISE = 2
##############################################################################
# module functions from math.py
##############################################################################


def sin(angle: float) -> float:
    """Calculates the sine of an angle.

    Parameters
    ----------

    angle: float
        angle in radians

    Notes
    -----

    Calculates the sine of an angle. This function expects the values of the angle
    parameter to be provided in radians (values from ``0`` to ``TWO_PI``). Values
    are returned in the range -1 to 1.

    This function makes a call to the numpy ``sin()`` function.
    """
    return Sketch.sin(angle)


def cos(angle: float) -> float:
    """Calculates the cosine of an angle.

    Parameters
    ----------

    angle: float
        angle in radians

    Notes
    -----

    Calculates the cosine of an angle. This function expects the values of the angle
    parameter to be provided in radians (values from ``0`` to ``TWO_PI``). Values
    are returned in the range -1 to 1.

    This function makes a call to the numpy ``cos()`` function.
    """
    return Sketch.cos(angle)


def tan(angle: float) -> float:
    """Calculates the ratio of the sine and cosine of an angle.

    Parameters
    ----------

    angle: float
        angle in radians

    Notes
    -----

    Calculates the ratio of the sine and cosine of an angle. This function expects
    the values of the angle parameter to be provided in radians (values from ``0``
    to ``TWO_PI``). Values are returned in the range infinity to -infinity.

    This function makes a call to the numpy ``tan()`` function.
    """
    return Sketch.tan(angle)


def asin(value: float) -> float:
    """The inverse of ``sin()``, returns the arc sine of a value.

    Parameters
    ----------

    value: float
        value in the range of -1 to 1 whose arc sine is to be returned

    Notes
    -----

    The inverse of ``sin()``, returns the arc sine of a value. This function expects
    the values in the range of -1 to 1 and values are returned in the range
    ``-HALF_PI`` to ``HALF_PI``.

    This function makes a call to the numpy ``asin()`` function.
    """
    return Sketch.asin(value)


def acos(value: float) -> float:
    """The inverse of ``cos()``, returns the arc cosine of a value.

    Parameters
    ----------

    value: float
        value in the range of -1 to 1 whose arc cosine is to be returned

    Notes
    -----

    The inverse of ``cos()``, returns the arc cosine of a value. This function
    expects the values in the range of -1 to 1 and values are returned in the range
    ``0`` to ``PI``.

    This function makes a call to the numpy ``acos()`` function.
    """
    return Sketch.acos(value)


def atan(value: float) -> float:
    """The inverse of ``tan()``, returns the arc tangent of a value.

    Parameters
    ----------

    value: float
        value whose arc tangent is to be returned

    Notes
    -----

    The inverse of ``tan()``, returns the arc tangent of a value. This function
    expects the values in the range of -Infinity to Infinity and values are returned
    in the range ``-HALF_PI`` to ``HALF_PI``.

    This function makes a call to the numpy ``atan()`` function.
    """
    return Sketch.atan(value)


def atan2(y: float, x: float) -> float:
    """Calculates the angle (in radians) from a specified point to the coordinate
    origin as measured from the positive x-axis.

    Parameters
    ----------

    x: float
        x-coordinate of the point

    y: float
        y-coordinate of the point

    Notes
    -----

    Calculates the angle (in radians) from a specified point to the coordinate
    origin as measured from the positive x-axis. Values are returned as a float in
    the range from ``PI`` to ``-PI``. The ``atan2()`` function is most often used
    for orienting geometry to the position of the cursor. Note: The y-coordinate of
    the point is the first parameter, and the x-coordinate is the second parameter,
    due the the structure of calculating the tangent.

    This function makes a call to the numpy ``atan2()`` function.
    """
    return Sketch.atan2(y, x)


def degrees(radians: float) -> float:
    """Converts a radian measurement to its corresponding value in degrees.

    Parameters
    ----------

    radians: float
        radian value to convert to degrees

    Notes
    -----

    Converts a radian measurement to its corresponding value in degrees. Radians and
    degrees are two ways of measuring the same thing. There are 360 degrees in a
    circle and ``2*PI`` radians in a circle. For example, ``90° = PI/2 =
    1.5707964``. All trigonometric functions in py5 require their parameters to be
    specified in radians.

    This function makes a call to the numpy ``degrees()`` function.
    """
    return Sketch.degrees(radians)


def radians(degrees: float) -> float:
    """Converts a degree measurement to its corresponding value in radians.

    Parameters
    ----------

    degrees: float
        degree value to convert to radians

    Notes
    -----

    Converts a degree measurement to its corresponding value in radians. Radians and
    degrees are two ways of measuring the same thing. There are 360 degrees in a
    circle and ``2*PI`` radians in a circle. For example, ``90° = PI/2 =
    1.5707964``. All trigonometric functions in py5 require their parameters to be
    specified in radians.

    This function makes a call to the numpy ``radians()`` function.
    """
    return Sketch.radians(degrees)


def constrain(amt: float, low: float, high: float) -> float:
    """Constrains a value to not exceed a maximum and minimum value.

    Parameters
    ----------

    amt: float
        the value to constrain

    high: float
        minimum limit

    low: float
        maximum limit

    Notes
    -----

    Constrains a value to not exceed a maximum and minimum value.
    """
    return Sketch.constrain(amt, low, high)


def remap(
        value: float,
        start1: float,
        stop1: float,
        start2: float,
        stop2: float) -> float:
    """Re-maps a number from one range to another.

    Parameters
    ----------

    start1: float
        lower bound of the value's current range

    start2: float
        upper bound of the value's current range

    stop1: float
        lower bound of the value's target range

    stop2: float
        upper bound of the value's target range

    value: float
        the incoming value to be converted

    Notes
    -----

    Re-maps a number from one range to another.

    In the first example, the number 0.5 is converted from a value in the range of 0
    to 1 into a value that ranges from the left edge of the window (0) to the right
    edge (``width``).

    As shown in the second example, numbers outside of the range are not clamped to
    the minimum and maximum parameters values, because out-of-range values are often
    intentional and useful. If that isn't what you want, try pairing this function
    with ``constrain()``.

    In Processing this functionality is provided by ``map()`` but was renamed in py5
    because of a name conflict with a builtin Python function.
    """
    return Sketch.remap(value, start1, stop1, start2, stop2)


@overload
def dist(x1: float, y1: float, x2: float, y2: float) -> float:
    """Calculates the distance between two points.

    Methods
    -------

    You can use any of the following signatures:

     * dist(x1: float, y1: float, x2: float, y2: float) -> float
     * dist(x1: float, y1: float, z1: float, x2: float, y2: float, z2: float) -> float

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

    Calculates the distance between two points.
    """
    pass


@overload
def dist(
        x1: float,
        y1: float,
        z1: float,
        x2: float,
        y2: float,
        z2: float) -> float:
    """Calculates the distance between two points.

    Methods
    -------

    You can use any of the following signatures:

     * dist(x1: float, y1: float, x2: float, y2: float) -> float
     * dist(x1: float, y1: float, z1: float, x2: float, y2: float, z2: float) -> float

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

    Calculates the distance between two points.
    """
    pass


def dist(*args: float) -> float:
    """Calculates the distance between two points.

    Methods
    -------

    You can use any of the following signatures:

     * dist(x1: float, y1: float, x2: float, y2: float) -> float
     * dist(x1: float, y1: float, z1: float, x2: float, y2: float, z2: float) -> float

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

    Calculates the distance between two points.
    """
    return Sketch.dist(*args)


def lerp(start: float, stop: float, amt: float) -> float:
    """Calculates a number between two numbers at a specific increment.

    Parameters
    ----------

    amt: float
        float between 0.0 and 1.0

    start: float
        first value

    stop: float
        second value

    Notes
    -----

    Calculates a number between two numbers at a specific increment. The ``amt``
    parameter is the amount to interpolate between the two values where 0.0 equal to
    the first point, 0.1 is very near the first point, 0.5 is half-way in between,
    etc. The lerp function is convenient for creating motion along a straight path
    and for drawing dotted lines.
    """
    return Sketch.lerp(start, stop, amt)


@overload
def mag(a: float, b: float) -> float:
    """Calculates the magnitude (or length) of a vector.

    Methods
    -------

    You can use any of the following signatures:

     * mag(a: float, b: float) -> float
     * mag(a: float, b: float, c: float) -> float

    Parameters
    ----------

    a: float
        first value

    b: float
        second value

    c: float
        third value

    Notes
    -----

    Calculates the magnitude (or length) of a vector. A vector is a direction in
    space commonly used in computer graphics and linear algebra. Because it has no
    "start" position, the magnitude of a vector can be thought of as the distance
    from the coordinate ``(0, 0)`` to its ``(x, y)`` value. Therefore, ``mag()`` is
    a shortcut for writing ``dist(0, 0, x, y)``.
    """
    pass


@overload
def mag(a: float, b: float, c: float) -> float:
    """Calculates the magnitude (or length) of a vector.

    Methods
    -------

    You can use any of the following signatures:

     * mag(a: float, b: float) -> float
     * mag(a: float, b: float, c: float) -> float

    Parameters
    ----------

    a: float
        first value

    b: float
        second value

    c: float
        third value

    Notes
    -----

    Calculates the magnitude (or length) of a vector. A vector is a direction in
    space commonly used in computer graphics and linear algebra. Because it has no
    "start" position, the magnitude of a vector can be thought of as the distance
    from the coordinate ``(0, 0)`` to its ``(x, y)`` value. Therefore, ``mag()`` is
    a shortcut for writing ``dist(0, 0, x, y)``.
    """
    pass


def mag(*args: float) -> float:
    """Calculates the magnitude (or length) of a vector.

    Methods
    -------

    You can use any of the following signatures:

     * mag(a: float, b: float) -> float
     * mag(a: float, b: float, c: float) -> float

    Parameters
    ----------

    a: float
        first value

    b: float
        second value

    c: float
        third value

    Notes
    -----

    Calculates the magnitude (or length) of a vector. A vector is a direction in
    space commonly used in computer graphics and linear algebra. Because it has no
    "start" position, the magnitude of a vector can be thought of as the distance
    from the coordinate ``(0, 0)`` to its ``(x, y)`` value. Therefore, ``mag()`` is
    a shortcut for writing ``dist(0, 0, x, y)``.
    """
    return Sketch.mag(*args)


def norm(value: float, start: float, stop: float) -> float:
    """Normalizes a number from another range into a value between 0 and 1.

    Parameters
    ----------

    start: float
        lower bound of the value's current range

    stop: float
        upper bound of the value's current range

    value: float
        the incoming value to be converted

    Notes
    -----

    Normalizes a number from another range into a value between 0 and 1. Identical
    to ``remap(value, low, high, 0, 1)``.

    Numbers outside of the range are not clamped to 0 and 1, because out-of-range
    values are often intentional and useful. (See the second example.) If that isn't
    what you want, try pairing this function with ``constrain()``.
    """
    return Sketch.norm(value, start, stop)


def sq(value: float) -> float:
    """Squares a number (multiplies a number by itself).

    Parameters
    ----------

    value: float
        number to square

    Notes
    -----

    Squares a number (multiplies a number by itself). The result is always a
    positive number, as multiplying two negative numbers always yields a positive
    result. For example, ``-1 * -1 = 1``.
    """
    return Sketch.sq(value)


def sqrt(value: float) -> Union[float, complex]:
    """Calculates the square root of a number.

    Parameters
    ----------

    value: float
        value to calculate the square root of

    Notes
    -----

    Calculates the square root of a number. The square root of a positive number is
    always positive, even though there may be a valid negative root. The square root
    of a negative number is a complex number. In either case, the square root ``s``
    of number ``a`` is such that ``s*s = a``. It is the opposite of squaring.

    Python supports complex numbers, but such values cannot be passed to py5 drawing
    functions. When using the ``sqrt()`` function, you should check if the result is
    complex before using the value. You can also extract the real and imaginary
    components of the complex value with ``.real`` and ``.imag``. See the second
    example to learn how to do both of these things.
    """
    return Sketch.sqrt(value)


def floor(value: float) -> int:
    """Calculates the closest int value that is less than or equal to the value of the
    parameter.

    Parameters
    ----------

    value: float
        number to round down

    Notes
    -----

    Calculates the closest int value that is less than or equal to the value of the
    parameter.

    This function makes a call to the numpy ``floor()`` function.
    """
    return Sketch.floor(value)


def ceil(value: float) -> int:
    """Calculates the closest int value that is greater than or equal to the value of
    the parameter.

    Parameters
    ----------

    value: float
        number to round up

    Notes
    -----

    Calculates the closest int value that is greater than or equal to the value of
    the parameter.

    This function makes a call to the numpy ``ceil()`` function.
    """
    return Sketch.ceil(value)


def exp(value: float) -> float:
    """Returns Euler's number e (2.71828...) raised to the power of the ``n``
    parameter.

    Parameters
    ----------

    value: float
        exponent to raise

    Notes
    -----

    Returns Euler's number e (2.71828...) raised to the power of the ``n``
    parameter. This function is the compliment to ``log()``.

    This function makes a call to the numpy ``exp()`` function.
    """
    return Sketch.exp(value)


def log(value: float) -> float:
    """Calculates the natural logarithm (the base-e logarithm) of a number.

    Parameters
    ----------

    value: float
        number greater than 0.0

    Notes
    -----

    Calculates the natural logarithm (the base-e logarithm) of a number. This
    function expects the ``n`` parameter to be a value greater than 0.0. This
    function is the compliment to ``exp()``.

    This function makes a call to the numpy ``log()`` function. If the ``n``
    parameter is less than or equal to 0.0, you will see a ``RuntimeWarning`` and
    the returned result will be numpy's Not-a-Number value, ``np.nan``.
    """
    return Sketch.log(value)


def random_seed(seed: int) -> None:
    """Sets the seed value for py5's random functions.

    Parameters
    ----------

    seed: int
        seed value

    Notes
    -----

    Sets the seed value for py5's random functions. This includes ``random()``,
    ``random_int()``, ``random_choice()``, and ``random_gaussian()``. By default,
    all of these functions would produce different results each time a program is
    run. Set the seed parameter to a constant value to return the same pseudo-random
    numbers each time the software is run.
    """
    return _py5sketch.random_seed(seed)


@overload
def random() -> float:
    """Generates random numbers.

    Methods
    -------

    You can use any of the following signatures:

     * random() -> float
     * random(high: float) -> float
     * random(low: float, high: float) -> float

    Parameters
    ----------

    high: float
        upper limit

    low: float
        lower limit

    Notes
    -----

    Generates random numbers. Each time the ``random()`` function is called, it
    returns an unexpected value within the specified range. This function's
    randomness can be influenced by ``random_seed()``.

    If no parameters are passed to the function, it will return a float between zero
    and one.

    If only one parameter is passed to the function, it will return a float between
    zero and the value of the ``high`` parameter. For example, ``random(5)`` returns
    values between 0 and 5 (starting at zero, and up to, but not including, 5).

    If two parameters are specified, the function will return a float with a value
    between the two values. For example, ``random(-5, 10.2)`` returns values
    starting at -5 and up to (but not including) 10.2. To convert a floating-point
    random number to an integer, use the ``int()`` function, or alternatively,
    consider using ``random_int()``.

    This function makes calls to numpy to generate the random values.
    """
    pass


@overload
def random(high: float) -> float:
    """Generates random numbers.

    Methods
    -------

    You can use any of the following signatures:

     * random() -> float
     * random(high: float) -> float
     * random(low: float, high: float) -> float

    Parameters
    ----------

    high: float
        upper limit

    low: float
        lower limit

    Notes
    -----

    Generates random numbers. Each time the ``random()`` function is called, it
    returns an unexpected value within the specified range. This function's
    randomness can be influenced by ``random_seed()``.

    If no parameters are passed to the function, it will return a float between zero
    and one.

    If only one parameter is passed to the function, it will return a float between
    zero and the value of the ``high`` parameter. For example, ``random(5)`` returns
    values between 0 and 5 (starting at zero, and up to, but not including, 5).

    If two parameters are specified, the function will return a float with a value
    between the two values. For example, ``random(-5, 10.2)`` returns values
    starting at -5 and up to (but not including) 10.2. To convert a floating-point
    random number to an integer, use the ``int()`` function, or alternatively,
    consider using ``random_int()``.

    This function makes calls to numpy to generate the random values.
    """
    pass


@overload
def random(low: float, high: float) -> float:
    """Generates random numbers.

    Methods
    -------

    You can use any of the following signatures:

     * random() -> float
     * random(high: float) -> float
     * random(low: float, high: float) -> float

    Parameters
    ----------

    high: float
        upper limit

    low: float
        lower limit

    Notes
    -----

    Generates random numbers. Each time the ``random()`` function is called, it
    returns an unexpected value within the specified range. This function's
    randomness can be influenced by ``random_seed()``.

    If no parameters are passed to the function, it will return a float between zero
    and one.

    If only one parameter is passed to the function, it will return a float between
    zero and the value of the ``high`` parameter. For example, ``random(5)`` returns
    values between 0 and 5 (starting at zero, and up to, but not including, 5).

    If two parameters are specified, the function will return a float with a value
    between the two values. For example, ``random(-5, 10.2)`` returns values
    starting at -5 and up to (but not including) 10.2. To convert a floating-point
    random number to an integer, use the ``int()`` function, or alternatively,
    consider using ``random_int()``.

    This function makes calls to numpy to generate the random values.
    """
    pass


def random(*args: float) -> float:
    """Generates random numbers.

    Methods
    -------

    You can use any of the following signatures:

     * random() -> float
     * random(high: float) -> float
     * random(low: float, high: float) -> float

    Parameters
    ----------

    high: float
        upper limit

    low: float
        lower limit

    Notes
    -----

    Generates random numbers. Each time the ``random()`` function is called, it
    returns an unexpected value within the specified range. This function's
    randomness can be influenced by ``random_seed()``.

    If no parameters are passed to the function, it will return a float between zero
    and one.

    If only one parameter is passed to the function, it will return a float between
    zero and the value of the ``high`` parameter. For example, ``random(5)`` returns
    values between 0 and 5 (starting at zero, and up to, but not including, 5).

    If two parameters are specified, the function will return a float with a value
    between the two values. For example, ``random(-5, 10.2)`` returns values
    starting at -5 and up to (but not including) 10.2. To convert a floating-point
    random number to an integer, use the ``int()`` function, or alternatively,
    consider using ``random_int()``.

    This function makes calls to numpy to generate the random values.
    """
    return _py5sketch.random(*args)


@overload
def random_int() -> int:
    """Generates random integers.

    Methods
    -------

    You can use any of the following signatures:

     * random_int() -> int
     * random_int(high: int) -> int
     * random_int(low: int, high: int) -> int

    Parameters
    ----------

    high: int
        upper limit

    low: int
        lower limit

    Notes
    -----

    Generates random integers. Each time the ``random_int()`` function is called, it
    returns an unexpected integer within the specified range. This function's
    randomness can be influenced by ``random_seed()``.

    If no parameters are passed to the function, it will return either 0 or 1.
    Recall that in a Python boolean expression, 0 evaluates to ``False`` and 1
    evaluates to ``True``. This is equivalent to a coin toss.

    If only one parameter is passed to the function, it will return an integer
    between zero and the value of the ``high`` parameter, inclusive. For example,
    ``random(5)`` returns one of 0, 1, 2, 3, 4, or 5.

    If two parameters are specified, the function will return an integer with a
    value between the two values, inclusive. For example, ``random(2, 5)`` returns
    one of 2, 3, 4, or 5.

    If you want to pick a random object from a list, recall that Python uses zero-
    indexing, so the first index value is 0 and the final index value is one less
    than the list length. Therefore, to pick a random index to use in the list
    ``words``, your code should be ``random_int(len(words)-1)``. Omitting the ``-1``
    will (occasionally) result in an index out of range error. Alternatively, you
    can also use ``random_choice()`` to pick a random object from a list.

    This function makes calls to numpy to generate the random integers.
    """
    pass


@overload
def random_int(high: int) -> int:
    """Generates random integers.

    Methods
    -------

    You can use any of the following signatures:

     * random_int() -> int
     * random_int(high: int) -> int
     * random_int(low: int, high: int) -> int

    Parameters
    ----------

    high: int
        upper limit

    low: int
        lower limit

    Notes
    -----

    Generates random integers. Each time the ``random_int()`` function is called, it
    returns an unexpected integer within the specified range. This function's
    randomness can be influenced by ``random_seed()``.

    If no parameters are passed to the function, it will return either 0 or 1.
    Recall that in a Python boolean expression, 0 evaluates to ``False`` and 1
    evaluates to ``True``. This is equivalent to a coin toss.

    If only one parameter is passed to the function, it will return an integer
    between zero and the value of the ``high`` parameter, inclusive. For example,
    ``random(5)`` returns one of 0, 1, 2, 3, 4, or 5.

    If two parameters are specified, the function will return an integer with a
    value between the two values, inclusive. For example, ``random(2, 5)`` returns
    one of 2, 3, 4, or 5.

    If you want to pick a random object from a list, recall that Python uses zero-
    indexing, so the first index value is 0 and the final index value is one less
    than the list length. Therefore, to pick a random index to use in the list
    ``words``, your code should be ``random_int(len(words)-1)``. Omitting the ``-1``
    will (occasionally) result in an index out of range error. Alternatively, you
    can also use ``random_choice()`` to pick a random object from a list.

    This function makes calls to numpy to generate the random integers.
    """
    pass


@overload
def random_int(low: int, high: int) -> int:
    """Generates random integers.

    Methods
    -------

    You can use any of the following signatures:

     * random_int() -> int
     * random_int(high: int) -> int
     * random_int(low: int, high: int) -> int

    Parameters
    ----------

    high: int
        upper limit

    low: int
        lower limit

    Notes
    -----

    Generates random integers. Each time the ``random_int()`` function is called, it
    returns an unexpected integer within the specified range. This function's
    randomness can be influenced by ``random_seed()``.

    If no parameters are passed to the function, it will return either 0 or 1.
    Recall that in a Python boolean expression, 0 evaluates to ``False`` and 1
    evaluates to ``True``. This is equivalent to a coin toss.

    If only one parameter is passed to the function, it will return an integer
    between zero and the value of the ``high`` parameter, inclusive. For example,
    ``random(5)`` returns one of 0, 1, 2, 3, 4, or 5.

    If two parameters are specified, the function will return an integer with a
    value between the two values, inclusive. For example, ``random(2, 5)`` returns
    one of 2, 3, 4, or 5.

    If you want to pick a random object from a list, recall that Python uses zero-
    indexing, so the first index value is 0 and the final index value is one less
    than the list length. Therefore, to pick a random index to use in the list
    ``words``, your code should be ``random_int(len(words)-1)``. Omitting the ``-1``
    will (occasionally) result in an index out of range error. Alternatively, you
    can also use ``random_choice()`` to pick a random object from a list.

    This function makes calls to numpy to generate the random integers.
    """
    pass


def random_int(*args: int) -> int:
    """Generates random integers.

    Methods
    -------

    You can use any of the following signatures:

     * random_int() -> int
     * random_int(high: int) -> int
     * random_int(low: int, high: int) -> int

    Parameters
    ----------

    high: int
        upper limit

    low: int
        lower limit

    Notes
    -----

    Generates random integers. Each time the ``random_int()`` function is called, it
    returns an unexpected integer within the specified range. This function's
    randomness can be influenced by ``random_seed()``.

    If no parameters are passed to the function, it will return either 0 or 1.
    Recall that in a Python boolean expression, 0 evaluates to ``False`` and 1
    evaluates to ``True``. This is equivalent to a coin toss.

    If only one parameter is passed to the function, it will return an integer
    between zero and the value of the ``high`` parameter, inclusive. For example,
    ``random(5)`` returns one of 0, 1, 2, 3, 4, or 5.

    If two parameters are specified, the function will return an integer with a
    value between the two values, inclusive. For example, ``random(2, 5)`` returns
    one of 2, 3, 4, or 5.

    If you want to pick a random object from a list, recall that Python uses zero-
    indexing, so the first index value is 0 and the final index value is one less
    than the list length. Therefore, to pick a random index to use in the list
    ``words``, your code should be ``random_int(len(words)-1)``. Omitting the ``-1``
    will (occasionally) result in an index out of range error. Alternatively, you
    can also use ``random_choice()`` to pick a random object from a list.

    This function makes calls to numpy to generate the random integers.
    """
    return _py5sketch.random_int(*args)


def random_choice(objects: List[Any]) -> Any:
    """Select a random item from a list.

    Parameters
    ----------

    objects: List[Any]
        list of objects to choose from

    Notes
    -----

    Select a random item from a list. The list items can be of any type. This
    function's randomness can be influenced by ``random_seed()``.

    This function makes calls to numpy to select the random items.
    """
    return _py5sketch.random_choice(objects)


@overload
def random_gaussian() -> float:
    """Generates random gaussian values.

    Methods
    -------

    You can use any of the following signatures:

     * random_gaussian() -> float
     * random_gaussian(loc: float) -> float
     * random_gaussian(loc: float, scale: float) -> float

    Parameters
    ----------

    loc: float
        average of randomly selected numbers

    scale: float
        standard deviation of randomly selected numbers

    Notes
    -----

    Generates random gaussian values. Each time the ``random_gaussian()`` function
    is called, it returns an unexpected float with a probability distribution set by
    the parameters.  This function's randomness can be influenced by
    ``random_seed()``.

    If no parameters are passed to the function, returned values will have an
    average of 0 and a standard deviation of 1. Although there is theoretically no
    minimum or maximum value that this function might return, in practice returned
    values will be within plus or minus one standard deviation of the mean 68% of
    the time and within two standard devations 95% of the time. Values farther and
    farther from the mean become increasingly less likely.

    If only one parameter is passed to the function, that parameter will be used as
    the average instead of 0. If two parameters are called, those values will be
    used as the average and standard deviation.

    This function makes calls to numpy to generate the random values.
    """
    pass


@overload
def random_gaussian(loc: float) -> float:
    """Generates random gaussian values.

    Methods
    -------

    You can use any of the following signatures:

     * random_gaussian() -> float
     * random_gaussian(loc: float) -> float
     * random_gaussian(loc: float, scale: float) -> float

    Parameters
    ----------

    loc: float
        average of randomly selected numbers

    scale: float
        standard deviation of randomly selected numbers

    Notes
    -----

    Generates random gaussian values. Each time the ``random_gaussian()`` function
    is called, it returns an unexpected float with a probability distribution set by
    the parameters.  This function's randomness can be influenced by
    ``random_seed()``.

    If no parameters are passed to the function, returned values will have an
    average of 0 and a standard deviation of 1. Although there is theoretically no
    minimum or maximum value that this function might return, in practice returned
    values will be within plus or minus one standard deviation of the mean 68% of
    the time and within two standard devations 95% of the time. Values farther and
    farther from the mean become increasingly less likely.

    If only one parameter is passed to the function, that parameter will be used as
    the average instead of 0. If two parameters are called, those values will be
    used as the average and standard deviation.

    This function makes calls to numpy to generate the random values.
    """
    pass


@overload
def random_gaussian(loc: float, scale: float) -> float:
    """Generates random gaussian values.

    Methods
    -------

    You can use any of the following signatures:

     * random_gaussian() -> float
     * random_gaussian(loc: float) -> float
     * random_gaussian(loc: float, scale: float) -> float

    Parameters
    ----------

    loc: float
        average of randomly selected numbers

    scale: float
        standard deviation of randomly selected numbers

    Notes
    -----

    Generates random gaussian values. Each time the ``random_gaussian()`` function
    is called, it returns an unexpected float with a probability distribution set by
    the parameters.  This function's randomness can be influenced by
    ``random_seed()``.

    If no parameters are passed to the function, returned values will have an
    average of 0 and a standard deviation of 1. Although there is theoretically no
    minimum or maximum value that this function might return, in practice returned
    values will be within plus or minus one standard deviation of the mean 68% of
    the time and within two standard devations 95% of the time. Values farther and
    farther from the mean become increasingly less likely.

    If only one parameter is passed to the function, that parameter will be used as
    the average instead of 0. If two parameters are called, those values will be
    used as the average and standard deviation.

    This function makes calls to numpy to generate the random values.
    """
    pass


def random_gaussian(*args: float) -> float:
    """Generates random gaussian values.

    Methods
    -------

    You can use any of the following signatures:

     * random_gaussian() -> float
     * random_gaussian(loc: float) -> float
     * random_gaussian(loc: float, scale: float) -> float

    Parameters
    ----------

    loc: float
        average of randomly selected numbers

    scale: float
        standard deviation of randomly selected numbers

    Notes
    -----

    Generates random gaussian values. Each time the ``random_gaussian()`` function
    is called, it returns an unexpected float with a probability distribution set by
    the parameters.  This function's randomness can be influenced by
    ``random_seed()``.

    If no parameters are passed to the function, returned values will have an
    average of 0 and a standard deviation of 1. Although there is theoretically no
    minimum or maximum value that this function might return, in practice returned
    values will be within plus or minus one standard deviation of the mean 68% of
    the time and within two standard devations 95% of the time. Values farther and
    farther from the mean become increasingly less likely.

    If only one parameter is passed to the function, that parameter will be used as
    the average instead of 0. If two parameters are called, those values will be
    used as the average and standard deviation.

    This function makes calls to numpy to generate the random values.
    """
    return _py5sketch.random_gaussian(*args)


@overload
def noise(x: float, **kwargs) -> float:
    """Generate pseudo-random noise values for specific coodinates.

    Methods
    -------

    You can use any of the following signatures:

     * noise(x: float, **kwargs) -> float
     * noise(x: float, y: float, **kwargs) -> float
     * noise(x: float, y: float, z: float, **kwargs) -> float
     * noise(x: float, y: float, z: float, w: float, **kwargs) -> float

    Parameters
    ----------

    kwargs
        keyword arguments to override existing noise detail or noise seed settings

    w: float
        w-coordinate in noise space

    x: float
        x-coordinate in noise space

    y: float
        y-coordinate in noise space

    z: float
        z-coordinate in noise space

    Notes
    -----

    Generate pseudo-random noise values for specific coodinates. Noise functions are
    random sequence generators that produce a more natural, harmonic succession of
    numbers compared to the ``random()`` function. Several well-known noise
    algorithms were developed by Ken Perlin and have been used in graphical
    applications to generate procedural textures, shapes, terrains, and other
    seemingly organic forms.

    In contrast to the ``random()`` function, noise is defined in an n-dimensional
    space, in which each coordinate corresponds to a fixed pseudo-random value
    (fixed only for the lifespan of the program). Py5 can generate Perlin Noise and
    Simplex Noise. By default, py5 will generate noise using the Simplex Noise
    algorithm. The noise value can be animated by moving through the noise space, as
    demonstrated in the examples. Any dimension can also be interpreted as time. An
    easy way to animate the noise value is to pass the ``noise()`` function the
    ``frame_count`` divided by a scaling factor, as is done in a few of the
    examples.

    The generated noise values for both Perlin Noise and Simplex Noise will be
    between -1 and 1. This contrasts with Processing's noise function, which
    typically returns values between 0 and 1.

    Perlin Noise can be generated in 1, 2, or 3 dimensions and Simplex Noise can be
    generated in 1, 2, 3, or 4 dimensions. Technically Simplex Noise cannot be
    generated in only 1 dimension, but as a convenience, py5 will add a second
    dimension for you (with a value of 0) if only one dimension is used.

    The actual noise structure is similar to that of an audio signal, in respect to
    the function's use of frequencies. Similar to the concept of harmonics in
    physics, both noise algorithms are computed over several octaves which are added
    together for the final result.

    The nature of the noise values returned can be adjusted with ``noise_mode()``,
    ``noise_seed()``, and ``noise_detail()``.

    Another way to adjust the character of the resulting sequence is the scale of
    the input coordinates. As the function works within an infinite space, the value
    of the coordinates doesn't matter as such; only the distance between successive
    coordinates is important (such as when using ``noise()`` within a loop). As a
    general rule, the smaller the difference between coordinates, the smoother the
    resulting noise sequence. Steps of 0.005-0.03 work best for most applications,
    but this will differ depending on the use case and the noise settings.

    Py5's noise functionality is provided by the Python noise library. The noise
    library provides more advanced features than what is documented here. To use the
    more advanced features, import that library directly.

    Py5's ``noise()`` function can also accept numpy arrays as parameters. It will
    automatically vectorize the operations and use broadcasting when needed.
    """
    pass


@overload
def noise(x: float, y: float, **kwargs) -> float:
    """Generate pseudo-random noise values for specific coodinates.

    Methods
    -------

    You can use any of the following signatures:

     * noise(x: float, **kwargs) -> float
     * noise(x: float, y: float, **kwargs) -> float
     * noise(x: float, y: float, z: float, **kwargs) -> float
     * noise(x: float, y: float, z: float, w: float, **kwargs) -> float

    Parameters
    ----------

    kwargs
        keyword arguments to override existing noise detail or noise seed settings

    w: float
        w-coordinate in noise space

    x: float
        x-coordinate in noise space

    y: float
        y-coordinate in noise space

    z: float
        z-coordinate in noise space

    Notes
    -----

    Generate pseudo-random noise values for specific coodinates. Noise functions are
    random sequence generators that produce a more natural, harmonic succession of
    numbers compared to the ``random()`` function. Several well-known noise
    algorithms were developed by Ken Perlin and have been used in graphical
    applications to generate procedural textures, shapes, terrains, and other
    seemingly organic forms.

    In contrast to the ``random()`` function, noise is defined in an n-dimensional
    space, in which each coordinate corresponds to a fixed pseudo-random value
    (fixed only for the lifespan of the program). Py5 can generate Perlin Noise and
    Simplex Noise. By default, py5 will generate noise using the Simplex Noise
    algorithm. The noise value can be animated by moving through the noise space, as
    demonstrated in the examples. Any dimension can also be interpreted as time. An
    easy way to animate the noise value is to pass the ``noise()`` function the
    ``frame_count`` divided by a scaling factor, as is done in a few of the
    examples.

    The generated noise values for both Perlin Noise and Simplex Noise will be
    between -1 and 1. This contrasts with Processing's noise function, which
    typically returns values between 0 and 1.

    Perlin Noise can be generated in 1, 2, or 3 dimensions and Simplex Noise can be
    generated in 1, 2, 3, or 4 dimensions. Technically Simplex Noise cannot be
    generated in only 1 dimension, but as a convenience, py5 will add a second
    dimension for you (with a value of 0) if only one dimension is used.

    The actual noise structure is similar to that of an audio signal, in respect to
    the function's use of frequencies. Similar to the concept of harmonics in
    physics, both noise algorithms are computed over several octaves which are added
    together for the final result.

    The nature of the noise values returned can be adjusted with ``noise_mode()``,
    ``noise_seed()``, and ``noise_detail()``.

    Another way to adjust the character of the resulting sequence is the scale of
    the input coordinates. As the function works within an infinite space, the value
    of the coordinates doesn't matter as such; only the distance between successive
    coordinates is important (such as when using ``noise()`` within a loop). As a
    general rule, the smaller the difference between coordinates, the smoother the
    resulting noise sequence. Steps of 0.005-0.03 work best for most applications,
    but this will differ depending on the use case and the noise settings.

    Py5's noise functionality is provided by the Python noise library. The noise
    library provides more advanced features than what is documented here. To use the
    more advanced features, import that library directly.

    Py5's ``noise()`` function can also accept numpy arrays as parameters. It will
    automatically vectorize the operations and use broadcasting when needed.
    """
    pass


@overload
def noise(x: float, y: float, z: float, **kwargs) -> float:
    """Generate pseudo-random noise values for specific coodinates.

    Methods
    -------

    You can use any of the following signatures:

     * noise(x: float, **kwargs) -> float
     * noise(x: float, y: float, **kwargs) -> float
     * noise(x: float, y: float, z: float, **kwargs) -> float
     * noise(x: float, y: float, z: float, w: float, **kwargs) -> float

    Parameters
    ----------

    kwargs
        keyword arguments to override existing noise detail or noise seed settings

    w: float
        w-coordinate in noise space

    x: float
        x-coordinate in noise space

    y: float
        y-coordinate in noise space

    z: float
        z-coordinate in noise space

    Notes
    -----

    Generate pseudo-random noise values for specific coodinates. Noise functions are
    random sequence generators that produce a more natural, harmonic succession of
    numbers compared to the ``random()`` function. Several well-known noise
    algorithms were developed by Ken Perlin and have been used in graphical
    applications to generate procedural textures, shapes, terrains, and other
    seemingly organic forms.

    In contrast to the ``random()`` function, noise is defined in an n-dimensional
    space, in which each coordinate corresponds to a fixed pseudo-random value
    (fixed only for the lifespan of the program). Py5 can generate Perlin Noise and
    Simplex Noise. By default, py5 will generate noise using the Simplex Noise
    algorithm. The noise value can be animated by moving through the noise space, as
    demonstrated in the examples. Any dimension can also be interpreted as time. An
    easy way to animate the noise value is to pass the ``noise()`` function the
    ``frame_count`` divided by a scaling factor, as is done in a few of the
    examples.

    The generated noise values for both Perlin Noise and Simplex Noise will be
    between -1 and 1. This contrasts with Processing's noise function, which
    typically returns values between 0 and 1.

    Perlin Noise can be generated in 1, 2, or 3 dimensions and Simplex Noise can be
    generated in 1, 2, 3, or 4 dimensions. Technically Simplex Noise cannot be
    generated in only 1 dimension, but as a convenience, py5 will add a second
    dimension for you (with a value of 0) if only one dimension is used.

    The actual noise structure is similar to that of an audio signal, in respect to
    the function's use of frequencies. Similar to the concept of harmonics in
    physics, both noise algorithms are computed over several octaves which are added
    together for the final result.

    The nature of the noise values returned can be adjusted with ``noise_mode()``,
    ``noise_seed()``, and ``noise_detail()``.

    Another way to adjust the character of the resulting sequence is the scale of
    the input coordinates. As the function works within an infinite space, the value
    of the coordinates doesn't matter as such; only the distance between successive
    coordinates is important (such as when using ``noise()`` within a loop). As a
    general rule, the smaller the difference between coordinates, the smoother the
    resulting noise sequence. Steps of 0.005-0.03 work best for most applications,
    but this will differ depending on the use case and the noise settings.

    Py5's noise functionality is provided by the Python noise library. The noise
    library provides more advanced features than what is documented here. To use the
    more advanced features, import that library directly.

    Py5's ``noise()`` function can also accept numpy arrays as parameters. It will
    automatically vectorize the operations and use broadcasting when needed.
    """
    pass


@overload
def noise(x: float, y: float, z: float, w: float, **kwargs) -> float:
    """Generate pseudo-random noise values for specific coodinates.

    Methods
    -------

    You can use any of the following signatures:

     * noise(x: float, **kwargs) -> float
     * noise(x: float, y: float, **kwargs) -> float
     * noise(x: float, y: float, z: float, **kwargs) -> float
     * noise(x: float, y: float, z: float, w: float, **kwargs) -> float

    Parameters
    ----------

    kwargs
        keyword arguments to override existing noise detail or noise seed settings

    w: float
        w-coordinate in noise space

    x: float
        x-coordinate in noise space

    y: float
        y-coordinate in noise space

    z: float
        z-coordinate in noise space

    Notes
    -----

    Generate pseudo-random noise values for specific coodinates. Noise functions are
    random sequence generators that produce a more natural, harmonic succession of
    numbers compared to the ``random()`` function. Several well-known noise
    algorithms were developed by Ken Perlin and have been used in graphical
    applications to generate procedural textures, shapes, terrains, and other
    seemingly organic forms.

    In contrast to the ``random()`` function, noise is defined in an n-dimensional
    space, in which each coordinate corresponds to a fixed pseudo-random value
    (fixed only for the lifespan of the program). Py5 can generate Perlin Noise and
    Simplex Noise. By default, py5 will generate noise using the Simplex Noise
    algorithm. The noise value can be animated by moving through the noise space, as
    demonstrated in the examples. Any dimension can also be interpreted as time. An
    easy way to animate the noise value is to pass the ``noise()`` function the
    ``frame_count`` divided by a scaling factor, as is done in a few of the
    examples.

    The generated noise values for both Perlin Noise and Simplex Noise will be
    between -1 and 1. This contrasts with Processing's noise function, which
    typically returns values between 0 and 1.

    Perlin Noise can be generated in 1, 2, or 3 dimensions and Simplex Noise can be
    generated in 1, 2, 3, or 4 dimensions. Technically Simplex Noise cannot be
    generated in only 1 dimension, but as a convenience, py5 will add a second
    dimension for you (with a value of 0) if only one dimension is used.

    The actual noise structure is similar to that of an audio signal, in respect to
    the function's use of frequencies. Similar to the concept of harmonics in
    physics, both noise algorithms are computed over several octaves which are added
    together for the final result.

    The nature of the noise values returned can be adjusted with ``noise_mode()``,
    ``noise_seed()``, and ``noise_detail()``.

    Another way to adjust the character of the resulting sequence is the scale of
    the input coordinates. As the function works within an infinite space, the value
    of the coordinates doesn't matter as such; only the distance between successive
    coordinates is important (such as when using ``noise()`` within a loop). As a
    general rule, the smaller the difference between coordinates, the smoother the
    resulting noise sequence. Steps of 0.005-0.03 work best for most applications,
    but this will differ depending on the use case and the noise settings.

    Py5's noise functionality is provided by the Python noise library. The noise
    library provides more advanced features than what is documented here. To use the
    more advanced features, import that library directly.

    Py5's ``noise()`` function can also accept numpy arrays as parameters. It will
    automatically vectorize the operations and use broadcasting when needed.
    """
    pass


def noise(*args, **kwargs) -> float:
    """Generate pseudo-random noise values for specific coodinates.

    Methods
    -------

    You can use any of the following signatures:

     * noise(x: float, **kwargs) -> float
     * noise(x: float, y: float, **kwargs) -> float
     * noise(x: float, y: float, z: float, **kwargs) -> float
     * noise(x: float, y: float, z: float, w: float, **kwargs) -> float

    Parameters
    ----------

    kwargs
        keyword arguments to override existing noise detail or noise seed settings

    w: float
        w-coordinate in noise space

    x: float
        x-coordinate in noise space

    y: float
        y-coordinate in noise space

    z: float
        z-coordinate in noise space

    Notes
    -----

    Generate pseudo-random noise values for specific coodinates. Noise functions are
    random sequence generators that produce a more natural, harmonic succession of
    numbers compared to the ``random()`` function. Several well-known noise
    algorithms were developed by Ken Perlin and have been used in graphical
    applications to generate procedural textures, shapes, terrains, and other
    seemingly organic forms.

    In contrast to the ``random()`` function, noise is defined in an n-dimensional
    space, in which each coordinate corresponds to a fixed pseudo-random value
    (fixed only for the lifespan of the program). Py5 can generate Perlin Noise and
    Simplex Noise. By default, py5 will generate noise using the Simplex Noise
    algorithm. The noise value can be animated by moving through the noise space, as
    demonstrated in the examples. Any dimension can also be interpreted as time. An
    easy way to animate the noise value is to pass the ``noise()`` function the
    ``frame_count`` divided by a scaling factor, as is done in a few of the
    examples.

    The generated noise values for both Perlin Noise and Simplex Noise will be
    between -1 and 1. This contrasts with Processing's noise function, which
    typically returns values between 0 and 1.

    Perlin Noise can be generated in 1, 2, or 3 dimensions and Simplex Noise can be
    generated in 1, 2, 3, or 4 dimensions. Technically Simplex Noise cannot be
    generated in only 1 dimension, but as a convenience, py5 will add a second
    dimension for you (with a value of 0) if only one dimension is used.

    The actual noise structure is similar to that of an audio signal, in respect to
    the function's use of frequencies. Similar to the concept of harmonics in
    physics, both noise algorithms are computed over several octaves which are added
    together for the final result.

    The nature of the noise values returned can be adjusted with ``noise_mode()``,
    ``noise_seed()``, and ``noise_detail()``.

    Another way to adjust the character of the resulting sequence is the scale of
    the input coordinates. As the function works within an infinite space, the value
    of the coordinates doesn't matter as such; only the distance between successive
    coordinates is important (such as when using ``noise()`` within a loop). As a
    general rule, the smaller the difference between coordinates, the smoother the
    resulting noise sequence. Steps of 0.005-0.03 work best for most applications,
    but this will differ depending on the use case and the noise settings.

    Py5's noise functionality is provided by the Python noise library. The noise
    library provides more advanced features than what is documented here. To use the
    more advanced features, import that library directly.

    Py5's ``noise()`` function can also accept numpy arrays as parameters. It will
    automatically vectorize the operations and use broadcasting when needed.
    """
    return _py5sketch.noise(*args, **kwargs)


def noise_mode(mode: int) -> None:
    """Sets the kind of noise that the ``noise()`` function will generate.

    Parameters
    ----------

    mode: int
        kind of noise to generate, either PERLIN_NOISE or SIMPLEX_NOISE

    Notes
    -----

    Sets the kind of noise that the ``noise()`` function will generate. This can be
    either Perlin Noise or Simplex Noise. By default, py5 will generate noise using
    the Simplex Noise algorithm.

    Perlin Noise can be generated in 1, 2, or 3 dimensions and Simplex Noise can be
    generated in 1, 2, 3, or 4 dimensions. Technically Simplex Noise cannot be
    generated in only 1 dimension, but as a convenience, py5 will add a second
    dimension for you (with a value of 0) if only one dimension is used.

    The specific Perlin Noise implementation provided by py5 is the "Improved Perlin
    Noise" algorithm as described in Ken Perlin's 2002 SIGGRAPH paper. This uses the
    fifth degree polynomial ``f(t)=6t^5-15t^4+10t^3`` as the blending function. This
    is different from the "Classic Perlin Noise" algorithm, described in Ken
    Perlin's 1985 SIGGRAPH paper, which uses the third degree polynomial
    ``f(t)=3t^2-2t^3`` instead. The Simplex Noise algorithm, also developed by Ken
    Perlin, is different from Perlin Noise, and uses a completely different approach
    for generating noise values. Processing's noise algorithm is a valid and useful
    noise algorithm but is not identical to any of the algorithms mentioned here, so
    py5's noise values will not match Processing's no matter what inputs or settings
    are used.

    Py5's noise functionality is provided by the Python noise library. The noise
    library provides more advanced features than what is documented here. To use the
    more advanced features, import that library directly.
    """
    return _py5sketch.noise_mode(mode)


def noise_detail(octaves: float = None, persistence: float = None,
                 lacunarity: float = None) -> None:
    """Adjusts the character and level of detail produced by the ``noise()`` function.

    Parameters
    ----------

    lacunarity: float = None
        change in noise frequency from one octave to the next

    octaves: float = None
        number of noise octaves

    persistence: float = None
        change in noise amplitude from one octave to the next

    Notes
    -----

    Adjusts the character and level of detail produced by the ``noise()`` function.
    Similar to harmonics in physics, noise is computed over several octaves. Lower
    octaves contribute more to the output signal and as such define the overall
    intensity of the noise, whereas higher octaves create finer-grained details in
    the noise sequence.

    By default, noise is computed over 4 octaves. Each octave has half the amplitude
    and twice the frequency of its predecessor. The decrease in amplitude can be
    adjusted with the ``persistence`` parameter. The increase in frequency can be
    adjusted with the ``lacunarity`` parameter.

    For example, a ``persistence`` parameter of 0.75 means each octave will now have
    75% impact (25% less) of the previous lower octave. A ``lacunarity`` parameter
    of 4 means that each octave will have 4 times the frequency of the previous
    lower octave, providing noise at a finer-grained scale than what the default
    value of 2 would provide.

    By changing these parameters, the signal created by the ``noise()`` function can
    be adapted to fit very specific needs and characteristics.

    Py5's noise functionality is provided by the Python noise library. The noise
    library provides more advanced features than what is documented here. To use the
    more advanced features, import that library directly.
    """
    return _py5sketch.noise_detail(
        octaves=octaves,
        persistence=persistence,
        lacunarity=lacunarity)


def noise_seed(seed: int) -> None:
    """Sets the seed value for ``noise()``.

    Parameters
    ----------

    seed: int
        seed value

    Notes
    -----

    Sets the seed value for ``noise()``. By default, ``noise()`` produces different
    results each time the program is run. Set the seed parameter to a constant to
    return the same pseudo-random numbers each time the Sketch is run.

    Py5's noise functionality is provided by the Python noise library. The noise
    library provides more advanced features than what is documented here. To use the
    more advanced features, import that library directly.
    """
    return _py5sketch.noise_seed(seed)

##############################################################################
# module functions from data.py
##############################################################################


def load_json(json_path: Union[str, Path], **kwargs: Dict[str, Any]) -> Any:
    """Load a JSON data file from a file or URL.

    Parameters
    ----------

    json_path: Union[str, Path]
        url or file path for JSON data file

    kwargs: Dict[str, Any]
        keyword arguments

    Notes
    -----

    Load a JSON data file from a file or URL. When loading a file, the path can be
    in the data directory, relative to the current working directory
    (``sketch_path()``), or an absolute path. When loading from a URL, the
    ``json_path`` parameter must start with ``http://`` or ``https://``.

    When loading JSON data from a URL, the data is retrieved using the Python
    requests library with the ``get`` method, and the ``kwargs`` parameter is passed
    along to that method. When loading JSON data from a file, the data is loaded
    using the Python json library with the ``load`` method, and again the ``kwargs``
    parameter passed along to that method.
    """
    return _py5sketch.load_json(json_path, **kwargs)


def save_json(json_data: Any,
              filename: Union[str,
                              Path],
              **kwargs: Dict[str,
                             Any]) -> None:
    """Save JSON data to a file.

    Parameters
    ----------

    filename: Union[str, Path]
        filename to save JSON data object to

    json_data: Any
        json data object

    kwargs: Dict[str, Any]
        keyword arguments

    Notes
    -----

    Save JSON data to a file. If ``filename`` is not an absolute path, it will be
    saved relative to the current working directory (``sketch_path()``).

    The JSON data is saved using the Python json library with the ``dump`` method,
    and the ``kwargs`` parameter is passed along to that method.
    """
    return _py5sketch.save_json(json_data, filename, **kwargs)


def parse_json(serialized_json: Any, **kwargs: Dict[str, Any]) -> Any:
    """Parse serialized JSON data from a string.

    Parameters
    ----------

    kwargs: Dict[str, Any]
        keyword arguments

    serialized_json: Any
        JSON data object that has been serialized as a string

    Notes
    -----

    Parse serialized JSON data from a string. When reading JSON data from a file,
    ``load_json()`` is the better choice.

    The JSON data is parsed using the Python json library with the ``loads`` method,
    and the ``kwargs`` parameter is passed along to that method.
    """
    return Sketch.parse_json(serialized_json, **kwargs)

##############################################################################
# module functions from threads.py
##############################################################################


def launch_thread(
        f: Callable,
        name: str = None,
        *,
        daemon: bool = True,
        args: Tuple = None,
        kwargs: Dict = None) -> str:
    """Launch a new thread to execute a function in parallel with your Sketch code.

    Parameters
    ----------

    args: Tuple = None
        positional arguments to pass to the given function

    daemon: bool = True
        if the thread should be a daemon thread

    f: Callable
        function to call in the launched thread

    kwargs: Dict = None
        keyword arguments to pass to the given function

    name: str = None
        name of thread to be created

    Notes
    -----

    Launch a new thread to execute a function in parallel with your Sketch code.
    This can be useful for executing non-py5 code that would otherwise slow down the
    animation thread and reduce the Sketch's frame rate.

    The ``name`` parameter is optional but useful if you want to monitor the thread
    with other methods such as ``has_thread()``. If the provided ``name`` is
    identical to an already running thread, the running thread will first be stopped
    with a call to ``stop_thread()`` with the ``wait`` parameter equal to ``True``.

    Use the ``args`` and ``kwargs`` parameters to pass positional and keyword
    arguments to the function.

    Use the ``daemon`` parameter to make the launched thread a daemon that will run
    without blocking Python from exiting. This parameter defaults to ``True``,
    meaning that function execution can be interupted if the Python process exits.
    Note that if the Python process continues running after the Sketch exits, which
    is typically the case when using a Jupyter Notebook, this parameter won't have
    any effect unless if you try to restart the Notebook kernel. Generally speaking,
    setting this parameter to ``False`` causes problems but it is available for
    those who really need it. See ``stop_all_threads()`` for a better approach to
    exit threads.

    The new thread is a Python thread, so all the usual caveats about the Global
    Interpreter Lock (GIL) apply here.
    """
    return _py5sketch.launch_thread(
        f, name=name, daemon=daemon, args=args, kwargs=kwargs)


def launch_promise_thread(
        f: Callable,
        name: str = None,
        *,
        daemon: bool = True,
        args: Tuple = None,
        kwargs: Dict = None) -> Py5Promise:
    """Create a ``Py5Promise`` object that will store the returned result of a function
    when that function completes.

    Parameters
    ----------

    args: Tuple = None
        positional arguments to pass to the given function

    daemon: bool = True
        if the thread should be a daemon thread

    f: Callable
        function to call in the launched thread

    kwargs: Dict = None
        keyword arguments to pass to the given function

    name: str = None
        name of thread to be created

    Notes
    -----

    Create a ``Py5Promise`` object that will store the returned result of a function
    when that function completes. This can be useful for executing non-py5 code that
    would otherwise slow down the animation thread and reduce the Sketch's frame
    rate.

    The ``Py5Promise`` object has an ``is_ready`` property that will be ``True``
    when the ``result`` property contains the value function ``f`` returned. Before
    then, the ``result`` property will be ``None``.

    The ``name`` parameter is optional but useful if you want to monitor the thread
    with other methods such as ``has_thread()``. If the provided ``name`` is
    identical to an already running thread, the running thread will first be stopped
    with a call to ``stop_thread()`` with the ``wait`` parameter equal to ``True``.

    Use the ``args`` and ``kwargs`` parameters to pass positional and keyword
    arguments to the function.

    Use the ``daemon`` parameter to make the launched thread a daemon that will run
    without blocking Python from exiting. This parameter defaults to ``True``,
    meaning that function execution can be interupted if the Python process exits.
    Note that if the Python process continues running after the Sketch exits, which
    is typically the case when using a Jupyter Notebook, this parameter won't have
    any effect unless if you try to restart the Notebook kernel. Generally speaking,
    setting this parameter to ``False`` causes problems but it is available for
    those who really need it. See ``stop_all_threads()`` for a better approach to
    exit threads.

    The new thread is a Python thread, so all the usual caveats about the Global
    Interpreter Lock (GIL) apply here.
    """
    return _py5sketch.launch_promise_thread(
        f, name=name, daemon=daemon, args=args, kwargs=kwargs)


def launch_repeating_thread(f: Callable, name: str = None, *,
                            time_delay: float = 0, daemon: bool = True,
                            args: Tuple = None, kwargs: Dict = None) -> str:
    """Launch a new thread that will repeatedly execute a function in parallel with
    your Sketch code.

    Parameters
    ----------

    args: Tuple = None
        positional arguments to pass to the given function

    daemon: bool = True
        if the thread should be a daemon thread

    f: Callable
        function to call in the launched thread

    kwargs: Dict = None
        keyword arguments to pass to the given function

    name: str = None
        name of thread to be created

    time_delay: float = 0
        time delay in seconds between calls to the given function

    Notes
    -----

    Launch a new thread that will repeatedly execute a function in parallel with
    your Sketch code. This can be useful for executing non-py5 code that would
    otherwise slow down the animation thread and reduce the Sketch's frame rate.

    Use the ``time_delay`` parameter to set the time in seconds between one call to
    function ``f`` and the next call. Set this parameter to ``0`` if you want each
    call to happen immediately after the previous call finishes. If the function
    ``f`` takes longer than expected to finish, py5 will wait for it to finish
    before making the next call. There will not be overlapping calls to function
    ``f``.

    The ``name`` parameter is optional but useful if you want to monitor the thread
    with other methods such as ``has_thread()``. If the provided ``name`` is
    identical to an already running thread, the running thread will first be stopped
    with a call to ``stop_thread()`` with the ``wait`` parameter equal to ``True``.

    Use the ``args`` and ``kwargs`` parameters to pass positional and keyword
    arguments to the function.

    Use the ``daemon`` parameter to make the launched thread a daemon that will run
    without blocking Python from exiting. This parameter defaults to ``True``,
    meaning that function execution can be interupted if the Python process exits.
    Note that if the Python process continues running after the Sketch exits, which
    is typically the case when using a Jupyter Notebook, this parameter won't have
    any effect unless if you try to restart the Notebook kernel. Generally speaking,
    setting this parameter to ``False`` causes problems but it is available for
    those who really need it. See ``stop_all_threads()`` for a better approach to
    exit threads.

    The new thread is a Python thread, so all the usual caveats about the Global
    Interpreter Lock (GIL) apply here.
    """
    return _py5sketch.launch_repeating_thread(
        f,
        name=name,
        time_delay=time_delay,
        daemon=daemon,
        args=args,
        kwargs=kwargs)


def has_thread(name: str) -> None:
    """Determine if a thread of a given name exists and is currently running.

    Parameters
    ----------

    name: str
        name of thread

    Notes
    -----

    Determine if a thread of a given name exists and is currently running. You can
    get the list of all currently running threads with ``list_threads()``.
    """
    return _py5sketch.has_thread(name)


def stop_thread(name: str, wait: bool = False) -> None:
    """Stop a thread of a given name.

    Parameters
    ----------

    name: str
        name of thread

    wait: bool = False
        wait for thread to exit before returning

    Notes
    -----

    Stop a thread of a given name. The ``wait`` parameter determines if the method
    call will return right away or wait for the thread to exit.

    This won't do anything useful if the thread was launched with either
    ``launch_thread()`` or ``launch_promise_thread()`` and the ``wait`` parameter is
    ``False``. Non-repeating threads are executed once and will stop when they
    complete execution. Setting the ``wait`` parameter to ``True`` will merely block
    until the thread exits on its own. Killing off a running thread in Python is
    complicated and py5 cannot do that for you. If you want a thread to perform some
    action repeatedly and be interuptable, use ``launch_repeating_thread()``
    instead.

    Use ``has_thread()`` to determine if a thread of a given name exists and
    ``list_threads()`` to get a list of all thread names. Use ``stop_all_threads()``
    to stop all threads.
    """
    return _py5sketch.stop_thread(name, wait=wait)


def stop_all_threads(wait: bool = False) -> None:
    """Stop all running threads.

    Parameters
    ----------

    wait: bool = False
        wait for thread to exit before returning

    Notes
    -----

    Stop all running threads. The ``wait`` parameter determines if the method call
    will return right away or wait for the threads to exit.

    When the Sketch shuts down, ``stop_all_threads(wait=False)`` is called for you.
    If you would rather the Sketch waited for threads to exit, create an ``exiting``
    method and make a call to ``stop_all_threads(wait=True)``.
    """
    return _py5sketch.stop_all_threads(wait=wait)


def list_threads() -> None:
    """List the names of all of the currently running threads.

    Notes
    -----

    List the names of all of the currently running threads. The names of previously
    launched threads that have exited will be removed from the list.
    """
    return _py5sketch.list_threads()

##############################################################################
# module functions from print_tools.py
##############################################################################


def set_println_stream(println_stream: Any) -> None:
    """Customize where the output of ``println()`` goes.

    Parameters
    ----------

    println_stream: Any
        println stream object to be used by println method

    Notes
    -----

    Customize where the output of ``println()`` goes.

    When running a Sketch asynchronously through Jupyter Notebook, any ``print``
    statements using Python's builtin function will always appear in the output of
    the currently active cell. This will rarely be desirable, as the active cell
    will keep changing as the user executes code elsewhere in the notebook. The
    ``println()`` method was created to provide users with print functionality in a
    Sketch without having to cope with output moving from one cell to the next. Use
    ``set_println_stream`` to change how the output is handled. The
    ``println_stream`` object must provide ``init()`` and ``print()`` methods, as
    shown in the example. The example demonstrates how to configure py5 to output
    text to an IPython Widget.
    """
    return _py5sketch.set_println_stream(println_stream)


def println(
    *args,
    sep: str = ' ',
    end: str = '\n',
        stderr: bool = False) -> None:
    """Print text or other values to the screen.

    Parameters
    ----------

    args
        values to be printed

    end: str = '\\n'
        string appended after the last value, defaults to newline character

    sep: str = ' '
        string inserted between values, defaults to a space

    stderr: bool = False
        use stderr instead of stdout

    Notes
    -----

    Print text or other values to the screen. For a Sketch running outside of a
    Jupyter Notebook, this method will behave the same as the Python's builtin
    ``print`` method. For Sketches running in a Jupyter Notebook, this will place
    text in the output of the cell that made the ``run_sketch()`` call.

    When running a Sketch asynchronously through Jupyter Notebook, any ``print``
    statements using Python's builtin function will always appear in the output of
    the currently active cell. This will rarely be desirable, as the active cell
    will keep changing as the user executes code elsewhere in the notebook. This
    method was created to provide users with print functionality in a Sketch without
    having to cope with output moving from one cell to the next.

    Use ``set_println_stream()`` to customize the behavior of ``println()``.
    """
    return _py5sketch.println(*args, sep=sep, end=end, stderr=stderr)

##############################################################################
# module functions from sketch.py
##############################################################################


@overload
def sketch_path() -> Path:
    """The Sketch's current path.

    Underlying Java method: PApplet.sketchPath

    Methods
    -------

    You can use any of the following signatures:

     * sketch_path() -> Path
     * sketch_path(where: str, /) -> Path

    Parameters
    ----------

    where: str
        subdirectories relative to the sketch path

    Notes
    -----

    The Sketch's current path. If the ``where`` parameter is used, the result will
    be a subdirectory of the current path.

    Result will be relative to Python's current working directory (``os.getcwd()``)
    unless it was specifically set to something else with the ``run_sketch()`` call
    by including a ``--sketch-path`` argument in the ``py5_options`` parameters.
    """
    pass


@overload
def sketch_path(where: str, /) -> Path:
    """The Sketch's current path.

    Underlying Java method: PApplet.sketchPath

    Methods
    -------

    You can use any of the following signatures:

     * sketch_path() -> Path
     * sketch_path(where: str, /) -> Path

    Parameters
    ----------

    where: str
        subdirectories relative to the sketch path

    Notes
    -----

    The Sketch's current path. If the ``where`` parameter is used, the result will
    be a subdirectory of the current path.

    Result will be relative to Python's current working directory (``os.getcwd()``)
    unless it was specifically set to something else with the ``run_sketch()`` call
    by including a ``--sketch-path`` argument in the ``py5_options`` parameters.
    """
    pass


def sketch_path(*args) -> Path:
    """The Sketch's current path.

    Underlying Java method: PApplet.sketchPath

    Methods
    -------

    You can use any of the following signatures:

     * sketch_path() -> Path
     * sketch_path(where: str, /) -> Path

    Parameters
    ----------

    where: str
        subdirectories relative to the sketch path

    Notes
    -----

    The Sketch's current path. If the ``where`` parameter is used, the result will
    be a subdirectory of the current path.

    Result will be relative to Python's current working directory (``os.getcwd()``)
    unless it was specifically set to something else with the ``run_sketch()`` call
    by including a ``--sketch-path`` argument in the ``py5_options`` parameters.
    """
    return _py5sketch.sketch_path(*args)


is_ready: bool = None
is_running: bool = None
is_dead: bool = None
is_dead_from_error: bool = None
is_mouse_pressed: bool = None
is_key_pressed: bool = None


def hot_reload_draw(draw: Callable) -> None:
    """Perform a hot reload of the Sketch's draw function.

    Parameters
    ----------

    draw: Callable
        function to replace existing draw function

    Notes
    -----

    Perform a hot reload of the Sketch's draw function. This method allows you to
    replace a running Sketch's draw function with a different one.
    """
    return _py5sketch.hot_reload_draw(draw)


def profile_functions(function_names: List[str]) -> None:
    """Profile the execution times of the Sketch's functions with a line profiler.

    Parameters
    ----------

    function_names: List[str]
        names of py5 functions to be profiled

    Notes
    -----

    Profile the execution times of the Sketch's functions with a line profiler. This
    uses the Python library lineprofiler to provide line by line performance data.
    The collected stats will include the number of times each line of code was
    executed (Hits) and the total amount of time spent on each line (Time). This
    information can be used to target the performance tuning efforts for a slow
    Sketch.

    This method can be called before or after ``run_sketch()``. You are welcome to
    profile multiple functions, but don't initiate profiling on the same function
    multiple times. To profile functions that do not belong to the Sketch, including
    any functions called from ``launch_thread()`` and the like, use lineprofiler
    directly and not through py5's performance tools.

    To profile just the draw function, you can also use ``profile_draw()``. To see
    the results, use ``print_line_profiler_stats()``.
    """
    return _py5sketch.profile_functions(function_names)


def profile_draw() -> None:
    """Profile the execution times of the draw function with a line profiler.

    Notes
    -----

    Profile the execution times of the draw function with a line profiler. This uses
    the Python library lineprofiler to provide line by line performance data. The
    collected stats will include the number of times each line of code was executed
    (Hits) and the total amount of time spent on each line (Time). This information
    can be used to target the performance tuning efforts for a slow Sketch.

    This method can be called before or after ``run_sketch()``. You are welcome to
    profile multiple functions, but don't initiate profiling on the same function
    multiple times. To profile functions that do not belong to the Sketch, including
    any functions called from ``launch_thread()`` and the like, use lineprofiler
    directly and not through py5's performance tools.

    To profile a other functions besides draw, use ``profile_functions()``. To see
    the results, use ``print_line_profiler_stats()``.
    """
    return _py5sketch.profile_draw()


def print_line_profiler_stats() -> None:
    """Print the line profiler stats initiated with ``profile_draw()`` or
    ``profile_functions()``.

    Notes
    -----

    Print the line profiler stats initiated with ``profile_draw()`` or
    ``profile_functions()``. The collected stats will include the number of times
    each line of code was executed (Hits) and the total amount of time spent on each
    line (Time). This information can be used to target the performance tuning
    efforts for a slow Sketch.

    This method can be called multiple times on a running Sketch.
    """
    return _py5sketch.print_line_profiler_stats()


def save_frame(filename: Union[str,
                               Path],
               *,
               format: str = None,
               drop_alpha: bool = True,
               use_thread: bool = True,
               **params) -> None:
    """Save the current frame as an image.

    Parameters
    ----------

    drop_alpha: bool = True
        remove the alpha channel when saving the image

    filename: Union[str, Path]
        output filename

    format: str = None
        image format, if not determined from filename extension

    params
        keyword arguments to pass to the PIL.Image save method

    use_thread: bool = True
        write file in separate thread

    Notes
    -----

    Save the current frame as an image. This method uses the Python library Pillow
    to write the image, so it can save images in any format that that library
    supports.

    Use the ``drop_alpha`` parameter to drop the alpha channel from the image. This
    defaults to ``True``. Some image formats such as JPG do not support alpha
    channels, and Pillow will throw an error if you try to save an image with the
    alpha channel in that format.

    The ``use_thread`` parameter will save the image in a separate Python thread.
    This improves performance by returning before the image has actually been
    written to the file.

    This method is the same as ``save()`` except it will replace a sequence of ``#``
    symbols in the ``filename`` parameter with the frame number. This is useful when
    saving an image sequence for a running animation. The first frame number will be
    1.
    """
    return _py5sketch.save_frame(
        filename,
        format=format,
        drop_alpha=drop_alpha,
        use_thread=use_thread,
        **params)


def create_image_from_numpy(
        array: np.array,
        bands: str = 'ARGB',
        *,
        dst: Py5Image = None) -> Py5Image:
    """Convert a numpy array into a Py5Image object.

    Parameters
    ----------

    array: np.array
        numpy image array

    bands: str = 'ARGB'
        color channels in array

    dst: Py5Image = None
        existing Py5Image object to put the image data into

    Notes
    -----

    Convert a numpy array into a Py5Image object. The numpy array must have 3
    dimensions and the array's ``dtype`` must be ``np.uint8``. The size of
    ``array``'s first and second dimensions will be the image's height and width,
    respectively. The third dimension is for the array's color channels.

    The ``bands`` parameter is used to interpret the ``array``'s color channel
    dimension (the array's third dimension). It can be one of ``'L'`` (single-
    channel grayscale), ``'ARGB'``, ``'RGB'``, or ``'RGBA'``. If there is no alpha
    channel, ``array`` is assumed to have no transparency. If the ``bands``
    parameter is ``'L'``, ``array``'s third dimension is optional.

    The caller can optionally pass an existing Py5Image object to put the image data
    into using the ``dst`` parameter. This can have performance benefits in code
    that would otherwise continuously create new Py5Image objects. The array's width
    and height must match that of the recycled Py5Image object.
    """
    return _py5sketch.create_image_from_numpy(array, bands=bands, dst=dst)


def convert_image(obj: Any, *, dst: Py5Image = None) -> Py5Image:
    """Convert non-py5 image objects into Py5Image objects.

    Parameters
    ----------

    dst: Py5Image = None
        existing Py5Image object to put the converted image into

    obj: Any
        object to convert into a Py5Image object

    Notes
    -----

    Convert non-py5 image objects into Py5Image objects. This facilitates py5
    compatability with other commonly used Python libraries.

    This method is comparable to ``load_image()``, except instead of reading image
    files from disk, it reads image data from other Python objects.

    Passed image object types must be known to py5's image conversion tools. New
    object types and functions to effect conversions can be registered with
    ``register_image_conversion()``.

    The ``convert_image()`` method has builtin support for conversion of
    ``PIL.Image`` objects. This will allow users to use image formats that
    ``load_image()`` cannot read. To convert a numpy array into a Py5Image, use
    ``create_image_from_numpy()``.

    The caller can optionally pass an existing Py5Image object to put the converted
    image into using the ``dst`` parameter. This can have performance benefits in
    code that would otherwise continuously create new Py5Image objects. The
    converted image width and height must match that of the recycled Py5Image
    object.
    """
    return _py5sketch.convert_image(obj, dst=dst)


def load_image(image_path: Union[str, Path], *,
               dst: Py5Image = None) -> Py5Image:
    """Load an image into a variable of type ``Py5Image``.

    Parameters
    ----------

    dst: Py5Image = None
        existing Py5Image object to load image into

    image_path: Union[str, Path]
        url or file path for image file

    Notes
    -----

    Load an image into a variable of type ``Py5Image``. Four types of images (GIF,
    JPG, TGA, PNG) can be loaded. To load images in other formats, consider using
    ``convert_image()``.

    The ``image_path`` parameter can be a file or a URL. When loading a file, the
    path can be in the data directory, relative to the current working directory
    (``sketch_path()``), or an absolute path. When loading from a URL, the
    ``image_path`` parameter must start with ``http://`` or ``https://``. If the
    image cannot be loaded, a Python ``RuntimeError`` will be thrown.

    In most cases, load all images in ``setup()`` to preload them at the start of
    the program. Loading images inside ``draw()`` will reduce the speed of a
    program. In those situations, consider using ``request_image()`` instead.

    The ``dst`` parameter allows users to store the loaded image into an existing
    Py5Image object instead of creating a new object. The size of the existing
    Py5Image object must match the size of the loaded image. Most users will not
    find the ``dst`` parameter helpful. This feature is needed internally for
    performance reasons.
    """
    return _py5sketch.load_image(image_path, dst=dst)


def request_image(image_path: Union[str, Path]) -> Py5Promise:
    """Use a Py5Promise object to load an image into a variable of type ``Py5Image``.

    Parameters
    ----------

    image_path: Union[str, Path]
        url or file path for image file

    Notes
    -----

    Use a Py5Promise object to load an image into a variable of type ``Py5Image``.
    This method provides a convenient alternative to combining
    ``launch_promise_thread()`` with ``load_image()`` to load image data.

    Consider using ``request_image()`` to load image data from within a Sketch's
    ``draw()`` function. Using ``load_image()`` in the ``draw()`` function would
    slow down the Sketch animation.

    The returned Py5Promise object has an ``is_ready`` property that will be
    ``True`` when the ``result`` property contains the value function ``f``
    returned. Before then, the ``result`` property will be ``None``.
    """
    return _py5sketch.request_image(image_path)


def run_sketch(block: bool = None, *,
               py5_options: List[str] = None,
               sketch_args: List[str] = None,
               sketch_functions: Dict[str, Callable] = None) -> None:
    """Run the Sketch.

    Parameters
    ----------

    block: bool = None
        method returns immediately (False) or blocks until Sketch exits (True)

    py5_options: List[str] = None
        command line arguments to pass to Processing as arguments

    sketch_args: List[str] = None
        command line arguments that become Sketch arguments

    sketch_functions: Dict[str, Callable] = None
        sketch methods when using module mode

    Notes
    -----

    Run the Sketch. Code in the ``settings()``, ``setup()``, and ``draw()``
    functions will be used to actualize your Sketch.

    Use the ``block`` parameter to specify if the call to ``run_sketch()`` should
    return immediately (asynchronous Sketch execution) or block until the Sketch
    exits. If the ``block`` parameter is not specified, py5 will first attempt to
    determine if the Sketch is running in a Jupyter Notebook or an IPython shell. If
    it is, ``block`` will default to ``False``, and ``True`` otherwise.

    A list of strings passed to ``py5_options`` will be passed to the Processing
    PApplet class as arguments to specify characteristics such as the window's
    location on the screen. A list of strings passed to ``sketch_args`` will be
    available to a running Sketch using ``args``. See the third example for an
    example of how this can be used.

    When calling ``run_sketch()`` in module mode, py5 will by default search for
    functions such as ``setup()``,  ``draw()``, etc. in the caller's stack frame and
    use those in the Sketch. If for some reason that is not what you want or does
    not work because you are hacking py5 to do something unusual, you can use the
    ``sketch_functions`` parameter to pass a dictionary of the desired callable
    functions. The ``sketch_functions`` parameter is not available when coding py5
    in class mode. Don't forget you can always replace the ``draw()`` function in a
    running Sketch using ``hot_reload_draw()``.

    When running a Sketch asynchronously through Jupyter Notebook, any ``print``
    statements using Python's builtin function will always appear in the output of
    the currently active cell. This will rarely be desirable, as the active cell
    will keep changing as the user executes code elsewhere in the notebook. As an
    alternative, use py5's ``println()`` method, which will place all text in the
    output of the cell that made the ``run_sketch()`` call. This will continue to be
    true if the user moves on to execute code in other Notebook cells. Use
    ``set_println_stream()`` to customize this behavior. All py5 error messages and
    stack traces are routed through the ``println()`` method. Be aware that some
    error messages and warnings generated inside the Processing Jars cannot be
    controlled in the same way, and may appear in the output of the active cell or
    mixed in with the Jupyter Kernel logs."""
    if block is None:
        block = not _in_ipython_session

    sketch_functions = sketch_functions or inspect.stack()[1].frame.f_locals
    functions = dict([(e, sketch_functions[e])
                     for e in reference.METHODS if e in sketch_functions and callable(sketch_functions[e])])

    if not set(functions.keys()) & set(['settings', 'setup', 'draw']):
        print(("Unable to find settings, setup, or draw functions. "
               "Your sketch will be a small boring gray square. "
               "If that isn't what you intended, you need to make sure "
               "your implementation of those functions are available in "
               "the local namespace that made the `run_sketch()` call."))

    global _py5sketch
    if _py5sketch.is_running:
        print(
            'Sketch is already running. To run a new sketch, exit the running sketch first.')
        return
    if _py5sketch.is_dead:
        _py5sketch = Sketch()

    _prepare_dynamic_variables(sketch_functions)

    _py5sketch._run_sketch(functions, block, py5_options, sketch_args)


def get_current_sketch() -> Sketch:
    """Get the py5 module's current ``Sketch`` instance.

    Notes
    -----

    Get the py5 module's current ``Sketch`` instance.

    When coding py5 in module mode, a Sketch instance is created on your behalf that
    is referenced within the py5 module itself. That Sketch is called the "current
    sketch." Use this method to access that Sketch instance directly."""
    return _py5sketch


def reset_py5() -> bool:
    """Reset the py5 module's current ``Sketch`` instance.

    Notes
    -----

    Reset the py5 module's current ``Sketch`` instance.

    When coding py5 in module mode, a Sketch instance is created on your behalf that
    is referenced within the py5 module itself. That Sketch is called the "Current
    Sketch." If the current Sketch exits, it will be in a dead state and cannot be
    re-run. ``reset_py5()`` will discard that exited Sketch instance and replace it
    with a new one in the ready state.

    If ``reset_py5()`` is called when the current Sketch is in the ready or running
    states, it will do nothing and return ``False``. If ``reset_py5()`` is called
    when the current Sketch is in the dead state, ``reset_py5()`` will replace it
    and return ``True``."""
    global _py5sketch
    if _py5sketch.is_dead:
        _py5sketch = Sketch()
        if _PY5_USE_IMPORTED_MODE:
            caller_locals = inspect.stack()[1].frame.f_locals
            _prepare_dynamic_variables(caller_locals)
        return True
    else:
        return False


def prune_tracebacks(prune: bool) -> None:
    """Set py5's exception handling to prune unhelpful stack trace frames when
    exceptions are thrown by a running Sketch.

    Parameters
    ----------

    prune: bool
        prune exception tracebacks

    Notes
    -----

    Set py5's exception handling to prune unhelpful stack trace frames when
    exceptions are thrown by a running Sketch. When using any Python library,
    exceptions are often thrown from within the library itself, resulting in stack
    traces that are a combination of the user's code and the library's own code.
    Often times the stack traces contributed by the library's code are not helpful
    to users because the users are not familiar with that code and/or those stack
    frames do not provide useful debugging information. This is particularly the
    case for py5, where most of the real functionality is provided by Processing's
    Java libraries and many of py5's methods are essentially thin wrappers making
    calls to Java. By default, py5 will prune its own stack trace frames from error
    messages. Almost always this is helpful, but when investigating bugs in py5
    itself, sometimes it is helpful to turn off this feature."""
    from . import methods
    methods._prune_tracebacks = prune


def set_stackprinter_style(style: str) -> None:
    """Set the formatting style for py5's stack traces.

    Parameters
    ----------

    style: str
        name of stackprinter style

    Notes
    -----

    Set the formatting style for py5's stack traces. Py5 uses the Python library
    stackprinter to show exception stack traces. The stackprinter library supports
    various color styles. By default py5 will use ``'plaintext'``, which does not
    use color. Alternative styles using color are ``'darkbg'``, ``'darkbg2'``,
    ``'darkbg3'``, ``'lightbg'``, ``'lightbg2'``, and ``'lightbg3'``."""
    from . import methods
    methods._stackprinter_style = style


def __getattr__(name):
    if hasattr(_py5sketch, name):
        return getattr(_py5sketch, name)
    else:
        raise AttributeError('py5 has no function or field named ' + name)


def __dir__():
    return py5_tools.reference.PY5_DIR_STR


__all__ = py5_tools.reference.PY5_ALL_STR
if _PY5_USE_IMPORTED_MODE:
    __all__.extend(py5_tools.reference.PY5_DYNAMIC_VARIABLES)


def _prepare_dynamic_variables(caller_locals):
    """prepare the dynamic variables for sketch execution.

    Before running the sketch, delete the module fields like `mouse_x` that need
    to be kept current as the sketch runs. This will allow the module's
    `__getattr__` function return the proper values.

    When running in imported mode, place variables in the the caller's local
    namespace that link to the Sketch's dynamic variable property objects.
    """
    for dvar in py5_tools.reference.PY5_DYNAMIC_VARIABLES:
        if dvar in globals():
            globals().pop(dvar)
        if _PY5_USE_IMPORTED_MODE:
            caller_locals[dvar] = getattr(_py5sketch, '_get_' + dvar)


_prepare_dynamic_variables(locals())
