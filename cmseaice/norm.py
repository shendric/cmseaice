# -*- coding: utf-8 -*-

"""
This module holds the norms associated to the colormaps for sea ice parameters
"""

from matplotlib.colors import Normalize


cmap_names = ["sit", "sit_thin", "sic", "sic_unit"]

# --- Sea Ice Thickness ---

# Regular Thickness Range for data on a space-time grid
sit = Normalize(vmin=0.,vmax=4.)

# Thin Thickness Range for data on a space-time grid
sit_thin = Normalize(vmin=0.,vmax=1.)

# --- Sea Ice Concentration ---

# in percent
sic = Normalize(vmin=0.,vmax=100.)  # in percent

# in 0-1 unit
sic_unitval = Normalize(vmin=0.,vmax=1.)  # in percent