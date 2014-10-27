from arduino import Arduino
import time,re
import serial.tools.list_ports


try:
    for p in serial.tools.list_ports.comports():
        if re.search('Arduino',str(p[1])):
            portString = str(p[0])
except:
    print "Could not open port!"
    sys.exit()

b = Arduino(portString)
pin = (1, 2, 3, 4, 5, 6, 7, 8)

#declare output pins as a list/tuple
b.output([pin])
b.turnOff()

try:
    while True:
        i=0
        while (i<8):
            b.setHigh(pin[i])
            time.sleep(.1)
            b.setLow(pin[i])
            time.sleep(.01)
            i+=1

except KeyboardInterrupt:
    while (i<8):
        b.setLow(pin[i])
        i+=1
    b.close()
    exit(0)

