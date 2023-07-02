#! /bin/sh
#PBS -A RRFS-DEV
#PBS -q pridev
#PBS -l select=13:mpiprocs=60:ompthreads=2:ncpus=120:mem=500G
#PBS -l walltime=00:40:00
#PBS -N test_mem0001
#PBS -j oe -o test.log
#PBS -l place=excl
set -x

module purge

module load envvar/1.0

module load PrgEnv-intel/8.1.0
module load intel/19.1.3.304
module load craype/2.7.13
module load cray-mpich/8.1.7

export HPC_OPT=/apps/ops/para/libs
module use /apps/ops/para/libs/modulefiles/compiler/intel/19.1.3.304
module use /apps/ops/para/libs/modulefiles/mpi/intel/19.1.3.304/cray-mpich/8.1.7

module load jasper/2.0.25
module load zlib/1.2.11
module load libpng/1.6.37

module load hdf5/1.10.6
module load netcdf/4.7.4
module load pio/2.5.2
module load esmf/8.3.0b09
module load fms/2022.01

module load libjpeg/9c
module load cray-pals/1.1.3
module load udunits/2.2.28
module load gsl/2.7
module load nco/4.9.7

    ulimit -s unlimited
    ulimit -a
    export OMP_PROC_BIND=true
    export OMP_NUM_THREADS=2
    export OMP_STACKSIZE=1G
    export OMP_PLACES=cores
    export MPICH_ABORT_ON_ERROR=1
    export MALLOC_MMAP_MAX_=0
    export MALLOC_TRIM_THRESHOLD_=134217728
    export FORT_FMT_NO_WRAP_MARGIN=true
    export MPICH_REDUCE_NO_SMP=1
    export FOR_DISABLE_KMP_MALLOC=TRUE
    export FI_OFI_RXM_RX_SIZE=40000
    export FI_OFI_RXM_TX_SIZE=40000
    export MPICH_OFI_STARTUP_CONNECT=1
    export MPICH_OFI_VERBOSE=1
    export MPICH_OFI_NIC_VERBOSE=1

FV3_EXE=/lfs/h2/emc/lam/noscrub/emc.lam/rrfs/v0.4.1/ufs-srweather-app/bin/ufs_model


#cd /lfs/h2/emc/stmp/emc.lam/rrfs/v0.4.1/2023032411/fcst_fv3lam
cd /lfs/h2/emc/stmp/emc.lam/rrfs/v0.4.1/2023032806/mem0001/fcst_fv3lam_spinup_one
mpiexec -n 780 -ppn 64 --cpu-bind core --depth 2 $FV3_EXE



#/lfs/h2/emc/lam/noscrub/emc.lam/rrfs/v0.4.1/ufs-srweather-app/regional_workflow/ush/load_modules_run_task.sh "run_fcst" "/lfs/h2/emc/lam/noscrub/emc.lam/rrfs/v0.4.1/ufs-srweather-app/regional_workflow/jobs/JREGIONAL_RUN_FCST"

