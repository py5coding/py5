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
import os
import sys
import ast
from multiprocessing import Process
from pathlib import Path
import re
import tempfile

import stackprinter

from . import jvm
from . import parsing
from . import import_hook


_imported_mode = False
_imported_mode_locked = False


def _lock_imported_mode():
    global _imported_mode_locked
    _imported_mode_locked = True


def set_imported_mode(imported_mode: bool):
    global _imported_mode
    if _imported_mode == imported_mode:
        return
    if _imported_mode_locked:
        raise RuntimeError(
            'Attempting to set imported mode after importing py5. This would put py5 into a confused state. Throwing an exception to prevent you from having to debug that.')
    _imported_mode = imported_mode
    import_hook.activate_py5_import_hook()


def get_imported_mode() -> bool:
    return _imported_mode


_STATIC_CODE_FRAMEWORK = """
import ast as _PY5STATIC_ast

import py5_tools
py5_tools.set_imported_mode(True)
import py5_tools.parsing as _PY5STATIC_parsing
from py5 import *
_PY5_NS_ = locals().copy()


def settings():
    with open('{0}', 'r') as f:
        exec(
            compile(
                _PY5STATIC_parsing.transform_py5_code(
                    _PY5STATIC_ast.parse(f.read(), filename='{0}', mode='exec'),
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
                _PY5STATIC_parsing.transform_py5_code(
                    _PY5STATIC_ast.parse(f.read(), filename='{1}', mode='exec'),
                ),
                filename='{1}',
                mode='exec'
            ),
            _PY5_NS_
        )
"""

_CODE_FRAMEWORK = """{0}



run_sketch(block={4}, py5_options={2}, sketch_args={3})
if {1} and is_dead_from_error:
    exit_sketch()
"""


SETTINGS_REGEX = re.compile(r'^def settings[^:]*:', flags=re.MULTILINE)
SETUP_REGEX = re.compile(r'^def setup[^:]*:', flags=re.MULTILINE)
DRAW_REGEX = re.compile(r'^def draw[^:]*:', flags=re.MULTILINE)


def is_static_mode(code):
    no_settings = SETTINGS_REGEX.search(code) is None
    no_setup = SETUP_REGEX.search(code) is None
    no_draw = DRAW_REGEX.search(code) is None

    return no_settings and no_setup and no_draw


def run_code(
        sketch_path,
        *,
        classpath=None,
        new_process=False,
        exit_if_error=False,
        py5_options=None,
        sketch_args=None,
        block=True):
    sketch_path = Path(sketch_path)
    if not sketch_path.exists():
        print(f'file {sketch_path} not found')
        return

    with open(sketch_path, 'r', encoding='utf8') as f:
        code = f.read()

    if is_static_mode(code):
        _run_static_code(
            code,
            sketch_path,
            classpath,
            new_process,
            exit_if_error,
            py5_options,
            sketch_args,
            block)
    else:
        _run_code(
            sketch_path,
            classpath,
            new_process,
            exit_if_error,
            py5_options,
            sketch_args,
            sketch_path,
            block)


def _run_static_code(
        code,
        sketch_path,
        classpath,
        new_process,
        exit_if_error,
        py5_options,
        sketch_args,
        block):
    success, result = parsing.check_for_problems(code, sketch_path)
    if success:
        py5static_globals, py5static_settings, py5static_setup = result

        tempdir = Path(tempfile.TemporaryDirectory().name)
        tempdir.mkdir(parents=True, exist_ok=True)
        settings_filename = tempdir / '_PY5_STATIC_SETTINGS_CODE_.py'
        setup_filename = tempdir / '_PY5_STATIC_SETUP_CODE_.py'

        with open(settings_filename, 'w') as f:
            f.write('\n' * sum(c == '\n' for c in py5static_globals))
            f.write(py5static_settings)

        with open(setup_filename, 'w') as f:
            f.write(py5static_globals)
            f.write('\n' * sum(c == '\n' for c in py5static_settings))
            f.write(py5static_setup)

        new_sketch_path = tempdir / '_PY5_STATIC_FRAMEWORK_CODE_.py'
        new_sketch_code = _STATIC_CODE_FRAMEWORK.format(
            settings_filename.as_posix(), setup_filename.as_posix())
        with open(new_sketch_path, 'w') as f:
            f.write(new_sketch_code)

        _run_code(
            new_sketch_path,
            classpath,
            new_process,
            exit_if_error,
            py5_options,
            sketch_args,
            sketch_path,
            block)
    else:
        print(result, file=sys.stderr)


def _run_code(
        sketch_path,
        classpath,
        new_process,
        exit_if_error,
        py5_options,
        sketch_args,
        original_sketch_path,
        block):
    def _run_sketch(sketch_path, classpath, exit_if_error):
        if not jvm.is_jvm_running():
            if classpath:
                jvm.add_classpath(classpath)
            jvm.add_jars(sketch_path.parent / 'jars')

        set_imported_mode(True)
        import py5
        if (py5.is_running() if callable(py5.is_running) else py5.is_running):
            print(
                'You must exit the currently running sketch before running another sketch.',
                file=sys.stderr)
            return None

        py5_options_str = str(
            [f'--{o}' for o in py5_options]) if py5_options else 'None'
        sketch_args_str = str(sketch_args)

        with open(sketch_path, 'r', encoding='utf8') as f:
            user_code = f.read()

        # does the code parse? if not, display an error message
        try:
            # this will make sure indentation and syntax errors are correctly
            # attributed to the user's code and not the _CODE_FRAMEWORK
            # template
            ast.parse(user_code, filename=sketch_path, mode='exec')
            # now do the real parsing
            sketch_code = _CODE_FRAMEWORK.format(
                user_code, exit_if_error, py5_options_str, sketch_args_str, block)
            sketch_ast = ast.parse(
                sketch_code, filename=sketch_path, mode='exec')
        except IndentationError as e:
            msg = f'There is an indentation problem with your code on line {e.lineno}:\n'
            arrow_msg = f'--> {e.lineno}    '
            msg += f'{arrow_msg}{e.text}'
            msg += ' ' * (len(arrow_msg) + e.offset) + '^'
            print(msg, file=sys.stderr)
            return
        except Exception as e:
            msg = stackprinter.format(e)
            m = re.search(r'^SyntaxError:', msg, flags=re.MULTILINE)
            if m:
                msg = msg[m.start(0):]
            msg = 'There is a problem with your code:\n' + msg
            print(msg, file=sys.stderr)
            return

        problems = parsing.check_reserved_words(sketch_code, sketch_ast)
        if problems:
            msg = 'There ' + ('is a problem' if len(problems) ==
                              1 else f'are {len(problems)} problems') + ' with your Sketch code'
            msg += '\n' + '=' * len(msg) + '\n' + '\n'.join(problems)
            print(msg, file=sys.stderr)
            return

        sketch_compiled = compile(
            parsing.transform_py5_code(sketch_ast),
            filename=sketch_path,
            mode='exec')

        sys.path.extend([str(sketch_path.absolute().parent), os.getcwd()])
        py5_ns = dict()
        py5_ns.update(py5.__dict__)
        py5_ns['__file__'] = str(original_sketch_path)

        try:
            exec(sketch_compiled, py5_ns)
        except import_hook.Py5ImportError as e:
            print(e.msg, file=sys.stderr)

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
