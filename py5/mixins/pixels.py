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
        """new template no description.

        Notes
        -----

        new template no description.
"""
        if self._np_pixels is None:
            self._init_np_pixels()
        self._instance.loadPixels()
        self._java_bb.asIntBuffer().put(self._instance.pixels)

    def update_np_pixels(self) -> None:
        """new template no description.

        Notes
        -----

        new template no description.
"""
        if self._np_pixels is None:
            self._init_np_pixels()
        self._java_bb.asIntBuffer().get(self._instance.pixels)
        self._instance.updatePixels()

    @property
    def np_pixels(self) -> np.ndarray:
        """new template no description.

        Notes
        -----

        new template no description.
"""
        return self._np_pixels

    def set_np_pixels(self, array: np.ndarray, bands: str = 'ARGB') -> None:
        """new template no description.

        Parameters
        ----------

        array: np.ndarray
            missing variable description

        bands: str
            missing variable description

        Notes
        -----

        new template no description.
"""
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
             **params) -> None:
        """new template no description.

        Parameters
        ----------

        drop_alpha: bool
            missing variable description

        filename: Union[str, Path]
            missing variable description

        format: str
            missing variable description

        params
            missing variable description

        Notes
        -----

        new template no description.
"""
        filename = Path(str(self._instance.savePath(str(filename))))
        self.load_np_pixels()
        arr = self.np_pixels[:, :, 1:] if drop_alpha else np.roll(
            self.np_pixels, -1, axis=2)
        Image.fromarray(arr).save(filename, format=format, **params)
