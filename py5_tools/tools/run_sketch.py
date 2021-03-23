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
import argparse

from py5_tools import imported


parser = argparse.ArgumentParser(description="Execute py5 sketch",
                                 epilog="this is the epilog")
parser.add_argument(
    action='store',
    dest='sketch_path',
    help='path to py5 sketch')
parser.add_argument('-c', '--classpath', action='store', dest='classpath',
                    help='extra directories to add to classpath')


def main():
    args = parser.parse_args()
    imported.run_code(args.sketch_path, classpath=args.classpath)


if __name__ == '__main__':
    main()
