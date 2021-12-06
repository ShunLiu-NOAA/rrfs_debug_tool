
emc_para=/gpfs/dell2/emc/modeling/noscrub/emc.campara/fv3lamdax/regional_workflow/parm/thompson
shun_para=/gpfs/dell6/emc/modeling/noscrub/Shun.Liu/rrfs/fix/parm_RRFS_NA_3km/thompson

echo ############################
echo ############################
set -x
diff $shun_para/input_sar_da_hourly.nml_no_gsi_bdy $emc_para/input_sar_da_hourly.nml
set +x 
echo ############################
echo ############################
set -x
diff $shun_para/input_sar_da.nml_no_gsi_bdy $emc_para/input_sar_da.nml
set +x 


shun_para=/gpfs/dell6/emc/modeling/noscrub/emc.campara/Shun.Liu/rrfs/fix/parm_RRFS_NA_3km/thompson
echo ############################
echo ############################
set -x
diff $shun_para/input_sar_da_hourly.nml_no_gsi_bdy $emc_para/input_sar_da_hourly.nml
set +x 
echo ############################
echo ############################
set -x
diff $shun_para/input_sar_da.nml_no_gsi_bdy $emc_para/input_sar_da.nml
set +x 
