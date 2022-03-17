#!/bin/bash


for ((i=80;i>=6;i--));
do
  echo $i

mydate=`date "+%Y%m%d%H" --date="$i hour ago"`
echo $mydate

#rundir=/gpfs/dell1/ptmp/Shun.Liu/stmp/tmpnwprd/RRFS_NA_3km_dev1/$mydate
#fitdir=/gpfs/dell2/emc/modeling/noscrub/Shun.Liu/test/wcoss_fit2obs/$mydate
#rundir=/gpfs/dell1/ptmp/Shun.Liu/stmp/tmpnwprd/RRFS_CONUS_3km/$mydate
#rundir=/gpfs/dell2/ptmp/Ming.Hu/NCO_dirs/stmp/tmpnwprd/RRFS_conus_3km/$mydate
#rundir=/gpfs/dell1/ptmp/Shun.Liu/stmp/tmpnwprd/RRFS_conus_3km/$mydate

#fitdir=/gpfs/dell2/emc/modeling/noscrub/Shun.Liu/test/wcoss_fit2obs_conus/$mydate
rundir=/gpfs/dell1/ptmp/Shun.Liu/stmp/tmpnwprd/RRFS_conus_3km/$mydate
#rundir=/gpfs/dell1/ptmp/emc.campara/stmp/tmpnwprd/RRFS_conus_3km/$mydate
fitdir=/gpfs/dell2/emc/modeling/noscrub/Shun.Liu/test/wcoss_fit2obs_conus_shun/$mydate

if [ -d $rundir/anal_gsi_spinup ]
then
mkdir -p $fitdir/anal_gsi_spinup
cp $rundir/anal_gsi_spinup/fort.2* $fitdir/anal_gsi_spinup
cp $rundir/anal_gsi_spinup/stdout $fitdir/anal_gsi_spinup

cd $fitdir/anal_gsi_spinup
sed -e 's/   asm all     /ps asm 900 0000/; s/   rej all     /ps rej 900 0000/; s/   mon all     /ps mon 900 0000/' fort.201 > fit_p1
sed -e 's/   asm all     /uv asm 900 0000/; s/   rej all     /uv rej 900 0000/; s/   mon all     /uv mon 900 0000/' fort.202 > fit_w1
sed -e 's/   asm all     / t asm 900 0000/; s/   rej all     / t rej 900 0000/; s/   mon all     / t mon 900 0000/' fort.203 > fit_t1
sed -e 's/   asm all     / q asm 900 0000/; s/   rej all     / q rej 900 0000/; s/   mon all     / q mon 900 0000/' fort.204 > fit_q1
sed -e 's/   asm all     /pw asm 900 0000/; s/   rej all     /pw rej 900 0000/; s/   mon all     /pw mon 900 0000/' fort.205 > fit_pw1
sed -e 's/   asm all     /rw asm 900 0000/; s/   rej all     /rw rej 900 0000/; s/   mon all     /rw mon 900 0000/' fort.209 > fit_rw1
cat fit_p1 fit_w1 fit_t1 fit_q1 fit_pw1 fit_rw1 fit_rad1 > rrfs_spinup.fits
cat fort.208 fort.210 fort.211 fort.212 fort.213 fort.220 > rrfs_spinup.fits2
fi

if [ -d $rundir/anal_gsi ]
then
mkdir -p $fitdir/anal_gsi
cp $rundir/anal_gsi/fort.2* $fitdir/anal_gsi
cp $rundir/anal_gsi/stdout $fitdir/anal_gsi

cd $fitdir/anal_gsi
sed -e 's/   asm all     /ps asm 900 0000/; s/   rej all     /ps rej 900 0000/; s/   mon all     /ps mon 900 0000/' fort.201 > fit_p1
sed -e 's/   asm all     /uv asm 900 0000/; s/   rej all     /uv rej 900 0000/; s/   mon all     /uv mon 900 0000/' fort.202 > fit_w1
sed -e 's/   asm all     / t asm 900 0000/; s/   rej all     / t rej 900 0000/; s/   mon all     / t mon 900 0000/' fort.203 > fit_t1
sed -e 's/   asm all     / q asm 900 0000/; s/   rej all     / q rej 900 0000/; s/   mon all     / q mon 900 0000/' fort.204 > fit_q1
sed -e 's/   asm all     /pw asm 900 0000/; s/   rej all     /pw rej 900 0000/; s/   mon all     /pw mon 900 0000/' fort.205 > fit_pw1
sed -e 's/   asm all     /rw asm 900 0000/; s/   rej all     /rw rej 900 0000/; s/   mon all     /rw mon 900 0000/' fort.209 > fit_rw1
cat fit_p1 fit_w1 fit_t1 fit_q1 fit_pw1 fit_rw1 fit_rad1 > rrfs_prod.fits
cat fort.208 fort.210 fort.211 fort.212 fort.213 fort.220 > rrfs_prod.fits2
fi


done
