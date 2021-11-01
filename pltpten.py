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
  
# Start the figure
  fig = plt.figure(figsize=(8, 6))
  plt.title('Mean Absolute Pressure Tendency')
  plt.ylabel('hPa/hr')
  plt.xlabel('Timestep (hours)')
  plt.plot(dat[:,0],dat[:,1],'k')
  plt.savefig('./ptend.png',bbox_inches='tight')
