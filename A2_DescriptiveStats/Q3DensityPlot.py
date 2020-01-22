''' 17-01-2020
    Shukrithi Rathna
    Assignment 2
    Q4. Generating Density and Rug Plots
'''


import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

water = [3.2, 3.5, 3.6, 2.5, 2.8, 5.9, 2.9, 3.9, 4.9, 6.9, 7.9, 8.0, 3.3, 6.6, 4.4]
beverages = [2.2, 2.5, 2.6, 1.5, 3.8, 1.9, 0.9, 3.9, 4.9, 6.9, 0.1, 8.0, 0.3, 2.6, 1.4]
plt.figure(figsize=(6,6))
sns.distplot(water,hist=False,rug=True,label='Water')
sns.distplot(beverages,hist=False,rug=True,label='Beverages')
plt.show()