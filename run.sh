
alldate='20220123 20220124'
allcyc='00 12'

for mydate in $alldate
do
  for cyc in $allcyc
  do 
    rpten.sh $mydate $cyc
  done
done
