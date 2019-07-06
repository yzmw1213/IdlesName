# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib.request as req
import json

url= "https://www.hinatazaka46.com/s/official/search/artist?ima=0000&link=ROBO004"

res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")

names = []
for name in soup.select(".c-member__name"):
    lastname, firstname = name.get_text(strip=True).split()
    names.append(
      {
        "last" : lastname,
        "first": firstname,
      }
    )

# 重複削除
names = list(map(json.loads,set(map(json.dumps,names))))

for name in names:
  print(name["last"] + ' ' + name["first"])
  print('\r')

