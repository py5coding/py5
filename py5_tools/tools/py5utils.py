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
import argparse

import py5_tools.utilities


parser = argparse.ArgumentParser(description="Generate Py5Utilities framework")
parser.add_argument('-o', '--output', action='store', dest='output_dir',
                    help='output destination (defaults to current directory)')


def main():
    args = parser.parse_args()
    py5_tools.utilities.generate_utilities_framework(args.output_dir)


if __name__ == '__main__':
    main()
