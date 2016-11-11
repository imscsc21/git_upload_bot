#!/bin/sh
cd $2
git config --global user.name "hsh97Erica"
git config --global user.email "imscs21@hanyang.ac.kr"
#time=$((60*60*6))
for i in $(seq 1 999999)
do
echo try loop $i times
cd $2
git pull origin
cd $1
python3 wordchain.py
cd $2

git add chain.txt
git commit -m "upload $(date)"
git push origin master
cd $1
tm=$(python3 getConsoleSleepTime.py)
echo $tm seconds sleep
sleep $tm
done