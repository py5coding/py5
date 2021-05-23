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
from .sketch import Sketch


class CreateFontTool(Sketch):

    def __init__(
            self,
            font_name,
            font_size,
            filename=None,
            characters=None,
            pause=True):
        super().__init__()
        self.font_name = font_name
        self.font_size = font_size
        self.pause = pause
        self.filename = filename or f'{font_name}-{font_size}.vlw'
        self.characters = characters

    def settings(self):
        self.size(400, 100, self.P2D)

    def setup(self):
        font = self.create_font(self.font_name, self.font_size)
        self.text_align(self.CENTER)

        self.background(0)
        self.fill(0)

        self.text_font(font)
        characters = self.characters or ''.join(font.CHARSET)
        self.text(characters, self.width / 2, self.height / 2)

        os = self._instance.createOutput(str(self.filename))
        font._instance.save(os)
        os.close()

        self.fill(255)
        msg = str(font.get_glyph_count()) + \
            ' glyphs written to ' + self.filename
        self.translate(self.width / 2, self.height / 2)
        self.scale(0.95 * self.width / self.text_width(msg))
        self.text(msg, 0, 0)

        if not self.pause:
            self.exit_sketch()


def create_font_file(
        font_name: str,
        font_size: int,
        filename: str = None,
        characters: str = None,
        pause: bool = True):
    """Utility function to create Processing's vlw font data files.

    Parameters
    ----------

    characters: str = None
        limit glyphs to characters found in string

    filename: str = None
        vlw data file to save font data to

    font_name: str
        name of font found on computer

    font_size: int
        font size in units of pixels

    pause: bool = True
        pause after creating font file

    Notes
    -----

    Utility function to create Processing's vlw font data files. In Processing,
    users would create these files through the PDE using the Create Font tool. This
    utility function accomplishes the same task.

    This function creates a small helper Sketch to create a font file. Do not use
    this function inside of another Sketch.

    By default it will create data files for every character available in the
    specified font. To reduce execution time and output file size, limit the
    characters using the ``characters`` parameter. The default output filename is
    ``{font_name}-{font_size}.vlw`` and will be saved to the current directory.

    This utility function opens a window that displays a short message about the
    number of glyphs written to the file. To make the window close automatically,
    set the ``pause`` parameter to ``False``.

    Get a list of font names available on your computer with Py5Font's
    ``Py5Font.list()`` method. If you request an unavailable font, it will create
    the data file anyway but using a default font."""
    vlw_creator = CreateFontTool(font_name, font_size,
                                 filename=filename, characters=characters,
                                 pause=pause)
    vlw_creator.run_sketch(block=pause)
