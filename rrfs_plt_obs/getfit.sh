#!/bin/bash
#set -x

USER=Shun.Liu
#sdate=2022011900
PDY=20230704
cyc=00
sdate=${PDY}$cyc

echo 'into getfit.sh'

rdasNA=/lfs/h2/emc/lam/save/emc.lam/Shun.Liu/code/rrfs_debug_tool/rrfs_plt_obs/fitobs/na/$PDY
mkdir -p $rdasNA/$sdate
rm -f fit_na

allcyc="00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23"
for cyc in $allcyc
do
fitdir=/lfs/f2/t2o/ptmp/emc/ptmp/emc.lam/rrfs/v0.5.3/prod/rrfs.$PDY/$cyc
cp $fitdir/*fits.* $rdasNA
cd $rdasNA
echo $PDY$cyc >> fit_na
grep "asm 900" rrfs_a.t${cyc}z.fits.tm00 | grep "o-g 01" >> fit_na
done
