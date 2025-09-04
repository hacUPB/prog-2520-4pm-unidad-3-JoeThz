""""
print("numeros pares del 20 al 80:")
numero = 20
while numero <= 80:
    print(numero)
    numero += 2 #numero = numero + 1

#Imprimir los números pares del 20 al 80

#Imprimir los número impares entre 99 y 61
print("numeros impares del 99 al 61:")
numero = 99
while numero >= 61:
    print(numero)
    numero -= 2


#Solicitar dos números al usuario e imprimir los números impares entre ellos
print("numeros impares entre los ingresados por el usuario")
numero1 = int(input("por favor, ingrese un número: "))
numero2 = int(input("por favor, ingrese un número mayor que el anterior: "))

if numero2 < numero1:
     print("dijite un número de la forma en que se solicita.")

while numero1 <= numero2:
     if numero1 % 2 == 0:
         numero1 += 1

     print(numero1)
     numero1 += 2


#Imprimir multiplos de 7 entre 0 y 100
print("multiplos de los numeros entre 0 hasta el 100")
numero = 0
while numero <= 100:
     if numero % 7 == 0:
         print(numero)
     numero += 1
"""

#Solicitar un número al usuario e imprimir su tabla de multiplicar hasta 15
print("Solicitar un número al usuario e imprimir su tabla de multiplicar hasta 15")
numero = int(input("Por favor ingrese un número: "))
multiplicar = 1
while multiplicar <= 15:
     resultado = numero * multiplicar
     multiplicar += 1
     print(resultado)

