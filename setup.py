#!/usr/bin/env python
# -*- coding:utf-8 -*-

# NOTE(StaticCube) Guidelines for Major.Minor.Micro
# - Major means an API contract change
# - Minor means API bugfix or new functionality
# - Micro means change of any kind
#   (unless significant enough for a minor/major).

from setuptools import setup

setup(
  name='python-openmediavault',
  packages=['Openmediavault'],
  version='0.0.1',
  description='Python API for communication with OpenMediaVault, \
    based on SynologyDSM python-synology by FG van Zeelst (StaticCube)',
  author='FG van Zeelst (StaticCube), Oskar Joelsson (orrpan)',
  author_email='',
  url='https://github.com/orrpan/python-openmediavault',
  download_url='https://github.com/orrpan/python-openmediavault/tarball/0.0.1',
  keywords=['openmediavault', 'omv'],
  classifiers=[],
  install_requires=[
    'requests>=1.0.0',
    'flake8>=3.7.7'
    ]
)
