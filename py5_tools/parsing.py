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
import ast
import re

import stackprinter

from . import reference as ref
from . import split_setup

try:
    from IPython.core.error import InputRejected
except ImportError:
    class InputRejected(Exception):
        pass


class Py5InputRejected(InputRejected):

    def _render_traceback_(self):
        return str(self).splitlines()


class TransformDynamicVariablesToCalls(ast.NodeTransformer):

    def __init__(self):
        super().__init__()
        self._dynamic_variables = ref.PY5_DYNAMIC_VARIABLES

    def visit_Call(self, node: ast.Call):
        # this makes sure that code like `mouse_x()` does not get transformed
        # to `mouse_x()()`.
        if isinstance(
                node.func,
                ast.Name) and node.func.id in self._dynamic_variables:
            # don't visit the node because that would allow `visit_Name` to
            # transform the call to `mouse_x()()`.
            return node
        else:
            self.generic_visit(node)
            return node

    def visit_Name(self, node: ast.Name):
        if node.id in self._dynamic_variables:
            if isinstance(node.ctx, ast.Load):
                return ast.Call(func=node, args=[], keywords=[])
            else:
                # TODO: if node.ctx is Store or Del, should it intervene?
                # no need to call generic_visit
                return node
        else:
            # no need to call generic_visit
            return node


class Py5CodeValidation(ast.NodeTransformer):

    def __init__(self, code=None, report_immediately=True):
        super().__init__()
        self._code = code
        self._report_immediately = report_immediately
        self._reserved_words = ref.PY5_DIR_STR
        self._problems = []

    def visit_Name(self, node: ast.Name):
        if node.id in self._reserved_words and isinstance(
                node.ctx, (ast.Store, ast.Del)):
            problem = self._format_problem_message(node)
            if self._report_immediately:
                # TODO: throwing an exception would cause the IPython kernel to
                # reject the input but I need syntax highlighting to work before
                # it makes sense to do this
                # raise Py5InputRejected(problem)
                sys.stdout.write(problem + '\n')
            self._problems.append(problem)
        self.generic_visit(node)
        return node

    def visit_FunctionDef(self, node: ast.FunctionDef):
        if node.name in self._reserved_words:
            problem = self._format_problem_message(node)
            if self._report_immediately:
                # raise Py5InputRejected(problem)
                sys.stdout.write(problem + '\n')
            self._problems.append(problem)
        self.generic_visit(node)
        return node

    def visit_Import(self, node: ast.Import):
        for alias in node.names:
            if alias.name == 'py5':
                problem = self._format_problem_message(node)
                if self._report_immediately:
                    raise Py5InputRejected(problem)
                self._problems.append(problem)

        self.generic_visit(node)
        return node

    def _format_problem_message(self, node):
        out = []

        if isinstance(node, ast.Name):
            if isinstance(node.ctx, ast.Del):
                out.append(
                    f'Deleting py5 reserved word "{node.id}" on line {node.lineno} is discouraged and may causes errors in your sketch.')
            elif isinstance(node.ctx, ast.Store):
                out.append(
                    f'Assignment to py5 reserved word "{node.id}" on line {node.lineno} is discouraged and may causes errors in your sketch.')
        elif isinstance(node, ast.Import):
            out.append(
                f'"import py5" found on line {node.lineno}. Do not import the py5 library, as this has already been done for you. Your code should be written without any "py5." prefixes.')
        elif isinstance(node, ast.FunctionDef):
            out.append(
                f'Defining a function named after py5 reserved word "{node.name}" on line {node.lineno} is discouraged and may causes errors in your sketch.')

        if self._code:
            lines = self._code.splitlines()
            out.append(lines[node.lineno - 1])
            out.append((' ' * node.col_offset) + '^')

        return '\n'.join(out)


def check_reserved_words(code, code_ast):
    validator = Py5CodeValidation(code, report_immediately=False)
    validator.visit(code_ast)
    return validator._problems


def transform_py5_code(code_ast: ast.Module):
    transformer = TransformDynamicVariablesToCalls()
    return ast.fix_missing_locations(transformer.visit(code_ast))


def check_for_problems(code, filename, *, tool=None):
    # if the code contains a setup() or a draw() function, the user could be
    # confused about static mode
    if (ms := re.findall(
            r'^def (setup|draw)[^:]*:', code, flags=re.MULTILINE)):
        msg = 'Your code contains ' + \
            (f'a {ms[0]}() function.' if len(ms) == 1 else 'setup() and draw() functions.')
        if tool:
            msg += f' When using {tool}, your code is written in static mode, without defining a setup() function or a draw() function.'
        else:
            msg += ' When coding in static mode, your code should not define a setup() function or  draw() function.'
        return False, msg

    # does the code parse? if not, return an error message
    try:
        sketch_ast = ast.parse(code, filename=filename, mode='exec')
    except IndentationError as e:
        msg = f'There is an indentation problem with your code on line {e.lineno}:\n'
        arrow_msg = f'--> {e.lineno}    '
        msg += f'{arrow_msg}{e.text}'
        msg += ' ' * (len(arrow_msg) + e.offset) + '^'
        return False, msg
    except Exception as e:
        msg = stackprinter.format(e)
        m = re.search(r'^SyntaxError:', msg, flags=re.MULTILINE)
        if m:
            msg = msg[m.start(0):]
        msg = 'There is a problem with your code:\n' + msg
        return False, msg

    # check for assignments to or deletions of reserved words
    problems = check_reserved_words(code, sketch_ast)
    if problems:
        msg = 'There ' + ('is a problem' if len(problems) ==
                          1 else f'are {len(problems)} problems') + ' with your code.\n'
        msg += '=' * len(msg) + '\n' + '\n'.join(problems)
        return False, msg

    cutoff1, cutoff2 = split_setup.find_cutoffs(
        code, 'imported', static_mode=True)
    lines = code.splitlines(keepends=True)
    py5static_globals = ''.join(lines[:cutoff1])
    py5static_settings = ''.join(lines[cutoff1:cutoff2])
    py5static_setup = ''.join(lines[cutoff2:])

    # check for calls to size, etc, that were not at the beginning of the code
    problems = split_setup.check_for_special_functions(
        py5static_setup, 'imported')
    if problems:
        msg = 'There ' + ('is a problem' if len(problems) ==
                          1 else f'are {len(problems)} problems') + ' with your code.\n'
        msg += 'The function ' + \
            ('call' if len(problems) == 1 else 'calls') + ' to '
        problems = [
            f'{name} (on line {i + cutoff2 + 1})' for i,
            name in problems]
        if len(problems) == 1:
            msg += problems[0]
        elif len(problems) == 2:
            msg += f'{problems[0]} and {problems[1]}'
        else:
            msg += ', and '.join(', '.join(problems).rsplit(', ', maxsplit=1))
        msg += ' must be moved to the beginning of your code, before any other code.'
        return False, msg

    return True, (py5static_globals, py5static_settings, py5static_setup)
