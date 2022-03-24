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
from pathlib import Path
from typing import Union
import re
import os

from . import util
from .. import reference


def translate_token(token):
    return 'py5.' + token if token in reference.PY5_DIR_STR else token


def post_translate(code):
    if not re.findall(r'^import py5' + chr(36), code, flags=re.MULTILINE):
        code = 'import py5' + (3 * os.linesep) + code
    if not re.findall(
        r'^run_sketch\([^)]*\)' +
        chr(36),
        code,
            flags=re.MULTILINE):
        code += (3 * os.linesep) + 'py5.run_sketch()' + os.linesep

    return code


def translate_code(code):
    return util.translate_code(
        translate_token,
        code,
        post_translate=post_translate)


def translate_file(src: Union[str, Path], dest: Union[str, Path]):
    util.translate_file(translate_token, src, dest,
                        post_translate=post_translate)


def translate_dir(src: Union[str, Path], dest: Union[str, Path], ext='.py'):
    util.translate_dir(translate_token, src, dest, ext,
                       post_translate=post_translate)


__ALL__ = [
    'translate_token',
    'translate_code',
    'translate_file',
    'translate_dir']


def __dir__():
    return __ALL__
