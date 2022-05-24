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
  print(fname)
  with open(fname, 'r') as f:
      for line in f:
          if any(x in line.strip() for x in keystrings):
              myptend.append([float(s) for s in line.split() if isfloat(s)])
  
  dat=np.array(myptend)

  fname1=sys.argv[2]   
  print(fname1)
  myptend1=[]
  with open(fname1, 'r') as f1:
      for line in f1:
          if any(x in line.strip() for x in keystrings):
              myptend1.append([float(s) for s in line.split() if isfloat(s)])
  
  dat1=np.array(myptend1)
  dat2=np.array(myptend1)

  dat2[:,1]=(dat[:,1]-dat1[:,1])*1.0

# Start the figure
  fig = plt.figure(figsize=(8, 6))
  cdate=sys.argv[3]
  mytitle='Mean Absolute Pressure Tendency '+cdate
  plt.title(mytitle)
  plt.ylabel('hPa/hr')
  plt.xlabel('Timestep (hours)')
  nhr=600
  plt.plot(dat[0:nhr,0],dat[0:nhr,1],color='red',label="RRFSp1")
  plt.plot(dat1[0:nhr,0],dat1[0:nhr,1],color='black',label="RRFSp1x")
# plt.plot(dat2[0:nhr,0],dat2[0:nhr,1],color='blue',label="(para-exp)x1.0")
  plt.legend()
  plt.savefig('./ptend.png',bbox_inches='tight')
