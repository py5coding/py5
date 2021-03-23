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
import sys
import ast

from . import reference as ref

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


class ReservedWordsValidation(ast.NodeTransformer):

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

    def _format_problem_message(self, node: ast.Name):
        out = []

        if isinstance(node.ctx, ast.Del):
            out.append(
                f'Deleting py5 reserved word "{node.id}" on line {node.lineno} is discouraged and may causes errors in your sketch.')
        elif isinstance(node.ctx, ast.Store):
            out.append(
                f'Assignment to py5 reserved word "{node.id}" on line {node.lineno} is discouraged and may causes errors in your sketch.')

        if self._code:
            lines = self._code.splitlines()
            out.append(lines[node.lineno - 1])
            out.append((' ' * node.col_offset) + '^')

        return '\n'.join(out)


def check_reserved_words(code, code_ast):
    validator = ReservedWordsValidation(code, report_immediately=False)
    validator.visit(code_ast)
    return validator._problems


def transform_py5_code(code_ast: ast.Module):
    transformer = TransformDynamicVariablesToCalls()
    return ast.fix_missing_locations(transformer.visit(code_ast))
