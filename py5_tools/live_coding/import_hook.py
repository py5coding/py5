# *****************************************************************************
#
#   Part of the py5 library
#   Copyright (C) 2020-2024 Jim Schmitz
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
from importlib.machinery import PathFinder
from pathlib import Path


class Py5LiveCodingFinder(PathFinder):
    def __init__(self, watch_dir: Path):
        super().__init__()

        self.watch_dir = watch_dir.absolute()
        self.imported_modules = []

    def flush_imported_modules(self):
        for module in self.imported_modules:
            if module in sys.modules:
                del sys.modules[module]

        self.imported_modules = []

    def find_spec(self, fullname, path, target=None):
        output = super().find_spec(fullname, path, target)

        if output is not None:
            try:
                origin = Path(output.origin).absolute()
                _ = origin.relative_to(self.watch_dir)

                if fullname not in self.imported_modules:
                    self.imported_modules.append(fullname)
            except Exception:
                # we don't care about this one
                pass

        return output


def activate_py5_live_coding_import_hook(watch_dir: Path) -> Py5LiveCodingFinder:
    finder = Py5LiveCodingFinder(watch_dir)
    sys.meta_path.insert(0, finder)

    return finder
