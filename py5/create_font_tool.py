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

        os = self.get_py5applet().createOutput(str(self.filename))
        font._instance.save(os)
        os.close()

        self.fill(255)
        msg = str(font.get_glyph_count()) + \
            ' glyphs written to ' + self.filename
        self.translate(self.width / 2, self.height / 2)
        self.scale(0.95 * self.width / self.text_width(msg))
        self.text(msg, 0, 0)

    def draw(self):
        if self.pause:
            self.no_loop()
        else:
            self.exit_sketch()


def create_font_file(
        font_name: str,
        font_size: int,
        filename: str = None,
        characters: str = None,
        pause: bool = True):
    """missing docstring"""
    vlw_creator = CreateFontTool(font_name, font_size,
                                 filename=filename, characters=characters,
                                 pause=pause)
    vlw_creator.run_sketch(block=pause)
