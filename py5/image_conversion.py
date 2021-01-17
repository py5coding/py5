import io
from pathlib import Path
import uuid
import tempfile
from dataclasses import dataclass

import numpy as np
from PIL import Image


pimage_functions = []

_TEMP_DIR = tempfile.TemporaryDirectory()


def _convert(obj):
    for precondition, convert_function in pimage_functions:
        if precondition(obj):
            obj = convert_function(obj)
            break
    else:
        raise RuntimeError(f'Py5 Converter is not able to convert {str(obj)}')

    return obj


def register_image_conversion(precondition, convert_function):
    pimage_functions.append((precondition, convert_function))


###############################################################################
# BUILT-IN CONVERSTION FUNCTIONS
###############################################################################


@dataclass
class NumpyImageArray:
    array: np.ndarray
    bands: str = 'ARGB'

    def __post_init__(self):
        if not isinstance(self.array, np.ndarray):
            raise RuntimeError("array parameter must be a numpy array")
        if not self.array.dtype == np.uint8:
            raise RuntimeError("array parameter must have uint8 dtype")
        if not isinstance(self.bands, str):
            raise RuntimeError("bands parameter must be a string")
        if self.bands in ['RGBA', 'ARGB', 'RGB']:
            if self.array.ndim != 3:
                raise RuntimeError(
                    f"array parameter must have 3 dimensions for '{self.bands}' image arrays")
            if self.array.shape[2] != len(self.bands):
                raise RuntimeError(
                    "third dimension of array parameter equal the length of the bands parameter")
        elif self.bands == 'L':
            if not (
                self.array.ndim == 2 or (
                    self.array.ndim == 3 and self.array.shape[2] == 1)):
                raise RuntimeError(
                    "for 'L' image arrays, array must have 2 dimensions or a 3rd dimension of size 1")
        else:
            raise RuntimeError(
                "bands parameter must be one of 'RGBA', 'ARGB', 'RGB', or 'L'")


def pillow_image_to_ndarray_precondition(obj):
    return isinstance(obj, Image.Image)


def pillow_image_to_ndarray_converter(img):
    if img.mode not in ['RGB', 'RGBA']:
        img = img.convert(mode='RGB')
    return NumpyImageArray(np.asarray(img), img.mode)


register_image_conversion(
    pillow_image_to_ndarray_precondition,
    pillow_image_to_ndarray_converter)


###############################################################################
# Py5 requires Pillow and numpy to be installed. The below libraries may or may
# not be installed. If they are, this registers their associated conversion
# functions.
###############################################################################


try:
    import cairosvg  # noqa
    import cairocffi  # noqa

    def svg_file_to_ndarray_precondition(obj):
        if isinstance(obj, (str, Path)):
            return Path(obj).suffix.lower() == '.svg'
        else:
            return False

    def svg_file_to_ndarray_converter(filename):
        filename = Path(filename)
        with open(filename, 'r') as f:
            img = Image.open(io.BytesIO(cairosvg.svg2png(file_obj=f)))
            return pillow_image_to_ndarray_converter(img)

    register_image_conversion(
        svg_file_to_ndarray_precondition,
        svg_file_to_ndarray_converter)
except ModuleNotFoundError:
    pass


try:
    import cairocffi  # noqa

    def cairocffi_surface_to_tempfile_precondition(obj):
        return isinstance(obj, cairocffi.Surface)

    def cairocffi_surface_to_tempfile_converter(surface):
        temp_png = Path(_TEMP_DIR.name) / f'{uuid.uuid4()}.png'
        surface.write_to_png(temp_png.as_posix())
        return temp_png

    register_image_conversion(
        cairocffi_surface_to_tempfile_precondition,
        cairocffi_surface_to_tempfile_converter)
except ModuleNotFoundError:
    pass


try:
    import cairo  # noqa

    def cairo_surface_to_tempfile_precondition(obj):
        return isinstance(obj, cairo.Surface)

    def cairo_surface_to_tempfile_converter(surface):
        temp_png = Path(_TEMP_DIR.name) / f'{uuid.uuid4()}.png'
        surface.write_to_png(temp_png.as_posix())
        return temp_png

    register_image_conversion(
        cairo_surface_to_tempfile_precondition,
        cairo_surface_to_tempfile_converter)
except ModuleNotFoundError:
    pass


try:
    from matplotlib.figure import Figure  # noqa
    from matplotlib.backends.backend_agg import FigureCanvasAgg  # noqa

    def figure_to_ndarray_precondition(obj):
        return isinstance(obj, Figure)

    def figure_to_ndarray_converter(figure):
        canvas = FigureCanvasAgg(figure)
        canvas.draw()
        return NumpyImageArray(np.asarray(canvas.buffer_rgba()), 'RGBA')

    register_image_conversion(
        figure_to_ndarray_precondition,
        figure_to_ndarray_converter)
except ModuleNotFoundError:
    pass
