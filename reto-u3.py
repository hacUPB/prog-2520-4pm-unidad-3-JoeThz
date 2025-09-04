"""
#Crear una carpeta que se llame reto e ingresarle los 3 problemas y comenzar a hacer la tabla de analisis añadiendo el tipo de variable.

#Como estudiante de primer año de Ingeniería Aeronáutica, tu reto es diseñar un programa interactivo en Python que funcione completamente por consola y contenga un **menú principal con cuatro opciones**:

# Opción 1: Problema propuesto por el estudiante
# Opción 2: Problema propuesto por el estudiante
# Opción 3: Problema propuesto por el estudiante
# Salir del programa

#Las **primeras tres opciones** deben ser problemas relacionados con conceptos aeronáuticos generales, fuerzas sobre el avión, conceptos de vuelo, etc.
#¡Tú debes proponer y diseñar cada uno de estos tres problemas!
#El menú debe repetirse hasta que el usuario elija salir.

"""
#Diseñar un programa interactivo en Python que funcione completamente por consola y contenga un **menú principal con cuatro opciones**:

# Problema 1: Simulación de consume de combustibe

# Problema 2: Monitoreo de temperatura de motores

# Problema 3: Simulación de consumo de combustible en un cohete por etapas.

# Opción 4: Salir del programa

while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Problema 1: Simulación de consume de combustibe")
    print("2. Problema 2: Monitoreo de temperatura de motores")
    print("3. Problema 3: Simulación de consumo de combustible en un cohete por etapas.")
    print("4. Salir")
    opcion = input("Elige una opción (1-4): ")

    match opcion:
        case "1":
            print("Has elegido el Problema 1.")
        case "2":
            print("Has elegido el Problema 2.")
        case "3":
            print("Has elegido el Problema 3.")
        case "4":
            print("Adios")
            break
        case _:
            print("Opción inválida. Por favor, elige una opción del 1 al 4.")     
      
