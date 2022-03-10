#!/bin/bash
#set -x

USER=Shun.Liu
mydate=`date "+%Y%m%d" --date="24 hour ago"`
myhour=`date "+%H" --date="24 hour ago"`

#module load prod_util/1.1.0
#thisdate=`$NDATE`
#echo $thisdate

echo $mydate
PDY=$mydate
cyc=$myhour
sdate=${PDY}$cyc

echo 'into getfit.sh'

fitdirp=/gpfs/dell2/ptmp/emc.campara/fv3lamdax/fv3lamdax.$PDY/$cyc
rdasNAt=/gpfs/dell2/emc/modeling/noscrub/Shun.Liu/test/fitobs/fv3lamdax_emc.$PDY/$cyc
mkdir -p $rdasNAt
cp $fitdirp/*fits.* $rdasNAt 
cd $rdasNAt
tm='tm06 tm05 tm04 tm03 tm02 tm01 tm00'
for itm in $tm
do
  sed -e 's/asm 900     /asm 900 0000/' fv3lam.t${cyc}z.fits.$itm > $itm
  mv $itm fv3lam.t${cyc}z.fits.$itm
done

fitdirp=/gpfs/dell5/ptmp/emc.campara/fv3lamdax/fv3lamda.$PDY/$cyc
rdasNAt=/gpfs/dell2/emc/modeling/noscrub/Shun.Liu/test/fitobs/fv3lamda_emc.$PDY/$cyc
mkdir -p $rdasNAt
cp $fitdirp/*fits.* $rdasNAt
cd $rdasNAt
tm='tm06 tm05 tm04 tm03 tm02 tm01 tm00'
for itm in $tm
do
  sed -e 's/asm 900     /asm 900 0000/' fv3lam.t${cyc}z.fits.$itm > $itm
  mv $itm fv3lam.t${cyc}z.fits.$itm
done

exit

fitdir=/gpfs/dell2/ptmp/Shun.Liu/fv3lamdax/fv3lamdax.$PDY/$cyc

if [ -d $fitdir ]; then
rdasNA=/gpfs/dell2/emc/modeling/noscrub/Shun.Liu/test/fitobs/fv3lamdax_shun.$PDY/$cyc
mkdir -p $rdasNA
cp $fitdir/*fits.* $rdasNA
cd $rdasNA
tm='tm06 tm05 tm04 tm03 tm02 tm01 tm00'
for itm in $tm
do
  sed -e 's/asm 900     /asm 900 0000/' fv3lam.t${cyc}z.fits.$itm > $itm
  mv $itm fv3lam.t${cyc}z.fits.$itm
done
fi

exit
