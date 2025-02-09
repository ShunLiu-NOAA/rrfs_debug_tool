
#cp /lfs/h1/ops/prod/com/gfs/v16.3/gfs.20250122/00/atmos/gfs.t00z.pgrb2.0p25.f000 .
wgrib2 gfs.t00z.pgrb2.0p25.f000 -match ":(TMP:2 m above ground|TMP:surface):" -grib new_grib
