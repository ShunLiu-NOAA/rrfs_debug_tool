#! /bin/bash
#PBS -q pridev
#PBS -A RRFS-DEV
#PBS -l walltime=00:45:00
#PBS -l select=1:mpiprocs=1:ncpus=1
##PBS -j oe -o /lfs/h2/emc/ptmp/emc.lam/Shun.Liu/rrfs_plt_lake/plot.log
#PBS -j oe
#PBS -N plt_test

#/lfs/h2/emc/ptmp/emc.lam/Shun.Liu/rrfs_plt_restart/load.sh
#/lfs/h2/emc/ptmp/emc.lam/Shun.Liu/rrfs_plt_lake/load.sh

date

cd /lfs/h2/emc/ptmp/emc.lam/Shun.Liu/rrfs_plt_lake
echo "start loading module"

#module purge
module load python/3.8.6
module use /lfs/h1/mdl/nbm/save/apps/modulefiles
module load python-modules/3.8.6
module load proj/7.1.0
module load geos/3.8.1
module load libjpeg-turbo/2.1.0
export PYTHONPATH="${PYTHONPATH}:/lfs/h2/emc/lam/noscrub/Benjamin.Blake/python:/lfs/h2/emc/lam/noscrub/Benjamin.Blake/rrfs_graphics/modulefiles"
#module load imagemagick/7.0.8-7

cd /lfs/h2/emc/ptmp/emc.lam/Shun.Liu/rrfs_plt_lake

python /lfs/h2/emc/ptmp/emc.lam/Shun.Liu/rrfs_plt_lake/plt_rrfs_nc_restart_surface.py >plot.log 2>&1
