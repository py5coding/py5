# *****************************************************************************
#
#   Part of the py5 library
#   Copyright (C) 2020-2026 Jim Schmitz
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
"""
Utilities and accessory tools for py5.
"""
from . import live_coding  # noqa
from . import processing  # noqa
from . import translators  # noqa
from .config import *  # noqa
from .constants import VERSION as __version__
from .hooks import *  # noqa
from .imported import _lock_imported_mode, get_imported_mode, set_imported_mode  # noqa
from .jvm import *  # noqa

__all__ = [
    "__version__",
    "add_classpath",
    "add_jars",
    "add_options",
    "animated_gif",
    "capture_frames",
    "get_classpath",
    "get_jvm_debug_info",
    "is_jvm_running",
    "live_coding",
    "offline_frame_processing",
    "processing",
    "register_processing_mode_key",
    "save_frames",
    "screenshot",
    "sketch_portal",
    "translators",
]


def __dir__():
    return __all__
