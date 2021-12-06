#!/bin/bash -l
#set -x

echo $SHELL
echo `date`
source ~/bin/loadp.sh

datadir=/gpfs/dell2/emc/modeling/noscrub/Shun.Liu/test/pten
 
python pltpten.py $datadir/pten_emc_para \
                  $datadir/pten_emc_rrfs_prepbufr_only_hyb_on \
                  $datadir/pten_emc_rrfs_prepbufr_satwnd_hyb_on \
                  $datadir/pten_emc_rrfs_prepbufr_satwnd_l2rw_hyb_on \
