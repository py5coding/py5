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

from jpype.types import JString


def _text_fix_str(f):
    @functools.wraps(f)
    def decorated(self_, *args):
        if isinstance(args[0], str):
            args = [JString(args[0]), *args[1:]]
        return f(self_, *args)

    return decorated


def _ret_str(f):
    @functools.wraps(f)
    def decorated(self_, *args):
        result = f(self_, *args)
        return str(result) if isinstance(result, JString) else result

    return decorated
