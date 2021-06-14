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
import io

from ipykernel.zmqshell import ZMQInteractiveShell
import ipywidgets as widgets

import PIL

from .hooks import SketchPortalHook


Sketch = 'Sketch'


class Py5SketchPortal(widgets.Image):
    pass


def sketch_portal(
    *,
    time_limit: float = 0.0,
    throttle_frame_rate: float = None,
    scale: float = 1.0,
    quality: int = 75,
    portal_widget: Py5SketchPortal = None,
    sketch: Sketch = None,
        hook_post_draw: bool = False) -> None:
    """Creates a portal widget to continuously stream frames from a running Sketch into
    a Jupyter notebook.

    Parameters
    ----------

    hook_post_draw: bool = False
        attach hook to Sketch's post_draw method instead of draw

    portal_widget: Py5SketchPortal = None
        Py5SketchPortal object to send stream to

    quality: int = 75
        JPEG stream quality between 1 (worst) and 100 (best)

    scale: float = 1.0
        scale factor to adjust the height and width of the portal

    sketch: Sketch = None
        running Sketch

    throttle_frame_rate: float = None
        throttle portal frame rate below Sketch's frame rate

    time_limit: float = 0.0
        time limit in seconds for Sketch portal; set to 0 (default) for no limit

    Notes
    -----

    Creates a portal widget to continuously stream frames from a running Sketch into
    a Jupyter notebook. Each frame will appear embedded in the notebook, with each
    new frame replacing the previous frame.

    By default the Sketch will be the currently running Sketch, as returned by
    ``get_current_sketch()``. Use the ``sketch`` parameter to specify a different
    running Sketch, such as a Sketch created using Class mode.

    The Sketch Portal cannot (currently) handle keyboard or mouse events. As an
    alternative, consider using Jupyter Widgets for user input.

    This magic is intended to be used when a real display is not available, such as
    when using py5 through an online Jupyter notebook system such as binder. You are
    free to execute code elsewhere in the notebook while the Sketch is running and
    the portal is open. This function can only be used in a Jupyter Notebook. It
    uses ZMQ to stream JPEG images from the kernel to the client front-end.

    If you are using Jupyter Lab, try right clicking in the output area of the cell
    and selecting "Create New View for Output". This will create a new panel just
    for the Sketch portal. Creating a "New Console for Notebook" and creating a
    portal there works well also.

    This command can be called before ``run_sketch()`` if the current Sketch is in
    the ``is_ready`` state.

    Use the ``time_limit`` parameter to set a time limit (seconds). Use
    ``throttle_frame_rate`` to throttle the stream's frame rate (frames per second)
    to a slower pace than the Sketch's actual draw frame rate. The ``scale``
    parameter is a scaling factor that can adjust the portal height and width. The
    ``quality`` parameter sets the JPEG quality factor (default 75) for the stream,
    which must be between 1 (worst) and 100 (best). If the portal causes the
    Sketch's frame rate to drop, try adjusting the portal's throttle frame rate,
    quality, and scale.

    If your Sketch has a ``post_draw()`` method, use the ``hook_post_draw``
    parameter to make this function run after ``post_draw()`` instead of ``draw()``.
    This is important when using Processing libraries that support ``post_draw()``
    such as Camera3D or ColorBlindness.

    To stop a Sketch portal, wait for the time limit to expire or call
    ``exit_sketch()``. If you delete the cell with the ``Py5SketchPortal`` object,
    the portal will no longer be visible but the Sketch will still be streaming
    frames to the notebook client, wasting resources. A Sketch can only have one
    open portal, so opening a new portal with different options will replace an
    existing portal."""
    try:
        __IPYTHON__  # type: ignore
        in_ipython_session = True
        in_jupyter_zmq_shell = isinstance(
            get_ipython(), ZMQInteractiveShell)  # type: ignore
    except NameError:
        in_ipython_session = False
        in_jupyter_zmq_shell = False

    if not in_ipython_session:
        raise RuntimeError(
            'The sketch_widget() function can only be used with IPython and ZMQInteractiveShell (such as Jupyter Lab)')
    if not in_jupyter_zmq_shell:
        raise RuntimeError(
            'The sketch_widget() function can only be used with ZMQInteractiveShell (such as Jupyter Lab)')

    if sketch is None:
        import py5
        sketch = py5.get_current_sketch()
        prefix = ' current'
    else:
        prefix = ''

    if not sketch.is_running:
        raise RuntimeError(f'The {prefix} sketch is not running')
    if throttle_frame_rate is not None and throttle_frame_rate <= 0:
        raise RuntimeError(
            'The throttle_frame_rate parameter must be None or greater than zero')
    if time_limit < 0:
        raise RuntimeError(
            'The time_limit parameter must be greater than or equal to zero')
    if quality < 1 or quality > 100:
        raise RuntimeError(
            'The quality parameter must be between 1 (worst) and 100 (best)')
    if scale <= 0:
        raise RuntimeError('The scale parameter must be greater than zero')

    if portal_widget is None:
        portal_widget = Py5SketchPortal()
        portal_widget.layout.width = f'{sketch.width}px'
        portal_widget.layout.height = f'{sketch.height}px'
        portal_widget.layout.border = '1px solid gray'

    def displayer(frame):
        img = PIL.Image.fromarray(frame)
        if scale != 1.0:
            img = img.resize(tuple(int(scale * x) for x in img.size))
        b = io.BytesIO()
        img.save(b, format='JPEG', quality=quality)
        portal_widget.value = b.getvalue()

    hook = SketchPortalHook(displayer, throttle_frame_rate, time_limit)

    sketch._add_post_hook(
        'post_draw' if hook_post_draw else 'draw',
        hook.hook_name,
        hook)

    return portal_widget
