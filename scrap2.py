import requests as r
from bs4 import BeautifulSoup
import urllib3
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

urls = []

for i in range(102,238):
    print(i)
    url = "http://www.fiis.uni.edu.pe/plana-docente/" + str(i)
    response = r.get(url, verify=False)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')

    if(len(soup.find_all('img')) > 2):
        if (str(soup.find_all('img')[2]["src"]) != "/images/Docentes/docente.jpg"):
            urls.append("http://www.fiis.uni.edu.pe" + str(soup.find_all('img')[2]["src"]))

    with open("urls.txt", "w", encoding="utf-8") as file:
        for i in range(0,len(urls)):
            file.write(urls[i] + "\n")
