import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter -') 
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('span')
for tag in tags:
    if tag.get('class',[]) == ['nonresponsive_hidden', 'responsive_reviewdesc']:
        print(tag)
