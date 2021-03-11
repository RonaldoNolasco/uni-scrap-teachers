import requests as r
from bs4 import BeautifulSoup
import urllib3
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

urls = []

def obteniendoImagenes():
    for i in range(0,127,18):
        url = "http://www.fiis.uni.edu.pe/plana-docente?start=" + str(i)
        response = r.get(url, verify=False)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')

        for i in range (2,20-(i==126)*9):
            if (str(soup.find_all('img')[i]["src"]) != "/images/Docentes/docente.jpg") and (str(soup.find_all('img')[i]["src"]) != "/images/Docentes/luis_zuloaga.jpg"):
                urls.append("http://www.fiis.uni.edu.pe" + str(soup.find_all('img')[i]["src"]))

    with open("urls.txt", "w", encoding="utf-8") as file:
        for i in range(0,len(urls)):
            file.write(urls[i] + "\n")

def almacenarImagenes():
    with open("urls.txt", "r", encoding="utf-8") as file:
        for value in file.read().split('\n'):
            urls.append(value)

    urls.pop(len(urls)-1)

def creandoJson():
    print("xd")


def main():
    #obteniendoImagenes()
    almacenarImagenes()
    #creandoJson()

    print(len(urls))

if __name__ == "__main__":
    main()