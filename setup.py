#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

with open("README.md") as readme_file:
    readme = readme_file.read()

install_requirements = [
    "sceptre>=2.0"
]

setup(
    name='sceptre-boilerplate-resolver',
    version="0.1",
    description="A Sceptre boilerplate resolver",
    py_modules=['main'],
    long_description=readme,
    long_description_content_type="text/markdown",
    author="",
    author_email="",
    license='Apache2',
    url="",
    entry_points={
        'sceptre.resolvers': [
            'main = main:Main',
        ],
    },
    keywords="sceptre",
    install_requires=install_requirements,
    include_package_data=True,
    zip_safe=False,
)
