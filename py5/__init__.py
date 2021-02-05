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
import logging
import inspect
from typing import overload, Any, Callable, Union, Dict, List, Tuple  # noqa
from nptyping import NDArray, Float  # noqa

import json  # noqa
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
    py5_tools.start_jvm()

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


__version__ = '0.3a5'

logger = logging.getLogger(__name__)

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
java_version: float = None
java_version_name: str = None
key: chr = None
key_code: int = None
mouse_button: int = None
mouse_x: int = None
mouse_y: int = None
pixel_height: int = None
pixel_width: int = None
pixels: JArray(JInt) = None
pmouse_x: int = None
pmouse_y: int = None
width: int = None


def alpha(rgb: int, /) -> float:
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
    with the ambient light component of environment. The color components set
    through the parameters define the reflectance. For example in the default color
    mode, setting v1=255, v2=127, v3=0, would cause all the red light to reflect and
    half of the green light to reflect. Used in combination with ``emissive()``,
    ``specular()``, and ``shininess()`` in setting the material properties of
    shapes.
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
    with the ambient light component of environment. The color components set
    through the parameters define the reflectance. For example in the default color
    mode, setting v1=255, v2=127, v3=0, would cause all the red light to reflect and
    half of the green light to reflect. Used in combination with ``emissive()``,
    ``specular()``, and ``shininess()`` in setting the material properties of
    shapes.
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
    with the ambient light component of environment. The color components set
    through the parameters define the reflectance. For example in the default color
    mode, setting v1=255, v2=127, v3=0, would cause all the red light to reflect and
    half of the green light to reflect. Used in combination with ``emissive()``,
    ``specular()``, and ``shininess()`` in setting the material properties of
    shapes.
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
    with the ambient light component of environment. The color components set
    through the parameters define the reflectance. For example in the default color
    mode, setting v1=255, v2=127, v3=0, would cause all the red light to reflect and
    half of the green light to reflect. Used in combination with ``emissive()``,
    ``specular()``, and ``shininess()`` in setting the material properties of
    shapes.
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
    and ``v3`` parameters are interpreted as either RGB or HSB values, depending on
    the current color mode.
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
    and ``v3`` parameters are interpreted as either RGB or HSB values, depending on
    the current color mode.
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
    and ``v3`` parameters are interpreted as either RGB or HSB values, depending on
    the current color mode.
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
    return _py5sketch.arc(*args)


@overload
def background(gray: float, /) -> None:
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
def background(gray: float, alpha: float, /) -> None:
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
def background(v1: float, v2: float, v3: float, /) -> None:
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
def background(v1: float, v2: float, v3: float, alpha: float, /) -> None:
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
def background(rgb: int, /) -> None:
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
def background(rgb: int, alpha: float, /) -> None:
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
def background(image: Py5Image, /) -> None:
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


def background(*args):
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
    return _py5sketch.begin_camera()


def begin_contour() -> None:
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
        missing variable description

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

    ``begin_record()`` works only with the PDF and SVG renderers.
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
        missing variable description

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

    ``begin_record()`` works only with the PDF and SVG renderers.
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
        missing variable description

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

    ``begin_record()`` works only with the PDF and SVG renderers.
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
    version requires rendering with P3D (see the Environment reference for more
    information).
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
    version requires rendering with P3D (see the Environment reference for more
    information).
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
    version requires rendering with P3D (see the Environment reference for more
    information).
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
    MODE parameter specified to ``begin_shape()``. Using the 3D version requires
    rendering with P3D (see the Environment reference for more information).
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
    MODE parameter specified to ``begin_shape()``. Using the 3D version requires
    rendering with P3D (see the Environment reference for more information).
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
    MODE parameter specified to ``begin_shape()``. Using the 3D version requires
    rendering with P3D (see the Environment reference for more information).
    """
    return _py5sketch.bezier_vertex(*args)


def bezier_vertices(coordinates: NDArray[(Any, Any), Float], /) -> None:
    """The documentation for this field or method has not yet been written.

    Underlying Java method: PApplet.bezierVertices

    Parameters
    ----------

    coordinates: NDArray[(Any, Any), Float]
        missing variable description

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
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


def clear() -> None:
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
    return _py5sketch.clear()


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
    either CORNER, CORNERS, or CENTER.
    """
    return _py5sketch.clip(a, b, c, d)


@overload
def color(fgray: float, /) -> int:
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
def color(fgray: float, falpha: float, /) -> int:
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
def color(v1: float, v2: float, v3: float, /) -> int:
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
def color(v1: float, v2: float, v3: float, alpha: float, /) -> int:
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
def color(gray: int, /) -> int:
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
def color(gray: int, alpha: int, /) -> int:
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
def color(v1: int, v2: int, v3: int, /) -> int:
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
def color(v1: int, v2: int, v3: int, alpha: int, /) -> int:
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


def color(*args):
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
    return _py5sketch.color(*args)


@overload
def color_mode(mode: int, /) -> None:
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
def color_mode(mode: int, max: float, /) -> None:
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
def color_mode(mode: int, max1: float, max2: float, max3: float, /) -> None:
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
def color_mode(mode: int, max1: float, max2: float,
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


def color_mode(*args):
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
    return _py5sketch.copy(*args)


@overload
def create_font(name: str, size: float, /) -> Py5Font:
    """Dynamically converts a font to the format used by Processing from a .ttf or .otf
    file inside the sketch's "data" folder or a font that's installed elsewhere on
    the computer.

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

    Dynamically converts a font to the format used by Processing from a .ttf or .otf
    file inside the sketch's "data" folder or a font that's installed elsewhere on
    the computer. If you want to use a font installed on your computer, use the
    ``Py5Font.list()`` method to first determine the names for the fonts recognized
    by the computer and are compatible with this function. Not all fonts can be used
    and some might work with one operating system and not others. When sharing a
    sketch with other people or posting it on the web, you may need to include a
    .ttf or .otf version of your font in the data directory of the sketch because
    other people might not have the font installed on their computer. Only fonts
    that can legally be distributed should be included with a sketch.

    The ``size`` parameter states the font size you want to generate. The ``smooth``
    parameter specifies if the font should be antialiased or not. The ``charset``
    parameter is an array of chars that specifies the characters to generate.

    This function allows Processing to work with the font natively in the default
    renderer, so the letters are defined by vector geometry and are rendered
    quickly. In the ``P2D`` and ``P3D`` renderers, the function sets the project to
    render the font as a series of small textures. For instance, when using the
    default renderer, the actual native version of the font will be employed by the
    sketch, improving drawing quality and performance. With the ``P2D`` and ``P3D``
    renderers, the bitmapped version will be used to improve speed and appearance,
    but the results are poor when exporting if the sketch does not include the .otf
    or .ttf file, and the requested font is not available on the machine running the
    sketch.
    """
    pass


@overload
def create_font(name: str, size: float, smooth: bool, /) -> Py5Font:
    """Dynamically converts a font to the format used by Processing from a .ttf or .otf
    file inside the sketch's "data" folder or a font that's installed elsewhere on
    the computer.

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

    Dynamically converts a font to the format used by Processing from a .ttf or .otf
    file inside the sketch's "data" folder or a font that's installed elsewhere on
    the computer. If you want to use a font installed on your computer, use the
    ``Py5Font.list()`` method to first determine the names for the fonts recognized
    by the computer and are compatible with this function. Not all fonts can be used
    and some might work with one operating system and not others. When sharing a
    sketch with other people or posting it on the web, you may need to include a
    .ttf or .otf version of your font in the data directory of the sketch because
    other people might not have the font installed on their computer. Only fonts
    that can legally be distributed should be included with a sketch.

    The ``size`` parameter states the font size you want to generate. The ``smooth``
    parameter specifies if the font should be antialiased or not. The ``charset``
    parameter is an array of chars that specifies the characters to generate.

    This function allows Processing to work with the font natively in the default
    renderer, so the letters are defined by vector geometry and are rendered
    quickly. In the ``P2D`` and ``P3D`` renderers, the function sets the project to
    render the font as a series of small textures. For instance, when using the
    default renderer, the actual native version of the font will be employed by the
    sketch, improving drawing quality and performance. With the ``P2D`` and ``P3D``
    renderers, the bitmapped version will be used to improve speed and appearance,
    but the results are poor when exporting if the sketch does not include the .otf
    or .ttf file, and the requested font is not available on the machine running the
    sketch.
    """
    pass


@overload
def create_font(name: str, size: float, smooth: bool,
                charset: List[chr], /) -> Py5Font:
    """Dynamically converts a font to the format used by Processing from a .ttf or .otf
    file inside the sketch's "data" folder or a font that's installed elsewhere on
    the computer.

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

    Dynamically converts a font to the format used by Processing from a .ttf or .otf
    file inside the sketch's "data" folder or a font that's installed elsewhere on
    the computer. If you want to use a font installed on your computer, use the
    ``Py5Font.list()`` method to first determine the names for the fonts recognized
    by the computer and are compatible with this function. Not all fonts can be used
    and some might work with one operating system and not others. When sharing a
    sketch with other people or posting it on the web, you may need to include a
    .ttf or .otf version of your font in the data directory of the sketch because
    other people might not have the font installed on their computer. Only fonts
    that can legally be distributed should be included with a sketch.

    The ``size`` parameter states the font size you want to generate. The ``smooth``
    parameter specifies if the font should be antialiased or not. The ``charset``
    parameter is an array of chars that specifies the characters to generate.

    This function allows Processing to work with the font natively in the default
    renderer, so the letters are defined by vector geometry and are rendered
    quickly. In the ``P2D`` and ``P3D`` renderers, the function sets the project to
    render the font as a series of small textures. For instance, when using the
    default renderer, the actual native version of the font will be employed by the
    sketch, improving drawing quality and performance. With the ``P2D`` and ``P3D``
    renderers, the bitmapped version will be used to improve speed and appearance,
    but the results are poor when exporting if the sketch does not include the .otf
    or .ttf file, and the requested font is not available on the machine running the
    sketch.
    """
    pass


def create_font(*args):
    """Dynamically converts a font to the format used by Processing from a .ttf or .otf
    file inside the sketch's "data" folder or a font that's installed elsewhere on
    the computer.

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

    Dynamically converts a font to the format used by Processing from a .ttf or .otf
    file inside the sketch's "data" folder or a font that's installed elsewhere on
    the computer. If you want to use a font installed on your computer, use the
    ``Py5Font.list()`` method to first determine the names for the fonts recognized
    by the computer and are compatible with this function. Not all fonts can be used
    and some might work with one operating system and not others. When sharing a
    sketch with other people or posting it on the web, you may need to include a
    .ttf or .otf version of your font in the data directory of the sketch because
    other people might not have the font installed on their computer. Only fonts
    that can legally be distributed should be included with a sketch.

    The ``size`` parameter states the font size you want to generate. The ``smooth``
    parameter specifies if the font should be antialiased or not. The ``charset``
    parameter is an array of chars that specifies the characters to generate.

    This function allows Processing to work with the font natively in the default
    renderer, so the letters are defined by vector geometry and are rendered
    quickly. In the ``P2D`` and ``P3D`` renderers, the function sets the project to
    render the font as a series of small textures. For instance, when using the
    default renderer, the actual native version of the font will be employed by the
    sketch, improving drawing quality and performance. With the ``P2D`` and ``P3D``
    renderers, the bitmapped version will be used to improve speed and appearance,
    but the results are poor when exporting if the sketch does not include the .otf
    or .ttf file, and the requested font is not available on the machine running the
    sketch.
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
    renderer. It can be defined as P2D, P3D, PDF, or SVG. If the third parameter
    isn't used, the default renderer is set. The PDF and SVG renderers require the
    filename parameter.

    It's important to consider the renderer used with ``create_graphics()`` in
    relation to the main renderer specified in ``size()``. For example, it's only
    possible to use P2D or P3D with ``create_graphics()`` when one of them is
    defined in ``size()``. Unlike Processing 1.0, P2D and P3D use OpenGL for
    drawing, and when using an OpenGL renderer it's necessary for the main drawing
    surface to be OpenGL-based. If P2D or P3D are used as the renderer in
    ``size()``, then any of the options can be used with ``create_graphics()``. If
    the default renderer is used in ``size()``, then only the default, PDF, or SVG
    can be used with ``create_graphics()``.

    It's important to run all drawing functions between the ``begin_draw()`` and
    ``end_draw()``. As the exception to this rule, ``smooth()`` should be run on the
    PGraphics object before ``begin_draw()``. See the reference for ``smooth()`` for
    more detail.

    The ``create_graphics()`` function should almost never be used inside ``draw()``
    because of the memory and time needed to set up the graphics. One-time or
    occasional use during ``draw()`` might be acceptable, but code that calls
    ``create_graphics()`` at 60 frames per second might run out of memory or freeze
    your sketch.

    Unlike the main drawing surface which is completely opaque, surfaces created
    with ``create_graphics()`` can have transparency. This makes it possible to draw
    into a graphics and maintain the alpha channel. By using ``save()`` to write a
    PNG or TGA file, the transparency of the graphics object will be honored.
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
    renderer. It can be defined as P2D, P3D, PDF, or SVG. If the third parameter
    isn't used, the default renderer is set. The PDF and SVG renderers require the
    filename parameter.

    It's important to consider the renderer used with ``create_graphics()`` in
    relation to the main renderer specified in ``size()``. For example, it's only
    possible to use P2D or P3D with ``create_graphics()`` when one of them is
    defined in ``size()``. Unlike Processing 1.0, P2D and P3D use OpenGL for
    drawing, and when using an OpenGL renderer it's necessary for the main drawing
    surface to be OpenGL-based. If P2D or P3D are used as the renderer in
    ``size()``, then any of the options can be used with ``create_graphics()``. If
    the default renderer is used in ``size()``, then only the default, PDF, or SVG
    can be used with ``create_graphics()``.

    It's important to run all drawing functions between the ``begin_draw()`` and
    ``end_draw()``. As the exception to this rule, ``smooth()`` should be run on the
    PGraphics object before ``begin_draw()``. See the reference for ``smooth()`` for
    more detail.

    The ``create_graphics()`` function should almost never be used inside ``draw()``
    because of the memory and time needed to set up the graphics. One-time or
    occasional use during ``draw()`` might be acceptable, but code that calls
    ``create_graphics()`` at 60 frames per second might run out of memory or freeze
    your sketch.

    Unlike the main drawing surface which is completely opaque, surfaces created
    with ``create_graphics()`` can have transparency. This makes it possible to draw
    into a graphics and maintain the alpha channel. By using ``save()`` to write a
    PNG or TGA file, the transparency of the graphics object will be honored.
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
    renderer. It can be defined as P2D, P3D, PDF, or SVG. If the third parameter
    isn't used, the default renderer is set. The PDF and SVG renderers require the
    filename parameter.

    It's important to consider the renderer used with ``create_graphics()`` in
    relation to the main renderer specified in ``size()``. For example, it's only
    possible to use P2D or P3D with ``create_graphics()`` when one of them is
    defined in ``size()``. Unlike Processing 1.0, P2D and P3D use OpenGL for
    drawing, and when using an OpenGL renderer it's necessary for the main drawing
    surface to be OpenGL-based. If P2D or P3D are used as the renderer in
    ``size()``, then any of the options can be used with ``create_graphics()``. If
    the default renderer is used in ``size()``, then only the default, PDF, or SVG
    can be used with ``create_graphics()``.

    It's important to run all drawing functions between the ``begin_draw()`` and
    ``end_draw()``. As the exception to this rule, ``smooth()`` should be run on the
    PGraphics object before ``begin_draw()``. See the reference for ``smooth()`` for
    more detail.

    The ``create_graphics()`` function should almost never be used inside ``draw()``
    because of the memory and time needed to set up the graphics. One-time or
    occasional use during ``draw()`` might be acceptable, but code that calls
    ``create_graphics()`` at 60 frames per second might run out of memory or freeze
    your sketch.

    Unlike the main drawing surface which is completely opaque, surfaces created
    with ``create_graphics()`` can have transparency. This makes it possible to draw
    into a graphics and maintain the alpha channel. By using ``save()`` to write a
    PNG or TGA file, the transparency of the graphics object will be honored.
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
    renderer. It can be defined as P2D, P3D, PDF, or SVG. If the third parameter
    isn't used, the default renderer is set. The PDF and SVG renderers require the
    filename parameter.

    It's important to consider the renderer used with ``create_graphics()`` in
    relation to the main renderer specified in ``size()``. For example, it's only
    possible to use P2D or P3D with ``create_graphics()`` when one of them is
    defined in ``size()``. Unlike Processing 1.0, P2D and P3D use OpenGL for
    drawing, and when using an OpenGL renderer it's necessary for the main drawing
    surface to be OpenGL-based. If P2D or P3D are used as the renderer in
    ``size()``, then any of the options can be used with ``create_graphics()``. If
    the default renderer is used in ``size()``, then only the default, PDF, or SVG
    can be used with ``create_graphics()``.

    It's important to run all drawing functions between the ``begin_draw()`` and
    ``end_draw()``. As the exception to this rule, ``smooth()`` should be run on the
    PGraphics object before ``begin_draw()``. See the reference for ``smooth()`` for
    more detail.

    The ``create_graphics()`` function should almost never be used inside ``draw()``
    because of the memory and time needed to set up the graphics. One-time or
    occasional use during ``draw()`` might be acceptable, but code that calls
    ``create_graphics()`` at 60 frames per second might run out of memory or freeze
    your sketch.

    Unlike the main drawing surface which is completely opaque, surfaces created
    with ``create_graphics()`` can have transparency. This makes it possible to draw
    into a graphics and maintain the alpha channel. By using ``save()`` to write a
    PNG or TGA file, the transparency of the graphics object will be honored.
    """
    return _py5sketch.create_graphics(*args)


def create_image(w: int, h: int, format: int, /) -> Py5Image:
    """Creates a new PImage (the datatype for storing images).

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

    Creates a new PImage (the datatype for storing images). This provides a fresh
    buffer of pixels to play with. Set the size of the buffer with the ``width`` and
    ``height`` parameters. The ``format`` parameter defines how the pixels are
    stored. See the PImage reference for more information.

    Be sure to include all three parameters, specifying only the width and height
    (but no format) will produce a strange error.

    Advanced users please note that ``create_image()`` should be used instead of the
    syntax ``new Py5Image()``.
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
        any variable of type PImage

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

    With the P2D and P3D renderers, a generic set of cursors are used because the
    OpenGL renderer doesn't have access to the default cursor images for each
    platform (Issue 3791).
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
        any variable of type PImage

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

    With the P2D and P3D renderers, a generic set of cursors are used because the
    OpenGL renderer doesn't have access to the default cursor images for each
    platform (Issue 3791).
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
        any variable of type PImage

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

    With the P2D and P3D renderers, a generic set of cursors are used because the
    OpenGL renderer doesn't have access to the default cursor images for each
    platform (Issue 3791).
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
        any variable of type PImage

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

    With the P2D and P3D renderers, a generic set of cursors are used because the
    OpenGL renderer doesn't have access to the default cursor images for each
    platform (Issue 3791).
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
        any variable of type PImage

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

    With the P2D and P3D renderers, a generic set of cursors are used because the
    OpenGL renderer doesn't have access to the default cursor images for each
    platform (Issue 3791).
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
    rendering with P3D (see the Environment reference for more information).
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
    rendering with P3D (see the Environment reference for more information).
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
    rendering with P3D (see the Environment reference for more information).
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
    function is only useful when using the P3D renderer as the default P2D renderer
    does not use this information.
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
    on the curve. As seen in the example above, this can be used once with the ``x``
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
    return _py5sketch.curve_vertex(*args)


def curve_vertices(coordinates: NDArray[(Any, Any), Float], /) -> None:
    """The documentation for this field or method has not yet been written.

    Underlying Java method: PApplet.curveVertices

    Parameters
    ----------

    coordinates: NDArray[(Any, Any), Float]
        missing variable description

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return _py5sketch.curve_vertices(coordinates)


def day() -> int:
    """Processing communicates with the clock on your computer.

    Underlying Java method: PApplet.day

    Notes
    -----

    Processing communicates with the clock on your computer. The ``day()`` function
    returns the current day as a value from 1 - 31.
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
    ``v3`` parameters are interpreted as either RGB or HSB values, depending on the
    current color mode. The ``nx``, ``ny``, and ``nz`` parameters specify the
    direction the light is facing. For example, setting ``ny`` to -1 will cause the
    geometry to be lit from below (since the light would be facing directly upward).
    """
    return _py5sketch.directional_light(v1, v2, v3, nx, ny, nz)


@overload
def display_density() -> int:
    """This function returns the number "2" if the screen is a high-density screen
    (called a Retina display on OS X or high-dpi on Windows and Linux) and a "1" if
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
    (called a Retina display on OS X or high-dpi on Windows and Linux) and a "1" if
    not. This information is useful for a program to adapt to run at double the
    pixel density on a screen that supports it.
    """
    pass


@overload
def display_density(display: int, /) -> int:
    """This function returns the number "2" if the screen is a high-density screen
    (called a Retina display on OS X or high-dpi on Windows and Linux) and a "1" if
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
    (called a Retina display on OS X or high-dpi on Windows and Linux) and a "1" if
    not. This information is useful for a program to adapt to run at double the
    pixel density on a screen that supports it.
    """
    pass


def display_density(*args):
    """This function returns the number "2" if the screen is a high-density screen
    (called a Retina display on OS X or high-dpi on Windows and Linux) and a "1" if
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
    (called a Retina display on OS X or high-dpi on Windows and Linux) and a "1" if
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

    The parameter must be written in ALL CAPS because Processing is a case-sensitive
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
    screen. Used in combination with ``ambient()``, ``specular()``, and
    ``shininess()`` in setting the material properties of shapes.
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
    screen. Used in combination with ``ambient()``, ``specular()``, and
    ``shininess()`` in setting the material properties of shapes.
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
    screen. Used in combination with ``ambient()``, ``specular()``, and
    ``shininess()`` in setting the material properties of shapes.
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
    screen. Used in combination with ``ambient()``, ``specular()``, and
    ``shininess()`` in setting the material properties of shapes.
    """
    return _py5sketch.emissive(*args)


def end_camera() -> None:
    """The ``begin_camera()`` and ``end_camera()`` functions enable advanced
    customization of the camera space.

    Underlying Java method: PApplet.endCamera

    Notes
    -----

    The ``begin_camera()`` and ``end_camera()`` functions enable advanced
    customization of the camera space. Please see the reference for
    ``begin_camera()`` for a description of how the functions are used.
    """
    return _py5sketch.end_camera()


def end_contour() -> None:
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
    image buffer. The constant CLOSE as the value for the MODE parameter to close
    the shape (to connect the beginning and the end).
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
    image buffer. The constant CLOSE as the value for the MODE parameter to close
    the shape (to connect the beginning and the end).
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
    image buffer. The constant CLOSE as the value for the MODE parameter to close
    the shape (to connect the beginning and the end).
    """
    return _py5sketch.end_shape(*args)


def exit_sketch() -> None:
    """Quits/stops/exits the program.

    Underlying Java method: PApplet.exit

    Notes
    -----

    Quits/stops/exits the program. Programs without a ``draw()`` function stop
    automatically after the last line has run, but programs with ``draw()`` run
    continuously until the program is manually stopped or ``exit()`` is run.

    Rather than terminating immediately, ``exit()`` will cause the sketch to exit
    after ``draw()`` has completed (or after ``setup()`` completes if called during
    the ``setup()`` function).

    For Java programmers, this is *not* the same as System.``exit()``. Further,
    System.``exit()`` should not be used because closing out an application while
    ``draw()`` is running may cause a crash (particularly with P3D).
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
    """This function is new for Processing 3.0.

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
        the screen to run the sketch on (1, 2, 3, etc. or on multiple screens using SPAN)

    renderer: str
        the renderer to use, e.g. P2D, P3D, JAVA2D (default)

    Notes
    -----

    This function is new for Processing 3.0. It opens a sketch using the full size
    of the computer's display. This function must be the first line in ``setup()``.
    The ``size()`` and ``full_screen()`` functions cannot both be used in the same
    program, just choose one.

    When ``full_screen()`` is used without a parameter, it draws the sketch to the
    screen currently selected inside the Preferences window. When it is used with a
    single parameter, this number defines the screen to display to program on (e.g.
    1, 2, 3...). When used with two parameters, the first defines the renderer to
    use (e.g. P2D) and the second defines the screen. The ``SPAN`` parameter can be
    used in place of a screen number to draw the sketch as a full-screen window
    across all of the attached displays if there are more than one.

    Prior to Processing 3.0, a full-screen program was defined with
    ``size(display_width, display_height)``.
    """
    pass


@overload
def full_screen(display: int, /) -> None:
    """This function is new for Processing 3.0.

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
        the screen to run the sketch on (1, 2, 3, etc. or on multiple screens using SPAN)

    renderer: str
        the renderer to use, e.g. P2D, P3D, JAVA2D (default)

    Notes
    -----

    This function is new for Processing 3.0. It opens a sketch using the full size
    of the computer's display. This function must be the first line in ``setup()``.
    The ``size()`` and ``full_screen()`` functions cannot both be used in the same
    program, just choose one.

    When ``full_screen()`` is used without a parameter, it draws the sketch to the
    screen currently selected inside the Preferences window. When it is used with a
    single parameter, this number defines the screen to display to program on (e.g.
    1, 2, 3...). When used with two parameters, the first defines the renderer to
    use (e.g. P2D) and the second defines the screen. The ``SPAN`` parameter can be
    used in place of a screen number to draw the sketch as a full-screen window
    across all of the attached displays if there are more than one.

    Prior to Processing 3.0, a full-screen program was defined with
    ``size(display_width, display_height)``.
    """
    pass


@overload
def full_screen(renderer: str, /) -> None:
    """This function is new for Processing 3.0.

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
        the screen to run the sketch on (1, 2, 3, etc. or on multiple screens using SPAN)

    renderer: str
        the renderer to use, e.g. P2D, P3D, JAVA2D (default)

    Notes
    -----

    This function is new for Processing 3.0. It opens a sketch using the full size
    of the computer's display. This function must be the first line in ``setup()``.
    The ``size()`` and ``full_screen()`` functions cannot both be used in the same
    program, just choose one.

    When ``full_screen()`` is used without a parameter, it draws the sketch to the
    screen currently selected inside the Preferences window. When it is used with a
    single parameter, this number defines the screen to display to program on (e.g.
    1, 2, 3...). When used with two parameters, the first defines the renderer to
    use (e.g. P2D) and the second defines the screen. The ``SPAN`` parameter can be
    used in place of a screen number to draw the sketch as a full-screen window
    across all of the attached displays if there are more than one.

    Prior to Processing 3.0, a full-screen program was defined with
    ``size(display_width, display_height)``.
    """
    pass


@overload
def full_screen(renderer: str, display: int, /) -> None:
    """This function is new for Processing 3.0.

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
        the screen to run the sketch on (1, 2, 3, etc. or on multiple screens using SPAN)

    renderer: str
        the renderer to use, e.g. P2D, P3D, JAVA2D (default)

    Notes
    -----

    This function is new for Processing 3.0. It opens a sketch using the full size
    of the computer's display. This function must be the first line in ``setup()``.
    The ``size()`` and ``full_screen()`` functions cannot both be used in the same
    program, just choose one.

    When ``full_screen()`` is used without a parameter, it draws the sketch to the
    screen currently selected inside the Preferences window. When it is used with a
    single parameter, this number defines the screen to display to program on (e.g.
    1, 2, 3...). When used with two parameters, the first defines the renderer to
    use (e.g. P2D) and the second defines the screen. The ``SPAN`` parameter can be
    used in place of a screen number to draw the sketch as a full-screen window
    across all of the attached displays if there are more than one.

    Prior to Processing 3.0, a full-screen program was defined with
    ``size(display_width, display_height)``.
    """
    pass


def full_screen(*args):
    """This function is new for Processing 3.0.

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
        the screen to run the sketch on (1, 2, 3, etc. or on multiple screens using SPAN)

    renderer: str
        the renderer to use, e.g. P2D, P3D, JAVA2D (default)

    Notes
    -----

    This function is new for Processing 3.0. It opens a sketch using the full size
    of the computer's display. This function must be the first line in ``setup()``.
    The ``size()`` and ``full_screen()`` functions cannot both be used in the same
    program, just choose one.

    When ``full_screen()`` is used without a parameter, it draws the sketch to the
    screen currently selected inside the Preferences window. When it is used with a
    single parameter, this number defines the screen to display to program on (e.g.
    1, 2, 3...). When used with two parameters, the first defines the renderer to
    use (e.g. P2D) and the second defines the screen. The ``SPAN`` parameter can be
    used in place of a screen number to draw the sketch as a full-screen window
    across all of the attached displays if there are more than one.

    Prior to Processing 3.0, a full-screen program was defined with
    ``size(display_width, display_height)``.
    """
    return _py5sketch.full_screen(*args)


@overload
def get() -> Py5Image:
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
def get(x: int, y: int, /) -> int:
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
def get(x: int, y: int, w: int, h: int, /) -> Py5Image:
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


def get(*args):
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
    return _py5sketch.get(*args)


def get_frame_rate() -> float:
    """The documentation for this field or method has not yet been written.

    Underlying Java method: PApplet.getFrameRate

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return _py5sketch.get_frame_rate()


def get_graphics() -> Py5Graphics:
    """The documentation for this field or method has not yet been written.

    Underlying Java method: PApplet.getGraphics

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return _py5sketch.get_graphics()


@overload
def get_matrix() -> NDArray[(Any, Any), Float]:
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
def get_matrix(target: NDArray[(2, 3), Float], /) -> NDArray[(2, 3), Float]:
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
def get_matrix(target: NDArray[(4, 4), Float], /) -> NDArray[(4, 4), Float]:
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


def get_matrix(*args):
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
    return _py5sketch.get_matrix(*args)


def get_surface() -> Py5Surface:
    """The documentation for this field or method has not yet been written.

    Underlying Java method: PApplet.getSurface

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
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
    return _py5sketch.green(rgb)


def hint(which: int, /) -> None:
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
    return _py5sketch.hint(which)


def hour() -> int:
    """Processing communicates with the clock on your computer.

    Underlying Java method: PApplet.hour

    Notes
    -----

    Processing communicates with the clock on your computer. The ``hour()`` function
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
    ``image()`` as the  location of one corner, and the fourth and fifth parameters
    as the opposite corner.

    ``image_mode(CENTER)`` interprets the second and third parameters of ``image()``
    as the image's center point. If two additional parameters are specified, they
    are used to set the image's width and height.

    The parameter must be written in ALL CAPS because Processing is a case-sensitive
    language.
    """
    return _py5sketch.image_mode(mode)


def is_key_pressed() -> bool:
    """The documentation for this field or method has not yet been written.

    Underlying Java method: PApplet.isKeyPressed

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return _py5sketch.is_key_pressed()


def is_mouse_pressed() -> bool:
    """The documentation for this field or method has not yet been written.

    Underlying Java method: PApplet.isMousePressed

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return _py5sketch.is_mouse_pressed()


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
    used to calculate the falloff with the following equation:

    d = distance from light position to vertex position
    falloff = 1 / (CONSTANT + d * LINEAR + (d*d) * QUADRATIC)

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
    The defaults are ambientLight(128, 128, 128) and directionalLight(128, 128, 128,
    0, 0, -1), lightFalloff(1, 0, 0), and lightSpecular(0, 0, 0). Lights need to be
    included in the ``draw()`` to remain persistent in a looping program. Placing
    them in the ``setup()`` of a looping program will cause them to only have an
    effect the first time through the loop.
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
    P3D parameter in combination with ``size()`` as shown in the above example.
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
    P3D parameter in combination with ``size()`` as shown in the above example.
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
    P3D parameter in combination with ``size()`` as shown in the above example.
    """
    return _py5sketch.line(*args)


def lines(coordinates: NDArray[(Any, Any), Float], /) -> None:
    """The documentation for this field or method has not yet been written.

    Underlying Java method: PApplet.lines

    Parameters
    ----------

    coordinates: NDArray[(Any, Any), Float]
        missing variable description

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
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

    Loads a .vlw formatted font into a ``Py5Font`` object. Create a .vlw font by
    selecting "Create Font..." from the Tools menu. This tool creates a texture for
    each alphanumeric character and then adds them as a .vlw file to the current
    sketch's data folder. Because the letters are defined as textures (and not
    vector data) the size at which the fonts are created must be considered in
    relation to the size at which they are drawn. For example, load a 32pt font if
    the sketch displays the font at 32 pixels or smaller. Conversely, if a 12pt font
    is loaded and displayed at 48pts, the letters will be distorted because the
    program will be stretching a small graphic to a large size.

    Like ``load_image()`` and other functions that load data, the ``load_font()``
    function should not be used inside ``draw()``, because it will slow down the
    sketch considerably, as the font will be re-loaded from the disk (or network) on
    each frame. It's recommended to load files inside ``setup()``

    To load correctly, fonts must be located in the "data" folder of the current
    sketch. Alternatively, the file maybe be loaded from anywhere on the local
    computer using an absolute path (something that starts with / on Unix and Linux,
    or a drive letter on Windows), or the filename parameter can be a URL for a file
    found on a network.

    If the file is not available or an error occurs, ``None`` will be returned and
    an error message will be printed to the console. The error message does not halt
    the program, however the null value may cause a NullPointerException if your
    code does not check whether the value returned is null.

    Use ``create_font()`` (instead of ``load_font()``) to enable vector data to be
    used with the default renderer setting. This can be helpful when many font sizes
    are needed, or when using any renderer based on the default renderer, such as
    the PDF library.
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
    ``pixels`` until ``load_pixels()`` is called again.
    """
    return _py5sketch.load_pixels()


@overload
def load_shader(frag_filename: str, /) -> Py5Shader:
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
def load_shader(frag_filename: str, vert_filename: str, /) -> Py5Shader:
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


def load_shader(*args):
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
    return _py5sketch.load_shape(*args)


def loop() -> None:
    """By default, Processing loops through ``draw()`` continuously, executing the code
    within it.

    Underlying Java method: PApplet.loop

    Notes
    -----

    By default, Processing loops through ``draw()`` continuously, executing the code
    within it. However, the ``draw()`` loop may be stopped by calling ``no_loop()``.
    In that case, the ``draw()`` loop can be resumed with ``loop()``.
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
    """Processing communicates with the clock on your computer.

    Underlying Java method: PApplet.minute

    Notes
    -----

    Processing communicates with the clock on your computer. The ``minute()``
    function returns the current minute as a value from 0 - 59.
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
    """Processing communicates with the clock on your computer.

    Underlying Java method: PApplet.month

    Notes
    -----

    Processing communicates with the clock on your computer. The ``month()``
    function returns the current month as a value from 1 - 12.
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

    Hides the cursor from view. Will not work when running the program in a web
    browser or in full screen (Present) mode.
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
    """Stops Processing from continuously executing the code within ``draw()``.

    Underlying Java method: PApplet.noLoop

    Notes
    -----

    Stops Processing from continuously executing the code within ``draw()``. If
    ``loop()`` is called, the code in ``draw()`` begins to run continuously again.
    If using ``no_loop()`` in ``setup()``, it should be the last line inside the
    block.

    When ``no_loop()`` is used, it's not possible to manipulate or access the screen
    inside event handling functions such as ``mouse_pressed()`` or
    ``key_pressed()``. Instead, use those functions to call ``redraw()`` or
    ``loop()``, which will run ``draw()``, which can update the screen properly.
    This means that when ``no_loop()`` has been called, no drawing can happen, and
    functions like ``save_frame()`` or ``load_pixels()`` may not be used.

    Note that if the sketch is resized, ``redraw()`` will be called to update the
    sketch, even after ``no_loop()`` has been specified. Otherwise, the sketch would
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
    ``no_smooth()`` to disable smoothing of geometry, fonts, and images. Since the
    release of Processing 3.0, the ``no_smooth()`` function can only be run once for
    each sketch, either at the top of a sketch without a ``setup()``, or after the
    ``size()`` function when used in a sketch with ``setup()``. See the examples
    above for both scenarios.
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


def no_texture() -> None:
    """The documentation for this field or method has not yet been written.

    Underlying Java method: PApplet.noTexture

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return _py5sketch.no_texture()


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
    which, in turn, determines how lighting affects it. Processing attempts to
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
    ortho(-width/2, width/2, -height/2, height/2).
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
    ortho(-width/2, width/2, -height/2, height/2).
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
    ortho(-width/2, width/2, -height/2, height/2).
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
    ortho(-width/2, width/2, -height/2, height/2).
    """
    return _py5sketch.ortho(*args)


def pause() -> None:
    """The documentation for this field or method has not yet been written.

    Underlying Java method: PApplet.pause

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return _py5sketch.pause()


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
    The default values are: perspective(PI/3.0, width/height, cameraZ/10.0,
    cameraZ*10.0) where cameraZ is ((height/2.0) / tan(PI*60.0/360.0));
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
    The default values are: perspective(PI/3.0, width/height, cameraZ/10.0,
    cameraZ*10.0) where cameraZ is ((height/2.0) / tan(PI*60.0/360.0));
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
    The default values are: perspective(PI/3.0, width/height, cameraZ/10.0,
    cameraZ*10.0) where cameraZ is ((height/2.0) / tan(PI*60.0/360.0));
    """
    return _py5sketch.perspective(*args)


def pixel_density(density: int, /) -> None:
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
    """The documentation for this field or method has not yet been written.

    Underlying Java method: PApplet.points

    Parameters
    ----------

    coordinates: NDArray[(Any, Any), Float]
        missing variable description

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
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
    ``text_font()``, ``text_mode()``, ``text_size()``, ``text_leading()``.

    The ``push()`` and ``pop()`` functions were added with Processing 3.5. They can
    be used in place of ``push_matrix()``, ``pop_matrix()``, ``push_styles()``, and
    ``pop_styles()``. The difference is that ``push()`` and ``pop()`` control both
    the transformations (rotate, scale, translate) and the drawing styles at the
    same time.
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
    current style information. The ``push_style()`` and ``pop_style()`` functions
    can be embedded to provide more control (see the second example above for a
    demonstration.)
    """
    return _py5sketch.pop_style()


def print_camera() -> None:
    """Prints the current camera matrix to the Console (the text window at the bottom
    of Processing).

    Underlying Java method: PApplet.printCamera

    Notes
    -----

    Prints the current camera matrix to the Console (the text window at the bottom
    of Processing).
    """
    return _py5sketch.print_camera()


def print_matrix() -> None:
    """Prints the current matrix to the Console (the text window at the bottom of
    Processing).

    Underlying Java method: PApplet.printMatrix

    Notes
    -----

    Prints the current matrix to the Console (the text window at the bottom of
    Processing).
    """
    return _py5sketch.print_matrix()


def print_projection() -> None:
    """Prints the current projection matrix to the Console (the text window at the
    bottom of Processing).

    Underlying Java method: PApplet.printProjection

    Notes
    -----

    Prints the current projection matrix to the Console (the text window at the
    bottom of Processing).
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

    The ``push()`` and ``pop()`` functions were added with Processing 3.5. They can
    be used in place of ``push_matrix()``, ``pop_matrix()``, ``push_styles()``, and
    ``pop_styles()``. The difference is that ``push()`` and ``pop()`` control both
    the transformations (rotate, scale, translate) and the drawing styles at the
    same time.
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
    prefaced with a call to ``vertex()`` to set the first anchor point. This
    function must be used between ``begin_shape()`` and ``end_shape()`` and only
    when there is no MODE parameter specified to ``begin_shape()``. Using the 3D
    version requires rendering with P3D (see the Environment reference for more
    information).
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
    prefaced with a call to ``vertex()`` to set the first anchor point. This
    function must be used between ``begin_shape()`` and ``end_shape()`` and only
    when there is no MODE parameter specified to ``begin_shape()``. Using the 3D
    version requires rendering with P3D (see the Environment reference for more
    information).
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
    prefaced with a call to ``vertex()`` to set the first anchor point. This
    function must be used between ``begin_shape()`` and ``end_shape()`` and only
    when there is no MODE parameter specified to ``begin_shape()``. Using the 3D
    version requires rendering with P3D (see the Environment reference for more
    information).
    """
    return _py5sketch.quadratic_vertex(*args)


def quadratic_vertices(coordinates: NDArray[(Any, Any), Float], /) -> None:
    """The documentation for this field or method has not yet been written.

    Underlying Java method: PApplet.quadraticVertices

    Parameters
    ----------

    coordinates: NDArray[(Any, Any), Float]
        missing variable description

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
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

    The parameter must be written in ALL CAPS because Processing is a case-sensitive
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


def resume() -> None:
    """The documentation for this field or method has not yet been written.

    Underlying Java method: PApplet.resume

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return _py5sketch.resume()


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
    function with the ``z`` parameter requires using P3D as a parameter for
    ``size()``, as shown in the third example above. This function can be further
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
    function with the ``z`` parameter requires using P3D as a parameter for
    ``size()``, as shown in the third example above. This function can be further
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
    function with the ``z`` parameter requires using P3D as a parameter for
    ``size()``, as shown in the third example above. This function can be further
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
    function with the ``z`` parameter requires using P3D as a parameter for
    ``size()``, as shown in the third example above. This function can be further
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
    """Processing communicates with the clock on your computer.

    Underlying Java method: PApplet.second

    Notes
    -----

    Processing communicates with the clock on your computer. The ``second()``
    function returns the current second as a value from 0 - 59.
    """
    return Sketch.second()


@overload
def set_matrix(source: NDArray[(2, 3), Float], /) -> None:
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
def set_matrix(source: NDArray[(4, 4), Float], /) -> None:
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


def set_matrix(*args):
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

    Applies the shader specified by the parameters. It's compatible with the P2D and
    P3D renderers, but not with the default renderer.
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

    Applies the shader specified by the parameters. It's compatible with the P2D and
    P3D renderers, but not with the default renderer.
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

    Applies the shader specified by the parameters. It's compatible with the P2D and
    P3D renderers, but not with the default renderer.
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

    Draws shapes to the display window. Shapes must be in the sketch's "data"
    directory to load correctly. Select "Add file..." from the "Sketch" menu to add
    the shape. Processing currently works with SVG, OBJ, and custom-created shapes.
    The ``shape`` parameter specifies the shape to display and the coordinate
    parameters define the location of the shape from its upper-left corner. The
    shape is displayed at its original size unless the ``c`` and ``d`` parameters
    specify a different size. The ``shape_mode()`` function can be used to change
    the way these parameters are interpreted.
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
    parameter must be written in "ALL CAPS" because Processing is a case sensitive
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

    Sets the amount of gloss in the surface of shapes. Used in combination with
    ``ambient()``, ``specular()``, and ``emissive()`` in setting the material
    properties of shapes.
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
    In a program that has the ``setup()`` function, the ``size()`` function must be
    the first line of code inside ``setup()``, and the ``setup()`` function must
    appear in the code tab with the same name as your sketch folder.

    The built-in variables ``width`` and ``height`` are set by the parameters passed
    to this function. For example, running ``size(640, 480)`` will assign 640 to the
    ``width`` variable and 480 to the height ``variable``. If ``size()`` is not
    used, the window will be given a default size of 100 x 100 pixels.

    The ``size()`` function can only be used once inside a sketch, and it cannot be
    used for resizing.

    As of Processing 3, to run a sketch at the full dimensions of a screen, use the
    ``full_screen()`` function, rather than the older way of using
    ``size(display_width, display_height)``.

    The maximum width and height is limited by your operating system, and is usually
    the width and height of your actual screen. On some machines it may simply be
    the number of pixels on your current screen, meaning that a screen of 800 x 600
    could support ``size(1600, 300)``, since that is the same number of pixels. This
    varies widely, so you'll have to try different rendering modes and sizes until
    you get what you're looking for. If you need something larger, use
    ``create_graphics`` to create a non-visible drawing surface.

    The minimum width and height is around 100 pixels in each direction. This is the
    smallest that is supported across Windows, macOS, and Linux. We enforce the
    minimum size so that sketches will run identically on different machines.

    The ``renderer`` parameter selects which rendering engine to use. For example,
    if you will be drawing 3D shapes, use ``P3D``. In addition to the default
    renderer, other renderers are:

    ``P2D`` (Processing 2D): 2D graphics renderer that makes use of OpenGL-
    compatible graphics hardware.

    ``P3D`` (Processing 3D): 3D graphics renderer that makes use of OpenGL-
    compatible graphics hardware.

    ``FX2D`` (JavaFX 2D): A 2D renderer that uses JavaFX, which may be faster for
    some applications, but has some compatibility quirks.

    ``PDF``: The PDF renderer draws 2D graphics directly to an Acrobat PDF file.
    This produces excellent results when you need vector shapes for high-resolution
    output or printing. You must first use Import Library → PDF to make use of the
    library. More information can be found in the PDF library reference.

    ``SVG``: The SVG renderer draws 2D graphics directly to an SVG file. This is
    great for importing into other vector programs or using for digital fabrication.
    You must first use Import Library → SVG Export to make use of the library.

    As of Processing 3.0, to use variables as the parameters to ``size()`` function,
    place the ``size()`` function within the ``settings()`` function (instead of
    ``setup()``). There is more information about this on the ``settings()``
    reference page.
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
    In a program that has the ``setup()`` function, the ``size()`` function must be
    the first line of code inside ``setup()``, and the ``setup()`` function must
    appear in the code tab with the same name as your sketch folder.

    The built-in variables ``width`` and ``height`` are set by the parameters passed
    to this function. For example, running ``size(640, 480)`` will assign 640 to the
    ``width`` variable and 480 to the height ``variable``. If ``size()`` is not
    used, the window will be given a default size of 100 x 100 pixels.

    The ``size()`` function can only be used once inside a sketch, and it cannot be
    used for resizing.

    As of Processing 3, to run a sketch at the full dimensions of a screen, use the
    ``full_screen()`` function, rather than the older way of using
    ``size(display_width, display_height)``.

    The maximum width and height is limited by your operating system, and is usually
    the width and height of your actual screen. On some machines it may simply be
    the number of pixels on your current screen, meaning that a screen of 800 x 600
    could support ``size(1600, 300)``, since that is the same number of pixels. This
    varies widely, so you'll have to try different rendering modes and sizes until
    you get what you're looking for. If you need something larger, use
    ``create_graphics`` to create a non-visible drawing surface.

    The minimum width and height is around 100 pixels in each direction. This is the
    smallest that is supported across Windows, macOS, and Linux. We enforce the
    minimum size so that sketches will run identically on different machines.

    The ``renderer`` parameter selects which rendering engine to use. For example,
    if you will be drawing 3D shapes, use ``P3D``. In addition to the default
    renderer, other renderers are:

    ``P2D`` (Processing 2D): 2D graphics renderer that makes use of OpenGL-
    compatible graphics hardware.

    ``P3D`` (Processing 3D): 3D graphics renderer that makes use of OpenGL-
    compatible graphics hardware.

    ``FX2D`` (JavaFX 2D): A 2D renderer that uses JavaFX, which may be faster for
    some applications, but has some compatibility quirks.

    ``PDF``: The PDF renderer draws 2D graphics directly to an Acrobat PDF file.
    This produces excellent results when you need vector shapes for high-resolution
    output or printing. You must first use Import Library → PDF to make use of the
    library. More information can be found in the PDF library reference.

    ``SVG``: The SVG renderer draws 2D graphics directly to an SVG file. This is
    great for importing into other vector programs or using for digital fabrication.
    You must first use Import Library → SVG Export to make use of the library.

    As of Processing 3.0, to use variables as the parameters to ``size()`` function,
    place the ``size()`` function within the ``settings()`` function (instead of
    ``setup()``). There is more information about this on the ``settings()``
    reference page.
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
    In a program that has the ``setup()`` function, the ``size()`` function must be
    the first line of code inside ``setup()``, and the ``setup()`` function must
    appear in the code tab with the same name as your sketch folder.

    The built-in variables ``width`` and ``height`` are set by the parameters passed
    to this function. For example, running ``size(640, 480)`` will assign 640 to the
    ``width`` variable and 480 to the height ``variable``. If ``size()`` is not
    used, the window will be given a default size of 100 x 100 pixels.

    The ``size()`` function can only be used once inside a sketch, and it cannot be
    used for resizing.

    As of Processing 3, to run a sketch at the full dimensions of a screen, use the
    ``full_screen()`` function, rather than the older way of using
    ``size(display_width, display_height)``.

    The maximum width and height is limited by your operating system, and is usually
    the width and height of your actual screen. On some machines it may simply be
    the number of pixels on your current screen, meaning that a screen of 800 x 600
    could support ``size(1600, 300)``, since that is the same number of pixels. This
    varies widely, so you'll have to try different rendering modes and sizes until
    you get what you're looking for. If you need something larger, use
    ``create_graphics`` to create a non-visible drawing surface.

    The minimum width and height is around 100 pixels in each direction. This is the
    smallest that is supported across Windows, macOS, and Linux. We enforce the
    minimum size so that sketches will run identically on different machines.

    The ``renderer`` parameter selects which rendering engine to use. For example,
    if you will be drawing 3D shapes, use ``P3D``. In addition to the default
    renderer, other renderers are:

    ``P2D`` (Processing 2D): 2D graphics renderer that makes use of OpenGL-
    compatible graphics hardware.

    ``P3D`` (Processing 3D): 3D graphics renderer that makes use of OpenGL-
    compatible graphics hardware.

    ``FX2D`` (JavaFX 2D): A 2D renderer that uses JavaFX, which may be faster for
    some applications, but has some compatibility quirks.

    ``PDF``: The PDF renderer draws 2D graphics directly to an Acrobat PDF file.
    This produces excellent results when you need vector shapes for high-resolution
    output or printing. You must first use Import Library → PDF to make use of the
    library. More information can be found in the PDF library reference.

    ``SVG``: The SVG renderer draws 2D graphics directly to an SVG file. This is
    great for importing into other vector programs or using for digital fabrication.
    You must first use Import Library → SVG Export to make use of the library.

    As of Processing 3.0, to use variables as the parameters to ``size()`` function,
    place the ``size()`` function within the ``settings()`` function (instead of
    ``setup()``). There is more information about this on the ``settings()``
    reference page.
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
    In a program that has the ``setup()`` function, the ``size()`` function must be
    the first line of code inside ``setup()``, and the ``setup()`` function must
    appear in the code tab with the same name as your sketch folder.

    The built-in variables ``width`` and ``height`` are set by the parameters passed
    to this function. For example, running ``size(640, 480)`` will assign 640 to the
    ``width`` variable and 480 to the height ``variable``. If ``size()`` is not
    used, the window will be given a default size of 100 x 100 pixels.

    The ``size()`` function can only be used once inside a sketch, and it cannot be
    used for resizing.

    As of Processing 3, to run a sketch at the full dimensions of a screen, use the
    ``full_screen()`` function, rather than the older way of using
    ``size(display_width, display_height)``.

    The maximum width and height is limited by your operating system, and is usually
    the width and height of your actual screen. On some machines it may simply be
    the number of pixels on your current screen, meaning that a screen of 800 x 600
    could support ``size(1600, 300)``, since that is the same number of pixels. This
    varies widely, so you'll have to try different rendering modes and sizes until
    you get what you're looking for. If you need something larger, use
    ``create_graphics`` to create a non-visible drawing surface.

    The minimum width and height is around 100 pixels in each direction. This is the
    smallest that is supported across Windows, macOS, and Linux. We enforce the
    minimum size so that sketches will run identically on different machines.

    The ``renderer`` parameter selects which rendering engine to use. For example,
    if you will be drawing 3D shapes, use ``P3D``. In addition to the default
    renderer, other renderers are:

    ``P2D`` (Processing 2D): 2D graphics renderer that makes use of OpenGL-
    compatible graphics hardware.

    ``P3D`` (Processing 3D): 3D graphics renderer that makes use of OpenGL-
    compatible graphics hardware.

    ``FX2D`` (JavaFX 2D): A 2D renderer that uses JavaFX, which may be faster for
    some applications, but has some compatibility quirks.

    ``PDF``: The PDF renderer draws 2D graphics directly to an Acrobat PDF file.
    This produces excellent results when you need vector shapes for high-resolution
    output or printing. You must first use Import Library → PDF to make use of the
    library. More information can be found in the PDF library reference.

    ``SVG``: The SVG renderer draws 2D graphics directly to an SVG file. This is
    great for importing into other vector programs or using for digital fabrication.
    You must first use Import Library → SVG Export to make use of the library.

    As of Processing 3.0, to use variables as the parameters to ``size()`` function,
    place the ``size()`` function within the ``settings()`` function (instead of
    ``setup()``). There is more information about this on the ``settings()``
    reference page.
    """
    return _py5sketch.size(*args)


@overload
def sketch_path() -> str:
    """The documentation for this field or method has not yet been written.

    Underlying Java method: PApplet.sketchPath

    Methods
    -------

    You can use any of the following signatures:

     * sketch_path() -> str
     * sketch_path(where: str, /) -> str

    Parameters
    ----------

    where: str
        missing variable description

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    pass


@overload
def sketch_path(where: str, /) -> str:
    """The documentation for this field or method has not yet been written.

    Underlying Java method: PApplet.sketchPath

    Methods
    -------

    You can use any of the following signatures:

     * sketch_path() -> str
     * sketch_path(where: str, /) -> str

    Parameters
    ----------

    where: str
        missing variable description

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    pass


def sketch_path(*args):
    """The documentation for this field or method has not yet been written.

    Underlying Java method: PApplet.sketchPath

    Methods
    -------

    You can use any of the following signatures:

     * sketch_path() -> str
     * sketch_path(where: str, /) -> str

    Parameters
    ----------

    where: str
        missing variable description

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return _py5sketch.sketch_path(*args)


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
    diffuse light). Used in combination with ``emissive()``, ``ambient()``, and
    ``shininess()`` in setting the material properties of shapes.
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
    diffuse light). Used in combination with ``emissive()``, ``ambient()``, and
    ``shininess()`` in setting the material properties of shapes.
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
    diffuse light). Used in combination with ``emissive()``, ``ambient()``, and
    ``shininess()`` in setting the material properties of shapes.
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
    diffuse light). Used in combination with ``emissive()``, ``ambient()``, and
    ``shininess()`` in setting the material properties of shapes.
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


def start() -> None:
    """The documentation for this field or method has not yet been written.

    Underlying Java method: PApplet.start

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return _py5sketch.start()


def stop() -> None:
    """The documentation for this field or method has not yet been written.

    Underlying Java method: PApplet.stop

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return _py5sketch.stop()


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
    SQUARE, PROJECT, and ROUND. The default cap is ROUND.

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
    parameters MITER, BEVEL, and ROUND. The default joint is MITER.
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

    Using ``point()`` with strokeWeight(1) or smaller may draw nothing to the
    screen, depending on the graphics settings of the computer. Workarounds include
    setting the pixel using ``set()`` or drawing the point using either ``circle()``
    or ``square()``.
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
    return _py5sketch.text_width(*args)


def texture(image: Py5Image, /) -> None:
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
    which refers to the actual coordinates of the image. ``NORMAL`` refers to a
    normalized space of values ranging from 0 to 1. This function only works with
    the P2D and P3D renderers.

    With ``IMAGE``, if an image is 100 x 200 pixels, mapping the image onto the
    entire size of a quad would require the points (0,0) (100, 0) (100,200) (0,200).
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
    are CLAMP (the default behavior) and REPEAT. This function only works with the
    P2D and P3D renderers.
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
    from the screen. Using this function with the ``z`` parameter requires using P3D
    as a parameter in combination with size as shown in the above example.

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
def vertex(x: float, y: float, z: float, /) -> None:
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
def vertex(x: float, y: float, u: float, v: float, /) -> None:
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
def vertex(x: float, y: float, z: float, u: float, v: float, /) -> None:
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
def vertex(v: NDArray[(Any,), Float], /) -> None:
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


def vertex(*args):
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
    return _py5sketch.vertex(*args)


def vertices(coordinates: NDArray[(Any, Any), Float], /) -> None:
    """The documentation for this field or method has not yet been written.

    Underlying Java method: PApplet.vertices

    Parameters
    ----------

    coordinates: NDArray[(Any, Any), Float]
        missing variable description

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return _py5sketch.vertices(coordinates)


def year() -> int:
    """Processing communicates with the clock on your computer.

    Underlying Java method: PApplet.year

    Notes
    -----

    Processing communicates with the clock on your computer. The ``year()`` function
    returns the current year as an integer (2003, 2004, 2005, etc).
    """
    return Sketch.year()

##############################################################################
# module functions from data.py
##############################################################################


def load_json(filename: Union[str, Path], **kwargs: Dict[str, Any]) -> Any:
    """The documentation for this field or method has not yet been written.

    Parameters
    ----------

    filename: Union[str, Path]
        missing variable description

    kwargs: Dict[str, Any]
        missing variable description

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return Sketch.load_json(filename, **kwargs)


def save_json(json_data: Any,
              filename: Union[str,
                              Path],
              **kwargs: Dict[str,
                             Any]) -> None:
    """The documentation for this field or method has not yet been written.

    Parameters
    ----------

    filename: Union[str, Path]
        missing variable description

    json_data: Any
        missing variable description

    kwargs: Dict[str, Any]
        missing variable description

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return Sketch.save_json(json_data, filename, **kwargs)


def parse_json(serialized_json: Any, **kwargs: Dict[str, Any]) -> Any:
    """The documentation for this field or method has not yet been written.

    Parameters
    ----------

    kwargs: Dict[str, Any]
        missing variable description

    serialized_json: Any
        missing variable description

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return Sketch.parse_json(serialized_json, **kwargs)


SIMPLEX_NOISE = 1
PERLIN_NOISE = 2
##############################################################################
# module functions from math.py
##############################################################################


def sin(angle: float) -> float:
    """The documentation for this field or method has not yet been written.

    Parameters
    ----------

    angle: float
        missing variable description

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return Sketch.sin(angle)


def cos(angle: float) -> float:
    """The documentation for this field or method has not yet been written.

    Parameters
    ----------

    angle: float
        missing variable description

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return Sketch.cos(angle)


def tan(angle: float) -> float:
    """The documentation for this field or method has not yet been written.

    Parameters
    ----------

    angle: float
        missing variable description

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return Sketch.tan(angle)


def asin(value: float) -> float:
    """The documentation for this field or method has not yet been written.

    Parameters
    ----------

    value: float
        missing variable description

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return Sketch.asin(value)


def acos(value: float) -> float:
    """The documentation for this field or method has not yet been written.

    Parameters
    ----------

    value: float
        missing variable description

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return Sketch.acos(value)


def atan(value: float) -> float:
    """The documentation for this field or method has not yet been written.

    Parameters
    ----------

    value: float
        missing variable description

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return Sketch.atan(value)


def atan2(y: float, x: float) -> float:
    """The documentation for this field or method has not yet been written.

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
    return Sketch.atan2(y, x)


def degrees(radians: float) -> float:
    """The documentation for this field or method has not yet been written.

    Parameters
    ----------

    radians: float
        missing variable description

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return Sketch.degrees(radians)


def radians(degrees: float) -> float:
    """The documentation for this field or method has not yet been written.

    Parameters
    ----------

    degrees: float
        missing variable description

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return Sketch.radians(degrees)


def constrain(amt: float, low: float, high: float) -> float:
    """The documentation for this field or method has not yet been written.

    Parameters
    ----------

    amt: float
        missing variable description

    high: float
        missing variable description

    low: float
        missing variable description

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return Sketch.constrain(amt, low, high)


def remap(
        value: float,
        start1: float,
        stop1: float,
        start2: float,
        stop2: float) -> float:
    """The documentation for this field or method has not yet been written.

    Parameters
    ----------

    start1: float
        missing variable description

    start2: float
        missing variable description

    stop1: float
        missing variable description

    stop2: float
        missing variable description

    value: float
        missing variable description

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return Sketch.remap(value, start1, stop1, start2, stop2)


def dist(*args: float) -> float:
    """The documentation for this field or method has not yet been written.

    Parameters
    ----------

    args: float
        missing variable description

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return Sketch.dist(*args)


def lerp(start: float, stop: float, amt: float) -> float:
    """The documentation for this field or method has not yet been written.

    Parameters
    ----------

    amt: float
        missing variable description

    start: float
        missing variable description

    stop: float
        missing variable description

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return Sketch.lerp(start, stop, amt)


def mag(*args: float) -> float:
    """The documentation for this field or method has not yet been written.

    Parameters
    ----------

    args: float
        missing variable description

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return Sketch.mag(*args)


def norm(value: float, start: float, stop: float) -> float:
    """The documentation for this field or method has not yet been written.

    Parameters
    ----------

    start: float
        missing variable description

    stop: float
        missing variable description

    value: float
        missing variable description

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return Sketch.norm(value, start, stop)


def sq(value: float) -> float:
    """The documentation for this field or method has not yet been written.

    Parameters
    ----------

    value: float
        missing variable description

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return Sketch.sq(value)


def sqrt(value: float) -> Union[float, complex]:
    """The documentation for this field or method has not yet been written.

    Parameters
    ----------

    value: float
        missing variable description

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return Sketch.sqrt(value)


def floor(value: float) -> int:
    """The documentation for this field or method has not yet been written.

    Parameters
    ----------

    value: float
        missing variable description

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return Sketch.floor(value)


def ceil(value: float) -> int:
    """The documentation for this field or method has not yet been written.

    Parameters
    ----------

    value: float
        missing variable description

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return Sketch.ceil(value)


def exp(value: float) -> float:
    """The documentation for this field or method has not yet been written.

    Parameters
    ----------

    value: float
        missing variable description

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return Sketch.exp(value)


def log(value: float) -> float:
    """The documentation for this field or method has not yet been written.

    Parameters
    ----------

    value: float
        missing variable description

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return Sketch.log(value)


@overload
def random(high: float) -> float:
    """The documentation for this field or method has not yet been written.

    Methods
    -------

    You can use any of the following signatures:

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

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    pass


@overload
def random(low: float, high: float) -> float:
    """The documentation for this field or method has not yet been written.

    Methods
    -------

    You can use any of the following signatures:

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

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    pass


def random_seed(seed: int) -> None:
    """The documentation for this field or method has not yet been written.

    Parameters
    ----------

    seed: int
        seed value

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return Sketch.random_seed(seed)


def random(*args: float) -> float:
    """The documentation for this field or method has not yet been written.

    Methods
    -------

    You can use any of the following signatures:

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

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return Sketch.random(*args)


def random_gaussian() -> float:
    """The documentation for this field or method has not yet been written.

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return Sketch.random_gaussian()


@overload
def noise(x, **kwargs) -> float:
    """The documentation for this field or method has not yet been written.

    Methods
    -------

    You can use any of the following signatures:

     * noise(x, **kwargs) -> float
     * noise(x, y, **kwargs) -> float
     * noise(x, y, z, **kwargs) -> float
     * noise(x, y, z, w, **kwargs) -> float

    Parameters
    ----------

    kwargs
        missing variable description

    w
        missing variable description

    x
        x-coordinate in noise space

    y
        y-coordinate in noise space

    z
        z-coordinate in noise space

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    pass


@overload
def noise(x, y, **kwargs) -> float:
    """The documentation for this field or method has not yet been written.

    Methods
    -------

    You can use any of the following signatures:

     * noise(x, **kwargs) -> float
     * noise(x, y, **kwargs) -> float
     * noise(x, y, z, **kwargs) -> float
     * noise(x, y, z, w, **kwargs) -> float

    Parameters
    ----------

    kwargs
        missing variable description

    w
        missing variable description

    x
        x-coordinate in noise space

    y
        y-coordinate in noise space

    z
        z-coordinate in noise space

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    pass


@overload
def noise(x, y, z, **kwargs) -> float:
    """The documentation for this field or method has not yet been written.

    Methods
    -------

    You can use any of the following signatures:

     * noise(x, **kwargs) -> float
     * noise(x, y, **kwargs) -> float
     * noise(x, y, z, **kwargs) -> float
     * noise(x, y, z, w, **kwargs) -> float

    Parameters
    ----------

    kwargs
        missing variable description

    w
        missing variable description

    x
        x-coordinate in noise space

    y
        y-coordinate in noise space

    z
        z-coordinate in noise space

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    pass


@overload
def noise(x, y, z, w, **kwargs) -> float:
    """The documentation for this field or method has not yet been written.

    Methods
    -------

    You can use any of the following signatures:

     * noise(x, **kwargs) -> float
     * noise(x, y, **kwargs) -> float
     * noise(x, y, z, **kwargs) -> float
     * noise(x, y, z, w, **kwargs) -> float

    Parameters
    ----------

    kwargs
        missing variable description

    w
        missing variable description

    x
        x-coordinate in noise space

    y
        y-coordinate in noise space

    z
        z-coordinate in noise space

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    pass


def noise(*args, **kwargs) -> float:
    """The documentation for this field or method has not yet been written.

    Methods
    -------

    You can use any of the following signatures:

     * noise(x, **kwargs) -> float
     * noise(x, y, **kwargs) -> float
     * noise(x, y, z, **kwargs) -> float
     * noise(x, y, z, w, **kwargs) -> float

    Parameters
    ----------

    kwargs
        missing variable description

    w
        missing variable description

    x
        x-coordinate in noise space

    y
        y-coordinate in noise space

    z
        z-coordinate in noise space

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return Sketch.noise(*args, **kwargs)


def noise_mode(mode: int) -> None:
    """The documentation for this field or method has not yet been written.

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
    return Sketch.noise_mode(mode)


def noise_detail(octaves: float = None, persistence: float = None,
                 lacunarity: float = None) -> None:
    """The documentation for this field or method has not yet been written.

    Parameters
    ----------

    lacunarity: float = None
        missing variable description

    octaves: float = None
        missing variable description

    persistence: float = None
        missing variable description

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return Sketch.noise_detail(
        octaves=octaves,
        persistence=persistence,
        lacunarity=lacunarity)


def noise_seed(seed: float) -> None:
    """The documentation for this field or method has not yet been written.

    Parameters
    ----------

    seed: float
        seed value

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return Sketch.noise_seed(seed)

##############################################################################
# module functions from pixels.py
##############################################################################


def load_np_pixels() -> None:
    """The documentation for this field or method has not yet been written.

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return _py5sketch.load_np_pixels()


def update_np_pixels() -> None:
    """The documentation for this field or method has not yet been written.

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return _py5sketch.update_np_pixels()


np_pixels: np.ndarray = None


def set_np_pixels(array: np.ndarray, bands: str = 'ARGB') -> None:
    """The documentation for this field or method has not yet been written.

    Parameters
    ----------

    array: np.ndarray
        missing variable description

    bands: str = 'ARGB'
        missing variable description

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return _py5sketch.set_np_pixels(array, bands=bands)


def save(filename: Union[str,
                         Path],
         format: str = None,
         drop_alpha: bool = True,
         use_thread: bool = True,
         **params) -> None:
    """The documentation for this field or method has not yet been written.

    Parameters
    ----------

    drop_alpha: bool = True
        missing variable description

    filename: Union[str, Path]
        missing variable description

    format: str = None
        missing variable description

    params
        missing variable description

    use_thread: bool = True
        missing variable description

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return _py5sketch.save(
        filename,
        format=format,
        drop_alpha=drop_alpha,
        use_thread=use_thread,
        **params)

##############################################################################
# module functions from threads.py
##############################################################################


def launch_thread(f: Callable, name: str = None, daemon: bool = True,
                  args: Tuple = None, kwargs: Dict = None) -> str:
    """The documentation for this field or method has not yet been written.

    Parameters
    ----------

    args: Tuple = None
        missing variable description

    daemon: bool = True
        missing variable description

    f: Callable
        missing variable description

    kwargs: Dict = None
        missing variable description

    name: str = None
        missing variable description

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return _py5sketch.launch_thread(
        f, name=name, daemon=daemon, args=args, kwargs=kwargs)


def launch_promise_thread(
        f: Callable,
        name: str = None,
        daemon: bool = True,
        args: Tuple = None,
        kwargs: Dict = None) -> Py5Promise:
    """The documentation for this field or method has not yet been written.

    Parameters
    ----------

    args: Tuple = None
        missing variable description

    daemon: bool = True
        missing variable description

    f: Callable
        missing variable description

    kwargs: Dict = None
        missing variable description

    name: str = None
        missing variable description

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return _py5sketch.launch_promise_thread(
        f, name=name, daemon=daemon, args=args, kwargs=kwargs)


def launch_repeating_thread(f: Callable, name: str = None,
                            time_delay: float = 0, daemon: bool = True,
                            args: Tuple = None, kwargs: Dict = None) -> str:
    """The documentation for this field or method has not yet been written.

    Parameters
    ----------

    args: Tuple = None
        missing variable description

    daemon: bool = True
        missing variable description

    f: Callable
        missing variable description

    kwargs: Dict = None
        missing variable description

    name: str = None
        missing variable description

    time_delay: float = 0
        missing variable description

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return _py5sketch.launch_repeating_thread(
        f,
        name=name,
        time_delay=time_delay,
        daemon=daemon,
        args=args,
        kwargs=kwargs)


def has_thread(name: str) -> None:
    """The documentation for this field or method has not yet been written.

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
    return _py5sketch.has_thread(name)


def stop_thread(name: str, wait: bool = False) -> None:
    """The documentation for this field or method has not yet been written.

    Parameters
    ----------

    name: str
        missing variable description

    wait: bool = False
        missing variable description

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return _py5sketch.stop_thread(name, wait=wait)


def stop_all_threads(wait: bool = False) -> None:
    """The documentation for this field or method has not yet been written.

    Parameters
    ----------

    wait: bool = False
        missing variable description

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return _py5sketch.stop_all_threads(wait=wait)


def list_threads() -> None:
    """The documentation for this field or method has not yet been written.

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return _py5sketch.list_threads()

##############################################################################
# module functions from sketch.py
##############################################################################


is_ready: bool = None
is_running: bool = None
is_dead: bool = None
is_dead_from_error: bool = None


def hot_reload_draw(draw: Callable) -> None:
    """The documentation for this field or method has not yet been written.

    Parameters
    ----------

    draw: Callable
        missing variable description

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return _py5sketch.hot_reload_draw(draw)


def profile_functions(function_names: List[str]) -> None:
    """The documentation for this field or method has not yet been written.

    Parameters
    ----------

    function_names: List[str]
        missing variable description

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return _py5sketch.profile_functions(function_names)


def profile_draw() -> None:
    """The documentation for this field or method has not yet been written.

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return _py5sketch.profile_draw()


def print_line_profiler_stats() -> None:
    """The documentation for this field or method has not yet been written.

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return _py5sketch.print_line_profiler_stats()


def save_frame(filename: Union[str,
                               Path],
               format: str = None,
               drop_alpha: bool = True,
               use_thread: bool = True,
               **params) -> None:
    """The documentation for this field or method has not yet been written.

    Parameters
    ----------

    drop_alpha: bool = True
        missing variable description

    filename: Union[str, Path]
        missing variable description

    format: str = None
        missing variable description

    params
        missing variable description

    use_thread: bool = True
        missing variable description

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return _py5sketch.save_frame(
        filename,
        format=format,
        drop_alpha=drop_alpha,
        use_thread=use_thread,
        **params)


def create_image_from_numpy(
        numpy_image: NumpyImageArray,
        dst: Py5Image = None) -> Py5Image:
    """The documentation for this field or method has not yet been written.

    Parameters
    ----------

    dst: Py5Image = None
        missing variable description

    numpy_image: NumpyImageArray
        missing variable description

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return _py5sketch.create_image_from_numpy(numpy_image, dst=dst)


def convert_image(obj: Any, dst: Py5Image = None) -> Py5Image:
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

    This method is comparable to :doc:`load_image`, except instead of reading image
    files from disk, it reads image data from other Python objects.

    Passed image object types must be known to py5's builtin image conversion tools.
    New object types and functions to effect conversions can be registered with
    :doc:`register_image_conversion`.

    The caller can optionally pass an existing Py5Image object to put the converted
    image into. This can have performance benefits in code that would otherwise
    continuously create new Py5Image objects. The converted image width and height
    must match that of the recycled Py5Image object.
    """
    return _py5sketch.convert_image(obj, dst=dst)


def load_image(filename: Union[str, Path], dst: Py5Image = None) -> Py5Image:
    """The documentation for this field or method has not yet been written.

    Parameters
    ----------

    dst: Py5Image = None
        missing variable description

    filename: Union[str, Path]
        missing variable description

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return _py5sketch.load_image(filename, dst=dst)


def request_image(filename: Union[str, Path]) -> Py5Promise:
    """The documentation for this field or method has not yet been written.

    Parameters
    ----------

    filename: Union[str, Path]
        missing variable description

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """
    return _py5sketch.request_image(filename)


def run_sketch(block: bool = None,
               py5_options: List = None,
               sketch_args: List = None) -> None:
    """Run the sketch.

    Parameters
    ----------

    block: bool = None
        method returns immediately (False) or blocks until sketch exits (True)

    py5_options: List = None
        command line arguments to pass to Processing as arguments

    sketch_args: List = None
        command line arguments that become Sketch arguments

    Notes
    -----

    Run the sketch. Code in the ``settings``, ``setup``, and ``draw`` functions will
    be used to actualize your sketch.

    Use the ``block`` parameter to specify if the call to ``run_sketch`` should
    return immediately or block until the sketch exits. If the ``block`` parameter
    is not specified, py5 will first attempt to determine if the sketch is running
    in a Jupyter Notebook or an IPython shell. If it is, ``block`` will default to
    ``False``, and ``True`` otherwise.

    A list of strings passed to ``py5_options`` will be passed to the Processing
    PApplet class as arguments to specify characteristics such as the window's
    location on the screen. A list of strings passed to ``sketch_args`` will be
    available to a running sketch using :doc:`args`. For example, if you launch a
    sketch with ``py5.run_sketch(py5_options=['--location=400,300', '--display=1'],
    sketch_args=['py5 is awesome'])``, the sketch window will appear at location
    (400, 300) on your second monitor and ``py5.args`` will equal ``['py5 is
    awesome']``."""
    # Before running the sketch, delete the module fields that need to be kept
    # uptodate. This will allow the module `__getattr__` function return the
    # proper values.
    if block is None:
        block = not _in_ipython_session

    try:

        global args
        del args
        global display_height
        del display_height
        global display_width
        del display_width
        global finished
        del finished
        global focused
        del focused
        global frame_count
        del frame_count
        global height
        del height
        global is_dead
        del is_dead
        global is_dead_from_error
        del is_dead_from_error
        global is_ready
        del is_ready
        global is_running
        del is_running
        global java_platform
        del java_platform
        global java_version
        del java_version
        global java_version_name
        del java_version_name
        global key
        del key
        global key_code
        del key_code
        global mouse_button
        del mouse_button
        global mouse_x
        del mouse_x
        global mouse_y
        del mouse_y
        global np_pixels
        del np_pixels
        global pixel_height
        del pixel_height
        global pixel_width
        del pixel_width
        global pixels
        del pixels
        global pmouse_x
        del pmouse_x
        global pmouse_y
        del pmouse_y
        global width
        del width
    except NameError:
        # these variables might have already been removed
        pass

    function_dict = inspect.stack()[1].frame.f_locals
    methods = dict([(e, function_dict[e])
                    for e in reference.METHODS if e in function_dict and callable(function_dict[e])])

    if not set(methods.keys()) & set(['settings', 'setup', 'draw']):
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

    _py5sketch._run_sketch(methods, block, py5_options, sketch_args)


def get_current_sketch() -> Sketch:
    """The documentation for this field or method has not yet been written.

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/."""
    return _py5sketch


def reset_py5() -> None:
    """The documentation for this field or method has not yet been written.

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/."""
    global _py5sketch
    _py5sketch = Sketch()


def prune_tracebacks(prune: bool) -> None:
    """The documentation for this field or method has not yet been written.

    Parameters
    ----------

    prune: bool
        missing variable description

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/."""
    from . import methods
    methods._prune_tracebacks = prune


def set_stackprinter_style(style: str) -> None:
    """The documentation for this field or method has not yet been written.

    Parameters
    ----------

    style: str
        missing variable description

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/."""
    from . import methods
    methods._stackprinter_style = style


def __getattr__(name):
    if hasattr(_py5sketch, name):
        return getattr(_py5sketch, name)
    else:
        raise AttributeError('py5 has no function or field named ' + name)


def __dir__():
    return reference.PY5_DIR_STR


__all__ = reference.PY5_ALL_STR
