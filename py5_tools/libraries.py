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
import re
import io
import zipfile
import requests
from functools import reduce
from pathlib import Path

import pandas as pd


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
        block_lines = [dict([line.split('=', 1)
                            for line in block.splitlines()
                            if line != "library"])
                       for block in blocks]
        df = pd.DataFrame.from_dict(block_lines, dtype="string")
        # lastUpdated is supposed to be the last column
        df = df.iloc[:, :(df.columns.get_loc('lastUpdated') + 1)]
        df.astype({'id': int, 'minRevision': int, 'maxRevision': int})
        df['id'] = df['id'].astype(int)
        df['minRevision'] = df['minRevision'].astype(int)
        df['maxRevision'] = df['maxRevision'].astype(int)
        df['categories'] = df['categories'].apply(lambda x: x.split(','))
        # get paragraph values from raw data because they could be on more than one
        # line or the paragraph could be missing
        df['paragraph'] = [PARAGRAPH_REGEX.findall(b) for b in blocks]
        df['paragraph'] = df['paragraph'].apply(
            lambda x: x[0] if x else '').astype('string')

        self._data = df
        self.categories = sorted(
            reduce(
                lambda x,
                y: x | set(y),
                df['categories'],
                set()))
        self.names = sorted(df['name'])

    def get_library_info(
            self,
            category=None,
            library_name=None,
            library_id=None):
        info = self._data
        # TODO: also make sure minRevision < version < maxRevision
        if category:
            info = info[info['categories'].apply(lambda x: category in x)]
        if library_name:
            info = info[info['name'] == library_name]
        if library_id:
            info = info[info['id'] == library_id]

        return info

    def download_zip(self, dest, library_name=None, library_id=None):
        info = self.get_library_info(
            library_name=library_name,
            library_id=library_id)

        if len(info) == 0:
            raise RuntimeError(f'library not found')
        if len(info) > 1:
            raise RuntimeError(f'more than one library')

        info = info.T.to_dict()[info.index[0]]
        download_url = info['download']

        response = requests.get(download_url)
        if response.status_code != 200:
            raise RuntimeError(f'could not download library at {download_url}')

        with zipfile.ZipFile(io.BytesIO(response.content)) as zf:
            jars = []
            for name in zf.namelist():
                path = Path(name)
                if len(
                        path.parts) > 2 and path.parts[1] == 'library' and path.suffix == '.jar':
                    jars.append(name)
            zf.extractall(dest, jars)


__all__ = ['ProcessingLibraryInfo']
