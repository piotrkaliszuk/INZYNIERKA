import os
import pandas as pd
import csv
import numpy as np
from sklearn.preprocessing import MinMaxScaler



arr1 = pd.read_table('DATAJEDNA.txt')
arr2 = pd.read_table('DATADWIE.txt')
arr3 = pd.read_table('DATATRZY.txt')
arr = arr1.append(arr2)
X = arr.append(arr3)
print(X)