#!/bin/bash -l
#set -x

echo $SHELL
echo `date`
source ~/bin/loadp.sh


#cdate=20220122
#cyc=12
cdate=$1
cyc=$2

dataemc=/gpfs/dell2/emc/modeling/noscrub/Shun.Liu/test/lamlog/fv3lamdax_emc/$cdate/$cyc
datashun=/gpfs/dell2/emc/modeling/noscrub/Shun.Liu/test/lamlog/fv3lamdax_shun/$cdate/$cyc
datadir=/gpfs/dell1/ptmp/Shun.Liu/tmp

cd $datadir
grep forecast $dataemc/regional_forecast_tm00_${cyc}.log* > emc
grep forecast $datashun/regional_forecast_tm00_${cyc}.log* > shun

cd /gpfs/dell2/emc/modeling/save/Shun.Liu/code/rrfs_debug_tool
 
python pltpten.py $datadir/emc \
                  $datadir/shun \
                  $cdate$cyc
mv ptend.png ptend_${cdate}_${cyc}.png


exit
datadir=/gpfs/dell2/emc/modeling/noscrub/Shun.Liu/test/pten
 
python pltpten.py $datadir/pten_emc_para \
                  $datadir/pten_emc_rrfs_prepbufr_only_hyb_on \
                  $datadir/pten_emc_rrfs_prepbufr_satwnd_hyb_on \
                  $datadir/pten_emc_rrfs_prepbufr_satwnd_l2rw_hyb_on \
