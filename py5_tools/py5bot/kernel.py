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

from ipykernel.zmqshell import ZMQInteractiveShell
from IPython.core.interactiveshell import InteractiveShellABC
from ipykernel.kernelapp import IPKernelApp

from traitlets import Type, Instance, Unicode, List

from ..kernel.kernel import Py5Kernel
from .. import split_setup
from . import py5bot
from ..parsing import TransformDynamicVariablesToCalls, Py5CodeValidation


class Py5BotShell(ZMQInteractiveShell):

    # needed to make sure code using the %%python bypass gets transformed
    ast_transformers = List(
        [TransformDynamicVariablesToCalls(), Py5CodeValidation()]).tag(config=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._py5bot_mgr = py5bot.Py5BotManager()

    banner2 = Unicode("Activating py5bot").tag(config=True)

    def run_cell(
            self,
            raw_cell,
            store_history=False,
            silent=False,
            shell_futures=True):
        # check for special code that should bypass py5bot processing
        if raw_cell.strip().startswith('%%python\n'):
            return super(
                Py5BotShell,
                self).run_cell(
                raw_cell.replace(
                    '%%python\n',
                    ''),
                store_history=store_history,
                silent=silent,
                shell_futures=shell_futures)

        success, result = py5bot.check_for_problems(raw_cell, "<py5bot>")
        if success:
            py5bot_globals, py5bot_settings, py5bot_setup = result
            if split_setup.count_noncomment_lines(py5bot_settings) == 0:
                py5bot_settings = 'size(100, 100, HIDDEN)'
            self._py5bot_mgr.write_code(
                py5bot_globals, py5bot_settings, py5bot_setup)

            return super(
                Py5BotShell,
                self).run_cell(
                self._py5bot_mgr.run_code,
                store_history=store_history,
                silent=silent,
                shell_futures=shell_futures)
        else:
            print(result, file=sys.stderr)

            return super(
                Py5BotShell,
                self).run_cell(
                'None',
                store_history=store_history,
                silent=silent,
                shell_futures=shell_futures)


InteractiveShellABC.register(Py5BotShell)


class Py5BotKernel(Py5Kernel):
    shell = Instance('IPython.core.interactiveshell.InteractiveShellABC',
                     allow_none=True)
    shell_class = Type(Py5BotShell)

    implementation = 'py5bot'
    implementation_version = '0.7.1a6'


class Py5BotApp(IPKernelApp):
    name = 'py5bot-kernel'

    kernel_class = Type('py5_tools.py5bot.Py5BotKernel',
                        klass='ipykernel.kernelbase.Kernel').tag(config=True)

    exec_lines = List(Unicode(), [
        '%%python\n' + py5bot.PY5BOT_CODE_STARTUP
    ]).tag(config=True)
