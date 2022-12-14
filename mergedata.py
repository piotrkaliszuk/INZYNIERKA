import os

directory = 'trzyosoby'
with open('DATATRZY.txt', 'w') as outfile:
    for filename in os.listdir(directory):
        print(filename)
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            with open(f'{directory}/{filename}') as infile:
                outfile.write(infile.read())
            outfile.write("\n")




