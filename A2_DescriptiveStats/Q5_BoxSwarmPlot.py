''' 18-01-2020
    Shukrithi Rathna
    Assignment 2
    Q8. Generating Box and Swarm  Plot
'''

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

chairs = [35, 54, 60, 65, 66, 67, 69, 70, 72,
          73, 75, 76, 54, 25, 15, 60, 65, 66,
          67, 69, 70, 72, 130, 73, 75, 76]

x = plt.figure(1,figsize=(6,6))
sns.boxplot(y=chairs)
plt.title('Box Plot for number of chairs')
plt.xlabel('Chair')
plt.ylabel('Count')

y = plt.figure(2,figsize=(6,6))
sns.swarmplot(y=chairs)
plt.title('Swarm Plot for number of chairs')
plt.xlabel('Chair')
plt.ylabel('Count')
plt.show()

x.show()
y.show()

