"""
Created on Tue Jan 21 14:19:36 2020

@author: Shukrithi Rathna
"""
import numpy as np
import seaborn as sns
import random
sns.set(style="ticks")

#rs = np.random.RandomState(11)
#x = rs.gamma(2, size=1000)
#y = -.5 * x + rs.normal(size=1000)
x=[random.randrange(25, 50, 1) for i in range(100)] 
y=[random.randrange(10, 50, 1) for i in range(100)] 
print(x,y)
#y= random.sample(range(10, 50), 100)
sns.jointplot(x, y, kind="hex", color="#4CB391", gridsize=25)