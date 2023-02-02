#!/usr/local/bin/python3.6
try:
    import serial
    import matplotlib.pyplot as plt
except Exception as exception:
    print(exception)
    print("FATAL ERROR: Make sure that the following package are installed")
    print(" - pyserial")
    exit()


serial_obj = serial.Serial("/dev/cu.usbmodem14401", 115200)
serial_obj.timeout = 1
WIN_SIZE = 1000
time = range(WIN_SIZE)
data = [0 for i in range(WIN_SIZE)]

scope, = plt.plot(time, data)
plt.xlim((0, WIN_SIZE))
plt.ylim((0, 1024))

while True:
    for index in range(WIN_SIZE):
        data[index] = int(serial_obj.readline().decode('utf-8'))
        scope.set_data(time, data)
    plt.pause(0.001)

serial_obj.close()
