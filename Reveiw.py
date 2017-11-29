import urllib.request, urllib.parse, urllib.error
import re
from bs4 import BeautifulSoup

url = input('Enter -') 
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('span')
# raw_info -- dictionary to store all info
raw_info = {}
# a_info --- dictionary to store analysis info
a_info = {}



# review info part

# In this case, since we need to seperate the 30 day review with the all time review,
# the basic concept is to first store the raw information to the raw_info dictionary
# then extract information that is related to analysis from raw_info so we can name them differently
raw_info['review'] = []
for tag in tags:
    if tag.get('class',[]) == ['nonresponsive_hidden', 'responsive_reviewdesc']:
       raw_info.get('review',[]).append(str(tag))
a_info['review'] = {}        
a_info['review']['30Day'] = re.findall('[0-9,]+',raw_info['review'][0])[0:2]
a_info['review']['AllTime'] = re.findall('[0-9,]+',raw_info['review'][1])
print (a_info['review'])
