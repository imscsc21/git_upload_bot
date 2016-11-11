#!/bin/sh
cd $1
python3 wordchain.py
cd $2
git config --global user.name "hsh97Erica"
git config --global user.email "imscs21@hanyang.ac.kr"
time=60
$((time*=60*24))
#for i in {1..10000}
#do
git init
git pull origin
cp $1/chain.txt ./

#echo $(date) >> a.test
#echo "" >>a.test
git add chain.txt
git commit -m "upload $(date)"
git push origin master
#sleep $time
#done
