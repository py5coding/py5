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


_DRAW_WRAPPER_CODE_TEMPLATE = """
if {1}:
    draw_ = draw

def draw():
    if {1}:
        draw_()

    if {2}:
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

    code = 'py5.reset_py5()\n\n' + code + '\n\n'

    if code.find("py5.run_sketch") >= 0:
        code += _EXIT_SKETCH
    else:
        code += _DRAW_WRAPPER_CODE_TEMPLATE.format(image,
                                                   code.find("def draw():") >= 0,
                                                   image is not None) + '\n\n' + _RUN_SKETCH_CODE

    # writing code to file so inspect.getsource() works correctly
    with open('/tmp/test_file.py', 'w') as f:
        f.write(code)

    exec(compile(code, filename='/tmp/test_file.py', mode="exec"), ns)

    return not py5.is_dead_from_error
