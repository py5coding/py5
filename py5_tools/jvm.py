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
from __future__ import annotations

import os
import sys
import platform
import subprocess
from pathlib import Path

from typing import Any, Union  # noqa


import jpype


_PY5_REQUIRED_JAVA_VERSION = 17

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


def add_options(*options: list[str]) -> None:
    """Provide JVM options to use when the JVM starts.

    Parameters
    ----------

    options: list[str]
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


def get_jvm_debug_info() -> dict[str, Any]:
    """Get Java Virtual Machine debug information.

    Notes
    -----

    Get Java Virtual Machine debug information. The py5 library requires Java 17 or
    greater to be installed and the ``$JAVA_HOME`` environment variable to be
    properly set. If one or both of these conditions are not true, py5 will not
    work.

    If the Java Virtual Machine cannot start, py5 will include this debug
    information in the error message. If that doesn't help the user figure out the
    problem, it will help whomever they go to asking for help."""
    out = dict()
    out['JAVA_HOME environment variable'] = os.environ.get(
        'JAVA_HOME', '<not set>')
    out['jvm version'] = jpype.getJVMVersion()
    out['default jvm path'] = jpype.getDefaultJVMPath()
    return out


def _evaluate_java_version(path, n=1):
    path = Path(path)
    for _ in range(n):
        try:
            if (java_path := path / 'bin' / ('java.exe' if platform.system()
                                             == 'Windows' else 'java')).exists():
                stderr = subprocess.run(
                    [str(java_path), "-XshowSettings:properties"], stderr=subprocess.PIPE
                ).stderr.decode("utf-8").splitlines()
                for l in stderr:
                    if l.find('java.version =') >= 0:
                        return int(l.split('=')[1].split('.', maxsplit=1)[0])
            path = path.parent
        except Exception:
            break

    return 0


def _start_jvm() -> None:
    jpype_exception = None
    default_jvm_path = None

    if hasattr(sys, '_MEIPASS'):
        if (pyinstaller_java_home := Path(
                getattr(sys, '_MEIPASS')) / 'JAVA_HOME').exists():
            os.environ['JAVA_HOME'] = str(pyinstaller_java_home)

    try:
        default_jvm_path = jpype.getDefaultJVMPath()
    except Exception as e:
        jpype_exception = e

    if 'JAVA_HOME' not in os.environ and (
        default_jvm_path is None or _evaluate_java_version(
            default_jvm_path,
            n=4) < _PY5_REQUIRED_JAVA_VERSION):
        possible_jdks = []
        if (dot_jdk := Path(Path.home(), '.jdk')).exists():
            possible_jdks.extend(
                dot_jdk.glob(
                    '*/Contents/Home/' if platform.system() == 'Darwin' else '*'))
        if (dot_jre := Path(Path.home(), '.jre')).exists():
            possible_jdks.extend(
                dot_jre.glob(
                    '*/Contents/Home/' if platform.system() == 'Darwin' else '*'))

        for d in possible_jdks:
            if _evaluate_java_version(d) >= _PY5_REQUIRED_JAVA_VERSION:
                os.environ['JAVA_HOME'] = str(d)
                try:
                    default_jvm_path = jpype.getDefaultJVMPath()
                    jpype_exception = None
                except Exception as e:
                    jpype_exception = e
                break

    for c in _classpath:
        jpype.addClassPath(c)

    if jpype_exception is not None:
        raise jpype_exception

    jpype.startJVM(default_jvm_path, *_options, convertStrings=False)


__all__ = ['is_jvm_running', 'add_options', 'get_classpath',
           'add_classpath', 'add_jars', 'get_jvm_debug_info']
