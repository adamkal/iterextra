# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'An extension to Python standard library itertools',
    'author': 'Adam Kaliński',
    'url': 'https://github.com/code22/iterextra',
    'download_url': 'https://github.com/code22/iterextra/archive/master.zip',
    'version': '0.1.1',
    'install_requires': ['nose'],
    'packages': ['iterextra'],
    'scripts': [],
    'name': 'iterextra'
}

setup(**config)
