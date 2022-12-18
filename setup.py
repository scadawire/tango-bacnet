#!/usr/bin/env python3

try:
    from setuptools import setup
except ImportError:
    print('Can\' t find setuptools.')
    from distutils.core import setup

setup(name='BACnetDS',
      version='0.9',
      description='DS for communicating with devices via BACnet.',
      author='Wojciech Kitka',
      author_email='kitka.wojciech@gmail.com',
      packages=['bacnetds'],
      package_dir={'bacnetds': 'src'},
      scripts=['scripts/BACnetDS'], )