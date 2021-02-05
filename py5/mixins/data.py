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
from pathlib import Path
from typing import Any, Union, Dict


class DataMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # *** BEGIN METHODS ***

    @classmethod
    def load_json(cls, filename: Union[str, Path],
                  **kwargs: Dict[str, Any]) -> Any:
        """The documentation for this field or method has not yet been written.

        Parameters
        ----------

        filename: Union[str, Path]
            missing variable description

        kwargs: Dict[str, Any]
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/."""
        with open(filename, 'r') as f:
            return json.load(f, **kwargs)

    @classmethod
    def save_json(cls,
                  json_data: Any,
                  filename: Union[str,
                                  Path],
                  **kwargs: Dict[str,
                                 Any]) -> None:
        """The documentation for this field or method has not yet been written.

        Parameters
        ----------

        filename: Union[str, Path]
            missing variable description

        json_data: Any
            missing variable description

        kwargs: Dict[str, Any]
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/."""
        with open(filename, 'w') as f:
            json.dump(json_data, f, **kwargs)

    @classmethod
    def parse_json(cls, serialized_json: Any, **kwargs: Dict[str, Any]) -> Any:
        """The documentation for this field or method has not yet been written.

        Parameters
        ----------

        kwargs: Dict[str, Any]
            missing variable description

        serialized_json: Any
            missing variable description

        Notes
        -----

        The documentation for this field or method has not yet been written. If you know
        what it does, please help out with a pull request to the relevant file in
        https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/."""
        return json.loads(serialized_json, **kwargs)
