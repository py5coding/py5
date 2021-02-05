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
from pathlib import Path

import jpype


_options = []
_classpath = []


def is_jvm_running():
    return jpype.isJVMStarted()


def check_jvm_running():
    if jpype.isJVMStarted():
        raise RuntimeError("the jvm is already running")


def set_options(*options):
    check_jvm_running()
    global _options
    _options = list(options)


def add_options(*options):
    check_jvm_running()
    _options.extend(options)


def get_classpath():
    return jpype.getClassPath()


def add_classpath(classpath):
    check_jvm_running()
    if not isinstance(classpath, Path):
        classpath = Path(classpath)
    jpype.addClassPath(classpath.absolute())


def add_jars(path):
    check_jvm_running()
    if not isinstance(path, Path):
        path = Path(path)
    if path.exists():
        for jarfile in path.glob("**/*.[Jj][Aa][Rr]"):
            jpype.addClassPath(jarfile.absolute())


def start_jvm():
    for c in _classpath:
        print(f'adding {c}')
        jpype.addClassPath(c)
    jpype.startJVM(*_options, convertStrings=False)


__all__ = ['is_jvm_running', 'check_jvm_running',
           'set_options', 'add_options',
           'get_classpath', 'add_classpath',
           'add_jars', 'start_jvm']
