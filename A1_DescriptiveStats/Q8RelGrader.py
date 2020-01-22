
"""
Created on Wed Jan  8 20:58:35 2020

@author: Shukrithi Rathna

Q8 Set up a relative grader
"""


import random

midsem = []
endsem = []
ass = []
total= []
grade = []

for i in range(20):
    midsem.append(random.randint(15,30))
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

freq = {}
for item in grade:
    if(item in freq):
        freq[item] +=1
    else:
        freq[item] = 1
        
final = {}
for i in range(20):
    final[total[i]] = grade[i]
    
PassSum = 0
PassCnt = 0
for item in total:
    if(item>0.5*Mean):
        PassSum += item
        PassCnt = PassCnt + 1
PassMean = PassSum/PassCnt

X = PassMean - Mean
MaxMark = max(total)
SCutoff = MaxMark - 0.1*(MaxMark - PassMean)
Y = SCutoff - PassMean
ACutoff = PassMean + (Y*(5/8))
BCutoff = PassMean + (Y*(2/8))
CCutoff = PassMean - (X*(2/8))
DCutoff = PassMean - (X*(5/8))
ECutoff = 0.5*Mean

for i in range(20):
    if(total[i]>SCutoff):
        grade[i] = 'S'
    elif(total[i]>ACutoff):
        grade[i] = 'A'
    elif(total[i]>BCutoff):
        grade[i] = 'B'
    elif(total[i]>CCutoff):
        grade[i] = 'C'
    elif(total[i]>DCutoff):
        grade[i] = 'D'
    elif(total[i]>ECutoff):
        grade[i] = 'E'
    
Freq = {}
for item in grade:
    if(item in Freq):
        Freq[item] +=1
    else:
        Freq[item] = 1

Final = {}
for i in range(20):
    Final[total[i]] = grade[i]
print(Freq)