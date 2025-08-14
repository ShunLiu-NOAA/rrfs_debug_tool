#! /bin/sh
#PBS -q devhigh
#PBS -A RRFS-DEV
#PBS -l walltime=00:45:00
#PBS -l select=1:mpiprocs=1:ncpus=1
#PBS -j oe -o /lfs/h2/emc/ptmp/emc.lam/Shun.Liu/blending/plot.log
#PBS -N allvars_rrfs_f39

/lfs/h2/emc/ptmp/emc.lam/Shun.Liu/blending/load.sh

