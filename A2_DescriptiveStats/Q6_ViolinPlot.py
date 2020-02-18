''' 18-01-2020
    Shukrithi Rathna
    Assignment 2
    Q6. Generating Violin Plot
'''

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

std_normal = np.random.randn(50)
log_normal = np.random.lognormal(size=50)

x = plt.figure(1,figsize=(6,6))
sns.violinplot(std_normal)
plt.title('Violin plot for N(0,1)')

y = plt.figure(2,figsize=(6,6))
plt.legend()
sns.violinplot(log_normal)
plt.title('Violin plot for Lognormal(0,1)')
