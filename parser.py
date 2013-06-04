from bs4 import BeautifulSoup
from urllib2 import urlopen

myAddress = "http://RealPython.com/practice/dionysus.html"
htmlPage = urlopen(myAddress)
htmlText = htmlPage.read()

mySoup = BeautifulSoup(htmlText)
