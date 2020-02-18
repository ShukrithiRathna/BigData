'''
Data Preproccessing
Normalization - z Score, Min-Max, Decimal  Scaling
29-1-20

'''
from scipy import stats

arr = [13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25,
       25, 30,33, 33, 35, 35, 35, 35, 36, 40, 45, 46, 52, 70]

minmax = [((item-arr[0])/(arr[len(arr)-1]-arr[0])) for item in arr]

zscore = stats.zscore(arr)

decimal = [item/(10**(len(str(arr[len(arr)-1])))) for item in arr]

print("Original Array :", arr)
print("Min-Max Normalization :",minmax)
print("Z-Score Normalization :",zscore)
print("Decimal Scaling :",decimal)

