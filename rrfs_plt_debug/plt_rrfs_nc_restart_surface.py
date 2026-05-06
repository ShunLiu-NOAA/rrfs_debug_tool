#!/usr/bin/env python3

import os
import yaml
import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from matplotlib.gridspec import GridSpec
from matplotlib import colors

# Changed: Added optional arguments highlight_lons, highlight_lats
def plot_world_map(lon, lat, data, cyctime, highlight_lons=None, highlight_lats=None):
    # Set up the map background with cartopy
    extent = [-176., 0., 0.5, 45.] # lonw, lone, lats, latn
    myproj = ccrs.Orthographic(central_longitude=-114, central_latitude=54.0, globe=None)

    # Plot generic world map
    fig = plt.figure(figsize=(24, 20))
    gs = GridSpec(24, 20, wspace=0.0, hspace=0.0)
    ax = fig.add_subplot(gs[0:24, 0:20], projection=myproj)
    ax.set_extent(extent)

    fline_wd = 0.5  # line width
    falpha = 0.5    # transparency
    back_res = '50m'

    # Add Map Features
    coastlines = cfeature.NaturalEarthFeature('physical', 'coastline', back_res,
                                              edgecolor='black', facecolor='none',
                                              linewidth=fline_wd, alpha=falpha)
    states = cfeature.NaturalEarthFeature('cultural', 'admin_1_states_provinces', back_res,
                                          edgecolor='black', facecolor='none',
                                          linewidth=fline_wd, alpha=falpha)

    # Added low zorder to features so data plots over them if needed
    ax.add_feature(states, zorder=2)
    ax.add_feature(coastlines, zorder=3)

    # Transform main coordinates
    vmin = np.min(data)
    vmax = np.max(data)
    print(f"Data Max and Min: {vmin:.2f}, {vmax:.2f}")
    
    x, y, _ = myproj.transform_points(ccrs.Geodetic(), lon, lat).T
    tmp2m_1 = data.T

    # Define Colors and Bounds
    cmap = colors.ListedColormap([
        'white','skyblue','dodgerblue','mediumblue','lime','limegreen','green',
        'yellow','gold','darkorange','red','firebrick','darkred','fuchsia',
        'darkorchid','purple'
    ])
    
    #bounds = [-3, -2, -1, -0.5, -0.1, 0.1, 0.5, 1, 1.5, 2.0, 3.0, 4.0, 50.0, 100.0, 150.0, 200.0]
    bounds = [-3, -2, -1, -0.5, 160.0, 180.0, 200.0, 210, 220.0, 230.0, 240.0, 250.0, 260.0, 270.0, 280.0, 300.0]
    norm = colors.BoundaryNorm(bounds, cmap.N)

    # Plot Full Data Background
    # Added zorder=1 to keep it at the bottom
    cs = ax.pcolormesh(x, y, tmp2m_1, cmap=cmap, norm=norm, zorder=1)
    cb = fig.colorbar(cs, ax=ax, orientation='horizontal', pad=0.01, aspect=60)

    # =======================================================
    # PLOT THE HIGHLIGHT POINTS (NEW LOGIC)
    # =======================================================
    # If highlight points were passed, plot them on top of the main data
    if highlight_lons is not None and len(highlight_lons) > 0:
        print(f"Highlighting {len(highlight_lons)} anomalous points on the map...")
        
        # Plot them using scatter. 
        # Crucial: zorder must be high to appear above pcolormesh and map features.
        ax.scatter(highlight_lons, highlight_lats, 
                   color='white',   # High-contrast color
                   marker='*',        # Star marker
                   s=5,             # Marker size
                   edgecolor='white', # Outline for visibility
                   linewidth=0.1,
                   transform=ccrs.PlateCarree(), # <--- THIS IS THE CRITICAL FIX
                   zorder=20)          # Force to the top layer

    # Save Output
    plttitle = f"IC_{cyctime}"
    plt.title(plttitle)
    plotname = f"{plttitle}.png"
    
    print(f"Saving plot as: {plotname}")
    plt.savefig(plotname, bbox_inches='tight', dpi=200)
    plt.close('all')

def readfield(rrfsfile, rrfsfile1, cyctime):
    
    # Safely read grid file
    with nc.Dataset(rrfsfile, 'r') as tmpdata:
        lat = tmpdata.variables['grid_latt'][:]
        lon = tmpdata.variables['grid_lont'][:]

    # Safely read restart file
    with nc.Dataset(rrfsfile1, 'r') as tmpdata1:
        #ref = tmpdata1.variables['tsnow_land'][:]
        ref = tmpdata1.variables['tslb'][:]

    # Extract the 2D slice
    #data = ref[0, :, :]
    data1 = ref[0,:, :, :]
    data = data1[0, :, :]

    # =======================================================
    # FIND VALUES <= 200 AND PRINT THEIR LAT/LON LOCATIONS
    # =======================================================
    #y_idx, x_idx = np.where(data >= 350.0)
    y_idx, x_idx = np.where((data > 0.0) & (data <= 170.0))
    num_found = len(y_idx)

    # Initialize variables to hold highlight points, defaulting to None
    hl_lons = None
    hl_lats = None

    if num_found > 0:
        # Changed: Extract specific coordinates for the map function
        hl_lats = lat[y_idx, x_idx]
        hl_lons = lon[y_idx, x_idx]

        print(f"\nFound {num_found} points where tsnow_land <= 200:")
        
        # Limit the print loop to the first 60
        limit = min(num_found, 60)
        for i in range(limit):
            y, x = y_idx[i], x_idx[i]
            val = data[y, x]
            latitude = lat[y, x]
            longitude = lon[y, x]
            
            print(f"Value: {val:.2f} | Index: (y:{y}, x:{x}) | Lat/Lon: ({latitude:.4f}, {longitude:.4f})")
    else:
        print("\nNo values found less than or equal to 200.")

    print("\nGenerating map...")
    # Changed: Pass highlight points to map function (will pass None if nothing found)
    plot_world_map(lon, lat, data, cyctime, hl_lons, hl_lats)


if __name__ == "__main__":
    
    # Read Configuration
    # (Assuming you have this file: config_rrfs_nc_restart_surface.yaml)
    with open("config_rrfs_nc_restart_surface.yaml", 'r') as stream:
        config = yaml.safe_load(stream)

    fldir = config['paths']['inputdir']
    restartfile = config['restartfile']
    gridfile = config['gridfile']
    cyctime = config['cyctime']

    # Create directory safely
    os.makedirs(str(cyctime), exist_ok=True)
    
    rrfsfile = gridfile
    rrfsfile1 = os.path.join(fldir, restartfile)
    
    print(f"Grid file: {rrfsfile}")
    print(f"Data file: {rrfsfile1}")
    
    # Execute primary logic
    readfield(rrfsfile, rrfsfile1, cyctime)
