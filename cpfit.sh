#!/bin/bash


for ((i=30;i>=6;i--));
do
  echo $i

mydate=`date "+%Y%m%d%H" --date="$i hour ago"`
echo $mydate

rundir=/gpfs/dell1/ptmp/Shun.Liu/stmp/tmpnwprd/RRFS_NA_3km_dev1/$mydate

fitdir=/gpfs/dell2/emc/modeling/noscrub/Shun.Liu/test/wcoss_fit2obs/$mydate

if [ -d $rundir/anal_gsi_spinup ]
then
mkdir -p $fitdir/anal_gsi_spinup
cp $rundir/anal_gsi_spinup/fort.2* $fitdir/anal_gsi_spinup
cp $rundir/anal_gsi_spinup/stdout $fitdir/anal_gsi_spinup
fi

if [ -d $rundir/anal_gsi ]
then
mkdir -p $fitdir/anal_gsi
cp $rundir/anal_gsi/fort.2* $fitdir/anal_gsi
cp $rundir/anal_gsi/stdout $fitdir/anal_gsi
fi


done
