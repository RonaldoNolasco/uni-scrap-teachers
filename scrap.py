

#Hallando los códigos de todos los profes
facultades = ['A','C','E','G','I','L','M','N','P','Q','S']
hojasPorFacultad = [19,30,20,16,19,21,23,21,9,13,19]

for i in range(0,len(facultades)):
    for j in range(0,hojasPorFacultad[i]):
        print (facultades[i] + " - " + str(j+1))


