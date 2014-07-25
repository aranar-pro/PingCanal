from arduino import Arduino
import time

#b = Arduino('/dev/ttyUSB0')
b = Arduino('/dev/tty.usbmodem1411')
pin = 9

#declare output pins as a list/tuple
b.output([pin])
b.turnOff()

i=0
while(i<10):
    b.setHigh(9)
    time.sleep(1)
    b.setLow(9)
    time.sleep(1)
    i+=1

b.close()


