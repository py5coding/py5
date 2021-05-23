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
from typing import Union, List  # noqa


import jpype


_options = []
_classpath = []


def is_jvm_running() -> bool:
    """Determine if the Java Virtual Machine (JVM) is or is not running.

    Notes
    -----

    Determine if the Java Virtual Machine (JVM) is or is not running. When the py5
    library is imported it will start the JVM.  Therefore this will be ``False``
    before ``import py5`` is executed and ``True`` afterwards. It should continue to
    always be ``True`` unless somewhere there is some Java code that calls
    ``System.exit()``. Calling ``System.exit()`` is not recommended. If for some
    reason the JVM crashes (perhaps through a segmentation fault), the JVM will no
    longer be running, but that crash will most likely also terminate the Python
    interpreter."""
    return jpype.isJVMStarted()


def _check_jvm_running() -> None:
    if jpype.isJVMStarted():
        raise RuntimeError("the jvm is already running")


def add_options(*options: List[str]) -> None:
    """Provide JVM options to use when the JVM starts.

    Parameters
    ----------

    options: List[str]
        list of desired JVM options

    Notes
    -----

    Provide JVM options to use when the JVM starts. This is useful to set the JVM
    memory size, for example.

    After the JVM has started, new options cannot be added. This function will throw
    a ``RuntimeError`` if it is called after the JVM has already started. Use
    ``py5_tools.is_jvm_running()`` to first determine if the JVM is running."""
    _check_jvm_running()
    _options.extend(options)


def get_classpath() -> str:
    """Get the Java classpath.

    Notes
    -----

    Get the Java classpath. If the JVM has not yet started, this will be the
    classpath the JVM will use when it does start. It will also be possible to
    change that classpath with ``py5_tools.add_classpath()`` and
    ``py5_tools.add_jars()``. After the JVM has started, the classpath cannot be
    changed and the aformentioned functions would throw a ``RuntimeError``. Use
    ``py5_tools.is_jvm_running()`` to first determine if the JVM is running."""
    return jpype.getClassPath()


def add_classpath(classpath: Union[Path, str]) -> None:
    """Add a Java jar file to the classpath.

    Parameters
    ----------

    classpath: Union[Path, str]
        path to Java jar file

    Notes
    -----

    Add a Java jar file to the classpath. The path to the file can be absolute or
    relative.

    After the JVM has started, the classpath cannot be changed. This function will
    throw a ``RuntimeError`` if it is called after the JVM has already started. Use
    ``py5_tools.is_jvm_running()`` to first determine if the JVM is running."""
    _check_jvm_running()
    if not isinstance(classpath, Path):
        classpath = Path(classpath)
    jpype.addClassPath(classpath.absolute())


def add_jars(path: Union[Path, str]) -> None:
    """Add all of the Java jar files contained in a directory and its subdirectories to
    the classpath.

    Parameters
    ----------

    path: Union[Path, str]
        path to directory containing jar files

    Notes
    -----

    Add all of the Java jar files contained in a directory and its subdirectories to
    the classpath. The path can be absolute or relative. If the directory does does
    not exist, it will be ignored.

    When ``import py5`` is executed, ``add_jars('jars')`` is called for you to
    automatically add jar files contained in a subdirectory called jars. This is
    similar to functionality provided by the Processing IDE.

    After the JVM has started, the classpath cannot be changed. This function will
    throw a ``RuntimeError`` if it is called after the JVM has already started. Use
    ``py5_tools.is_jvm_running()`` to first determine if the JVM is running."""
    _check_jvm_running()
    if not isinstance(path, Path):
        path = Path(path)
    if path.exists():
        for jarfile in path.glob("**/*.[Jj][Aa][Rr]"):
            jpype.addClassPath(jarfile.absolute())


def _start_jvm() -> None:
    for c in _classpath:
        print(f'adding {c}')
        jpype.addClassPath(c)
    jpype.startJVM(*_options, convertStrings=False)


__all__ = [
    'is_jvm_running',
    'add_options',
    'get_classpath',
    'add_classpath',
    'add_jars']
