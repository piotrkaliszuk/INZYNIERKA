import numpy as np
srodowisko_wiersze = 12
srodowisko_kolumny = 12
wartosciQ = np.zeros((srodowisko_wiersze, srodowisko_kolumny, 4)) #Q
#print(wartosciQ)
kierunki = ['up', 'down', 'right', 'left']

nagrody = np.full((srodowisko_wiersze, srodowisko_kolumny), -100)
nagrody[0, 8] = 100
przejścia = {}
przejścia[1] = [1, 2, 3,4,5,6,7,8]
przejścia[2] = [0, 1, 2,3,4,5,6,7,8]
przejścia[3] = [2, 3,4,5,6,7,8,9,10]
przejścia[4] = [1, 2, 3, 4,5,6,7,8,9,10]
przejścia[5] = [1, 2, 3, 4,5,6,7,10,11]
przejścia[6] = [1, 2, 3, 4,5,6]
przejścia[7] = [1, 2, 3, 4,5,6,7,8]
przejścia[8] = [3, 4,5,6,7,8,9,10]
przejścia[9] = [2, 3, 4,5,6,7,8]
przejścia[10] = [1, 2, 3, 4,5,6]


for wiersz in range(1, 11): #Podstawienie -1 pod odpowiednie indeksy
    for kolumna in przejścia[wiersz]:
        nagrody[wiersz, kolumna] = -1

for row in nagrody:
  print(row)

def czy_przeszkoda(curr_wiersz, curr_kolumna):
  if nagrody[curr_wiersz, curr_kolumna] == -1:
    return False
  else:
    return True

def losowy_start(): #wygenerowanie losowego startu
  wiersz = np.random.randint(srodowisko_wiersze)
  kolumna = np.random.randint(srodowisko_kolumny)
  while czy_przeszkoda(wiersz, kolumna):
    wiersz = np.random.randint(srodowisko_wiersze)
    kolumna = np.random.randint(srodowisko_kolumny)
  return wiersz, kolumna

def akcja(wiersz, kolumna, eps): #wybór indeksu odpowiedzialnego za kierunek
  if np.random.random() < eps:
    return np.argmax(wartosciQ[wiersz, kolumna])
  else:
    return np.random.randint(4)

def zmiana_pozycji(wiersz, kolumna, akcja): #zmiana indeksów
  nowy_wiersz = wiersz
  nowa_kolumna = kolumna
  if kierunki[akcja] == 'up' and wiersz > 0:
    nowy_wiersz -= 1
  elif kierunki[akcja] == 'right' and kolumna < srodowisko_kolumny - 1:
    nowa_kolumna += 1
  elif kierunki[akcja] == 'down' and wiersz < srodowisko_wiersze - 1:
    nowy_wiersz += 1
  elif kierunki[akcja] == 'left' and kolumna > 0:
    nowa_kolumna -= 1
  return nowy_wiersz, nowa_kolumna

def droga(wiersz, kolumna): #wyznaczenie najkrótszej drogi
    curr_wiersz, curr_kolumna = wiersz, kolumna
    najkrótsza_droga = []
    najkrótsza_droga.append([curr_wiersz, curr_kolumna])
    while not czy_przeszkoda(curr_wiersz, curr_kolumna):
        kierunek = akcja(curr_wiersz, curr_kolumna, 1)
        curr_wiersz, curr_kolumna = zmiana_pozycji(curr_wiersz, curr_kolumna, kierunek)
        najkrótsza_droga.append([curr_wiersz, curr_kolumna])
    return najkrótsza_droga

eps = 0.9
gamma = 0.8
alfa = 0.8
for x in range(1000): #główna pętla
    wiersz, kolumna = losowy_start()
    #print(wiersz,kolumna)
    while not czy_przeszkoda(wiersz, kolumna):
        kierunek = akcja(wiersz, kolumna, eps) #kierunek wykonania akcji
        #print(kierunek)
        stary_wiersz, stara_kolumna = wiersz, kolumna #zapis wartości
        wiersz, kolumna = zmiana_pozycji(wiersz, kolumna, kierunek) #wykonanie akcji przemieszczenie
        nagroda = nagrody[wiersz, kolumna] #pobranie nagrody z tablicy
        stareQ = wartosciQ[stary_wiersz, stara_kolumna, kierunek] #zapis starej wartosci Q, potrzebnej do wzoru
        noweQ = stareQ + (alfa * (nagroda + (gamma * np.max(wartosciQ[wiersz, kolumna])) - stareQ)) #wyliczenie wzóru
        wartosciQ[stary_wiersz, stara_kolumna, kierunek] = noweQ #podpisanie nowej wartości do tablicy
        #print(wartosciQ)
print(wartosciQ)

print(droga(10,2))
