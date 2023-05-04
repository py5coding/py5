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
import re
import io
import zipfile
import requests
from pathlib import Path


PROCESSING_LIBRARY_URL = 'http://download.processing.org/contribs'

PARAGRAPH_REGEX = re.compile(
    '^paragraph=(.*?)^[a-z]*?=',
    re.DOTALL | re.MULTILINE)


class ProcessingLibraryInfo:

    def __init__(self):
        self._load_data()

    def _load_data(self):
        response = requests.get(PROCESSING_LIBRARY_URL)
        if response.status_code != 200:
            raise RuntimeError(
                f'could not download data file at {PROCESSING_LIBRARY_URL}')

        blocks = [b for b in response.text.split(
            '\n\n') if b.startswith('library')]
        data = [dict([line.split('=', 1)
                      for line in block.splitlines()
                      if line != "library"])
                for block in blocks]

        categories = set()
        names = list()
        for i, libinfo in enumerate(data):
            libinfo['id'] = int(libinfo['id'])
            libinfo['minRevision'] = int(libinfo['minRevision'])
            libinfo['maxRevision'] = int(libinfo['maxRevision'])
            libinfo['categories'] = libinfo['categories'].split(',')
            paragraph = PARAGRAPH_REGEX.findall(blocks[i])
            libinfo['paragraph'] = paragraph[0] if paragraph else ''

            categories.update(libinfo['categories'])
            names.append(libinfo['name'])

        self.categories = sorted(categories)
        self.names = sorted(names)
        self._data = data

    def get_library_info(
            self,
            category=None,
            library_name=None,
            library_id=None):
        # TODO: also make sure minRevision < version < maxRevision, but how?
        info = self._data
        if category:
            info = filter(lambda x: category in x.get('categories', []), info)
        if library_name:
            info = filter(lambda x: x.get('name') == library_name, info)
        if library_id:
            info = filter(lambda x: x.get('id') == int(library_id), info)

        return list(info)

    def download_zip(self, dest, library_name=None, library_id=None):
        info = self.get_library_info(
            library_name=library_name,
            library_id=library_id)

        if len(info) == 0:
            raise RuntimeError('There are no libraries named ' + library_name)
        if len(info) > 1:
            raise RuntimeError(
                'Multiple libraries found named ' +
                library_name)

        info = info[0]
        download_url = info['download']

        response = requests.get(download_url)
        if response.status_code != 200:
            raise RuntimeError(f'could not download library at {download_url}')

        with zipfile.ZipFile(io.BytesIO(response.content)) as zf:
            jars = []
            for name in zf.namelist():
                path = Path(name)
                if len(path.parts) > 2 and path.parts[1] == 'library':
                    jars.append(name)
            zf.extractall(dest, jars)


__all__ = ['ProcessingLibraryInfo']
