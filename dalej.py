import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def load_csv(filepath):
    data =  []
    col = []
    checkcol = False
    with open(filepath) as f:
        for val in f.readlines():
            val = val.replace("\n","")
            val = val.split(',')
            if checkcol is False:
                col = val
                checkcol = True
            else:
                data.append(val)
    df = pd.DataFrame(data=data, columns=col)
    return df
directory = 'PRZEBIEGJEDNA'

X = load_csv(f'{directory}/Przebiegjedna1.txt')

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        X = load_csv(f'{f}')

print(X)