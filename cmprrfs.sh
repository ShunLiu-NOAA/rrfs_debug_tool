#!/bin/bash -l
#set -x

########################
# input:
# file1: rrfs file1
# file2: rrfs file2
########################

echo $SHELL
echo `date`
#source ~/bin/loadp.sh

execdir=/lfs/h2/emc/lam/save/emc.lam/Shun.Liu/code/rrfs_debug_tool
#thisdate=`$NDATE -24 |cut -c1-8`

file1=/lfs/f2/t2o/ptmp/emc/stmp/emc.lam/rrfs/v0.9.1/2025032811/anal_conv_dbz_gsi/fv3_dynvars
file2=/lfs/h3/emc/lam/noscrub/ecflow/stmp/emc.lam/rrfs/ecflow_rrfs/rrfs_analysis_gsi_40214_11_v1.0/det/rrfs_det_analysis_gsi_11.187923563.cbqs01

python $execdir/cmprrfs.py -file1 $file1 -file2 $file2 
