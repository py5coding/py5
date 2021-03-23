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
import numpy as np
from jpype import _jcustomizer

from .sketch import Sketch, Py5Graphics, Py5Image, Py5Font, Py5Shape, Py5Shader
from .pmath import _numpy_to_pvector_converter, _numpy_to_pmatrix_converter


def init_jpype_converters():
    data = [
        ("processing.core.PImage", Py5Image),
        ("processing.core.PImage", Py5Graphics),
        ("processing.core.PFont", Py5Font),
        ("processing.core.PShape", Py5Shape),
        ("processing.opengl.PShader", Py5Shader),
        ("processing.core.PApplet", Sketch),
    ]

    def convert(jcls, obj):
        return obj._instance

    for javaname, cls_ in data:
        _jcustomizer.JConversion(javaname, cls_)(convert)

    _jcustomizer.JConversion(
        'processing.core.PVector',
        np.ndarray)(_numpy_to_pvector_converter)
    _jcustomizer.JConversion(
        'processing.core.PMatrix',
        np.ndarray)(_numpy_to_pmatrix_converter)
