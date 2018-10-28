#!/usr/bin/env python
from __future__ import print_function
import re
import sys


MODULE_REGEX = re.compile(r'^[_a-zA-Z][_a-zA-Z0-9]+$')
package_name = '{{ cookiecutter.package_name }}'

for part in package_name.split('.'):
    if not MODULE_REGEX.match(part):
        print('ERROR: %s is not a valid Python package name!' % package_name)
        sys.exit(1)
