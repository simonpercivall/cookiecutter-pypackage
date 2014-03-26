Welcome to {{ cookiecutter.project_name }}'s documentation!
{{ '=' * (cookiecutter.project_name|count + 11 + 17) }}

Contents:
=========

.. include:: ../README.rst
    :start-line: 16

.. toctree::
   :maxdepth: 2

   installation
   usage
   {{ cookiecutter.package_name }}
   contributing
   authors
   history

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

