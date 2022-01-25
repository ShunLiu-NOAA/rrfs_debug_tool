#!/bin/bash

mydate=20220122
cyc=12
cdate=$mydate$cyc

#logdir=/gpfs/dell2/emc/modeling/noscrub/Shun.Liu/test/lamlog/fv3lamdax_shun/20220119

logdir=/gpfs/dell2/ptmp/Shun.Liu/fv3lamdax/log
slogdir=/gpfs/dell2/emc/modeling/noscrub/Shun.Liu/test/lamlog/fv3lamdax_shun/$mydate/$cyc

#logdir=/gpfs/dell2/ptmp/emc.campara/fv3lamdax/log
#slogdir=/gpfs/dell2/emc/modeling/noscrub/Shun.Liu/test/lamlog/fv3lamdax_emc/$mydate/$cyc

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
