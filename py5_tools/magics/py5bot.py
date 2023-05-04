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
import sys

from IPython.display import display
from IPython.core.magic import Magics, magics_class, cell_magic
from IPython.core.magic_arguments import parse_argstring, argument, magic_arguments, kwds

from py5jupyter.kernels.py5bot.py5bot import Py5BotManager

from .. import split_setup
from ..parsing import check_for_problems

from .util import CellMagicHelpFormatter, filename_check, variable_name_check


@magics_class
class Py5BotMagics(Magics):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._py5bot_mgr = Py5BotManager()

    @magic_arguments()
    @argument('-f', '--filename', dest='filename', help='save image to file')
    @argument('-v', '--var', dest='variable', help='assign image to variable')
    @kwds(formatter_class=CellMagicHelpFormatter)
    @cell_magic
    def py5bot(self, line, cell):
        """Notes
        -----

        Create a PNG image using py5bot and embed the result in the notebook.

        This cell magic uses the same rendering mechanism as the py5bot kernel. For
        users who are familiar with Processing and py5 programming, you can pretend the
        code in this cell will be executed as a static Sketch with no `draw()` function
        and your code in the `setup()` function. The first line in the cell should be a
        call to `size()`.

        This magic is similar to `%%py5draw` in that both can be used to create a static
        Sketch. One key difference is that `%%py5bot` requires the user to begin the
        code with a call to `size()`, while `%%py5draw` calls `size()` for you based on
        the magic's arguments.

        This magic supports the default renderer and the `P2D` and `P3D` renderers. Note
        that both of the OpenGL renderers will briefly open a window on your screen.
        This magic is only available when using the py5 kernel and coding in imported
        mode. The `P2D` and `P3D` renderers are not available when the py5 kernel is
        hosted on an OSX computer.

        Code used in this cell can reference functions and variables defined in other
        cells because a copy of the user namespace is provided during execution.
        Variables and functions created in this cell will be local to only this cell
        because to do otherwise would be unsafe. Mutable objects in the user namespace,
        however, can be altered and those changes will persist elsewhere in the
        notebook. Be aware that using py5 objects in a different notebook cell or
        reusing them in another Sketch can result in nasty errors and bizzare
        consequences."""
        args = parse_argstring(self.py5bot, line)

        success, result = check_for_problems(cell, "<py5bot>")
        if success:
            py5bot_globals, py5bot_settings, py5bot_setup = result
            if split_setup.count_noncomment_lines(py5bot_settings) == 0:
                py5bot_settings = 'size(100, 100, HIDDEN)'
            self._py5bot_mgr.write_code(
                '\n' + py5bot_globals, py5bot_settings, py5bot_setup)

            ns = self.shell.user_ns
            exec(self._py5bot_mgr.startup_code + self._py5bot_mgr.run_code, ns)
            png = ns['_PY5BOT_OUTPUT_']

            if args.filename:
                filename = filename_check(args.filename)
                png.save(filename)
                print(f'PNG file written to {filename}')
            if args.variable:
                if variable_name_check(args.variable):
                    self.shell.user_ns[args.variable] = png
                    print(f'PIL Image assigned to {args.variable}')
                else:
                    print(
                        f'Invalid variable name {args.variable}',
                        file=sys.stderr)

            if png is not None:
                display(png)
            del ns['_PY5BOT_OUTPUT_']
        else:
            print(result, file=sys.stderr)


def load_ipython_extension(ipython):
    ipython.register_magics(Py5BotMagics)
