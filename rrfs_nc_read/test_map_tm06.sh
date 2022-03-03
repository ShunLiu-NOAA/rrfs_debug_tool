#!/bin/bash -l
#set -x

echo $SHELL
echo `date`
source ~/bin/loadp.sh

execdir=/gpfs/dell2/emc/modeling/save/Shun.Liu/code/rrfs_debug_tool
thisdate=`$NDATE -24 |cut -c1-8`
rundir=$execdir/test

mkdir -p $rundir
cd $rundir

allcyc='00 12'
alltmmark='tm06'
allanl='guess anl'

datadir=/gpfs/dell2/emc/modeling/noscrub/emc.campara/fv3lamdax/regional_workflow/fix_temp
gdata=$datadir/grid_spec.nc
#data=$datadir/fv3_dynvars
datadir=/gpfs/dell1/ptmp/Shun.Liu/tmp
data=$datadir/phis_emc.nc

cd $execdir/test
python $execdir/plt_fv3lam_tm06_profl_map.py -g $gdata -c $data -t $data
mv fv3grid.png phis_emc.png

data=$datadir/phis_gsl.nc

python $execdir/plt_fv3lam_tm06_profl_map.py -g $gdata -c $data -t $data
mv fv3grid.png phis_gsl.png

exit

convert phis_emc.png phis_gsl.png +append phis_emc_gsl.png
