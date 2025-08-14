##!/bin/bash

#PBS -A RRFS-DEV
#PBS -q dev_transfer
#PBS -l select=1:ncpus=1:mem=2G
#PBS -l walltime=5:59:00
#PBS -j oe
#PBS -N log_get_gfs_hpss

set -x

mkdir -p /lfs/h2/emc/ptmp/emc.lam/Shun.Liu
cd /lfs/h2/emc/ptmp/emc.lam/Shun.Liu

#YEAR=${version},MON="03",sdate="15",edate="31"

mon=$MON
year=$YEAR
sdate=$SDATE
edate=$EDATE
for iday in $(seq -f "%02g" $sdate $edate)
do
 echo $iday
 htar xf /NCEPPROD/hpssprod/runhistory/rh${year}/${year}${mon}/${year}${mon}${iday}/com_gfs_v16.3_gfs.${year}${mon}${iday}_00.gfs_pgrb2.tar ./gfs.${year}${mon}${iday}/00/atmos/gfs.t00z.pgrb2.0p25.f000
done

