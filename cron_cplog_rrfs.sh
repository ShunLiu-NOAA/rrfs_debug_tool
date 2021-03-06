#!/bin/bash

mydate=`date "+%Y%m%d" --date="24 hour ago"`
cyc=`date "+%H" --date="24 hour ago"`
echo $mydate

logdir=/gpfs/dell1/ptmp/emc.campara/logs/rrfs_a/rrfs_a.$mydate/$cyc
savedir=/gpfs/dell2/emc/modeling/noscrub/Shun.Liu/test/lamlog/rrfs.$mydate/$cyc

if [ -d $rundir ]
then
  mkdir -p $savedir
  cp $logdir/run_fcst_prod_*.log $savedir
  cp $logdir/run_fcst_spinup_*.log $savedir
fi

logdir=/gpfs/dell1/ptmp/Shun.Liu/ptmp/com/logs/RRFS_CONUS/RRFS_conus_3km.$mydate/$cyc
savedir=/gpfs/dell2/emc/modeling/noscrub/Shun.Liu/test/lamlog/rrfsx.$mydate/$cyc

if [ -d $rundir ]
then
  mkdir -p $savedir
  cp $logdir/run_fcst_prod_*.log $savedir
  cp $logdir/run_fcst_spinup_*.log $savedir
fi

exit
