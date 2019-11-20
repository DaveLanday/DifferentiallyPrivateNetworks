#!/usr/bin/env python
# -*-coding: utf-8 -*-
 
#setup.py
#Dave Landay
#LAST UPDATED: 11-19-2019

from setuptools import setup, find_packages
import sys

with open('requirements.txt', 'r') as f:
    required = f.read().splitlines()

setup(version='0.1',
      name='dpNet',
      description='Final project for CS295 data privacy. Implements Lipschitz extensions of differentially private networks',
      author='Dave w. Landay & Samson C. Durst',
      packages=find_packages(),
      install_requires=required)
