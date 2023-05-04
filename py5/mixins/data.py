# *****************************************************************************
#
#   Part of the py5 library
#   Copyright (C) 2020-2023 Jim Schmitz
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
from __future__ import annotations

import json
import re
import pickle
from pathlib import Path
from typing import Any, Union
import requests


class DataMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # *** BEGIN METHODS ***
    def load_json(
            self, json_path: Union[str, Path], **kwargs: dict[str, Any]) -> Any:
        """Load a JSON data file from a file or URL.

        Parameters
        ----------

        json_path: Union[str, Path]
            url or file path for JSON data file

        kwargs: dict[str, Any]
            keyword arguments

        Notes
        -----

        Load a JSON data file from a file or URL. When loading a file, the path can be
        in the data directory, relative to the current working directory
        (`sketch_path()`), or an absolute path. When loading from a URL, the `json_path`
        parameter must start with `http://` or `https://`.

        When loading JSON data from a URL, the data is retrieved using the Python
        requests library with the `get` method, and any extra keyword arguments (the
        `kwargs` parameter) are passed along to that method. When loading JSON data from
        a file, the data is loaded using the Python json library with the `load` method,
        and again any extra keyword arguments are passed along to that method."""
        if isinstance(
                json_path,
                str) and re.match(
                r'https?://',
                json_path.lower()):
            response = requests.get(json_path, **kwargs)
            if response.status_code == 200:
                return response.json()
            else:
                raise RuntimeError(
                    'Unable to download JSON URL: ' +
                    response.reason)
        else:
            path = Path(json_path)
            if not path.is_absolute():
                cwd = self.sketch_path()
                if (cwd / 'data' / json_path).exists():
                    path = cwd / 'data' / json_path
                else:
                    path = cwd / json_path
            if path.exists():
                with open(path, 'r', encoding='utf8') as f:
                    return json.load(f, **kwargs)
            else:
                raise RuntimeError(
                    'Unable to find JSON file ' + str(json_path))

    def save_json(self,
                  json_data: Any,
                  filename: Union[str,
                                  Path],
                  **kwargs: dict[str,
                                 Any]) -> None:
        """Save JSON data to a file.

        Parameters
        ----------

        filename: Union[str, Path]
            filename to save JSON data object to

        json_data: Any
            json data object

        kwargs: dict[str, Any]
            keyword arguments

        Notes
        -----

        Save JSON data to a file. If `filename` is not an absolute path, it will be
        saved relative to the current working directory (`sketch_path()`). The saved
        file can be reloaded with `load_json()`.

        The JSON data is saved using the Python json library with the `dump` method, and
        the `kwargs` parameter is passed along to that method."""
        path = Path(filename)
        if not path.is_absolute():
            cwd = self.sketch_path()
            path = cwd / filename
        if not path.parent.exists():
            path.parent.mkdir(parents=True)
        with open(path, 'w') as f:
            json.dump(json_data, f, **kwargs)

    @classmethod
    def parse_json(cls, serialized_json: Any, **kwargs: dict[str, Any]) -> Any:
        """Parse serialized JSON data from a string.

        Parameters
        ----------

        kwargs: dict[str, Any]
            keyword arguments

        serialized_json: Any
            JSON data object that has been serialized as a string

        Notes
        -----

        Parse serialized JSON data from a string. When reading JSON data from a file,
        `load_json()` is the better choice.

        The JSON data is parsed using the Python json library with the `loads` method,
        and the `kwargs` parameter is passed along to that method."""
        return json.loads(serialized_json, **kwargs)

    def load_strings(
            self, string_path: Union[str, Path], **kwargs: dict[str, Any]) -> list[str]:
        """Load a list of strings from a file or URL.

        Underlying Processing method: Sketch.loadStrings

        Parameters
        ----------

        kwargs: dict[str, Any]
            keyword arguments

        string_path: Union[str, Path]
            url or file path for string data file

        Notes
        -----

        Load a list of strings from a file or URL. When loading a file, the path can be
        in the data directory, relative to the current working directory
        (`sketch_path()`), or an absolute path. When loading from a URL, the
        `string_path` parameter must start with `http://` or `https://`.

        When loading string data from a URL, the data is retrieved using the Python
        requests library with the `get` method, and any extra keyword arguments (the
        `kwargs` parameter) are passed along to that method. When loading string data
        from a file, the `kwargs` parameter is not used."""
        if isinstance(
                string_path,
                str) and re.match(
                r'https?://',
                string_path.lower()):
            response = requests.get(string_path, **kwargs)
            if response.status_code == 200:
                return response.text.splitlines()
            else:
                raise RuntimeError(
                    'Unable to download URL: ' +
                    response.reason)
        else:
            path = Path(string_path)
            if not path.is_absolute():
                cwd = self.sketch_path()
                if (cwd / 'data' / string_path).exists():
                    path = cwd / 'data' / string_path
                else:
                    path = cwd / string_path
            if path.exists():
                with open(path, 'r', encoding='utf8') as f:
                    return f.read().splitlines()
            else:
                raise RuntimeError('Unable to find file ' + str(string_path))

    def save_strings(self,
                     string_data: list[str],
                     filename: Union[str,
                                     Path],
                     *,
                     end: str = '\n') -> None:
        """Save a list of strings to a file.

        Underlying Processing method: Sketch.saveStrings

        Parameters
        ----------

        end: str = '\\n'
            line terminator for each string

        filename: Union[str, Path]
            filename to save string data to

        string_data: list[str]
            string data to save in a file

        Notes
        -----

        Save a list of strings to a file. If `filename` is not an absolute path, it will
        be saved relative to the current working directory (`sketch_path()`). If the
        contents of the list are not already strings, it will be converted to strings
        with the Python builtin `str`. The saved file can be reloaded with
        `load_strings()`.

        Use the `end` parameter to set the line terminator for each string in the list.
        If items in the list of strings already have line terminators, set the `end`
        parameter to `''` to keep the output file from being saved with a blank line
        after each item."""
        path = Path(filename)
        if not path.is_absolute():
            path = self.sketch_path() / filename
        if not path.parent.exists():
            path.parent.mkdir(parents=True)
        with open(path, 'w') as f:
            f.write(end.join(str(s) for s in string_data))

    def load_bytes(
            self, bytes_path: Union[str, Path], **kwargs: dict[str, Any]) -> bytearray:
        """Load byte data from a file or URL.

        Underlying Processing method: Sketch.loadBytes

        Parameters
        ----------

        bytes_path: Union[str, Path]
            url or file path for bytes data file

        kwargs: dict[str, Any]
            keyword arguments

        Notes
        -----

        Load byte data from a file or URL. When loading a file, the path can be in the
        data directory, relative to the current working directory (`sketch_path()`), or
        an absolute path. When loading from a URL, the `bytes_path` parameter must start
        with `http://` or `https://`.

        When loading byte data from a URL, the data is retrieved using the Python
        requests library with the `get` method, and any extra keyword arguments (the
        `kwargs` parameter) are passed along to that method. When loading byte data from
        a file, the `kwargs` parameter is not used."""
        if isinstance(
                bytes_path,
                str) and re.match(
                r'https?://',
                bytes_path.lower()):
            response = requests.get(bytes_path, **kwargs)
            if response.status_code == 200:
                return bytearray(response.content)
            else:
                raise RuntimeError(
                    'Unable to download URL: ' +
                    response.reason)
        else:
            path = Path(bytes_path)
            if not path.is_absolute():
                cwd = self.sketch_path()
                if (cwd / 'data' / bytes_path).exists():
                    path = cwd / 'data' / bytes_path
                else:
                    path = cwd / bytes_path
            if path.exists():
                with open(path, 'rb') as f:
                    return bytearray(f.read())
            else:
                raise RuntimeError('Unable to find file ' + str(bytes_path))

    def save_bytes(self,
                   bytes_data: Union[bytes,
                                     bytearray],
                   filename: Union[str,
                                   Path]) -> None:
        """Save byte data to a file.

        Underlying Processing method: Sketch.saveBytes

        Parameters
        ----------

        bytes_data: Union[bytes, bytearray]
            byte data to save in a file

        filename: Union[str, Path]
            filename to save byte data to

        Notes
        -----

        Save byte data to a file. If `filename` is not an absolute path, it will be
        saved relative to the current working directory (`sketch_path()`). The saved
        file can be reloaded with `load_bytes()`."""
        path = Path(filename)
        if not path.is_absolute():
            path = self.sketch_path() / filename
        if not path.parent.exists():
            path.parent.mkdir(parents=True)
        with open(path, 'wb') as f:
            f.write(bytes_data)

    def load_pickle(self, pickle_path: Union[str, Path]) -> Any:
        """Load a pickled Python object from a file.

        Underlying Processing method: Sketch.loadPickle

        Parameters
        ----------

        pickle_path: Union[str, Path]
            file path for pickle object file

        Notes
        -----

        Load a pickled Python object from a file. The path can be in the data directory,
        relative to the current working directory (`sketch_path()`), or an absolute
        path.

        There are security risks associated with Python pickle files. A pickle file can
        contain malicious code, so never load a pickle file from an untrusted source."""
        path = Path(pickle_path)
        if not path.is_absolute():
            cwd = self.sketch_path()
            if (cwd / 'data' / pickle_path).exists():
                path = cwd / 'data' / pickle_path
            else:
                path = cwd / pickle_path
        if path.exists():
            with open(path, 'rb') as f:
                return pickle.load(f)
        else:
            raise RuntimeError('Unable to find file ' + str(pickle_path))

    def save_pickle(self, obj: Any, filename: Union[str, Path]) -> None:
        """Pickle a Python object to a file.

        Underlying Processing method: Sketch.savePickle

        Parameters
        ----------

        filename: Union[str, Path]
            filename to save pickled object to

        obj: Any
            any non-py5 Python object

        Notes
        -----

        Pickle a Python object to a file. If `filename` is not an absolute path, it will
        be saved relative to the current working directory (`sketch_path()`). The saved
        file can be reloaded with `load_pickle()`.

        Object "pickling" is a method for serializing objects and saving them to a file
        for later retrieval. The recreated objects will be clones of the original
        objects. Not all Python objects can be saved to a Python pickle file. This
        limitation prevents any py5 object from being pickled."""
        path = Path(filename)
        if not path.is_absolute():
            path = self.sketch_path() / filename
        if not path.parent.exists():
            path.parent.mkdir(parents=True)
        with open(path, 'wb') as f:
            pickle.dump(obj, f)
