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

def plot_world_map(lon, lat, data, plotpath,cychr,thisdir,varname):

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

# plot generic world map
    figL=60
    figH=50
    fig = plt.figure(figsize=(figL,figH))
    gs = GridSpec(figL,figH,wspace=0.0,hspace=0.0)
    ax = fig.add_subplot(gs[0:figL,0:figH], projection=myproj)
    ax.set_extent(extent)
#   ax.stock_img()
    axes = [ax]

    fline_wd = 0.5  # line width
    fline_wd_lakes = 0.35  # line width
    falpha = 0.5    # transparency

  # natural_earth
    back_res='50m'
    back_img='off'
#   land=cfeature.NaturalEarthFeature('physical','land',back_res,
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

    #data=data
    vmin=np.min(data)
    vmax=np.max(data)
    print(vmin, vmax)
    x, y,_ = myproj.transform_points(ccrs.Geodetic(), lon, lat).T
    tmp2m_1=data.T
    tmp2m_1=tmp2m_1
    print("max and min:",vmin,vmax)

#   cmap = colors.ListedColormap(['white','lightgray','gray','skyblue','dodgerblue','mediumblue',\
#              'lime','limegreen','green','yellow','gold','darkorange','red','firebrick',\
#              'darkred','fuchsia','darkorchid','black'])
#   cmap = colors.ListedColormap(['white','gray','skyblue','dodgerblue','mediumblue',\
#              'lime','limegreen','green','yellow','gold','darkorange','red','firebrick',\
#              'darkred','fuchsia','darkorchid','black'])

#   bounds=[0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80]

    vmin=np.min(data)
    vmax=np.max(data)
#   intv=nint(maxmark)/18
#   print(intv)
#   #maxmark=76
#   bounds=range(0,int(maxmark),int(intv))
#   print(bounds)

#   norm = colors.BoundaryNorm(bounds, cmap.N)

    cmap='bwr'
    print(vmin)
    print(vmax)

#   cs = ax.pcolormesh(x, y, tmp2m_1,cmap=cmap,norm=norm)
    cs = ax.pcolormesh(x, y, tmp2m_1,vmin=vmin,vmax=vmax,cmap=cmap)
    #cb = fig.colorbar(cs, ax=ax, location='bottom',pad=0.05,extend='both')

#   cbar_ax = fig.add_axes([0.09, 0.06, 0.84, 0.02])
    cb = fig.colorbar(cs, ax=ax, orientation='horizontal',pad=0.01, aspect=40)

    tick_font_size = 25
    cb.ax.tick_params(labelsize=tick_font_size)

    plttitle=varname+cychr
    plt.title(plttitle)
    #plotname=thisdir+"/"+plttitle+".png"
    plotname=plttitle+".png"
    print(plotname)
    plt.savefig(plotname,bbox_inches='tight',dpi=100)
    plt.close('all')

def readfield(gridfile,rrfsfile1,rrfsfile2,varname):
    tmpdata = nc.Dataset(gridfile,'r')
    lat = tmpdata.variables['grid_latt'][:]
    lon = tmpdata.variables['grid_lont'][:]
    arrayshape=lat.shape

    tmpdata1 = nc.Dataset(rrfsfile1,'r')
    ref = tmpdata1.variables[varname][:]
    arrayref=ref.shape
    ref3d=ref[0,:,:,:]

    tmpdata2 = nc.Dataset(rrfsfile2,'r')
    ref2 = tmpdata2.variables[varname][:]
    ref3d2=ref2[0,:,:,:]

    data=ref3d[55,:,:]-ref3d2[55,:,:]
    #data=np.amax(ref3d,axis=0)
    print(data.shape)

#   for i in range(0,65):
#     t2d=ref3d[i,:,:]-ref3d2[i,:,:]
#     print(np.max(t2d),np.max(ref3d[i,:,:]),np.max(ref3d2[i,:,:]))
#     ref2d=ref3d[i,:,:]
#     sp2d=sp3d[i,:,:]
#     print('%s ref %s, sphum %s, T, %s '%(i,np.max(ref2d),np.max(sp2d), np.max(t2d)))
#   exit()
   
    plotpath='./'
    cychr='00'
    thisdir='./'
    plot_world_map(lon, lat, data, plotpath, cychr,thisdir,varname)
    exit()

if __name__ == "__main__":

    stream = open("config_rrfs_increment.yaml", 'r')
    config = yaml.safe_load(stream)

    fldir1=config['paths1']['inputdir1']
    restartfile1=config['paths1']['restart1']
    fldir2=config['paths2']['inputdir2']
    restartfile2=config['paths2']['restart2']

    gridfile=config['gridfile']
    cyctime=config['cyctime']
    varname=config['varname']

    rrfsfile1=fldir1+"/"+restartfile1
    rrfsfile2=fldir2+"/"+restartfile2
    print(rrfsfile1)
    print(rrfsfile2)
    readfield(gridfile,rrfsfile1,rrfsfile2,varname)
    exit()
