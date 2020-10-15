#Este programa analiza el archivo mbox-short.txt en busca de la direccion de correo que más se repite
#y retorna dicha dirección y el número de veces que esta aparece
#Hecho por Carlos Correa para el curso de Python de la plataforma Coursera


name = input("Enter file:")
#name = "mbox-short.txt"
handle = open(name)
count = dict()
for x in handle:
    line = x.rstrip()
    if not line.startswith('From: '): continue
    mail = line.split()    
    for word in mail:
        if word == mail[1]:
            count[word] = count.get(word, 0 ) + 1
most = None
cant = None
for k, v in count.items():
    if cant is None or v > cant:    
        most = k
        cant = v
print(most, cant )
