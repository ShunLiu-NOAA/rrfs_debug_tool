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

def plot_world_map(lon, lat, data, vartype, cychr,thisdir):

# NA domain
    llcrnrlon = -160.0
    llcrnrlat = 15.0
    urcrnrlon = -55.0
    urcrnrlat = 65.0
    cen_lat = 35.4
    cen_lon = -105.0
    xextent = -3700000
    yextent = -2500000
    offset = 1

# set up the map background with cartopy
    extent = [-176.,0.,0.5,45.] #lonw, lone, lats, latn
    myproj=ccrs.Orthographic(central_longitude=-114, central_latitude=54.0, globe=None)

# plot generic world ma p
    fig = plt.figure(figsize=(12,10))
    gs = GridSpec(12,10,wspace=0.0,hspace=0.0)
    ax = fig.add_subplot(gs[0:12,0:8], projection=myproj)
    ax.set_extent(extent)
#    ax.stock_img()
    axes = [ax]

    fline_wd = 0.5  # line width
    fline_wd_lakes = 0.35  # line width
    falpha = 0.5    # transparency

  # natural_earth
    back_res='50m'
    back_img='off'

#  land=cfeature.NaturalEarthFeature('physical','land',back_res,
#                    edgecolor='face',facecolor=cfeature.COLORS['land'],
#                    alpha=falpha)
#   lakes=cfeature.NaturalEarthFeature('physical','lakes',back_res,
#                   edgecolor='black',facecolor='none',
#                   linewidth=fline_wd_lakes,alpha=falpha)
    coastlines=cfeature.NaturalEarthFeature('physical','coastline',
                    back_res,edgecolor='black',facecolor='none',
                    linewidth=fline_wd,alpha=falpha)
    states=cfeature.NaturalEarthFeature('cultural','admin_1_states_provinces',
                    back_res,edgecolor='black',facecolor='none',
                    linewidth=fline_wd,alpha=falpha)
    borders=cfeature.NaturalEarthFeature('cultural','admin_0_countries',
                    back_res,edgecolor='black',facecolor='none',
                    linewidth=fline_wd,alpha=falpha)

# All lat lons are earth relative, so setup the associated projection correct for that data
    transform = ccrs.RotatedPole(pole_longitude=67.0, pole_latitude=35.0)

#   ax.add_feature(lakes)
    ax.add_feature(states)
    ax.add_feature(coastlines)

    data=data
    vmin=np.min(data)
    vmax=np.max(data)
    print(vmin, vmax)
    x, y,_ = myproj.transform_points(ccrs.Geodetic(), lon, lat).T
    tmp2m_1=data

    cmap = colors.ListedColormap(['white','lightgray','gray','skyblue','dodgerblue','mediumblue',\
               'lime','limegreen','green','yellow','gold','darkorange','red','firebrick',\
               'darkred','fuchsia','darkorchid','black'])

    bounds=[0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80]

#   maxmark=72
#   intv=int(maxmark)/18
#   print(intv)
#   maxmark=76
#   bounds=range(0,int(maxmark),int(intv))
#   print(bounds)

    norm = colors.BoundaryNorm(bounds, cmap.N)

#   cs = ax.scatter(x, y, tmp2m_1,s=10, marker='o',cmap=cmap,norm=norm)
    cs = ax.scatter(x, y, s=1, marker='.')
#   cs = ax.pcolormesh(x, y, tmp2m_1,cmap=cmap,norm=norm)
#   cb = m.colorbar(cs, location='bottom',pad=0.05,extend='both')

    plttitle="diag_"+vartype+"_"+cychr
    plt.title(plttitle)
    plotname=thisdir+"/"+plttitle+".png"
    figpath=thisdir+plotname
    plt.savefig(plotname,bbox_inches='tight',dpi=100)
    plt.close('all')

def readobs(diagfile):
    tmpdata = nc.Dataset(diagfile,'r')
    lat = tmpdata.variables['Latitude'][:]
    lon = tmpdata.variables['Longitude'][:]
    return lat, lon


if __name__ == "__main__":

    stream = open("config_rrfs_obs.yaml", 'r')
    config = yaml.safe_load(stream)

    fldir=config['paths']['inputdir']
    filename=config['filename']
    vartype=config['VARTYPE']
    outfile=config['out_nc_file']
    cyctime=config['cyctime']

    obsdir=config['rrfsobs']['inputdir']
    obsconus=config['rrfsobs']['obs_file_name']
    diagconus=obsdir+obsconus

    obsdir=config['rrfsobs']['inputna']
    obsna=config['rrfsobs']['obs_file_na']
    diagna=obsdir+obsna

    cmd="mkdir "+str(cyctime) 
    thisdir="./"+str(cyctime)
    os.system(cmd)
    cmd="pwd"
    os.system(cmd)

    cychr="conus"
    latconus, lonconus = readobs(diagconus)
    dataconus=lonconus
    plot_world_map(lonconus, latconus, dataconus, vartype, cychr, thisdir) 
    cychr="na"
    latna, lonna = readobs(diagna)
    datana=lonna
    plot_world_map(lonna, latna, datana, vartype, cychr, thisdir) 
