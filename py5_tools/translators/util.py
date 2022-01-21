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
from pathlib import Path
from typing import Union, Callable
from io import StringIO
import shlex
import autopep8


def translate_code(
        translate_token: Callable,
        code: str,
        post_translate: Callable = None):
    tokens = shlex.shlex(code)
    tokens.whitespace = ''
    tokens.wordchars += '.'
    tokens.commenters = ''
    tokens.quotes = ''

    out = StringIO()
    in_comment = False
    in_quote = None
    for token in tokens:
        if token in ["'", '"'] and not in_comment:
            if not in_quote:
                in_quote = token
            elif in_quote and token == in_quote:
                in_quote = None
        elif token == '#':
            in_comment = True
        elif token == '\n':
            in_comment = False
            in_quote = None
        elif not (in_comment or in_quote):
            token = translate_token(token)

        out.write(token)

    new_code = out.getvalue()

    if post_translate:
        new_code = post_translate(new_code)

    new_code = autopep8.fix_code(
        autopep8.fix_2to3(new_code),
        options=dict(
            aggressive=2))

    return new_code


def translate_file(translate_token: Callable,
                   src: Union[str,
                              Path],
                   dest: Union[str,
                               Path],
                   post_translate: Callable = None):
    src = Path(src)
    dest = Path(dest)

    with open(src, 'r') as f:
        new_code = translate_code(
            translate_token,
            f.read(),
            post_translate=post_translate)

    if not dest.parent.exists():
        dest.parent.mkdir(parents=True)

    with open(dest, "w") as f:
        f.write(new_code)


def translate_dir(translate_token: Callable,
                  src: Union[str,
                             Path],
                  dest: Union[str,
                              Path],
                  ext: str,
                  post_translate: Callable = None):
    src = Path(src)
    dest = Path(dest)

    print('translating code in', str(src))

    count = 0
    for src_file in src.glob('**/*' + ext):
        try:
            dest_file = dest / src_file.relative_to(src).with_suffix('.py')
            translate_file(
                translate_token,
                src_file,
                dest_file,
                post_translate=post_translate)
            print("translated " + str(src_file.relative_to(src)))
            count += 1
        except BaseException:
            print("error translating " + str(src_file.relative_to(src)))

    print(
        "complete: translated",
        count,
        "files written to output directory",
        str(dest))
