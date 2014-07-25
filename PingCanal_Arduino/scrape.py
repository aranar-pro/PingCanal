from bs4 import BeautifulSoup
from time import sleep
from arduino import Arduino
import urllib2,re


b = Arduino('/dev/tty.usbmodem1411')
pin = (1, 2, 3, 4, 5, 6, 7, 8)

b.output([pin])
b.turnOff()

def set_lights(*bridges):
    
    for j in range(0,8):
        if (bridges[j] == 0):
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
    while True:
        print "Checking bridges...\n"
        check_bridges()
        sleep(30)
    
