
"""
Created on Wed Jan  8 20:56:40 2020

@author: Shukrithi Rathna
Q7 Set up an absolute Grader
"""


import random

midsem = []
endsem = []
ass = []
total= []
grade = []

for i in range(20):
    midsem.append(random.randint(0,30))
    endsem.append(random.randint(0,50))
    ass.append(random.randint(0,20))
    total.append(midsem[i]+endsem[i]+ass[i])
    if (total[i]>=90):
        grade.append('S')
    elif (total[i]>=80):
        grade.append('A')
    elif (total[i]>=70):
        grade.append('B')
    elif (total[i]>=60):
        grade.append('C')
    elif (total[i]>=50):
        grade.append('D')
    else :
        grade.append('E')

Sum = 0
for i in range(20):
    Sum = Sum + total[i]
Mean = Sum/20
for i in range(20):
    if(total[i]<(0.5*Mean)):
        grade[i] = 'U'
p
freq = {}
for item in grade:
    if(item in freq):
        freq[item] +=1
    else:
        freq[item] = 1
    
print(freq)




