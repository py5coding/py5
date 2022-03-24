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
from __future__ import annotations

from typing import Union
import operator
from collections.abc import Sequence, Iterable
import re

import numpy as np
import numpy.typing as npt


class Py5Vector(Sequence):
    """Class to describe a 2D, 3D, or 4D vector.

    Notes
    -----

    Class to describe a 2D, 3D, or 4D vector. A vector is an entity that has both a
    magnitude and a direction. This datatype stores the components of the vector as
    a set of coordinates. A 3D vector, for example, has ``Py5Vector.x``,
    ``Py5Vector.y``, and ``Py5Vector.z`` values that quantify the vector along the 3
    dimensions X, Y, and Z. The magnitude and direction can be accessed via the
    properties ``Py5Vector.mag`` and ``Py5Vector.heading``.

    In many of the py5 examples, you will see ``Py5Vector`` used to describe a
    position, velocity, or acceleration. For example, if you consider a rectangle
    moving across the screen, at any given instant it has a position (a vector that
    points from the origin to its location), a velocity (the rate at which the
    object's position changes per time unit, expressed as a vector), and
    acceleration (the rate at which the object's velocity changes per time unit,
    expressed as a vector).

    The ``Py5Vector`` class works well with numpy and in most cases you will be able
    to do math operations that combine vectors and numpy arrays.

    To create a vector, you can write code like ``v = Py5Vector(1, 2, 3)``, which
    would create a 3D vector with the x, y, and z values equal to 1, 2, and 3. To
    create a vector of zeros, omit the vector values and specify the desired
    dimension with the ``dim`` parameter, such as ``v = Py5Vector(dim=4)``.

    Internally, Py5Vector stores the vector values in a numpy array. By default, the
    data type (dtype) of that numpy array is the default float size for your
    computer, which is typically a 64 bit float, or ``np.float64``. To create a
    vector with a different float size, pass your desired numpy float dtype to the
    ``dtype`` parameter, like ``v3 = py5.Py5Vector(1 / 3, 1 / 7,
    dtype=np.float16)``.

    When creating a new Py5Vector, the initial vector values need not be discrete
    values. You can provide a list of numbers, a numpy array, or another Py5Vector.
    For example, ``v4 = py5.Py5Vector([1, 2, 3])`` creates a Py5Vector from a list,
    and ``v5 = py5.Py5Vector(v4, 0)`` creates a 4D Py5Vector from a 3D Py5Vector and
    a constant value.

    When creating a new Py5Vector from a single numpy array, py5 will by default
    create its own copy of the numpy array for the Py5Vector to use. To instruct py5
    to instead use the same numpy array and share its data with provided array, set
    the ``copy`` parameter to ``False``, such as ``v6 = py5.Py5Vector(arr,
    copy=False)``.
    """

    def __new__(
            cls,
            *args,
            dim: int = None,
            dtype: type = None,
            copy: bool = True):
        kwarg_dim = dim
        kwarg_dtype = dtype

        dim = 3 if dim is None else dim
        dtype = np.float_ if dtype is None else dtype

        if not isinstance(
                dtype, (type, np.dtype)) or not np.issubdtype(
                dtype, np.floating):
            raise RuntimeError(
                'dtype parameter is not a valid numpy float type (i.e., np.float32, np.float64, etc)')

        if not copy:
            if not (
                len(args) == 1 and isinstance(
                    args[0],
                    np.ndarray) and np.issubdtype(
                    args[0].dtype,
                    np.floating)):
                raise RuntimeError(
                    'When the copy parameter is False, please provide a single properly sized numpy array with a floating dtype for py5 to store vector data')
            if kwarg_dtype is not None and args[0].dtype != kwarg_dtype:
                raise RuntimeError(
                    "When the copy parameter is False, the dtype parameter cannot differ from the provided numpy array's dtype")

        if len(args) == 0:
            data = np.zeros(dim, dtype=dtype)
        elif len(args) == 1 and isinstance(args[0], Iterable):
            arg0 = args[0]
            if not hasattr(arg0, '__len__'):
                arg0 = list(arg0)
            if 2 <= len(arg0) <= 4:
                if isinstance(arg0, Py5Vector):
                    arg0 = arg0._data
                if isinstance(arg0, np.ndarray):
                    if copy:
                        data = arg0.astype(dtype)
                    else:
                        data = arg0
                else:
                    data = np.array(arg0, dtype=dtype)
            else:
                raise RuntimeError(
                    f'Cannot create a Py5Vector with {len(arg0)} values')
        elif 2 <= len(args) <= 4:
            dtype_ = None or kwarg_dtype
            data_ = []
            for i, item in enumerate(args):
                if isinstance(item, (np.ndarray, Py5Vector)):
                    if np.issubdtype(
                            item.dtype,
                            np.floating) or np.issubdtype(
                            item.dtype,
                            np.integer):
                        if kwarg_dtype is None:
                            dtype_ = item.dtype if dtype_ is None else max(
                                dtype_, item.dtype)
                        data_.extend(item.tolist())
                    else:
                        raise RuntimeError(
                            f'Argument {i} is a numpy array with dtype {item.dtype} and cannot be used in a Py5Vector')
                elif isinstance(item, Iterable):
                    data_.extend(item)
                elif isinstance(item, (int, float, np.integer, np.floating)):
                    data_.append(item)
                else:
                    raise RuntimeError(
                        f'Argument {i} has type {type(item).__name__} and cannot be used used in a Py5Vector')
            if 2 <= len(data_) <= 4:
                data = np.array(data_, dtype=dtype_ or dtype)
            else:
                raise RuntimeError(
                    f'Cannot create a Py5Vector with {len(data_)} values')
        else:
            raise RuntimeError(
                f'Cannot create Py5Vector instance with {str(args)}')

        dim = len(data)
        dtype = data.dtype

        if kwarg_dim is not None and dim != kwarg_dim:
            raise RuntimeError(
                f"dim parameter is {kwarg_dim} but Py5Vector values imply dimension of {dim}")
        if kwarg_dtype is not None and dtype != kwarg_dtype:
            raise RuntimeError(
                f"dtype parameter is {kwarg_dtype} but Py5Vector values imply dtype of {dtype}")

        if dim == 2:
            v = object.__new__(Py5Vector2D)
        elif dim == 3:
            v = object.__new__(Py5Vector3D)
        elif dim == 4:
            v = object.__new__(Py5Vector4D)
        else:
            raise RuntimeError(f'Why is dim == {dim}? Please report bug')

        v._data = data

        return v

    def __getattr__(self, name):
        if hasattr(self, '_data') and not (
                set(name) - set('xyzw'[:self._data.size])):
            if 2 <= len(name) <= 4:
                return Py5Vector(
                    self._data[['xyzw'.index(c) for c in name]], dtype=self._data.dtype, copy=True)
            else:
                raise RuntimeError(
                    'Invalid swizzle: length must be between 2 and 4 characters')
        else:
            raise AttributeError(
                f"'Py5Vector' object has no attribute '{name}'")

    def __setattr__(self, name, val):
        if name.startswith('_') or not (hasattr(self, '_data') and not (
                set(name) - set('xyzw'[:self._data.size]))):
            super().__setattr__(name, val)
        elif len(name) == len(set(name)):
            if not isinstance(val, Iterable) or len(val) in [1, len(name)]:
                self._data[['xyzw'.index(c) for c in name]] = val
            else:
                raise RuntimeError(
                    f'Mismatch: value length of {len(val)} cannot be assigned to swizzle of length {len(name)}')
        else:
            raise RuntimeError(
                'Invalid swizzle: repeats are not allowed in assignments')

    def __getitem__(self, key):
        return self._data[key]

    def __setitem__(self, key, val):
        self._data[key] = val

    def __len__(self):
        return self._data.size

    def __iter__(self):
        return self._data.__iter__()

    def __str__(self):
        vals = ', '.join(re.split(r'\s+', str(self._data)[1:-1].strip()))
        return f'Py5Vector{self._data.size}D({vals})'

    def __repr__(self):
        return f'Py5Vector{self._data.size}D{repr(self._data)[5:]}'

    def _run_op(
            self,
            op,
            other,
            opname,
            swap=False,
            inplace=False,
            allow2vectors=False):
        if isinstance(other, Py5Vector):
            if not allow2vectors:
                raise RuntimeError(
                    f"Cannot perform {opname} operation on two Py5Vectors. If you want to do {opname} on the Py5Vector's data elementwise, use the `.data` attribute to access the Py5Vector's data as a numpy array.")
            elif self._data.size != other._data.size:
                raise RuntimeError(
                    f"Cannot perform {opname} operation on a {self._data.size}D Py5Vector a {other._data.size}D Py5Vector. The dimensions must be the same.")
            elif inplace:
                op(self._data[:other._data.size],
                   other._data[:other._data.size])
                return self
            else:
                a, b = (other, self) if swap else (self, other)
                return Py5Vector(op(a._data, b._data),
                                 dim=a._data.size, copy=False)
        else:
            try:
                if inplace:
                    op(self._data, other)
                    return self
                else:
                    a, b = (other, self._data) if swap else (self._data, other)
                    result = op(a, b)
                    return Py5Vector(
                        result, copy=False) if result.ndim == 1 and 2 <= result.size <= 4 else result
            except ValueError as e:
                other_type = 'numpy array' if isinstance(
                    other, np.ndarray) else f'{type(other).__name__} object'
                raise RuntimeError(
                    f'Unable to perform {opname} on a Py5Vector and a {other_type}, probably because of a size mismatch. The error message is: ' +
                    str(e)) from None

    def __add__(self, other):
        return self._run_op(
            operator.add,
            other,
            'addition',
            allow2vectors=True)

    def __iadd__(self, other):
        return self._run_op(
            operator.iadd,
            other,
            'addition',
            inplace=True,
            allow2vectors=True)

    def __radd__(self, other):
        return self._run_op(
            operator.add,
            other,
            'addition',
            swap=True,
            allow2vectors=True)

    def __sub__(self, other):
        return self._run_op(
            operator.sub,
            other,
            'subtraction',
            allow2vectors=True)

    def __isub__(self, other):
        return self._run_op(
            operator.isub,
            other,
            'subtraction',
            inplace=True,
            allow2vectors=True)

    def __rsub__(self, other):
        return self._run_op(
            operator.sub,
            other,
            'subtraction',
            swap=True,
            allow2vectors=True)

    def __mul__(self, other):
        return self._run_op(operator.mul, other, 'multiplication')

    def __imul__(self, other):
        return self._run_op(
            operator.imul,
            other,
            'multiplication',
            inplace=True)

    def __rmul__(self, other):
        return self._run_op(operator.mul, other, 'multiplication', swap=True)

    def __truediv__(self, other):
        return self._run_op(operator.truediv, other, 'division')

    def __itruediv__(self, other):
        return self._run_op(operator.itruediv, other, 'division', inplace=True)

    def __rtruediv__(self, other):
        return self._run_op(operator.truediv, other, 'division', swap=True)

    def __floordiv__(self, other):
        return self._run_op(operator.floordiv, other, 'integer division')

    def __ifloordiv__(self, other):
        return self._run_op(
            operator.ifloordiv,
            other,
            'integer division',
            inplace=True)

    def __rfloordiv__(self, other):
        return self._run_op(
            operator.floordiv,
            other,
            'integer division',
            swap=True)

    def __mod__(self, other):
        return self._run_op(operator.mod, other, 'modular division')

    def __imod__(self, other):
        return self._run_op(
            operator.imod,
            other,
            'modular division',
            inplace=True)

    def __rmod__(self, other):
        return self._run_op(operator.mod, other, 'modular division', swap=True)

    def __divmod__(self, other):
        return self._run_op(
            operator.floordiv, other, 'integer division'), self._run_op(
            operator.mod, other, 'modular division')

    def __rdivmod__(self, other):
        return self._run_op(
            operator.floordiv, other, 'integer division', swap=True), self._run_op(
            operator.mod, other, 'modular division', swap=True)

    def __pow__(self, other):
        return self._run_op(operator.pow, other, 'power')

    def __ipow__(self, other):
        return self._run_op(operator.ipow, other, 'power', inplace=True)

    def __matmul__(self, other):
        return self._run_op(operator.matmul, other, 'matrix multiplication')

    def __rmatmul__(self, other):
        return self._run_op(
            operator.matmul,
            other,
            'matrix multiplication',
            swap=True)

    def __imatmul__(self, other):
        return self._run_op(operator.imatmul, other, 'matrix multiplication')

    def __pos__(self):
        return self

    def __neg__(self):
        return Py5Vector(-self._data, copy=False)

    def __abs__(self):
        return Py5Vector(np.abs(self._data), copy=False)

    def __round__(self):
        return Py5Vector(np.round(self._data), copy=False)

    def __bool__(self):
        return any(self._data != 0.0)

    def __eq__(self, other):
        return isinstance(other, type(self)) and all(self._data == other._data)

    def __ne__(self, other):
        return not isinstance(
            other, type(self)) or any(
            self._data != other._data)

    # *** BEGIN METHODS ***

    def astype(self, dtype) -> Py5Vector:
        """Create a new Py5Vector instance with a specified numpy dtype.

        Parameters
        ----------

        dtype
            numpy floating dtype

        Notes
        -----

        Create a new Py5Vector instance with a specified numpy dtype. Only floating
        types (``np.float16``, ``np.float32``, ``np.float64``, and ``np.float128``) are
        allowed.
        """
        return Py5Vector(self._data, dtype=dtype, copy=True)

    def tolist(self) -> list[float]:
        """Return the vector's values as a list.

        Notes
        -----

        Return the vector's values as a list. The length of the list will be equal to
        the vector's dimension.
        """
        return self._data.tolist()

    def _get_x(self) -> float:
        """The vector's x dimension value.

        Notes
        -----

        The vector's x dimension value. This is the vector's 1st dimension.
        """
        return self._data[0]

    def _set_x(self, val: float) -> None:
        """The vector's x dimension value.

        Notes
        -----

        The vector's x dimension value. This is the vector's 1st dimension.
        """
        self._data[0] = val

    def _get_y(self) -> float:
        """The vector's y dimension value.

        Notes
        -----

        The vector's y dimension value. This is the vector's 2nd dimension.
        """
        return self._data[1]

    def _set_y(self, val: float) -> None:
        """The vector's y dimension value.

        Notes
        -----

        The vector's y dimension value. This is the vector's 2nd dimension.
        """
        self._data[1] = val

    def _get_data(self) -> float:
        """Numpy array used to store the vector's data values.

        Notes
        -----

        Numpy array used to store the vector's data values.
        """
        return self._data

    def _get_copy(self) -> Py5Vector:
        """Create an identical copy of this Py5Vector instance.

        Notes
        -----

        Create an identical copy of this Py5Vector instance.
        """
        return Py5Vector(self._data, dtype=self._data.dtype, copy=True)

    def _get_dim(self) -> int:
        """The vector's dimension.

        Notes
        -----

        The vector's dimension. This will be either 2, 3, or 4.
        """
        return self._data.size

    def _get_dtype(self) -> type:
        """Vector data type.

        Notes
        -----

        Vector data type. This will be one of ``np.float16``, ``np.float32``,
        ``np.float64``, or ``np.float128``.
        """
        return self._data.dtype

    x: float = property(_get_x, _set_x, doc="""The vector's x dimension value.

        Notes
        -----

        The vector's x dimension value. This is the vector's 1st dimension.""")
    y: float = property(_get_y, _set_y, doc="""The vector's y dimension value.

        Notes
        -----

        The vector's y dimension value. This is the vector's 2nd dimension.""")
    data: npt.NDArray[np.floating] = property(
        _get_data, doc="""Numpy array used to store the vector's data values.

        Notes
        -----

        Numpy array used to store the vector's data values.""")
    copy = property(
        _get_copy,
        doc="""Create an identical copy of this Py5Vector instance.

        Notes
        -----

        Create an identical copy of this Py5Vector instance.""")
    dim: int = property(_get_dim, doc="""The vector's dimension.

        Notes
        -----

        The vector's dimension. This will be either 2, 3, or 4.""")
    dtype: type = property(_get_dtype, doc="""Vector data type.

        Notes
        -----

        Vector data type. This will be one of ``np.float16``, ``np.float32``,
        ``np.float64``, or ``np.float128``.""")

    def _run_calc(self, other, calc, name, maybe_vector=False):
        other_type = 'numpy array' if isinstance(
            other, np.ndarray) else f'{type(other).__name__} object'
        if isinstance(other, Py5Vector):
            if self._data.size == other._data.size:
                other = other._data
            else:
                raise RuntimeError(
                    f'Py5Vector dimensions must be the same to calculate the {name} two Py5Vectors')

        if isinstance(other, np.ndarray):
            try:
                result = calc(self._data, other)
                if result.ndim == 0:
                    return float(result)
                if maybe_vector and result.ndim == 1 and 2 <= result.size <= 4:
                    return Py5Vector(result, copy=False)
                else:
                    return result
            except ValueError as e:
                raise RuntimeError(
                    f'Unable to calculate the {name} between a Py5Vector and {other_type}, probably because of a size mismatch. The error message is: ' +
                    str(e)) from None
        else:
            raise RuntimeError(
                f'Do not know how to calculate the {name} {type(self).__name__} and {type(other).__name__}')

    def lerp(self,
             other: Union[Py5Vector,
                          np.ndarray],
             amt: Union[float,
                        np.ndarray]) -> Union[Py5Vector,
                                              np.ndarray[np.floating]]:
        """Calculates a vector between two vectors at a specific increment.

        Parameters
        ----------

        amt: Union[float, np.ndarray]
            float between 0.0 and 1.0

        other: Union[Py5Vector, np.ndarray]
            other vector to interpolate between

        Notes
        -----

        Calculates a vector between two vectors at a specific increment. The two vectors
        must have the same dimension. The ``amt`` parameter is the amount to interpolate
        between the two values where 0.0 equal to the first point, 0.1 is very near the
        first point, 0.5 is half-way in between, etc. If the ``amt`` parameter is
        greater than 1.0 or less than 0.0, the interpolated vector will be outside of
        the range specified by the two vectors.

        This method is similar to ``lerp()`` and ``lerp_color()``, but for vectors
        instead of numbers or colors.
        """
        return self._run_calc(other,
                              lambda s,
                              o: s + (o - s) * amt,
                              'lerp of',
                              maybe_vector=True)

    def dist(self, other: Union[Py5Vector, np.ndarray]
             ) -> Union[Py5Vector, np.ndarray[np.floating]]:
        """Calculate the distance between two vectors.

        Parameters
        ----------

        other: Union[Py5Vector, np.ndarray]
            vector to calculate the distance from

        Notes
        -----

        Calculate the distance between two vectors.
        """
        return self._run_calc(
            other,
            lambda s,
            o: np.sqrt(
                np.sum(
                    (s - o)**2,
                    axis=-1)),
            'distance between')

    def dot(self, other: Union[Py5Vector, np.ndarray]
            ) -> Union[float, np.ndarray[np.floating]]:
        """Calculate the dot product between two vectors.

        Parameters
        ----------

        other: Union[Py5Vector, np.ndarray]
            vector to calculate the dot product with

        Notes
        -----

        Calculate the dot product between two vectors.
        """
        return self._run_calc(other, lambda s, o: (
            s * o).sum(axis=-1), 'dot product for')

    def angle_between(self,
                      other: Union[Py5Vector,
                                   np.ndarray]) -> Union[Py5Vector,
                                                         np.ndarray[np.floating]]:
        """Measure the angle between two vectors.

        Parameters
        ----------

        other: Union[Py5Vector, np.ndarray]
            vector to measure angle between

        Notes
        -----

        Measure the angle between two vectors.
        """
        return self._run_calc(other, lambda s, o: np.arccos(
            ((s / np.sum(s**2)**0.5) * (o / np.sum(o**2, axis=-1)**0.5)).sum(axis=-1)), 'angle between')

    def cross(self,
              other: Union[Py5Vector,
                           np.ndarray]) -> Union[float,
                                                 Py5Vector,
                                                 np.ndarray[np.floating]]:
        """Calculate the vector cross product of two 3D vectors.

        Parameters
        ----------

        other: Union[Py5Vector, np.ndarray]
            2D or 3D vector to calculate the cross product with

        Notes
        -----

        Calculate the vector cross product of two 3D vectors. If one of the vectors is a
        2D vector, its z-value is assumed to be zero and the vector cross product is
        calculated normally. If both vectors are 2D vectors, the returned value will be
        the wedge product.
        """
        if self._data.size == 4 or isinstance(other, Py5Vector4D):
            raise RuntimeError(
                'Cannot calculate the cross product with a 4D Py5Vector')
        elif self._data.size == 2:
            maybe_vector = isinstance(other, Py5Vector3D)
            if isinstance(other, Py5Vector):
                other = other._data
            return self._run_calc(
                other,
                np.cross,
                'cross product of',
                maybe_vector=maybe_vector)
        else:  # self._data.size == 3:
            if isinstance(other, Py5Vector):
                other = other._data
            return self._run_calc(
                other,
                np.cross,
                'cross product of',
                maybe_vector=True)

    def _get_mag(self) -> float:
        """The vector's magnitude.

        Notes
        -----

        The vector's magnitude. Setting this property to a non-negative number will
        adjust the vector's magnitude to that value. Negative values will result in an
        error.
        """
        return float(np.sum(self._data**2)**0.5)

    def set_mag(self, mag: float) -> Py5Vector:
        """The vector's magnitude.

        Notes
        -----

        The vector's magnitude. Setting this property to a non-negative number will
        adjust the vector's magnitude to that value. Negative values will result in an
        error.
        """
        if mag < 0:
            raise RuntimeError('Cannot set magnitude to a negative number')
        elif mag == 0:
            self._data[:] = 0
        else:
            self.normalize()
            self._data *= mag
        return self

    def _get_mag_sq(self) -> float:
        """The square of the vector's magnitude.

        Notes
        -----

        The square of the vector's magnitude. Setting this property to a non-negative
        number will adjust the vector's squared magnitude to that value. Negative values
        will result in an error.
        """
        return float(np.sum(self._data**2))

    def set_mag_sq(self, mag_sq: float) -> Py5Vector:
        """The square of the vector's magnitude.

        Notes
        -----

        The square of the vector's magnitude. Setting this property to a non-negative
        number will adjust the vector's squared magnitude to that value. Negative values
        will result in an error.
        """
        if mag_sq < 0:
            raise RuntimeError(
                'Cannot set squared magnitude to a negative number')
        elif mag_sq == 0:
            self._data[:] = 0
        else:
            self.normalize()
            self._data *= mag_sq**0.5
        return self

    def normalize(self) -> Py5Vector:
        """Normalize the vector by setting the vector's magnitude to 1.0.

        Notes
        -----

        Normalize the vector by setting the vector's magnitude to 1.0. This method
        cannot be used on a vector of zeros, because a vector of zeros cannot be
        normalized.
        """
        mag = np.sum(self._data**2)**0.5
        if mag > 0:
            self._data /= mag
            return self
        else:
            raise RuntimeError('Cannot normalize Py5Vector of zeros')

    def _get_norm(self) -> Py5Vector:
        """Normalized copy of the vector.

        Notes
        -----

        Normalized copy of the vector. The normalized copy will have a magnitude of 1.0.
        This property cannot be used on a vector of zeros, because a vector of zeros
        cannot be normalized.
        """
        return self.copy.normalize()

    mag: float = property(_get_mag, set_mag, doc="""The vector's magnitude.

        Notes
        -----

        The vector's magnitude. Setting this property to a non-negative number will
        adjust the vector's magnitude to that value. Negative values will result in an
        error.""")
    mag_sq: float = property(
        _get_mag_sq,
        set_mag_sq,
        doc="""The square of the vector's magnitude.

        Notes
        -----

        The square of the vector's magnitude. Setting this property to a non-negative
        number will adjust the vector's squared magnitude to that value. Negative values
        will result in an error.""")
    norm: Py5Vector = property(_get_norm, doc="""Normalized copy of the vector.

        Notes
        -----

        Normalized copy of the vector. The normalized copy will have a magnitude of 1.0.
        This property cannot be used on a vector of zeros, because a vector of zeros
        cannot be normalized.""")

    def set_limit(self, max_mag: float) -> Py5Vector:
        """Constrain the vector's magnitude to a specified value.

        Parameters
        ----------

        max_mag: float
            maximum vector magnitude

        Notes
        -----

        Constrain the vector's magnitude to a specified value. If the vector's magnitude
        is already less than or equal to ``max_mag``, this method will have no effect.
        If the vector's magnitude is larger, it will be set to ``max_mag``. The
        ``max_mag`` parameter cannot be a negative number.
        """
        if max_mag < 0:
            raise RuntimeError('Cannot set limit to a negative number')
        elif max_mag == 0:
            self._data[:] = 0
        else:
            mag_sq = np.sum(self._data**2)
            if mag_sq > max_mag * max_mag:
                self._data *= max_mag / (mag_sq**0.5)
        return self

    def _get_heading(self) -> Union(float, tuple[float]):
        """The vector's heading, measured in radians.

        Notes
        -----

        The vector's heading, measured in radians. The heading will be measured with 1,
        2, or 3 numbers for 2D, 3D, or 4D vectors, respectively.

        For 2D vectors, the heading angle is the counter clockwise rotation of the
        vector relative to the positive x axis.

        For 3D vectors, the heading values follow the ISO convention for spherical
        coordinates. The first heading value, inclination, is the angle relative to the
        positive z axis. The second heading value, azimuth, is the counter clockwise
        rotation of the vector around the z axis relative to the positive x axis. Note
        that this is slightly different from p5's ``fromAngles()`` function, which also
        follows the ISO convention but measures angles relative to the top of the screen
        (negative y axis).

        For 4D vectors, the heading values follow the spherical coordinate system
        defined in Wikipedia's N-sphere article. The first heading value is the rotation
        around the zw plane relative to the positive x axis. The second heading value is
        the rotation around the xw plane relative to the positive y axis. The third
        heading value is the rotation around the xy plane relative to the positive z
        axis.
        """
        if self._data.size == 2:
            return float(np.arctan2(self._data[1], self._data[0]))
        elif self._data.size == 3:
            return (float(np.arctan2((self._data[:2]**2).sum()**0.5, self._data[2])),
                    float(np.arctan2(self._data[1], self._data[0])))
        else:
            return (float(np.arctan2((self._data[1:]**2).sum()**0.5, self._data[0])),
                    float(np.arctan2((self._data[2:]**2).sum()**0.5, self._data[1])),
                    float(2 * np.arctan2(self._data[3], self._data[2] + (self._data[2:]**2).sum()**0.5)))

    def set_heading(self, *heading) -> Py5Vector:
        """Align vector with the specified heading.

        Parameters
        ----------

        heading
            heading values in radians

        Notes
        -----

        Align vector with the specified heading. Use 1, 2, or 3 heading values for 2D,
        3D, or 4D vectors, respectively. The number of heading values passed to this
        method must match the vector's actual dimension.

        For 2D vectors, the heading angle is the counter clockwise rotation of the
        vector relative to the positive x axis.

        For 3D vectors, the heading values follow the ISO convention for spherical
        coordinates. The first heading value, inclination, is the angle relative to the
        positive z axis. The second heading value, azimuth, is the counter clockwise
        rotation of the vector around the z axis relative to the positive x axis. Note
        that this is slightly different from p5's ``fromAngles()`` function, which also
        follows the ISO convention but measures angles relative to the top of the screen
        (negative y axis).

        For 4D vectors, the heading values follow the spherical coordinate system
        defined in Wikipedia's N-sphere article. The first heading value is the rotation
        around the zw plane relative to the positive x axis. The second heading value is
        the rotation around the xw plane relative to the positive y axis. The third
        heading value is the rotation around the xy plane relative to the positive z
        axis.
        """
        if len(heading) == 1 and isinstance(heading[0], Iterable):
            heading = heading[0]

        mag = self._get_mag()
        if len(heading) == 1 and self._data.size == 2:
            theta = heading[0]
            x = mag * np.cos(theta)
            y = mag * np.sin(theta)
            self._data[:] = [x, y]
            return self
        elif len(heading) == 2 and self._data.size == 3:
            theta, phi = heading
            sin_theta = np.sin(theta)
            x = mag * np.cos(phi) * sin_theta
            y = mag * np.sin(phi) * sin_theta
            z = mag * np.cos(theta)
            self._data[:] = [x, y, z]
            return self
        elif len(heading) == 3 and self._data.size == 4:
            phi1, phi2, phi3 = heading
            sin_phi1 = np.sin(phi1)
            sin_phi2 = np.sin(phi2)
            x1 = mag * np.cos(phi1)
            x2 = mag * sin_phi1 * np.cos(phi2)
            x3 = mag * sin_phi1 * sin_phi2 * np.cos(phi3)
            x4 = mag * sin_phi1 * sin_phi2 * np.sin(phi3)
            self._data[:] = [x1, x2, x3, x4]
            return self
        else:
            raise RuntimeError(
                f'This Py5Vector has dimension {self._data.size} and requires {self._data.size - 1} values to set the heading, not {len(heading)}')

    heading: tuple[float] = property(
        _get_heading, set_heading, doc="""The vector's heading, measured in radians.

        Notes
        -----

        The vector's heading, measured in radians. The heading will be measured with 1,
        2, or 3 numbers for 2D, 3D, or 4D vectors, respectively.

        For 2D vectors, the heading angle is the counter clockwise rotation of the
        vector relative to the positive x axis.

        For 3D vectors, the heading values follow the ISO convention for spherical
        coordinates. The first heading value, inclination, is the angle relative to the
        positive z axis. The second heading value, azimuth, is the counter clockwise
        rotation of the vector around the z axis relative to the positive x axis. Note
        that this is slightly different from p5's ``fromAngles()`` function, which also
        follows the ISO convention but measures angles relative to the top of the screen
        (negative y axis).

        For 4D vectors, the heading values follow the spherical coordinate system
        defined in Wikipedia's N-sphere article. The first heading value is the rotation
        around the zw plane relative to the positive x axis. The second heading value is
        the rotation around the xw plane relative to the positive y axis. The third
        heading value is the rotation around the xy plane relative to the positive z
        axis.""")

    @classmethod
    def from_heading(cls, *heading, dtype: int = np.float_) -> Py5Vector:
        """Class method to create a new vector with a given heading, measured in radians.

        Parameters
        ----------

        dtype: int = np.float_
            dtype of new vector to create

        heading
            heading values in radians

        Notes
        -----

        Class method to create a new vector with a given heading, measured in radians.
        Use 1, 2, or 3 heading values for 2D, 3D, or 4D vectors, respectively.

        For 2D vectors, the heading angle is the counter clockwise rotation of the
        vector relative to the positive x axis.

        For 3D vectors, the heading values follow the ISO convention for spherical
        coordinates. The first heading value, inclination, is the angle relative to the
        positive z axis. The second heading value, azimuth, is the counter clockwise
        rotation of the vector around the z axis relative to the positive x axis. Note
        that this is slightly different from p5's ``fromAngles()`` function, which also
        follows the ISO convention but measures angles relative to the top of the screen
        (negative y axis).

        For 4D vectors, the heading values follow the spherical coordinate system
        defined in Wikipedia's N-sphere article. The first heading value is the rotation
        around the zw plane relative to the positive x axis. The second heading value is
        the rotation around the xw plane relative to the positive y axis. The third
        heading value is the rotation around the xy plane relative to the positive z
        axis.
        """
        if len(heading) == 1 and isinstance(heading[0], Iterable):
            heading = heading[0]

        if len(heading) == 1:
            return Py5Vector(1, 0, dtype=dtype).set_heading(*heading)
        elif len(heading) == 2:
            return Py5Vector(1, 0, 0, dtype=dtype).set_heading(*heading)
        elif len(heading) == 3:
            return Py5Vector(1, 0, 0, 0, dtype=dtype).set_heading(*heading)
        else:
            raise RuntimeError(
                f'Cannot create a Py5Vector from {len(heading)} arguments')

    @classmethod
    def random(cls, dim: int, *, dtype: type = np.float_) -> Py5Vector:
        """Create a new vector with random values.

        Parameters
        ----------

        dim: int
            dimension of the random vector to create

        dtype: type = np.float_
            dtype of the random vector to create

        Notes
        -----

        Create a new vector with random values. Use the ``dim`` parameter to specify if
        the vector should have 2, 3, or 4 dimensions.

        The new vector will have a magnitude of 1 and a heading that is uniformly
        distributed across all possible headings for a vector with the given dimension.

        When used as a ``Py5Vector`` class method, the ``dim`` parameter is required to
        specify what the new vector's dimension should be. When used as a class method
        for the ``Py5Vector2D``, ``Py5Vector3D``, or ``Py5Vector4D`` child classes, the
        ``dim`` parameter is optional and will default to the dimension implied by the
        specific class. When used as a method on a vector instance, the ``dim``
        parameter is also optional and will default to the vector instance's dimension.
        See the example code for examples of all of these use cases.
        """
        if dim == 2:
            return Py5Vector(
                np.cos(
                    angle := np.random.rand() *
                    2 *
                    np.pi),
                np.sin(angle),
                dtype=dtype)
        elif dim == 3:
            return Py5Vector((v := np.random.randn(3).astype(
                dtype)) / (v**2).sum()**0.5, copy=False)
        elif dim == 4:
            return Py5Vector((v := np.random.randn(4).astype(
                dtype)) / (v**2).sum()**0.5, copy=False)
        else:
            raise RuntimeError(
                f'Cannot create a random Py5Vector with dimension {dim}')

    # *** END METHODS ***


class Py5Vector2D(Py5Vector):
    """Class to describe a 2D, 3D, or 4D vector.

    Notes
    -----

    Class to describe a 2D, 3D, or 4D vector. A vector is an entity that has both a
    magnitude and a direction. This datatype stores the components of the vector as
    a set of coordinates. A 3D vector, for example, has ``Py5Vector.x``,
    ``Py5Vector.y``, and ``Py5Vector.z`` values that quantify the vector along the 3
    dimensions X, Y, and Z. The magnitude and direction can be accessed via the
    properties ``Py5Vector.mag`` and ``Py5Vector.heading``.

    In many of the py5 examples, you will see ``Py5Vector`` used to describe a
    position, velocity, or acceleration. For example, if you consider a rectangle
    moving across the screen, at any given instant it has a position (a vector that
    points from the origin to its location), a velocity (the rate at which the
    object's position changes per time unit, expressed as a vector), and
    acceleration (the rate at which the object's velocity changes per time unit,
    expressed as a vector).

    The ``Py5Vector`` class works well with numpy and in most cases you will be able
    to do math operations that combine vectors and numpy arrays.

    To create a vector, you can write code like ``v = Py5Vector(1, 2, 3)``, which
    would create a 3D vector with the x, y, and z values equal to 1, 2, and 3. To
    create a vector of zeros, omit the vector values and specify the desired
    dimension with the ``dim`` parameter, such as ``v = Py5Vector(dim=4)``.

    Internally, Py5Vector stores the vector values in a numpy array. By default, the
    data type (dtype) of that numpy array is the default float size for your
    computer, which is typically a 64 bit float, or ``np.float64``. To create a
    vector with a different float size, pass your desired numpy float dtype to the
    ``dtype`` parameter, like ``v3 = py5.Py5Vector(1 / 3, 1 / 7,
    dtype=np.float16)``.

    When creating a new Py5Vector, the initial vector values need not be discrete
    values. You can provide a list of numbers, a numpy array, or another Py5Vector.
    For example, ``v4 = py5.Py5Vector([1, 2, 3])`` creates a Py5Vector from a list,
    and ``v5 = py5.Py5Vector(v4, 0)`` creates a 4D Py5Vector from a 3D Py5Vector and
    a constant value.

    When creating a new Py5Vector from a single numpy array, py5 will by default
    create its own copy of the numpy array for the Py5Vector to use. To instruct py5
    to instead use the same numpy array and share its data with provided array, set
    the ``copy`` parameter to ``False``, such as ``v6 = py5.Py5Vector(arr,
    copy=False)``.
    """

    def __new__(cls, *args, dtype: type = np.float_):
        return super().__new__(cls, *args, dim=2, dtype=dtype)

    # *** BEGIN METHODS ***

    def rotate(self, angle: float) -> Py5Vector2D:
        """Rotate vector by a specified angle.

        Methods
        -------

        You can use any of the following signatures:

         * rotate(angle: float) -> Py5Vector2D
         * rotate(angle: float, dim: Union[int, str]) -> Py5Vector3D

        Parameters
        ----------

        angle: float
            angle of rotation, measured in radians

        dim: Union[int, str]
            dimension to rotate around

        Notes
        -----

        Rotate vector by a specified angle. This method is only applicable to 2D and 3D
        vectors. Use the ``angle`` parameter to specify the rotation angle. To rotate 3D
        vectors, you must use the ``dim`` parameter to specify which dimension to rotate
        around. The dimension can be specified with the values 1, 2, or 3, or by using
        the strings ``'x'``, ``'y'``, or ``'z'``.

        A 2D vector will be rotated in the counter-clockwise direction for positive
        ``angle`` values and in the clockwise direction for negative ``angle`` values.

        A 3D vector's rotation will follow the right-hand rule. Using your right hand,
        point your thumb in the direction of the axis to rotate around. Your fingers
        will curl in the direction of rotation when the ``angle`` parameter is positive.
        """
        sin_angle = np.sin(angle)
        cos_angle = np.cos(angle)
        rot = np.array([[cos_angle, -sin_angle], [sin_angle, cos_angle]])
        self._data[:] = rot @ self._data
        return self

    # *** END METHODS ***

    @classmethod
    def random(cls, dim: int = 2, *, dtype: type = np.float_) -> Py5Vector2D:
        """Create a new vector with random values.

        Parameters
        ----------

        dim: int
            dimension of the random vector to create

        dtype: type = np.float_
            dtype of the random vector to create

        Notes
        -----

        Create a new vector with random values. Use the ``dim`` parameter to specify if
        the vector should have 2, 3, or 4 dimensions.

        The new vector will have a magnitude of 1 and a heading that is uniformly
        distributed across all possible headings for a vector with the given dimension.

        When used as a ``Py5Vector`` class method, the ``dim`` parameter is required to
        specify what the new vector's dimension should be. When used as a class method
        for the ``Py5Vector2D``, ``Py5Vector3D``, or ``Py5Vector4D`` child classes, the
        ``dim`` parameter is optional and will default to the dimension implied by the
        specific class. When used as a method on a vector instance, the ``dim``
        parameter is also optional and will default to the vector instance's dimension.
        See the example code for examples of all of these use cases.
        """
        return super().random(dim, dtype=dtype)


class Py5Vector3D(Py5Vector):
    """Class to describe a 2D, 3D, or 4D vector.

    Notes
    -----

    Class to describe a 2D, 3D, or 4D vector. A vector is an entity that has both a
    magnitude and a direction. This datatype stores the components of the vector as
    a set of coordinates. A 3D vector, for example, has ``Py5Vector.x``,
    ``Py5Vector.y``, and ``Py5Vector.z`` values that quantify the vector along the 3
    dimensions X, Y, and Z. The magnitude and direction can be accessed via the
    properties ``Py5Vector.mag`` and ``Py5Vector.heading``.

    In many of the py5 examples, you will see ``Py5Vector`` used to describe a
    position, velocity, or acceleration. For example, if you consider a rectangle
    moving across the screen, at any given instant it has a position (a vector that
    points from the origin to its location), a velocity (the rate at which the
    object's position changes per time unit, expressed as a vector), and
    acceleration (the rate at which the object's velocity changes per time unit,
    expressed as a vector).

    The ``Py5Vector`` class works well with numpy and in most cases you will be able
    to do math operations that combine vectors and numpy arrays.

    To create a vector, you can write code like ``v = Py5Vector(1, 2, 3)``, which
    would create a 3D vector with the x, y, and z values equal to 1, 2, and 3. To
    create a vector of zeros, omit the vector values and specify the desired
    dimension with the ``dim`` parameter, such as ``v = Py5Vector(dim=4)``.

    Internally, Py5Vector stores the vector values in a numpy array. By default, the
    data type (dtype) of that numpy array is the default float size for your
    computer, which is typically a 64 bit float, or ``np.float64``. To create a
    vector with a different float size, pass your desired numpy float dtype to the
    ``dtype`` parameter, like ``v3 = py5.Py5Vector(1 / 3, 1 / 7,
    dtype=np.float16)``.

    When creating a new Py5Vector, the initial vector values need not be discrete
    values. You can provide a list of numbers, a numpy array, or another Py5Vector.
    For example, ``v4 = py5.Py5Vector([1, 2, 3])`` creates a Py5Vector from a list,
    and ``v5 = py5.Py5Vector(v4, 0)`` creates a 4D Py5Vector from a 3D Py5Vector and
    a constant value.

    When creating a new Py5Vector from a single numpy array, py5 will by default
    create its own copy of the numpy array for the Py5Vector to use. To instruct py5
    to instead use the same numpy array and share its data with provided array, set
    the ``copy`` parameter to ``False``, such as ``v6 = py5.Py5Vector(arr,
    copy=False)``.
    """

    def __new__(cls, *args, dtype: type = np.float_):
        return super().__new__(cls, *args, dim=3, dtype=dtype)

    def _get_z(self) -> float:
        """The vector's z dimension value.

        Notes
        -----

        The vector's z dimension value. This is the vector's 3rd dimension, and is only
        applicable to 3D and 4D vectors.
        """
        return self._data[2]

    def _set_z(self, val: float) -> None:
        """The vector's z dimension value.

        Notes
        -----

        The vector's z dimension value. This is the vector's 3rd dimension, and is only
        applicable to 3D and 4D vectors.
        """
        self._data[2] = val

    z: float = property(_get_z, _set_z, doc="""The vector's z dimension value.

        Notes
        -----

        The vector's z dimension value. This is the vector's 3rd dimension, and is only
        applicable to 3D and 4D vectors.""")

    # *** BEGIN METHODS ***

    def rotate(self, angle: float, dim: Union[int, str]) -> Py5Vector3D:
        """Rotate vector by a specified angle.

        Methods
        -------

        You can use any of the following signatures:

         * rotate(angle: float) -> Py5Vector2D
         * rotate(angle: float, dim: Union[int, str]) -> Py5Vector3D

        Parameters
        ----------

        angle: float
            angle of rotation, measured in radians

        dim: Union[int, str]
            dimension to rotate around

        Notes
        -----

        Rotate vector by a specified angle. This method is only applicable to 2D and 3D
        vectors. Use the ``angle`` parameter to specify the rotation angle. To rotate 3D
        vectors, you must use the ``dim`` parameter to specify which dimension to rotate
        around. The dimension can be specified with the values 1, 2, or 3, or by using
        the strings ``'x'``, ``'y'``, or ``'z'``.

        A 2D vector will be rotated in the counter-clockwise direction for positive
        ``angle`` values and in the clockwise direction for negative ``angle`` values.

        A 3D vector's rotation will follow the right-hand rule. Using your right hand,
        point your thumb in the direction of the axis to rotate around. Your fingers
        will curl in the direction of rotation when the ``angle`` parameter is positive.
        """
        sin_angle = np.sin(angle)
        cos_angle = np.cos(angle)
        if dim in [1, 'x']:
            rot = np.array(
                [[1, 0, 0], [0, cos_angle, -sin_angle], [0, sin_angle, cos_angle]])
        elif dim in [2, 'y']:
            rot = np.array([[cos_angle, 0, sin_angle], [
                           0, 1, 0], [-sin_angle, 0, cos_angle]])
        elif dim in [3, 'z']:
            rot = np.array([[cos_angle, -sin_angle, 0],
                           [sin_angle, cos_angle, 0], [0, 0, 1]])
        else:
            raise RuntimeError(
                "dim parameter must be 1, 2, or 3, or one of 'x', 'y', and 'z'")
        self._data[:] = rot @ self._data
        return self

    def rotate_around(self, angle: float, v: Py5Vector3D) -> Py5Vector3D:
        """Rotate around an arbitrary 3D vector.

        Parameters
        ----------

        angle: float
            angle of rotation, measured in radians

        v: Py5Vector3D
            3D vector to rotate vector around

        Notes
        -----

        Rotate around an arbitrary 3D vector. This method is only applicable to 3D
        vectors. Use the ``angle`` parameter to specify the rotation angle and the ``v``
        parameter to specify the vector to rotate around. The ``v`` vector does not need
        to be aligned to any axis or normalized, but it must be a 3D vector and it
        cannot be a vector of zeros.

        The vector's rotation will follow the right-hand rule. Using your right hand,
        point your thumb in the direction of the vector to rotate around. Your fingers
        will curl in the direction of rotation when the ``angle`` parameter is positive.
        """
        if not isinstance(v, Py5Vector3D):
            raise RuntimeError('Can only rotate around another 3D Py5Vector')
        if not v:
            raise RuntimeError('Cannot rotate around a vector of zeros')
        u = v.norm
        ux, uy, uz = u.x, u.y, u.z
        sin, cos = np.sin(angle), np.cos(angle)
        ncosp1 = 1 - cos
        rot = np.array([[cos +
                         ux *
                         ux *
                         ncosp1, ux *
                         uy *
                         ncosp1 -
                         uz *
                         sin, ux *
                         uz *
                         ncosp1 +
                         uy *
                         sin], [uy *
                                ux *
                                ncosp1 +
                                uz *
                                sin, cos +
                                uy *
                                uy *
                                ncosp1, uy *
                                uz *
                                ncosp1 -
                                ux *
                                sin], [uz *
                                       ux *
                                       ncosp1 -
                                       uy *
                                       sin, uz *
                                       uy *
                                       ncosp1 +
                                       ux *
                                       sin, cos +
                                       uz *
                                       uz *
                                       ncosp1]])
        self._data[:] = rot @ self._data
        return self

    # *** END METHODS ***

    @classmethod
    def random(cls, dim: int = 3, *, dtype: type = np.float_) -> Py5Vector3D:
        """Create a new vector with random values.

        Parameters
        ----------

        dim: int
            dimension of the random vector to create

        dtype: type = np.float_
            dtype of the random vector to create

        Notes
        -----

        Create a new vector with random values. Use the ``dim`` parameter to specify if
        the vector should have 2, 3, or 4 dimensions.

        The new vector will have a magnitude of 1 and a heading that is uniformly
        distributed across all possible headings for a vector with the given dimension.

        When used as a ``Py5Vector`` class method, the ``dim`` parameter is required to
        specify what the new vector's dimension should be. When used as a class method
        for the ``Py5Vector2D``, ``Py5Vector3D``, or ``Py5Vector4D`` child classes, the
        ``dim`` parameter is optional and will default to the dimension implied by the
        specific class. When used as a method on a vector instance, the ``dim``
        parameter is also optional and will default to the vector instance's dimension.
        See the example code for examples of all of these use cases.
        """
        return super().random(dim, dtype=dtype)


class Py5Vector4D(Py5Vector):
    """Class to describe a 2D, 3D, or 4D vector.

    Notes
    -----

    Class to describe a 2D, 3D, or 4D vector. A vector is an entity that has both a
    magnitude and a direction. This datatype stores the components of the vector as
    a set of coordinates. A 3D vector, for example, has ``Py5Vector.x``,
    ``Py5Vector.y``, and ``Py5Vector.z`` values that quantify the vector along the 3
    dimensions X, Y, and Z. The magnitude and direction can be accessed via the
    properties ``Py5Vector.mag`` and ``Py5Vector.heading``.

    In many of the py5 examples, you will see ``Py5Vector`` used to describe a
    position, velocity, or acceleration. For example, if you consider a rectangle
    moving across the screen, at any given instant it has a position (a vector that
    points from the origin to its location), a velocity (the rate at which the
    object's position changes per time unit, expressed as a vector), and
    acceleration (the rate at which the object's velocity changes per time unit,
    expressed as a vector).

    The ``Py5Vector`` class works well with numpy and in most cases you will be able
    to do math operations that combine vectors and numpy arrays.

    To create a vector, you can write code like ``v = Py5Vector(1, 2, 3)``, which
    would create a 3D vector with the x, y, and z values equal to 1, 2, and 3. To
    create a vector of zeros, omit the vector values and specify the desired
    dimension with the ``dim`` parameter, such as ``v = Py5Vector(dim=4)``.

    Internally, Py5Vector stores the vector values in a numpy array. By default, the
    data type (dtype) of that numpy array is the default float size for your
    computer, which is typically a 64 bit float, or ``np.float64``. To create a
    vector with a different float size, pass your desired numpy float dtype to the
    ``dtype`` parameter, like ``v3 = py5.Py5Vector(1 / 3, 1 / 7,
    dtype=np.float16)``.

    When creating a new Py5Vector, the initial vector values need not be discrete
    values. You can provide a list of numbers, a numpy array, or another Py5Vector.
    For example, ``v4 = py5.Py5Vector([1, 2, 3])`` creates a Py5Vector from a list,
    and ``v5 = py5.Py5Vector(v4, 0)`` creates a 4D Py5Vector from a 3D Py5Vector and
    a constant value.

    When creating a new Py5Vector from a single numpy array, py5 will by default
    create its own copy of the numpy array for the Py5Vector to use. To instruct py5
    to instead use the same numpy array and share its data with provided array, set
    the ``copy`` parameter to ``False``, such as ``v6 = py5.Py5Vector(arr,
    copy=False)``.
    """

    def __new__(cls, *args, dtype: type = np.float_):
        return super().__new__(cls, *args, dim=4, dtype=dtype)

    def _get_z(self) -> float:
        """The vector's z dimension value.

        Notes
        -----

        The vector's z dimension value. This is the vector's 3rd dimension, and is only
        applicable to 3D and 4D vectors.
        """
        return self._data[2]

    def _set_z(self, val: float) -> None:
        """The vector's z dimension value.

        Notes
        -----

        The vector's z dimension value. This is the vector's 3rd dimension, and is only
        applicable to 3D and 4D vectors.
        """
        self._data[2] = val

    def _get_w(self) -> float:
        """The vector's w dimension value.

        Notes
        -----

        The vector's w dimension value. This is the vector's 4th dimension, and is only
        applicable to 4D vectors.
        """
        return self._data[3]

    def _set_w(self, val: float) -> None:
        """The vector's w dimension value.

        Notes
        -----

        The vector's w dimension value. This is the vector's 4th dimension, and is only
        applicable to 4D vectors.
        """
        self._data[3] = val

    z: float = property(_get_z, _set_z, doc="""The vector's z dimension value.

        Notes
        -----

        The vector's z dimension value. This is the vector's 3rd dimension, and is only
        applicable to 3D and 4D vectors.""")
    w: float = property(_get_w, _set_w, doc="""The vector's w dimension value.

        Notes
        -----

        The vector's w dimension value. This is the vector's 4th dimension, and is only
        applicable to 4D vectors.""")

    @classmethod
    def random(cls, dim: int = 4, *, dtype: type = np.float_) -> Py5Vector4D:
        """Create a new vector with random values.

        Parameters
        ----------

        dim: int
            dimension of the random vector to create

        dtype: type = np.float_
            dtype of the random vector to create

        Notes
        -----

        Create a new vector with random values. Use the ``dim`` parameter to specify if
        the vector should have 2, 3, or 4 dimensions.

        The new vector will have a magnitude of 1 and a heading that is uniformly
        distributed across all possible headings for a vector with the given dimension.

        When used as a ``Py5Vector`` class method, the ``dim`` parameter is required to
        specify what the new vector's dimension should be. When used as a class method
        for the ``Py5Vector2D``, ``Py5Vector3D``, or ``Py5Vector4D`` child classes, the
        ``dim`` parameter is optional and will default to the dimension implied by the
        specific class. When used as a method on a vector instance, the ``dim``
        parameter is also optional and will default to the vector instance's dimension.
        See the example code for examples of all of these use cases.
        """
        return super().random(dim, dtype=dtype)
