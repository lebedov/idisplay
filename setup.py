#!/usr/bin/env python

import os
import re

from setuptools import find_packages
from setuptools import setup

NAME =               'idisplay'
VERSION =            '0.1.2'
AUTHOR =             'Lev Givon'
AUTHOR_EMAIL =       'lev@columbia.edu'
URL =                'https://github.com/lebedov/idisplay/'
DESCRIPTION =        'IPython rich display magic functions'
with open('README.rst', 'r') as f:
    LONG_DESCRIPTION = f.read()
LONG_DESCRIPTION = re.search('.*(^Package Description.*)', LONG_DESCRIPTION, re.MULTILINE|re.DOTALL).group(1)
DOWNLOAD_URL =       URL
LICENSE =            'BSD'
CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development']
PACKAGES =           find_packages()

if __name__ == "__main__":
    if os.path.exists('MANIFEST'):
        os.remove('MANIFEST')

    setup(
        name = NAME,
        version = VERSION,
        author = AUTHOR,
        author_email = AUTHOR_EMAIL,
        license = LICENSE,
        classifiers = CLASSIFIERS,
        description = DESCRIPTION,
        long_description = LONG_DESCRIPTION,
        url = URL,
        packages = find_packages(),
        install_requires = ['ipython>=1.0'])
