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
import re
from pathlib import Path
from collections import defaultdict
from typing import Union
import inspect
import line_profiler
import traceback

from jpype import JClass, JImplements, JOverride, JString

import stackprinter

import py5_tools
from . import reference
from . import custom_exceptions

_stackprinter_style = 'plaintext'
# prune tracebacks to only show only show stack levels in the user's py5 code.
_prune_tracebacks = True

_MODULE_INSTALL_DIR = str(Path(__file__).parent)
_PY5TOOLS_MODULE_INSTALL_DIR = str(Path(py5_tools.__file__).parent)

_PY5_STATIC_CODE_FILENAME_REGEX = re.compile(
    r'File "[^\"]*?_PY5_STATIC_(SETUP|SETTINGS|FRAMEWORK)_CODE_\.py", line \d+, in .*')

_EXCEPTION_MSGS = {
    **custom_exceptions.CUSTOM_EXCEPTION_MSGS,
}

_JAVA_RUNTIMEEXCEPTION = JClass('java.lang.RuntimeException')


def check_run_method_callstack():
    for t in traceback.extract_stack():
        if t.filename == __file__ and t.name == 'run_method':
            return True
    else:
        return False


def _exception_msg(println, exc_type_name, exc_msg, py5info):
    try:
        msg = _EXCEPTION_MSGS.get(exc_type_name, exc_msg)
        if isinstance(msg, str):
            return msg
        elif callable(msg):
            return msg(exc_type_name, exc_msg, py5info)
        else:
            println(
                f'unknown exception msg type for {exc_type_name}: {type(msg).__name__}',
                stderr=True)
            return exc_msg
    except Exception as e:
        println(
            f'error generating exception msg for {exc_type_name}: {e}',
            stderr=True)
        return exc_msg


def register_exception_msg(exc_type_name: str, msg: Union[str, callable]):
    _EXCEPTION_MSGS[exc_type_name] = msg


def handle_exception(println, exc_type, exc_value, exc_tb):
    py5info = []
    try:
        if _prune_tracebacks and hasattr(exc_tb, 'tb_next'):
            prev_tb = exc_tb
            trim_tb = None
            tb = exc_tb.tb_next
            while hasattr(tb, 'tb_next') and hasattr(tb, 'tb_frame'):
                f_code = tb.tb_frame.f_code
                if f_code.co_filename.startswith(
                        _MODULE_INSTALL_DIR) and not f_code.co_name.endswith('py5_no_prune'):
                    py5info.append((Path(f_code.co_filename[(len(_MODULE_INSTALL_DIR) + 1):]).parts,
                                    f_code.co_name))
                    if trim_tb is None:
                        trim_tb = prev_tb
                elif f_code.co_filename.startswith(_PY5TOOLS_MODULE_INSTALL_DIR) and not f_code.co_name.endswith('py5_no_prune'):
                    py5info.append((Path(f_code.co_filename[(
                        len(_PY5TOOLS_MODULE_INSTALL_DIR) + 1):]).parts, f_code.co_name))
                    if trim_tb is None:
                        trim_tb = prev_tb
                prev_tb = tb
                tb = tb.tb_next
            if trim_tb:
                trim_tb.tb_next = None
    except Exception as e:
        println(
            f'Exception thrown while examining error traceback: {str(e)}',
            stderr=True)

    errmsg = stackprinter.format(
        thing=(exc_type, exc_value, exc_tb.tb_next),
        show_vals='line',
        style=_stackprinter_style,
        suppressed_paths=[r"lib/python.*?/site-packages/numpy/",
                          r"lib/python.*?/site-packages/py5/",
                          r"lib/python.*?/site-packages/py5tools/"])

    if _prune_tracebacks:
        errmsg = errmsg.replace(
            str(exc_value),
            _exception_msg(
                println,
                exc_type.__name__,
                str(exc_value),
                py5info))

        while m := _PY5_STATIC_CODE_FILENAME_REGEX.search(errmsg):
            errmsg = errmsg[m.span()[1]:]
        else:
            errmsg = "py5 encountered an error in your code:\n\n" + errmsg

    println(errmsg, stderr=True)

    sys.last_type, sys.last_value, sys.last_traceback = exc_type, exc_value, exc_tb


def _extract_py5_user_function_data(d: dict):
    functions = dict()
    function_param_counts = dict()
    for name, allowed_parg_count in reference.METHODS.items():
        if name not in d or not callable(d[name]):
            continue

        sig = inspect.signature(d[name])
        pargs_count = len([p for p in sig.parameters.values() if p.kind in [
                          inspect.Parameter.POSITIONAL_ONLY, inspect.Parameter.POSITIONAL_OR_KEYWORD]])
        if pargs_count != len(
                sig.parameters) or pargs_count not in allowed_parg_count:
            continue

        functions[name] = d[name]
        function_param_counts[name] = pargs_count

    return functions, function_param_counts


@JImplements('py5.core.Py5Bridge')
class Py5Bridge:

    def __init__(self, sketch):
        self._sketch = sketch
        self._caller_locals = dict()
        self._caller_globals = dict()
        self._functions = dict()
        self._function_param_counts = dict()
        self._pre_hooks = defaultdict(dict)
        self._post_hooks = defaultdict(dict)
        self._profiler = line_profiler.LineProfiler()
        self._current_running_method = None
        self._is_terminated = False

        from .object_conversion import convert_to_python_types, convert_to_java_type
        self._convert_to_python_types = convert_to_python_types
        self._convert_to_java_type = convert_to_java_type

    def set_caller_locals_globals(self, locals, globals):
        self._caller_locals = locals
        self._caller_globals = globals

    def set_functions(self, functions, function_param_counts):
        self._function_param_counts = dict()
        self._functions = dict()
        self.add_functions(functions, function_param_counts)

    def add_functions(self, functions, function_param_counts):
        for name, f in functions.items():
            self._functions[name] = f
            if name == 'settings':
                self._function_param_counts['settings'] = function_param_counts.get(
                    'settings', function_param_counts.get('setup'))
            else:
                self._function_param_counts[name] = function_param_counts[name]

    def has_function(self, function_name):
        return function_name in self._functions

    def profile_functions(self, function_names):
        for fname in function_names:
            func = self._functions[fname]
            self._profiler.add_function(func)
            self._functions[fname] = self._profiler.wrap_function(func)

    def dump_stats(self):
        self._profiler.print_stats()

    def add_pre_hook(self, method_name, hook_name, hook):
        if self._is_terminated and hasattr(hook, 'sketch_terminated'):
            hook.sketch_terminated()
        else:
            self._pre_hooks[method_name][hook_name] = hook

    def add_post_hook(self, method_name, hook_name, hook):
        if self._is_terminated and hasattr(hook, 'sketch_terminated'):
            hook.sketch_terminated()
        else:
            self._post_hooks[method_name][hook_name] = hook

    def add_pre_hooks(self, method_hooks):
        for method_name, hook_name, hook in method_hooks:
            self.add_pre_hook(method_name, hook_name, hook)

    def add_post_hooks(self, method_hooks):
        for method_name, hook_name, hook in method_hooks:
            self.add_post_hook(method_name, hook_name, hook)

    def remove_pre_hook(self, method_name, hook_name):
        if hook_name in self._pre_hooks[method_name]:
            self._pre_hooks[method_name].pop(hook_name)

    def remove_post_hook(self, method_name, hook_name):
        if hook_name in self._post_hooks[method_name]:
            self._post_hooks[method_name].pop(hook_name)

    def terminate_hooks(self):
        for method_name, hooks in self._pre_hooks.items():
            for hook_name, hook in list(hooks.items()):
                if hasattr(hook, 'sketch_terminated'):
                    hook.sketch_terminated()
                self.remove_pre_hook(method_name, hook_name)
        for method_name, hooks in self._post_hooks.items():
            for hook_name, hook in list(hooks.items()):
                if hasattr(hook, 'sketch_terminated'):
                    hook.sketch_terminated()
                self.remove_post_hook(method_name, hook_name)

    @JOverride
    def get_function_list(self):
        return [JString(f'{name}:{self._function_param_counts[name]}')
                for name in self._functions.keys()]

    @JOverride
    def terminate_sketch(self):
        self._sketch._terminate_sketch()

    @JOverride
    def run_method(self, method_name, params):
        try:
            if method_name in self._functions:
                self._current_running_method = method_name

                # first run the pre-hooks, if any
                if method_name in self._pre_hooks:
                    for hook in list(self._pre_hooks[method_name].values()):
                        hook(self._sketch)

                # now run the actual method
                self._functions[method_name](
                    *self._convert_to_python_types(params))

                # finally, post-hooks
                if method_name in self._post_hooks:
                    for hook in list(self._post_hooks[method_name].values()):
                        hook(self._sketch)
            return True
        except Exception:
            handle_exception(self._sketch.println, *sys.exc_info())
            self.terminate_sketch()
            return False
        finally:
            self._current_running_method = None

    def _get_current_running_method(self):
        return self._current_running_method
    current_running_method = property(fget=_get_current_running_method)

    @JOverride
    def call_function(self, key, params):
        try:
            key = str(key)
            *str_hierarchy, c = key.split('.')
            key_start = key.split('.')[0]

            if key_start in py5_tools.config._PY5_PROCESSING_MODE_KEYS:
                d = py5_tools.config._PY5_PROCESSING_MODE_KEYS
            elif key_start in self._caller_locals:
                d = self._caller_locals
            elif key_start in self._caller_globals:
                d = self._caller_globals
            else:
                return _JAVA_RUNTIMEEXCEPTION(
                    f'callable {c} not found with key {key}')

            for s in str_hierarchy:
                if s in d:
                    subd = d[s]
                    if isinstance(subd, dict):
                        d = subd
                    elif hasattr(subd, '__dir__') or hasattr(subd, '__dict__'):
                        d = {k: getattr(subd, k) for k in dir(subd)}
                    else:
                        return _JAVA_RUNTIMEEXCEPTION(
                            f'{s} in key {key} does not map to a dict or an object that can be inspected with dir()')
                else:
                    return _JAVA_RUNTIMEEXCEPTION(
                        f'{s} not found with key {key}')

            if c not in d or not callable(func := d[c]):
                return _JAVA_RUNTIMEEXCEPTION(
                    f'callable {c} not found with key {key}')

            try:
                retval = func(*self._convert_to_python_types(params))
                if key in py5_tools.config._PY5_PROCESSING_MODE_CALLBACK_ONCE:
                    py5_tools.config._PY5_PROCESSING_MODE_CALLBACK_ONCE.remove(
                        key)
                    if key in py5_tools.config._PY5_PROCESSING_MODE_KEYS:
                        py5_tools.config._PY5_PROCESSING_MODE_KEYS.pop(key)
                return self._convert_to_java_type(retval)
            except Exception as e:
                handle_exception(self._sketch.println, *sys.exc_info())
                return _JAVA_RUNTIMEEXCEPTION(str(e))
        except Exception as e:
            return _JAVA_RUNTIMEEXCEPTION(str(e))

    @JOverride
    def py5_println(self, text, stderr):
        self._sketch.println(text, stderr=stderr)

    @JOverride
    def shutdown(self):
        try:
            self._sketch._shutdown()
            self._is_terminated = True
            self.terminate_hooks()
        except Exception:
            self._sketch.println(
                'exception in sketch shutdown sequence',
                stderr=True)
