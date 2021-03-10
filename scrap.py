import requests as r
from bs4 import BeautifulSoup
import urllib3
import json


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#Hallando los códigos de todos los profes
facultades = ['A','C','E','G','I','L','M','N','P','Q','S']
hojasPorFacultad = [19,30,20,16,19,21,23,21,9,13,19]

url = "https://www.orce.uni.edu.pe/profFacultad.php?flag=profFacu&facul=A&pag=1"

cookies = dict(PHPSESSID='4pcpkms76g5r9f8jki1a5s7292')

response = r.get(url, cookies=cookies)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')
print(soup)
