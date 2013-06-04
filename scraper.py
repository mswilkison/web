import re
from urllib.request import urlopen

myAddress = "http://RealPython.com/practice/dionysus.html"
htmlPage = urlopen(myAddress)
htmlText = htmlPage.read().decode('utf-8')

matchResults = re.search("<title .*?>.*</title .*?>", htmlText,
			 re.IGNORECASE)
title = matchResults.group()
title = re.sub("<.*?>", "", title)
print(title)
