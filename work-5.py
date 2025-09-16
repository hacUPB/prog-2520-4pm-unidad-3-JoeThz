#Cambiar el codigo de este ejercicio 4 por el modo de match case.

print("Ingrese la zona a la que va dirigido el paquete, elija el número correspondiente a la zona")
zona = int(input("1. Norteamérica\n2. Centroamérica\n3. Sudamérica\n4. Europa\n5. Asia \nIngrese el número de la zona: "))

if zona > 0 and zona < 6:
    peso = float(input("Ingrese el peso del paquete en gramos: "))
    if peso <= 5000:
        match zona:
            case 1:
                costo = 11
            case 2:
                costo = 10
            case 3:
                costo = 12
            case 4:
                costo = 24
            case 5:
                costo = 27
        total = peso * costo
        print(f"El costo total del envío es: ${total}.")
    else:
        print("El paquete no puede ser enviado por exceder el peso máximo permitido de 5 kg")