#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 09:19:49 2021
"""
import matplotlib
import matplotlib.pyplot as plt
import sys
import numpy as np

#Necessary to generate figs when not running an Xserver (e.g. via PBS)
plt.switch_backend('agg')
matplotlib.style.use('ggplot')

def isfloat(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

if __name__ == '__main__':

  fname=sys.argv[1]   
  #fname='./forecast_out_2021102012.log'
  myptend=[]
  keystrings=['At forecast hour','mean abs pgr change is','hPa/hr']
  with open(fname, 'r') as f:
      for line in f:
          if any(x in line.strip() for x in keystrings):
              myptend.append([float(s) for s in line.split() if isfloat(s)])
  
  dat=np.array(myptend)


  fname1=sys.argv[2]   
  myptend1=[]
  with open(fname1, 'r') as f1:
      for line in f1:
          if any(x in line.strip() for x in keystrings):
              myptend1.append([float(s) for s in line.split() if isfloat(s)])
  
  dat1=np.array(myptend1)

  fname3=sys.argv[3]
  myptend3=[]
  with open(fname3, 'r') as f3:
      for line in f3:
          if any(x in line.strip() for x in keystrings):
              myptend3.append([float(s) for s in line.split() if isfloat(s)])
  dat3=np.array(myptend3)

  fname4=sys.argv[4]
  myptend4=[]
  with open(fname4, 'r') as f4:
      for line in f4:
          if any(x in line.strip() for x in keystrings):
              myptend4.append([float(s) for s in line.split() if isfloat(s)])
  dat4=np.array(myptend4)
  
# Start the figure
  fig = plt.figure(figsize=(8, 6))
  plt.title('Mean Absolute Pressure Tendency')
  plt.ylabel('hPa/hr')
  plt.xlabel('Timestep (hours)')
  plt.plot(dat[:,0],dat[:,1],color='red',label="gfs_noda")
  plt.plot(dat1[:,0],dat1[:,1],color='black',label="fv3lamdx_nodelz")
  plt.plot(dat3[:,0],dat3[:,1],color='blue',label="fv3lamdx")
  plt.plot(dat1[:,0],dat4[:,1],color='green',label="rrfs_gsl_grib_noda")
  plt.legend()
  plt.savefig('./ptend.png',bbox_inches='tight')
