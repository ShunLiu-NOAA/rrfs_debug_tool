#!/bin/bash

#tcyc="00 06 12 18"
tcyc="00"
tfhr="000"
rm -f ttt

year=2025
mon=02
day1=01
day2=28

yyyymmdd1=$year$mon$day1
yyyymmdd2=$year$mon$day2
echo $yyyymmdd1
echo $yyyymmdd2
startday=`date -d ${yyyymmdd1} +%j`
endday=`date -d ${yyyymmdd2} +%j`
echo $startday, $endday
#year=`echo $thisdate | cut -c1-4`

rm -f tmp_${year}${mon}.csv

echo "Date,tm000" > tmp.csv
for fdate in $(seq -f "%08g" $startday $endday)
do
  for cyc in $tcyc ; do
  for fhr in $tfhr ; do
  echo $fdate
  thisdate=`date -d "${year}-01-01 +$((10#$fdate - 1)) days" +%Y%m%d`
  echo $thisdate
  #thisdate=202501${fdate}
  savedir=./gfs/${thisdate}/${cyc}
  grbfile=$savedir/gfs.${thisdate}.t${cyc}z.grib2.f$fhr
  tmp=$(wgrib2 $grbfile -match "TMP:surface" -lon 283.31 39.18 | awk -F'=' '{print $NF}')
  #grbfile=$savedir/gfs.${thisdate}.t${cyc}z.grib2.f048
  #tmp02=$(wgrib2 $grbfile -match "TMP:surface" -lon 283.31 39.18 | awk -F'=' '{print $NF}')
  #grbfile=$savedir/gfs.${thisdate}.t${cyc}z.grib2.f096
  #tmp04=$(wgrib2 $grbfile -match "TMP:surface" -lon 283.31 39.18 | awk -F'=' '{print $NF}')
  #grbfile=$savedir/gfs.${thisdate}.t${cyc}z.grib2.f240
  #tmp10=$(wgrib2 $grbfile -match "TMP:surface" -lon 283.31 39.18 | awk -F'=' '{print $NF}')
  #echo $thisdate, $tmp, $tmp02, $tmp04, $tmp10 >> ttt
  echo $thisdate,$tmp >> tmp_${year}${mon}.csv
  done; done
done

#cp /lfs/h1/ops/prod/com/gfs/v16.3/gfs.20250122/00/atmos/gfs.t00z.pgrb2.0p25.f000 .
#wgrib2 gfs.t00z.pgrb2.0p25.f000 -match ":(TMP:2 m above ground|TMP:surface):" -grib new_grib

# there is an analysis file for each cycle, however, the file only keep for 8 days on WCOSS
# /lfs/h1/ops/prod/com/gfs/v16.3/gfs.20250?0?/00/atmos/gfs.t00z.pgrb2.0p25.anl

