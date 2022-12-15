import os
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
    #print(iter)
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
Xminmax = scaler.fit_transform(X)
#print(Xminmax)
#print(len(Xminmax))
zbiorX  = []
zbior120 = []
for i in range(len(Xminmax)):
    a = Xminmax[i]
    zbior120.append(a)
    if len(zbior120) == 120:
        zbiorX.append(zbior120)
        zbior120 = []
#print(len(zbiorX))
#print(zbiorX)
Y = np.ones((300,1))
for i in range(len(Y)):
    if i > 98 and i < 199:
        Y[i] = 2
    if i > 199:
        Y[i] = 3


#print(Y[299])
#print(count)
