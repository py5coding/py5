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
from pathlib import Path
import ast
import re

from importlib.abc import Loader, MetaPathFinder
from importlib.util import spec_from_file_location

import py5_tools


PY5_IMPORTED_MODE_CODE_MARKER_REGEX = re.compile(
    r"^# PY5 IMPORTED MODE CODE\s*$",
    re.MULTILINE | re.IGNORECASE)
PY5_HEADER = '\n\n\n'.join(
    [f'def {dvar}():\n    return get_current_sketch().{dvar}' for dvar in py5_tools.reference.PY5_DYNAMIC_VARIABLES])


class Py5ImportError(ImportError):
    pass


class Py5ImportedModeFinder(MetaPathFinder):

    def __init__(self):
        super().__init__()
        self._validated_py5_module_mode_paths = []

    def find_spec(self, fullname, path, target=None):
        if path is None or path == "":
            path = [Path.cwd()]

            # first, determine if this is py5 imported mode code
            marker_file1 = Path(path[0], fullname + ".py")
            marker_file2 = Path(path[0], fullname, "__init__.py")

            if marker_file1.exists():
                with open(marker_file1) as f:
                    data = f.read()
                if not PY5_IMPORTED_MODE_CODE_MARKER_REGEX.search(data):
                    return None
            elif marker_file2.exists():
                with open(marker_file2) as f:
                    data = f.read()
                if PY5_IMPORTED_MODE_CODE_MARKER_REGEX.search(data):
                    self._validated_py5_module_mode_paths.append(
                        marker_file2.parent)
                else:
                    return None
            else:
                # if we get here, this must be a module without a __init__.py
                # file?
                return None

        else:
            # this is a subpackage import. is it one we've seen before and
            # determined to be a py5 imported mode code?
            for approved_path in self._validated_py5_module_mode_paths:
                if str(path[0]).startswith(str(approved_path)):
                    break
            else:
                return None

        # this is py5 imported mode code
        name = fullname.split(".")[-1]
        for entry in path:
            if Path(entry, name).is_dir():
                filename = Path(entry, name, "__init__.py")
                submodule_locations = [Path(entry, name)]
            else:
                filename = Path(entry, name + ".py")
                submodule_locations = None
            if not filename.exists():
                continue

            return spec_from_file_location(
                fullname,
                filename,
                loader=Py5ImportedModeLoader(filename),
                submodule_search_locations=submodule_locations)

        return None  # don't import this


class Py5ImportedModeLoader(Loader):
    def __init__(self, filename):
        self.filename = filename

    def create_module(self, spec):
        # default module creation semantics
        return None

    def exec_module(self, module):
        with open(self.filename) as f:
            code_src = f.read()

        # parse the unaltered code to check for reserved word problems
        code_ast = ast.parse(code_src, filename=self.filename, mode='exec')
        problems = py5_tools.parsing.check_reserved_words(code_src, code_ast)
        if problems:
            msg = 'There ' + ('is a problem' if len(problems) ==
                              1 else f'are {len(problems)} problems') + ' with the imported "' + str(module.__name__) + '" module.\n'
            msg += '=' * len(msg) + '\n' + '\n'.join(problems)
            raise Py5ImportError(msg)

        # add the necessary helper methods for for dynamic variables
        code_src = PY5_HEADER + "\n\n\n" + code_src

        # parse and compile the altered code
        code_ast = ast.parse(code_src, filename=self.filename, mode='exec')
        code_ast = py5_tools.parsing.transform_py5_code(code_ast)
        source = compile(code_ast, self.filename, 'exec')

        # exec the code in a temporary namespace
        import py5
        exec(source, ns := {**vars(py5), **vars(module)})

        # add user's code to the module. the filtering makes sure we don't add
        # py5 methods necessary for proper execution to the module's namespace
        for name, value in ns.items():
            if name not in py5.__dict__ and name not in py5_tools.reference.PY5_DYNAMIC_VARIABLES:
                setattr(module, name, value)


def activate_py5_import_hook():
    sys.meta_path.insert(0, Py5ImportedModeFinder())
