#Desarrolla un juego donde la computadora "piensa" en un número entre 1 y 100 y el usuario debe adivinarlo. El programa debe:
#1. Generar un número aleatorio entre 1 y 100
#2. Pedir al usuario que adivine el número
#3. Indicar si el número ingresado es mayor o menor que el número secreto
#4. Contar los intentos que toma el usuario para adivinar el número
#5. Mostrar el número de intentos cuando el usuario adivine correctamente
"""
import random
num_aleatorio = random.randint(0,100)
print(num_aleatorio)

"""
"""
---- Variable de entrada ----
| Nombre      | Tipo
| num         | int

---- Variable de salida ----
| Nombre      | Tipo
| i           | int

---- Variable de control ----
| Nombre      | Tipo
| num         | int

"""

print("--- ADIVINA UN NUMERO DEL 1 AL 100 ---")
from random import randint
num_aleatorio = randint(1,100)
num = -1 #Obliga a entrar al while la primera vez
i = 0 #Iteraciones
while num != num_aleatorio:
    num = int(input("Escribe un numero entre el 1 y el 100: "))
    i += 1
    if num > num_aleatorio:
        print("Tu número es mayor")
    elif num < num_aleatorio:
        print("Tu número es menor")
    else:
        print("¡Felicidades Shinji!")

print(f"Adivinaste en {i} intentos.")