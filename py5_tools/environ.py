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

class Environment:

    def __init__(self):
        try:
            __IPYTHON__  # type: ignore
            from ipykernel.zmqshell import ZMQInteractiveShell
            self.in_ipython_session = True
            self.ipython_shell = get_ipython()  # type: ignore
            self.in_jupyter_zmq_shell = isinstance(
                self.ipython_shell, ZMQInteractiveShell)
        except Exception:
            self.in_ipython_session = False
            self.ipython_shell = None
            self.in_jupyter_zmq_shell = False
