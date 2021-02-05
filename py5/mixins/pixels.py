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
import threading
from pathlib import Path
from typing import overload, List, Union  # noqa

import numpy as np
from PIL import Image
import jpype


class PixelMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._instance = kwargs['instance']
        self._np_pixels = None

    def _replace_instance(self, new_instance):
        self._instance = new_instance
        super()._replace_instance(new_instance)

    def _init_np_pixels(self):
        width = self.pixel_width
        height = self.pixel_height
        self._py_bb = bytearray(width * height * 4)
        self._java_bb = jpype.nio.convertToDirectBuffer(self._py_bb)
        self._np_pixels = np.asarray(
            self._py_bb, dtype=np.uint8).reshape(
            height, width, 4)

    # *** BEGIN METHODS ***

    def load_np_pixels(self) -> None:
        """The documentation for this field or method has not yet been written.

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/."""
        if self._np_pixels is None:
            self._init_np_pixels()
        self._instance.loadPixels()
        self._java_bb.asIntBuffer().put(self._instance.pixels)

    def update_np_pixels(self) -> None:
        """The documentation for this field or method has not yet been written.

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/."""
        if self._np_pixels is None:
            self._init_np_pixels()
        self._java_bb.asIntBuffer().get(self._instance.pixels)
        self._instance.updatePixels()

    @property
    def np_pixels(self) -> np.ndarray:
        """The documentation for this field or method has not yet been written.

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/."""
        return self._np_pixels

    def set_np_pixels(self, array: np.ndarray, bands: str = 'ARGB') -> None:
        """The documentation for this field or method has not yet been written.

        Parameters
        ----------

        array: np.ndarray
            missing variable description

        bands: str = 'ARGB'
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/."""
        self.load_np_pixels()
        if bands == 'L':
            self._np_pixels[:, :, 0] = 255
            self._np_pixels[:, :, 1:] = array[:, :,
                                              None] if array.ndim == 2 else array
        elif bands == 'ARGB':
            self._np_pixels[:] = array
        elif bands == 'RGB':
            self._np_pixels[:, :, 0] = 255
            self._np_pixels[:, :, 1:] = array
        elif bands == 'RGBA':
            self._np_pixels[:, :, 0] = array[:, :, 3]
            self._np_pixels[:, :, 1:] = array[:, :, :3]
        self.update_np_pixels()

    def save(self,
             filename: Union[str,
                             Path],
             format: str = None,
             drop_alpha: bool = True,
             use_thread: bool = True,
             **params) -> None:
        """The documentation for this field or method has not yet been written.

        Parameters
        ----------

        drop_alpha: bool = True
            missing variable description

        filename: Union[str, Path]
            missing variable description

        format: str = None
            missing variable description

        params
            missing variable description

        use_thread: bool = True
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/."""
        filename = Path(str(self._instance.savePath(str(filename))))
        self.load_np_pixels()
        arr = self.np_pixels[:, :, 1:] if drop_alpha else np.roll(
            self.np_pixels, -1, axis=2)

        if use_thread:
            def _save(arr, filename, format, params):
                Image.fromarray(arr).save(filename, format=format, **params)

            t = threading.Thread(
                target=_save,
                args=(
                    arr,
                    filename,
                    format,
                    params),
                daemon=True)
            t.start()
        else:
            Image.fromarray(arr).save(filename, format=format, **params)
