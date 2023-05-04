# *****************************************************************************
#
#   Part of the py5 library
#   Copyright (C) 2020-2023 Jim Schmitz
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
import jpype

from . import spelling


class Py5Utilities:
    """Py5Utilities enables hybrid programming, enabling you to augment your py5 Sketch
    code with Java.

    Notes
    -----

    Py5Utilities enables hybrid programming, enabling you to augment your py5 Sketch
    code with Java. This is very much like creating custom Processing extensions to
    enhance py5. Read the online documentation to learn more about how to use this
    feature.
    """

    def __init__(self, sketch):
        self._sketch = sketch
        try:
            self._instance = jpype.JClass(
                'py5utils.Py5Utilities')(sketch._instance)
            self._dir = list(set(dir(self._instance)) -
                             set('equals getClass hashCode notify notifyAll wait toString'.split()))
        except BaseException:
            self._instance = None
            self._dir = []

        from .object_conversion import convert_to_python_type
        self._convert_to_python_type = convert_to_python_type

    def __str__(self) -> str:
        if self._instance is None:
            return "Py5Utilities(<this feature is not available for this Sketch>)"
        else:
            return "Py5Utilities(sketch=" + self._sketch.__str__() + ")"

    def __repr__(self) -> str:
        return self.__str__()

    def __dir__(self):
        return self._dir

    def __getattr__(self, name):
        if self._instance is None:
            raise AttributeError(
                "Py5Utilities class was not instantiated for this Sketch. Check your classpath if you believe this to be an error.")
        elif hasattr(self._instance, name):
            attr = getattr(self._instance, name)
            if callable(attr):
                return lambda *args: self._convert_to_python_type(attr(*args))
            else:
                return self._convert_to_python_type(attr)
        else:
            raise AttributeError(
                spelling.error_msg(
                    'Py5Utilities',
                    name,
                    self._instance))
