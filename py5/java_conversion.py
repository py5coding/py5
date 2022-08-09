# *****************************************************************************
#
#   Part of the py5 library
#   Copyright (C) 2020-2022 Jim Schmitz
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
from jpype import JClass, JArray, _jcustomizer

from .sketch import _Sketch, Sketch, Py5Graphics, Py5Image, Py5Font, Py5Shape, Py5Shader, Py5KeyEvent, Py5MouseEvent
from .pmath import _py5vector_to_pvector_converter, _numpy_to_pvector_converter, _numpy_to_pmatrix_converter
from .vector import Py5Vector


JCONVERSION_CLASS_MAP = [
    ("processing.core.PImage", Py5Image),
    ("processing.core.PImage", Py5Graphics),
    ("processing.core.PGraphics", Py5Graphics),
    ("processing.core.PFont", Py5Font),
    ("processing.core.PShape", Py5Shape),
    ("processing.opengl.PShader", Py5Shader),
    ("processing.event.Event", Py5KeyEvent),
    ("processing.event.KeyEvent", Py5KeyEvent),
    ("processing.event.Event", Py5MouseEvent),
    ("processing.event.MouseEvent", Py5MouseEvent),
    ("processing.core.PApplet", Sketch),
    ("py5.core.Sketch", Sketch),
]

PROCESSING_TO_PY5_CLASS_MAP = [
    (JClass("processing.core.PGraphics"), Py5Graphics),
    (JClass("processing.core.PImage"), Py5Image),
    (JClass("processing.core.PFont"), Py5Font),
    (JClass("processing.core.PShape"), Py5Shape),
    (JClass("processing.opengl.PShader"), Py5Shader),
    (JClass("processing.event.KeyEvent"), Py5KeyEvent),
    (JClass("processing.event.MouseEvent"), Py5MouseEvent),
]

_String = JClass("java.lang.String")


def init_jpype_converters():

    def convert(jcls, obj):
        return obj._instance

    for javaname, cls_ in JCONVERSION_CLASS_MAP:
        _jcustomizer.JConversion(javaname, cls_)(convert)

    _jcustomizer.JConversion(
        'processing.core.PVector',
        Py5Vector)(_py5vector_to_pvector_converter)
    _jcustomizer.JConversion(
        'processing.core.PVector',
        np.ndarray)(_numpy_to_pvector_converter)
    _jcustomizer.JConversion(
        'processing.core.PMatrix',
        np.ndarray)(_numpy_to_pmatrix_converter)


def convert_to_python_types(params):
    for p in params:
        for jclass, py5class in PROCESSING_TO_PY5_CLASS_MAP:
            if isinstance(p, jclass):
                yield py5class(p)
                break
        else:
            if isinstance(p, _String):
                yield str(p)
            elif isinstance(p, _Sketch):
                yield Sketch(_instance=p)
            elif isinstance(p, JArray):
                yield np.asarray(p)
            else:
                yield p
