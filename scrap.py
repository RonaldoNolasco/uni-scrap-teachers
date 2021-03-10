import requests as r
from bs4 import BeautifulSoup
import urllib3
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

codigos = []

def hallarCodigos():
    #Hallando los códigos de todos los profes, ejecutar la primera vez
    facultades = ['A']
    hojasPorFacultad = [1]

    cookies = dict(PHPSESSID='4pcpkms76g5r9f8jki1a5s7292')

    for i in range(0,len(facultades)):
        for j in range(0,hojasPorFacultad[i]):
            url = "https://www.orce.uni.edu.pe/profFacultad.php?flag=profFacu&facul=" + facultades[i] + "&pag=" + str(j+1)
            response = r.get(url, cookies=cookies, verify=False)
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'html.parser')
            for link in soup.find_all('td'):
                if(link.get('width') == "79"):
                    codigos.append(str(link.contents[0]))

    with open("codigos.txt", "w", encoding="utf-8") as file:
        for i in range(0,len(codigos)):
            file.write(codigos[i] + "\n")

    print(codigos)

def almacenarCodigos():
    with open("codigos.txt", "r", encoding="utf-8") as file:
        for value in file.read().split('\n'):
            codigos.append(value)

    codigos.pop(len(codigos)-1)

    print(codigos)

# SEGUNDA PARTE: UTILIZANDO LOS CÓDIGOS PARA HALLAR TODOS LOS DATOS

# https://www.orce.uni.edu.pe/detaalu.php?id=07686040&op=detdoc


def main():
    #hallarCodigos()
    almacenarCodigos()

    print(codigos)


if __name__ == "__main__":
    main()




# . <- navigable object


# print(soup.prettify())

# contents

#print(soup.table.tbody)
"""
print("--------------------------------------------")
#print(soup.tbody)
#print("THEY'RE THE SAME")

#print(soup.tbody.find_all('tr'))
for x in soup.tbody.find_all('tr')[3:10]:
  tds = x.find_all('td')
  if len(tds)>1:
    print(tds[1].string)

"""