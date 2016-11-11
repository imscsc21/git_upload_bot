import random
unit=60*60 #hour
tmp=random.randrange(0,10)
if(tmp>6):
    tmp=6
print(unit*tmp)