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
import re
import functools

import numpy as np
from jpype.types import JString, JInt


HEX_COLOR_REGEX = re.compile(r'#[0-9A-F]{6}' + chr(36))
HEX_3DIGIT_COLOR_REGEX = re.compile(r'#[0-9A-F]{3}' + chr(36))


def _text_fix_str(f):
    @functools.wraps(f)
    def decorated(self_, *args):
        if isinstance(args[0], str):
            args = [JString(args[0]), *args[1:]]
        elif isinstance(args[0], int):
            args = [JInt(args[0]), *args[1:]]
        return f(self_, *args)

    return decorated


def _ret_str(f):
    @functools.wraps(f)
    def decorated(self_, *args):
        result = f(self_, *args)
        return str(result) if isinstance(result, JString) else result

    return decorated


def _hex_converter(arg):
    if isinstance(arg, str) and HEX_COLOR_REGEX.match(arg.upper()):
        return JInt(int("0xFF" + arg[1:], base=16))
    elif isinstance(arg, str) and HEX_3DIGIT_COLOR_REGEX.match(arg.upper()):
        return JInt(int("0xFF" + ''.join([c + c for c in arg[1:]]), base=16))
    elif isinstance(arg, (int, np.integer)) and 0x7FFFFFFF < arg <= 0xFFFFFFFF:
        return JInt(arg)
    return None


def _convert_hex_color(indices=[0]):
    def _hex_color(f):
        @functools.wraps(f)
        def decorated(self_, *args):
            args = list(args)
            for i, arg in [(i, args[i]) for i in indices if i < len(args)]:
                if (new_arg := _hex_converter(arg)) is not None:
                    args[i] = new_arg
            return f(self_, *args)
        return decorated
    return _hex_color


def _convert_hex_color2(f):
    @functools.wraps(f)
    def decorated(self_, *args):
        args = list(args)
        if len(args) == 1 and (new_arg := _hex_converter(args[0])):
            args[0] = new_arg
        elif len(args) == 2 and (new_arg := _hex_converter(args[1])):
            args[1] = new_arg
        return f(self_, *args)
    return decorated


class _Py5ContextManager:

    def __init__(self, exit_function, exit_args=()):
        self._exit_function = exit_function
        self._exit_args = exit_args

    def __enter__(self):
        pass

    def __exit__(self, *exc):
        self._exit_function(*self._exit_args)


def _context_wrapper(exit_function_name, exit_attr_args=()):
    def _decorator(f):
        @functools.wraps(f)
        def decorated(self_, *args):
            exit_args = tuple(getattr(self_, arg) for arg in exit_attr_args)
            exit_function = getattr(self_, exit_function_name)
            out = f(self_, *args)
            if out is None:
                return _Py5ContextManager(exit_function, exit_args=exit_args)
            elif hasattr(out, '_activate_context_manager'):
                out._activate_context_manager(exit_function, exit_args)
            return out
        return decorated
    return _decorator
