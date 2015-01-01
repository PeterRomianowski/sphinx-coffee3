===================
CoffeeScript Domain
===================

Extension: Python3 and automodule
=================================

:author: Peter Romianowski <honbkert@gmail.com> (Python3 support)

This extension requires Python3. 

In order to be able to use ``automodule`` for both, Python and CoffeeScript
sources, this version of the extensions uses ``autocoffeemodule`` (see Autodoc_)
as directive.

About
=====

:author: Stephen Sugden <glurgle@gmail.com> (Original)

This extension adds a CoffeeScript domain with autodoc support to Sphinx.

This relies on coffeedoc_ to extract source comments from ``.coffee``
files. To install coffeedoc globally::

  npm install -g coffeedoc

.. _coffeedoc: https://github.com/omarkhan/coffeedoc

Usage
=====

First you must add the extension to your list of extensions in conf.py::

  extensions = ['sphinx.ext.autodoc', 'sphinxcontrib.coffeedomain']

Because Python has no clue about where your CoffeeScript sources are located,
you must tell it where to look in your conf.py like so::

  coffee_src_dir = os.path.abspath('../')

Depending on the module system you use, you might want to change the coffeedoc
parser from its default ``commonjs`` to ``requirejs``::

  coffee_src_parser = 'requirejs'

Finally, if your project is primarily CoffeeScript, you might want to
define the primary domain as well::

  primary_domain = 'coffee'

Directives and Roles
====================

This domain provides module, function, class and method directives, as
well as meth, class, and func roles for cross-referencing. In order to
reference another object, use it's fully-qualified name: The module name,
a double colon, and the dot separate path to the object within the module.

For example, to reference the ``swizzle`` function in the file
``lib/widgets.coffee``, write ``:coffee:func:`lib/widgets::swizzle``. You
can drop the leading ``:coffee`` if your primary domain has been
set to coffee, and you can drop the module name iff you are linking from
within the ``lib/widgets`` module.

Autodoc
=======

You can document entire modules easily with ``autocoffeemodule``:

.. sourcecode:: rst

  .. autocoffeemodule:: mymodule