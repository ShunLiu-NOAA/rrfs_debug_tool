#!/bin/bash -l
#BSUB -P RRFS-T2O
#BSUB -eo test.err
#BSUB -oo test.out
#BSUB -J fv3.c768
#BSUB -W 00:45
#BSUB -q "dev"
#BSUB -n 700 
#BSUB -R span[ptile=28]
##BSUB -R affinity[core(2):distribute=balance]
#
set -x

. /usrx/local/prod/lmod/lmod/init/sh

ulimit -s unlimited
ulimit -a

export HOMEfv3=/gpfs/dell6/emc/modeling/noscrub/emc.campara/fv3lamda/regional_workflow
export PARMfv3=$HOMEfv3/parm
export EXECfv3=$HOMEfv3/exec
export USHfv3=$HOMEfv3/ush
export UTILfv3=$HOMEfv3/util/ush
export LD_LIBRARY_PATH="/gpfs/dell6/emc/modeling/noscrub/Eric.Rogers/fv3lam_for_dellp3.5/sorc/regional_forecast.fd/ccpp/lib/${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"

set -x -u -e
date

. ${HOMEfv3}/rocoto/machine-setup.sh
export machine=wcoss_dell_p3.5

if [ "$machine" = "wcoss_dell_p3" ] ; then
  . /usrx/local/prod/lmod/lmod/init/sh
elif [ "$machine" = "wcoss_dell_p3.5" ] ; then
  . /usrx/local/prod/lmod/lmod/init/sh
elif [ "$machine" = "wcoss_cray" ] ; then
  . /opt/modules/default/init/sh
elif [ "$machine" = "hera" ] ; then
  . /apps/lmod/lmod/init/sh
elif [ "$machine" = "jet" ] ; then
  . /apps/lmod/lmod/init/sh
fi

jobpre=regional_firstgue
module use ${HOMEfv3}/modulefiles/wcoss_dell_p3.5
jobpre=$(echo ${job} | cut -c1-17)
if [ "${jobpre}" = "regional_forecast" ]; then
  module load fv3
elif [ "${jobpre}" = "regional_bufrpost" ]; then
  module load bufr
elif [ "${jobpre}" = "regional_post_con" ]; then
  module load post
elif [ "${jobpre}" = "regional_firstgue" ]; then
  module load chgres_cube
elif [ "${jobpre}" = "regional_make_bc_" ]; then
  module load chgres_cube
elif [ "${jobpre}" = "regional_postgoes" ]; then
  module load post
else
  module load regional
fi
module list

exec "$@"

#cd /gpfs/dell5/ptmp/Shun.Liu/fv3lamda/tmpnwprd/regional_firstguess_2021081112
#cd /gpfs/dell1/ptmp/Shun.Liu/stmp/tmpnwprd/rrfs_NA_3km_retro/2021111806/anal_gsi_spinup
#cd /gpfs/dell1/ptmp/Shun.Liu/stmp/tmpnwprd/rrfs_NA_3km/2021121206/anal_gsi_spinup
cd /gpfs/dell1/ptmp/Shun.Liu/regional_gsianl_tm06_2022012712
#EXEC=/gpfs/dell6/emc/modeling/noscrub/Shun.Liu/fv3lamda/regional_workflow/exec/regional_chgres_cube.x
rm -f pe0*
rm -f obs_input*
cp /gpfs/dell2/ptmp/Shun.Liu/fv3lamdax/fv3lamdax.20220127/12/guess.tm06/sfc_data.tile7.nc fv3_sfcdata
cp /gpfs/dell2/ptmp/Shun.Liu/fv3lamdax/fv3lamdax.20220127/12/guess.tm06/gfs_data.tile7.nc .
ln -sf gfs_data.tile7.nc fv3_dynvars
ln -sf gfs_data.tile7.nc fv3_tracer
#EXEC=/gpfs/dell6/emc/modeling/noscrub/emc.campara/Shun.Liu/rrfs/ufs-srweather-app/bin/regional_gsi.x
#EXEC=/gpfs/dell2/emc/modeling/noscrub/Shun.Liu/fv3lamdax/regional_workflow/exec/regional_gsi.x
EXEC=/gpfs/dell2/emc/modeling/noscrub/Shun.Liu/fv3lamdax/regional_workflow/sorc1/regional_gsi.fd_06jan21_tingcode/exec/global_gsi.x

mpirun $EXEC <gsiparm.anl > outtest 2> errtest
