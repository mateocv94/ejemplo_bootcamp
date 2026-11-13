"""
x=5
f=10
#> >= < <= == !=

numero = int(input("Digite un numero"))
#        1   == 0
if numero % 2 == 0 :
    print("El numero es par")
else:
    print("Es el numero impar")
    
    
    
#       1 == 1
if numero %2 == 1:
    print("El numero es impar")
else:
    print("El numero es par")
    
    
#   1       != 0 
if numero % 2 !=0:
    print("El numero es impar")
else:
    print("El numero es par")

#      1  !=   1
if numero %2 !=1:
    print("El numero es par")
else:
    print("El numero es impar")
"""    
    
    
#Luis compra 10 productos del mismo precio, si el precio total es mayor a 100 dolares, tendra un descuento del 20% de lo contrario, el descuento será del 10%.
#5
precio_productos = float(input("Productos del mismo precio"))
#50
total_compra = precio_productos * 10
#50
if total_compra > 100:
    descuento = total_compra * 20/100
    print("Total descuento ",descuento)
    print("Total pago ", total_compra - descuento)
    
else:
    #5               50*10/100
    descuento2 = total_compra * 10/100
    #                            5
    print("Total descuento ",descuento2)
    #                        50          5 = 45
    print("Total pago ", total_compra - descuento2)
    
# Forma 2 

if total_compra > 100:
    total_descuento = total_compra * 20/100
    descuento= "20%"
    
else:
    # 5                   50*10/100=5
    total_descuento = total_compra * 10/100
    
    descuento_dos= "10%"
    
    print(f"Total descuento es del ${descuento:,.0f}",total_descuento)
    print("Total pago ", total_compra - total_descuento)
    
    
