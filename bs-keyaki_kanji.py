# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request as req
import json

url= "http://www.keyakizaka46.com/s/k46o/search/artist?ima=0000"

res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")

names = []
for name in soup.select(".box-member p.name"):
    lastname, firstname = name.get_text(strip=True).split()
    names.append(
      {
        "last" : lastname,
        "first": firstname
      }
    )

#重複削除
names = list(map(json.loads,set(map(json.dumps,names))))
lastnames = '('
firstnames = '('
for name in names:
  lastnames += name["last"] + '|'
  firstnames += name["first"] + '|'

lastnames = lastnames.rstrip('|') + ')'
firstnames = firstnames.rstrip('|') + ')'

print('lastnames',lastnames)
print('firstnames',firstnames)