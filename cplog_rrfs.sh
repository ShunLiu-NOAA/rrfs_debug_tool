#!/bin/bash

for ((i=120;i>=6;i--));
do
  echo $i
mydate=`date "+%Y%m%d" --date="$i hour ago"`
cyc=`date "+%H" --date="$i hour ago"`
echo $mydate

logdir=/gpfs/dell1/ptmp/emc.campara/logs/rrfs_a/rrfs_a.$mydate/$cyc
savedir=/gpfs/dell2/emc/modeling/noscrub/Shun.Liu/test/lamlog/rrfs.$mydate/$cyc

if [ -d $logdir ]
then
  mkdir -p $savedir
  cp $logdir/run_fcst_prod_*.log $savedir
  cp $logdir/run_fcst_spinup_*.log $savedir
fi

logdir=/gpfs/dell1/ptmp/Shun.Liu/logs/rrfs_a/rrfs_a.$mydate/$cyc
savedir=/gpfs/dell2/emc/modeling/noscrub/Shun.Liu/test/lamlog/rrfsx.$mydate/$cyc

if [ -d $logdir ]
then
  mkdir -p $savedir
  cp $logdir/run_fcst_prod_*.log $savedir
  cp $logdir/run_fcst_spinup_*.log $savedir
fi

done

exit
