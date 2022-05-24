#!/bin/bash
shopt -s extglob
fl=`ls -1d 2*`
for ifl in $fl
do 
  echo $ifl
  cd $ifl
  rm -fr F*
  rm -fr l*
  if [ -d anal_gsi_spinup ]
  then
    cd ./anal_gsi_spinup
    rm --f !(fort.*)
    cd ..
  fi
  if [ -d anal_gsi ]
  then
    cd ./anal_gsi
    rm --f !(fort.*)
    cd ..
  fi
  cd ..
done
