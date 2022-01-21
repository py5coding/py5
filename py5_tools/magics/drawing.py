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
import sys
import re
import ast
import io
from pathlib import Path
import tempfile

from IPython.display import display, SVG, Image
from IPython.core.magic import Magics, magics_class, cell_magic
from IPython.core.magic_arguments import parse_argstring, argument, magic_arguments, kwds

import stackprinter
import PIL

from .util import CellMagicHelpFormatter, filename_check, variable_name_check
from .. import imported
from .. import parsing


_CODE_FRAMEWORK_BEGIN = """
import py5
import py5_tools.parsing as _PY5BOT_parsing
import ast as _PY5BOT_ast
"""


_CODE_FRAMEWORK_IMPORTED_BEGIN = """
from py5 import *
import py5_tools.parsing as _PY5BOT_parsing
import ast as _PY5BOT_ast
"""


_CODE_TEMPLATE_END = """
py5.run_sketch(block=True, sketch_functions=dict(settings=_py5_settings, setup=_py5_setup))
if py5.is_dead_from_error:
    py5.exit_sketch()

del _PY5BOT_parsing
del _PY5BOT_ast
del _py5_settings
del _py5_setup
"""


_STANDARD_CODE_TEMPLATE = """
def _py5_settings():
    py5.size({0}, {1}, py5.{2})


def _py5_setup():
    with open('{4}', 'r') as f:
        exec(
            compile(
                _PY5BOT_parsing.transform_py5_code(  # TRANSFORM
                    _PY5BOT_ast.parse(f.read(), filename='{4}', mode='exec'),
                ),  # TRANSFORM
                filename='{4}',
                mode='exec'
            ),
            _py5_user_ns
        )

    py5.get(0, 0, {0}, {1}).save("{3}", use_thread=False)
    py5.exit_sketch()
"""


_SAVE_OUTPUT_CODE_TEMPLATE = """
def _py5_settings():
    py5.size({0}, {1}, py5.{2}, "{3}")


def _py5_setup():
    with open('{4}', 'r') as f:
        exec(
            compile(
                _PY5BOT_parsing.transform_py5_code(  # TRANSFORM
                    _PY5BOT_ast.parse(f.read(), filename='{4}', mode='exec'),
                ),  # TRANSFORM
                filename='{4}',
                mode='exec'
            ),
            _py5_user_ns
        )

    py5.exit_sketch()
"""


_DXF_CODE_TEMPLATE = """
def _py5_settings():
    py5.size({0}, {1}, py5.P3D)


def _py5_setup():
    py5.begin_raw(py5.DXF, "{3}")

    with open('{4}', 'r') as f:
        exec(
            compile(
                _PY5BOT_parsing.transform_py5_code(  # TRANSFORM
                    _PY5BOT_ast.parse(f.read(), filename='{4}', mode='exec'),
                ),  # TRANSFORM
                filename='{4}',
                mode='exec'
            ),
            _py5_user_ns
        )

    py5.end_raw()
    py5.exit_sketch()
"""


def _run_sketch(renderer, code, width, height, user_ns, safe_exec):
    if renderer == 'SVG':
        template = _SAVE_OUTPUT_CODE_TEMPLATE + _CODE_TEMPLATE_END
        suffix = '.svg'
        read_mode = 'r'
    elif renderer == 'PDF':
        template = _SAVE_OUTPUT_CODE_TEMPLATE + _CODE_TEMPLATE_END
        suffix = '.pdf'
        read_mode = 'rb'
    elif renderer == 'DXF':
        template = _DXF_CODE_TEMPLATE + _CODE_TEMPLATE_END
        suffix = '.dxf'
        read_mode = 'r'
    else:
        template = _STANDARD_CODE_TEMPLATE + _CODE_TEMPLATE_END
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

    # does the code parse? if not, display an error message
    try:
        sketch_ast = ast.parse(code, filename='<py5magic>', mode='exec')
    except IndentationError as e:
        msg = f'There is an indentation problem with your code on line {e.lineno}:\n'
        arrow_msg = f'--> {e.lineno}    '
        msg += f'{arrow_msg}{e.text}'
        msg += ' ' * (len(arrow_msg) + e.offset) + '^'
        print(msg)
        return None
    except Exception as e:
        msg = stackprinter.format(e)
        m = re.search(r'^SyntaxError:', msg, flags=re.MULTILINE)
        if m:
            msg = msg[m.start(0):]
        print('There is a problem with your code:\n' + msg, file=sys.stderr)
        return None

    if imported.get_imported_mode():
        # check for assignments to or deletions of reserved words
        problems = parsing.check_reserved_words(code, sketch_ast)
        if problems:
            msg = 'There ' + ('is a problem' if len(problems) ==
                              1 else f'are {len(problems)} problems') + ' with your code.\n'
            msg += '=' * len(msg) + '\n' + '\n'.join(problems)
            print(msg, file=sys.stderr)
            return None

        code_framework = _CODE_FRAMEWORK_IMPORTED_BEGIN + \
            template.replace('py5.', '')
    else:
        code_framework = _CODE_FRAMEWORK_BEGIN + \
            '\n'.join([l for l in template.splitlines() if l.find('# TRANSFORM') == -1])

    with tempfile.TemporaryDirectory() as tempdir:
        temp_py = Path(tempdir) / '_PY5_STATIC_SETUP_CODE_.py'
        temp_out = Path(tempdir) / ('output' + suffix)

        with open(temp_py, 'w') as f:
            f.write(code)

        py5.reset_py5()
        if imported.get_imported_mode():
            py5._prepare_dynamic_variables(user_ns, user_ns)

        user_ns['_py5_user_ns'] = user_ns.copy() if safe_exec else user_ns
        exec(
            code_framework.format(
                width,
                height,
                renderer,
                temp_out.as_posix(),
                temp_py.as_posix()),
            user_ns)

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

    @magic_arguments()
    @argument('width', type=int, help='width of PDF output')
    @argument('height', type=int, help='height of PDF output')
    @argument('filename', type=str, help='filename for PDF output')
    @argument('--unsafe', dest='unsafe', action='store_true',
              help='allow new variables to enter the user namespace')
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
        cells because a copy of the user namespace is provided during execution. By
        default, variables and functions created in this cell will be local to only this
        cell because to do otherwise would be unsafe. Mutable objects in the user
        namespace, however, can be altered and those changes will persist elsewhere in
        the notebook.

        If you understand the risks, you can use the ``--unsafe`` argument so that
        variables and functions created in this cell are stored in the user namespace
        instead of a copy, making them available in other notebook cells. This may be
        very useful to you, but be aware that using py5 objects in a different notebook
        cell or reusing them in another Sketch can result in nasty errors and bizzare
        consequences."""
        args = parse_argstring(self.py5drawpdf, line)

        pdf = _run_sketch('PDF', cell, args.width, args.height,
                          self.shell.user_ns, not args.unsafe)
        if pdf:
            filename = filename_check(args.filename)
            with open(filename, 'wb') as f:
                f.write(pdf)
            print(f'PDF written to {filename}')

    @magic_arguments()
    @argument('width', type=int, help='width of SVG drawing')
    @argument('height', type=int, help='height of SVG drawing')
    @argument('-f', '--filename', type=str, dest='filename',
              help='save SVG drawing to file')
    @argument('--unsafe', dest='unsafe', action='store_true',
              help='allow new variables to enter the user namespace')
    @kwds(formatter_class=CellMagicHelpFormatter)
    @cell_magic
    def py5drawsvg(self, line, cell):
        """Notes
        -----

        Create a SVG drawing with py5 and embed the result in the notebook.

        For users who are familiar with Processing and py5 programming, you can pretend
        the code in this cell will be executed in a Sketch with no ``draw()`` function
        and your code in the ``setup()`` function. It will use the ``SVG`` renderer.

        As this is creating a SVG drawing, you cannot do operations on the ``pixels[]``
        or ``np_pixels[]`` arrays. Use ``%%py5draw`` instead.

        Code used in this cell can reference functions and variables defined in other
        cells because a copy of the user namespace is provided during execution. By
        default, variables and functions created in this cell will be local to only this
        cell because to do otherwise would be unsafe. Mutable objects in the user
        namespace, however, can be altered and those changes will persist elsewhere in
        the notebook.

        If you understand the risks, you can use the ``--unsafe`` argument so that
        variables and functions created in this cell are stored in the user namespace
        instead of a copy, making them available in other notebook cells. This may be
        very useful to you, but be aware that using py5 objects in a different notebook
        cell or reusing them in another Sketch can result in nasty errors and bizzare
        consequences."""
        args = parse_argstring(self.py5drawsvg, line)

        svg = _run_sketch('SVG', cell, args.width, args.height,
                          self.shell.user_ns, not args.unsafe)
        if svg:
            if args.filename:
                filename = filename_check(args.filename)
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
              help='allow new variables to enter the user namespace')
    @kwds(formatter_class=CellMagicHelpFormatter)
    @cell_magic
    def py5draw(self, line, cell):
        """Notes
        -----

        Create a PNG image with py5 and embed the result in the notebook.

        For users who are familiar with Processing and py5 programming, you can pretend
        the code in this cell will be executed in a Sketch with no ``draw()`` function
        and your code in the ``setup()`` function. By default it will use the default
        Processing renderer.

        On OSX, only the default renderer is currently supported. Other platforms
        support the default renderer and the OpenGL renderers (P2D and P3D).

        Internally this magic command creates a static Sketch using the user provided
        code. The static Sketch drawing surface does not allow transparency. If you want
        to quickly create an image that has transparency, consider using ``@render()``
        or ``render_frame()`` with the ``use_py5graphics`` parameter.

        Code used in this cell can reference functions and variables defined in other
        cells because a copy of the user namespace is provided during execution. By
        default, variables and functions created in this cell will be local to only this
        cell because to do otherwise would be unsafe. Mutable objects in the user
        namespace, however, can be altered and those changes will persist elsewhere in
        the notebook.

        If you understand the risks, you can use the ``--unsafe`` argument so that
        variables and functions created in this cell are stored in the user namespace
        instead of a copy, making them available in other notebook cells. This may be
        very useful to you, but be aware that using py5 objects in a different notebook
        cell or reusing them in another Sketch can result in nasty errors and bizzare
        consequences."""
        args = parse_argstring(self.py5draw, line)

        if sys.platform == 'darwin':
            if args.renderer in ['P2D', 'P3D', 'DXF']:
                print(
                    f'Sorry, py5 magics do not support the {args.renderer} renderer on OSX.',
                    file=sys.stderr)
                return
            if args.renderer == 'JAVA2D':
                args.renderer = 'HIDDEN'
        if args.renderer == 'SVG':
            print('please use %%py5drawsvg for SVG drawings.', file=sys.stderr)
            return
        if args.renderer == 'DXF':
            print('please use %%py5drawdxf for DXF output.', file=sys.stderr)
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
                    filename = filename_check(args.filename)
                    pil_img.save(filename)
                    print(f'PNG file written to {filename}')
                if args.variable:
                    if variable_name_check(args.variable):
                        self.shell.user_ns[args.variable] = pil_img
                        print(f'PIL Image assigned to {args.variable}')
                    else:
                        print(
                            f'Invalid variable name {args.variable}',
                            file=sys.stderr)
            display(Image(png))


@magics_class
class DXFDrawingMagic(Magics):

    @magic_arguments()
    @argument('width', type=int, help='width of DXF output')
    @argument('height', type=int, help='height of DXF output')
    @argument('filename', type=str, help='filename for DXF output')
    @argument('--unsafe', dest='unsafe', action='store_true',
              help='allow new variables to enter the user namespace')
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

        This magic is not available on OSX.

        Code used in this cell can reference functions and variables defined in other
        cells because a copy of the user namespace is provided during execution. By
        default, variables and functions created in this cell will be local to only this
        cell because to do otherwise would be unsafe. Mutable objects in the user
        namespace, however, can be altered and those changes will persist elsewhere in
        the notebook.

        If you understand the risks, you can use the ``--unsafe`` argument so that
        variables and functions created in this cell are stored in the user namespace
        instead of a copy, making them available in other notebook cells. This may be
        very useful to you, but be aware that using py5 objects in a different notebook
        cell or reusing them in another Sketch can result in nasty errors and bizzare
        consequences."""
        args = parse_argstring(self.py5drawdxf, line)

        dxf = _run_sketch('DXF', cell, args.width, args.height,
                          self.shell.user_ns, not args.unsafe)
        if dxf:
            filename = filename_check(args.filename)
            with open(filename, 'w') as f:
                f.write(dxf)
            print(f'DXF written to {filename}')
