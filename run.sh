
alldate='20220205'
allcyc='00 12'

for mydate in $alldate
do
  for cyc in $allcyc
  do 
    rpten.sh $mydate $cyc
  done
  convert ptend_${mydate}_00.png ptend_${mydate}_12.png +append ptend_${mydate}.png
  scpfv3 ptend_${mydate}.png
done


