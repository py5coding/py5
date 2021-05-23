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
from typing import overload, Union, Any, List

import numpy as np

import noise


class MathMixin:

    SIMPLEX_NOISE = 1  # CODEBUILDER INCLUDE
    PERLIN_NOISE = 2  # CODEBUILDER INCLUDE

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._NOISE_MODE = self.SIMPLEX_NOISE
        self._NOISE_SEED = np.random.randint(1024)
        self._NOISE_OCTAVES = 4
        self._NOISE_PERSISTENCE = 0.5
        self._NOISE_LACUNARITY = 2.0
        self._rng = np.random.default_rng()

    # *** BEGIN METHODS ***

    @classmethod
    def sin(cls, angle: float) -> float:
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

        This function makes a call to the numpy ``sin()`` function."""
        return np.sin(angle)

    @classmethod
    def cos(cls, angle: float) -> float:
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

        This function makes a call to the numpy ``cos()`` function."""
        return np.cos(angle)

    @classmethod
    def tan(cls, angle: float) -> float:
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

        This function makes a call to the numpy ``tan()`` function."""
        return np.tan(angle)

    @classmethod
    def asin(cls, value: float) -> float:
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

        This function makes a call to the numpy ``asin()`` function."""
        return np.arcsin(value)

    @classmethod
    def acos(cls, value: float) -> float:
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

        This function makes a call to the numpy ``acos()`` function."""
        return np.arccos(value)

    @classmethod
    def atan(cls, value: float) -> float:
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

        This function makes a call to the numpy ``atan()`` function."""
        return np.arctan(value)

    @classmethod
    def atan2(cls, y: float, x: float) -> float:
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

        This function makes a call to the numpy ``atan2()`` function."""
        return np.arctan2(y, x)

    @classmethod
    def degrees(cls, radians: float) -> float:
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

        This function makes a call to the numpy ``degrees()`` function."""
        return np.degrees(radians)

    @classmethod
    def radians(cls, degrees: float) -> float:
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

        This function makes a call to the numpy ``radians()`` function."""
        return np.radians(degrees)

    @classmethod
    def constrain(cls, amt: float, low: float, high: float) -> float:
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

        Constrains a value to not exceed a maximum and minimum value."""
        return np.where(amt < low, low, np.where(amt > high, high, amt))

    @classmethod
    def remap(
            cls,
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
        because of a name conflict with a builtin Python function."""
        return start2 + (stop2 - start2) * \
            ((value - start1) / (stop1 - start1))

    @overload
    def dist(cls, x1: float, y1: float, x2: float, y2: float) -> float:
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

        Calculates the distance between two points."""
        pass

    @overload
    def dist(
            cls,
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

        Calculates the distance between two points."""
        pass

    @classmethod
    def dist(cls, *args: float) -> float:
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

        Calculates the distance between two points."""
        if len(args) % 2 == 1:
            raise RuntimeError(
                f'Cannot apply dist function to arguments {args}')
        return sum([(a - b)**2 for a,
                    b in zip(args[:(len(args) // 2)],
                             args[(len(args) // 2):])])**0.5

    @classmethod
    def lerp(cls, start: float, stop: float, amt: float) -> float:
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
        and for drawing dotted lines."""
        return amt * (stop - start) + start

    @overload
    def mag(cls, a: float, b: float) -> float:
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
        a shortcut for writing ``dist(0, 0, x, y)``."""
        pass

    @overload
    def mag(cls, a: float, b: float, c: float) -> float:
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
        a shortcut for writing ``dist(0, 0, x, y)``."""
        pass

    @classmethod
    def mag(cls, *args: float) -> float:
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
        a shortcut for writing ``dist(0, 0, x, y)``."""
        return sum([x * x for x in args])**0.5

    @classmethod
    def norm(cls, value: float, start: float, stop: float) -> float:
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
        what you want, try pairing this function with ``constrain()``."""
        return (value - start) / (stop - start)

    @classmethod
    def sq(cls, value: float) -> float:
        """Squares a number (multiplies a number by itself).

        Parameters
        ----------

        value: float
            number to square

        Notes
        -----

        Squares a number (multiplies a number by itself). The result is always a
        positive number, as multiplying two negative numbers always yields a positive
        result. For example, ``-1 * -1 = 1``."""
        return value * value

    @classmethod
    def sqrt(cls, value: float) -> Union[float, complex]:
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
        example to learn how to do both of these things."""
        return value**0.5

    @classmethod
    def floor(cls, value: float) -> int:
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

        This function makes a call to the numpy ``floor()`` function."""
        return int(np.floor(value))

    @classmethod
    def ceil(cls, value: float) -> int:
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

        This function makes a call to the numpy ``ceil()`` function."""
        return int(np.ceil(value))

    @classmethod
    def exp(cls, value: float) -> float:
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

        This function makes a call to the numpy ``exp()`` function."""
        return np.exp(value)

    @classmethod
    def log(cls, value: float) -> float:
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
        the returned result will be numpy's Not-a-Number value, ``np.nan``."""
        return np.log(value)

    def random_seed(self, seed: int) -> None:
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
        numbers each time the software is run."""
        self._rng = np.random.default_rng(seed)

    @overload
    def random(self) -> float:
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

        This function makes calls to numpy to generate the random values."""
        pass

    @overload
    def random(self, high: float) -> float:
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

        This function makes calls to numpy to generate the random values."""
        pass

    @overload
    def random(self, low: float, high: float) -> float:
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

        This function makes calls to numpy to generate the random values."""
        pass

    def random(self, *args: float) -> float:
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

        This function makes calls to numpy to generate the random values."""
        if len(args) == 0:
            return self._rng.uniform()
        elif len(args) == 1:
            high = args[0]
            if isinstance(high, (int, float)):
                return self._rng.uniform(0, high)
        elif len(args) == 2:
            low, high = args
            if isinstance(
                    low, (int, float)) and isinstance(
                    high, (int, float)):
                return self._rng.uniform(low, high)

        types = ','.join([type(a).__name__ for a in args])
        raise TypeError(
            f'No matching overloads found for Sketch.random({types})')

    @overload
    def random_int(self) -> int:
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

        This function makes calls to numpy to generate the random integers."""
        pass

    @overload
    def random_int(self, high: int) -> int:
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

        This function makes calls to numpy to generate the random integers."""
        pass

    @overload
    def random_int(self, low: int, high: int) -> int:
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

        This function makes calls to numpy to generate the random integers."""
        pass

    def random_int(self, *args: int) -> int:
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

        This function makes calls to numpy to generate the random integers."""
        if len(args) == 0:
            return self._rng.integers(0, 1, endpoint=True)
        elif len(args) == 1:
            high = args[0]
            if isinstance(high, int):
                return self._rng.integers(0, high, endpoint=True)
        elif len(args) == 2:
            low, high = args
            if isinstance(low, int) and isinstance(high, int):
                return self._rng.integers(low, high, endpoint=True)

        types = ','.join([type(a).__name__ for a in args])
        raise TypeError(
            f'No matching overloads found for Sketch.random_int({types})')

    def random_choice(self, objects: List[Any]) -> Any:
        """Select a random item from a list.

        Parameters
        ----------

        objects: List[Any]
            list of objects to choose from

        Notes
        -----

        Select a random item from a list. The list items can be of any type. This
        function's randomness can be influenced by ``random_seed()``.

        This function makes calls to numpy to select the random items."""
        return self._rng.choice(objects)

    @overload
    def random_gaussian(self) -> float:
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

        This function makes calls to numpy to generate the random values."""
        pass

    @overload
    def random_gaussian(self, loc: float) -> float:
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

        This function makes calls to numpy to generate the random values."""
        pass

    @overload
    def random_gaussian(self, loc: float, scale: float) -> float:
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

        This function makes calls to numpy to generate the random values."""
        pass

    def random_gaussian(self, *args: float) -> float:
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

        This function makes calls to numpy to generate the random values."""
        if len(args) == 0:
            return self._rng.normal()
        elif len(args) == 1:
            loc = args[0]
            if isinstance(loc, int):
                return self._rng.normal(loc)
        elif len(args) == 2:
            loc, scale = args
            if isinstance(
                    loc, (int, float)) and isinstance(
                    scale, (int, float)):
                return self._rng.normal(loc, scale)

        types = ','.join([type(a).__name__ for a in args])
        raise TypeError(
            f'No matching overloads found for Sketch.random_gaussian({types})')

    @overload
    def noise(self, x: float, **kwargs) -> float:
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
        automatically vectorize the operations and use broadcasting when needed."""
        pass

    @overload
    def noise(self, x: float, y: float, **kwargs) -> float:
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
        automatically vectorize the operations and use broadcasting when needed."""
        pass

    @overload
    def noise(self, x: float, y: float, z: float, **kwargs) -> float:
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
        automatically vectorize the operations and use broadcasting when needed."""
        pass

    @overload
    def noise(self, x: float, y: float, z: float, w: float, **kwargs) -> float:
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
        automatically vectorize the operations and use broadcasting when needed."""
        pass

    def noise(self, *args, **kwargs) -> float:
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
        automatically vectorize the operations and use broadcasting when needed."""
        len_args = len(args)
        noise_args = {
            'octaves': self._NOISE_OCTAVES,
            'persistence': self._NOISE_PERSISTENCE,
            'lacunarity': self._NOISE_LACUNARITY,
            'base': self._NOISE_SEED,
            # this will override other parameters if specified by the user
            **kwargs
        }
        noisef = lambda *x, **_: x[0]
        if self._NOISE_MODE == self.PERLIN_NOISE:
            if len_args not in [1, 2, 3]:
                raise RuntimeError(
                    'Sorry, Perlin noise can only be generated in 1, 2, or 3 dimensions.')
            noisef = {
                1: noise.pnoise1,
                2: noise.pnoise2,
                3: noise.pnoise3}[len_args]
        elif self._NOISE_MODE == self.SIMPLEX_NOISE:
            if len_args not in [1, 2, 3, 4]:
                raise RuntimeError(
                    'Sorry, Simplex noise can only be generated in 1, 2, 3, or 4 dimensions.')
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

    def noise_mode(self, mode: int) -> None:
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
        more advanced features, import that library directly."""
        if mode in [self.PERLIN_NOISE, self.SIMPLEX_NOISE]:
            self._NOISE_MODE = mode

    def noise_detail(self, octaves: float = None, persistence: float = None,
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
        more advanced features, import that library directly."""
        if octaves:
            self._NOISE_OCTAVES = octaves
        if persistence:
            self._NOISE_PERSISTENCE = persistence
        if lacunarity:
            self._NOISE_LACUNARITY = lacunarity

    def noise_seed(self, seed: int) -> None:
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
        more advanced features, import that library directly."""
        # NOTE: perlin noise requires integer seeds
        self._NOISE_SEED = seed
