# -*- coding: utf-8 -*-
# *** FORMAT PARAMS ***
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

    def __init__(self, psurface, pimage_cache):
        self._instance = psurface
        self._pimage_cache = pimage_cache

    def get_native(self) -> Any:
        """new template no description.

        Notes
        -----

        new template no description.
"""
        return self._instance.getNative()

    def is_stopped(self) -> bool:
        """new template no description.

        Notes
        -----

        new template no description.
"""
        return self._instance.isStopped()

    def open_link(self, url: str, /) -> bool:
        """new template no description.

        Parameters
        ----------

        url: str
            the link to open

        Notes
        -----

        new template no description.
"""
        return self._instance.openLink(url)

    def pause_thread(self) -> None:
        """new template no description.

        Notes
        -----

        new template no description.
"""
        return self._instance.pauseThread()

    def resume_thread(self) -> None:
        """new template no description.

        Notes
        -----

        new template no description.
"""
        return self._instance.resumeThread()

    def set_always_on_top(self, always: bool, /) -> None:
        """new template no description.

        Parameters
        ----------

        always: bool
            missing variable description

        Notes
        -----

        new template no description.
"""
        return self._instance.setAlwaysOnTop(always)

    def set_icon(self, icon: Py5Image, /) -> None:
        """new template no description.

        Parameters
        ----------

        icon: Py5Image
            missing variable description

        Notes
        -----

        new template no description.
"""
        return self._instance.setIcon(icon)

    def set_location(self, x: int, y: int, /) -> None:
        """new template no description.

        Parameters
        ----------

        x: int
            missing variable description

        y: int
            missing variable description

        Notes
        -----

        new template no description.
"""
        return self._instance.setLocation(x, y)

    def set_resizable(self, resizable: bool, /) -> None:
        """new template no description.

        Parameters
        ----------

        resizable: bool
            missing variable description

        Notes
        -----

        new template no description.
"""
        return self._instance.setResizable(resizable)

    def set_size(self, width: int, height: int, /) -> None:
        """new template no description.

        Parameters
        ----------

        height: int
            missing variable description

        width: int
            missing variable description

        Notes
        -----

        new template no description.
"""
        return self._instance.setSize(width, height)

    def set_title(self, title: str, /) -> None:
        """new template no description.

        Parameters
        ----------

        title: str
            missing variable description

        Notes
        -----

        new template no description.
"""
        return self._instance.setTitle(title)

    def set_visible(self, visible: bool, /) -> None:
        """new template no description.

        Parameters
        ----------

        visible: bool
            missing variable description

        Notes
        -----

        new template no description.
"""
        return self._instance.setVisible(visible)

    def stop_thread(self) -> bool:
        """new template no description.

        Notes
        -----

        new template no description.
"""
        return self._instance.stopThread()
