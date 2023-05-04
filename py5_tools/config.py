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
from typing import Union, Callable
from types import ModuleType


_PY5_PROCESSING_MODE_KEYS = {}
_PY5_PROCESSING_MODE_CALLBACK_ONCE = set()


def register_processing_mode_key(
        key: str, value: Union[Callable, ModuleType], *, callback_once: bool = False):
    """Register a callable or module when programming in py5's Processing Mode.

    Parameters
    ----------

    callback_once: bool = False
        deregister key after single use

    key: str
        key used from Processing Mode callPython() method

    value: Union[Callable, ModuleType]
        callable or module to link to key

    Notes
    -----

    Register a callable or module when programming in py5's Processing Mode. This
    will make Python code available to Processing Mode py5 users to call in Java
    with the `callPython()` method. Please read py5's online documentation to learn
    more about Processing Mode.

    The `value` parameter can be a callable, a module or an object. If `value` is a
    module or an object, the `key` parameter in the Java `callPython()` call should
    use dots ("`.`") to access the module's or object's callables."""
    _PY5_PROCESSING_MODE_KEYS[key] = value
    if callback_once:
        _PY5_PROCESSING_MODE_CALLBACK_ONCE.add(key)


__all__ = ['register_processing_mode_key']
