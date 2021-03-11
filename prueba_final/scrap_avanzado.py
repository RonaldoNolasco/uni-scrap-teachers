import requests as r
from bs4 import BeautifulSoup
import urllib3
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

urls = []

def todosLosDNIaString():
    with open('profe.json', 'r') as input_file:
        data = json.load(input_file)

    for value in data:
        value["dni"] = str(value["dni"])

    with open('profe_fix.json', 'w') as output_file:
        json.dump(data, output_file, indent=4)


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
    count = 0
    with open('profe_fix.json', 'r') as input_file:
        data = json.load(input_file)

    for value in data:
        nombre = value["nombres"].split(" ")[0].lower()
        apellido = value["apellidos"].split(" ")[0].lower()
        for url in urls:
            if (nombre.lower() in url.lower() and apellido.lower() in url.lower()):
                value["imgUrl"] = url
                count += 1
                break
            else:
                value["imgUrl"] = "http://www.fiis.uni.edu.pe/images/Docentes/docente.jpg"

    # VERIFICANDO CUALES NO SE AGREGARON
    noAgregados = []
    
    for url in urls:
        siEsta = False
        for value in data:
            if (url in value["imgUrl"]):
                siEsta = True
                break
        if (siEsta == False):
            noAgregados.append(url)
    
    with open('no_agregados.txt', 'w') as output_file:
        for value in noAgregados:
            output_file.write(value + "\n")

    with open('profe_fix_with_url.json', 'w') as output_file:
        json.dump(data, output_file, indent=4)

def updateSQL():
    with open('profe_fix_with_url.json', 'r') as input_file:
        data = json.load(input_file)

    # CREANDO EL SQL DE LOS QUE SI ESTAN MATCHEADOS
    with open('updatesql.txt', 'w') as output_file:
        for i in range(0,len(data)):
            output_file.write("update file set public_url = '" + data[i]["imgUrl"] + "' where id = " + str(i+3) + ";\n")

    # CREANDO EL SQL DE LOS QUE NO ESTAN MATCHEADOS
    noAgregados = []

    with open('no_agregados.txt', 'r') as input_file:
        with open('updatesql_no_agregados.txt', 'w') as output_file:
            for value in input_file.readlines():
                output_file.write("update file set public_url = '" + value[:-1] + "' where id = ;\n")

def main():
    #SOLO SE EJECUTA UNA VEZ
    #todosLosDNIaString()

    #obteniendoImagenes()
    almacenarImagenes()
    creandoJson()

    updateSQL()

if __name__ == "__main__":
    main()