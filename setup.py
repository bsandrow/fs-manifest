from __future__ import print_function

from glob import glob

try:
    from setuptools import setup
except ImportError:
    print("Falling back to distutils. Functionality may be limited.")
    from distutils.core import setup

long_description = open('README.rst').read() + "\n\n" + open("ChangeLog").read()

config = {
    'name'            : 'fs-manifest',
    'description'     : 'Create a listing of a filesystem.',
    'long_description': long_description,
    'author'          : 'Brandon Sandrowicz',
    'author_email'    : 'brandon@sandrowicz.org',
    'url'             : 'https://github.com/bsandrow/fs-manifest',
    'version'         : '0.1',
    'scripts'         : glob('bin/*'),
    'license'         : open('LICENSE').read(),
}

setup(**config)
