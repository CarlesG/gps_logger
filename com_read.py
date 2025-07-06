# SCRIPT TO READ THE GPS DATA FROM COM
#
# TODO: save log in a file 

import serial
import time
import serial.tools.list_ports as port_list
import sys

# Search the com of gps device
ports = list(port_list.comports())
gps_device = "Prolific PL2303GC USB"
print("PRINTING COM DEVICES........")
for p in ports:
    print(p)
    a = str(p)
    if a.__contains__(gps_device):
        com = a[0:4]
print('Status:\n')
if 'com' in locals():
    print('Device connected! in ' + com)
else:
    print('Device not found!')
print("\n................\n")

# Configuration of the port
ser = serial.Serial(port=com, baudrate = 4800, bytesize = 8, timeout = 2, stopbits=serial.STOPBITS_ONE)
serialString =""
file_out_name = 'log.txt'
# Print serial port on the terminal
serialString = ser.readline()
while 1:
    try:
        serialString = ser.readline()
        print(serialString.decode("Ascii").replace("\n", ""))
        with open(file_out_name, "a+") as file:
            file.writelines(serialString.decode("Ascii").replace("\n", ""))
    except KeyboardInterrupt:
        ser.close() 
        print("Keyboard Interruption caught. Exiting program----")
        sys.exit(0)
    except: 
        pass
