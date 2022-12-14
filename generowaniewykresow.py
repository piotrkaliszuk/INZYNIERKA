from matplotlib import pyplot as plt
import pandas as pd
import os


directory = 'Przebiegi'

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        print(f)
        df = pd.read_csv(f"Przebiegi/{filename}")
        print(df)
        plt.plot(df)
        filename = filename[:-4]
        plt.title(f'{filename}')
        plt.ylabel('Drgania')
        plt.xlabel('Próbki')
        plt.legend(['x','y','z'])
        filename = filename + ".png"
        plt.savefig(f"PrzebiegiPlot/{filename}")
        plt.show()


