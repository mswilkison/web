import re
from urllib.request import urlopen

myAddress = "http://RealPython.com/practice/dionysus.html"
htmlPage = urlopen(myAddress)
htmlText = htmlPage.read().decode('utf-8')

matchNameResults = re.search("Name: .*?<", htmlText, re.IGNORECASE)
name = matchNameResults.group()
name = re.sub("Name: ", "", name[0:-1])

matchColorResults = re.search("Favorite Color: .*?\n", htmlText, re.IGNORECASE)
color = matchColorResults.group()
color = re.sub("Favorite Color: ", "", color)
print(name, color)
