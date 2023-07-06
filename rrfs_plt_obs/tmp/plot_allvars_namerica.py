#!/bin/env/python

import pyproj
import cartopy.crs as ccrs
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import cartopy.feature as cfeature
import matplotlib
#matplotlib.use('Agg')
import io
import matplotlib.pyplot as plt
from PIL import Image
import matplotlib.image as image
from matplotlib.gridspec import GridSpec
import numpy as np
import time,os,sys,multiprocessing
import multiprocessing.pool
import ncepy
from scipy import ndimage
from netCDF4 import Dataset
import cartopy
from datetime import datetime

########################################
#    START PLOTTING FOR EACH DOMAIN    #
########################################

def create_figure():

  # Map corners for each domain

  dom="namerica"
  if dom == 'namerica':
    llcrnrlon = -160.0
    llcrnrlat = 15.0
    urcrnrlon = -55.0
    urcrnrlat = 65.0
    cen_lat = 35.4
    cen_lon = -105.0
    xextent = -3700000
    yextent = -2500000
    offset = 1

  # create figure and axes instances
  fig = plt.figure(figsize=(10,8))
  gs = GridSpec(10,8,wspace=0.0,hspace=0.0)
  im = image.imread('/lfs/h2/emc/lam/noscrub/Benjamin.Blake/python.rrfs/noaa.png')
  par = 1

  # Define where Cartopy maps are located
  cartopy.config['data_dir'] = '/lfs/h2/emc/lam/noscrub/Benjamin.Blake/python/NaturalEarth'

  back_res='50m'
  back_img='off'

  # set up the map background with cartopy
  extent = [-176.,0.,0.5,45.] #lonw, lone, lats, latn
  myproj=ccrs.Orthographic(central_longitude=-114, central_latitude=54.0, globe=None)

  ax1 = fig.add_subplot(gs[0:10,0:8], projection=myproj)
  ax1.set_extent(extent)
  ax1.stock_img()
  axes = [ax1]

  fline_wd = 0.5  # line width
  fline_wd_lakes = 0.35  # line width
  falpha = 0.5    # transparency

  # natural_earth
#  land=cfeature.NaturalEarthFeature('physical','land',back_res,
#                    edgecolor='face',facecolor=cfeature.COLORS['land'],
#                    alpha=falpha)
  lakes=cfeature.NaturalEarthFeature('physical','lakes',back_res,
                    edgecolor='black',facecolor='none',
                    linewidth=fline_wd_lakes,alpha=falpha)
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

# ax1.add_feature(lakes)
  ax1.add_feature(states)
  ax1.add_feature(coastlines)
  
  lats = np.array([37.761659, 47.7405, 27.755100, 57.737167])
  lons = np.array([-114.864466, -115.8671, -112.849660, -112.795714])
  x, y,_ = myproj.transform_points(ccrs.Geodetic(), lons, lats).T
  ax1.scatter(x,y,c='r',s=10,marker='o')

  plttitle = 'Blue: EMC 3km CONUS v.s. Red: GSL 3km CONUS'
  plt.title(plttitle)
  now=datetime.now()
  t=now.strftime("_%Y%m%d%H%M")
  plotpath ='fv3grid'+t+'.png'
  plt.savefig(plotpath,bbox_inches='tight',dpi=100)
  plt.close('all')


if __name__ == "__main__":
  create_figure()

