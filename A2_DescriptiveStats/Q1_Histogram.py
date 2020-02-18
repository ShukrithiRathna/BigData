import matplotlib.pyplot as plt
import numpy as np

age = [7, 9, 27, 28, 55, 45, 34, 65, 54, 67,
       34, 23, 24, 66, 53, 45, 44, 88, 22, 33,
       55, 35, 33, 37, 47, 41,31, 30, 29, 12]

mean = np.mean(age)
median = np.median(age)
stddev = np.std(age)

skew = (3*(mean-median)/stddev)
print("Mean: ",mean,"Median: ", median,"Std Dev: ",stddev,"Skew: ",skew)
plt.figure(figsize=(6,6))

plt.hist(x=age, bins=8, range=None, density=None, weights=None, 
        cumulative=False, bottom=None, histtype='bar', align='mid', 
        orientation='vertical', rwidth=0.9, log=False, color=None, 
        label='Age of customers', stacked=False, normed=None, data=None)

plt.xlabel('Age of customers', fontsize= 13 );
plt.ylabel(' Count ', fontsize= 13);
plt.title('Distribution of age of Customers', fontsize=15);

plt.show()

