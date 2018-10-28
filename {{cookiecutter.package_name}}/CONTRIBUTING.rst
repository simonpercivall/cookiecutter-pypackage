============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given. 

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs {% if cookiecutter.vcs_url -%}
at {{ cookiecutter.vcs_url }}.{% else -%}
to {{ cookiecutter.email }}{% endif %}

If you are reporting a bug, please include:

* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

{% if "github.com" in cookiecutter.vcs_url -%}
Look through the GitHub issues for bugs. Anything tagged with "bug"
is open to whoever wants to implement it.{% else -%}
Contact the author for more information.
{%- endif %}

Implement Features
~~~~~~~~~~~~~~~~~~

{% if "github.com" in cookiecutter.vcs_url -%}
Look through the GitHub issues for features. Anything tagged with "feature"
is open to whoever wants to implement it.{% else -%}
Contact the author if you've implemented something useful.
{%- endif %}

Write Documentation
~~~~~~~~~~~~~~~~~~~

{{ cookiecutter.project_name }} could always use more documentation, whether as part of the 
official {{ cookiecutter.project_name }} docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue 
{%- if "github.com" in cookiecutter.vcs_url -%}
at {{ cookiecutter.vcs_url }}/issues.
{%- else -%}to the author.
{%- endif %}

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up `{{ cookiecutter.package_name }}` for local development.

1. Check out the repository.

5. When you're done making changes, check that your changes pass flake8 and the tests, including testing other Python versions with tox::

    $ flake8 {{ cookiecutter.package_name }} tests
    $ python setup.py test
    $ tox

   To get flake8 and tox, just pip install them into your virtualenv. 

6. Commit and send the patch or create a pull request.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
3. The pull request should work for Python 2.7, and 3.3.
