#serie de Fibonacci
# El usuario ingresa el número de términos y se imprimen los términos de la serie de Fibonacci hasta ese número.
n = int(input("Ingrese el número de términos: "))
if n <= 0:
    print("Por favor ingrese un número entero positivo.")
elif n == 1:
    print(0)
else:
    a, b = 0, 1
    print(a)
    print(b)
    i = 1
    # El ciclo debe ir hasta n-2 porque ya se imprimieron los dos primeros términos
    while i <= (n - 2):
        c = a + b
        print(c)
        a = b
        b = c
        i += 1
    print("Serie de Fibonacci completada.")





