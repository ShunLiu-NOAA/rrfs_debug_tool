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

  #fname=sys.argv[1]   
  #fname='./forecast_out_2021102012.log'

  keystrings=['At forecast hour','mean abs pgr change is','hPa/hr']

  ndim=11
  datm=np.zeros((ndim,5999))
  datmean=np.zeros((5999))

  for i in range(1,ndim,2): 
    #fname=fname+f'{i:01d}'
    fname='/gpfs/dell1/ptmp/Shun.Liu/tmp/emc'
    fname=fname+'_'+f'{i}' + '.nc4'
    print(fname)
    myptend=[]
    with open(fname, 'r') as f:
      for line in f:
          if any(x in line.strip() for x in keystrings):
              myptend.append([float(s) for s in line.split() if isfloat(s)])
    f.close()
    dat=np.zeros((5999,1))
    dat=np.array(myptend)
    datm[i,:]=dat[:,1]
  
  datmean=np.mean(datm,axis=0)*10.0/5.0

# fname1=sys.argv[2]   
  datm1=np.zeros((ndim,5999))
  datmean1=np.zeros((5999))
  datdiff=np.zeros((5999))

  for i in range(1,ndim,2): 
    fname1='/gpfs/dell1/ptmp/Shun.Liu/tmp/shun'
    fname1=fname1+'_'+f'{i}' + '.nc4'
    print(fname1)
    myptend1=[]
    with open(fname1, 'r') as f1:
      for line in f1:
          if any(x in line.strip() for x in keystrings):
              myptend1.append([float(s) for s in line.split() if isfloat(s)])
    f1.close()
    dat=np.array(myptend1)
    datm1[i,:]=dat[:,1]
  
  datmean1=np.mean(datm1,axis=0)*10/5.0
  datdiff=(datmean-datmean1)*10.0

# for i in range(0,10):
#   print(datm[0,i],datm1[0,i],(datm[0,i]-datm1[0,i]))


# Start the figure
  fig = plt.figure(figsize=(8, 6))
  #cdate=sys.argv[3]
  cdate='average'
  mytitle='Mean Absolute Pressure Tendency '+cdate
  plt.title(mytitle)
  plt.ylabel('hPa/hr')
  plt.xlabel('Timestep (hours)')
  nhr=4800
  #plt.plot(dat[0:nhr,0],datm[0,0:nhr],color='red',label="EMC para")
  #plt.plot(dat[0:nhr,0],datm1[0,0:nhr],color='black',label="pressure layer intp")
  plt.plot(dat[0:nhr,0],datmean[0:nhr],color='red',label="EMC para")
  plt.plot(dat[0:nhr,0],datmean1[0:nhr],color='black',label="pressure layer intp")
  plt.plot(dat[0:nhr,0],datdiff[0:nhr],color='blue',label="(para-exp)x10")
  plt.legend()

  for i in range(0,10):
    print(datmean[i],datmean1[i],(datmean[i]-datmean[i])*20.0)

  plt.savefig('./ptend.png',bbox_inches='tight')
