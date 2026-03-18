from time import sleep

def calculadora():
    print("Bienvenido a la calculadora de subredes via VLSM en ipv4")
    print("Creado por Eligabriel Espinal Hernandez")
    print("==========================================================")
    
    while True:
        try:
            prefijo = int(input("Ingrese el prefijo de subred sin el simbolo '/'. (Ejemplo: 24): "))
            if prefijo > 0 and prefijo <= 32:
                break
            else:
                print("Error: El prefijo debe estar entre 0 y 32.")
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")

    print("El prefijo ingresado es: /" + str(prefijo))
    sleep(2)
    print("Calculando los datos...")

    # Obtener la mascara de subred
    mascaras = {
        0: "0.0.0.0", 1: "128.0.0.0", 2: "192.0.0.0", 3: "224.0.0.0",
        4: "240.0.0.0", 5: "248.0.0.0", 6: "252.0.0.0", 7: "254.0.0.0",
        8: "255.0.0.0", 9: "255.128.0.0", 10: "255.192.0.0", 11: "255.224.0.0",
        12: "255.240.0.0", 13: "255.248.0.0", 14: "255.252.0.0", 15: "255.254.0.0",
        16: "255.255.0.0", 17: "255.255.128.0", 18: "255.255.192.0", 19: "255.255.224.0",
        20: "255.255.240.0", 21: "255.255.248.0", 22: "255.255.252.0", 23: "255.255.254.0",
        24: "255.255.255.0", 25: "255.255.255.128", 26: "255.255.255.192", 27: "255.255.255.224",
        28: "255.255.255.240", 29: "255.255.255.248", 30: "255.255.255.252",
        31: "255.255.255.254", 32: "255.255.255.255"
    }
   

    mascara_subred = mascaras.get(prefijo, "Prefijo no valido")
    sleep(5)
    print("La mascara de subred es: " + mascara_subred)
    print("==========================================================")

    # Calculos de ips totales y asignables
    ipst = 2 ** (32 - prefijo)
    ipsa = ipst - 2
    sleep(2)
    print("El numero total de ips es: " + str(ipst))
    print("===========================================================")
    sleep(2)
    print("El numero de ips asignables es: " + str(ipsa))
    print("===========================================================")

while True:
    calculadora()
    
    print("           ¿Qué deseas hacer?     ")
    print("  1. Realizar otro cálculo        ")
    print("  2. Salir del programa           ")
    print("===========================================================")

    while True:
        opcion = input("Seleccione una opción (1 o 2): ").strip()
        if opcion == "1":
            print("\nReiniciando calculadora...\n")
            sleep(1)
            break
        elif opcion == "2":
            print("\nGracias por usar la calculadora. ¡Hasta luego!")
            exit()
        else:
            print("Opción no válida. Por favor ingrese 1 o 2.")
