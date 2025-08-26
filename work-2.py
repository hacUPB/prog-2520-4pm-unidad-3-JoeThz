#Determinar si un número es par o impar
#Leer número
numero = int(input("Ingrese un número entero: "))
residuo = numero % 2
#Si residuo es 0, el número es par
if residuo == 0:
    print("El número es par")
else:
    print("El número es impar")