# py5

[![py5 montly downloads](https://pepy.tech/badge/py5/month)](https://pepy.tech/project/py5)

[![py5 weekly downloads](https://pepy.tech/badge/py5/week)](https://pepy.tech/project/py5)

[![mybinder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/py5coding/py5examples/HEAD?urlpath=lab)

py5 is a new version of [**Processing**][processing] for Python 3.8+. It makes the Java [**Processing**][processing] jars available to the CPython interpreter using [**JPype**][jpype]. It can do just about all of the 2D and 3D drawing [**Processing**][processing] can do, except with Python instead of Java code.

The goal of py5 is to create a new version of Processing that is integrated into the Python ecosystem. Built into the library are thoughtful choices about how to best get py5 to work with other popular Python libraries and tools such as [Jupyter][jupyter], [numpy][numpy], and [Pillow][pillow].

## Simple Example

Here is a simple example of a working py5 Sketch, written in module mode:

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

[Detailed installation instructions](https://py5coding.org/content/install.html) are available on the documentation website. There are some [Special Notes for Mac Users](https://py5coding.org/content/osx_users.html) that you should read if you use OSX.

## Getting Started

There are currently four basic ways to use py5. They are:

* **module mode**: create a sketch with `setup()` and `draw()` functions that call methods provided by the `py5` library. The above example is created in module mode.
* **class mode**: create a Python class inherited from `py5.Sketch`. This mode supports multiple Sketches running at the same time.
* **imported mode**: simplified code that omits the `py5.` prefix. This mode is supported by the py5 Jupyter notebook kernel and the `run_sketch` command line utility.
* **static mode**: functionless code to create static images. This mode is supported by the py5bot Jupyter notebook kernel, the `%%py5bot` IPython magic, and the `run_sketch` command line utility.

The documentation website, [https://py5coding.org/](https://py5coding.org/), is a work in progress. The reference documentation is solid but the how-to's and tutorials are incomplete.

[py5generator][py5_generator_repo] is a meta-programming project that creates the py5 library. To view the actual installed py5 library code, look at the [py5 repository][py5_repo]. All py5 library development is done through py5generator.

## Get In Touch

Have a comment or question? We'd love to hear from you! The best ways to reach out are:

* github [discussions](https://github.com/py5coding/py5generator/discussions) and [issues](https://github.com/py5coding/py5generator/issues)
* Mastodon <a rel="me" href="https://fosstodon.org/@py5coding">fosstodon.org/@py5coding</a>
* twitter [@py5coding](https://twitter.com/py5coding)
* [processing foundation discourse](https://discourse.processing.org/)

[py5_repo]: https://github.com/py5coding/py5
[py5_generator_repo]: https://github.com/py5coding/py5generator
[processing]: https://github.com/processing/processing4
[jpype]: https://github.com/jpype-project/jpype

[jupyter]: https://jupyter.org/
[numpy]: https://numpy.org/
[pillow]: https://python-pillow.org/
