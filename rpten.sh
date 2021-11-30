#!/bin/bash -l
#set -x

echo $SHELL
echo `date`
source ~/bin/loadp.sh

datadir=/gpfs/dell2/emc/modeling/noscrub/Shun.Liu/test/pten
 
python pltpten.py $datadir/pten_emc_rrfs_noda $datadir/pten_emc_rrfs_da_nodelz $datadir/pten_emc_rrfs_gdas_da $datadir/pten_gsl_grib_noda
