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
import os
import sys
import ast
from multiprocessing import Process
from pathlib import Path
import re

import jpype
if sys.platform == 'darwin':
    from PyObjCTools import AppHelper
else:
    AppHelper = None

import stackprinter

from . import jvm
from .py5bot import py5bot
from . import parsing


_imported_mode = False


def set_imported_mode(imported_mode: bool):
    global _imported_mode
    _imported_mode = imported_mode


def get_imported_mode() -> bool:
    return _imported_mode


_STATIC_CODE_FRAMEWORK = """
import ast as _PY5BOT_ast

import py5_tools
py5_tools.set_imported_mode(True)
import py5_tools.parsing as _PY5BOT_parsing
from py5 import *
_PY5_NS_ = locals().copy()


def settings():
    with open('{0}', 'r') as f:
        exec(
            compile(
                _PY5BOT_parsing.transform_py5_code(
                    _PY5BOT_ast.parse(f.read(), filename='{0}', mode='exec'),
                ),
                filename='{0}',
                mode='exec'
            ),
            _PY5_NS_
        )


def setup():
    with open('{1}', 'r') as f:
        exec(
            compile(
                _PY5BOT_parsing.transform_py5_code(
                    _PY5BOT_ast.parse(f.read(), filename='{1}', mode='exec'),
                ),
                filename='{1}',
                mode='exec'
            ),
            _PY5_NS_
        )
"""

_STATIC_CODE_FRAMEWORK_OSX_EXTRA = """
def draw():
    pass
"""

_CODE_FRAMEWORK = """
{0}

run_sketch(block=True, py5_options={2}, sketch_args={3})
if {1} and is_dead_from_error:
    exit_sketch()
"""


SETTINGS_REGEX = re.compile(r'^def settings\(\):', flags=re.MULTILINE)
SETUP_REGEX = re.compile(r'^def setup\(\):', flags=re.MULTILINE)
DRAW_REGEX = re.compile(r'^def draw\(\):', flags=re.MULTILINE)


def is_static_mode(code):
    no_settings = SETTINGS_REGEX.search(code) is None
    no_setup = SETUP_REGEX.search(code) is None
    no_draw = DRAW_REGEX.search(code) is None

    return no_settings and no_setup and no_draw


def run_code(
        sketch_path,
        classpath=None,
        new_process=False,
        exit_if_error=False,
        py5_options=None,
        sketch_args=None):
    sketch_path = Path(sketch_path)
    if not sketch_path.exists():
        print(f'file {sketch_path} not found')
        return

    with open(sketch_path, 'r') as f:
        code = f.read()

    if is_static_mode(code):
        _run_static_code(
            code,
            sketch_path,
            classpath,
            new_process,
            exit_if_error,
            py5_options,
            sketch_args)
    else:
        _run_code(
            sketch_path,
            classpath,
            new_process,
            exit_if_error,
            py5_options,
            sketch_args)


def _run_static_code(
        code,
        sketch_path,
        classpath,
        new_process,
        exit_if_error,
        py5_options,
        sketch_args):
    py5bot_mgr = py5bot.Py5BotManager()
    success, result = py5bot.check_for_problems(code, sketch_path)
    if success:
        py5bot_globals, py5bot_settings, py5bot_setup = result
        py5bot_mgr.write_code(py5bot_globals, py5bot_settings, py5bot_setup)
        new_sketch_path = py5bot_mgr.tempdir / '_PY5_STATIC_FRAMEWORK_CODE_.py'
        new_sketch_code = _STATIC_CODE_FRAMEWORK.format(
            py5bot_mgr.settings_filename.as_posix(),
            py5bot_mgr.setup_filename.as_posix())
        if sys.platform == 'darwin':
            new_sketch_code += _STATIC_CODE_FRAMEWORK_OSX_EXTRA
        with open(new_sketch_path, 'w') as f:
            f.write(new_sketch_code)
        _run_code(
            new_sketch_path,
            classpath,
            new_process,
            exit_if_error,
            py5_options,
            sketch_args)
    else:
        print(result, file=sys.stderr)


def _run_code(
        sketch_path,
        classpath,
        new_process,
        exit_if_error,
        py5_options,
        sketch_args):
    def _run_sketch(sketch_path, classpath, exit_if_error):
        if not jvm.is_jvm_running():
            if classpath:
                jvm.add_classpath(classpath)
            jvm.add_jars(sketch_path.parent / 'jars')

        set_imported_mode(True)
        import py5
        if (py5.is_running() if callable(py5.is_running) else py5.is_running):
            print(
                'You must exit the currently running sketch before running another sketch.')
            return None

        py5_options_str = str(
            [f'--{o}' for o in py5_options]) if py5_options else 'None'
        sketch_args_str = str(sketch_args)

        with open(sketch_path, 'r') as f:
            sketch_code = _CODE_FRAMEWORK.format(
                f.read(), exit_if_error, py5_options_str, sketch_args_str)

        # does the code parse? if not, display an error message
        try:
            sketch_ast = ast.parse(
                sketch_code, filename=sketch_path, mode='exec')
        except IndentationError as e:
            msg = f'There is an indentation problem with your code on line {e.lineno}:\n'
            arrow_msg = f'--> {e.lineno}    '
            msg += f'{arrow_msg}{e.text}'
            msg += ' ' * (len(arrow_msg) + e.offset) + '^'
            print(msg)
            return
        except Exception as e:
            msg = stackprinter.format(e)
            m = re.search(r'^SyntaxError:', msg, flags=re.MULTILINE)
            if m:
                msg = msg[m.start(0):]
            msg = 'There is a problem with your code:\n' + msg
            print(msg)
            return

        problems = parsing.check_reserved_words(sketch_code, sketch_ast)
        if problems:
            msg = 'There ' + ('is a problem' if len(problems) ==
                              1 else f'are {len(problems)} problems') + ' with your Sketch code'
            msg += '\n' + '=' * len(msg) + '\n' + '\n'.join(problems)
            print(msg)
            return

        sketch_compiled = compile(
            parsing.transform_py5_code(sketch_ast),
            filename=sketch_path,
            mode='exec')

        sys.path.extend([str(sketch_path.absolute().parent), os.getcwd()])
        py5_ns = dict()
        py5_ns.update(py5.__dict__)

        def exec_compiled_code():
            exec(sketch_compiled, py5_ns)

        if sys.platform == 'darwin':
            def launch_exec_compiled_code():
                exec_compiled_code()
                AppHelper.stopEventLoop()

            proxy = jpype.JProxy(
                'java.lang.Runnable', {
                    'run': launch_exec_compiled_code})
            run_sketch_thread = jpype.JClass('java.lang.Thread')(proxy)
            run_sketch_thread.start()
            AppHelper.runConsoleEventLoop()
        else:
            exec_compiled_code()

    if new_process:
        p = Process(
            target=_run_sketch,
            args=(
                sketch_path,
                classpath,
                exit_if_error))
        p.start()
        return p
    else:
        _run_sketch(sketch_path, classpath, exit_if_error)
