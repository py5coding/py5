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
import datetime as dt


def _get_sketch_and_sync_draw():
    import py5

    sketch = py5.get_current_sketch()
    sync_draw = sketch._get_sync_draw()

    return sketch, sync_draw


def screenshot(screenshot_name: str = None):
    """Create a screenshot of the current Sketch window.

    Parameters
    ----------

    screenshot_name: str = None
        name of file for screenshot

    Notes
    -----

    Create a screenshot of the current Sketch window. The screenshot image will be
    saved to the archive directory. By default, this is an `archive` subdirectory
    under the Sketch code's current working directory.

    If the `screenshot_name` parameter contains date format codes, the string will
    be formatted with the current timestamp. If `screenshot_name` is omitted, it
    will default to your filename stem followed by `"_%Y%m%d_%H%M%S"`. If you are
    using this function through a Jupyter Notebook, there is no usable filename so
    it will default to `"screenshot_%Y%m%d_%H%M%S"`.

    This function will save PNG images with the appropriate filename suffix if
    `screenshot_name` does not have a suffix. It won't overwrite an existing file if
    the file it tries to write to already exists.

    A suggested use case for this is to put the function calls in your code but
    leave them commented out. When you have working code that you want to create a
    screenshot for but don't want to pause your workflow to do that manually, simply
    uncomment the code and save the file. A screenshot will then be created for you
    in the `archive` subdirectory.

    This function will do nothing when not running through py5's Live Coding
    feature.

    Look at the online "Live Coding" documentation to learn more."""
    sketch, sync_draw = _get_sketch_and_sync_draw()

    if sketch.is_running and sync_draw is not None:
        stem = sync_draw.get_filename_stem() or "screenshot"
        screenshot_name = dt.datetime.now().strftime(
            screenshot_name or f"{stem}_%Y%m%d_%H%M%S"
        )

        sync_draw.take_screenshot(sketch, screenshot_name)


def copy_code(copy_name: str = None):
    """Create a backup copy of the current code.

    Parameters
    ----------

    copy_name: str = None
        name of file for copy of code

    Notes
    -----

    Create a backup copy of the current code. The copy will be saved to the archive
    directory. By default, this is an `archive` subdirectory under the Sketch code's
    current working directory.

    If the `copy_name` parameter contains date format codes, the string will be
    formatted with the current timestamp. If `copy_name` is omitted, it will default
    to your filename stem followed by `"_%Y%m%d_%H%M%S"`.

    This function will not work if the Live Coding feature is being used in a
    Jupyter Notebook because the code is not in a Python file that can be copied.

    If Live Coding is watching the directory for changes, the backup copy will be a
    zip file containing every file in the watched directory. Otherwise, it will be a
    regular Python file. The appropriate filename suffix will be set if `copy_name`
    does not already have it. It won't overwrite an existing file if the file it
    tries to write to already exists.

    A suggested use case for this is to put the function calls in your code but
    leave them commented out. When you have working code that you want to create a
    backup for but don't want to pause your workflow to do that manually, simply
    uncomment the code and resave the file. A copy of the code will then be created
    for you in the `archive` subdirectory.

    This function will do nothing when not running through py5's Live Coding
    feature.

    Look at the online "Live Coding" documentation to learn more."""
    sketch, sync_draw = _get_sketch_and_sync_draw()

    if sketch.is_running and sync_draw is not None:
        # if sync_draw.get_filename_stem() is None, the Sketch is running
        # through a notebook and sync_draw will decline to copy the code
        stem = sync_draw.get_filename_stem() or "copy"
        copy_name = dt.datetime.now().strftime(copy_name or f"{stem}_%Y%m%d_%H%M%S")

        sync_draw.copy_code(sketch, copy_name)


def snapshot(snapshot_name: str = None):
    """Create a screenshot of the current Sketch window and a backup copy of the
    current code.

    Parameters
    ----------

    snapshot_name: str = None
        name of file for screenshot and code archive

    Notes
    -----

    Create a screenshot of the current Sketch window and a backup copy of the
    current code. This function combines the functionality of
    `py5_tools.live_coding.screenshot()` and `py5_tools.live_coding.copy_code()`.
    Everything will be saved to the archive directory. By default, this is an
    `archive` subdirectory under the Sketch code's current working directory.

    See the documentation for `py5_tools.live_coding.screenshot()` and
    `py5_tools.live_coding.copy_code()` for more information about each feature.

    If the `snapshot_name` parameter contains date format codes, the string will be
    formatted with the current timestamp. If `snapshot_name` is omitted, it will
    default to your filename stem followed by `"_%Y%m%d_%H%M%S"`. If you are using
    this function through a Jupyter Notebook, there is no usable filename so it will
    default to `"snapshot_%Y%m%d_%H%M%S"`. Although if you are using this function
    through a Jupyter Notebook, it will decline to create a backup copy of the code
    so you are better off using `py5_tools.live_coding.screenshot()` instead.

    A suggested use case for this is to put the function calls in your code but
    leave them commented out. When you have working code that you want to create a
    backup and a screenshot for but don't want to pause your workflow to do both
    manually, simply uncomment the code and save the file. A backup and a screenshot
    will then be created for you in the `archive` subdirectory.

    This function will do nothing when not running through py5's Live Coding
    feature.

    Look at the online "Live Coding" documentation to learn more."""
    sketch, sync_draw = _get_sketch_and_sync_draw()

    if sketch.is_running and sync_draw is not None:
        # if sync_draw.get_filename_stem() is None, the Sketch is running
        # through a notebook and sync_draw will decline to copy the code
        stem = sync_draw.get_filename_stem() or "snapshot"
        snapshot_name = dt.datetime.now().strftime(
            snapshot_name or f"{stem}_%Y%m%d_%H%M%S"
        )

        screenshot(screenshot_name=snapshot_name)
        copy_code(copy_name=snapshot_name)


def count() -> int:
    """Return the number of times the live code has been updated.

    Notes
    -----

    Return the number of times the live code has been updated. This starts at zero
    and increments by one each time py5's Live Coding system updates the code. If
    you exit a Sketch using py5's Live Coding functionality and restart it, the
    counter resets to zero. The purpose of this function is to provide people using
    Live Coding with a value that changes from one code iteration to the next. This
    isn't otherwise possible because the Live Coding feature will reset the global
    namespace each time the code is updated.

    A good use case for this is to pair it with `py5_tools.live_coding.screenshot()`
    or `py5_tools.live_coding.copy_code()` to create a unique string to name the
    code backup copy or the screenshot. This is an alternative to timestamps.

    This function will always return 0 when not running through py5's Live Coding
    feature.

    Look at the online "Live Coding" documentation to learn more."""
    sketch, sync_draw = _get_sketch_and_sync_draw()

    if sketch.is_running and sync_draw is not None:
        return sync_draw.update_count
    else:
        return 0
