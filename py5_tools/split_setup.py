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
import re
import ast
import inspect

import py5_tools.parsing as parsing


COMMENT_LINE = re.compile(r'^\s*#.*' + chr(36), flags=re.MULTILINE)
DOCSTRING = re.compile(r'^\s*"""[^"]*"""', flags=re.MULTILINE | re.DOTALL)
MODULE_MODE_METHOD_LINE = re.compile(r'^\s*py5\.(\w+)\([^\)]*\)')
IMPORTED_MODE_METHOD_LINE = re.compile(r'^\s*(\w+)\([^\)]*\)')
GLOBAL_STATEMENT_LINE = re.compile(
    r'^\s*global\s+.*' + chr(36),
    flags=re.MULTILINE)


def _get_method_line_regex(mode):
    if mode == 'module':
        return MODULE_MODE_METHOD_LINE
    elif mode == 'imported':
        return IMPORTED_MODE_METHOD_LINE
    else:
        raise RuntimeError('only module mode and imported mode are supported')


def _remove_comments(code):
    # remove # comments
    code = COMMENT_LINE.sub('', code)
    # remove docstrings
    for docstring in DOCSTRING.findall(code):
        code = code.replace(docstring, (len(docstring.split('\n')) - 1) * '\n')

    return code


def find_cutoff(code, mode):
    method_line = _get_method_line_regex(mode)
    code = _remove_comments(code)

    # find the cutoff point
    for i, line in enumerate(code.split('\n')):
        if line == 'def setup():':
            continue
        if line.strip() and GLOBAL_STATEMENT_LINE.match(line):
            continue
        if line.strip() and not ((m := method_line.match(line)) and m.groups()[0] in [
                'size', 'full_screen', 'smooth', 'no_smooth', 'pixel_density']):
            cutoff = i
            break
    else:
        cutoff = i + 1

    return cutoff


def find_leading_global_statements_cutoff(code):
    code = _remove_comments(code)
    found_global_statement = False

    # find the cutoff point
    for i, line in enumerate(code.split('\n')):
        if line == 'def setup():':
            continue
        if line.strip() and GLOBAL_STATEMENT_LINE.match(line):
            found_global_statement = True
        if line.strip() and not GLOBAL_STATEMENT_LINE.match(line):
            cutoff = i
            break
    else:
        cutoff = i + 1

    return cutoff if found_global_statement else 0


def check_for_special_functions(code, mode):
    method_line = _get_method_line_regex(mode)
    code = _remove_comments(code)

    out = []
    for i, line in enumerate(code.split('\n')):
        m = method_line.match(line)
        if m and m.groups()[0] in [
            'size',
            'full_screen',
            'smooth',
            'no_smooth',
                'pixel_density']:
            out.append((i, m.groups()[0]))

    return out


def count_noncomment_lines(code):
    stripped_code = COMMENT_LINE.sub('', code).strip()
    return len(stripped_code.split('\n')) if stripped_code else 0


def transform(functions, sketch_globals, sketch_locals, println, *, mode):
    """if appropriate, transform setup() into settings() and (maybe) setup()

    This mimics the Processing functionality to allow users to put calls to
    size() in the setup() method instead of settings(), where truthfully it
    belongs. The Processing IDE will do some code transformation before Sketch
    execution to adjust the code and make it seem like the call to size() can
    be in setup(). This does the same thing.

    This only works for module mode and imported mode.
    """
    # return if there is nothing to do
    if 'settings' in functions or 'setup' not in functions:
        return functions

    try:
        setup = functions['setup']
        code = inspect.getsource(setup).strip()
        global_cutoff = find_leading_global_statements_cutoff(code) or 1
        cutoff = find_cutoff(code, mode)

        # build the fake code
        lines, lineno = inspect.getsourcelines(setup)
        filename = inspect.getfile(setup)
        fake_settings_code = (lineno - 1) * '\n' + "def _py5_faux_settings():\n" + (
            global_cutoff - 1) * '\n' + ''.join(lines[global_cutoff:cutoff])
        fake_setup_code = (lineno - 1) * '\n' + "def _py5_faux_setup():\n" + (
            cutoff - global_cutoff) * '\n' + ''.join([*lines[1:global_cutoff], *lines[cutoff:]])

        # if the fake settings code is empty, there's no need to change
        # anything
        if count_noncomment_lines(fake_settings_code) > 1:
            # parse the fake settings code and transform it if using imported
            # mode
            fake_settings_ast = ast.parse(
                fake_settings_code, filename=filename, mode='exec')
            if mode == 'imported':
                fake_settings_ast = parsing.transform_py5_code(
                    fake_settings_ast)
            # compile the fake code
            exec(
                compile(
                    fake_settings_ast,
                    filename=filename,
                    mode='exec'),
                sketch_globals,
                sketch_locals)
            # extract the results and cleanup
            functions['settings'] = sketch_locals['_py5_faux_settings']
            del sketch_globals['_py5_faux_settings']

            # if the fake setup code is empty, get rid of it. otherwise,
            # compile it
            if count_noncomment_lines(fake_setup_code) == 1:
                del functions['setup']
            else:
                # parse the fake setup code and transform it if using imported
                # mode
                fake_setup_ast = ast.parse(
                    fake_setup_code, filename=filename, mode='exec')
                if mode == 'imported':
                    fake_setup_ast = parsing.transform_py5_code(fake_setup_ast)
                # compile the fake code
                exec(
                    compile(
                        fake_setup_ast,
                        filename=filename,
                        mode='exec'),
                    sketch_globals,
                    sketch_locals)
                # extract the results and cleanup
                functions['setup'] = sketch_locals['_py5_faux_setup']
                del sketch_globals['_py5_faux_setup']

    except OSError as e:
        println(
            "Unable to obtain source code for setup(). Either make it obtainable or create a settings() function for calls to size(), fullscreen(), etc.",
            stderr=True)
    except Exception as e:
        println(
            "Exception thrown while analyzing setup() function:",
            str(e),
            stderr=True)

    return functions
