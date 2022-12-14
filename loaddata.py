import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

directory = 'PRZEBIEGJEDNA'
Y = pd.DataFrame()
appended_data = []
i = 0
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        i = i + 1
        data = pd.read_csv(f"{directory}/Przebiegjedna{i}",header=None)
        appended_data.append(data)
        appended_data = pd.concat(appended_data)


print(Y)
scaler = MinMaxScaler()
#X_train_minmax = scaler.fit_transform(X)
df = pd.DataFrame(scaler.fit_transform(X))
#print(df)