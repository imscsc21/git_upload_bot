#!/bin/sh
cd $2
git config --global user.name "hsh97Erica"
git config --global user.email "imscs21@hanyang.ac.kr"
time=$((60*60*6))#loop per 6 hours
for i in $(seq 1 99999)
do
echo $i 번째 구동
cd $1
python3 wordchain.py
cd $2
git pull origin

#echo $(date) >> a.test
#echo "" >>a.test
git add chain.txt
git commit -m "upload $(date)"
git push origin master
sleep $time
done
