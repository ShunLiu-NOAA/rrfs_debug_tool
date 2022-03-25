#!/bin/bash

for ((i=120;i>=6;i--));
do
  echo $i
mydate=`date "+%Y%m%d" --date="$i hour ago"`
cyc=`date "+%H" --date="$i hour ago"`
echo $mydate

logdir=/gpfs/dell1/ptmp/emc.campara/ptmp/com/logs/RRFS_CONUS/RRFS_conus_3km.$mydate/$cyc
savedir=/gpfs/dell2/emc/modeling/noscrub/Shun.Liu/test/lamlog/rrfs.$mydate/$cyc

if [ -d $logdir ]
then
  mkdir -p $savedir
  cp $logdir/run_fcst_prod_*.log $savedir
  cp $logdir/run_fcst_spinup_*.log $savedir
fi

logdir=/gpfs/dell1/ptmp/Shun.Liu/ptmp/com/logs/RRFS_CONUS/RRFS_conus_3km.$mydate/$cyc
savedir=/gpfs/dell2/emc/modeling/noscrub/Shun.Liu/test/lamlog/rrfsx.$mydate/$cyc

if [ -d $logdir ]
then
  mkdir -p $savedir
  cp $logdir/run_fcst_prod_*.log $savedir
  cp $logdir/run_fcst_spinup_*.log $savedir
fi

done

exit
