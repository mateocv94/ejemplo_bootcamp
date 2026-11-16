#En un juego de preguntas a las que se responde Si o No gana quien responda correctamente las tres preguntas.
#Si se responde mal a cualquiera de ellas ya no se pregunta la siguiente y termina el juego. Las preguntas son:
#  ¿Colon descubrió América?
#  ¿La independencia de México fue en el año 1810?
#  ¿The Doors fue un grupo de rock Americano?
#pregunta_3 = "The Doors fue un grupo de rock Americano"
"""
print("Colon descubrìo América")
# si
pre_1 = input("Responda la pregunta (si o no): ").lower()
print(pre_1)

#    si  == si
if pre_1 == "si":
    print("La independencia de México fue en el año 1810")
    # si
    res_2 = input("Responda la pregunda (si o no)")
    #   si  == si
    if res_2 == "si":
        print("The door fue un grupo de rock Americon")
        res_3 = input("Responda la pregunta (si o no)")
        if res_3 == "si":
            print("Ganas el Juego de Preguntas")
        else:
            print("Perdiste el Juego de Preguntas")
    else:
        print("Perdiste el Juego de Preguntas")
else:
    print("Perdiste el Juego de Preguntas")
"""

#Escribe un programa que pida la edad (entero). Si la persona es menor de 18 años, debe mostrar Eres menor de edad y no pedir nada más. Si tiene 18 años o más, debe pedir el dinero que tiene (entero) para pagar una compra de 20000 pesos: si tiene 20000 o más, debe mostrar Compra realizada; si tiene menos, debe mostrar Dinero insuficiente.
"""
#17
edad = int(input("Ingrese la edad: "))
print(edad)
#    17 < 18
if edad < 18: 
    print("Es menor de edad")
else:
    dinero = int(input("Ingrese la cantidad de dinero que tiene: $"))
    if dinero >= 20000:
        print("compra realizada")
    else:
        print("Saldo Insuficiente")
"""      
    
#Enunciado. Escribe un programa que decida si se aprueba un crédito. Primero pide la edad (entero). Si es menor de 18, debe mostrar No cumples la edad mínima. Si tiene 18 años o más, debe preguntar si tiene empleo (si o no). Si no tiene empleo, debe mostrar Necesitas un empleo para solicitar el crédito. Si tiene empleo, debe pedir los ingresos mensuales en pesos (entero): con 2000000 o más debe mostrar Crédito aprobado; con menos, debe mostrar Ingresos insuficientes.
"""
edad = int(input("Ingrese la edas: "))
print(edad)

if edad < 18:
    print("No cumples la edad minima ")
else:
    empleo = input("Tienes empleo: (si o no) ")
    if empleo == "no":
        print("Necesitas un empleo para un credito")
    else:
        ingreso = int(input("Ingresos mensuales en pesos: $"))
        if ingreso >=2000000:
            print("Credito Aprobado")
        else:
            print("Ingreso Insuficientes")
"""

#Obtener el total que tendrá que pagar un alumno si la colegiatura para alumnos de profesional es de $300
#por cada cinco unidades y para alumnos de preparatoria es de $180 por cada cinco unidades, de acuerdo a los siguientes criterios:
#  Si el promedio es de 9.5 o más y el alumno es de preparatoria, entonces este podrá cursar 55 unidades y se le hará un 25% de descuento.
#  Si el promedio es mayor o igual a 9 pero menor que 9.5 y el alumno es de preparatoria, entonces este podrá cursar 50 unidades y se le hará un 10% de descuento.
#  Si el promedio es mayor que 7 y menor que 9 y el alumno es de preparatoria, este podrá cursar 50 unidades y no tendrá ningún descuento.
#  Si el promedio es de 7 o menor, el número de materias reprobadas es de 0 a 3 y el alumno es depreparatoria, entonces podrá cursar 45 unidades y no tendrá descuento.
#  Si el promedio es de 7 o menor, el número de materias reprobadas es de 4 o más y el alumno es de preparatoria, entonces podrá cursar 40 unidades y no tendrá ningún descuento.
#  Si el promedio es mayor o igual a 9.5 y el alumno es de profesional, entonces podrá cursar 55 unidades y se le hará un 20% de descuento.
#  Si el promedio es menor de 9.5 y el alumno es de profesional, entonces podrá cursar 55 unidades y no tendrá descuento.  
#9.5

promedio = float(input("Ingrese su promedio"))
#preparatoria
alumno = input("Ingrese el nivel (preparatoria o profesional):").lower()
print(alumno)
#    preparatria                9.5
if alumno == "preparatoria" and promedio >= 9.5: 
    unidades = 55
    #1980               11  * 180    
    sub_total = unidades / 5 * 180
    #              1980 - 0.25 
    pago_total = sub_total - (sub_total * 0.25)
elif alumno == "preparatoria" and promedio >= 9:
    unidades = 50
    sub_total = unidades / 5 * 180
    pago_total = sub_total - (sub_total * 0.10)
    
elif alumno == "preparatoria" and promedio > 7:
    unidades = 50
    sub_total = unidades / 5 * 180
    pago_total = sub_total
    
        
    
    
        
    
    

