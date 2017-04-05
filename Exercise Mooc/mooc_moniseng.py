#python 2.7
import math
def isprime(x):
    'Test x is prime?'
    k=int(math.sqrt(x))
    for i in range(2,k+1):
        if x%i==0:
            return False
            break
    else:
        return True

p=2;count=0    
while count<5:
   m=2**p-1
   if isprime(m) and isprime(p):
        print 'The number is :',p, ' and the number of Monisen is:', m
        p=p+1
        count=count+1
   else:
        print 'The number is :',p
        p=p+1
print 'count is: ',count
