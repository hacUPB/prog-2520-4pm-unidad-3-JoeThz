#Leer estatura
estatura = input("Ingrese su estatura en metros: ")
estatura = float(estatura)

#Leer peso
peso = input("Ingrese su peso en kilogramos: ")
peso = float(peso)

#Calcular IMC
imc = peso / (estatura ** 2)

#Mostrar resultado
print("Su IMC es: ", imc)

#Determinar si la persona tiene sobrepeso
if imc > 25:
    print("Tiene sobrepeso")    
else: 
    if imc > 29.9:
        print("Tiene obesidad")   
    else: 
        if imc > 39.9:
         print("Tiene obesidad severa")

#Determinar si la persona tiene bajo peso
if imc < 18.5:
    print("Tiene bajo peso")   
else:
    print("No tiene bajo peso") 

#Determinar si la persona tiene peso normal
if imc >= 18.5 and imc <= 24.9:
    print("Tiene peso normal")

print(f"{nombre}, su IMC es {imc:0.2f}")
