#!/bin/env/python

import pyproj
import cartopy.crs as ccrs
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import matplotlib
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

def readfield(rrfsfile,rrfsfile1,rrfsfile2):
    tmpdata = nc.Dataset(rrfsfile,'r')
    #lat = tmpdata.variables['lat'][:]
    #lon = tmpdata.variables['lon'][:]
    ref = tmpdata.variables['ref_f3d'][:]
    arrayref=ref.shape
    #arrayshape=lat.shape
    print(ref.shape)
    #print(lat.shape)
    #print(lon.shape)

    ref3d=ref[0,:,:,:]
    arrayshape=[2700, 3950]
    data=np.empty(arrayshape)

    tmpdata1 = nc.Dataset(rrfsfile1,'r')
    t4d=tmpdata1.variables['T'][:]
    t3d=t4d[0,:,:,:]

    tmpdata2 = nc.Dataset(rrfsfile2,'r')
    sp4d=tmpdata2.variables['sphum'][:]
    sp3d=sp4d[0,:,:,:]

    for i in range(0,65):
      t2d=t3d[i,:,:]
      ref2d=ref3d[i,:,:]
      sp2d=sp3d[i,:,:]
      print('%s ref %s, sphum %s, T, %s '%(i,np.max(ref2d),np.max(sp2d), np.max(t2d)))

if __name__ == "__main__":

    stream = open("config_rrfs_restart_levmax.yaml", 'r')
    config = yaml.safe_load(stream)

    fldir=config['paths']['inputdir']
    filename=config['filename']
    filename1=config['filename1']
    filename2=config['filename2']

    rrfsfile=fldir+"/"+filename
    rrfsfile1=fldir+"/"+filename1
    rrfsfile2=fldir+"/"+filename2
    print(rrfsfile)
    readfield(rrfsfile,rrfsfile1,rrfsfile2)
    exit()
