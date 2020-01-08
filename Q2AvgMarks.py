"""
Created on Wed Jan  8 21:53:44 2020

@author: Shukrithi Rathna
Q2 Find average of marks

"""
import matplotlib.pyplot as plt
import numpy as np
import os #to change working directory
import pandas as pd #to work with dataframes/

marks = {}
rollstring="CSED2000"
rollnum=1
for i in range(19):
    if rollnum%2==0:
        marks[rollstring+str(rollnum)] = 25+((rollnum+8)%10)
    else:
        marks[rollstring+str(rollnum)] = 25+((rollnum+7)%10)
    rollnum+=1

mark=list((marks.values()))
print(np.mean(mark),np.median(mark))