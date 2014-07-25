from bs4 import BeautifulSoup
import urllib2,re

bridges = [0,0,0,0,0,0,0,0]

url = "http://greatlakes-seaway.com/R2/jsp/NiaBrdgStatus.jsp?language=E"
needle = "Unavailable|Available"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page)

result = re.findall(needle, str(soup))

for i in range(0,8):
    if(result[i]=="Available"):
        bridges[i] = 1
    
print bridges
