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
import re
import io
from pathlib import Path
import tempfile
import textwrap

from IPython.display import display, SVG, Image
from IPython.core.magic import Magics, magics_class, cell_magic
from IPython.core.magic_arguments import parse_argstring, argument, magic_arguments, kwds

import PIL

from .util import fix_triple_quote_str, CellMagicHelpFormatter
from .. import imported


_CODE_FRAMEWORK = """
import py5

with open('{0}', 'r') as f:
    eval(compile(f.read(), '{0}', 'exec'))

py5.run_sketch(block=True, sketch_functions=dict(settings=_py5_settings, setup=_py5_setup))
if py5.is_dead_from_error:
    py5.exit_sketch()
"""


_CODE_FRAMEWORK_IMPORTED_MODE = """
with open('{0}', 'r') as f:
    eval(compile(f.read(), '{0}', 'exec'))

run_sketch(block=True, sketch_functions=dict(settings=_py5_settings, setup=_py5_setup))
if is_dead_from_error:
    exit_sketch()
"""


_STANDARD_CODE_TEMPLATE = """
def _py5_settings():
    py5.size({0}, {1}, py5.{2})


def _py5_setup():
{4}

    py5.get(0, 0, {0}, {1}).save("{3}", use_thread=False)
    py5.exit_sketch()
"""


_SAVE_OUTPUT_CODE_TEMPLATE = """
def _py5_settings():
    py5.size({0}, {1}, py5.{2}, "{3}")


def _py5_setup():
{4}

    py5.exit_sketch()
"""


_DXF_CODE_TEMPLATE = """
def _py5_settings():
    py5.size({0}, {1}, py5.P3D)


def _py5_setup():
    py5.begin_raw(py5.DXF, "{3}")

{4}

    py5.end_raw()
    py5.exit_sketch()
"""


def _run_sketch(renderer, code, width, height, user_ns, safe_exec):
    if renderer == 'SVG':
        template = _SAVE_OUTPUT_CODE_TEMPLATE
        suffix = '.svg'
        read_mode = 'r'
    elif renderer == 'PDF':
        template = _SAVE_OUTPUT_CODE_TEMPLATE
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
    is_running = py5.is_running
    if (isinstance(is_running, bool) and is_running) or (
            callable(is_running) and is_running()):
        print(
            'You must exit the currently running sketch before running another sketch.',
            file=sys.stderr)
        return None

    if imported.get_imported_mode():
        template = template.replace('py5.', '')
        code_framework = _CODE_FRAMEWORK_IMPORTED_MODE
    else:
        code_framework = _CODE_FRAMEWORK

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
                width, height, renderer, temp_out.as_posix(), prepared_code)
            f.write(code)

        exec(code_framework.format(temp_py.as_posix()), user_ns)

        if temp_out.exists():
            with open(temp_out, read_mode) as f:
                result = f.read()
        else:
            result = None

    if not safe_exec:
        del user_ns['_py5_user_ns']

    return result


@magics_class
class DrawingMagics(Magics):

    def _filename_check(self, filename):
        filename = Path(filename)
        if not filename.parent.exists():
            filename.parent.mkdir(parents=True)
        return filename

    def _variable_name_check(self, varname):
        return re.match('^[a-zA-Z_]\\w*' + chr(36), varname)

    @magic_arguments()
    @argument('width', type=int, help='width of PDF output')
    @argument('height', type=int, help='height of PDF output')
    @argument('filename', type=str, help='filename for PDF output')
    @argument('--unsafe', dest='unsafe', action='store_true',
              help='allow new variables to enter the global namespace')
    @kwds(formatter_class=CellMagicHelpFormatter)
    @cell_magic
    def py5drawpdf(self, line, cell):
        """Notes
        -----

        Create a PDF with py5.

        For users who are familiar with Processing and py5 programming, you can pretend
        the code in this cell will be executed in a Sketch with no ``draw()`` function
        and your code in the ``setup()`` function. It will use the ``PDF`` renderer.

        As this is creating a PDF, you cannot do operations on the ``pixels[]`` or
        ``np_pixels[]`` arrays. Use ``%%py5draw`` instead.

        Code used in this cell can reference functions and variables defined in other
        cells. By default, variables and functions created in this cell will be local to
        only this cell because to do otherwise would be unsafe. If you understand the
        risks, you can use the ``global`` keyword to add a single function or variable
        to the notebook namespace or the ``--unsafe`` argument to add everything to the
        notebook namespace. Either option may be very useful to you, but be aware that
        using py5 objects in a different notebook cell or reusing them in another Sketch
        can result in nasty errors and bizzare consequences."""
        args = parse_argstring(self.py5drawpdf, line)

        pdf = _run_sketch('PDF', cell, args.width, args.height,
                          self.shell.user_ns, not args.unsafe)
        if pdf:
            filename = self._filename_check(args.filename)
            with open(filename, 'wb') as f:
                f.write(pdf)
            print(f'PDF written to {filename}')

    @magic_arguments()
    @argument('width', type=int, help='width of DXF output')
    @argument('height', type=int, help='height of DXF output')
    @argument('filename', type=str, help='filename for DXF output')
    @argument('--unsafe', dest='unsafe', action='store_true',
              help='allow new variables to enter the global namespace')
    @kwds(formatter_class=CellMagicHelpFormatter)
    @cell_magic
    def py5drawdxf(self, line, cell):
        """Notes
        -----

        Create a DXF file with py5.

        For users who are familiar with Processing and py5 programming, you can pretend
        the code in this cell will be executed in a Sketch with no ``draw()`` function
        and your code in the ``setup()`` function. It will use the ``DXF`` renderer.

        As this is creating a DXF file, your code will be limited to the capabilities of
        that renderer.

        Code used in this cell can reference functions and variables defined in other
        cells. By default, variables and functions created in this cell will be local to
        only this cell because to do otherwise would be unsafe. If you understand the
        risks, you can use the ``global`` keyword to add a single function or variable
        to the notebook namespace or the ``--unsafe`` argument to add everything to the
        notebook namespace. Either option may be very useful to you, but be aware that
        using py5 objects in a different notebook cell or reusing them in another Sketch
        can result in nasty errors and bizzare consequences."""
        args = parse_argstring(self.py5drawdxf, line)

        dxf = _run_sketch('DXF', cell, args.width, args.height,
                          self.shell.user_ns, not args.unsafe)
        if dxf:
            filename = self._filename_check(args.filename)
            with open(filename, 'w') as f:
                f.write(dxf)
            print(f'DXF written to {filename}')

    @magic_arguments()
    @argument('width', type=int, help='width of SVG drawing')
    @argument('height', type=int, help='height of SVG drawing')
    @argument('-f', '--filename', type=str, dest='filename',
              help='save SVG drawing to file')
    @argument('--unsafe', dest='unsafe', action='store_true',
              help='allow new variables to enter the global namespace')
    @kwds(formatter_class=CellMagicHelpFormatter)
    @cell_magic
    def py5drawsvg(self, line, cell):
        """Notes
        -----

        Create a SVG drawing with py5 and embed result in the notebook.

        For users who are familiar with Processing and py5 programming, you can pretend
        the code in this cell will be executed in a Sketch with no ``draw()`` function
        and your code in the ``setup()`` function. It will use the ``SVG`` renderer.

        As this is creating a SVG drawing, you cannot do operations on the ``pixels[]``
        or ``np_pixels[]`` arrays. Use ``%%py5draw`` instead.

        Code used in this cell can reference functions and variables defined in other
        cells. By default, variables and functions created in this cell will be local to
        only this cell because to do otherwise would be unsafe. If you understand the
        risks, you can use the ``global`` keyword to add a single function or variable
        to the notebook namespace or the ``--unsafe`` argument to add everything to the
        notebook namespace. Either option may be very useful to you, but be aware that
        using py5 objects in a different notebook cell or reusing them in another Sketch
        can result in nasty errors and bizzare consequences."""
        args = parse_argstring(self.py5drawsvg, line)

        svg = _run_sketch('SVG', cell, args.width, args.height,
                          self.shell.user_ns, not args.unsafe)
        if svg:
            if args.filename:
                filename = self._filename_check(args.filename)
                with open(filename, 'w') as f:
                    f.write(svg)
                print(f'SVG drawing written to {filename}')
            display(SVG(svg))

    @magic_arguments()
    @argument('width', type=int, help='width of PNG image')
    @argument('height', type=int, help='height of PNG image')
    @argument('-f', '--filename', dest='filename', help='save image to file')
    @argument('-v', '--var', dest='variable', help='assign image to variable')
    @argument('-r', '--renderer', type=str, dest='renderer',
              default='HIDDEN', help='processing renderer to use for Sketch')
    @argument('--unsafe', dest='unsafe', action='store_true',
              help='allow new variables to enter the global namespace')
    @kwds(formatter_class=CellMagicHelpFormatter)
    @cell_magic
    def py5draw(self, line, cell):
        """Notes
        -----

        Create a PNG image with py5 and embed result in the notebook.

        For users who are familiar with Processing and py5 programming, you can pretend
        the code in this cell will be executed in a Sketch with no ``draw()`` function
        and your code in the ``setup()`` function. By default it will use the default
        Processing renderer.

        Code used in this cell can reference functions and variables defined in other
        cells. By default, variables and functions created in this cell will be local to
        only this cell because to do otherwise would be unsafe. If you understand the
        risks, you can use the ``global`` keyword to add a single function or variable
        to the notebook namespace or the ``--unsafe`` argument to add everything to the
        notebook namespace. Either option may be very useful to you, but be aware that
        using py5 objects in a different notebook cell or reusing them in another Sketch
        can result in nasty errors and bizzare consequences."""
        args = parse_argstring(self.py5draw, line)

        if args.renderer == 'SVG':
            print('please use %%py5drawsvg for SVG drawings.', file=sys.stderr)
            return
        if args.renderer == 'PDF':
            print('please use %%py5drawpdf for PDFs.', file=sys.stderr)
            return
        if args.renderer not in ['HIDDEN', 'JAVA2D', 'P2D', 'P3D']:
            print(f'unknown renderer {args.renderer}', file=sys.stderr)
            return

        png = _run_sketch(args.renderer, cell, args.width, args.height,
                          self.shell.user_ns, not args.unsafe)
        if png:
            if args.filename or args.variable:
                pil_img = PIL.Image.open(io.BytesIO(png)).convert(mode='RGB')
                if args.filename:
                    filename = self._filename_check(args.filename)
                    pil_img.save(filename)
                    print(f'PNG file written to {filename}')
                if args.variable:
                    if self._variable_name_check(args.variable):
                        self.shell.user_ns[args.variable] = pil_img
                        print(f'PIL Image assigned to {args.variable}')
                    else:
                        print(
                            f'Invalid variable name {args.variable}',
                            file=sys.stderr)
            display(Image(png))
