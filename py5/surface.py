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
import functools
from typing import overload, Any  # noqa

from .image import Py5Image  # noqa


def _return_py5surface(f):
    @functools.wraps(f)
    def decorated(self_, *args):
        return Py5Surface(
            f(self_, *args), getattr(self_, '_pimage_cache', None))
    return decorated


class Py5Surface:
    """The Py5Surface object is the actual window py5 draws animations to.

    Underlying Java class: PSurface.PSurface

    Notes
    -----

    The Py5Surface object is the actual window py5 draws animations to. You can use
    this to interact with the window and change some of its characteristics, such as
    the window title or location.
    """

    def __init__(self, psurface, pimage_cache):
        self._instance = psurface
        self._pimage_cache = pimage_cache

    def get_native(self) -> Any:
        """Get the Sketch's Java native window object.

        Underlying Java method: PSurface.getNative

        Notes
        -----

        Get the Sketch's Java native window object. Here there be dragons! The returned
        object will be a Java object you can interact with through py5's Python-Java
        bridge, jpype. The type of the native window will depend on your operating
        system and the Sketch's renderer, and is subject to change in future releases of
        Processing.

        This method may be useful to you if you research the Java libraries Processing
        uses to display animations. Any errors will result in Java Exceptions.
        """
        return self._instance.getNative()

    def is_stopped(self) -> bool:
        """Determine if the surface is currently running an animation.

        Underlying Java method: PSurface.isStopped

        Notes
        -----

        Determine if the surface is currently running an animation. A Sketch that has
        called ``no_loop()`` or has no ``draw()`` function is not animating, and will
        result in this method returning ``True``. If there is a ``draw()`` function and
        ``no_loop()`` has not been called, this will return ``False``. Calling
        Py5Surface's ``Py5Surface.stop_thread()`` will make all future calls to
        ``is_stopped()`` return ``True``.

        The output of this method is independent of ``Py5Surface.pause_thread()`` and
        ``Py5Surface.resume_thread()``.
        """
        return self._instance.isStopped()

    def pause_thread(self) -> None:
        """Pause a running Sketch.

        Underlying Java method: PSurface.pauseThread

        Notes
        -----

        Pause a running Sketch. The Sketch window will be static and unresponsive. You
        can resume the Sketch with ``Py5Surface.resume_thread()``.

        The ``frame_count`` will not increment while the Sketch is paused.

        Pausing a Sketch is not the same as stopping a Sketch, so this method will not
        change the results of ``Py5Surface.is_stopped()``.
        """
        return self._instance.pauseThread()

    def resume_thread(self) -> None:
        """Resume a paused Sketch.

        Underlying Java method: PSurface.resumeThread

        Notes
        -----

        Resume a paused Sketch. The Sketch window will resume operating as it did before
        ``Py5Surface.pause_thread()`` was called.

        The ``frame_count`` will continue incrementing after the Sketch is resumed.
        """
        return self._instance.resumeThread()

    def set_always_on_top(self, always: bool, /) -> None:
        """Set the Sketch window to always be on top of other windows.

        Underlying Java method: PSurface.setAlwaysOnTop

        Parameters
        ----------

        always: bool
            should the Sketch window always be on top of other windows

        Notes
        -----

        Set the Sketch window to always be on top of other windows. By default, the
        Sketch window can be covered by other windows. Setting this to ``True`` will
        keep that from happening.
        """
        return self._instance.setAlwaysOnTop(always)

    def set_icon(self, icon: Py5Image, /) -> None:
        """Set the Sketch window icon.

        Underlying Java method: PSurface.setIcon

        Parameters
        ----------

        icon: Py5Image
            image to use as the window icon

        Notes
        -----

        Set the Sketch window icon. This will typically appear in the window's title
        bar. The default window icon is the same as Processing's.

        This method will not work for the ``P2D`` or ``P3D`` renderers. Setting the icon
        for those renderers is a bit tricky; see the second example to learn how to do
        that.
        """
        return self._instance.setIcon(icon)

    def set_location(self, x: int, y: int, /) -> None:
        """Set the Sketch's window location.

        Underlying Java method: PSurface.setLocation

        Parameters
        ----------

        x: int
            x-coordinate for window location

        y: int
            y-coordinate for window location

        Notes
        -----

        Set the Sketch's window location. Calling this repeatedly from the ``draw()``
        function may result in a sluggish Sketch. Negative or invalid coordinates are
        ignored. To hide a Sketch window, use ``Py5Surface.set_visible()``.
        """
        return self._instance.setLocation(x, y)

    def set_resizable(self, resizable: bool, /) -> None:
        """Set the Sketch window as resizable by the user.

        Underlying Java method: PSurface.setResizable

        Parameters
        ----------

        resizable: bool
            should the Sketch window be resizable

        Notes
        -----

        Set the Sketch window as resizable by the user. The user will be able to resize
        the window in the same way as they do for many other windows on their computer.
        By default, the Sketch window is not resizable.

        Changing the window size will clear the drawing canvas. If your Sketch uses
        this, the ``width`` and ``height`` variables will change.
        """
        return self._instance.setResizable(resizable)

    def set_size(self, width: int, height: int, /) -> None:
        """Set a new width and height for the Sketch window.

        Underlying Java method: PSurface.setSize

        Parameters
        ----------

        height: int
            new window height

        width: int
            new window width

        Notes
        -----

        Set a new width and height for the Sketch window. You do not need to call
        ``Py5Surface.set_resizable()`` before calling this.

        Changing the window size will clear the drawing canvas. If your Sketch uses
        this, the ``width`` and ``height`` variables will change.
        """
        return self._instance.setSize(width, height)

    def set_title(self, title: str, /) -> None:
        """Set the Sketch window's title.

        Underlying Java method: PSurface.setTitle

        Parameters
        ----------

        title: str
            new window title

        Notes
        -----

        Set the Sketch window's title. This will typically appear at the window's title
        bar. The default window title is "Sketch".
        """
        return self._instance.setTitle(title)

    def set_visible(self, visible: bool, /) -> None:
        """Set the Sketch window's visiblity.

        Underlying Java method: PSurface.setVisible

        Parameters
        ----------

        visible: bool
            desired surface visiblity

        Notes
        -----

        Set the Sketch window's visiblity. The animation will continue to run but the
        window will not be visible.
        """
        return self._instance.setVisible(visible)

    def stop_thread(self) -> bool:
        """Stop the animation thread.

        Underlying Java method: PSurface.stopThread

        Notes
        -----

        Stop the animation thread. The Sketch window will remain open but will be static
        and unresponsive. Use ``Py5Surface.is_stopped()`` to determine if a Sketch has
        been stopped or not.

        This method is different from ``Py5Surface.pause_thread()`` in that it will
        irreversably stop the animation. Use ``Py5Surface.pause_thread()`` and
        ``Py5Surface.resume_thread()`` if you want to pause and resume a running Sketch.
        """
        return self._instance.stopThread()
