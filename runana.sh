#!/bin/bash -l
#BSUB -P RRFS-T2O
#BSUB -eo test.err
#BSUB -oo test.out
#BSUB -J fv3.c768
#BSUB -W 00:10
#BSUB -q "dev2"
#BSUB -n 320
#BSUB -R span[ptile=20]
#BSUB -R affinity[core(2):distribute=balance]
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
cd /gpfs/dell1/ptmp/Shun.Liu/stmp/tmpnwprd/testdomain_rrfs_conus_3km/2021081106/anal_gsi_spinup
#EXEC=/gpfs/dell6/emc/modeling/noscrub/Shun.Liu/fv3lamda/regional_workflow/exec/regional_chgres_cube.x
EXEC=/gpfs/dell6/emc/modeling/noscrub/Shun.Liu/fv3lamda/regional_workflow/exec/regional_gsi.x

mpirun $EXEC <gsiparm.anl > outtest 2> errtest
