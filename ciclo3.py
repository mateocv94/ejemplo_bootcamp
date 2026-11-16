"""
x=1
suma_notas=0
while x < 4:
    #4
    nota = float(input(f"Ingrese la nota número {x} "))
    
    #9                5 +4
    suma_notas = suma_notas + nota 
    
    x=x+1
    print(suma_notas)

print(x)  
#3                  12/4
promedio = suma_notas / x
    

print(f"Promedio {promedio:.1f}")
"""

#Elabore un algoritmo que calcule e imprima la suma de los números pares del 2 hasta el 160.
#2 + 4 = 6 + 6 = 12+8+20
"""
contador = 2 
suma_numeros = 0

while contador <= 160:
    #12                6               6
    suma_numeros = suma_numeros + contador 
    #6             4
    contador = contador + 2

print(f"La suma de los numeros pares del 2 hasta el 160 es{suma_numeros}")
"""

#Elabore un algoritmo que lea un valor N y que imprima un triángulo de asteriscos. Si el valor leído es 5 imprimir:
# *
# **
# ***
# ****
# *****


#Pedirle al usuario que ingrese 10 numeros y los sume. Se debe mostrar la suma
"""
x=1
suma_numero= 0
#15 
cantidad_numeros = int(input("Digite la cantidad de números a sumar "))
#
while x <= cantidad_numeros:
    numero= int(input("Ingrese un numero "))
    
    suma_numero = suma_numero + numero
    x=x+1
    
print("La suma de los números es: ",suma_numero)
"""

#Pedirle al usuario que ingrese varios numeros y los une. El programa termina si el usuario digita 0.
#Se debe mostrar la suma

"""
#    ==0
numero = 8
suma_numero = 0
#        0
while numero != 0:
#   0 
    numero=int(input("Ingrese un número "))
#   26                26           0
    suma_numero - suma_numero + numero 
    
    
print("la suma de los numeros: ",suma_numero)
"""

suma_numero = 0
while True:
    numero = int(input("Ingrese un numero"))
    if numero==suma_numero:
        break
    print("La suma de los numeros: ",suma_numero)
"""
cont=0
while True:
    #5    4  +1
    cont-cont+1
    #     5
    if cont==5:
     break
    print("hola")

#Hacer un algoritmo    
"""

#Pide 10 números. Si alguno es negativo, se rompe el ciclo y muestra un mensaje.
#1 2 3 4 5 6 1 2 3 3 4 5
#3 4 2 1 5 -5
 
contador1 = 1

while True:
    numero = int(input("Digite un número:"))
    contador = contador1 + 1
    if contador > 10:
        print("Haz completado los 10 intentos")
        break
    elif numero < 0:
        print("No puedes digitar numeros negativos")
        break



#Solicita 10 números. Si alguno es mayor a 100, termina el ciclo con un mensaje.

contador2 = 0

while contador2 <=10:
    numero= int(input("Ingrese un numero"))
    contador2 += 1
    if numero > 100:
        print("Rompiste el ciclo")
        break



#Pide al usuario ingresar 10 números. Si la suma acumulada llega a 50, termina el ciclo.

contador3 = 0
suma = 0

while contador3 < 10 and suma < 50:
    numero = int(input("Ingrese un número: "))
    suma = suma + numero
    contador3 += 1

print("La suma acumulada es:", suma)