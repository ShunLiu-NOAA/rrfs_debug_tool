module purge
module load lsf/10.1
module use /gpfs/dell3/usrx/local/dev/emc_rocoto/modulefiles/
module load ruby/2.5.1 rocoto/1.3.0rc2 #rocoto/1.2.4
rocotostat -w FV3LAM_wflow.xml -d FV3LAM_wflow.db -c all | more
#rocotostat -w FV3LAM_wflow.xml -d FV3LAM_wflow.db -c all | more
