#!/bin/bash


mydate=`date "+%Y%m%d%H" --date="6 hour ago"`
echo $mydate

rundir=/mnt/lfs4/BMC/nrtrr/NCO_dirs/stmp/tmpnwprd/RRFS_NA_3km_dev1/$mydate

fitdir=/mnt/lfs1/BMC/wrfruc/Shun.Liu/test/jet_fit2obs/$mydate

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
