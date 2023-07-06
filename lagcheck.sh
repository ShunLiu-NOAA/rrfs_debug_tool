#!/bin/bash
# check log file and search queue status

savedir=/lfs/h2/emc/lam/noscrub/emc.lam/Shun.Liu/test/lagcheck
mkdir -p $savedir
rm -f $savedir/lag.log
rm -f ./lag.log

for ((i=120;i>=6;i--));
do
  echo $i
mydate=`date "+%Y%m%d" --date="$i hour ago"`
cyc=`date "+%H" --date="$i hour ago"`
echo $mydate $cyc

#logdir=/lfs/h2/emc/ptmp/emc.lam/Shun.Liu/logs/rrfs_a/rrfs_a.$mydate/$cyc
logdir=/lfs/h2/emc/ptmp/emc.lam/conus/logs/rrfs_a/rrfs_a.$mydate/$cyc

if [ -d $logdir ]
then
  for ((j=1;j<=30;j++))
  do
  nmem=`printf %2.2i $j`
  echo $nmem
  numlag=`grep QUEUE $logdir/FV3LAM_wflow_enkf.log | grep run_fcst_prod_mem00$nmem |wc -l` 
  echo $mydate $cyc $numlag >> lag.log
  #grep QUEUE $logdir/FV3LAM_wflow.log | grep run_fcst
  #grep QUEUE $logdir/FV3LAM_wflow.log >> lag.log
  done
fi

done

exit
