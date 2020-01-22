
"""
Created on Wed Jan  8 20:53:42 2020

@author: Shukrithi Rathna

Q4 Plot bar graph
"""

import random
import math
import matplotlib.pyplot as plt

y=[167.65,167,172,175,165,167,168,167,167.3,170,167.5,170,167,169,172]
orig=y.copy()
y.sort()
Sum=0
for i in range(15):
    Sum = Sum+y[i]
Mean = Sum/15
SSE = 0
for i in range(15):
    SSE = (y[i]-Mean)**2
StdDev = math.sqrt(SSE/15)
Median = y[7]
Mode = y[14]
Skew = (Mean-Mode)/StdDev
print(StdDev,Median,Mode,Skew)
plt.bar(x=range(15),height=orig)
plt.hist(x = range(15),bins= 40,color='red')
plt.show()

