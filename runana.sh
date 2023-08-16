#!/bin/bash
#PBS -A RRFS-DEV
#PBS -q pridev
#PBS -l walltime=01:45:00
#PBS -l select=60:mpiprocs=128:ncpus=128
#PBS -l place=vscatter:exclhost
#PBS -N rrfs_a_run_fcst_spinup
#PBS -j oe -o test.log


#/lfs/h2/emc/da/noscrub/Shun.Liu/rrfs/testD/ufs-srweather-app/regional_workflow/ush/load_modules_run_task.sh run_anal_gsi /lfs/h2/emc/da/noscrub/Shun.Liu/rrfs/testD/ufs-srweather-app/regional_workflow/jobs/JREGIONAL_RUN_ANAL

source /lfs/h2/emc/lam/noscrub/emc.lam/rrfs/v0.6.3/ufs-srweather-app/env/build_wcoss2_intel.env


ulimit -s unlimited
ulimit -a

set -x -u -e
date

#rundir=/lfs/h2/emc/ptmp/emc.lam/Shun.Liu/anal_conv_gsi_spinup
rundir=/lfs/h2/emc/ptmp/emc.lam/Shun.Liu/anal_conv_dbz_gsi_spinup_all

cd $rundir

rm -f pe0*
rm -f obs_input*
rm -f stdout

#cp ./bk/* .

EXEC=/lfs/h2/emc/lam/noscrub/emc.lam/rrfs/v0.6.3/ufs-srweather-app/bin/gsi.x

APRUN="mpiexec -n 480 -ppn 8 --cpu-bind core --depth 16"
export FI_OFI_RXM_SAR_LIMIT=3145728
export OMP_STACKSIZE=500M
export OMP_NUM_THREADS=16
#export OMP_PROC_BIND=close
#export OMP_PLACES=threads

$APRUN $EXEC <gsiparm.anl > stdout 2> stderr
exit

cd /lfs/h2/emc/lam/save/emc.lam/Shun.Liu/code/rrfs_debug_tool
expdir=/lfs/h2/emc/lam/noscrub/emc.lam/Shun.Liu/test/gsi/exp8
mkdir $expdir

sleep 30
cp test.log $expdir
cp /lfs/h2/emc/ptmp/emc.lam/Shun.Liu/anal_conv_gsi_spinup/stdout $expdir

