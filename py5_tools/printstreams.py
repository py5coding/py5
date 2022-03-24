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

from . import environ as _environ


class _DefaultPrintlnStream:

    def init(self):
        return self

    def print(self, text, end='\n', stderr=False):
        print(text, end=end, file=sys.stderr if stderr else sys.stdout)


class _DisplayPubPrintlnStream:

    def init(self):
        try:
            self.display_pub = _environ.Environment().ipython_shell.display_pub
            self.parent_header = self.display_pub.parent_header
        except BaseException:
            self.display_pub = None
            self.parent_header = None

        return self

    def print(self, text, end='\n', stderr=False):
        if self.display_pub is None or self.parent_header is None:
            print(text, end=end, file=sys.stderr if stderr else sys.stdout)
        else:
            content = dict(
                name='stderr' if stderr else 'stdout',
                text=text + end)
            msg = self.display_pub.session.msg(
                'stream', content, parent=self.parent_header)
            self.display_pub.session.send(
                self.display_pub.pub_socket, msg, ident=b'stream')


class _WidgetPrintlnStream:

    def init(self):
        try:
            import ipywidgets as widgets
            from IPython.display import display

            self.out = widgets.Output(layout=dict(
                max_height='200px', overflow='auto'))
            display(self.out)
        except BaseException:
            self.out = None

        return self

    def print(self, text, end='\n', stderr=False):
        if self.out is None:
            print(text, end=end, file=sys.stderr if stderr else sys.stdout)
        else:
            if stderr:
                self.out.append_stderr(text + end)
            else:
                self.out.append_stdout(text + end)
