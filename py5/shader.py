# -*- coding: utf-8 -*-
# *** FORMAT PARAMS ***
import functools
from typing import overload, List, Any  # noqa
from nptyping import NDArray, Float  # noqa

import numpy as np  # noqa

from .base import Py5Base
from .image import Py5Image  # noqa
from jpype.types import JException, JArray, JBoolean, JInt, JFloat  # noqa
from .pmath import _numpy_to_pvector, _numpy_to_pmatrix2d, _numpy_to_pmatrix3d  # noqa


def _return_py5shader(f):
    @functools.wraps(f)
    def decorated(self_, *args):
        return Py5Shader(f(self_, *args))
    return decorated


def _load_py5shader(f):
    @functools.wraps(f)
    def decorated(self_, *args):
        try:
            return Py5Shader(f(self_, *args))
        except JException as e:
            msg = e.message()
            if msg == 'None':
                msg = 'shader file cannot be found'
        raise RuntimeError('cannot load shader file ' +
                           str(args[0]) + '. error message: ' + msg)
    return decorated


def _py5shader_set_wrapper(f):
    @functools.wraps(f)
    def decorated(self_, name, *args):
        args = list(args)
        if isinstance(args[0], np.ndarray):
            array = args[0]
            if array.shape in [(2,), (3,)]:
                args[0] = _numpy_to_pvector(array)
            elif array.shape == (2, 3):
                args[0] = _numpy_to_pmatrix2d(array)
            elif array.shape == (4, 4):
                args[0] = _numpy_to_pmatrix3d(array)
        else:
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
        return f(self_, name, *tuple(args))
    return decorated


class Py5Shader(Py5Base):

    def __init__(self, pshader):
        self._instance = pshader
        super().__init__(instance=pshader)

    @overload
    def set(self, name: str, x: bool, /) -> None:
        """Sets the uniform variables inside the shader to modify the effect while the
        program is running.

        Notes
        -----

        Sets the uniform variables inside the shader to modify the effect while the
        program is running.
"""
        pass

    @overload
    def set(self, name: str, x: bool, y: bool, /) -> None:
        """Sets the uniform variables inside the shader to modify the effect while the
        program is running.

        Notes
        -----

        Sets the uniform variables inside the shader to modify the effect while the
        program is running.
"""
        pass

    @overload
    def set(self, name: str, x: bool, y: bool, z: bool, /) -> None:
        """Sets the uniform variables inside the shader to modify the effect while the
        program is running.

        Notes
        -----

        Sets the uniform variables inside the shader to modify the effect while the
        program is running.
"""
        pass

    @overload
    def set(self, name: str, x: bool, y: bool, z: bool, w: bool, /) -> None:
        """Sets the uniform variables inside the shader to modify the effect while the
        program is running.

        Notes
        -----

        Sets the uniform variables inside the shader to modify the effect while the
        program is running.
"""
        pass

    @overload
    def set(self, name: str, vec: JArray(JBoolean), /) -> None:
        """Sets the uniform variables inside the shader to modify the effect while the
        program is running.

        Notes
        -----

        Sets the uniform variables inside the shader to modify the effect while the
        program is running.
"""
        pass

    @overload
    def set(self, name: str, boolvec: JArray(
            JBoolean), ncoords: int, /) -> None:
        """Sets the uniform variables inside the shader to modify the effect while the
        program is running.

        Notes
        -----

        Sets the uniform variables inside the shader to modify the effect while the
        program is running.
"""
        pass

    @overload
    def set(self, name: str, x: float, /) -> None:
        """Sets the uniform variables inside the shader to modify the effect while the
        program is running.

        Notes
        -----

        Sets the uniform variables inside the shader to modify the effect while the
        program is running.
"""
        pass

    @overload
    def set(self, name: str, x: float, y: float, /) -> None:
        """Sets the uniform variables inside the shader to modify the effect while the
        program is running.

        Notes
        -----

        Sets the uniform variables inside the shader to modify the effect while the
        program is running.
"""
        pass

    @overload
    def set(self, name: str, x: float, y: float, z: float, /) -> None:
        """Sets the uniform variables inside the shader to modify the effect while the
        program is running.

        Notes
        -----

        Sets the uniform variables inside the shader to modify the effect while the
        program is running.
"""
        pass

    @overload
    def set(self, name: str, x: float, y: float,
            z: float, w: float, /) -> None:
        """Sets the uniform variables inside the shader to modify the effect while the
        program is running.

        Notes
        -----

        Sets the uniform variables inside the shader to modify the effect while the
        program is running.
"""
        pass

    @overload
    def set(self, name: str, vec: NDArray[(Any,), Float], /) -> None:
        """Sets the uniform variables inside the shader to modify the effect while the
        program is running.

        Notes
        -----

        Sets the uniform variables inside the shader to modify the effect while the
        program is running.
"""
        pass

    @overload
    def set(self, name: str, vec: NDArray[(
            Any,), Float], ncoords: int, /) -> None:
        """Sets the uniform variables inside the shader to modify the effect while the
        program is running.

        Notes
        -----

        Sets the uniform variables inside the shader to modify the effect while the
        program is running.
"""
        pass

    @overload
    def set(self, name: str, x: int, /) -> None:
        """Sets the uniform variables inside the shader to modify the effect while the
        program is running.

        Notes
        -----

        Sets the uniform variables inside the shader to modify the effect while the
        program is running.
"""
        pass

    @overload
    def set(self, name: str, x: int, y: int, /) -> None:
        """Sets the uniform variables inside the shader to modify the effect while the
        program is running.

        Notes
        -----

        Sets the uniform variables inside the shader to modify the effect while the
        program is running.
"""
        pass

    @overload
    def set(self, name: str, x: int, y: int, z: int, /) -> None:
        """Sets the uniform variables inside the shader to modify the effect while the
        program is running.

        Notes
        -----

        Sets the uniform variables inside the shader to modify the effect while the
        program is running.
"""
        pass

    @overload
    def set(self, name: str, x: int, y: int, z: int, w: int, /) -> None:
        """Sets the uniform variables inside the shader to modify the effect while the
        program is running.

        Notes
        -----

        Sets the uniform variables inside the shader to modify the effect while the
        program is running.
"""
        pass

    @overload
    def set(self, name: str, vec: JArray(JInt), /) -> None:
        """Sets the uniform variables inside the shader to modify the effect while the
        program is running.

        Notes
        -----

        Sets the uniform variables inside the shader to modify the effect while the
        program is running.
"""
        pass

    @overload
    def set(self, name: str, vec: JArray(JInt), ncoords: int, /) -> None:
        """Sets the uniform variables inside the shader to modify the effect while the
        program is running.

        Notes
        -----

        Sets the uniform variables inside the shader to modify the effect while the
        program is running.
"""
        pass

    @overload
    def set(self, name: str, tex: Py5Image, /) -> None:
        """Sets the uniform variables inside the shader to modify the effect while the
        program is running.

        Notes
        -----

        Sets the uniform variables inside the shader to modify the effect while the
        program is running.
"""
        pass

    @overload
    def set(self, name: str, mat: NDArray[(2, 3), Float], /) -> None:
        """Sets the uniform variables inside the shader to modify the effect while the
        program is running.

        Notes
        -----

        Sets the uniform variables inside the shader to modify the effect while the
        program is running.
"""
        pass

    @overload
    def set(self, name: str, mat: NDArray[(4, 4), Float], /) -> None:
        """Sets the uniform variables inside the shader to modify the effect while the
        program is running.

        Notes
        -----

        Sets the uniform variables inside the shader to modify the effect while the
        program is running.
"""
        pass

    @overload
    def set(self, name: str, mat: NDArray[(
            4, 4), Float], use3x3: bool, /) -> None:
        """Sets the uniform variables inside the shader to modify the effect while the
        program is running.

        Notes
        -----

        Sets the uniform variables inside the shader to modify the effect while the
        program is running.
"""
        pass

    @_py5shader_set_wrapper
    def set(self, *args):
        """Sets the uniform variables inside the shader to modify the effect while the
        program is running.

        Notes
        -----

        Sets the uniform variables inside the shader to modify the effect while the
        program is running.
"""
        return self._instance.set(*args)
