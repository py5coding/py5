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
from pathlib import Path


_DRAW_WRAPPER_CODE_TEMPLATE = """
if _PY5_HAS_DRAW_:
    draw_ = draw

def draw():
    if _PY5_HAS_DRAW_:
        draw_()

    if _PY5_SAVE_FRAME_:
        py5.save_frame("{0}", use_thread=False)
    py5.exit_sketch()
"""


_RUN_SKETCH_CODE = """
if py5.is_ready:
    py5.run_sketch(block=True)
if py5.is_dead_from_error:
    py5.exit_sketch()
"""

_EXIT_SKETCH = """
import time
time.sleep(1)
py5.exit_sketch()
time.sleep(1)
"""


def run_code(code: str, image: Path) -> bool:
    import py5
    ns = dict(py5=py5)

    exec("py5.reset_py5()", ns)
    exec(code, ns)
    ns['_PY5_HAS_DRAW_'] = 'draw' in ns
    ns['_PY5_SAVE_FRAME_'] = image is not None

    if code.find("py5.run_sketch") >= 0:
        exec(_EXIT_SKETCH, ns)
    else:
        exec(_DRAW_WRAPPER_CODE_TEMPLATE.format(image), ns)
        exec(_RUN_SKETCH_CODE, ns)

    return not py5.is_dead_from_error
