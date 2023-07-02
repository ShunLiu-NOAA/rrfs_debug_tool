#!/bin/env/python
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import mpl_toolkits
from matplotlib import colors
mpl_toolkits.__path__.append('/gpfs/dell2/emc/modeling/noscrub/gwv/py/lib/python/basemap-1.2.1-py3.6-linux-x86_64.egg/mpl_toolkits/')
from mpl_toolkits.basemap import Basemap, maskoceans, cm
#import cartopy.crs as ccrs
#import cartopy.feature as cfeature
import netCDF4 as nc
import numpy as np
import argparse
import glob
import os
import pandas as pd
import yaml
import ncepy

def plot_world_map(lon, lat, data, plotpath,cychr,thisdir):
    # plot generic world map
    fig = plt.figure(figsize=(12,12))
    #ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree(central_longitude=240))
    ax = fig.add_subplot(1, 1, 1)

# NA domain
    llcrnrlon = -161.0
    llcrnrlat = 8.5
    urcrnrlon = -22.75
    urcrnrlat = 40.25

#CONUS domain
    llcrnrlon=272.5
    urcrnrlon=281.6
    llcrnrlat=38.0
    urcrnrlat=42.5
    lat_0 = 45.0
    lon_0 = -98.0
    lat_ts = 30.0

#domain
    dom="conus"
    llcrnrlon,llcrnrlat,urcrnrlon,urcrnrlat,res=ncepy.corners_res(dom)    

#   m = Basemap(ax=ax,projection='stere',lat_ts=lat_ts,lat_0=lat_0,lon_0=lon_0,\
#                 llcrnrlon=llcrnrlon, llcrnrlat=llcrnrlat,\
#                 urcrnrlon=urcrnrlon,urcrnrlat=urcrnrlat,\
#                 rsphere=6371229,resolution='l')
    m = Basemap(llcrnrlon=llcrnrlon,llcrnrlat=llcrnrlat,urcrnrlon=urcrnrlon,urcrnrlat=urcrnrlat,\
   	      rsphere=(6378137.00,6356752.3142),\
   	      resolution=res,projection='lcc',\
   	      lat_1=30.0,lon_0=-98.0,ax=ax)

    m.fillcontinents(color='LightGrey',zorder=0)
    m.drawcoastlines(linewidth=0.75)
    m.drawstates(linewidth=0.5)
    m.drawcountries(linewidth=0.5)

    data=data
    vmin=np.min(data)
    vmax=np.max(data)
    print(vmin, vmax)
    x,y = m(lon,lat)
    tmp2m_1=data

    cmap = colors.ListedColormap(['white','lightgray','gray','skyblue','dodgerblue','mediumblue',\
               'lime','limegreen','green','yellow','gold','darkorange','red','firebrick',\
               'darkred','fuchsia','darkorchid','black'])

#   bounds=[0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80]
#   bounds=[0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80]

    maxmark=72
    intv=int(maxmark)/18
    print(intv)
    maxmark=76
    bounds=range(0,int(maxmark),int(intv))
    print(bounds)

    norm = colors.BoundaryNorm(bounds, cmap.N)

    cs = m.pcolormesh(x, y, tmp2m_1,cmap=cmap,norm=norm)
    cb = m.colorbar(cs, location='bottom',pad=0.05,extend='both')

    plttitle="cref_"+cychr
    plt.title(plttitle)
    plotname=thisdir+"/"+plttitle+".png"
    plt.savefig(plotname,bbox_inches='tight',dpi=100)
    plt.close('all')

def write_to_nc(lon,lat,data,out_nc_file):
    outnc=nc.Dataset(out_nc_file,'w',format="NETCDF4")
    arrayshape=lat.shape
    nx=arrayshape[0]
    ny=arrayshape[1]
    print(nx,ny)
    outnc.createDimension('nx',nx)
    outnc.createDimension('ny',ny)
    outnc.createVariable("lon",'f',('nx','ny'))
    outnc.createVariable("lat",'f',('nx','ny'))
    outnc.createVariable("data",'f',('nx','ny'))
    outnc.variables['lon'][:]=lon
    outnc.variables['lat'][:]=lat
    outnc.variables['data'][:]=data
    outnc.close()

def readfield(rrfsfile,out_nc_file,cychr,thisdir):
    tmpdata = nc.Dataset(rrfsfile,'r')
    lat = tmpdata.variables['lat'][:]
    lon = tmpdata.variables['lon'][:]
    ref = tmpdata.variables['refl_10cm'][:]
    arrayref=ref.shape
    arrayshape=lat.shape
    print(ref.shape)
    print(lat.shape)
    print(lon.shape)

    ref3d=ref[0,:,:,:]

    plotpath ='ref_i_small.png'
    data=np.empty(arrayshape)
    data=ref3d.max(axis=0)
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

    write_to_nc(lon1,lat1,data1,out_nc_file)
    
    plot_world_map(lon1, lat1, data1, plotpath, cychr,thisdir)

def readfield2d(rrfsfile,out_nc_file,cychr,thisdir):
    tmpdata = nc.Dataset(rrfsfile,'r')
    lat = tmpdata.variables['lat'][:]
    lon = tmpdata.variables['lon'][:]
    hgtsfc = tmpdata.variables['hgtsfc'][:]
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

    write_to_nc(lon1,lat1,data1,out_nc_file)


if __name__ == "__main__":

    stream = open("config_rrfs_his_nc.yaml", 'r')
    config = yaml.safe_load(stream)

    fldir=config['paths']['inputdir']
    filename=config['filename']
    outfile=config['out_nc_file']
    cyctime=config['cyctime']
    #hpc=config['hpc']
    #nmem=config['nmember']

    cmd="mkdir "+str(cyctime) 
    thisdir="./"+str(cyctime)
    os.system(cmd)
    cmd="pwd"
    os.system(cmd)
    for ifhr in range(0,1):
      hr=str(ifhr).zfill(3)
      cychr=str(cyctime)+"_f"+hr
      out_nc_file=thisdir+"/"+outfile+"_"+str(cyctime)+"_f"+hr+".nc"
      rrfsfile=fldir+"/"+filename[0:4]+hr+".nc"
      print(out_nc_file)
      print(rrfsfile)
      readfield2d(rrfsfile,out_nc_file,cychr,thisdir)
