import math

for x in range(10000):
    r1=int(math.sqrt(x+100))
    r2=int(math.sqrt(x+268))
    if r1*r1==x+100 and r2*r2==x+268:
        print x,r1,r2

