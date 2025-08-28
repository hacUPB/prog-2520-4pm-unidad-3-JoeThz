#menú



# Utilizamos una variable tipo booleana -> una bandera

while True: #Bucle infinito, la condición siempre es verdadera.
    print("1.Entradas\n2. Platos\n3. Bebidas\n4. Postres\n5. Salir")
    opcion = int(input("Elija una opción: "))
    match opcion:
        case 1:
            print("1. Patacón con hogao.")
            print("2. Yuca con chicharrón.")
            print("3. Guineo con suero.")
            print()
            opc1 = int(input("Ingrese su elección: "))
            match opc1:
                case 1:
                    print("$50.000")
                case 2:
                    print("$30.000")
                case 3:
                    print("$70.000")
        case 2:
            print("1. Solomito.")
            print("2. Hamburguesa.")
            print("3. Mojarra frita.")
            print()
            opc2 = int(input("Ingrese su elección: "))
            print()
            match opc2:
                case 1:
                    print("$120.000")
                case 2:
                    print("$130.000")
                case 3:
                    print("$170.000")
            print()
        case 3:
            print("1. Cerezada")
            print("2. Michelada")
            print("3. Cerveza")
            print()
            opc3 = int(input("Ingrese su elección: "))
            match opc3:
                case 1:
                    print("$50.000")
                case 2:
                    print("$45.000")
                case 3:
                    print("$65.000")
            print()
        case 4:
            print("1. Tiramisú")
            print("2. Tres leche")
            print("3. Arroz con leche")
            print()
            opc4 = int(input("Ingrese su elección: "))
            match opc4:
                case 1:
                    print("$85.000")
                case 2:
                    print("$75.000")
                case 3:
                    print("$55.000")
            print()
        case 5:
            break
        case _:
            print("Opción no disponible")
            print()
    
