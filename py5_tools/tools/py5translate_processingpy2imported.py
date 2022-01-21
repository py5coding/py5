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
from pathlib import Path

from py5_tools import translators


parser = argparse.ArgumentParser(
    description="Translate processing.py code to imported mode code")
parser.add_argument(
    action='store',
    dest='src',
    help='path to processing.py code')
parser.add_argument(
    action='store',
    dest='dest',
    help='path to imported mode code')


def main():
    args = parser.parse_args()
    src = Path(args.src)
    dest = Path(args.dest)

    if not src.exists():
        print(f'Error: Code source {src} does not exist')
        return

    if src.is_dir() and (dest.is_dir() or not dest.exists()):
        translators.processingpy2imported.translate_dir(src, dest)
    elif src.is_file() and (dest.is_file() or not dest.exists()):
        translators.processingpy2imported.translate_file(src, dest)
    else:
        print('Error: The two arguments must both be directories or both be files')


if __name__ == '__main__':
    main()
