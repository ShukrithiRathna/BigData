''' 07-01-2020
    Shukrithi Rathna
    Assignment 1
    Q6. Generating Pie Chart
'''

import numpy as np
import os #to change working directory
import pandas as pd #to work with dataframes
import matplotlib.pyplot as plt

data = {'Activity': ['Studying', 'Sleeping', 'Playing', 'Hobbies','Others'],
        'Time Spent': [33,30,18,5,14],}
df = pd.DataFrame(data, columns = ['Activity', 'Time Spent'])
	
	
# Create a list of colors (from iWantHue)
colors = ["#E13F29", "#D69A80", "#D63B59", "#AE5552", "#CB5C3B", "#EB8076", "#96624E"]

# Create a pie chart
plt.pie(   df['Time Spent'],labels=df['Activity'], colors=colors, autopct='%1.1f%%', startangle=90)

plt.show()

