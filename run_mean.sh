
alldate='20220207 20220206 20220202 20220203 20220204 20220205'
allcyc='00 12'

for mydate in $alldate
do
  for cyc in $allcyc
  do 
    rpten_mean.sh $mydate $cyc
  done
done
