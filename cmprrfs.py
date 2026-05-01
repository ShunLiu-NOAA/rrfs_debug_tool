#!/usr/bin/env python3
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import mpl_toolkits
#mpl_toolkits.__path__.append('/gpfs/dell2/emc/modeling/noscrub/gwv/py/lib/python/basemap-1.2.1-py3.6-linux-x86_64.egg/mpl_toolkits/')
#from mpl_toolkits.basemap import Basemap, maskoceans
#import cartopy.crs as ccrs
#import cartopy.feature as cfeature
import netCDF4 as nc
import numpy as np
import argparse
import glob
import os
import pandas as pd

import netCDF4 as nc
import numpy as np


def readfield(file1, file2):

    # 1. Read first file
    tmpdata = nc.Dataset(file1, 'r')
    u = tmpdata.variables['u'][:]
    v = tmpdata.variables['v'][:]
    W = tmpdata.variables['W'][:]
    T = tmpdata.variables['T'][:]
    delp = tmpdata.variables['delp'][:]
    tmpdata.close()

    # 2. Read second file
    tmpdata = nc.Dataset(file2, 'r')
    u1 = tmpdata.variables['u'][:]
    v1 = tmpdata.variables['v'][:]
    W1 = tmpdata.variables['W'][:]
    T1 = tmpdata.variables['T'][:]
    delp1 = tmpdata.variables['delp'][:]
    tmpdata.close()

    # ==========================================
    # 3. HELPER FUNCTION
    # ==========================================
    def print_diff_stats(var_name, var_base, var_compare):
        # Calculate raw difference and absolute difference
        result = np.subtract(var_base, var_compare)
        abs_diff = np.abs(result)
        
        # Find maximum absolute difference and its location
        max_abs_diff = np.max(abs_diff)
        max_loc = np.unravel_index(np.argmax(abs_diff), abs_diff.shape)
        
        # Print results neatly
        print(f"{var_name} diff sum:: {np.sum(result)}")
        print(f"{var_name} max abs diff:: {max_abs_diff} at index {max_loc}")
        print("-" * 40) # Adds a separator line for readability

    # ==========================================
    # 4. EXECUTE FOR ALL VARIABLES
    # ==========================================
    print_diff_stats("u", u, u1)
    print_diff_stats("v", v, v1)
    print_diff_stats("T", T, T1)
    print_diff_stats("delp", delp, delp1)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument('-file1', '--file1', help="rrfs file1", required=True)
    ap.add_argument('-file2', '--file2', help="rrfs file2", required=True)
    MyArgs = ap.parse_args()
    readfield(MyArgs.file1,MyArgs.file2)
