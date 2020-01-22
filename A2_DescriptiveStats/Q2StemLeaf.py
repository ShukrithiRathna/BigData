''' 017-01-2020
    Shukrithi Rathna
    Assignment 2
    Q1. Generating Stem and  Leaf  Plot
'''
import matplotlib.pyplot as plt
import numpy as np

arr = [22, 21, 24, 19, 27, 28, 24, 25, 29, 28,
       26, 31, 28, 27, 22, 39, 20, 10, 26, 24,
       27, 28, 26, 28, 18, 32, 29, 25, 31, 27]

plt.figure(figsize=(6,6))
arr.sort()

stem = []   
for i in range(0,len(arr)):
    stem.append((int)(arr[i]/10))
    arr[i]=arr[i]%10
#stem.sort()
plt.stem(stem,arr,linefmt='-.')

plt.title('Stem Leaf Plot')
plt.xlabel('Range/Stems')
plt.ylabel('Points/Leaves')
plt.show()
 