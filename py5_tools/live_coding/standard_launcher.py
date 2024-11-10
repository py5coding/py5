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
import platform
import sys
from pathlib import Path

######################################################################
# STANDARD *.PY FILE LIVE CODING
######################################################################


class MockRunSketch:
    def __init__(self, global_namespace):
        self._global_namespace = global_namespace
        self._kwargs = {}
        self._called = False

    def __call__(self, *args, **kwargs):
        import py5

        from .syncing import Py5RunSketchBlockException

        self._called = True
        if "sketch_functions" in kwargs:
            kwargs.pop("sketch_functions")

        self._kwargs = kwargs

        if platform.system() == "Darwin":
            kwargs["block"] = True

        (
            self._functions,
            self._function_param_counts,
        ) = py5.bridge._extract_py5_user_function_data(self._global_namespace)

        if "block" not in kwargs or kwargs["block"]:
            raise Py5RunSketchBlockException("run_sketch() blocking")


def launch_live_coding(
    filename,
    *,
    always_rerun_setup=True,
    always_on_top=True,
    show_framerate=False,
    activate_keyboard_shortcuts=False,
    watch_dir=False,
    archive_dir="archive",
):
    try:
        sys.path[0] = str(Path(filename).absolute().parent)

        import py5

        from .syncing import LIVE_CODING_FILE, SyncDraw, init_namespace

        global_namespace = dict()
        init_namespace(filename, global_namespace)

        # this needs to be before keep_functions_current_from_file() is called
        # The MockRunSketch class captures user parameters passed to run_sketch()
        real_run_sketch = py5.run_sketch
        py5.run_sketch = (mock_run_sketch := MockRunSketch(global_namespace))

        sync_draw = SyncDraw(
            LIVE_CODING_FILE,
            filename=filename,
            global_namespace=global_namespace,
            always_rerun_setup=always_rerun_setup,
            always_on_top=always_on_top,
            show_framerate=show_framerate,
            activate_keyboard_shortcuts=activate_keyboard_shortcuts,
            watch_dir=watch_dir,
            archive_dir=archive_dir,
            mock_run_sketch=mock_run_sketch,
        )

        sketch = py5.get_current_sketch()
        sync_draw._init_hooks(sketch)

        if sync_draw.keep_functions_current_from_file(sketch, force_update=True):
            if not mock_run_sketch._called:
                sketch.println(
                    f"File {filename} has no call to py5's run_sketch() method. py5 will make the call for you, but please add it to the end of the file to avoid this message."
                )

            real_run_sketch(
                sketch_functions=sync_draw.functions, **mock_run_sketch._kwargs
            )
        else:
            sketch.println("Error in live coding startup...please fix and try again")

    except Exception as e:
        print(e)
