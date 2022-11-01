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

def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


if __name__ == '__main__':

  #fname=sys.argv[1]   
  fname='./lag.log'
  myptend=[]
  cdate='20221030'
  keystrings=[cdate]
  print(fname)
  with open(fname, 'r') as f:
      for line in f:
          if any(x in line.strip() for x in keystrings):
              myptend.append([int(s) for s in line.split() if isint(s)])
  
  dat=np.array(myptend)

  print(dat)

# Start the figure
  fig = plt.figure(figsize=(12, 6))
  #cdate=sys.argv[3]
  #cdate="20221026"
  mytitle='forecast job in queue time '+cdate
  plt.title(mytitle)
  plt.ylabel('minutes')
  plt.xlabel('cycle (hours)')
  nhr=23
  plt.scatter(dat[0:nhr,1],dat[0:nhr,2],color='blue',label="in queue time")
  #plt.legend()
  figname=cdate+'_queue_time.png'
  plt.savefig(figname,bbox_inches='tight')
  exit(0);
