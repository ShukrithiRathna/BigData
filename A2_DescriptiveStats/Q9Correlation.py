''' 18-01-2020
    Shukrithi Rathna
    Assignment 2
    Q9. Correlation
'''

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

temp = [98,87,90,85,95,75]
sales = [15,12,10,10,16,7]

sns.scatterplot(x=temp,y=sales)
plt.show()
corr_coeff = np.corrcoef(x=temp,y=sales)

print(corr_coeff)

