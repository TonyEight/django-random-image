#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from setuptools import setup, find_packages
 
import random_image
 

setup(
 
    name='django_random_image',
 
    version=random_image.__version__,
 
    packages=find_packages(),
 
    author="TonyEight",
 
    author_email="ludoic.legendart@gmail.com",
 
    description="A simple tag that get you a random image URL from the specified directory under STATIC ROOT",

    long_description=open('README.rst').read(),
 
    include_package_data=True,

    url='https://github.com/TonyEight/django-random-image',
 
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Topic :: Django Template Tag",
    ],
 
)
