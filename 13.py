from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import datetime
import re
html=urlopen("http://www.pythonscraping.com")
bsObj=BeautifulSoup(html.read())
#imageLocations=bsObj.findAll("img")
#print(len(imageLocations))
#for imageLocation in imageLocations:
    #print(imageLocation.attrs["src"])
#for imageLocation in imageLocations:
    #urlretrieve(imageLocation.attrs["src"],"logo"+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+".jpg")
imageLocations= bsObj.findAll("",{"src":re.compile("(\.jpg|\.gif)$")})
print(len(imageLocations))
for imageLocation in imageLocations:
    print(imageLocation.attrs["src"])
for imageLocation in imageLocations:
    urlretrieve(imageLocation.attrs["src"],"logo"+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+".jpg")
