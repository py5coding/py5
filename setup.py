from pathlib import Path
from setuptools import setup

with open('README.rst') as f:
    README = f.read()


with open(Path('py5', '__init__.py')) as f:
    for line in f.readlines():
        if line.startswith('__version__'):
            break
    VERSION = line.split("'")[-2]


INSTALL_REQUIRES = [
    'cairocffi>=1.1',
    'cairosvg>=2.4',
    'jpype1>=1.0.1',
    'line_profiler>=2.1.2',
    'matplotlib>=3.2',
    'nptyping>=1.3',
    'numpy>=1.18',
    'pandas>=1.0',
    'requests>=2.24',
    'stackprinter>=0.2.4',
]

setup(
    name='py5',
    version=VERSION,
    packages=['py5', 'py5.mixins', 'py5_tools', 'py5_tools.tools'],
    py_modules=['setup'],
    package_data={
        "py5": ['jars/*.jar', 'jars/*/*.jar', '*.pyi', 'py.typed']
    },
    python_requires='>3.8',
    install_requires=INSTALL_REQUIRES,
    description='Processing for CPython',
    long_description=README,
    author='Jim Schmitz',
    author_email='jim@ixora.io',
    entry_points={
        'console_scripts': [
            'run_sketch = py5_tools.tools.run_sketch:main',
            'py5cmd = py5_tools.tools.py5cmd:main',
        ],
    },
    classifiers=[
        'Intended Audience :: Developers',
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3.8',
    ],
)
