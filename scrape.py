from bs4 import BeautifulSoup
from time import sleep
import urllib2,re


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
    
