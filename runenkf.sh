#!/bin/sh
#PBS -A RRFS-DEV
#PBS -q pridev 
#PBS -l walltime=00:25:00
#PBS -l select=10:ncpus=128
#PBS -l place=vscatter:exclhost
#PBS -N peter10-emc_enkf_debug
#PBS -j oe -o test.log

export GLOBAL_VAR_DEFNS_FP='/lfs/h2/emc/lam/noscrub/emc.lam/rrfs/rrfse/var_defns.sh'
export nens='30'
export CDATE='2022102318'
export CYCLE_DIR='/lfs/h2/emc/stmp/emc.lam/Shun.Liu/stmp/tmpnwprd/rrfs_a/2022102318'
export CYCLE_ROOT='/lfs/h2/emc/stmp/emc.lam/Shun.Liu/stmp/tmpnwprd/rrfs_a'
export NWGES_DIR='/lfs/h2/emc/ptmp/emc.lam/Shun.Liu/nwges/para/rrfs_a/2022102318'
export OB_TYPE='conv'
set -x
source /lfs/h2/emc/lam/noscrub/emc.lam/rrfs/v0.4.1/ufs-srweather-app/env/build_wcoss2_intel.env
set -x

module list


ulimit -s unlimited
ulimit -a

date

rundir=/lfs/h2/emc/stmp/emc.lam/rrfs/v0.4.1/2023032507/enkfupdt_conv

cd $rundir


#clt EXEC=/lfs/h2/emc/da/noscrub/Ting.Lei/dr-jeff/GSI//build_normal/src/enkf/enkf.x
#EXEC=/lfs/h2/emc/da/noscrub/Ting.Lei/dr-ou-gsi/GSI//build/src/enkf/enkf.x
EXEC=enkf.x

#clt APRUN="mpiexec -n 640 -ppn 8 "
#export FI_OFI_RXM_SAR_LIMIT=3145728
#export OMP_STACKSIZE=500M
export OMP_STACKSIZE=2048M
export OMP_NUM_THREADS=8
export OMP_PROC_BIND=close
export OMP_PLACES=threads

export MPICH_RANK_REORDER_METHOD=0

#cp enkf.nml_ens30 enkf.nml
#cp anavinfo.org anavinfo
rm -f outtest
rm -f errtest
#clt $APRUN -l    $EXEC <enkf.nml > opt4_hera-jeff-ctrl5ens30-outtest 2> opt4_hera-jeff-ctrl5ens30-errtest
mpiexec -n 80 -ppn 8 --label --line-buffer -cpu-bind depth -depth 16 $EXEC <enkf.nml

date

