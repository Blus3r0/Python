prog = True

niño = 4400
adulto = 7700
mayor = 3300
dcto = 0.65
cantniño = 0
cantadulto = 0
cantmayor = 0
ticketn = 0
ticketad = 0
ticketmay = 0

while prog:
    try:
        ini = int(input("""Bievenido a teatro DuocUC!
    Compra de boletos:
    1.-Iniciar compra
    2.-Salir"""))
        if ini == 1:
            print("""Tarifas:
            Menores (de 7 a 12 años):  $4.400
            Adultos (de 12 a 64 años): $7.700
            Adulto mayor(65 + ):       $3.300   
            Socios del teatro cuentan con un ¡35%! descuento""")
            while prog:
                try:
                    entrada = int(input("1.-Seleccionar entrada\n2.-Terminar compra"))
                    if entrada == 1:
                        try:
                            soc = input("¿Es usted socio?(S/N)\n")
                            if soc == "S" or "s":
                                try:
                                    tipo1 = int(input("Seleccione tipo de entrada\n1.-Niños\n2.-Adulto\n3.-Adulto mayor\n"))
                                    if tipo1 == 1:
                                        ticketn = niño * dcto                                                                                
                                        cantniño += 1
                                        print(f"{cantniño} niño(s)")
                                    elif tipo1 == 2:
                                        ticketad = adulto * dcto                                        
                                        cantadulto += 1
                                        print(f"{cantadulto} adulto(s)") 
                                    elif tipo1 == 3:
                                        ticketmay = mayor * dcto                                        
                                        cantmayor +=1
                                        print(f"{cantmayor} adulto mayor(es)")
                                    else: 
                                        print("Seleccione una opción válida")
                                except:
                                    print("Seleccione una opción válida")        
                            elif soc == "N" or "n":
                                try:
                                    tipo2 = int(input("Seleccione tipo de entrada\n1.-Niños\n2.-Adulto\n3.-Adulto mayor\n"))                                    
                                    if tipo2 == 1:
                                        ticketn = niño
                                        cantniño += 1
                                        print(f"{cantniño} niño(s)") 
                                    elif tipo2 == 2:
                                        ticketad = adulto
                                        cantadulto += 1
                                        print(f"{cantadulto} adulto(s)") 
                                    elif tipo2 == 3:
                                        ticketmay = mayor
                                        cantmayor +=1
                                        print(f"{cantmayor} adulto mayor(es)")
                                    else:
                                        print("Seleccione una opción válida")    
                                except:
                                    print("Seleccione una opción válida")
                            else:
                                print("Seleccione una opción válida") 
                        except:
                            print("Seleccione una opción válida")
                    elif entrada == 2:
                        print(f"""Compra:
{cantniño} Menor(s): {cantniño * ticketn}
{cantadulto} Adulto(s): {cantadulto * ticketad}
{cantmayor} Adulto Mayor(s): {cantmayor * ticketmay}""") 
                        prog = False                            
                    else:
                        print("Seleccione una opción válida")   
                except:
                    print("Seleccione una opción válida")       
        elif ini == 2:
            print("Gracias por su visita")
            prog = False
        else: 
            print("Seleccione una opción válida")
                  
    except:
        print("Ingrese 1 para iniciar su compra o 2 para salir")
 
