import numpy as np


class MathMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # *** BEGIN METHODS ***

    @classmethod
    def sin(cls, angle: float) -> float:
        """new template no description.

        Parameters
        ----------

        angle: float
            missing variable description

        Notes
        -----

        new template no description.
"""
        return np.sin(angle)

    @classmethod
    def cos(cls, angle: float) -> float:
        """new template no description.

        Parameters
        ----------

        angle: float
            missing variable description

        Notes
        -----

        new template no description.
"""
        return np.cos(angle)

    @classmethod
    def tan(cls, angle: float) -> float:
        """new template no description.

        Parameters
        ----------

        angle: float
            missing variable description

        Notes
        -----

        new template no description.
"""
        return np.tan(angle)

    @classmethod
    def asin(cls, value: float) -> float:
        """new template no description.

        Parameters
        ----------

        value: float
            missing variable description

        Notes
        -----

        new template no description.
"""
        return np.arcsin(value)

    @classmethod
    def acos(cls, value: float) -> float:
        """new template no description.

        Parameters
        ----------

        value: float
            missing variable description

        Notes
        -----

        new template no description.
"""
        return np.arccos(value)

    @classmethod
    def atan(cls, value: float) -> float:
        """new template no description.

        Parameters
        ----------

        value: float
            missing variable description

        Notes
        -----

        new template no description.
"""
        return np.arctan(value)

    @classmethod
    def atan2(cls, y: float, x: float) -> float:
        """new template no description.

        Parameters
        ----------

        x: float
            missing variable description

        y: float
            missing variable description

        Notes
        -----

        new template no description.
"""
        return np.arctan2(y, x)

    @classmethod
    def degrees(cls, radians: float) -> float:
        """new template no description.

        Parameters
        ----------

        radians: float
            missing variable description

        Notes
        -----

        new template no description.
"""
        return np.degrees(radians)

    @classmethod
    def radians(cls, degrees: float) -> float:
        """new template no description.

        Parameters
        ----------

        degrees: float
            missing variable description

        Notes
        -----

        new template no description.
"""
        return np.radians(degrees)

    @classmethod
    def constrain(cls, amt: float, low: float, high: float) -> float:
        """new template no description.

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

        new template no description.
"""
        return np.where(amt < low, low, np.where(amt > high, high, amt))

    @classmethod
    def dist(cls, *args) -> float:
        """new template no description.

        Parameters
        ----------

        args
            missing variable description

        Notes
        -----

        new template no description.
"""
        p1 = args[:(len(args) // 2)]
        p2 = args[(len(args) // 2):]
        assert len(p1) == len(p2)
        return sum([(a - b)**2 for a, b in zip(p1, p2)])**0.5

    @classmethod
    def lerp(cls, start: float, stop: float, amt: float) -> float:
        """new template no description.

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

        new template no description.
"""
        return amt * (stop - start) + start

    @classmethod
    def mag(cls, *args) -> float:
        """new template no description.

        Parameters
        ----------

        args
            missing variable description

        Notes
        -----

        new template no description.
"""
        return sum([x * x for x in args])**0.5

    @classmethod
    def norm(cls, value: float, start: float, stop: float) -> float:
        """new template no description.

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

        new template no description.
"""
        return (value - start) / (stop - start)

    @classmethod
    def sq(cls, n: float) -> float:
        """new template no description.

        Parameters
        ----------

        n: float
            missing variable description

        Notes
        -----

        new template no description.
"""
        return n * n
