#!/usr/bin/env python
# encoding: utf-8

from setuptools import setup, find_packages

setup(
    name='compress',
    version='1.0',
    description='Compress ',
    author='Andrew Ning',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    entry_points={
        'console_scripts': [
          'sortphotos = src.sortphotos:main',
        ]
      }
)

