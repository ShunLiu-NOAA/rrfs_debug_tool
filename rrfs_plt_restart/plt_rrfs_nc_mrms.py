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

def plot_world_map(lon, lat, data, plotpath,cychr,thisdir):

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
#   extent = [-176.,0.,0.5,45.] #lonw, lone, lats, latn
#   myproj=ccrs.Orthographic(central_longitude=-114, central_latitude=54.0, globe=None)
    extent = [-126.,-55.,15.5,48.] #lonw, lone, lats, latn
    #extent = [-100.,-80.,25.5,38.] #lonw, lone, lats, latn
    myproj=ccrs.Orthographic(central_longitude=-100, central_latitude=44.0, globe=None)

# plot generic world map
    fig = plt.figure(figsize=(24,20))
    gs = GridSpec(24,20,wspace=0.0,hspace=0.0)
    ax = fig.add_subplot(gs[0:24,0:20], projection=myproj)
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
    cmap = colors.ListedColormap(['white','skyblue','dodgerblue','mediumblue',\
               'lime','limegreen','green','yellow','gold','darkorange','red','firebrick',\
               'darkred','fuchsia','darkorchid','purple'])

    bounds=[0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75]

#   maxmark=72
#   maxmark=36
#   intv=int(maxmark)/18
#   print(intv)
#   #maxmark=76
#   bounds=range(0,int(maxmark),int(intv))
#   print(bounds)

    norm = colors.BoundaryNorm(bounds, cmap.N)

    cs = ax.pcolormesh(x, y, tmp2m_1,cmap=cmap,norm=norm)
    #cb = fig.colorbar(cs, ax=ax, location='bottom',pad=0.05,extend='both')
    cb = fig.colorbar(cs, ax=ax, orientation='horizontal',pad=0.01,aspect=60)

    plttitle = f"cref_{cyctime}"
    plt.title(plttitle)
    #plotname=thisdir+"/"+plttitle+".png"
    plotname=plttitle+".png"
    print(plotname)
    plt.savefig(plotname,bbox_inches='tight',dpi=200)
    plt.close('all')

def readfield(rrfsfile,rrfsfile1):
    tmpdata = nc.Dataset(rrfsfile,'r')
    lat = tmpdata.variables['grid_latt'][:]
    lon = tmpdata.variables['grid_lont'][:]
    arrayshape=lat.shape

    tmpdata1 = nc.Dataset(rrfsfile1,'r')
    ref = tmpdata1.variables['reflectivity'][:]
    arrayref=ref.shape

    ref3d=ref[:,:,:]
#   lat1=np.empty(arrayshape)
#   lon1=np.empty(arrayshape)
#   data=np.empty(arrayshape)

    #data=ref3d[5,:,:]
    data=np.amax(ref3d,axis=0)
    print(data.shape)

#   for i in range(0,65):
#     t2d=t3d[i,:,:]
#     ref2d=ref3d[i,:,:]
#     sp2d=sp3d[i,:,:]
#     print('%s ref %s, sphum %s, T, %s '%(i,np.max(ref2d),np.max(sp2d), np.max(t2d)))
   
    plotpath='./'
    cychr='00'
    thisdir='./'
    plot_world_map(lon, lat, data, plotpath, cychr,thisdir)
    exit()

def readfield2d(rrfsfile,out_nc_file,cychr,thisdir):
    tmpdata = nc.Dataset(rrfsfile,'r')
    lat = tmpdata.variables['lat'][:]
    lon = tmpdata.variables['lon'][:]
    hgtsfc = tmpdata.variables['hgt_hyblev1'][:]
    arrayshape=lat.shape

    hgt=hgtsfc[0,:,:]

    data=np.empty(arrayshape)
    data=hgt
    #print (data.shape)

    arrayshape=[512,512]
    lat1=np.empty(arrayshape)
    lon1=np.empty(arrayshape)
    data1=np.empty(arrayshape)
#   512x512 domain
    nxs=150
    nys=650
    nint=512

#   1024x1024 domain
#   nxs=150 
#   nys=150
#   nint=1024

    lat1=lat[nxs:nxs+nint,nys:nys+nint]
    lon1=lon[nxs:nxs+nint,nys:nys+nint]
    data1=data[nxs:nxs+nint,nys:nys+nint]
    print(lat1.shape)
    print("max:",np.max(data1))
    print("min:",np.min(data1))

    print("start plot:")
    plotpath="test"
    plot_world_map(lon1, lat1, data1, plotpath, cychr,thisdir)


if __name__ == "__main__":

    global cyctime
    stream = open("config_rrfs_nc_mrms.yaml", 'r')
    config = yaml.safe_load(stream)

    fldir=config['paths']['inputdir']
    restartfile=config['restartfile']
    gridfile=config['gridfile']
    outfile=config['out_nc_file']
    cyctime=config['cyctime']
    #hpc=config['hpc']
    #nmem=config['nmember']

    cmd="mkdir "+str(cyctime) 
    thisdir="./"+str(cyctime)
    #os.system(cmd)
    cmd="pwd"
    #os.system(cmd)
    rrfsfile=gridfile
    rrfsfile1=fldir+"/"+restartfile
    print(rrfsfile)
    readfield(rrfsfile,rrfsfile1)
    exit()
