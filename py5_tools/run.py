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
import sys
import os
from multiprocessing import Process
from pathlib import Path
import re
import tempfile
import textwrap

from . import jvm
from . import reference as ref


_CODE_FRAMEWORK_EXTRAS = """
def _py5_init_dynamic_variables(sketch):
    sketch.load_pixels()
    sketch.load_np_pixels()
{0}

def _py5_update_dynamic_variables(sketch):
{0}

py5._py5sketch._add_pre_hook('setup', '_py5_init_dynamic_variables', _py5_init_dynamic_variables)
py5._py5sketch._add_pre_hook('draw', '_py5_update_dynamic_variables', _py5_update_dynamic_variables)
"""


_CODE_FRAMEWORK = """
import py5

{2}

with open('{0}', 'r') as f:
    eval(compile(f.read(), '{0}', 'exec'))

py5.run_sketch(block=True)
if {1} and py5.is_dead_from_error:
    py5.exit_sketch()
"""


_STANDARD_CODE_TEMPLATE = """
import py5

def settings():
    py5.size({0}, {1}, py5.{2})


def setup():
{4}

    py5.save_frame("{3}", use_thread=False)
    py5.exit_sketch()
"""


_ALT_CODE_TEMPLATE = """
import py5

def settings():
    py5.size({0}, {1}, py5.{2}, "{3}")


def setup():
{4}

    py5.exit_sketch()
"""


_DXF_CODE_TEMPLATE = """
import py5

def settings():
    py5.size({0}, {1}, py5.P3D)


def setup():
    py5.begin_raw(py5.DXF, "{3}")

{4}

    py5.end_raw()
    py5.exit_sketch()
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


def fix_triple_quote_str(code):
    for m in re.finditer(r'\"\"\"[^\"]*\"\"\"', code):
        code = code.replace(
            m.group(), m.group().replace('\n    ', '\n'))
    return code


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
        remaining_code = fix_triple_quote_str(remaining_code)
    else:
        # remaining code has been modified with key lines moved from setup to
        # settings
        remaining_code = code

    return True, f'{settings.strip()}\n\n{remaining_code.strip()}\n'


def run_sketch(
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

        import py5
        if not py5.get_current_sketch().is_ready:
            py5.reset_py5()
        sys.path.extend([str(sketch_path.absolute().parent), os.getcwd()])
        py5_ns = dict()
        py5_ns.update(py5.__dict__)
        update_dynamic_variables_code = '\n'.join(
            f'    global {v}\n    {v} = sketch.{v}' for v in ref.UPDATE_DYNAMIC_VARIABLES)
        exec(
            _CODE_FRAMEWORK.format(
                sketch_path,
                exit_if_error,
                _CODE_FRAMEWORK_EXTRAS.format(update_dynamic_variables_code)),
            py5_ns)

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


def run_single_frame_sketch(renderer, code, width, height, user_ns, safe_exec):
    if renderer == 'SVG':
        template = _ALT_CODE_TEMPLATE
        suffix = '.svg'
        read_mode = 'r'
    elif renderer == 'PDF':
        template = _ALT_CODE_TEMPLATE
        suffix = '.pdf'
        read_mode = 'rb'
    elif renderer == 'DXF':
        template = _DXF_CODE_TEMPLATE
        suffix = '.dxf'
        read_mode = 'r'
    else:
        template = _STANDARD_CODE_TEMPLATE
        suffix = '.png'
        read_mode = 'rb'

    import py5
    if not py5.get_current_sketch().is_ready:
        py5.reset_py5()

    if safe_exec:
        prepared_code = textwrap.indent(code, '    ')
        prepared_code = fix_triple_quote_str(prepared_code)
    else:
        user_ns['_py5_user_ns'] = user_ns
        code = code.replace('"""', r'\"\"\"')
        prepared_code = f'    exec("""{code}""", _py5_user_ns)'

    with tempfile.TemporaryDirectory() as tempdir:
        temp_py = Path(tempdir) / 'py5_code.py'
        temp_out = Path(tempdir) / ('output' + suffix)

        with open(temp_py, 'w') as f:
            code = template.format(
                width,
                height,
                renderer,
                temp_out.as_posix(),
                prepared_code)
            f.write(code)

        exec(_CODE_FRAMEWORK.format(temp_py.as_posix(), True, ''), user_ns)

        if temp_out.exists():
            with open(temp_out, read_mode) as f:
                result = f.read()
        else:
            result = None

    py5.reset_py5()

    if not safe_exec:
        del user_ns['_py5_user_ns']

    return result


__all__ = ['run_sketch', 'run_single_frame_sketch']
