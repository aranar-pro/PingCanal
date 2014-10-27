from bs4 import BeautifulSoup
from time import sleep
from arduino import Arduino
import urllib2,re
import serial,time,datetime,os,urllib2,sys
import serial.tools.list_ports


#Print the ports out just in case
for p in serial.tools.list_ports.comports():
    print p

try:
    for p in serial.tools.list_ports.comports():
        if re.search('Arduino',str(p[1])):
            portString = str(p[0])
except:
    print "Could not open port!"
    sys.exit()
                     
b = Arduino(portString)
pin = (1, 2, 3, 4, 5, 6, 7, 8)

b.output([pin])
b.turnOff()

def check_led_on_startup():
    i=0
    while (i<8):
        b.setHigh(pin[i])
        sleep(.1)
        b.setLow(pin[i])
        sleep(.01)
        i+=1
    sleep(2)
    i=0
    while (i<8):
        b.setHigh(pin[i])
        sleep(.1)
        b.setLow(pin[i])
        sleep(.01)
        i+=1

def set_lights(bridges):
    
    for j in range(0,8):
        if (bridges[j] == 1):
            b.setHigh(pin[j])
        else:
            b.setLow(pin[j])

def check_bridges():
    bridges = [0,0,0,0,0,0,0,0]
    bstatus = open("status.txt","w")
    url = "http://greatlakes-seaway.com/R2/jsp/NiaBrdgStatus.jsp?language=E"
    needle = "Unavailable|Available"
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page)

    result = re.findall(needle, str(soup))

    for i in range(0,8):
        if(result[i]=="Available"):
            bridges[i] = 1
        
    #print bridges
    set_lights(bridges)

    for i in range(0,8):
        if (bridges[i] == 0):
            bstatus.write("0")
        else:
            bstatus.write("1")
    bstatus.close()


if __name__ == "__main__":
    check_led_on_startup()
    try:
        while True:
            print "Checking bridges...\n"
            check_bridges()
            sleep(30)
    except KeyboardInterrupt:
        i=0
        while (i<8):
            b.setLow(pin[i])
            i+=1
        b.close()
        exit(0)

    
