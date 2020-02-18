
"""
Created on Tue Jan 21 15:09:18 2020

@author: Shukrithi Rathna
"""


#%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')
import numpy as np

def ConPlot(x,y):
    return pow((x**2+y**2),0.5)

x=np.linspace(-3,3,100)
y=np.linspace(-3,3,100)
X, Y = np.meshgrid(x, y)
Z = ConPlot(X, Y)
plt.contour(X, Y, Z, colors='black');