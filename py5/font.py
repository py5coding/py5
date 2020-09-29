# -*- coding: utf-8 -*-
# *** FORMAT PARAMS ***
import functools
from typing import overload, List  # noqa

import jpype
from jpype import JException, JArray, JString  # noqa

from .shape import Py5Shape, _return_py5shape  # noqa


def _return_py5font(f):
    @functools.wraps(f)
    def decorated(self_, *args):
        return Py5Font(f(self_, *args))
    return decorated


def _load_py5font(f):
    @functools.wraps(f)
    def decorated(self_, *args):
        # TODO: for load_font this prints a Java exception to strerr if the
        # file cannot be found or read
        try:
            ret = f(self_, *args)
        except JException as e:
            msg = e.message()
        else:
            if ret is None:
                msg = 'font file is missing or inaccessible.'
            else:
                return Py5Font(ret)
        raise RuntimeError('cannot load font file ' +
                           str(args[0]) + '. error message: ' + msg)
    return decorated


def _return_list_str(f):
    @functools.wraps(f)
    def decorated(cls_, *args):
        return [str(x) for x in f(cls_, *args) or []]
    return decorated


class Py5Font:

    _cls = jpype.JClass('processing.core.PFont')
    CHARSET = _cls.CHARSET

    def __init__(self, pfont):
        self._instance = pfont

    def ascent(self) -> float:
        """new template no description.

        Notes
        -----

        new template no description.
"""
        return self._instance.ascent()

    def descent(self) -> float:
        """new template no description.

        Notes
        -----

        new template no description.
"""
        return self._instance.descent()

    def get_default_size(self) -> int:
        """new template no description.

        Notes
        -----

        new template no description.
"""
        return self._instance.getDefaultSize()

    def get_glyph_count(self) -> int:
        """new template no description.

        Notes
        -----

        new template no description.
"""
        return self._instance.getGlyphCount()

    def get_name(self) -> str:
        """new template no description.

        Notes
        -----

        new template no description.
"""
        return self._instance.getName()

    def get_post_script_name(self) -> str:
        """new template no description.

        Notes
        -----

        new template no description.
"""
        return self._instance.getPostScriptName()

    @overload
    def get_shape(self, ch: chr, /) -> Py5Shape:
        """new template no description.

        Methods
        -------

        You can use any of the following signatures:

         * get_shape(ch: chr) -> Py5Shape
         * get_shape(ch: chr, detail: float) -> Py5Shape

        Parameters
        ----------

        ch: chr
            missing variable description

        detail: float
            missing variable description

        Notes
        -----

        new template no description.
"""
        pass

    @overload
    def get_shape(self, ch: chr, detail: float, /) -> Py5Shape:
        """new template no description.

        Methods
        -------

        You can use any of the following signatures:

         * get_shape(ch: chr) -> Py5Shape
         * get_shape(ch: chr, detail: float) -> Py5Shape

        Parameters
        ----------

        ch: chr
            missing variable description

        detail: float
            missing variable description

        Notes
        -----

        new template no description.
"""
        pass

    @_return_py5shape
    def get_shape(self, *args):
        """new template no description.

        Methods
        -------

        You can use any of the following signatures:

         * get_shape(ch: chr) -> Py5Shape
         * get_shape(ch: chr, detail: float) -> Py5Shape

        Parameters
        ----------

        ch: chr
            missing variable description

        detail: float
            missing variable description

        Notes
        -----

        new template no description.
"""
        return self._instance.getShape(*args)

    def get_size(self) -> int:
        """new template no description.

        Notes
        -----

        new template no description.
"""
        return self._instance.getSize()

    def is_smooth(self) -> bool:
        """new template no description.

        Notes
        -----

        new template no description.
"""
        return self._instance.isSmooth()

    def is_stream(self) -> bool:
        """new template no description.

        Notes
        -----

        new template no description.
"""
        return self._instance.isStream()

    @classmethod
    @_return_list_str
    def list(cls) -> List[str]:
        """Gets a list of the fonts installed on the system.

        Notes
        -----

        Gets a list of the fonts installed on the system. The data is returned as a
        String array. This list provides the names of each font for input into
        ``create_font()``, which allows Processing to dynamically format fonts.
"""
        return cls._cls.list()

    def set_subsetting(self) -> None:
        """new template no description.

        Notes
        -----

        new template no description.
"""
        return self._instance.setSubsetting()

    def width(self, c: chr, /) -> float:
        """new template no description.

        Parameters
        ----------

        c: chr
            missing variable description

        Notes
        -----

        new template no description.
"""
        return self._instance.width(c)
