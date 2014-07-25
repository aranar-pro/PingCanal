from arduino import Arduino
import time

#b = Arduino('/dev/ttyUSB0')
b = Arduino('/dev/tty.usbmodem1411')
pin = 13

#declare output pins as a list/tuple
b.output([pin])


for i in range (0,10):
    b.setHigh(pin)
    time.sleep(1)
    print b.getState(pin)
    b.setLow(pin)
    print b.getState(pin)
    time.sleep(1)

b.close()

