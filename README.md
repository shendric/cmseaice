# cmseaice

Colormaps for visualizing sea ice thickness and other sea ice parameters with matplotlib. Inspired and depending on cmocean (https://matplotlib.org/cmocean/).


Example usage:

    import cmseaice
    
    # for typical sea ice thickness on a coarse space-time grid
    # (thickness range 0-4 m)
    plt.figure()
    plt.imshow(some_sit_grid, cmap=cmseaice.cm.sit, norm=cmseaice.norm.sit)
    plt.show()
    
    # for thin sea ice thickness on a coarse space-time grid
    # (thickness range 0-1 m)
    plt.figure()
    plt.imshow(some_thinsit_grid, cmap=cmseaice.cm.sit_thin, norm=cmseaice.norm.sit_thin)
    plt.show()