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
import functools

import numpy as np
from jpype import JClass

from .vector import Py5Vector


_PVector = JClass('processing.core.PVector')
_PMatrix2D = JClass('processing.core.PMatrix2D')
_PMatrix3D = JClass('processing.core.PMatrix3D')


# the next four functions are used by decorators in various places to do
# conversions
def _numpy_to_pvector(array):
    if array.shape in [(2,), (3,)]:
        return _PVector(*array.tolist())
    else:
        raise RuntimeError(
            'numpy array is the wrong size to convert to a pvector')


def _py5vector_to_pvector(vec):
    if vec.dim in [2, 3]:
        return _PVector(*vec.tolist())
    else:
        raise RuntimeError(
            'Py5Vector must be 2D or 3D to convert to a pvector')


def _numpy_to_pmatrix2d(array):
    return _PMatrix2D(*array.flatten().tolist())


def _numpy_to_pmatrix3d(array):
    return _PMatrix3D(*array.flatten().tolist())


# the next three functions are only used for the jpype conversion customizer
# they are registered in java_conversion.py
def _numpy_to_pvector_converter(jcls, array):
    return _numpy_to_pvector(array)


def _py5vector_to_pvector_converter(jcls, array):
    return _py5vector_to_pvector(array)


def _numpy_to_pmatrix_converter(jcls, array):
    if array.shape == (2, 3):
        return _numpy_to_pmatrix2d(array)
    elif array.shape == (4, 4):
        return _numpy_to_pmatrix3d(array)
    else:
        raise RuntimeError(
            'numpy array is the wrong size to convert to a pmatrix')


def _pvector_to_py5vector(pvector):
    return Py5Vector(pvector.x, pvector.y, pvector.z)


def _pmatrix2d_to_numpy(pmatrix2d):
    return np.array([[pmatrix2d.m00, pmatrix2d.m01, pmatrix2d.m02],
                     [pmatrix2d.m10, pmatrix2d.m11, pmatrix2d.m12]])


def _pmatrix3d_to_numpy(pmatrix3d):
    return np.array([[pmatrix3d.m00, pmatrix3d.m01, pmatrix3d.m02, pmatrix3d.m03],
                     [pmatrix3d.m10, pmatrix3d.m11, pmatrix3d.m12, pmatrix3d.m13],
                     [pmatrix3d.m20, pmatrix3d.m21, pmatrix3d.m22, pmatrix3d.m23],
                     [pmatrix3d.m30, pmatrix3d.m31, pmatrix3d.m32, pmatrix3d.m33]])


def _pmatrix_to_numpy(pmatrix):
    if isinstance(pmatrix, _PMatrix2D):
        return _pmatrix2d_to_numpy(pmatrix)
    elif isinstance(pmatrix, _PMatrix3D):
        return _pmatrix3d_to_numpy(pmatrix)
    else:
        raise RuntimeError(
            f'do not know how to convert object of type {type(pmatrix).__name__}')


def _get_matrix_wrapper(f):
    @functools.wraps(f)
    def decorated(self_, *args):
        ret = f(self_)
        if not args:
            return _pmatrix_to_numpy(ret)
        if len(args) == 1:
            target = args[0]
            if (isinstance(target, np.ndarray) and target.shape == (2, 3)
                    and isinstance(ret, _PMatrix2D)):
                target[0, 0] = ret.m00
                target[0, 1] = ret.m01
                target[0, 2] = ret.m02
                target[1, 0] = ret.m10
                target[1, 1] = ret.m11
                target[1, 2] = ret.m12
                return target
            elif (isinstance(target, np.ndarray) and target.shape == (4, 4)
                    and isinstance(ret, _PMatrix3D)):
                target[0, 0] = ret.m00
                target[0, 1] = ret.m01
                target[0, 2] = ret.m02
                target[0, 3] = ret.m03
                target[1, 0] = ret.m10
                target[1, 1] = ret.m11
                target[1, 2] = ret.m12
                target[1, 3] = ret.m13
                target[2, 0] = ret.m20
                target[2, 1] = ret.m21
                target[2, 2] = ret.m22
                target[2, 3] = ret.m23
                target[3, 0] = ret.m30
                target[3, 1] = ret.m31
                target[3, 2] = ret.m32
                target[3, 3] = ret.m33
                return target
            raise RuntimeError(
                "target must be a numpy array that matches the size of processing's matrix")
        raise RuntimeError(
            'unexpected arguments passed to set_matrix function')
    return decorated


def _get_pvector_wrapper(f):
    @functools.wraps(f)
    def decorated(self_, *args):
        ret = f(self_, args[0])  # ret will always be a PVector
        if len(args) == 1:
            return _pvector_to_py5vector(ret)
        if len(args) == 2:
            target = args[1]
            if isinstance(target, np.ndarray) and target.shape in [(2,), (3,)]:
                target[0] = ret.x
                target[1] = ret.y
                if target.shape == (3,):
                    target[2] = ret.z
                return target
            if isinstance(target, Py5Vector) and target.dim in [2, 3]:
                target.x = ret.x
                target.y = ret.y
                if target.dim == 3:
                    target.z = ret.z
                return target
            raise RuntimeError(
                "target must be a Py5Vector or a numpy array that matches the size of processing's pvector")
        raise RuntimeError('unexpected arguments passed to function')
    return decorated
