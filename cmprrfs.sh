#!/bin/bash -l
#set -x

########################
# input:
# file1: rrfs file1
# file2: rrfs file2
########################

echo $SHELL
echo `date`
source ~/bin/loadp.sh

execdir=/gpfs/dell2/emc/modeling/save/Shun.Liu/code/rrfs_debug_tool
thisdate=`$NDATE -24 |cut -c1-8`

file1=/gpfs/dell1/ptmp/emc.campara/guess.tm06/gfs_data.tile7.nc
file2=/gpfs/dell1/ptmp/emc.campara/guess.tm06/out.atm.tile7.nc


python $execdir/cmprrfs.py -file1 $file1 -file2 $file2 
