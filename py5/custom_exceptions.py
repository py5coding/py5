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
import re

from . import reference

JPYPE_TYPEERROR_REGEX = re.compile(
    r'No matching overloads found for [\w\.]*(\([^\)]*\))')


def handle_typeerror(exc_type_name, exc_msg, py5info):
    if py5info:
        filename, fname = py5info[-1]
        signatures = reference.METHOD_SIGNATURES_LOOKUP.get(
            (reference.FILE_CLASS_LOOKUP.get(filename), fname))
        if signatures:
            m = JPYPE_TYPEERROR_REGEX.search(exc_msg)
            passed = m.groups(1)[0].replace(',', ', ') + ' ' if m else ''
            exc_msg = 'The parameter types ' + passed + \
                'are invalid for method ' + fname + '.\n'
            if len(signatures) == 1:
                exc_msg += 'Your parameters must match the following signature:\n'
                exc_msg += ' * ' + fname + signatures[0]
            else:
                exc_msg += 'Your parameters must match one of the following signatures:\n'
                exc_msg += '\n'.join([' * ' + fname +
                                     sig for sig in signatures])

    return exc_msg


CUSTOM_EXCEPTION_MSGS = dict(
    TypeError=handle_typeerror,
)
