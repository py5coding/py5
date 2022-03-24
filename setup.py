# *****************************************************************************
#
#   Part of the py5 library
#   Copyright (C) 2020-2022 Jim Schmitz
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

VERSION = '0.7.1a6'

INSTALL_REQUIRES = [
    'autopep8>=1.5',
    'ipykernel>=5.3',
    'ipython>=7.22',
    'ipywidgets>=7.6',
    'jpype1>=1.3',
    'line_profiler>=2.1.2',
    'numpy>=1.21',
    'pandas>=1.0',
    'pillow>=8.1',
    'pyobjc>=7.3;sys_platform=="darwin"',
    'requests>=2.25',
    'stackprinter>=0.2.4',
    'traitlets>=5.0',
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
    package_data={
        "py5": ['jars/*.jar', 'jars/*/*.jar', 'natives/*/*.dll', 'natives/*/*.so', 'natives/*/*.dylib'],
        "py5_tools": ['kernel/resources/*.png', 'py5bot/resources/*.png'],
    },
    python_requires='>3.8',
    install_requires=INSTALL_REQUIRES,
    description='Processing for CPython',
    long_description=README,
    long_description_content_type='text/x-rst',
    author='Jim Schmitz',
    author_email='jim@ixora.io',
    url='https://github.com/hx2A/py5generator',
    entry_points={
        'console_scripts': [
            'run_sketch = py5_tools.tools.run_sketch:main',
            'py5cmd = py5_tools.tools.py5cmd:main',
            'py5utils = py5_tools.tools.py5utils:main',
            'py5translate-module2imported = py5_tools.tools.py5translate_module2imported:main',
            'py5translate-imported2module = py5_tools.tools.py5translate_imported2module:main',
            'py5translate-processingpy2imported = py5_tools.tools.py5translate_processingpy2imported:main',
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
