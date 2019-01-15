# -*- coding: utf-8 -*-

"""
This module holds the colormap definitions for sea ice parameters
"""

from matplotlib.colors import LinearSegmentedColormap
import cmocean

cmap_names = ["sit", "sit_thin", "sic"]

# --- Sea Ice Thickness colormaps ---

# Default sea ice thickness colormap (crossover of plt.cm.plasma and cmocean.cm.thermal)
sit_cmap_list = [(0.010, 0.008, 0.200),
                 (0.080, 0.021, 0.595),
                 (0.165, 0.035, 0.708),
                 (0.257, 0.054, 0.784),
                 (0.380, 0.093, 0.729),
                 (0.500, 0.167, 0.664),
                 (0.650, 0.241, 0.582),
                 (0.746, 0.315, 0.501),
                 (0.811, 0.392, 0.433),
                 (0.858, 0.472, 0.376),
                 (0.905, 0.559, 0.318),
                 (0.936, 0.632, 0.261),
                 (0.957, 0.724, 0.240),
                 (0.976, 0.793, 0.251),
                 (0.983, 0.861, 0.302),
                 (0.990, 0.925, 0.401),
                 (0.993, 0.971, 0.659),
                 (0.997, 0.991, 0.909)]

sit = LinearSegmentedColormap.from_list("sit", sit_cmap_list)


# Thin ice colormap
sit_thin = cmocean.cm.dense_r


# --- Sea Ice Concentration colormaps ---

sic = cmocean.cm.ice


