# -*- coding: utf-8 -*-

""" """

__all__ = ["cm", "norm"]

import warnings
warnings.filterwarnings("ignore")

import os
import sys
from distutils import log
log.set_verbosity(log.INFO)
log.set_threshold(log.INFO)

# Get version from VERSION in package root
PACKAGE_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
try:
    version_file = open(os.path.abspath(os.path.join(PACKAGE_ROOT_DIR, "VERSION")))
    with version_file as f:
        version = f.read().strip()
except IOError:
    sys.exit("Cannot find VERSION file in package (expected: VERSION in lib root)")

# Package Metadata
__version__ = version
__author__ = "Stefan Hendricks"
__author_email__ = "stefan.hendricks@awi.de"