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
import json
import re
from pathlib import Path
from typing import Any, Union, Dict, overload
import requests


class DataMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # *** BEGIN METHODS ***
    def load_json(
            self, json_path: Union[str, Path], **kwargs: Dict[str, Any]) -> Any:
        """Load a JSON data file from a file or URL.

        Parameters
        ----------

        json_path: Union[str, Path]
            url or file path for JSON data file

        kwargs: Dict[str, Any]
            keyword arguments

        Notes
        -----

        Load a JSON data file from a file or URL. When loading a file, the path can be
        in the data directory, relative to the current working directory
        (``sketch_path()``), or an absolute path. When loading from a URL, the
        ``json_path`` parameter must start with ``http://`` or ``https://``.

        When loading JSON data from a URL, the data is retrieved using the Python
        requests library with the ``get`` method, and the ``kwargs`` parameter is passed
        along to that method. When loading JSON data from a file, the data is loaded
        using the Python json library with the ``load`` method, and again the ``kwargs``
        parameter passed along to that method."""
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
                with open(path, 'r') as f:
                    return json.load(f, **kwargs)
            else:
                raise RuntimeError(
                    'Unable to find JSON file ' + str(json_path))

    def save_json(self,
                  json_data: Any,
                  filename: Union[str,
                                  Path],
                  **kwargs: Dict[str,
                                 Any]) -> None:
        """Save JSON data to a file.

        Parameters
        ----------

        filename: Union[str, Path]
            filename to save JSON data object to

        json_data: Any
            json data object

        kwargs: Dict[str, Any]
            keyword arguments

        Notes
        -----

        Save JSON data to a file. If ``filename`` is not an absolute path, it will be
        saved relative to the current working directory (``sketch_path()``).

        The JSON data is saved using the Python json library with the ``dump`` method,
        and the ``kwargs`` parameter is passed along to that method."""
        path = Path(filename)
        if not path.is_absolute():
            cwd = self.sketch_path()
            path = cwd / filename
        with open(path, 'w') as f:
            json.dump(json_data, f, **kwargs)

    @classmethod
    def parse_json(cls, serialized_json: Any, **kwargs: Dict[str, Any]) -> Any:
        """Parse serialized JSON data from a string.

        Parameters
        ----------

        kwargs: Dict[str, Any]
            keyword arguments

        serialized_json: Any
            JSON data object that has been serialized as a string

        Notes
        -----

        Parse serialized JSON data from a string. When reading JSON data from a file,
        ``load_json()`` is the better choice.

        The JSON data is parsed using the Python json library with the ``loads`` method,
        and the ``kwargs`` parameter is passed along to that method."""
        return json.loads(serialized_json, **kwargs)
