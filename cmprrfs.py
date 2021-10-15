#!/usr/bin/env python3
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import mpl_toolkits
mpl_toolkits.__path__.append('/gpfs/dell2/emc/modeling/noscrub/gwv/py/lib/python/basemap-1.2.1-py3.6-linux-x86_64.egg/mpl_toolkits/')
from mpl_toolkits.basemap import Basemap, maskoceans
#import cartopy.crs as ccrs
#import cartopy.feature as cfeature
import netCDF4 as nc
import numpy as np
import argparse
import glob
import os
import pandas as pd

def readfield(file1,file2):

    tmpdata = nc.Dataset(file1,'r')
    u = tmpdata.variables['u_s'][:]
    v = tmpdata.variables['v_s'][:]
    W = tmpdata.variables['w'][:]
    T = tmpdata.variables['t'][:]
    delp = tmpdata.variables['delp'][:]
    tmpdata.close()

    tmpdata = nc.Dataset(file2,'r')
    u1 = tmpdata.variables['u_s'][:]
    v1 = tmpdata.variables['v_s'][:]
    W1 = tmpdata.variables['w'][:]
    T1 = tmpdata.variables['t'][:]
    delp1 = tmpdata.variables['delp'][:]
    tmpdata.close()

    result=np.subtract(u, u1)
    print("u diff::", np.sum(result))

    result=np.subtract(v, v1)
    print("v diff::", np.sum(result))

    result=np.subtract(T, T1)
    print("T diff::", np.sum(result))

    result=np.subtract(delp, delp1)
    print("delp diff::", np.sum(result))

#   sphum = tmpdata.variables['sphum'][:]
#   liq_wat = tmpdata.variables['liq_wat'][:]
#   ice_wat = tmpdata.variables['ice_wat'][:]
#   rainwat = tmpdata.variables['rainwat'][:]
#   snowwat = tmpdata.variables['snowwat'][:]
#   graupel = tmpdata.variables['graupel'][:]
#   ice_nc = tmpdata.variables['ice_nc'][:]
#   rain_nc = tmpdata.variables['rain_nc'][:]
#   sgs_tke = tmpdata.variables['sgs_tke'][:]
#   tmpdata.close()


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument('-file1', '--file1', help="rrfs file1", required=True)
    ap.add_argument('-file2', '--file2', help="rrfs file2", required=True)
    MyArgs = ap.parse_args()
    readfield(MyArgs.file1,MyArgs.file2)
