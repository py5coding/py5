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
from __future__ import annotations

import sys
import functools
from typing import Callable

import numpy as np

import PIL
import PIL.ImageFile
from PIL import Image

from .sketch import Sketch


class RenderHelperSketch(Sketch):
    def __init__(
            self,
            setup,
            draw,
            width,
            height,
            renderer,
            *,
            limit=1,
            setup_args=None,
            setup_kwargs=None,
            draw_args=None,
            draw_kwargs=None):
        super().__init__()
        self._setup = setup
        self._draw = draw
        self._width = width
        self._height = height
        self._renderer = renderer
        self._limit = limit
        self._setup_args = setup_args or []
        self._setup_kwargs = setup_kwargs or {}
        self._draw_args = draw_args or []
        self._draw_kwargs = draw_kwargs or {}
        self.output = []

    def settings(self):
        self.size(self._width, self._height, self._renderer)

    def setup(self):
        if self._setup:
            self._setup(self, *self._setup_args, **self._setup_kwargs)

    def draw(self):
        self._draw(self, *self._draw_args, **self._draw_kwargs)
        self.load_np_pixels()
        self.output.append(Image.fromarray(self.np_pixels[:, :, 1:]))
        if self.frame_count == self._limit:
            self.exit_sketch()


class RenderHelperGraphicsCanvas(Sketch):
    def __init__(
            self,
            setup,
            draw,
            width,
            height,
            renderer,
            *,
            limit=1,
            setup_args=None,
            setup_kwargs=None,
            draw_args=None,
            draw_kwargs=None):
        super().__init__()
        self._setup = setup
        self._draw = draw
        self._width = width
        self._height = height
        self._renderer = renderer
        self._limit = limit
        self._setup_args = setup_args or []
        self._setup_kwargs = setup_kwargs or {}
        self._draw_args = draw_args or []
        self._draw_kwargs = draw_kwargs or {}
        self.output = []
        self._g = None

    def settings(self):
        self.size(100, 100, self._renderer)

    def setup(self):
        self.frame_rate(1000)  # performance boost :)
        self._g = self.create_graphics(
            self._width, self._height, self._renderer)
        # this begin/end draw pair is necessary when using the opengl renderers
        self._g.begin_draw()
        self._g.end_draw()

    def draw(self):
        self._g.begin_draw()
        if self.frame_count == 1 and self._setup:
            # call setup here so that _g can be drawn upon
            self._setup(self._g, *self._setup_args, **self._setup_kwargs)
        self._draw(self._g, *self._draw_args, **self._draw_kwargs)
        self._g.end_draw()
        self._g.load_np_pixels()
        g_pixels = np.dstack(
            (self._g.np_pixels[:, :, 1:], self._g.np_pixels[:, :, 0]))
        self.output.append(Image.fromarray(g_pixels))
        if self.frame_count >= self._limit:
            self.exit_sketch()


def _check_allowed_renderer(renderer):
    renderer_name = {
        Sketch.SVG: 'SVG',
        Sketch.PDF: 'PDF',
        Sketch.DXF: 'DXF',
        Sketch.P2D: 'P2D',
        Sketch.P3D: 'P3D'}.get(
        renderer,
        renderer)
    renderers = [
        Sketch.HIDDEN,
        Sketch.JAVA2D] if sys.platform == 'darwin' else [
        Sketch.HIDDEN,
        Sketch.JAVA2D,
        Sketch.P2D,
        Sketch.P3D]
    if renderer not in renderers:
        return f'Sorry, the render helper tools do not support the {renderer_name} renderer' + (
            ' on OSX.' if sys.platform == 'darwin' else '.')
    else:
        return None


def _osx_renderer_check(renderer):
    if sys.platform == 'darwin' and renderer == Sketch.JAVA2D:
        print('The render helper tools do not support the JAVA2D renderer on OSX. Switching to the default option instead.')
        return Sketch.HIDDEN
    else:
        return renderer


def render_frame(draw: Callable, width: int, height: int,
                 renderer: str = Sketch.HIDDEN, *,
                 draw_args: tuple = None, draw_kwargs: dict = None,
                 use_py5graphics=False) -> PIL.ImageFile.ImageFile:
    """Helper function to render a single frame using the passed ``draw`` function
    argument.

    Parameters
    ----------

    draw: Callable
        function that executes py5 draw commands

    draw_args: tuple = None
        additional positional arguments to pass to draw function

    draw_kwargs: dict = None
        additional keyword arguments to pass to draw function

    height: int
        height of the display window in units of pixels

    renderer: str = Sketch.HIDDEN
        rendering engine to use

    use_py5graphics: bool = False
        pass a py5graphics object instead of a sketch object

    width: int
        width of the display window in units of pixels

    Notes
    -----

    Helper function to render a single frame using the passed ``draw`` function
    argument. The output is returned as a ``PIL.Image`` object.

    The passed function's first parameter must be either a ``py5.Sketch`` object or
    a ``py5.Py5Graphics`` object, depending on the parameter ``use_py5graphics``.
    That object must be used for all of the function's py5 commands. The function
    can have additional positional and keyword arguments. To use them, pass the
    desired values as ``render_frame``'s ``draw_args`` and ``draw_kwargs``
    arguments.

    On OSX, only the default renderer is currently supported. Other platforms
    support the default renderer and the OpenGL renderers (P2D and P3D).

    The rendered frame can have transparent pixels if and only if the
    ``use_py5graphics`` parameter is ``True`` because only a ``py5.Py5Graphics``
    object can create an image with transparency. There is no need to call
    ``Py5Graphics.begin_draw()`` or ``Py5Graphics.end_draw()`` in the passed
    function as ``render_frame()`` does that for you.

    This function facilitates the creation and execution of a py5 Sketch, and as a
    result makes it easy to run a Sketch inside of another Sketch. This is
    discouraged, and may fail catastrophically.

    This function is available in decorator form as ``@render()``."""
    if msg := _check_allowed_renderer(renderer):
        print(msg, file=sys.stderr)
        return None
    renderer = _osx_renderer_check(renderer)

    HelperClass = RenderHelperGraphicsCanvas if use_py5graphics else RenderHelperSketch
    ahs = HelperClass(None, draw, width, height, renderer,
                      draw_args=draw_args, draw_kwargs=draw_kwargs)
    ahs.run_sketch(block=True)

    if not ahs.is_dead_from_error and ahs.output:
        return ahs.output[0]


def render_frame_sequence(draw: Callable,
                          width: int,
                          height: int,
                          renderer: str = Sketch.HIDDEN,
                          *,
                          limit: int = 1,
                          setup: Callable = None,
                          setup_args: tuple = None,
                          setup_kwargs: dict = None,
                          draw_args: tuple = None,
                          draw_kwargs: dict = None,
                          use_py5graphics=False) -> list[PIL.ImageFile.ImageFile]:
    """Helper function to render a sequence of frames using the passed ``draw``
    function argument.

    Parameters
    ----------

    draw: Callable
        function that executes py5 draw commands

    draw_args: tuple = None
        additional positional arguments to pass to draw function

    draw_kwargs: dict = None
        additional keyword arguments to pass to draw function

    height: int
        height of the display window in units of pixels

    limit: int = 1
        number of frames in the output sequence

    renderer: str = Sketch.HIDDEN
        rendering engine to use

    setup: Callable = None
        function that executes py5 setup commands

    setup_args: tuple = None
        additional positional arguments to pass to setup function

    setup_kwargs: dict = None
        additional keyword arguments to pass to setup function

    use_py5graphics: bool = False
        pass a py5graphics object instead of a sketch object

    width: int
        width of the display window in units of pixels

    Notes
    -----

    Helper function to render a sequence of frames using the passed ``draw``
    function argument. The output is returned as a list of ``PIL.Image`` objects.
    Use the ``limit`` keyword argument to specify the number of frames to return.

    The passed ``draw`` function's first parameter must be either a ``py5.Sketch``
    object or a ``py5.Py5Graphics`` object, depending on the parameter
    ``use_py5graphics``. That object must be used for all py5 commands. The function
    can have additional positional and keyword arguments. To use them, pass the
    desired values to ``render_frame_sequence``'s ``draw_args`` and ``draw_kwargs``
    arguments.

    On OSX, only the default renderer is currently supported. Other platforms
    support the default renderer and the OpenGL renderers (P2D and P3D).

    The rendered frames can have transparent pixels if and only if the
    ``use_py5graphics`` parameter is ``True`` because only a ``py5.Py5Graphics``
    object can create an image with transparency. If you need to clear the canvas
    between one frame and the next, use ``Py5Graphics.clear()``. There is no need to
    call ``Py5Graphics.begin_draw()`` or ``Py5Graphics.end_draw()`` in the passed
    ``draw`` function as ``render_frame_sequence()`` does that for you.

    Optionally the caller can pass a ``setup`` function, along with corresponding
    ``setup_args`` and ``setup_kwargs`` arguments. This will be called once, just
    like it would for any other py5 Sketch. The type of the first parameter must
    also depend on the ``use_py5graphics`` parameter.

    This function facilitates the creation and execution of a py5 Sketch, and as a
    result makes it easy to run a Sketch inside of another Sketch. This is
    discouraged, and may fail catastrophically.

    This function is available in decorator form as ``@render_sequence()``."""
    if msg := _check_allowed_renderer(renderer):
        print(msg, file=sys.stderr)
        return None
    renderer = _osx_renderer_check(renderer)

    HelperClass = RenderHelperGraphicsCanvas if use_py5graphics else RenderHelperSketch
    ahs = HelperClass(setup, draw, width, height, renderer, limit=limit,
                      setup_args=setup_args, setup_kwargs=setup_kwargs,
                      draw_args=draw_args, draw_kwargs=draw_kwargs)
    ahs.run_sketch(block=True)

    if not ahs.is_dead_from_error:
        return ahs.output


def render(width: int, height: int, renderer: str = Sketch.HIDDEN, *,
           use_py5graphics=False) -> PIL.ImageFile.ImageFile:
    """Decorator function to render a single frame using the decorated ``draw``
    function.

    Parameters
    ----------

    height: int
        height of the display window in units of pixels

    renderer: str = Sketch.HIDDEN
        rendering engine to use

    use_py5graphics: bool = False
        pass a py5graphics object instead of a sketch object

    width: int
        width of the display window in units of pixels

    Notes
    -----

    Decorator function to render a single frame using the decorated ``draw``
    function. The output is returned as a ``PIL.Image`` object.

    The decorated draw function's first parameter must be either a ``py5.Sketch``
    object or a ``py5.Py5Graphics`` object, depending on the parameter
    ``use_py5graphics``. That object must be used for all of the function's py5
    commands. The function can have additional positional and keyword arguments. To
    use them, pass the desired values when you call the decorated function as you
    would to any other Python function.

    On OSX, only the default renderer is currently supported. Other platforms
    support the default renderer and the OpenGL renderers (P2D and P3D).

    The rendered frame can have transparent pixels if and only if the
    ``use_py5graphics`` parameter is ``True`` because only a ``py5.Py5Graphics``
    object can create an image with transparency. There is no need to call
    ``Py5Graphics.begin_draw()`` or ``Py5Graphics.end_draw()`` in the decorated
    function as ``@render()`` does that for you.

    This function facilitates the creation and execution of a py5 Sketch, and as a
    result makes it easy to run a Sketch inside of another Sketch. This is
    discouraged, and may fail catastrophically.

    This function is available in non-decorator form as ``render_frame()``."""
    if msg := _check_allowed_renderer(renderer):
        raise RuntimeError(msg)
    renderer = _osx_renderer_check(renderer)

    def decorator(draw):
        @functools.wraps(draw)
        def run_render_frame(*draw_args, **draw_kwargs):
            return render_frame(draw, width, height, renderer,
                                draw_args=draw_args, draw_kwargs=draw_kwargs,
                                use_py5graphics=use_py5graphics)
        return run_render_frame
    return decorator


def render_sequence(width: int, height: int, renderer: str = Sketch.HIDDEN, *,
                    limit: int = 1, setup: Callable = None,
                    setup_args: tuple = None, setup_kwargs: dict = None,
                    use_py5graphics=False) -> list[PIL.ImageFile.ImageFile]:
    """Decorator function to render a sequence of frames using the decorated ``draw``
    function.

    Parameters
    ----------

    height: int
        height of the display window in units of pixels

    limit: int = 1
        number of frames in the output sequence

    renderer: str = Sketch.HIDDEN
        rendering engine to use

    setup: Callable = None
        optional setup function

    setup_args: tuple = None
        additional positional arguments to pass to setup function

    setup_kwargs: dict = None
        additional keyword arguments to pass to setup function

    use_py5graphics: bool = False
        pass a py5graphics object instead of a sketch object

    width: int
        width of the display window in units of pixels

    Notes
    -----

    Decorator function to render a sequence of frames using the decorated ``draw``
    function. The output is returned as a list of ``PIL.Image`` objects. Use the
    ``limit`` keyword argument to specify the number of frames to return.

    The decorated function's first parameter must be either a ``py5.Sketch`` object
    or a ``py5.Py5Graphics`` object, depending on the parameter ``use_py5graphics``.
    That object must be used for all py5 commands. The function can have additional
    positional and keyword arguments. To use them, pass the desired values when you
    call the decorated function as you would to any other Python function.

    Optionally, the caller can pass the decorator a ``setup`` function, along with
    corresponding ``setup_args`` and ``setup_kwargs`` arguments. This will be called
    once, just like it would for any other py5 Sketch. The type of the first
    parameter must also depend on the ``use_py5graphics`` parameter.

    On OSX, only the default renderer is currently supported. Other platforms
    support the default renderer and the OpenGL renderers (P2D and P3D).

    The rendered frames can have transparent pixels if and only if the
    ``use_py5graphics`` parameter is ``True`` because only a ``py5.Py5Graphics``
    object can create an image with transparency. If you need to clear the canvas
    between one frame and the next, use ``Py5Graphics.clear()``. There is no need to
    call ``Py5Graphics.begin_draw()`` or ``Py5Graphics.end_draw()`` in the decorated
    function as ``@render_sequence()`` does that for you.

    This function facilitates the creation and execution of a py5 Sketch, and as a
    result makes it easy to run a Sketch inside of another Sketch. This is
    discouraged, and may fail catastrophically.

    This function is available in non-decorator form as ``render_frame_sequence()``."""
    if msg := _check_allowed_renderer(renderer):
        raise RuntimeError(msg)
    renderer = _osx_renderer_check(renderer)

    def decorator(draw):
        @functools.wraps(draw)
        def run_render_frames(*draw_args, **draw_kwargs):
            return render_frame_sequence(
                draw,
                width,
                height,
                renderer,
                limit=limit,
                setup=setup,
                setup_args=setup_args,
                setup_kwargs=setup_kwargs,
                draw_args=draw_args,
                draw_kwargs=draw_kwargs,
                use_py5graphics=use_py5graphics)
        return run_render_frames
    return decorator
