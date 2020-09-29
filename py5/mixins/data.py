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
        """new template no description.

        Parameters
        ----------

        filename: Union[str, Path]
            missing variable description

        kwargs: Dict[str, Any]
            missing variable description

        Notes
        -----

        new template no description.
"""
        with open(filename, 'r') as f:
            return json.load(f, **kwargs)

    @classmethod
    def save_json(cls,
                  json_data: Any,
                  filename: Union[str,
                                  Path],
                  **kwargs: Dict[str,
                                 Any]) -> None:
        """new template no description.

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

        new template no description.
"""
        with open(filename, 'w') as f:
            json.dump(json_data, f, **kwargs)

    @classmethod
    def parse_json(cls, serialized_json: Any, **kwargs: Dict[str, Any]) -> Any:
        """new template no description.

        Parameters
        ----------

        kwargs: Dict[str, Any]
            missing variable description

        serialized_json: Any
            missing variable description

        Notes
        -----

        new template no description.
"""
        return json.loads(serialized_json, **kwargs)
