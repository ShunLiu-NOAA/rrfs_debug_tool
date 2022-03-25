#!/bin/bash

for ((i=120;i>=6;i--));
do
  echo $i

mydate=`date "+%Y%m%d" --date="$i hour ago"`
cyc=`date "+%H" --date="$i hour ago"`
#mydate=20220324
cyc00=00
cyc12=12
#mydate=$1
#cyc=$2
cdate=$mydate$cyc

if [[ "$cyc" == "00" || "$cyc" == "12" ]]; then

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

fi

done
