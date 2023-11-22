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

def readfield(rrfsfile,rrfsfile1):
    tmpdata1 = nc.Dataset(rrfsfile,'r')
    tmpdata2 = nc.Dataset(rrfsfile1,'r')

#   for varname in tmpdata1.variables.keys():
    ref1 = tmpdata1.variables['ref_f3d'][:]
    ref2 = tmpdata2.variables['ref_f3d'][:]

    #arrayshape=[2700, 3950]
    ref13d=ref1[0,:,:,:]
    ref23d=ref2[0,:,:,:]


    for i in range(0,65):
      ref12d=ref13d[i,:,:]
      ref22d=ref23d[i,:,:]
      print('%3d    max1 %6.2f, max2 %6.2f,     min1 %6.2f, min2 %6.2f,      avg1 %6.2f,  avg1 %6.2f,      diff, %6.2f '%(i,np.max(ref12d),np.max(ref22d), \
                         np.min(ref12d),np.min(ref22d),np.average(ref12d),np.average(ref22d),np.max(ref12d-ref22d)))

if __name__ == "__main__":

    stream = open("config_rrfs_restart_levdiff.yaml", 'r')
    config = yaml.safe_load(stream)

    fldir=config['paths']['inputdir']
    fldir1=config['paths']['inputdir1']
    filename=config['filename']
    filename1=config['filename1']

    rrfsfile=fldir+"/"+filename
    rrfsfile1=fldir1+"/"+filename1
    print(rrfsfile)
    readfield(rrfsfile,rrfsfile1)
    exit()
