import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def check(tab):
    for i,val in enumerate(tab):
        if len(val) != 3:
            print(i)
arr1 = []
arr2 = []
arr3 = []
text_file = open("DATAJEDNA.txt", "r")
lines = text_file.readlines()
for iter,line in enumerate(lines):
    x = line[:-2]
    x = x.split(',')
    print(iter)
    for j , val in enumerate(x):
        if val == '':
            continue
        else:
            x[j] = float(val)
    arr1.append(x)
text_file = open("DATADWIE.txt", "r")
lines = text_file.readlines()
for line in lines:
    x = line[:-2]
    x = x.split(',')
    for j , val in enumerate(x):
        if val == '':
            continue
        else:
            x[j] = float(val)
    arr2.append(x)
#print(arr2)
text_file = open("DATATRZY.txt", "r")
lines = text_file.readlines()
for line in lines:
    x = line[:-2]
    x = x.split(',')
    for j , val in enumerate(x):
        if val == '':
            continue
        else:
            x[j] = float(val)
    arr3.append(x)
print("check1")
check(arr1)
print("check2")
check(arr2)
print("check3")
check(arr3)
scaler = MinMaxScaler()
X = arr1 + arr2 + arr3
X_train_minmax = scaler.fit_transform(X)

y1 = np.ones((12000, 1))
y2 = np.ones((12000, 1))
y2[np.where(y2==1)]=2
y3 = np.ones((12000, 1))
y3[np.where(y3==1)]=3
yy = np.vstack([y1, y2])
Y = np.vstack([yy,y3])
Y = pd.DataFrame(Y)
label = Y.to_numpy()