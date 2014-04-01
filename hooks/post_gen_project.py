#!/usr/bin/env python
from __future__ import print_function
import sys
import os
import functools


libjoin = functools.partial(os.path.join, 'lib')
testsjoin = functools.partial(os.path.join, 'tests')


def main(argv):
    # find the package
    for item in os.listdir('lib'):
        if os.path.isfile(libjoin(item, '__init__.py')):
            break
    else:
        return 1

    # it's not a namespace package, all okay
    if not '.' in item:
        return

    package_name = item

    # make the hierarchy
    parts = package_name.split('.')
    os.makedirs(libjoin(*parts[:-1]))
    os.rename(libjoin(package_name), libjoin(*parts))

    # put __init__.py on every step except for the last
    for i in range(1, len(parts)):
        with open(libjoin(*parts[:i] + ['__init__.py']), 'w') as f:
            f.write("__import__('pkg_resources').declare_namespace(__name__)\n")

    # rename the test file
    test_file_name = testsjoin('test_%s.py' % package_name)
    if os.path.isfile(test_file_name):
        base, ext = os.path.splitext(test_file_name)
        base = base.replace('.', '_')
        os.rename(test_file_name, base + ext)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
