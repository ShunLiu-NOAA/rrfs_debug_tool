#!/bin/bash

cd /lfs/h2/emc/ptmp/emc.lam/Shun.Liu/blending

#/lfs/f2/t2o/ptmp/emc/Shun.Liu/stmp/rrfs/rrfs_ics_19_v1.0/enkf/m001
module load netcdf nccmp
module load gsl nco

# Test preblending
filename="preblend.nc"
new="/lfs/f2/t2o/ptmp/emc/Shun.Liu/stmp/rrfs_ics_19_v1.0_new_1/enkf/m001/rrfs_enkf_make_ics_mem001_19.213386917.cbqs01/cold2warm_all.nc"
old="/lfs/f2/t2o/ptmp/emc/Shun.Liu/stmp/rrfs_ics_19_v1.0_old_rerun/enkf/m001/rrfs_enkf_make_ics_mem001_19.213268086.cbqs01/out.atm.tile7.nc"
echo "new: $new"
echo "old: $old"
vars="u_cold2fv3,v_cold2fv3,t_cold2fv3,delp_cold2fv3,sphum_cold2fv3"
ncdiff -O -v "${vars}" ${new} ${old} new_minus_old."${filename}"

echo "Diff file: new_minus_old.${filename}"
