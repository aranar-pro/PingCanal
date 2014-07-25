from arduino import Arduino
import time

#b = Arduino('/dev/ttyUSB0')
b = Arduino('/dev/tty.usbmodem1411')
pin = 9

#declare output pins as a list/tuple
b.output([pin])
b.turnOff()

while True:
    i=0
    j=0
    while (i<3):
        while(j<3):
            b.setHigh(pin)
            time.sleep(.100)
            b.setLow(pin)
            time.sleep(1)
            j+=1
        i+=1

b.close()
exit(0)

