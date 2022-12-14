import serial
import keyboard
ser = serial.Serial('COM2', 115200)
x = True
flaga = 0
stop = 0
while x == True:
    if keyboard.read_key() == "r":
        sensor_data = []
        datatofiletxt = []
        flaga = flaga + 1
        stop = 0
        ser.flushInput()
        while stop < 120:
            getData = ser.readline()
            dataString = getData.decode('utf-8')
            sensor_data.append(dataString)
            stop = len(sensor_data)
        for i in range(len(sensor_data)):
            datatofile = sensor_data[i][:-2]
            datatofiletxt.append(datatofile)
        print(f"Przebieg{flaga}: {datatofiletxt}")
        file = open(f"Przebieg{flaga}.txt", 'x')
        file.write('\n'.join(datatofiletxt))
        file.close()

    if keyboard.read_key() == "q":
        x = False




