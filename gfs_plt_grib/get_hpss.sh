#PBS -A RRFS-DEV
#PBS -q dev_transfer
#PBS -l select=1:mpiprocs=1:ncpus=1
#PBS -l walltime=05:55:00
#PBS -N get_retro
#PBS -j oe -o get_retro.log
set -x

mkdir -p /lfs/h2/emc/ptmp/emc.lam/Shun.Liu
cd /lfs/h2/emc/ptmp/emc.lam/Shun.Liu

#for ihh in $(seq -f "%03g" 0 12)
#for ihh in {12..21..3}

mon=12
year=2024
for iday in $(seq -f "%02g" 1 31)
do
htar xf /NCEPPROD/hpssprod/runhistory/rh${year}/${year}${mon}/${year}${mon}${iday}/com_gfs_v16.3_gfs.${year}${mon}${iday}_00.gfs_pgrb2.tar ./gfs.${year}${mon}${iday}/00/atmos/gfs.t00z.pgrb2.0p25.f000
done

