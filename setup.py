#!/usr/bin/env python3

# @Author: George Onoufriou <georgeraven>
# @Date:   2018-09-05
# @Filename: setup.py
# @Last modified by:   georgeraven
# @Last modified time: 2019-01-09
# @License: Please see LICENSE file in project root

import subprocess as sp

from setuptools import find_namespace_packages, find_packages, setup

# getting version from git as this is vcs
runArgs = ["git", "describe", "--long"]
version = sp.run(runArgs, stdout=sp.PIPE).stdout.decode("utf-8")

with open("README.md", "r") as fh:
    readme = fh.read()

setup(
    name="tosv",
    version=str(version),
    description="A simple delimited file type converter",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="George Onoufriou",
    url="https://github.com/DreamingRaven/tosv",
    packages=find_namespace_packages(),
    scripts=['tosv'],
)
