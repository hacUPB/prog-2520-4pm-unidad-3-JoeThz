##Algoritmo que determine si un numero es primo
print("---- ¿TU NÚMERO ES PRIMO? ----")
num = int(input("Ingrese un número entero mayor que 1: "))
div = num // 2 #division entera
cont = 0
for i in range(2, div + 1):
    if num % i == 0:
        cont += 1
        print(f"{num} no es primo.")
        break
        
if cont == 0:
    print(f"El {num} es primo.")
else:
    print(f"Los divisores de {num} son: ")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)
