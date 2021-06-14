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
import os
from setuptools import setup

with open('README.rst') as f:
    README = f.read()

VERSION = '0.4a2'

INSTALL_REQUIRES = [
    'jpype1>=1.2',
    'line_profiler>=2.1.2',
    'noise>=1.2',
    'nptyping>=1.4',
    'numpy>=1.19',
    'pandas>=1.0',
    'pillow>=8.1',
    'requests>=2.25',
    'stackprinter>=0.2.4',
]

pjoin = os.path.join
here = os.path.abspath(os.path.dirname(__file__))

packages = []
for d, _, _ in [*os.walk(pjoin(here, 'py5')), *
                os.walk(pjoin(here, 'py5_tools'))]:
    if os.path.exists(pjoin(d, '__init__.py')):
        packages.append(d[len(here)+1:].replace(os.path.sep, '.'))

setup(
    name='py5',
    version=VERSION,
    packages=packages,
    py_modules=['setup'],
    package_data={
        "py5": ['jars/*.jar', 'jars/*/*.jar'],
        "py5_tools": ['kernel/resources/*.png'],
    },
    python_requires='>3.8',
    install_requires=INSTALL_REQUIRES,
    description='Processing for CPython',
    long_description=README,
    long_description_content_type='text/x-rst',
    author='Jim Schmitz',
    author_email='jim@ixora.io',
    entry_points={
        'console_scripts': [
            'run_sketch = py5_tools.tools.run_sketch:main',
            'py5cmd = py5_tools.tools.py5cmd:main',
            'py5utils = py5_tools.tools.py5utils:main',
        ],
    },
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Topic :: Artistic Software',
        'Topic :: Multimedia :: Graphics',
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Java',
    ],
)
