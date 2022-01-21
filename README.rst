py5
---

.. image:: https://img.shields.io/pypi/dm/py5?label=py5%20PyPI%20downloads

.. image:: https://mybinder.org/badge_logo.svg
    :target: https://mybinder.org/v2/gh/hx2A/py5examples/HEAD?urlpath=lab

py5 is a new version of Processing_ for Python 3.8+. It makes the Processing_ Java libraries available to the CPython interpreter using JPype_. It can do just about everything Processing_ can do, except with Python instead of Java code.

The goal of py5 is to create a new version of Processing that is integrated into the Python ecosystem. Built into the library are thoughtful choices about how to best get py5 to work with other popular Python libraries such as `numpy 
<https://www.numpy.org/>`_ or `Pillow 
<https://python-pillow.org/>`_.

Here is a simple example of a working py5 Sketch:

.. code::

    import py5


    def setup():
        py5.size(200, 200)
        py5.rect_mode(py5.CENTER)


    def draw():
        py5.square(py5.mouse_x, py5.mouse_y, 10)


    py5.run_sketch()



If you have Java 11 installed on your computer, you can install py5 using pip:

.. code::

    pip install py5

`Detailed installation instructions 
<https://py5.ixora.io/content/install.html>`_ are available on the documentation website. There are some `Special Notes for Mac Users 
<https://py5.ixora.io/content/osx_users.html>`_ that you should read if you use OSX.

There are currently four basic ways to use py5. They are:

- **module mode**, as shown above
- **class mode**: create a Python class inherited from ``py5.Sketch``. This mode supports multiple Sketches running at the same time.
- **imported mode**: simplified code that omits the ``py5.`` prefix. This mode is supported by the py5 Jupyter notebook kernel and the ``run_sketch`` command line utility.
- **static mode**: functionless code to create static images. This mode is supported by the py5bot Jupyter notebook kernel, the ``%%py5bot`` IPython magic, and the ``run_sketch`` command line utility.

The py5 library is created by the meta-programming project py5generator_. Therefore, the py5 code should not be changed manually. Any issues, etc, should be directed to the py5generator_ repository.

The `py5 documentation website 
<https://py5.ixora.io/>`_ provides basic tutorials and reference documentation. The website is very much a work in progress. The reference documentation is solid but the how-to's and tutorials need a lot of work.

.. _Processing: https://github.com/processing/processing4
.. _JPype: https://github.com/jpype-project/jpype
.. _py5generator: https://github.com/hx2A/py5generator
