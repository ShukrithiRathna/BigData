
"""
Created on Wed Jan  8 20:40:25 2020

@author: Shukrithi Rathna
 
Q3. Standard Deviation
"""
import random
import math

x=[]
y=[]
Max=100
Sum=0
for i in range(20):
    x.append(random.randint(5,Max))
    y.append((2*x[i])+3)
    Sum = Sum+y[i]
Mean = Sum/20
SSE = 0
for i in range(20):
    SSE = (y[i]-Mean)**2
StdDev = math.sqrt(SSE/19)
print(x)
print(y)
print(StdDev)
    