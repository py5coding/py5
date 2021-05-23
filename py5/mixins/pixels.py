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


_Sketch = jpype.JClass('py5.core.Sketch')


class PixelMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._instance = kwargs['instance']
        self._np_pixels = None

    def _replace_instance(self, new_instance):
        self._instance = new_instance
        super()._replace_instance(new_instance)

    def _init_np_pixels(self):
        width = self.pixel_width if hasattr(
            self, 'pixel_width') else self.width
        height = self.pixel_height if hasattr(
            self, 'pixel_height') else self.height
        self._py_bb = bytearray(width * height * 4)
        self._java_bb = jpype.nio.convertToDirectBuffer(self._py_bb)
        self._np_pixels = np.asarray(
            self._py_bb, dtype=np.uint8).reshape(
            height, width, 4)

    # *** BEGIN METHODS ***

    def load_np_pixels(self) -> None:
        """Loads the pixel data of the current display window into the ``np_pixels[]``
        array.

        Notes
        -----

        Loads the pixel data of the current display window into the ``np_pixels[]``
        array. This method must always be called before reading from or writing to
        ``np_pixels[]``. Subsequent changes to the display window will not be reflected
        in ``np_pixels[]`` until ``load_np_pixels()`` is called again.

        The ``load_np_pixels()`` method is similar to ``load_pixels()`` in that
        ``load_np_pixels()`` must be called before reading from or writing to
        ``np_pixels[]`` just as ``load_pixels()`` must be called before reading from or
        writing to ``pixels[]``.

        Note that ``load_np_pixels()`` will as a side effect call ``load_pixels()``, so
        if your code needs to read ``np_pixels[]`` and ``pixels[]`` simultaneously,
        there is no need for a separate call to ``load_pixels()``. However, be aware
        that modifying both ``np_pixels[]`` and ``pixels[]`` simultaneously will likely
        result in the updates to ``pixels[]`` being discarded."""
        if self._np_pixels is None:
            self._init_np_pixels()
        self._instance.loadPixels()
        self._java_bb.asIntBuffer().put(self._instance.pixels)

    def update_np_pixels(self) -> None:
        """Updates the display window with the data in the ``np_pixels[]`` array.

        Notes
        -----

        Updates the display window with the data in the ``np_pixels[]`` array. Use in
        conjunction with ``load_np_pixels()``. If you're only reading pixels from the
        array, there's no need to call ``update_np_pixels()`` — updating is only
        necessary to apply changes.

        The ``update_np_pixels()`` method is similar to ``update_pixels()`` in that
        ``update_np_pixels()`` must be called after modifying ``np_pixels[]`` just as
        ``update_pixels()`` must be called after modifying ``pixels[]``."""
        if self._np_pixels is None:
            self._init_np_pixels()
        self._java_bb.asIntBuffer().get(self._instance.pixels)
        self._instance.updatePixels()

    def _get_np_pixels(self) -> np.ndarray:
        """The ``np_pixels[]`` array contains the values for all the pixels in the display
        window.

        Notes
        -----

        The ``np_pixels[]`` array contains the values for all the pixels in the display
        window. Unlike the one dimensional array ``pixels[]``, the ``np_pixels[]`` array
        organizes the color data in a 3 dimensional numpy array. The size of the array's
        dimensions are defined by the size of the display window. The first dimension is
        the height, the second is the width, and the third represents the color
        channels. The color channels are ordered alpha, red, green, blue (ARGB). Every
        value in ``np_pixels[]`` is an integer between 0 and 255.

        This numpy array is very similar to the image arrays used by other popular
        Python image libraries, but note that some of them like opencv will by default
        order the color channels as RGBA.

        When the pixel density is set to higher than 1 with the ``pixel_density()``
        function, the size of ``np_pixels[]``'s height and width dimensions will change.
        See the reference for ``pixel_width`` or ``pixel_height`` for more information.
        Nothing about ``np_pixels[]`` will change as a result of calls to
        ``color_mode()``.

        Much like the ``pixels[]`` array, there are load and update methods that must be
        called before and after making changes to the data in ``np_pixels[]``. Before
        accessing ``np_pixels[]``, the data must be loaded with the ``load_np_pixels()``
        method. If this is not done, ``np_pixels`` will be equal to ``None`` and your
        code will likely result in Python exceptions. After ``np_pixels[]`` has been
        modified, the ``update_np_pixels()`` method must be called to update the content
        of the display window.

        To set the entire contents of ``np_pixels[]`` to the contents of another
        properly sized numpy array, consider using ``set_np_pixels()``."""
        return self._np_pixels
    np_pixels: np.ndarray = property(fget=_get_np_pixels)

    def set_np_pixels(self, array: np.ndarray, bands: str = 'ARGB') -> None:
        """Set the entire contents of ``np_pixels[]`` to the contents of another properly
        sized and typed numpy array.

        Parameters
        ----------

        array: np.ndarray
            properly sized numpy array to be copied to np_pixels[]

        bands: str = 'ARGB'
            color channels in the array's third dimension

        Notes
        -----

        Set the entire contents of ``np_pixels[]`` to the contents of another properly
        sized and typed numpy array. The size of ``array``'s first and second dimensions
        must match the height and width of the Sketch window, respectively. The array's
        ``dtype`` must be ``np.uint8``.

        The ``bands`` parameter is used to interpret the ``array``'s color channel
        dimension (the array's third dimension). It can be one of ``'L'`` (single-
        channel grayscale), ``'ARGB'``, ``'RGB'``, or ``'RGBA'``. If there is no alpha
        channel, ``array`` is assumed to have no transparency, but recall that the
        display window's pixels can never be transparent so any transparency in
        ``array`` will have no effect. If the ``bands`` parameter is ``'L'``,
        ``array``'s third dimension is optional.

        This method makes its own calls to ``load_np_pixels()`` and
        ``update_np_pixels()`` so there is no need to call either explicitly.

        This method exists because setting the array contents with the code
        ``py5.np_pixels = array`` will cause an error, while the correct syntax,
        ``py5.np_pixels[:] = array``, might also be unintuitive for beginners."""
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
             *,
             format: str = None,
             drop_alpha: bool = True,
             use_thread: bool = True,
             **params) -> None:
        """Save image data to a file.

        Parameters
        ----------

        drop_alpha: bool = True
            remove the alpha channel when saving the image

        filename: Union[str, Path]
            output filename

        format: str = None
            image format, if not determined from filename extension

        params
            keyword arguments to pass to the PIL.Image save method

        use_thread: bool = True
            write file in separate thread

        Notes
        -----

        Save image data to a file. This method uses the Python library Pillow to write
        the image, so it can save images in any format that that library supports.

        Use the ``drop_alpha`` parameter to drop the alpha channel from the image. This
        defaults to ``True``. Some image formats such as JPG do not support alpha
        channels, and Pillow will throw an error if you try to save an image with the
        alpha channel in that format.

        The ``use_thread`` parameter will save the image in a separate Python thread.
        This improves performance by returning before the image has actually been
        written to the file."""
        sketch_instance = self._instance if isinstance(
            self._instance, _Sketch) else self._instance.parent
        filename = Path(str(sketch_instance.savePath(str(filename))))
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
