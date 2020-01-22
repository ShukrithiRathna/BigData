
"""
Created on Wed Jan  8 20:59:59 2020

@author: Shukrithi Rathna

Q9 Histogram of heights
"""
import matplotlib.pyplot as plt
import seaborn as sns


y = [79,71,89,57,76,64,82,82,67,80,81,65,73,79,79,60,58,83,74,
     68,78,80,78,81,76,65,70,76,58,82,59,73,72,79,87,63,74,90,
     69,70,83,76,61,66,71,60,57,81,57,65,81,78,77,81,81,63,71,
     66,56,62,75,64,74,74,70,71,56,69,63,72,81,54,72,91,92]

plt.hist(x = y,bins= 40,color='red')
plt.show()
sns.distplot(a=y,bins=40,color="Blue")   

