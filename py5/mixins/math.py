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
from typing import overload, Union

import numpy as np
from numpy.random import MT19937
from numpy.random import RandomState, SeedSequence

import noise


class MathMixin:

    _rs = RandomState(MT19937(SeedSequence()))

    SIMPLEX_NOISE = 1  # CODEBUILDER INCLUDE
    PERLIN_NOISE = 2  # CODEBUILDER INCLUDE
    _NOISE_MODE = SIMPLEX_NOISE
    _NOISE_SEED = 0
    _NOISE_OCTAVES = 4
    _NOISE_PERSISTENCE = 0.5
    _NOISE_LACUNARITY = 2.0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # *** BEGIN METHODS ***

    @classmethod
    def sin(cls, angle: float) -> float:
        """The documentation for this field or method has not yet been written.

        Parameters
        ----------

        angle: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/."""
        return np.sin(angle)

    @classmethod
    def cos(cls, angle: float) -> float:
        """The documentation for this field or method has not yet been written.

        Parameters
        ----------

        angle: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/."""
        return np.cos(angle)

    @classmethod
    def tan(cls, angle: float) -> float:
        """The documentation for this field or method has not yet been written.

        Parameters
        ----------

        angle: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/."""
        return np.tan(angle)

    @classmethod
    def asin(cls, value: float) -> float:
        """The documentation for this field or method has not yet been written.

        Parameters
        ----------

        value: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/."""
        return np.arcsin(value)

    @classmethod
    def acos(cls, value: float) -> float:
        """The documentation for this field or method has not yet been written.

        Parameters
        ----------

        value: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/."""
        return np.arccos(value)

    @classmethod
    def atan(cls, value: float) -> float:
        """The documentation for this field or method has not yet been written.

        Parameters
        ----------

        value: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/."""
        return np.arctan(value)

    @classmethod
    def atan2(cls, y: float, x: float) -> float:
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
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/."""
        return np.arctan2(y, x)

    @classmethod
    def degrees(cls, radians: float) -> float:
        """The documentation for this field or method has not yet been written.

        Parameters
        ----------

        radians: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/."""
        return np.degrees(radians)

    @classmethod
    def radians(cls, degrees: float) -> float:
        """The documentation for this field or method has not yet been written.

        Parameters
        ----------

        degrees: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/."""
        return np.radians(degrees)

    @classmethod
    def constrain(cls, amt: float, low: float, high: float) -> float:
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
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/."""
        return np.where(amt < low, low, np.where(amt > high, high, amt))

    @classmethod
    def remap(
            cls,
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
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/."""
        return start2 + (stop2 - start2) * \
            ((value - start1) / (stop1 - start1))

    @classmethod
    def dist(cls, *args: float) -> float:
        """The documentation for this field or method has not yet been written.

        Parameters
        ----------

        args: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/."""
        p1 = args[:(len(args) // 2)]
        p2 = args[(len(args) // 2):]
        assert len(p1) == len(p2)
        return sum([(a - b)**2 for a, b in zip(p1, p2)])**0.5

    @classmethod
    def lerp(cls, start: float, stop: float, amt: float) -> float:
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
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/."""
        return amt * (stop - start) + start

    @classmethod
    def mag(cls, *args: float) -> float:
        """The documentation for this field or method has not yet been written.

        Parameters
        ----------

        args: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/."""
        return sum([x * x for x in args])**0.5

    @classmethod
    def norm(cls, value: float, start: float, stop: float) -> float:
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
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/."""
        return (value - start) / (stop - start)

    @classmethod
    def sq(cls, value: float) -> float:
        """The documentation for this field or method has not yet been written.

        Parameters
        ----------

        value: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/."""
        return value * value

    @classmethod
    def sqrt(cls, value: float) -> Union[float, complex]:
        """The documentation for this field or method has not yet been written.

        Parameters
        ----------

        value: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/."""
        return value**0.5

    @classmethod
    def floor(cls, value: float) -> int:
        """The documentation for this field or method has not yet been written.

        Parameters
        ----------

        value: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/."""
        return int(np.floor(value))

    @classmethod
    def ceil(cls, value: float) -> int:
        """The documentation for this field or method has not yet been written.

        Parameters
        ----------

        value: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/."""
        return int(np.ceil(value))

    @classmethod
    def exp(cls, value: float) -> float:
        """The documentation for this field or method has not yet been written.

        Parameters
        ----------

        value: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/."""
        return np.exp(value)

    @classmethod
    def log(cls, value: float) -> float:
        """The documentation for this field or method has not yet been written.

        Parameters
        ----------

        value: float
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/."""
        return np.log(value)

    @overload
    def random(cls, high: float) -> float:
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
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/."""
        pass

    @overload
    def random(cls, low: float, high: float) -> float:
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
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/."""
        pass

    @classmethod
    def random_seed(cls, seed: int) -> None:
        """The documentation for this field or method has not yet been written.

        Parameters
        ----------

        seed: int
            seed value

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/."""
        cls._rs = RandomState(MT19937(SeedSequence(seed)))

    @classmethod
    def random(cls, *args: float) -> float:
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
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/."""
        if len(args) == 1:
            high = args[0]
            if isinstance(high, (int, float)):
                return high * cls._rs.rand()
        elif len(args) == 2:
            low, high = args
            if isinstance(
                    low, (int, float)) and isinstance(
                    high, (int, float)):
                return low + (high - low) * cls._rs.rand()

        types = ','.join([type(a).__name__ for a in args])
        raise TypeError(
            f'No matching overloads found for Sketch.random({types})')

    @classmethod
    def random_gaussian(cls) -> float:
        """The documentation for this field or method has not yet been written.

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/."""
        return cls._rs.randn()

    @overload
    def noise(cls, x, **kwargs) -> float:
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
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/."""
        pass

    @overload
    def noise(cls, x, y, **kwargs) -> float:
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
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/."""
        pass

    @overload
    def noise(cls, x, y, z, **kwargs) -> float:
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
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/."""
        pass

    @overload
    def noise(cls, x, y, z, w, **kwargs) -> float:
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
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/."""
        pass

    @classmethod
    def noise(cls, *args, **kwargs) -> float:
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
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/."""
        len_args = len(args)
        noise_args = {
            'octaves': cls._NOISE_OCTAVES,
            'persistence': cls._NOISE_PERSISTENCE,
            'lacunarity': cls._NOISE_LACUNARITY,
            'base': cls._NOISE_SEED,
            # this will override other parameters if specified by the user
            **kwargs
        }
        noisef = lambda *x, **_: x[0]
        if cls._NOISE_MODE == cls.PERLIN_NOISE:
            if len_args not in [1, 2, 3]:
                raise RuntimeError(
                    'Sorry, this noise function can only generate 1D, 2D, or 3D Perlin noise.')
            noisef = {
                1: noise.pnoise1,
                2: noise.pnoise2,
                3: noise.pnoise3}[len_args]
        elif cls._NOISE_MODE == cls.SIMPLEX_NOISE:
            if len_args not in [1, 2, 3, 4]:
                raise RuntimeError(
                    'Sorry, this noise function can only generate 1D, 2D, 3D, or 4D Simplex noise.')
            noisef = {
                1: noise.snoise2,
                2: noise.snoise2,
                3: noise.snoise3,
                4: noise.snoise4}[len_args]
            if len_args == 1:
                args = args[0], 0
            if len_args in [3, 4]:
                del noise_args['base']
        if any(isinstance(v, np.ndarray) for v in args):
            noisef = np.vectorize(noisef)
        return noisef(*args, **noise_args)

    @classmethod
    def noise_mode(cls, mode: int) -> None:
        """The documentation for this field or method has not yet been written.

        Parameters
        ----------

        mode: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/."""
        if mode in [cls.PERLIN_NOISE, cls.SIMPLEX_NOISE]:
            cls._NOISE_MODE = mode

    @classmethod
    def noise_detail(cls, octaves: float = None, persistence: float = None,
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
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/."""
        if octaves:
            cls._NOISE_OCTAVES = octaves
        if persistence:
            cls._NOISE_PERSISTENCE = persistence
        if lacunarity:
            cls._NOISE_LACUNARITY = lacunarity

    @classmethod
    def noise_seed(cls, seed: float) -> None:
        """The documentation for this field or method has not yet been written.

        Parameters
        ----------

        seed: float
            seed value

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/."""
        cls._NOISE_SEED = seed
