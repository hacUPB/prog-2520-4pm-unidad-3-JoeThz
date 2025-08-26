#Una compañía de paquetería internacional tiene servicio en algunos países según su zona. 
#El costo por el servicio de paquetería se basa en el peso del paquete y la zona a la que va dirigido. 
#Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados por seguridad. 
#Usa la siguiente tabla para resolver el problema:

#Zona 1: América del Norte con un costo de $11.00
#Zona 2: América Central con un costo de $10.00
#Zona 3: América del Sur con un costo de $12.00
#Zona 4: Europa con un costo de $24.00
#Zona 5: Asia con un costo de $27.00

print("Ingrese la zona a la que va dirigido el paquete, elija el número correspondiente a la zona")
zona = int(input("1. Norteamérica\n2. Centroamérica\n3. Sudamérica\n4. Europa\n5. Asia \n ingrese el número de la zona: "))

if zona > 0 and zona < 6:
    peso = float(input("Ingrese el peso del paquete en gramos: "))
    if peso <= 5000:
         if zona == 1:
          total = peso * 11
         elif zona == 2:
          total = peso * 10
         elif zona == 3:
          total = peso * 12
         elif zona == 4:
          total = peso * 24
         elif zona == 5:
          total = peso * 27
    else:
     print("El paquete no puede ser enviado por exceder el peso máximo permitido de 5 kg")
else:
        print("Zona no válida")
        total = 0
print("El envio de su paquete cuesta: ${total}.")

print(f"El costo total del envío es: ${total}.")
