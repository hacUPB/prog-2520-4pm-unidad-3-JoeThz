"""
def suma(a, b):
	resultado = a + b
	return resultado


#Llamando a la función
numero1 = 5
numero2 = 3
resultado_suma = suma(numero1, numero2)
print(f"{numero1} + {numero2} = {resultado_suma}")
print(suma(9898,564))
suma(45, 78)

"""
"""
#Función de multiplicación:

def mul(a, b):
    prod = a * b
    return prod

num1 = int(input("Ingrese un número que desee multiplicar: "))
num2 = int(input("Ingrese otro número por el cual desea multiplicar el anterior: "))
producto = mul(num1, num2)
print(f"{num1} x {num2} = {producto}")
"""
"""
#Función que imprime la tabla de cualquier número | bucle "for".

def tabla(num):
    for i in range(1,11):
        producto = i * num
        print(f"{num} x {i} = {producto}")
    #Esta función no tiene ningún retorno.

numero = int(input("Ingrese un valor: "))
tabla(numero)
"""
"""
Función: menú
Parámetros de entrada: Ninguno
Ejecución: Imprimir en pantalla de 4 opciones diferentes. Solicitar que se elija una opción y la guarda en una variable.
Valor de retorno: Opción elegida
"""
def menu():
    print(" 1. Encabezado.\n 2. Porcentaje.\n3 \n 4. Zapatos.")
    selec = int(input("Seleccione una opción: "))
    return selec

def encabezado(mensaje):
    print("Nombre: Joe Frazer Tamayo Hernandez")
    print("Estado civil: Vagabundo")
    print("Estado mental: Deplorable")
    print("Apodo: Erdaaaaaaa, que pelaito tan fastidioso vale")
    print("Edad: Nadie sabe pero ponele 35")
    print("")


eleccion = menu()
print(f"Opción elejida: {eleccion}")

match(eleccion):
    case 1:
        print("Nombre: Joe")
        print("Edad: 35")
        print("Intitución educativa: UPB")
        int(input("Quien eres: "))
    case 2:
        total = int(input("Ingrese un valor"))
        porcentaje = total