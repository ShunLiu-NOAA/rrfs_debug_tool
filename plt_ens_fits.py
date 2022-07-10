## 
## Plot fit-to-obs from ensemble members
## 
## input:   
## output:  
##
## History log:
## 2022-02-18:  Shun Liu  - Created

#from mpl_toolkits.basemap import Basemap, cm
#import pygrib
import matplotlib
#matplotlib.use('Agg')   #Necessary to generate figs when not running an Xserver (e.g. via PBS)
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.ticker import FormatStrFormatter
import numpy as np
import yaml
import sys 
import os 

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

#   for d in sys.path:
#     print d

    stream = open("config_ens_fits.yaml", 'r')
    config = yaml.safe_load(stream)

    OBSTYPE=config['OBSTYPE']
    pltTYPE=config['pltTYPE']
    cyctime=config['cyctime']
    hpc=config['hpc']
    fldir=config['paths']['inputdir']
    varmin=config['varRange']['minvalue']
    varmax=config['varRange']['maxvalue']
    nmem=config['nmember']

    print(fldir)
    nmem=nmem+1

    if OBSTYPE=="wind":
      fortfile="fort.202"
    elif OBSTYPE=="t":
      fortfile="fort.203"

    if pltTYPE=="rms":
      keystrings=['o-g 01         asm all        rms']
    elif pltTYPE=="count":
      keystrings=['o-g 01         asm all      count']
 

    mytmp=[]
    for i in range(0,nmem):
      if i==0 :
        fname=fldir+'/ensmean'+'/observer_gsi/'+fortfile
        mem="ensmean"
      else:
        #fname=fldir+'/mem'+str(i).zfill(4)+'/observer_gsi/'+fortfile
        fname=fldir+'/'+str(i)+'/observer_gsi/'+fortfile
        mem=str(i)
      print(fname)
      with open(fname,'r') as f:
        for line in f:
          if any(x in line.strip() for x in keystrings):
              print(line)
              mytmp.append([float(s) for s in line.split() if isfloat(s)])

    dat=np.array(mytmp)
    print(dat.shape)
    #exit()

    for i in range(0,13):
      print(dat[0,i],dat[15,i])
    
    levels = [1000, 900, 800, 600, 400, 300, 250, 200, 150, 100, 50, 0]

    figname=OBSTYPE+'_'+pltTYPE
    tname=str(cyctime)+'_'+OBSTYPE+'_'+pltTYPE+'_'+hpc

    plt.rcParams.update({'font.size': 16})
    fig=plt.figure(figsize=(10,10))
    ax=fig.add_subplot(111)

    colormap=plt.cm.gist_ncar
    colorst=[colormap(i) for i in np.linspace(0, 0.9, nmem)]

    for i in range(0,nmem):
      mem=i
      if i>0 :
        plt.plot(dat[i,1:13],levels[:],label=mem,color=colorst[i])
      else: 
        plt.plot(dat[i,1:13],levels[:],label=mem,color=colorst[i],linewidth=3,marker='o',markerfacecolor='r',markersize=16)

    ax=plt.gca()
    ax.invert_yaxis()

    plt.title(tname,fontsize=20)

    ax.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))

    plt.xlabel(OBSTYPE)
    plt.ylabel('pressure (hPa)')

    plt.xlim(varmin,varmax)

    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

    ax.legend(ncol=1, loc='upper right', 
           bbox_to_anchor=[1.10, 0.7], 
           columnspacing=1.0, labelspacing=0.0,
           handletextpad=0.0, handlelength=1.5,
           fancybox=True, shadow=True,fontsize=10)

    plt.savefig(tname+'.png',bbox_inches='tight',dpi=100)
    plt.clf()

    exit()

    cmd='convert '+var+'_bias.png '+var+'_max.png'+' +append '+var+'_mean.png'
