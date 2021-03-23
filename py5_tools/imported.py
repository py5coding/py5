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
import os
import sys
import ast
from multiprocessing import Process
from pathlib import Path
import re
import textwrap

from . import jvm
from .magics import util
from . import parsing


_imported_mode = False


def set_imported_mode(imported_mode: bool):
    global _imported_mode
    _imported_mode = imported_mode


def get_imported_mode() -> bool:
    return _imported_mode


_CODE_FRAMEWORK = """
{0}

run_sketch(block=True)
if {1} and is_dead_from_error:
    exit_sketch()
"""


SETTINGS_REGEX = re.compile(r'^def settings\(\):', flags=re.MULTILINE)
SETUP_REGEX = re.compile(r'^def setup\(\):', flags=re.MULTILINE)
SETUP_CODE_REGEX = re.compile(
    r'^def setup\(\):.*?(?=^\w|\Z)',
    flags=re.MULTILINE | re.DOTALL)
DRAW_REGEX = re.compile(r'^def draw\(\):', flags=re.MULTILINE)
CODE_REGEXES = {
    f: re.compile(
        r'^\s*(' + f + r'\([^\)]*\))',
        flags=re.MULTILINE) for f in [
            'size',
            'full_screen',
            'smooth',
            'no_smooth',
        'pixel_density']}


# TODO: this is ugly and should be done with ast instead
def prepare_code(code):
    "transform functionless or setttings-less py5 code into code that runs"
    if SETTINGS_REGEX.search(code):
        return False, code
    no_setup = SETUP_REGEX.search(code) is None
    no_draw = DRAW_REGEX.search(code) is None

    # get just the setup function if it is defined
    code2 = code if no_setup else SETUP_CODE_REGEX.search(code).group()
    # find the key lines in the relevant code
    matches = [m for m in [r.search(code2)
                           for r in CODE_REGEXES.values()] if m]

    # if anything was found, build the settings function
    if matches:
        lines = [(m.start(), m.group(1)) for m in matches]
        settings = 'def settings():\n'
        for start, line in sorted(lines):
            settings += f'    {line}\n'
            # replace the original line so it doesn't get called in setup
            code = code.replace(line, f'pass  # moved to settings(): {line}')
    else:
        settings = ''

    if no_setup and no_draw:
        # put all of the remaining code into a setup function
        remaining_code = 'def setup():\n' + textwrap.indent(code, prefix='    ')
        remaining_code = util.fix_triple_quote_str(remaining_code)
    else:
        # remaining code has been modified with key lines moved from setup to
        # settings
        remaining_code = code

    return True, f'{settings.strip()}\n\n{remaining_code.strip()}\n'


def run_code(
        sketch_path,
        classpath=None,
        new_process=False,
        exit_if_error=False):
    sketch_path = Path(sketch_path)
    if not sketch_path.exists():
        print(f'file {sketch_path} not found')
        return

    with open(sketch_path, 'r') as f:
        code = f.read()
    tranformed, code = prepare_code(code)
    if tranformed:
        temp_py = sketch_path.with_suffix('.tmp.py')
        with open(temp_py, 'w') as f:
            f.write(code)
        sketch_path = temp_py

    def _run_sketch(sketch_path, classpath, exit_if_error):
        if not jvm.is_jvm_running():
            if classpath:
                jvm.add_classpath(classpath)
            jvm.add_jars(sketch_path.parent / 'jars')

        set_imported_mode(True)
        import py5
        if py5.is_running():
            print(
                'You must exit the currently running sketch before running another sketch.')
            return None

        with open(sketch_path, 'r') as f:
            sketch_code = _CODE_FRAMEWORK.format(f.read(), exit_if_error)

        sketch_ast = ast.parse(sketch_code, mode='exec')
        problems = parsing.check_reserved_words(sketch_code, sketch_ast)
        if problems:
            if len(problems) == 1:
                msg = 'There is a problem with your Sketch code'
            else:
                msg = f'There are {len(problems)} problems with your Sketch code'
            print(msg)
            print('=' * len(msg))
            print('\n'.join(problems))
            return

        sketch_compiled = compile(
            parsing.transform_py5_code(sketch_ast),
            filename=sketch_path,
            mode='exec')

        sys.path.extend([str(sketch_path.absolute().parent), os.getcwd()])
        py5_ns = dict()
        py5_ns.update(py5.__dict__)
        exec(sketch_compiled, py5_ns)

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
        if tranformed:
            os.remove(temp_py)
