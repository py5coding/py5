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
import time
import re

from IPython.core.magic_arguments import MagicHelpFormatter


class CellMagicHelpFormatter(MagicHelpFormatter):

    def add_usage(self, usage, actions, groups, prefix="::\n\n  %%"):
        super(
            MagicHelpFormatter,
            self).add_usage(
            usage,
            actions,
            groups,
            prefix)


def fix_triple_quote_str(code):
    for m in re.finditer(r'\"\"\"[^\"]*\"\"\"', code):
        code = code.replace(
            m.group(), m.group().replace('\n    ', '\n'))
    return code


def wait(wait_time, sketch):
    end_time = time.time() + wait_time
    while time.time() < end_time and sketch.is_running:
        time.sleep(0.1)


__all__ = ['CellMagicHelpFormatter', 'fix_triple_quote_str', 'wait']
