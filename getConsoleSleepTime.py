import random
unit=60*60 #hour
tmp=random.randrange(0,8)
rrange=60*30
randomvar=random.randrange(-1*rrange,rrange)
if(tmp>6):
    tmp=6
tmptime=unit*tmp
if(tmptime+randomvar>=0):
    tmptime+=randomvar
print(tmptime)