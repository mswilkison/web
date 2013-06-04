from bs4 import BeautifulSoup
from urllib2 import urlopen

myAddress = "http://RealPython.com/practice/profiles.html"
htmlPage = urlopen(myAddress)
htmlText = htmlPage.read()

mySoup = BeautifulSoup(htmlText)

links = mySoup.find_all("a")

for l in links:
    linkAddress = "http://RealPython.com/practice/" + l['href']
    linkPage = urlopen(linkAddress)
    linkText = linkPage.read()
    linkSoup = BeautifulSoup(linkText)
    print linkSoup.get_text()
