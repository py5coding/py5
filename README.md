# py5

[![py5 montly downloads](https://pepy.tech/badge/py5/month)](https://pepy.tech/project/py5)

[![py5 weekly downloads](https://pepy.tech/badge/py5/week)](https://pepy.tech/project/py5)

[![mybinder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/py5coding/py5examples/HEAD?urlpath=lab)

py5 is a new version of [Processing][processing] for Python 3.9+. The goal of py5 is to create a version of Processing that is [integrated into the Python ecosystem](https://py5coding.org/integrations/python_ecosystem_integrations.html). Built into the library are thoughtful choices about how to best get py5 to work with other popular Python libraries and tools such as [Jupyter](https://jupyter.org/), [numpy](https://numpy.org/), [shapely](https://shapely.readthedocs.io/en/stable/), [trimesh](https://trimesh.org/), [matplotlib](https://matplotlib.org/), and [Pillow](https://python-pillow.org/).

py5 is an excellent choice for educators looking to teach Python in the context of creative coding and is currently used in classrooms all around the world. The documentation website includes [introductory tutorials](https://py5coding.org/tutorials/intro_to_py5_and_python.html) as well as extensive [reference documentation](https://py5coding.org/reference/summary.html), complete with example code.

## Basic Example

Here is a basic example of a working py5 Sketch:

```python3
import py5


def setup():
    py5.size(400, 400)
    py5.rect_mode(py5.CENTER)


def draw():
    py5.square(py5.mouse_x, py5.mouse_y, 10)


def mouse_clicked():
    py5.fill(py5.random_int(255), py5.random_int(255), py5.random_int(255))


py5.run_sketch()
```

## Installation

If you have Java 17 installed on your computer, you can install py5 using pip:

```bash
pip install py5
```

[Detailed installation instructions](https://py5coding.org/content/install.html) are available on the documentation website. There are some [Special Notes for Mac Users](https://py5coding.org/content/macos_users.html) that you should read if you use macOS.

## Getting Started

If you are new to Python, start with the [intro to py5 and python](https://py5coding.org/tutorials/intro_to_py5_and_python.html) tutorials. If you are familiar with Java programming and Processing, you'll find the [Tips for Processing Java Users](https://py5coding.org/content/coming_from_processing_java.html) page to be helpful.

There are currently five basic ways to use py5. They are:

* **module mode**: create a sketch with `setup()` and `draw()` functions that call methods provided by the `py5` library. The above example is created in module mode.
* **class mode**: create a Python class inherited from `py5.Sketch`. This mode supports multiple Sketches running at the same time.
* **imported mode**: simplified code that omits the `py5.` prefix. This mode is supported by the py5 Jupyter notebook kernel and the `run_sketch` command line utility.
* **static mode**: functionless code to create static images. This mode is supported by the py5bot Jupyter notebook kernel, the `%%py5bot` IPython magic, and the `run_sketch` command line utility.
* **processing mode**: make calls to Python from a Processing (Java) Sketch. This mode enables py5 to function as bridge, connecting the Python and Java ecosystems through a new `callPython()` method.

## Source Code

py5 was created by the artist and software developer [Jim Schmitz](https://ixora.io/) ([@hx2A](https://github.com/hx2A)) starting in March of 2020. The library is the foundation of his [art practice](https://ixora.io/art/).

The py5 library makes the Java Processing jars available to the CPython interpreter using [JPype][jpype]. It can do just about everything Processing can do, except with Python instead of Java code. New py5 features and bug fixes are being added to py5 every day. The library is always in active development and is well maintained.

To view the actual installed py5 library code, look at the [py5 repository][py5_repo]. The py5 library code is the output of the meta-programming project [py5generator][py5generator_repo]. All py5 development is done through [py5generator][py5generator_repo].

## Funding

[Please sponsor py5!](https://github.com/sponsors/py5coding)

This project is not an official part of the Processing Foundation and is not receiving any funding from them. Any funds you contribute will be used first for website expenses and next to support [@hx2A](https://github.com/hx2A/)'s time to further develop py5 as a solid creative coding framework used by educators, artists, and hobbyists all around the world.

## Get In Touch

Have a comment or question? We'd love to hear from you! The best ways to reach out are:

* github [discussions](https://github.com/py5coding/py5generator/discussions) and [issues](https://github.com/py5coding/py5generator/issues)
* Mastodon <a rel="me" href="https://fosstodon.org/@py5coding">fosstodon.org/@py5coding</a>
* twitter [@py5coding](https://twitter.com/py5coding)
* [processing foundation discourse](https://discourse.processing.org/c/28)

[processing]: https://github.com/processing/processing4
[jpype]: https://github.com/jpype-project/jpype
[py5_repo]: https://github.com/py5coding/py5
[py5generator_repo]: https://github.com/py5coding/py5generator
