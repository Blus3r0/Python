suma = 0
prog = True

while prog:
    try:
        ini = int(input("¡Bienenido a pasapalabra!...\n1.-Para jugar presione 1\n2.-Para salir presione 2\n"))
        if  ini == 1:
            try:
                frase = input("Ingrese su palabra ganadora: ").lower()                       
                for x in frase:  
                    if x == "c" or x == "b" or x == "d" or x == "f" or x == "m" or x == "g":         
                        suma += 1 
                print(f"Puntaje total: {suma}")                                 
                if suma <= 3:
                    print("Lo lamento, esta vez pierde ¯\_(ツ)_/¯")
                elif suma >= 4 and suma <= 7:
                    print("Uy! su palabra casi es ganadora... ¡vuelvalo a intentar!") 
                elif suma > 7:
                    print("¡Felicidades! ha ganado 3 jumbitos 🐘🐘🐘")              
            except:
                print("Ingrese una palabra")                                               
              
        elif ini == 2:
            print("Gracias por jugar") 
            prog = False   
    except:
        print("Ingrese 1 para jugar o 2 para salir")        