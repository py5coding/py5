from jpype import _jcustomizer

from .sketch import Sketch, Py5Graphics, Py5Image, Py5Font, Py5Shape, Py5Shader


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
