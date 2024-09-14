#!/bin/env/python

import pyproj
import cartopy.crs as ccrs
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import cartopy.feature as cfeature
import matplotlib
import io
import matplotlib.pyplot as plt
from PIL import Image
import matplotlib.image as image
from matplotlib.gridspec import GridSpec
from matplotlib import colors
import numpy as np
import time,os,sys,multiprocessing
import multiprocessing.pool

import ncepy
from scipy import ndimage
#from netCDF4 import Dataset
import cartopy
from datetime import datetime

import netCDF4 as nc
import numpy as np
import argparse
import glob
import os
import pandas as pd
import yaml
import ncepy

def plot_world_map(lon, lat, data, plotpath, cychr, thisdir):
# NA domain
    #extent = [-176., 0., 0.5, 45.]
    #myproj = ccrs.Orthographic(central_longitude=-114, central_latitude=54.0)
    extent = [-100.,-80.,25.5,38.] #lonw, lone, lats, latn
    myproj=ccrs.Orthographic(central_longitude=-100, central_latitude=44.0, globe=None)

    fig = plt.figure(figsize=(36, 30))
    gs = GridSpec(36, 30, wspace=0.0, hspace=0.0)
    ax = fig.add_subplot(gs[0:36, 0:30], projection=myproj)
    ax.set_extent(extent)
    
    fline_wd = 0.5
    falpha = 0.5
    back_res = '50m'

    coastlines = cfeature.NaturalEarthFeature('physical', 'coastline',
                                              back_res, edgecolor='black', facecolor='none',
                                              linewidth=fline_wd, alpha=falpha)
    states = cfeature.NaturalEarthFeature('cultural', 'admin_1_states_provinces',
                                          back_res, edgecolor='black', facecolor='none',
                                          linewidth=fline_wd, alpha=falpha)

    ax.add_feature(states)
    ax.add_feature(coastlines)

    x, y, _ = myproj.transform_points(ccrs.Geodetic(), lon, lat).T

    # Ensure no non-finite values
    x = np.nan_to_num(x, nan=np.nan)
    y = np.nan_to_num(y, nan=np.nan)
    data = np.nan_to_num(data, nan=np.nan)
    data = data.T

    print(f"x shape: {x.shape}, y shape: {y.shape}, z shape: {data.shape}")
    print(f"x has non-finite values: {np.any(~np.isfinite(x))}")
    print(f"y has non-finite values: {np.any(~np.isfinite(y))}")
    print(f"z has non-finite values: {np.any(~np.isfinite(data))}")

    cmap = colors.ListedColormap(['white', 'skyblue', 'dodgerblue', 'mediumblue',
                                  'lime', 'limegreen', 'green', 'yellow', 'gold', 'darkorange',
                                  'red', 'firebrick', 'darkred', 'fuchsia', 'darkorchid', 'purple'])
    bounds = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
    norm = colors.BoundaryNorm(bounds, cmap.N)

    cs = ax.pcolormesh(x, y, data, cmap=cmap, norm=norm, shading='auto')
    cb = fig.colorbar(cs, ax=ax, orientation='horizontal', pad=0.001)

    #plttitle = f"cref_{cychr}"
    plttitle = f"cref_{cyctime}"
    plt.title(plttitle)
    plotname = f"{plttitle}.png"
    plt.savefig(plotname, bbox_inches='tight', dpi=200)
    plt.close('all')

def readoutput(rrfsfile, rrfsfile1):
    tmpdata = nc.Dataset(rrfsfile1, 'r')
    lat1 = tmpdata.variables['lat'][:]
    lon1 = tmpdata.variables['lon'][:]
    data1 = tmpdata.variables['refdmax'][:]

    lat = lat1.filled(np.nan)
    lon = lon1.filled(np.nan)
    data2 = np.amax(data1, axis=0)
    data = data2.filled(np.nan)  # If data2 is a masked array

    plotpath = './'
    cychr = '00'
    thisdir = './'
    plot_world_map(lon, lat, data, plotpath, cychr, thisdir)
    exit()

if __name__ == "__main__":
    global cyctime
    stream = open("config_rrfs_nc_output.yaml", 'r')
    config = yaml.safe_load(stream)

    fldir = config['paths']['inputdir']
    restartfile = config['restartfile']
    gridfile = config['gridfile']
    outfile = config['out_nc_file']
    cyctime = config['cyctime']

    rrfsfile = gridfile
    rrfsfile1 = os.path.join(fldir, restartfile)
    readoutput(rrfsfile, rrfsfile1)
