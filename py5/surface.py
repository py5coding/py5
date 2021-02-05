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
    """The documentation for this field or method has not yet been written.

    Underlying Java class: PSurface.PSurface

    Notes
    -----

    The documentation for this field or method has not yet been written. If you know
    what it does, please help out with a pull request to the relevant file in
    https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
    """

    def __init__(self, psurface, pimage_cache):
        self._instance = psurface
        self._pimage_cache = pimage_cache

    def get_native(self) -> Any:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PSurface.getNative

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.getNative()

    def is_stopped(self) -> bool:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PSurface.isStopped

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.isStopped()

    def open_link(self, url: str, /) -> bool:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PSurface.openLink

        Parameters
        ----------

        url: str
            the link to open

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.openLink(url)

    def pause_thread(self) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PSurface.pauseThread

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.pauseThread()

    def resume_thread(self) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PSurface.resumeThread

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.resumeThread()

    def set_always_on_top(self, always: bool, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PSurface.setAlwaysOnTop

        Parameters
        ----------

        always: bool
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.setAlwaysOnTop(always)

    def set_icon(self, icon: Py5Image, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PSurface.setIcon

        Parameters
        ----------

        icon: Py5Image
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.setIcon(icon)

    def set_location(self, x: int, y: int, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PSurface.setLocation

        Parameters
        ----------

        x: int
            missing variable description

        y: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.setLocation(x, y)

    def set_resizable(self, resizable: bool, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PSurface.setResizable

        Parameters
        ----------

        resizable: bool
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.setResizable(resizable)

    def set_size(self, width: int, height: int, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PSurface.setSize

        Parameters
        ----------

        height: int
            missing variable description

        width: int
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.setSize(width, height)

    def set_title(self, title: str, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PSurface.setTitle

        Parameters
        ----------

        title: str
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.setTitle(title)

    def set_visible(self, visible: bool, /) -> None:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PSurface.setVisible

        Parameters
        ----------

        visible: bool
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.setVisible(visible)

    def stop_thread(self) -> bool:
        """The documentation for this field or method has not yet been written.

        Underlying Java method: PSurface.stopThread

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/.
        """
        return self._instance.stopThread()
