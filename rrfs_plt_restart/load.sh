#!/bin/bash

date

echo "start loading module"

#module purge
module load python/3.8.6
module use /lfs/h1/mdl/nbm/save/apps/modulefiles
module load python-modules/3.8.6
module load proj/7.1.0
module load geos/3.8.1
module load libjpeg-turbo/2.1.0
export PYTHONPATH="${PYTHONPATH}:/lfs/h2/emc/lam/noscrub/Benjamin.Blake/python:/lfs/h2/emc/lam/noscrub/Benjamin.Blake/rrfs_graphics/modulefiles"
#module load imagemagick/7.0.8-7

cd /lfs/h2/emc/lam/save/emc.lam/Shun.Liu/code/rrfs_debug_tool/rrfs_plt_restart/

#python /lfs/h2/emc/lam/save/emc.lam/Shun.Liu/code/rrfs_debug_tool/rrfs_plt_restart/plt_rrfs_nc_output.py
#python /lfs/h2/emc/lam/save/emc.lam/Shun.Liu/code/rrfs_debug_tool/rrfs_plt_restart/plt_rrfs_nc_restart.py
python /lfs/h2/emc/lam/save/emc.lam/Shun.Liu/code/rrfs_debug_tool/rrfs_plt_restart/plt_rrfs_nc_restart_surface.py
#python /lfs/h2/emc/lam/save/emc.lam/Shun.Liu/code/rrfs_debug_tool/rrfs_plt_restart/plt_rrfs_nc_mrms.py
