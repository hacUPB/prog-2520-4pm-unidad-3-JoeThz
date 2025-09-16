"""""
#rango
print("Rango de 5 a 20 con paso de 2:")
for i in range(5, 20, 2):
    print(i)
print("")

print("Rango de 20 a 5 con paso de -1:")
for i in range(0, -21, -1):
    print(i)
print("")

print("pruebas: ")
for i in range(0, -201, 0):
    print(i)
print("")

"""
#Calcular la suma de todos los numeros pares desde 1 hasta el numero ingresado por el usuario.
numero = int(input("ingrese un número entero positivo: "))
suma = 0
for i in range(2, numero + 1, 2):
     print("los numeros pares entre 0 y",numero,"son: ", i,end=',')
     suma += i
print("la suma de los numeros anteriormente dados es:", suma)
