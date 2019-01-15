# -*- coding: utf-8 -*-

""" """

__all__ = ["cm", "norm"]

try:
    from . import cm, norm
except ValueError:
    import cm, norm

import numpy as np
import matplotlib.pyplot as plt

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


def cmseaice_examples():

    n = 100
    x = np.linspace(0, 1, n)
    xx, yy = np.meshgrid(x, x)
    grid = np.flipud(xx+yy)/2.

    # for typical sea ice thickness on a coarse space-time grid
    # (thickness range 0-4 m)
    plt.figure("Regular sea ice thickness on space-time grid")
    plt.imshow(grid*4, cmap=cm.sit, norm=norm.sit)
    plt.axis("off")
    plt.colorbar()
    plt.show(block=False)

    # for thin sea ice thickness on a coarse space-time grid
    # (thickness range 0-1 m)
    plt.figure("Thin sea ice thickness on space-time grid")
    plt.imshow(grid, cmap=cm.sit_thin, norm=norm.sit_thin)
    plt.colorbar()
    plt.axis("off")
    plt.show(block=False)

    plt.figure("Sea ice concentration on space-time grid")
    plt.imshow(grid*100., cmap=cm.sic, norm=norm.sic)
    plt.colorbar()
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    cmseaice_examples()