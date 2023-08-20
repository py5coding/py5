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
import re

import py5_tools

from . import reference
from . import spelling

JPYPE_TYPEERROR_REGEX = re.compile(
    r'No matching overloads found for [\w\.]*(\([^\)]*\))')
IMPORTED_MODE_NAMEERROR_REGEX = re.compile(r"name '(\w+)' is not defined")


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


def handle_nameerror(exc_type_name, exc_msg, py5info):
    if py5_tools.imported.get_imported_mode():
        m = IMPORTED_MODE_NAMEERROR_REGEX.match(exc_msg)
        if m:
            fname = m.group(1)
            exc_msg = 'The name "' + fname + '" is not defined.'
            if fname == 'py5':
                return exc_msg + (' Your Sketch is also running in Imported Mode. ' +
                                  'Remember that in imported mode you do not access py5\'s methods ' +
                                  'with the `py5.` module prefix.')
            elif fname in py5_tools.reference.PY5_DIR_STR:
                return exc_msg + (' Your Sketch is also running in Imported Mode. ' +
                                  'If the code throwing this exception was imported into your ' +
                                  'main py5 Sketch code, please ensure the py5 Imported Mode marker ' +
                                  '"# PY5 IMPORTED MODE CODE" has been properly added to the module.')
            else:
                suggestion_list = spelling.suggestions(
                    fname, py5_tools.reference.PY5_DIR_STR)
                if suggestion_list:
                    exc_msg += ' Did you mean ' + suggestion_list + '?'

    return exc_msg


CUSTOM_EXCEPTION_MSGS = dict(
    TypeError=handle_typeerror,
    NameError=handle_nameerror,
)
