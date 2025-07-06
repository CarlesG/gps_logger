# Script for parsing data from NMEA 

import pynmea2

file = open('log.txt',encoding='utf-8')

for line in file.readlines():
    try:
        #print(line)
        msg = pynmea2.parse(line.replace("\n", "").replace("\r", "")) 
        if line.__contains__("$GNGGA"):
            #print(repr(msg))
            print(msg)
            print(msg.timestamp, msg.latitude,  msg.longitude)
    except pynmea2.ParseError as e: # a veces ocurre que hay campos que no consigue parsear
        #print('Parse error: {} '.format(e))
        pass
