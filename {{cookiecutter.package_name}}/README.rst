{{ '=' * (cookiecutter.project_name|count) }}
{{ cookiecutter.project_name }}
{{ '=' * (cookiecutter.project_name|count) }}

.. This is an example of how the readme could be decorated with badges.
    .. image:: https://badge.fury.io/py/{{ cookiecutter.package_name }}.png
        :target: http://badge.fury.io/py/{{ cookiecutter.package_name }}

    .. image:: https://travis-ci.org/<your github username>/{{ cookiecutter.package_name }}.png?branch=master
        :target: https://travis-ci.org/<your github username>/{{ cookiecutter.package_name }}

    .. image:: https://pypip.in/d/{{ cookiecutter.package_name }}/badge.png
        :target: https://crate.io/packages/{{ cookiecutter.package_name }}?version=latest


{{ cookiecutter.project_short_description}}

* Free software: BSD license
* Documentation: http://{{ cookiecutter.package_name }}.rtfd.org.

Features
--------

* TODO
