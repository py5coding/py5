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
import functools
from typing import overload, List, Any  # noqa
from nptyping import NDArray, Float, Int  # noqa

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
        if isinstance(args[0], np.ndarray):
            array = args[0]
            if array.shape in [(2,), (3,)]:
                args = _numpy_to_pvector(array), *args[1:]
            elif array.shape == (2, 3):
                args = _numpy_to_pmatrix2d(array), *args[1:]
            elif array.shape == (4, 4):
                args = _numpy_to_pmatrix3d(array), *args[1:]
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
        return f(self_, name, *args)
    return decorated


class Py5Shader(Py5Base):
    """This class encapsulates a GLSL shader program, including a vertex and a fragment
    shader.

    Underlying Java class: PShader.PShader

    Notes
    -----

    This class encapsulates a GLSL shader program, including a vertex and a fragment
    shader. It's compatible with the ``P2D`` and ``P3D`` renderers, but not with the
    default renderer. Use the ``load_shader()`` function to load your shader code
    and create ``Py5Shader`` objects.
    """

    def __init__(self, pshader):
        self._instance = pshader
        super().__init__(instance=pshader)

    @overload
    def set(self, name: str, x: bool, /) -> None:
        """Sets the uniform variables inside the shader to modify the effect while the
        program is running.

        Underlying Java method: PShader.set

        Methods
        -------

        You can use any of the following signatures:

         * set(name: str, boolvec: JArray(JBoolean), ncoords: int, /) -> None
         * set(name: str, mat: NDArray[(2, 3), Float], /) -> None
         * set(name: str, mat: NDArray[(4, 4), Float], /) -> None
         * set(name: str, mat: NDArray[(4, 4), Float], use3x3: bool, /) -> None
         * set(name: str, tex: Py5Image, /) -> None
         * set(name: str, vec: JArray(JBoolean), /) -> None
         * set(name: str, vec: NDArray[(Any,), Float], /) -> None
         * set(name: str, vec: NDArray[(Any,), Float], ncoords: int, /) -> None
         * set(name: str, vec: NDArray[(Any,), Int], /) -> None
         * set(name: str, vec: NDArray[(Any,), Int], ncoords: int, /) -> None
         * set(name: str, x: bool, /) -> None
         * set(name: str, x: bool, y: bool, /) -> None
         * set(name: str, x: bool, y: bool, z: bool, /) -> None
         * set(name: str, x: bool, y: bool, z: bool, w: bool, /) -> None
         * set(name: str, x: float, /) -> None
         * set(name: str, x: float, y: float, /) -> None
         * set(name: str, x: float, y: float, z: float, /) -> None
         * set(name: str, x: float, y: float, z: float, w: float, /) -> None
         * set(name: str, x: int, /) -> None
         * set(name: str, x: int, y: int, /) -> None
         * set(name: str, x: int, y: int, z: int, /) -> None
         * set(name: str, x: int, y: int, z: int, w: int, /) -> None

        Parameters
        ----------

        boolvec: JArray(JBoolean)
            modifies all the components of an array/vector uniform variable

        mat: NDArray[(2, 3), Float]
            numpy array of values

        mat: NDArray[(4, 4), Float]
            numpy array of values

        name: str
            the name of the uniform variable to modify

        ncoords: int
            number of coordinates per element, max 4

        tex: Py5Image
            sets the sampler uniform variable to read from this image texture

        use3x3: bool
            enforces the numpy array is 3 x 3

        vec: JArray(JBoolean)
            modifies all the components of an array/vector uniform variable

        vec: NDArray[(Any,), Float]
            numpy array of values to modify all the components of an array/vector uniform variable

        vec: NDArray[(Any,), Int]
            modifies all the components of an array/vector uniform variable

        w: bool
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        w: float
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        w: int
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        x: bool
            first component of the variable to modify

        x: float
            first component of the variable to modify

        x: int
            first component of the variable to modify

        y: bool
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        y: float
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        y: int
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        z: bool
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

        z: float
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

        z: int
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

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

        Underlying Java method: PShader.set

        Methods
        -------

        You can use any of the following signatures:

         * set(name: str, boolvec: JArray(JBoolean), ncoords: int, /) -> None
         * set(name: str, mat: NDArray[(2, 3), Float], /) -> None
         * set(name: str, mat: NDArray[(4, 4), Float], /) -> None
         * set(name: str, mat: NDArray[(4, 4), Float], use3x3: bool, /) -> None
         * set(name: str, tex: Py5Image, /) -> None
         * set(name: str, vec: JArray(JBoolean), /) -> None
         * set(name: str, vec: NDArray[(Any,), Float], /) -> None
         * set(name: str, vec: NDArray[(Any,), Float], ncoords: int, /) -> None
         * set(name: str, vec: NDArray[(Any,), Int], /) -> None
         * set(name: str, vec: NDArray[(Any,), Int], ncoords: int, /) -> None
         * set(name: str, x: bool, /) -> None
         * set(name: str, x: bool, y: bool, /) -> None
         * set(name: str, x: bool, y: bool, z: bool, /) -> None
         * set(name: str, x: bool, y: bool, z: bool, w: bool, /) -> None
         * set(name: str, x: float, /) -> None
         * set(name: str, x: float, y: float, /) -> None
         * set(name: str, x: float, y: float, z: float, /) -> None
         * set(name: str, x: float, y: float, z: float, w: float, /) -> None
         * set(name: str, x: int, /) -> None
         * set(name: str, x: int, y: int, /) -> None
         * set(name: str, x: int, y: int, z: int, /) -> None
         * set(name: str, x: int, y: int, z: int, w: int, /) -> None

        Parameters
        ----------

        boolvec: JArray(JBoolean)
            modifies all the components of an array/vector uniform variable

        mat: NDArray[(2, 3), Float]
            numpy array of values

        mat: NDArray[(4, 4), Float]
            numpy array of values

        name: str
            the name of the uniform variable to modify

        ncoords: int
            number of coordinates per element, max 4

        tex: Py5Image
            sets the sampler uniform variable to read from this image texture

        use3x3: bool
            enforces the numpy array is 3 x 3

        vec: JArray(JBoolean)
            modifies all the components of an array/vector uniform variable

        vec: NDArray[(Any,), Float]
            numpy array of values to modify all the components of an array/vector uniform variable

        vec: NDArray[(Any,), Int]
            modifies all the components of an array/vector uniform variable

        w: bool
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        w: float
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        w: int
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        x: bool
            first component of the variable to modify

        x: float
            first component of the variable to modify

        x: int
            first component of the variable to modify

        y: bool
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        y: float
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        y: int
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        z: bool
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

        z: float
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

        z: int
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

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

        Underlying Java method: PShader.set

        Methods
        -------

        You can use any of the following signatures:

         * set(name: str, boolvec: JArray(JBoolean), ncoords: int, /) -> None
         * set(name: str, mat: NDArray[(2, 3), Float], /) -> None
         * set(name: str, mat: NDArray[(4, 4), Float], /) -> None
         * set(name: str, mat: NDArray[(4, 4), Float], use3x3: bool, /) -> None
         * set(name: str, tex: Py5Image, /) -> None
         * set(name: str, vec: JArray(JBoolean), /) -> None
         * set(name: str, vec: NDArray[(Any,), Float], /) -> None
         * set(name: str, vec: NDArray[(Any,), Float], ncoords: int, /) -> None
         * set(name: str, vec: NDArray[(Any,), Int], /) -> None
         * set(name: str, vec: NDArray[(Any,), Int], ncoords: int, /) -> None
         * set(name: str, x: bool, /) -> None
         * set(name: str, x: bool, y: bool, /) -> None
         * set(name: str, x: bool, y: bool, z: bool, /) -> None
         * set(name: str, x: bool, y: bool, z: bool, w: bool, /) -> None
         * set(name: str, x: float, /) -> None
         * set(name: str, x: float, y: float, /) -> None
         * set(name: str, x: float, y: float, z: float, /) -> None
         * set(name: str, x: float, y: float, z: float, w: float, /) -> None
         * set(name: str, x: int, /) -> None
         * set(name: str, x: int, y: int, /) -> None
         * set(name: str, x: int, y: int, z: int, /) -> None
         * set(name: str, x: int, y: int, z: int, w: int, /) -> None

        Parameters
        ----------

        boolvec: JArray(JBoolean)
            modifies all the components of an array/vector uniform variable

        mat: NDArray[(2, 3), Float]
            numpy array of values

        mat: NDArray[(4, 4), Float]
            numpy array of values

        name: str
            the name of the uniform variable to modify

        ncoords: int
            number of coordinates per element, max 4

        tex: Py5Image
            sets the sampler uniform variable to read from this image texture

        use3x3: bool
            enforces the numpy array is 3 x 3

        vec: JArray(JBoolean)
            modifies all the components of an array/vector uniform variable

        vec: NDArray[(Any,), Float]
            numpy array of values to modify all the components of an array/vector uniform variable

        vec: NDArray[(Any,), Int]
            modifies all the components of an array/vector uniform variable

        w: bool
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        w: float
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        w: int
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        x: bool
            first component of the variable to modify

        x: float
            first component of the variable to modify

        x: int
            first component of the variable to modify

        y: bool
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        y: float
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        y: int
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        z: bool
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

        z: float
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

        z: int
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

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

        Underlying Java method: PShader.set

        Methods
        -------

        You can use any of the following signatures:

         * set(name: str, boolvec: JArray(JBoolean), ncoords: int, /) -> None
         * set(name: str, mat: NDArray[(2, 3), Float], /) -> None
         * set(name: str, mat: NDArray[(4, 4), Float], /) -> None
         * set(name: str, mat: NDArray[(4, 4), Float], use3x3: bool, /) -> None
         * set(name: str, tex: Py5Image, /) -> None
         * set(name: str, vec: JArray(JBoolean), /) -> None
         * set(name: str, vec: NDArray[(Any,), Float], /) -> None
         * set(name: str, vec: NDArray[(Any,), Float], ncoords: int, /) -> None
         * set(name: str, vec: NDArray[(Any,), Int], /) -> None
         * set(name: str, vec: NDArray[(Any,), Int], ncoords: int, /) -> None
         * set(name: str, x: bool, /) -> None
         * set(name: str, x: bool, y: bool, /) -> None
         * set(name: str, x: bool, y: bool, z: bool, /) -> None
         * set(name: str, x: bool, y: bool, z: bool, w: bool, /) -> None
         * set(name: str, x: float, /) -> None
         * set(name: str, x: float, y: float, /) -> None
         * set(name: str, x: float, y: float, z: float, /) -> None
         * set(name: str, x: float, y: float, z: float, w: float, /) -> None
         * set(name: str, x: int, /) -> None
         * set(name: str, x: int, y: int, /) -> None
         * set(name: str, x: int, y: int, z: int, /) -> None
         * set(name: str, x: int, y: int, z: int, w: int, /) -> None

        Parameters
        ----------

        boolvec: JArray(JBoolean)
            modifies all the components of an array/vector uniform variable

        mat: NDArray[(2, 3), Float]
            numpy array of values

        mat: NDArray[(4, 4), Float]
            numpy array of values

        name: str
            the name of the uniform variable to modify

        ncoords: int
            number of coordinates per element, max 4

        tex: Py5Image
            sets the sampler uniform variable to read from this image texture

        use3x3: bool
            enforces the numpy array is 3 x 3

        vec: JArray(JBoolean)
            modifies all the components of an array/vector uniform variable

        vec: NDArray[(Any,), Float]
            numpy array of values to modify all the components of an array/vector uniform variable

        vec: NDArray[(Any,), Int]
            modifies all the components of an array/vector uniform variable

        w: bool
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        w: float
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        w: int
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        x: bool
            first component of the variable to modify

        x: float
            first component of the variable to modify

        x: int
            first component of the variable to modify

        y: bool
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        y: float
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        y: int
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        z: bool
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

        z: float
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

        z: int
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

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

        Underlying Java method: PShader.set

        Methods
        -------

        You can use any of the following signatures:

         * set(name: str, boolvec: JArray(JBoolean), ncoords: int, /) -> None
         * set(name: str, mat: NDArray[(2, 3), Float], /) -> None
         * set(name: str, mat: NDArray[(4, 4), Float], /) -> None
         * set(name: str, mat: NDArray[(4, 4), Float], use3x3: bool, /) -> None
         * set(name: str, tex: Py5Image, /) -> None
         * set(name: str, vec: JArray(JBoolean), /) -> None
         * set(name: str, vec: NDArray[(Any,), Float], /) -> None
         * set(name: str, vec: NDArray[(Any,), Float], ncoords: int, /) -> None
         * set(name: str, vec: NDArray[(Any,), Int], /) -> None
         * set(name: str, vec: NDArray[(Any,), Int], ncoords: int, /) -> None
         * set(name: str, x: bool, /) -> None
         * set(name: str, x: bool, y: bool, /) -> None
         * set(name: str, x: bool, y: bool, z: bool, /) -> None
         * set(name: str, x: bool, y: bool, z: bool, w: bool, /) -> None
         * set(name: str, x: float, /) -> None
         * set(name: str, x: float, y: float, /) -> None
         * set(name: str, x: float, y: float, z: float, /) -> None
         * set(name: str, x: float, y: float, z: float, w: float, /) -> None
         * set(name: str, x: int, /) -> None
         * set(name: str, x: int, y: int, /) -> None
         * set(name: str, x: int, y: int, z: int, /) -> None
         * set(name: str, x: int, y: int, z: int, w: int, /) -> None

        Parameters
        ----------

        boolvec: JArray(JBoolean)
            modifies all the components of an array/vector uniform variable

        mat: NDArray[(2, 3), Float]
            numpy array of values

        mat: NDArray[(4, 4), Float]
            numpy array of values

        name: str
            the name of the uniform variable to modify

        ncoords: int
            number of coordinates per element, max 4

        tex: Py5Image
            sets the sampler uniform variable to read from this image texture

        use3x3: bool
            enforces the numpy array is 3 x 3

        vec: JArray(JBoolean)
            modifies all the components of an array/vector uniform variable

        vec: NDArray[(Any,), Float]
            numpy array of values to modify all the components of an array/vector uniform variable

        vec: NDArray[(Any,), Int]
            modifies all the components of an array/vector uniform variable

        w: bool
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        w: float
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        w: int
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        x: bool
            first component of the variable to modify

        x: float
            first component of the variable to modify

        x: int
            first component of the variable to modify

        y: bool
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        y: float
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        y: int
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        z: bool
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

        z: float
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

        z: int
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

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

        Underlying Java method: PShader.set

        Methods
        -------

        You can use any of the following signatures:

         * set(name: str, boolvec: JArray(JBoolean), ncoords: int, /) -> None
         * set(name: str, mat: NDArray[(2, 3), Float], /) -> None
         * set(name: str, mat: NDArray[(4, 4), Float], /) -> None
         * set(name: str, mat: NDArray[(4, 4), Float], use3x3: bool, /) -> None
         * set(name: str, tex: Py5Image, /) -> None
         * set(name: str, vec: JArray(JBoolean), /) -> None
         * set(name: str, vec: NDArray[(Any,), Float], /) -> None
         * set(name: str, vec: NDArray[(Any,), Float], ncoords: int, /) -> None
         * set(name: str, vec: NDArray[(Any,), Int], /) -> None
         * set(name: str, vec: NDArray[(Any,), Int], ncoords: int, /) -> None
         * set(name: str, x: bool, /) -> None
         * set(name: str, x: bool, y: bool, /) -> None
         * set(name: str, x: bool, y: bool, z: bool, /) -> None
         * set(name: str, x: bool, y: bool, z: bool, w: bool, /) -> None
         * set(name: str, x: float, /) -> None
         * set(name: str, x: float, y: float, /) -> None
         * set(name: str, x: float, y: float, z: float, /) -> None
         * set(name: str, x: float, y: float, z: float, w: float, /) -> None
         * set(name: str, x: int, /) -> None
         * set(name: str, x: int, y: int, /) -> None
         * set(name: str, x: int, y: int, z: int, /) -> None
         * set(name: str, x: int, y: int, z: int, w: int, /) -> None

        Parameters
        ----------

        boolvec: JArray(JBoolean)
            modifies all the components of an array/vector uniform variable

        mat: NDArray[(2, 3), Float]
            numpy array of values

        mat: NDArray[(4, 4), Float]
            numpy array of values

        name: str
            the name of the uniform variable to modify

        ncoords: int
            number of coordinates per element, max 4

        tex: Py5Image
            sets the sampler uniform variable to read from this image texture

        use3x3: bool
            enforces the numpy array is 3 x 3

        vec: JArray(JBoolean)
            modifies all the components of an array/vector uniform variable

        vec: NDArray[(Any,), Float]
            numpy array of values to modify all the components of an array/vector uniform variable

        vec: NDArray[(Any,), Int]
            modifies all the components of an array/vector uniform variable

        w: bool
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        w: float
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        w: int
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        x: bool
            first component of the variable to modify

        x: float
            first component of the variable to modify

        x: int
            first component of the variable to modify

        y: bool
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        y: float
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        y: int
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        z: bool
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

        z: float
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

        z: int
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

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

        Underlying Java method: PShader.set

        Methods
        -------

        You can use any of the following signatures:

         * set(name: str, boolvec: JArray(JBoolean), ncoords: int, /) -> None
         * set(name: str, mat: NDArray[(2, 3), Float], /) -> None
         * set(name: str, mat: NDArray[(4, 4), Float], /) -> None
         * set(name: str, mat: NDArray[(4, 4), Float], use3x3: bool, /) -> None
         * set(name: str, tex: Py5Image, /) -> None
         * set(name: str, vec: JArray(JBoolean), /) -> None
         * set(name: str, vec: NDArray[(Any,), Float], /) -> None
         * set(name: str, vec: NDArray[(Any,), Float], ncoords: int, /) -> None
         * set(name: str, vec: NDArray[(Any,), Int], /) -> None
         * set(name: str, vec: NDArray[(Any,), Int], ncoords: int, /) -> None
         * set(name: str, x: bool, /) -> None
         * set(name: str, x: bool, y: bool, /) -> None
         * set(name: str, x: bool, y: bool, z: bool, /) -> None
         * set(name: str, x: bool, y: bool, z: bool, w: bool, /) -> None
         * set(name: str, x: float, /) -> None
         * set(name: str, x: float, y: float, /) -> None
         * set(name: str, x: float, y: float, z: float, /) -> None
         * set(name: str, x: float, y: float, z: float, w: float, /) -> None
         * set(name: str, x: int, /) -> None
         * set(name: str, x: int, y: int, /) -> None
         * set(name: str, x: int, y: int, z: int, /) -> None
         * set(name: str, x: int, y: int, z: int, w: int, /) -> None

        Parameters
        ----------

        boolvec: JArray(JBoolean)
            modifies all the components of an array/vector uniform variable

        mat: NDArray[(2, 3), Float]
            numpy array of values

        mat: NDArray[(4, 4), Float]
            numpy array of values

        name: str
            the name of the uniform variable to modify

        ncoords: int
            number of coordinates per element, max 4

        tex: Py5Image
            sets the sampler uniform variable to read from this image texture

        use3x3: bool
            enforces the numpy array is 3 x 3

        vec: JArray(JBoolean)
            modifies all the components of an array/vector uniform variable

        vec: NDArray[(Any,), Float]
            numpy array of values to modify all the components of an array/vector uniform variable

        vec: NDArray[(Any,), Int]
            modifies all the components of an array/vector uniform variable

        w: bool
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        w: float
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        w: int
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        x: bool
            first component of the variable to modify

        x: float
            first component of the variable to modify

        x: int
            first component of the variable to modify

        y: bool
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        y: float
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        y: int
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        z: bool
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

        z: float
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

        z: int
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

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

        Underlying Java method: PShader.set

        Methods
        -------

        You can use any of the following signatures:

         * set(name: str, boolvec: JArray(JBoolean), ncoords: int, /) -> None
         * set(name: str, mat: NDArray[(2, 3), Float], /) -> None
         * set(name: str, mat: NDArray[(4, 4), Float], /) -> None
         * set(name: str, mat: NDArray[(4, 4), Float], use3x3: bool, /) -> None
         * set(name: str, tex: Py5Image, /) -> None
         * set(name: str, vec: JArray(JBoolean), /) -> None
         * set(name: str, vec: NDArray[(Any,), Float], /) -> None
         * set(name: str, vec: NDArray[(Any,), Float], ncoords: int, /) -> None
         * set(name: str, vec: NDArray[(Any,), Int], /) -> None
         * set(name: str, vec: NDArray[(Any,), Int], ncoords: int, /) -> None
         * set(name: str, x: bool, /) -> None
         * set(name: str, x: bool, y: bool, /) -> None
         * set(name: str, x: bool, y: bool, z: bool, /) -> None
         * set(name: str, x: bool, y: bool, z: bool, w: bool, /) -> None
         * set(name: str, x: float, /) -> None
         * set(name: str, x: float, y: float, /) -> None
         * set(name: str, x: float, y: float, z: float, /) -> None
         * set(name: str, x: float, y: float, z: float, w: float, /) -> None
         * set(name: str, x: int, /) -> None
         * set(name: str, x: int, y: int, /) -> None
         * set(name: str, x: int, y: int, z: int, /) -> None
         * set(name: str, x: int, y: int, z: int, w: int, /) -> None

        Parameters
        ----------

        boolvec: JArray(JBoolean)
            modifies all the components of an array/vector uniform variable

        mat: NDArray[(2, 3), Float]
            numpy array of values

        mat: NDArray[(4, 4), Float]
            numpy array of values

        name: str
            the name of the uniform variable to modify

        ncoords: int
            number of coordinates per element, max 4

        tex: Py5Image
            sets the sampler uniform variable to read from this image texture

        use3x3: bool
            enforces the numpy array is 3 x 3

        vec: JArray(JBoolean)
            modifies all the components of an array/vector uniform variable

        vec: NDArray[(Any,), Float]
            numpy array of values to modify all the components of an array/vector uniform variable

        vec: NDArray[(Any,), Int]
            modifies all the components of an array/vector uniform variable

        w: bool
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        w: float
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        w: int
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        x: bool
            first component of the variable to modify

        x: float
            first component of the variable to modify

        x: int
            first component of the variable to modify

        y: bool
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        y: float
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        y: int
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        z: bool
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

        z: float
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

        z: int
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

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

        Underlying Java method: PShader.set

        Methods
        -------

        You can use any of the following signatures:

         * set(name: str, boolvec: JArray(JBoolean), ncoords: int, /) -> None
         * set(name: str, mat: NDArray[(2, 3), Float], /) -> None
         * set(name: str, mat: NDArray[(4, 4), Float], /) -> None
         * set(name: str, mat: NDArray[(4, 4), Float], use3x3: bool, /) -> None
         * set(name: str, tex: Py5Image, /) -> None
         * set(name: str, vec: JArray(JBoolean), /) -> None
         * set(name: str, vec: NDArray[(Any,), Float], /) -> None
         * set(name: str, vec: NDArray[(Any,), Float], ncoords: int, /) -> None
         * set(name: str, vec: NDArray[(Any,), Int], /) -> None
         * set(name: str, vec: NDArray[(Any,), Int], ncoords: int, /) -> None
         * set(name: str, x: bool, /) -> None
         * set(name: str, x: bool, y: bool, /) -> None
         * set(name: str, x: bool, y: bool, z: bool, /) -> None
         * set(name: str, x: bool, y: bool, z: bool, w: bool, /) -> None
         * set(name: str, x: float, /) -> None
         * set(name: str, x: float, y: float, /) -> None
         * set(name: str, x: float, y: float, z: float, /) -> None
         * set(name: str, x: float, y: float, z: float, w: float, /) -> None
         * set(name: str, x: int, /) -> None
         * set(name: str, x: int, y: int, /) -> None
         * set(name: str, x: int, y: int, z: int, /) -> None
         * set(name: str, x: int, y: int, z: int, w: int, /) -> None

        Parameters
        ----------

        boolvec: JArray(JBoolean)
            modifies all the components of an array/vector uniform variable

        mat: NDArray[(2, 3), Float]
            numpy array of values

        mat: NDArray[(4, 4), Float]
            numpy array of values

        name: str
            the name of the uniform variable to modify

        ncoords: int
            number of coordinates per element, max 4

        tex: Py5Image
            sets the sampler uniform variable to read from this image texture

        use3x3: bool
            enforces the numpy array is 3 x 3

        vec: JArray(JBoolean)
            modifies all the components of an array/vector uniform variable

        vec: NDArray[(Any,), Float]
            numpy array of values to modify all the components of an array/vector uniform variable

        vec: NDArray[(Any,), Int]
            modifies all the components of an array/vector uniform variable

        w: bool
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        w: float
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        w: int
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        x: bool
            first component of the variable to modify

        x: float
            first component of the variable to modify

        x: int
            first component of the variable to modify

        y: bool
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        y: float
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        y: int
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        z: bool
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

        z: float
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

        z: int
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

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

        Underlying Java method: PShader.set

        Methods
        -------

        You can use any of the following signatures:

         * set(name: str, boolvec: JArray(JBoolean), ncoords: int, /) -> None
         * set(name: str, mat: NDArray[(2, 3), Float], /) -> None
         * set(name: str, mat: NDArray[(4, 4), Float], /) -> None
         * set(name: str, mat: NDArray[(4, 4), Float], use3x3: bool, /) -> None
         * set(name: str, tex: Py5Image, /) -> None
         * set(name: str, vec: JArray(JBoolean), /) -> None
         * set(name: str, vec: NDArray[(Any,), Float], /) -> None
         * set(name: str, vec: NDArray[(Any,), Float], ncoords: int, /) -> None
         * set(name: str, vec: NDArray[(Any,), Int], /) -> None
         * set(name: str, vec: NDArray[(Any,), Int], ncoords: int, /) -> None
         * set(name: str, x: bool, /) -> None
         * set(name: str, x: bool, y: bool, /) -> None
         * set(name: str, x: bool, y: bool, z: bool, /) -> None
         * set(name: str, x: bool, y: bool, z: bool, w: bool, /) -> None
         * set(name: str, x: float, /) -> None
         * set(name: str, x: float, y: float, /) -> None
         * set(name: str, x: float, y: float, z: float, /) -> None
         * set(name: str, x: float, y: float, z: float, w: float, /) -> None
         * set(name: str, x: int, /) -> None
         * set(name: str, x: int, y: int, /) -> None
         * set(name: str, x: int, y: int, z: int, /) -> None
         * set(name: str, x: int, y: int, z: int, w: int, /) -> None

        Parameters
        ----------

        boolvec: JArray(JBoolean)
            modifies all the components of an array/vector uniform variable

        mat: NDArray[(2, 3), Float]
            numpy array of values

        mat: NDArray[(4, 4), Float]
            numpy array of values

        name: str
            the name of the uniform variable to modify

        ncoords: int
            number of coordinates per element, max 4

        tex: Py5Image
            sets the sampler uniform variable to read from this image texture

        use3x3: bool
            enforces the numpy array is 3 x 3

        vec: JArray(JBoolean)
            modifies all the components of an array/vector uniform variable

        vec: NDArray[(Any,), Float]
            numpy array of values to modify all the components of an array/vector uniform variable

        vec: NDArray[(Any,), Int]
            modifies all the components of an array/vector uniform variable

        w: bool
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        w: float
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        w: int
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        x: bool
            first component of the variable to modify

        x: float
            first component of the variable to modify

        x: int
            first component of the variable to modify

        y: bool
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        y: float
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        y: int
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        z: bool
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

        z: float
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

        z: int
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

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

        Underlying Java method: PShader.set

        Methods
        -------

        You can use any of the following signatures:

         * set(name: str, boolvec: JArray(JBoolean), ncoords: int, /) -> None
         * set(name: str, mat: NDArray[(2, 3), Float], /) -> None
         * set(name: str, mat: NDArray[(4, 4), Float], /) -> None
         * set(name: str, mat: NDArray[(4, 4), Float], use3x3: bool, /) -> None
         * set(name: str, tex: Py5Image, /) -> None
         * set(name: str, vec: JArray(JBoolean), /) -> None
         * set(name: str, vec: NDArray[(Any,), Float], /) -> None
         * set(name: str, vec: NDArray[(Any,), Float], ncoords: int, /) -> None
         * set(name: str, vec: NDArray[(Any,), Int], /) -> None
         * set(name: str, vec: NDArray[(Any,), Int], ncoords: int, /) -> None
         * set(name: str, x: bool, /) -> None
         * set(name: str, x: bool, y: bool, /) -> None
         * set(name: str, x: bool, y: bool, z: bool, /) -> None
         * set(name: str, x: bool, y: bool, z: bool, w: bool, /) -> None
         * set(name: str, x: float, /) -> None
         * set(name: str, x: float, y: float, /) -> None
         * set(name: str, x: float, y: float, z: float, /) -> None
         * set(name: str, x: float, y: float, z: float, w: float, /) -> None
         * set(name: str, x: int, /) -> None
         * set(name: str, x: int, y: int, /) -> None
         * set(name: str, x: int, y: int, z: int, /) -> None
         * set(name: str, x: int, y: int, z: int, w: int, /) -> None

        Parameters
        ----------

        boolvec: JArray(JBoolean)
            modifies all the components of an array/vector uniform variable

        mat: NDArray[(2, 3), Float]
            numpy array of values

        mat: NDArray[(4, 4), Float]
            numpy array of values

        name: str
            the name of the uniform variable to modify

        ncoords: int
            number of coordinates per element, max 4

        tex: Py5Image
            sets the sampler uniform variable to read from this image texture

        use3x3: bool
            enforces the numpy array is 3 x 3

        vec: JArray(JBoolean)
            modifies all the components of an array/vector uniform variable

        vec: NDArray[(Any,), Float]
            numpy array of values to modify all the components of an array/vector uniform variable

        vec: NDArray[(Any,), Int]
            modifies all the components of an array/vector uniform variable

        w: bool
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        w: float
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        w: int
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        x: bool
            first component of the variable to modify

        x: float
            first component of the variable to modify

        x: int
            first component of the variable to modify

        y: bool
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        y: float
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        y: int
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        z: bool
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

        z: float
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

        z: int
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

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

        Underlying Java method: PShader.set

        Methods
        -------

        You can use any of the following signatures:

         * set(name: str, boolvec: JArray(JBoolean), ncoords: int, /) -> None
         * set(name: str, mat: NDArray[(2, 3), Float], /) -> None
         * set(name: str, mat: NDArray[(4, 4), Float], /) -> None
         * set(name: str, mat: NDArray[(4, 4), Float], use3x3: bool, /) -> None
         * set(name: str, tex: Py5Image, /) -> None
         * set(name: str, vec: JArray(JBoolean), /) -> None
         * set(name: str, vec: NDArray[(Any,), Float], /) -> None
         * set(name: str, vec: NDArray[(Any,), Float], ncoords: int, /) -> None
         * set(name: str, vec: NDArray[(Any,), Int], /) -> None
         * set(name: str, vec: NDArray[(Any,), Int], ncoords: int, /) -> None
         * set(name: str, x: bool, /) -> None
         * set(name: str, x: bool, y: bool, /) -> None
         * set(name: str, x: bool, y: bool, z: bool, /) -> None
         * set(name: str, x: bool, y: bool, z: bool, w: bool, /) -> None
         * set(name: str, x: float, /) -> None
         * set(name: str, x: float, y: float, /) -> None
         * set(name: str, x: float, y: float, z: float, /) -> None
         * set(name: str, x: float, y: float, z: float, w: float, /) -> None
         * set(name: str, x: int, /) -> None
         * set(name: str, x: int, y: int, /) -> None
         * set(name: str, x: int, y: int, z: int, /) -> None
         * set(name: str, x: int, y: int, z: int, w: int, /) -> None

        Parameters
        ----------

        boolvec: JArray(JBoolean)
            modifies all the components of an array/vector uniform variable

        mat: NDArray[(2, 3), Float]
            numpy array of values

        mat: NDArray[(4, 4), Float]
            numpy array of values

        name: str
            the name of the uniform variable to modify

        ncoords: int
            number of coordinates per element, max 4

        tex: Py5Image
            sets the sampler uniform variable to read from this image texture

        use3x3: bool
            enforces the numpy array is 3 x 3

        vec: JArray(JBoolean)
            modifies all the components of an array/vector uniform variable

        vec: NDArray[(Any,), Float]
            numpy array of values to modify all the components of an array/vector uniform variable

        vec: NDArray[(Any,), Int]
            modifies all the components of an array/vector uniform variable

        w: bool
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        w: float
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        w: int
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        x: bool
            first component of the variable to modify

        x: float
            first component of the variable to modify

        x: int
            first component of the variable to modify

        y: bool
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        y: float
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        y: int
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        z: bool
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

        z: float
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

        z: int
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

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

        Underlying Java method: PShader.set

        Methods
        -------

        You can use any of the following signatures:

         * set(name: str, boolvec: JArray(JBoolean), ncoords: int, /) -> None
         * set(name: str, mat: NDArray[(2, 3), Float], /) -> None
         * set(name: str, mat: NDArray[(4, 4), Float], /) -> None
         * set(name: str, mat: NDArray[(4, 4), Float], use3x3: bool, /) -> None
         * set(name: str, tex: Py5Image, /) -> None
         * set(name: str, vec: JArray(JBoolean), /) -> None
         * set(name: str, vec: NDArray[(Any,), Float], /) -> None
         * set(name: str, vec: NDArray[(Any,), Float], ncoords: int, /) -> None
         * set(name: str, vec: NDArray[(Any,), Int], /) -> None
         * set(name: str, vec: NDArray[(Any,), Int], ncoords: int, /) -> None
         * set(name: str, x: bool, /) -> None
         * set(name: str, x: bool, y: bool, /) -> None
         * set(name: str, x: bool, y: bool, z: bool, /) -> None
         * set(name: str, x: bool, y: bool, z: bool, w: bool, /) -> None
         * set(name: str, x: float, /) -> None
         * set(name: str, x: float, y: float, /) -> None
         * set(name: str, x: float, y: float, z: float, /) -> None
         * set(name: str, x: float, y: float, z: float, w: float, /) -> None
         * set(name: str, x: int, /) -> None
         * set(name: str, x: int, y: int, /) -> None
         * set(name: str, x: int, y: int, z: int, /) -> None
         * set(name: str, x: int, y: int, z: int, w: int, /) -> None

        Parameters
        ----------

        boolvec: JArray(JBoolean)
            modifies all the components of an array/vector uniform variable

        mat: NDArray[(2, 3), Float]
            numpy array of values

        mat: NDArray[(4, 4), Float]
            numpy array of values

        name: str
            the name of the uniform variable to modify

        ncoords: int
            number of coordinates per element, max 4

        tex: Py5Image
            sets the sampler uniform variable to read from this image texture

        use3x3: bool
            enforces the numpy array is 3 x 3

        vec: JArray(JBoolean)
            modifies all the components of an array/vector uniform variable

        vec: NDArray[(Any,), Float]
            numpy array of values to modify all the components of an array/vector uniform variable

        vec: NDArray[(Any,), Int]
            modifies all the components of an array/vector uniform variable

        w: bool
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        w: float
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        w: int
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        x: bool
            first component of the variable to modify

        x: float
            first component of the variable to modify

        x: int
            first component of the variable to modify

        y: bool
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        y: float
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        y: int
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        z: bool
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

        z: float
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

        z: int
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

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

        Underlying Java method: PShader.set

        Methods
        -------

        You can use any of the following signatures:

         * set(name: str, boolvec: JArray(JBoolean), ncoords: int, /) -> None
         * set(name: str, mat: NDArray[(2, 3), Float], /) -> None
         * set(name: str, mat: NDArray[(4, 4), Float], /) -> None
         * set(name: str, mat: NDArray[(4, 4), Float], use3x3: bool, /) -> None
         * set(name: str, tex: Py5Image, /) -> None
         * set(name: str, vec: JArray(JBoolean), /) -> None
         * set(name: str, vec: NDArray[(Any,), Float], /) -> None
         * set(name: str, vec: NDArray[(Any,), Float], ncoords: int, /) -> None
         * set(name: str, vec: NDArray[(Any,), Int], /) -> None
         * set(name: str, vec: NDArray[(Any,), Int], ncoords: int, /) -> None
         * set(name: str, x: bool, /) -> None
         * set(name: str, x: bool, y: bool, /) -> None
         * set(name: str, x: bool, y: bool, z: bool, /) -> None
         * set(name: str, x: bool, y: bool, z: bool, w: bool, /) -> None
         * set(name: str, x: float, /) -> None
         * set(name: str, x: float, y: float, /) -> None
         * set(name: str, x: float, y: float, z: float, /) -> None
         * set(name: str, x: float, y: float, z: float, w: float, /) -> None
         * set(name: str, x: int, /) -> None
         * set(name: str, x: int, y: int, /) -> None
         * set(name: str, x: int, y: int, z: int, /) -> None
         * set(name: str, x: int, y: int, z: int, w: int, /) -> None

        Parameters
        ----------

        boolvec: JArray(JBoolean)
            modifies all the components of an array/vector uniform variable

        mat: NDArray[(2, 3), Float]
            numpy array of values

        mat: NDArray[(4, 4), Float]
            numpy array of values

        name: str
            the name of the uniform variable to modify

        ncoords: int
            number of coordinates per element, max 4

        tex: Py5Image
            sets the sampler uniform variable to read from this image texture

        use3x3: bool
            enforces the numpy array is 3 x 3

        vec: JArray(JBoolean)
            modifies all the components of an array/vector uniform variable

        vec: NDArray[(Any,), Float]
            numpy array of values to modify all the components of an array/vector uniform variable

        vec: NDArray[(Any,), Int]
            modifies all the components of an array/vector uniform variable

        w: bool
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        w: float
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        w: int
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        x: bool
            first component of the variable to modify

        x: float
            first component of the variable to modify

        x: int
            first component of the variable to modify

        y: bool
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        y: float
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        y: int
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        z: bool
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

        z: float
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

        z: int
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

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

        Underlying Java method: PShader.set

        Methods
        -------

        You can use any of the following signatures:

         * set(name: str, boolvec: JArray(JBoolean), ncoords: int, /) -> None
         * set(name: str, mat: NDArray[(2, 3), Float], /) -> None
         * set(name: str, mat: NDArray[(4, 4), Float], /) -> None
         * set(name: str, mat: NDArray[(4, 4), Float], use3x3: bool, /) -> None
         * set(name: str, tex: Py5Image, /) -> None
         * set(name: str, vec: JArray(JBoolean), /) -> None
         * set(name: str, vec: NDArray[(Any,), Float], /) -> None
         * set(name: str, vec: NDArray[(Any,), Float], ncoords: int, /) -> None
         * set(name: str, vec: NDArray[(Any,), Int], /) -> None
         * set(name: str, vec: NDArray[(Any,), Int], ncoords: int, /) -> None
         * set(name: str, x: bool, /) -> None
         * set(name: str, x: bool, y: bool, /) -> None
         * set(name: str, x: bool, y: bool, z: bool, /) -> None
         * set(name: str, x: bool, y: bool, z: bool, w: bool, /) -> None
         * set(name: str, x: float, /) -> None
         * set(name: str, x: float, y: float, /) -> None
         * set(name: str, x: float, y: float, z: float, /) -> None
         * set(name: str, x: float, y: float, z: float, w: float, /) -> None
         * set(name: str, x: int, /) -> None
         * set(name: str, x: int, y: int, /) -> None
         * set(name: str, x: int, y: int, z: int, /) -> None
         * set(name: str, x: int, y: int, z: int, w: int, /) -> None

        Parameters
        ----------

        boolvec: JArray(JBoolean)
            modifies all the components of an array/vector uniform variable

        mat: NDArray[(2, 3), Float]
            numpy array of values

        mat: NDArray[(4, 4), Float]
            numpy array of values

        name: str
            the name of the uniform variable to modify

        ncoords: int
            number of coordinates per element, max 4

        tex: Py5Image
            sets the sampler uniform variable to read from this image texture

        use3x3: bool
            enforces the numpy array is 3 x 3

        vec: JArray(JBoolean)
            modifies all the components of an array/vector uniform variable

        vec: NDArray[(Any,), Float]
            numpy array of values to modify all the components of an array/vector uniform variable

        vec: NDArray[(Any,), Int]
            modifies all the components of an array/vector uniform variable

        w: bool
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        w: float
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        w: int
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        x: bool
            first component of the variable to modify

        x: float
            first component of the variable to modify

        x: int
            first component of the variable to modify

        y: bool
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        y: float
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        y: int
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        z: bool
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

        z: float
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

        z: int
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

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

        Underlying Java method: PShader.set

        Methods
        -------

        You can use any of the following signatures:

         * set(name: str, boolvec: JArray(JBoolean), ncoords: int, /) -> None
         * set(name: str, mat: NDArray[(2, 3), Float], /) -> None
         * set(name: str, mat: NDArray[(4, 4), Float], /) -> None
         * set(name: str, mat: NDArray[(4, 4), Float], use3x3: bool, /) -> None
         * set(name: str, tex: Py5Image, /) -> None
         * set(name: str, vec: JArray(JBoolean), /) -> None
         * set(name: str, vec: NDArray[(Any,), Float], /) -> None
         * set(name: str, vec: NDArray[(Any,), Float], ncoords: int, /) -> None
         * set(name: str, vec: NDArray[(Any,), Int], /) -> None
         * set(name: str, vec: NDArray[(Any,), Int], ncoords: int, /) -> None
         * set(name: str, x: bool, /) -> None
         * set(name: str, x: bool, y: bool, /) -> None
         * set(name: str, x: bool, y: bool, z: bool, /) -> None
         * set(name: str, x: bool, y: bool, z: bool, w: bool, /) -> None
         * set(name: str, x: float, /) -> None
         * set(name: str, x: float, y: float, /) -> None
         * set(name: str, x: float, y: float, z: float, /) -> None
         * set(name: str, x: float, y: float, z: float, w: float, /) -> None
         * set(name: str, x: int, /) -> None
         * set(name: str, x: int, y: int, /) -> None
         * set(name: str, x: int, y: int, z: int, /) -> None
         * set(name: str, x: int, y: int, z: int, w: int, /) -> None

        Parameters
        ----------

        boolvec: JArray(JBoolean)
            modifies all the components of an array/vector uniform variable

        mat: NDArray[(2, 3), Float]
            numpy array of values

        mat: NDArray[(4, 4), Float]
            numpy array of values

        name: str
            the name of the uniform variable to modify

        ncoords: int
            number of coordinates per element, max 4

        tex: Py5Image
            sets the sampler uniform variable to read from this image texture

        use3x3: bool
            enforces the numpy array is 3 x 3

        vec: JArray(JBoolean)
            modifies all the components of an array/vector uniform variable

        vec: NDArray[(Any,), Float]
            numpy array of values to modify all the components of an array/vector uniform variable

        vec: NDArray[(Any,), Int]
            modifies all the components of an array/vector uniform variable

        w: bool
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        w: float
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        w: int
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        x: bool
            first component of the variable to modify

        x: float
            first component of the variable to modify

        x: int
            first component of the variable to modify

        y: bool
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        y: float
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        y: int
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        z: bool
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

        z: float
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

        z: int
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

        Notes
        -----

        Sets the uniform variables inside the shader to modify the effect while the
        program is running.
        """
        pass

    @overload
    def set(self, name: str, vec: NDArray[(Any,), Int], /) -> None:
        """Sets the uniform variables inside the shader to modify the effect while the
        program is running.

        Underlying Java method: PShader.set

        Methods
        -------

        You can use any of the following signatures:

         * set(name: str, boolvec: JArray(JBoolean), ncoords: int, /) -> None
         * set(name: str, mat: NDArray[(2, 3), Float], /) -> None
         * set(name: str, mat: NDArray[(4, 4), Float], /) -> None
         * set(name: str, mat: NDArray[(4, 4), Float], use3x3: bool, /) -> None
         * set(name: str, tex: Py5Image, /) -> None
         * set(name: str, vec: JArray(JBoolean), /) -> None
         * set(name: str, vec: NDArray[(Any,), Float], /) -> None
         * set(name: str, vec: NDArray[(Any,), Float], ncoords: int, /) -> None
         * set(name: str, vec: NDArray[(Any,), Int], /) -> None
         * set(name: str, vec: NDArray[(Any,), Int], ncoords: int, /) -> None
         * set(name: str, x: bool, /) -> None
         * set(name: str, x: bool, y: bool, /) -> None
         * set(name: str, x: bool, y: bool, z: bool, /) -> None
         * set(name: str, x: bool, y: bool, z: bool, w: bool, /) -> None
         * set(name: str, x: float, /) -> None
         * set(name: str, x: float, y: float, /) -> None
         * set(name: str, x: float, y: float, z: float, /) -> None
         * set(name: str, x: float, y: float, z: float, w: float, /) -> None
         * set(name: str, x: int, /) -> None
         * set(name: str, x: int, y: int, /) -> None
         * set(name: str, x: int, y: int, z: int, /) -> None
         * set(name: str, x: int, y: int, z: int, w: int, /) -> None

        Parameters
        ----------

        boolvec: JArray(JBoolean)
            modifies all the components of an array/vector uniform variable

        mat: NDArray[(2, 3), Float]
            numpy array of values

        mat: NDArray[(4, 4), Float]
            numpy array of values

        name: str
            the name of the uniform variable to modify

        ncoords: int
            number of coordinates per element, max 4

        tex: Py5Image
            sets the sampler uniform variable to read from this image texture

        use3x3: bool
            enforces the numpy array is 3 x 3

        vec: JArray(JBoolean)
            modifies all the components of an array/vector uniform variable

        vec: NDArray[(Any,), Float]
            numpy array of values to modify all the components of an array/vector uniform variable

        vec: NDArray[(Any,), Int]
            modifies all the components of an array/vector uniform variable

        w: bool
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        w: float
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        w: int
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        x: bool
            first component of the variable to modify

        x: float
            first component of the variable to modify

        x: int
            first component of the variable to modify

        y: bool
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        y: float
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        y: int
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        z: bool
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

        z: float
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

        z: int
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

        Notes
        -----

        Sets the uniform variables inside the shader to modify the effect while the
        program is running.
        """
        pass

    @overload
    def set(self, name: str, vec: NDArray[(
            Any,), Int], ncoords: int, /) -> None:
        """Sets the uniform variables inside the shader to modify the effect while the
        program is running.

        Underlying Java method: PShader.set

        Methods
        -------

        You can use any of the following signatures:

         * set(name: str, boolvec: JArray(JBoolean), ncoords: int, /) -> None
         * set(name: str, mat: NDArray[(2, 3), Float], /) -> None
         * set(name: str, mat: NDArray[(4, 4), Float], /) -> None
         * set(name: str, mat: NDArray[(4, 4), Float], use3x3: bool, /) -> None
         * set(name: str, tex: Py5Image, /) -> None
         * set(name: str, vec: JArray(JBoolean), /) -> None
         * set(name: str, vec: NDArray[(Any,), Float], /) -> None
         * set(name: str, vec: NDArray[(Any,), Float], ncoords: int, /) -> None
         * set(name: str, vec: NDArray[(Any,), Int], /) -> None
         * set(name: str, vec: NDArray[(Any,), Int], ncoords: int, /) -> None
         * set(name: str, x: bool, /) -> None
         * set(name: str, x: bool, y: bool, /) -> None
         * set(name: str, x: bool, y: bool, z: bool, /) -> None
         * set(name: str, x: bool, y: bool, z: bool, w: bool, /) -> None
         * set(name: str, x: float, /) -> None
         * set(name: str, x: float, y: float, /) -> None
         * set(name: str, x: float, y: float, z: float, /) -> None
         * set(name: str, x: float, y: float, z: float, w: float, /) -> None
         * set(name: str, x: int, /) -> None
         * set(name: str, x: int, y: int, /) -> None
         * set(name: str, x: int, y: int, z: int, /) -> None
         * set(name: str, x: int, y: int, z: int, w: int, /) -> None

        Parameters
        ----------

        boolvec: JArray(JBoolean)
            modifies all the components of an array/vector uniform variable

        mat: NDArray[(2, 3), Float]
            numpy array of values

        mat: NDArray[(4, 4), Float]
            numpy array of values

        name: str
            the name of the uniform variable to modify

        ncoords: int
            number of coordinates per element, max 4

        tex: Py5Image
            sets the sampler uniform variable to read from this image texture

        use3x3: bool
            enforces the numpy array is 3 x 3

        vec: JArray(JBoolean)
            modifies all the components of an array/vector uniform variable

        vec: NDArray[(Any,), Float]
            numpy array of values to modify all the components of an array/vector uniform variable

        vec: NDArray[(Any,), Int]
            modifies all the components of an array/vector uniform variable

        w: bool
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        w: float
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        w: int
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        x: bool
            first component of the variable to modify

        x: float
            first component of the variable to modify

        x: int
            first component of the variable to modify

        y: bool
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        y: float
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        y: int
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        z: bool
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

        z: float
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

        z: int
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

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

        Underlying Java method: PShader.set

        Methods
        -------

        You can use any of the following signatures:

         * set(name: str, boolvec: JArray(JBoolean), ncoords: int, /) -> None
         * set(name: str, mat: NDArray[(2, 3), Float], /) -> None
         * set(name: str, mat: NDArray[(4, 4), Float], /) -> None
         * set(name: str, mat: NDArray[(4, 4), Float], use3x3: bool, /) -> None
         * set(name: str, tex: Py5Image, /) -> None
         * set(name: str, vec: JArray(JBoolean), /) -> None
         * set(name: str, vec: NDArray[(Any,), Float], /) -> None
         * set(name: str, vec: NDArray[(Any,), Float], ncoords: int, /) -> None
         * set(name: str, vec: NDArray[(Any,), Int], /) -> None
         * set(name: str, vec: NDArray[(Any,), Int], ncoords: int, /) -> None
         * set(name: str, x: bool, /) -> None
         * set(name: str, x: bool, y: bool, /) -> None
         * set(name: str, x: bool, y: bool, z: bool, /) -> None
         * set(name: str, x: bool, y: bool, z: bool, w: bool, /) -> None
         * set(name: str, x: float, /) -> None
         * set(name: str, x: float, y: float, /) -> None
         * set(name: str, x: float, y: float, z: float, /) -> None
         * set(name: str, x: float, y: float, z: float, w: float, /) -> None
         * set(name: str, x: int, /) -> None
         * set(name: str, x: int, y: int, /) -> None
         * set(name: str, x: int, y: int, z: int, /) -> None
         * set(name: str, x: int, y: int, z: int, w: int, /) -> None

        Parameters
        ----------

        boolvec: JArray(JBoolean)
            modifies all the components of an array/vector uniform variable

        mat: NDArray[(2, 3), Float]
            numpy array of values

        mat: NDArray[(4, 4), Float]
            numpy array of values

        name: str
            the name of the uniform variable to modify

        ncoords: int
            number of coordinates per element, max 4

        tex: Py5Image
            sets the sampler uniform variable to read from this image texture

        use3x3: bool
            enforces the numpy array is 3 x 3

        vec: JArray(JBoolean)
            modifies all the components of an array/vector uniform variable

        vec: NDArray[(Any,), Float]
            numpy array of values to modify all the components of an array/vector uniform variable

        vec: NDArray[(Any,), Int]
            modifies all the components of an array/vector uniform variable

        w: bool
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        w: float
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        w: int
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        x: bool
            first component of the variable to modify

        x: float
            first component of the variable to modify

        x: int
            first component of the variable to modify

        y: bool
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        y: float
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        y: int
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        z: bool
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

        z: float
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

        z: int
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

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

        Underlying Java method: PShader.set

        Methods
        -------

        You can use any of the following signatures:

         * set(name: str, boolvec: JArray(JBoolean), ncoords: int, /) -> None
         * set(name: str, mat: NDArray[(2, 3), Float], /) -> None
         * set(name: str, mat: NDArray[(4, 4), Float], /) -> None
         * set(name: str, mat: NDArray[(4, 4), Float], use3x3: bool, /) -> None
         * set(name: str, tex: Py5Image, /) -> None
         * set(name: str, vec: JArray(JBoolean), /) -> None
         * set(name: str, vec: NDArray[(Any,), Float], /) -> None
         * set(name: str, vec: NDArray[(Any,), Float], ncoords: int, /) -> None
         * set(name: str, vec: NDArray[(Any,), Int], /) -> None
         * set(name: str, vec: NDArray[(Any,), Int], ncoords: int, /) -> None
         * set(name: str, x: bool, /) -> None
         * set(name: str, x: bool, y: bool, /) -> None
         * set(name: str, x: bool, y: bool, z: bool, /) -> None
         * set(name: str, x: bool, y: bool, z: bool, w: bool, /) -> None
         * set(name: str, x: float, /) -> None
         * set(name: str, x: float, y: float, /) -> None
         * set(name: str, x: float, y: float, z: float, /) -> None
         * set(name: str, x: float, y: float, z: float, w: float, /) -> None
         * set(name: str, x: int, /) -> None
         * set(name: str, x: int, y: int, /) -> None
         * set(name: str, x: int, y: int, z: int, /) -> None
         * set(name: str, x: int, y: int, z: int, w: int, /) -> None

        Parameters
        ----------

        boolvec: JArray(JBoolean)
            modifies all the components of an array/vector uniform variable

        mat: NDArray[(2, 3), Float]
            numpy array of values

        mat: NDArray[(4, 4), Float]
            numpy array of values

        name: str
            the name of the uniform variable to modify

        ncoords: int
            number of coordinates per element, max 4

        tex: Py5Image
            sets the sampler uniform variable to read from this image texture

        use3x3: bool
            enforces the numpy array is 3 x 3

        vec: JArray(JBoolean)
            modifies all the components of an array/vector uniform variable

        vec: NDArray[(Any,), Float]
            numpy array of values to modify all the components of an array/vector uniform variable

        vec: NDArray[(Any,), Int]
            modifies all the components of an array/vector uniform variable

        w: bool
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        w: float
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        w: int
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        x: bool
            first component of the variable to modify

        x: float
            first component of the variable to modify

        x: int
            first component of the variable to modify

        y: bool
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        y: float
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        y: int
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        z: bool
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

        z: float
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

        z: int
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

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

        Underlying Java method: PShader.set

        Methods
        -------

        You can use any of the following signatures:

         * set(name: str, boolvec: JArray(JBoolean), ncoords: int, /) -> None
         * set(name: str, mat: NDArray[(2, 3), Float], /) -> None
         * set(name: str, mat: NDArray[(4, 4), Float], /) -> None
         * set(name: str, mat: NDArray[(4, 4), Float], use3x3: bool, /) -> None
         * set(name: str, tex: Py5Image, /) -> None
         * set(name: str, vec: JArray(JBoolean), /) -> None
         * set(name: str, vec: NDArray[(Any,), Float], /) -> None
         * set(name: str, vec: NDArray[(Any,), Float], ncoords: int, /) -> None
         * set(name: str, vec: NDArray[(Any,), Int], /) -> None
         * set(name: str, vec: NDArray[(Any,), Int], ncoords: int, /) -> None
         * set(name: str, x: bool, /) -> None
         * set(name: str, x: bool, y: bool, /) -> None
         * set(name: str, x: bool, y: bool, z: bool, /) -> None
         * set(name: str, x: bool, y: bool, z: bool, w: bool, /) -> None
         * set(name: str, x: float, /) -> None
         * set(name: str, x: float, y: float, /) -> None
         * set(name: str, x: float, y: float, z: float, /) -> None
         * set(name: str, x: float, y: float, z: float, w: float, /) -> None
         * set(name: str, x: int, /) -> None
         * set(name: str, x: int, y: int, /) -> None
         * set(name: str, x: int, y: int, z: int, /) -> None
         * set(name: str, x: int, y: int, z: int, w: int, /) -> None

        Parameters
        ----------

        boolvec: JArray(JBoolean)
            modifies all the components of an array/vector uniform variable

        mat: NDArray[(2, 3), Float]
            numpy array of values

        mat: NDArray[(4, 4), Float]
            numpy array of values

        name: str
            the name of the uniform variable to modify

        ncoords: int
            number of coordinates per element, max 4

        tex: Py5Image
            sets the sampler uniform variable to read from this image texture

        use3x3: bool
            enforces the numpy array is 3 x 3

        vec: JArray(JBoolean)
            modifies all the components of an array/vector uniform variable

        vec: NDArray[(Any,), Float]
            numpy array of values to modify all the components of an array/vector uniform variable

        vec: NDArray[(Any,), Int]
            modifies all the components of an array/vector uniform variable

        w: bool
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        w: float
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        w: int
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        x: bool
            first component of the variable to modify

        x: float
            first component of the variable to modify

        x: int
            first component of the variable to modify

        y: bool
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        y: float
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        y: int
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        z: bool
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

        z: float
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

        z: int
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

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

        Underlying Java method: PShader.set

        Methods
        -------

        You can use any of the following signatures:

         * set(name: str, boolvec: JArray(JBoolean), ncoords: int, /) -> None
         * set(name: str, mat: NDArray[(2, 3), Float], /) -> None
         * set(name: str, mat: NDArray[(4, 4), Float], /) -> None
         * set(name: str, mat: NDArray[(4, 4), Float], use3x3: bool, /) -> None
         * set(name: str, tex: Py5Image, /) -> None
         * set(name: str, vec: JArray(JBoolean), /) -> None
         * set(name: str, vec: NDArray[(Any,), Float], /) -> None
         * set(name: str, vec: NDArray[(Any,), Float], ncoords: int, /) -> None
         * set(name: str, vec: NDArray[(Any,), Int], /) -> None
         * set(name: str, vec: NDArray[(Any,), Int], ncoords: int, /) -> None
         * set(name: str, x: bool, /) -> None
         * set(name: str, x: bool, y: bool, /) -> None
         * set(name: str, x: bool, y: bool, z: bool, /) -> None
         * set(name: str, x: bool, y: bool, z: bool, w: bool, /) -> None
         * set(name: str, x: float, /) -> None
         * set(name: str, x: float, y: float, /) -> None
         * set(name: str, x: float, y: float, z: float, /) -> None
         * set(name: str, x: float, y: float, z: float, w: float, /) -> None
         * set(name: str, x: int, /) -> None
         * set(name: str, x: int, y: int, /) -> None
         * set(name: str, x: int, y: int, z: int, /) -> None
         * set(name: str, x: int, y: int, z: int, w: int, /) -> None

        Parameters
        ----------

        boolvec: JArray(JBoolean)
            modifies all the components of an array/vector uniform variable

        mat: NDArray[(2, 3), Float]
            numpy array of values

        mat: NDArray[(4, 4), Float]
            numpy array of values

        name: str
            the name of the uniform variable to modify

        ncoords: int
            number of coordinates per element, max 4

        tex: Py5Image
            sets the sampler uniform variable to read from this image texture

        use3x3: bool
            enforces the numpy array is 3 x 3

        vec: JArray(JBoolean)
            modifies all the components of an array/vector uniform variable

        vec: NDArray[(Any,), Float]
            numpy array of values to modify all the components of an array/vector uniform variable

        vec: NDArray[(Any,), Int]
            modifies all the components of an array/vector uniform variable

        w: bool
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        w: float
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        w: int
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        x: bool
            first component of the variable to modify

        x: float
            first component of the variable to modify

        x: int
            first component of the variable to modify

        y: bool
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        y: float
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        y: int
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        z: bool
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

        z: float
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

        z: int
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

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

        Underlying Java method: PShader.set

        Methods
        -------

        You can use any of the following signatures:

         * set(name: str, boolvec: JArray(JBoolean), ncoords: int, /) -> None
         * set(name: str, mat: NDArray[(2, 3), Float], /) -> None
         * set(name: str, mat: NDArray[(4, 4), Float], /) -> None
         * set(name: str, mat: NDArray[(4, 4), Float], use3x3: bool, /) -> None
         * set(name: str, tex: Py5Image, /) -> None
         * set(name: str, vec: JArray(JBoolean), /) -> None
         * set(name: str, vec: NDArray[(Any,), Float], /) -> None
         * set(name: str, vec: NDArray[(Any,), Float], ncoords: int, /) -> None
         * set(name: str, vec: NDArray[(Any,), Int], /) -> None
         * set(name: str, vec: NDArray[(Any,), Int], ncoords: int, /) -> None
         * set(name: str, x: bool, /) -> None
         * set(name: str, x: bool, y: bool, /) -> None
         * set(name: str, x: bool, y: bool, z: bool, /) -> None
         * set(name: str, x: bool, y: bool, z: bool, w: bool, /) -> None
         * set(name: str, x: float, /) -> None
         * set(name: str, x: float, y: float, /) -> None
         * set(name: str, x: float, y: float, z: float, /) -> None
         * set(name: str, x: float, y: float, z: float, w: float, /) -> None
         * set(name: str, x: int, /) -> None
         * set(name: str, x: int, y: int, /) -> None
         * set(name: str, x: int, y: int, z: int, /) -> None
         * set(name: str, x: int, y: int, z: int, w: int, /) -> None

        Parameters
        ----------

        boolvec: JArray(JBoolean)
            modifies all the components of an array/vector uniform variable

        mat: NDArray[(2, 3), Float]
            numpy array of values

        mat: NDArray[(4, 4), Float]
            numpy array of values

        name: str
            the name of the uniform variable to modify

        ncoords: int
            number of coordinates per element, max 4

        tex: Py5Image
            sets the sampler uniform variable to read from this image texture

        use3x3: bool
            enforces the numpy array is 3 x 3

        vec: JArray(JBoolean)
            modifies all the components of an array/vector uniform variable

        vec: NDArray[(Any,), Float]
            numpy array of values to modify all the components of an array/vector uniform variable

        vec: NDArray[(Any,), Int]
            modifies all the components of an array/vector uniform variable

        w: bool
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        w: float
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        w: int
            fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)

        x: bool
            first component of the variable to modify

        x: float
            first component of the variable to modify

        x: int
            first component of the variable to modify

        y: bool
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        y: float
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        y: int
            second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)

        z: bool
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

        z: float
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

        z: int
            third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)

        Notes
        -----

        Sets the uniform variables inside the shader to modify the effect while the
        program is running.
        """
        return self._instance.set(*args)
