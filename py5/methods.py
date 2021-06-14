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
from pathlib import Path
from collections import defaultdict
from typing import Union
import line_profiler

from jpype import JImplements, JOverride, JString, JClass

import stackprinter

from . import custom_exceptions


_JavaNullPointerException = JClass('java.lang.NullPointerException')

# *** stacktrace configuration ***
# set stackprinter color style. Default is plaintext. Other choices are darkbg,
# darkbg2, darkbg3, lightbg, lightbg2, lightbg3.
_stackprinter_style = 'plaintext'
# prune tracebacks to only show only show stack levels in the user's py5 code.
_prune_tracebacks = True
_module_install_dir = str(Path(__file__).parent)


_EXCEPTION_MSGS = {
    **custom_exceptions.CUSTOM_EXCEPTION_MSGS,
}


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
                if f_code.co_filename.startswith(_module_install_dir):
                    py5info.append((Path(f_code.co_filename[(len(_module_install_dir) + 1):]).parts,
                                    f_code.co_name))
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
                          r"lib/python.*?/site-packages/py5/"])

    if _prune_tracebacks:
        errmsg = errmsg.replace(
            str(exc_value),
            _exception_msg(
                println,
                exc_type.__name__,
                str(exc_value),
                py5info))

    println(errmsg, stderr=True)

    sys.last_type, sys.last_value, sys.last_traceback = exc_type, exc_value, exc_tb


@JImplements('py5.core.Py5Methods')
class Py5Methods:

    def __init__(self, sketch):
        self._sketch = sketch
        self._functions = dict()
        self._pre_hooks = defaultdict(dict)
        self._post_hooks = defaultdict(dict)
        self._profiler = line_profiler.LineProfiler()
        self._is_terminated = False

    def set_functions(self, **kwargs):
        self._functions.update(kwargs)

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
        return [JString(s) for s in self._functions.keys()]

    @JOverride
    def run_method(self, method_name, params):
        try:
            if method_name in self._functions:
                # first run the pre-hooks, if any
                if method_name in self._pre_hooks:
                    for hook in list(self._pre_hooks[method_name].values()):
                        hook(self._sketch)

                # now run the actual method
                self._functions[method_name](*params)

                # finally, post-hooks
                if method_name in self._post_hooks:
                    for hook in list(self._post_hooks[method_name].values()):
                        hook(self._sketch)
            return True
        except Exception:
            handle_exception(self._sketch.println, *sys.exc_info())
            self._sketch._terminate_sketch()
            return False

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
