
#this script should be placed in /gpfs/dell6/emc/modeling/noscrub/Shun.Liu/com 
#get rap observation
mydate=20211205

dothis=false
if [ $dothis = "true" ]; then
rapdir=/gpfs/hps/nco/ops/com/rap/prod/rap.$mydate
mkdir -p rap/prod/rap.$mydate
cp $rapdir/*bufr* rap/prod/rap.$mydate

#get gfs ics
gfsdir=/gpfs/dell1/nco/ops/com/gfs/prod/gfs.$mydate/00/atmos
mkdir -p gfs/prod/gfs.$mydate/00/atmos
cp $gfsdir/gfs.t00z.atmf006.nc gfs/prod/gfs.$mydate/00/atmos
cp $gfsdir/gfs.t00z.atmf007.nc gfs/prod/gfs.$mydate/00/atmos

#get gdas ics
gdasdir=/gpfs/dell1/nco/ops/com/gfs/prod/gdas.$mydate/00/atmos
mkdir -p gfs/prod/gdas.$mydate/00/atmos
cp $gdasdir/gdas.t00z.atmf006.nc gfs/prod/gdas.$mydate/00/atmos
cp $gdasdir/gdas.t00z.atmf007.nc gfs/prod/gdas.$mydate/00/atmos

#get gfs lbcs
cp $gfsdir/gfs.t00z.pgrb2.0p25.f00* gfs/prod/gfs.$mydate/00/atmos
cp $gfsdir/gfs.t00z.pgrb2.0p25.f01* gfs/prod/gfs.$mydate/00/atmos
cp $gfsdir/gfs.t00z.pgrb2.0p25.f02* gfs/prod/gfs.$mydate/00/atmos
cp $gfsdir/gfs.t00z.pgrb2.0p25.f03* gfs/prod/gfs.$mydate/00/atmos
exit
fi


memdir=/gpfs/dell1/nco/ops/com/gfs/prod/enkfgdas.$mydate/00/atmos

#get enkf mean
mkdir -p gfs/prod/enkfgdas.$mydate/00/atmos
cp $memdir/gdas.t00z.atmf006.ensmean.nc gfs/prod/enkfgdas.$mydate/00/atmos
cp $memdir/gdas.t00z.sfcf006.ensmean.nc gfs/prod/enkfgdas.$mydate/00/atmos
cp $memdir/gdas.t00z.atmf007.ensmean.nc gfs/prod/enkfgdas.$mydate/00/atmos
cp $memdir/gdas.t00z.sfcf007.ensmean.nc gfs/prod/enkfgdas.$mydate/00/atmos
cp $memdir/gdas.t00z.atmf008.ensmean.nc gfs/prod/enkfgdas.$mydate/00/atmos
cp $memdir/gdas.t00z.sfcf008.ensmean.nc gfs/prod/enkfgdas.$mydate/00/atmos
cp $memdir/gdas.t00z.atmf009.ensmean.nc gfs/prod/enkfgdas.$mydate/00/atmos
cp $memdir/gdas.t00z.sfcf009.ensmean.nc gfs/prod/enkfgdas.$mydate/00/atmos
mkdir -p gfs/prod/enkfgdas.$mydate/06/atmos
cp $memdir/gdas.t00z.atmf004.ensmean.nc gfs/prod/enkfgdas.$mydate/06/atmos
cp $memdir/gdas.t00z.sfcf004.ensmean.nc gfs/prod/enkfgdas.$mydate/06/atmos
cp $memdir/gdas.t00z.atmf005.ensmean.nc gfs/prod/enkfgdas.$mydate/06/atmos
cp $memdir/gdas.t00z.sfcf005.ensmean.nc gfs/prod/enkfgdas.$mydate/06/atmos
cp $memdir/gdas.t00z.atmf006.ensmean.nc gfs/prod/enkfgdas.$mydate/06/atmos
cp $memdir/gdas.t00z.sfcf006.ensmean.nc gfs/prod/enkfgdas.$mydate/06/atmos

#get enkf mem
for i in $(seq -f "%03g" 1 80)
do
  echo $i
  mkdir -p gfs/prod/enkfgdas.$mydate/00/atmos/mem${i}
  cp $memdir/mem${i}/gdas.t00z.atmf006.nc gfs/prod/enkfgdas.$mydate/00/atmos/mem${i}
  cp $memdir/mem${i}/gdas.t00z.atmf007.nc gfs/prod/enkfgdas.$mydate/00/atmos/mem${i}
  cp $memdir/mem${i}/gdas.t00z.atmf008.nc gfs/prod/enkfgdas.$mydate/00/atmos/mem${i}
  cp $memdir/mem${i}/gdas.t00z.atmf009.nc gfs/prod/enkfgdas.$mydate/00/atmos/mem${i}

  mkdir -p gfs/prod/enkfgdas.$mydate/00/atmos/mem${i}
  cp $memdir/mem${i}/gdas.t00z.atmf004.nc gfs/prod/enkfgdas.$mydate/06/atmos/mem${i}
  cp $memdir/mem${i}/gdas.t00z.atmf005.nc gfs/prod/enkfgdas.$mydate/06/atmos/mem${i}
  cp $memdir/mem${i}/gdas.t00z.atmf006.nc gfs/prod/enkfgdas.$mydate/06/atmos/mem${i}
done
