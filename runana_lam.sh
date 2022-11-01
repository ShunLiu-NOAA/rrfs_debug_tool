#!/bin/bash -l
#!/bin/bash
#PBS -A RRFS-DEV
#PBS -q dev
#PBS -l walltime=00:25:00
#PBS -l select=22:mpiprocs=128:ncpus=128
#PBS -l place=vscatter:exclhost
#PBS -N gsi_test
#PBS -j oe -o test.log


#/lfs/h2/emc/da/noscrub/Shun.Liu/rrfs/testD/ufs-srweather-app/regional_workflow/ush/load_modules_run_task.sh run_anal_gsi /lfs/h2/emc/da/noscrub/Shun.Liu/rrfs/testD/ufs-srweather-app/regional_workflow/jobs/JREGIONAL_RUN_ANAL

source /lfs/h2/emc/lam/noscrub/emc.lam/Shun.Liu/rrfs/testD/ufs-srweather-app/env/build_wcoss2_intel.env
set -x

module list


ulimit -s unlimited
ulimit -a

set -x -u -e
date

rundir=/lfs/h2/emc/lam/noscrub/emc.lam/Shun.Liu/test/anal_gsi

cd $rundir

rm -f pe0*
rm -f obs_input*

EXEC=/lfs/h2/emc/lam/noscrub/emc.lam/Shun.Liu/rrfs/testD/ufs-srweather-app/bin/gsi.x

APRUN="mpiexec -n 352 -ppn 16 --cpu-bind core --depth 8"
export FI_OFI_RXM_SAR_LIMIT=3145728
export OMP_STACKSIZE=500M
export OMP_NUM_THREADS=8


$APRUN $EXEC <gsiparm.anl > outtest 2> errtest

date
