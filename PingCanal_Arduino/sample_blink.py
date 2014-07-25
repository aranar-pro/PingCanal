from arduino import Arduino
import time

#b = Arduino('/dev/ttyUSB0')
b = Arduino('/dev/tty.usbmodem1411')
pin = (1, 2, 3, 4, 5, 6, 7, 8)
#pin = 13

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

