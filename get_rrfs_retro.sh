
#this script should be placed in /gpfs/dell6/emc/modeling/noscrub/Shun.Liu/com 
#get rap observation
rapdir=/gpfs/hps/nco/ops/com/rap/prod/rap.20211118
mkdir -p rap/prod/rap.20211118
cp $rapdir/*bufr* rap/prod/rap.20211118

exit
#get gfs ics
gfsdir=/gpfs/dell1/nco/ops/com/gfs/prod/gfs.20211118/00/atmos
mkdir -p gfs/prod/gfs.20211118/00/atmos
cp $gfsdir/gfs.t00z.atmf006.nc gfs/prod/gfs.20211118/00/atmos
cp $gfsdir/gfs.t00z.atmf007.nc gfs/prod/gfs.20211118/00/atmos

#get gdas ics
gdasdir=/gpfs/dell1/nco/ops/com/gfs/prod/gdas.20211118/00/atmos
mkdir -p gfs/prod/gdas.20211118/00/atmos
cp $gdasdir/gdas.t00z.atmf006.nc gfs/prod/gdas.20211118/00/atmos
cp $gdasdir/gdas.t00z.atmf007.nc gfs/prod/gdas.20211118/00/atmos

#get gfs lbcs
cp $gfsdir/gfs.t00z.pgrb2.0p25.f00* gfs/prod/gfs.20211118/00/atmos
cp $gfsdir/gfs.t00z.pgrb2.0p25.f01* gfs/prod/gfs.20211118/00/atmos
cp $gfsdir/gfs.t00z.pgrb2.0p25.f02* gfs/prod/gfs.20211118/00/atmos


memdir=/gpfs/dell1/nco/ops/com/gfs/prod/enkfgdas.20211118/00/atmos

#get enkf mean
mkdir -p gfs/prod/enkfgdas.20211118/00/atmos
cp $memdir/gdas.t00z.atmf006.ensmean.nc gfs/prod/enkfgdas.20211118/00/atmos
cp $memdir/gdas.t00z.sfcf006.ensmean.nc gfs/prod/enkfgdas.20211118/00/atmos
cp $memdir/gdas.t00z.atmf007.ensmean.nc gfs/prod/enkfgdas.20211118/00/atmos
cp $memdir/gdas.t00z.sfcf007.ensmean.nc gfs/prod/enkfgdas.20211118/00/atmos

#get enkf mem
for i in $(seq -f "%03g" 1 80)
do
  echo $i
  mkdir -p gfs/prod/enkfgdas.20211118/00/atmos/mem${i}
  cp $memdir/mem${i}/gdas.t00z.atmf006.nc gfs/prod/enkfgdas.20211118/00/atmos/mem${i}
  cp $memdir/mem${i}/gdas.t00z.atmf007.nc gfs/prod/enkfgdas.20211118/00/atmos/mem${i}
done
