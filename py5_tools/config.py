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
from typing import Union
from types import ModuleType


_PY5_PROCESSING_MODE_KEYS = {}
_PY5_PROCESSING_MODE_CALLBACK_ONCE = set()


def register_processing_mode_key(
        key: str, value: Union[callable, ModuleType], *, callback_once: bool = False):
    _PY5_PROCESSING_MODE_KEYS[key] = value
    if callback_once:
        _PY5_PROCESSING_MODE_CALLBACK_ONCE.add(key)


__all__ = ['register_processing_mode_key']
