import functools
from typing import Union, Callable, Tuple, Dict, List, NewType

import PIL
from PIL import Image

from .sketch import Sketch


PIL_Image = NewType('PIL_Image', PIL.Image)


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
        if renderer not in [
                Sketch.HIDDEN,
                Sketch.JAVA2D,
                Sketch.P2D,
                Sketch.P3D]:
            raise RuntimeError(
                f'Processing Renderer {renderer} not yet supported')
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


def render_frame(draw: Callable, width: int, height: int,
                 renderer: str = Sketch.HIDDEN, *,
                 draw_args: Tuple = None, draw_kwargs: Dict = None) -> Image:
    """Helper function to render a single frame using the passed ``draw`` function
    argument.

    Parameters
    ----------

    draw: Callable
        function that executes py5 draw commands

    draw_args: Tuple = None
        additional positional arguments to pass to draw function

    draw_kwargs: Dict = None
        additional keyword arguments to pass to draw function

    height: int
        height of the display window in units of pixels

    renderer: str = Sketch.HIDDEN
        rendering engine to use

    width: int
        width of the display window in units of pixels

    Notes
    -----

    Helper function to render a single frame using the passed ``draw`` function
    argument. The output is returned as a ``PIL.Image`` object.

    The passed function's first parameter must be a ``py5.Sketch`` object, and that
    object must be used for all of the function's py5 commands. The function can
    have additional positional and keyword arguments. To use them, pass the desired
    values as ``render_frame``'s ``draw_args`` and ``draw_kwargs`` arguments.

    Currently, only the default and OpenGL renderers are supported.

    This function facilitates the creation and execution of a py5 Sketch, and as a
    result makes it easy to run a Sketch inside of another Sketch. This is
    discouraged, and may fail catastrophically.

    This function is available in decorator form as :doc:`render`."""
    ahs = RenderHelperSketch(None, draw, width, height, renderer,
                             draw_args=draw_args, draw_kwargs=draw_kwargs)
    ahs.run_sketch(block=True)

    if not ahs.is_dead_from_error and ahs.output:
        return ahs.output[0]


def render_frame_sequence(
        draw: Callable,
        width: int,
        height: int,
        renderer: str = Sketch.HIDDEN,
        *,
        limit: int = 1,
        setup: Callable = None,
        setup_args: Tuple = None,
        setup_kwargs: Dict = None,
        draw_args: Tuple = None,
        draw_kwargs: Dict = None) -> List[PIL_Image]:
    """Helper function to render a sequence of frames using the passed ``draw``
    function argument.

    Parameters
    ----------

    draw: Callable
        function that executes py5 draw commands

    draw_args: Tuple = None
        additional positional arguments to pass to draw function

    draw_kwargs: Dict = None
        additional keyword arguments to pass to draw function

    height: int
        height of the display window in units of pixels

    limit: int = 1
        number of frames in the output sequence

    renderer: str = Sketch.HIDDEN
        rendering engine to use

    setup: Callable = None
        function that executes py5 setup commands

    setup_args: Tuple = None
        additional positional arguments to pass to setup function

    setup_kwargs: Dict = None
        additional keyword arguments to pass to setup function

    width: int
        width of the display window in units of pixels

    Notes
    -----

    Helper function to render a sequence of frames using the passed ``draw``
    function argument. The output is returned as a list of ``PIL.Image`` objects.
    Use the ``limit`` keyword argument to specify the number of frames to return.

    The passed function's first parameter must be a ``py5.Sketch`` object, and that
    object must be used for all of the function's py5 commands. The function can
    have additional positional and keyword arguments. To use them, pass the desired
    values to ``render_frame_sequence``'s ``draw_args`` and ``draw_kwargs``
    arguments.

    Optionally, the caller can pass a ``setup`` function, along with corresponding
    ``setup_args`` and ``setup_kwargs`` arguments. This will be called once, just
    like it would for any other py5 sketch. As with the passed ``draw`` function,
    the first parameter must be a ``py5.Sketch`` object.

    Currently, only the default and OpenGL renderers are supported.

    This function facilitates the creation and execution of a py5 Sketch, and as a
    result makes it easy to run a Sketch inside of another Sketch. This is
    discouraged, and may fail catastrophically.

    This function is available in decorator form as :doc:`render_sequence`."""
    ahs = RenderHelperSketch(setup, draw, width, height, renderer, limit=limit,
                             setup_args=setup_args, setup_kwargs=setup_kwargs,
                             draw_args=draw_args, draw_kwargs=draw_kwargs)
    ahs.run_sketch(block=True)

    if not ahs.is_dead_from_error:
        return ahs.output


def render(width: int, height: int, renderer: str = Sketch.HIDDEN) -> Image:
    """Decorator function to render a single frame using the decorated ``draw``
    function.

    Parameters
    ----------

    height: int
        height of the display window in units of pixels

    renderer: str = Sketch.HIDDEN
        rendering engine to use

    width: int
        width of the display window in units of pixels

    Notes
    -----

    Decorator function to render a single frame using the decorated ``draw``
    function. The output is returned as a ``PIL.Image`` object.

    The decorated draw function's first parameter must be a ``py5.Sketch`` object,
    and that object must be used for all of the function's py5 commands. The
    function can have additional positional and keyword arguments. To use them, pass
    the desired values when you call the decorated function as you would to any
    other Python function.

    Currently, only the default and OpenGL renderers are supported.

    This function facilitates the creation and execution of a py5 Sketch, and as a
    result makes it easy to run a Sketch inside of another Sketch. This is
    discouraged, and may fail catastrophically.

    This function is available in non-decorator form as :doc:`render_frame`."""
    def decorator(draw):
        @functools.wraps(draw)
        def run_render_frame(*draw_args, **draw_kwargs):
            return render_frame(draw, width, height, renderer,
                                draw_args=draw_args, draw_kwargs=draw_kwargs)
        return run_render_frame
    return decorator


def render_sequence(
        width: int,
        height: int,
        renderer: str = Sketch.HIDDEN,
        *,
        limit: int = 1,
        setup: Callable = None,
        setup_args: Tuple = None,
        setup_kwargs: Dict = None) -> List[PIL_Image]:
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
        missing variable description

    setup_args: Tuple = None
        additional positional arguments to pass to setup function

    setup_kwargs: Dict = None
        additional keyword arguments to pass to setup function

    width: int
        width of the display window in units of pixels

    Notes
    -----

    Decorator function to render a sequence of frames using the decorated ``draw``
    function. The output is returned as a list of ``PIL.Image`` objects. Use the
    ``limit`` keyword argument to specify the number of frames to return.

    The decorated function's first parameter must be a ``py5.Sketch`` object, and
    that object must be used for all of the function's py5 commands. The function
    can have additional positional and keyword arguments. To use them, pass the
    desired values when you call the decorated function as you would to any other
    Python function.

    Optionally, the caller can pass the decorator a ``setup`` function, along with
    corresponding ``setup_args`` and ``setup_kwargs`` arguments. This will be called
    once, just like it would for any other py5 sketch. As with the passed ``draw``
    function, the first parameter must be a ``py5.Sketch`` object.

    Currently, only the default and OpenGL renderers are supported.

    This function facilitates the creation and execution of a py5 Sketch, and as a
    result makes it easy to run a Sketch inside of another Sketch. This is
    discouraged, and may fail catastrophically.

    This function is available in non-decorator form as
    :doc:`render_frame_sequence`."""
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
                draw_kwargs=draw_kwargs)
        return run_render_frames
    return decorator
