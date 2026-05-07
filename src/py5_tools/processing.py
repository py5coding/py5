# *****************************************************************************
#
#   Part of the py5 library
#   Copyright (C) 2020-2026 Jim Schmitz
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
import datetime as dt
import shutil
from pathlib import Path

from .constants import PY5_HOME
from .libraries import ProcessingLibraryInfo

STORAGE_DIR = Path(PY5_HOME) / "processing-libraries"
STORAGE_DIR.mkdir(parents=True, exist_ok=True)

_library_manager = None


class ProcessingLibraryManager:

    def __init__(self):
        self._libraries = None

    def _check_libraries(self):
        try:
            if self._libraries is None:
                self._libraries = ProcessingLibraryInfo()
        except:
            raise RuntimeError(
                "Processing library information not available. Your network connection might not be working."
            ) from None

    def _store_library_info(self, library_name, info):
        info_file = STORAGE_DIR / f"{library_name}.txt"
        current_date = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(info_file, "w") as f:
            f.write(f"name={info['name']}\n")
            f.write(f"version={info['version']}\n")
            f.write(f"prettyVersion={info['prettyVersion']}\n")
            f.write(f"downloadDate={current_date}\n")
            f.write(f"dir={info['dir']}\n")

    def _load_library_info(self, library_name):
        info_file = STORAGE_DIR / f"{library_name}.txt"
        if not info_file.exists():
            return None

        with open(info_file, "r") as f:
            lines = f.readlines()

        info = {}
        for line in lines:
            key, value = line.strip().split("=", maxsplit=1)
            if key == "version":
                info[key] = int(value)
            if key == "downloadDate":
                info[key] = dt.datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
            else:
                info[key] = value

        return info

    def installed_libraries(self):
        return {f.stem for f in STORAGE_DIR.glob("*.txt")}

    def check_library(self, library_name):
        """Check if a library is available and up to date.

        Args:
            library_name (str): The name of the library to check.

        Returns:
            bool: True if the library is available and up to date, False otherwise.
        """
        self._check_libraries()

        info = self._libraries.get_library_info(library_name=library_name)

        if len(info) == 0:
            return False
        if len(info) > 1:
            raise ValueError(f"Library {library_name} is ambiguous")

        info = info[0]

        stored_info = self._load_library_info(library_name)
        if stored_info and stored_info["version"] == info["version"]:
            return True
        else:
            return False

    def get_library(self, library_name):
        """Download a library if it is not already downloaded or is outdated.

        Args:
            library_name (str): The name of the library to download.

        Returns:
            dict: Information about the downloaded library.
        """
        self._check_libraries()

        info = self._libraries.get_library_info(library_name=library_name)

        if len(info) == 0:
            print(f"Library {library_name} not found")
            return
        if len(info) > 1:
            print(f"Library {library_name} is ambiguous")
            return

        info = info[0]

        stored_info = self._load_library_info(library_name)
        if stored_info:
            if stored_info["version"] == info["version"]:
                return stored_info
            print(f"Library {library_name} is outdated. Updating...")

        try:
            parts0 = self._libraries.download_zip(
                STORAGE_DIR, library_name=library_name
            )
            info["dir"] = parts0
            self._store_library_info(library_name, info)
            return self._load_library_info(library_name)
        except Exception as e:
            print(f"Failed to download library {library_name}: {e}")
            return

    def remove_library(self, library_name):
        """Remove a library from the storage directory.

        Args:
            library_name (str): The name of the library to remove.
        """
        info = self._load_library_info(library_name)
        if info:
            # Remove the library directory
            lib_dir = STORAGE_DIR / info["dir"]
            if lib_dir.exists():
                shutil.rmtree(lib_dir)

            # Remove the info file
            info_file = STORAGE_DIR / f"{library_name}.txt"
            if info_file.exists():
                info_file.unlink()
        else:
            print(f"Library {library_name} not found in storage.")


def library_storage_dir() -> Path:
    """Return the location of the Processing library storage directory.

    Notes
    -----

    Return the location of the Processing library storage directory. You should
    never need to manually edit files in this directory, but if for some reason you
    do, you'll first need to find it. By default, this will be in `~/.cache/py5` on
    Linux and MacOS machines and `~/AppData/Local/py5` on Windows machines. These
    locations are similar to where other Python libraries store their data files. If
    you wish, set the `PY5_HOME` environment variable to move the storage directory
    to a location of your choosing.

    If you wish to manually add Java Jar files to py5's classpath, don't use this
    directory. Instead, put jars in a `jars` subdirectory (relative to the current
    working directory of your Python code) or set the `PY5_JARS` environment
    variable to the path of the directory you wish to use."""
    return STORAGE_DIR


def installed_libraries() -> set[str]:
    """List the Processing libraries stored in your computer's Processing library
    storage directory.

    Notes
    -----

    List the Processing libraries stored in your computer's Processing library
    storage directory. These are all of the Processing libraries that have been
    installed using the `py5_tools.processing.download_library()` function. To get
    the location of the library storage directory, use the
    `py5_tools.processing.library_storage_dir()` function.

    Downloaded libraries will be saved in the Processing library storage directory.
    Use `py5_tools.processing.library_storage_dir()` to get the specific location of
    the storage directory on your machine."""
    global _library_manager
    if _library_manager is None:
        _library_manager = ProcessingLibraryManager()

    return _library_manager.installed_libraries()


def check_library(library_name: str) -> bool:
    """Check if a Processing library has been downloaded and stored by py5.

    Parameters
    ----------

    library_name: str
        name of Processing library

    Notes
    -----

    Check if a Processing library has been downloaded and stored by py5. These are
    the same libraries available to you in the Library Manager when you use the
    Processing Development Environment (PDE). Downloaded libraries are available for
    you to import in Python after you import py5.

    Downloaded libraries will be saved in the Processing library storage directory.
    Use `py5_tools.processing.library_storage_dir()` to get the specific location of
    the storage directory on your machine."""
    global _library_manager
    if _library_manager is None:
        _library_manager = ProcessingLibraryManager()

    return _library_manager.check_library(library_name)


def download_library(library_name: str) -> dict:
    """Download and store a Processing library.

    Parameters
    ----------

    library_name: str
        name of Processing library

    Notes
    -----

    Download and store a Processing library. These are the same libraries available
    to you in the Library Manager when you use the Processing Development
    Environment (PDE). After this function downloads a Processing library, it will
    be available for you to import in Python after you import py5.

    This function will also return a dictionary containing some basic information
    about the installed library. If the library was previously downloaded, it will
    check the version numbers and will update the library if it is not current. If
    you want to remove an installed library, use
    `py5_tools.processing.remove_library()`.

    Downloaded libraries will be saved in the Processing library storage directory.
    Use `py5_tools.processing.library_storage_dir()` to get the specific location of
    the storage directory on your machine."""
    global _library_manager
    if _library_manager is None:
        _library_manager = ProcessingLibraryManager()

    return _library_manager.get_library(library_name)


def remove_library(library_name: str) -> None:
    """Remove a previously downloaded and stored Processing library.

    Parameters
    ----------

    library_name: str
        name of Processing library

    Notes
    -----

    Remove a previously downloaded and stored Processing library. These are the same
    libraries available to you in the Library Manager when you use the Processing
    Development Environment (PDE). You download and install Processing libraries
    with `py5_tools.processing.download_library()`. After this function removes a
    Processing library, it will no longer be available for you to use with py5."""
    global _library_manager
    if _library_manager is None:
        _library_manager = ProcessingLibraryManager()

    _library_manager.remove_library(library_name)


__all__ = [
    "check_library",
    "download_library",
    "installed_libraries",
    "library_storage_dir",
    "remove_library",
]


def __dir__():
    return __all__
