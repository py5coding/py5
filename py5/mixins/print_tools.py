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
from typing import Any


class PrintlnStream:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._println_stream = None

    def _init_println_stream(self):
        self._println_stream.init()

    # *** BEGIN METHODS ***

    def set_println_stream(self, println_stream: Any) -> None:
        """Customize where the output of ``println()`` goes.

        Parameters
        ----------

        println_stream: Any
            println stream object to be used by println method

        Notes
        -----

        Customize where the output of ``println()`` goes.

        When running a Sketch asynchronously through Jupyter Notebook, any ``print``
        statements using Python's builtin function will always appear in the output of
        the currently active cell. This will rarely be desirable, as the active cell
        will keep changing as the user executes code elsewhere in the notebook. The
        ``println()`` method was created to provide users with print functionality in a
        Sketch without having to cope with output moving from one cell to the next. Use
        ``set_println_stream`` to change how the output is handled. The
        ``println_stream`` object must provide ``init()`` and ``print()`` methods, as
        shown in the example. The example demonstrates how to configure py5 to output
        text to an IPython Widget."""
        self._println_stream = println_stream

    def println(
            self,
            *args,
            sep: str = ' ',
            end: str = '\n',
            stderr: bool = False) -> None:
        """Print text or other values to the screen.

        Parameters
        ----------

        args
            values to be printed

        end: str = '\\n'
            string appended after the last value, defaults to newline character

        sep: str = ' '
            string inserted between values, defaults to a space

        stderr: bool = False
            use stderr instead of stdout

        Notes
        -----

        Print text or other values to the screen. For a Sketch running outside of a
        Jupyter Notebook, this method will behave the same as the Python's builtin
        ``print`` method. For Sketches running in a Jupyter Notebook, this will place
        text in the output of the cell that made the ``run_sketch()`` call.

        When running a Sketch asynchronously through Jupyter Notebook, any ``print``
        statements using Python's builtin function will always appear in the output of
        the currently active cell. This will rarely be desirable, as the active cell
        will keep changing as the user executes code elsewhere in the notebook. This
        method was created to provide users with print functionality in a Sketch without
        having to cope with output moving from one cell to the next.

        Use ``set_println_stream()`` to customize the behavior of ``println()``."""
        self._println_stream.print(sep.join(str(x)
                                   for x in args), end=end, stderr=stderr)
