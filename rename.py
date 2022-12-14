import os

directory = 'trzyosoby'
i = 0
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        i += 1
        old_name = f
        new_name = f'Przebiegtrzy{i}.txt'
        os.rename(old_name, new_name)