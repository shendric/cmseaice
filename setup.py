# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import os

# Get the readme
with open('README.md') as f:
    readme = f.read()

# Get the licence
with open('LICENSE') as f:
    license = f.read()

# Get the version
mypackage_root_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(mypackage_root_dir, "cmseaice", 'VERSION')) as version_file:
    version = version_file.read().strip()

# Package requirements
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name='cmseaice',
    version=version,
    description='Colormaps for visualizing sea ice thickness and other sea ice parameters',
    long_description=readme,
    author='Stefan Hendricks',
    author_email='stefan.hendricks@awi.de',
    url='https://github.com/shendric/cmseaice',
    license=license,
    install_requires=requirements,
    packages=find_packages(exclude=('tests', 'docs')),
    include_package_data=True,
)