import requests as r
from bs4 import BeautifulSoup
import urllib3
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#Hallando los códigos de todos los profes
facultades = ['A','C','E','G','I','L','M','N','P','Q','S']
hojasPorFacultad = [19,30,20,16,19,21,23,21,9,13,19]
codigos = []

cookies = dict(PHPSESSID='4pcpkms76g5r9f8jki1a5s7292')

for i in range(0,len(facultades)):
    for j in range(0,hojasPorFacultad[i]):
        url = "https://www.orce.uni.edu.pe/profFacultad.php?flag=profFacu&facul=" + facultades[i] + "&pag=" + str(j+1)
        response = r.get(url, cookies=cookies, verify=False)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup)

# 4 kind of objects Tag, NavigableString, BeautifulSoup, and Comment


# . <- navigable object


# print(soup.prettify())

# contents

#print(soup.table.tbody)
print("--------------------------------------------")
#print(soup.tbody)
#print("THEY'RE THE SAME")

#print(soup.tbody.find_all('tr'))
for x in soup.tbody.find_all('tr')[3:10]:
  tds = x.find_all('td')
  if len(tds)>1:
    print(tds[1].string)

