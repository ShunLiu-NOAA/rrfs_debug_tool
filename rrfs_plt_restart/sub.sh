#! /bin/sh
#PBS -q pridev
#PBS -A RRFS-DEV
#PBS -l walltime=00:45:00
#PBS -l select=1:mpiprocs=1:ncpus=1
#PBS -j oe -o /lfs/h2/emc/lam/save/emc.lam/Shun.Liu/code/rrfs_debug_tool/rrfs_plt_restart//plot.log
#PBS -N allvars_rrfs_f39

/lfs/h2/emc/lam/save/emc.lam/Shun.Liu/code/rrfs_debug_tool/rrfs_plt_restart/load.sh

