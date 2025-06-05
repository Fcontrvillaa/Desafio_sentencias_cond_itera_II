
print(" Iniciando protocolo de Primeros Auxilios.")

responde_estimulos = input("¿La persona responde a estímulos? (sí/no): ").lower() 

if responde_estimulos == "si":
    print("Valore la necesidad de llevarlo al hospital más cercano.")
    print("Fin del protocolo.")     

elif responde_estimulos == "no":
    print("Abrir la vía aérea.") 

    # ¿Respira?
    respira = input("¿La persona respira? (sí/no): ").lower() 

    if respira == "si":
        print("Permita posición de suficiente ventilación.")
        ("Fin del protocolo.") 
    elif respira == "no":
        print("Administrar 5 ventilaciones y llamar a la ambulancia.") 

         # signos de vida 
        ambulancia_llego = False
        while not ambulancia_llego:
            signos_vida = input("¿Hay signos de vida? (sí/no): ").lower() 

            if signos_vida == "si":
                print("Reevaluar a la espera de la ambulancia.") 
            elif signos_vida == "no":
                print("Administrar compresiones torácicas hasta que llegue la ambulancia.") 

            #  ¿Llegó la ambulancia?
            llegada_ambulancia = input("¿Llegó la ambulancia? (sí/no): ").lower() 
            if llegada_ambulancia == "si":
                ambulancia_llego = True
                print("Fin del protocolo.") 
            
    else:
        print("Respuesta inválida para '¿Respira?'. Por favor, responda 'sí' o 'no'.")
else:
    print("Respuesta inválida para '¿Responde a estímulos?'. Por favor, responda 'sí' o 'no'.")

