#!/bin/bash

#tcyc="00 06 12 18"
#tfhr="000 048 096 240"
tcyc="00"
tfhr="000"
for fdate in $(seq -f "%02g" 01 31)
do
  for cyc in $tcyc ; do
  for fhr in $tfhr ; do
  for imon in $(seq -f "%02g" 01 11);do
  thisdate=2023${imon}${fdate}
  #grbfile=/lfs/h1/ops/prod/com/gfs/v16.3/gfs.${thisdate}/${cyc}/atmos/gfs.t${cyc}z.pgrb2.0p25.f$fhr
  grbfile=/lfs/h2/emc/ptmp/emc.lam/Shun.Liu/gfs.${thisdate}/${cyc}/atmos/gfs.t${cyc}z.pgrb2.0p25.f$fhr
  mkdir -p ./gfs/${thisdate}/${cyc}/
  savedir=./gfs/${thisdate}/${cyc}
  wgrib2 $grbfile -match ":(TMP:2 m above ground|TMP:surface):" -grib $savedir/gfs.${thisdate}.t${cyc}z.grib2.f$fhr
  done; done; done
done

#cp /lfs/h1/ops/prod/com/gfs/v16.3/gfs.20250122/00/atmos/gfs.t00z.pgrb2.0p25.f000 .
#wgrib2 gfs.t00z.pgrb2.0p25.f000 -match ":(TMP:2 m above ground|TMP:surface):" -grib new_grib

# there is an analysis file for each cycle, however, the file only keep for 8 days on WCOSS
# /lfs/h1/ops/prod/com/gfs/v16.3/gfs.20250?0?/00/atmos/gfs.t00z.pgrb2.0p25.anl

