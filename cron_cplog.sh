#!/bin/bash
#set -x

USER=Shun.Liu
mydate=`date "+%Y%m%d" --date="24 hour ago"`
cyc=`date "+%H" --date="24 hour ago"`

cdate=$mydate$cyc

#logdir=/gpfs/dell2/emc/modeling/noscrub/Shun.Liu/test/lamlog/fv3lamdax_shun/20220119

#logdir=/gpfs/dell2/ptmp/Shun.Liu/fv3lamdax/log
#slogdir=/gpfs/dell2/emc/modeling/noscrub/Shun.Liu/test/lamlog/fv3lamdax_shun/$mydate/$cyc

logdir=/gpfs/dell2/ptmp/emc.campara/fv3lamdax/log
slogdir=/gpfs/dell2/emc/modeling/noscrub/Shun.Liu/test/lamlog/fv3lamdax_emc/$mydate/$cyc

mkdir -p $slogdir

cp -p $logdir/regional_forecast_tm*_${cyc}* $slogdir

cd $slogdir

files=`ls -1tr regional*`
for ifile in $files
do
  echo $ifile
  tdate=`grep CDATE $ifile | cut -c7-17`
  thisdate=${tdate:0:10}
  echo $thisdate

  if [ $thisdate =  $cdate ]; then
     echo $thisdate
  else
     rm -f $ifile
  fi
done


logdir=/gpfs/dell5/ptmp/emc.campara/fv3lamda/log
slogdir=/gpfs/dell2/emc/modeling/noscrub/Shun.Liu/test/lamlog/fv3lamda_emc/$mydate/$cyc

mkdir -p $slogdir

cp -p $logdir/regional_forecast_tm*_${cyc}* $slogdir

cd $slogdir

files=`ls -1tr regional*`
for ifile in $files
do
  echo $ifile
  tdate=`grep CDATE $ifile | cut -c7-17`
  thisdate=${tdate:0:10}
  echo $thisdate

  if [ $thisdate =  $cdate ]; then
     echo $thisdate
  else
     rm -f $ifile
  fi
done

mydate=`date "+%Y%m%d" --date="24 hour ago"`
cyc=`date "+%H" --date="24 hour ago"`
echo $mydate

logdir=/gpfs/dell1/ptmp/emc.campara/ptmp/com/logs/RRFS_CONUS/RRFS_conus_3km.$mydate/$cyc
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

exit

