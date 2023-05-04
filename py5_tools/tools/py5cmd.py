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
import cmd
import argparse
import platform
import glob
from pathlib import Path

import py5_tools
import py5_tools.imported


parser = argparse.ArgumentParser(description="py5 command tool")


SHORT_LIBRARY_TEMPLATE = """[{id}] Name: {name}
Author: {authors}
Summary: {sentence}
Categories: {categories}
Description: {paragraph}"""

FULL_LIBRARY_TEMPLATE = """[{id}] Name: {name}
Author: {authors}
Summary: {sentence}
Categories: {categories}
Library version: {prettyVersion}
Project URL: {url}
Download URL: {download}
Description: {paragraph}"""


class Py5Cmd(cmd.Cmd):

    def __init__(self):
        super().__init__()
        self._libraries = py5_tools.ProcessingLibraryInfo()
        self._running_sketches = []

    prompt = 'py5: '
    intro = "Welcome to the py5 command tool."

    def _print_library_info(self, info):
        info = info[0]

        return SHORT_LIBRARY_TEMPLATE.format(**info)

    def do_list_categories(self, line):
        """list_categories
        List the Processing library categories."""
        for c in self._libraries.categories:
            print(c)

    def do_show_category(self, line):
        """show_category [category name]
        Show information for all of the available libraries in a given category."""
        category_libraries = sorted(
            self._libraries.get_library_info(
                category=line),
            key=lambda x: x.get('name'))

        if category_libraries:
            for info in category_libraries:
                print(SHORT_LIBRARY_TEMPLATE.format(**info).strip() + '\n')
        else:
            print('No libraries found in category ' + line)

    def complete_show_category(self, text, line, begidx, endidx):
        if not text:
            completions = self._libraries.categories
        else:
            completions = [
                c for c in self._libraries.categories if c.startswith(text)]

        return completions

    def do_run_sketch(self, line):
        """run_sketch [path]
        Run the imported mode Sketch found at the given path."""
        if line:
            try:
                new_process = platform.system() != 'Windows'
                p = py5_tools.imported.run_code(line, new_process=new_process)
                if p:
                    self._running_sketches.append(p)
            except Exception as e:
                print(e)

    def complete_run_sketch(self, text, line, begidx, endidx):
        path = line[10:].strip()
        completions = []
        for p in glob.glob(path + '*'):
            completions.append(p[(len(path) - len(text)):] +
                               ('/' if Path(p).is_dir() else ''))
        return completions

    def do_get_library(self, line):
        """get_library [library name]
        Download a library and unzip it into a jars subdirectory."""
        try:
            self._libraries.download_zip('jars', library_name=line)
        except Exception as e:
            print(e)

    def complete_get_library(self, text, line, begidx, endidx):
        if not text:
            completions = self._libraries.names
        else:
            completions = [
                n for n in self._libraries.names if n.startswith(text)]

        return completions

    def do_library_info(self, line):
        """library_info [library name]
        Show information for the given library."""
        info = self._libraries.get_library_info(library_name=line)

        if len(info) == 0:
            print('There are no libraries named ' + line)
        elif len(info) == 1:
            print(FULL_LIBRARY_TEMPLATE.format(**info[0]).strip() + '\n')
        else:
            print('Multiple libraries found named ' + line)

    def complete_library_info(self, text, line, begidx, endidx):
        if not text:
            completions = self._libraries.names
        else:
            completions = [
                n for n in self._libraries.names if n.startswith(text)]

        return completions

    def emptyline(self):
        return None

    def shutdown(self):
        for p in self._running_sketches:
            p.terminate()
            p.join()

    def do_exit(self, line):
        """exit
        Quit the py5 command tool."""
        self.shutdown()
        return True

    def do_EOF(self, line):
        """exit
        Quit the py5 command tool."""
        self.shutdown()
        return True

    def postloop(self):
        print()


def main():
    args = parser.parse_args()
    py5cmd = Py5Cmd()
    py5cmd.cmdloop()


if __name__ == '__main__':
    main()
