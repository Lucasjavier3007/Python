# Day_6_of_30_With_Python 😁: Bucles
"""
Mientras que los condicionales nos permiten ejecutar distintos fragmentos de codigo dependiendo de ciertas condiciones
los bucles nos permiten ejecutar un mismo fragmento de codigo un cierto numero de veces, mientras se cumpla una determinada condicion.
"""
# While

edad = 0                                           #si olvidaramos escribir la instruccion de aumentar la edad, en este caso nunca se llegaria a la condicion
while edad <150:                                  # de que edad fuese igual o mayor que 18, siempre seria 0, y el bucle continuaria ejecutandose 
    edad= edad +1                                 #indefinidamente escribiendo en la pantalla: Tienes 0 años.
    print ("Felicidades!! tienes",edad,"años")        #Esto es lo que se conoce como bucle infinito

'''
Hay situaciones en las que un bucle infinito es util, por ej: Veamos un programa que repite todo lo que el usuario
diga, hasta que escriba "adios"
'''
# reveer linea 20
"""salir = False
while not salir:
    entrada = raw_input()
    if entrada == "adios":
        salir = True
    else:
        print(entrada)
"""

Listado = 0
while Listado<200:
    Listado = Listado+1
    print("Felicitaciones!!, eres el convocado n°:",Listado)
    

# otra palabra calve que podemos encontrar en un bucle es: "continue", lo que permite pasar directamente a a la siguiente iteracion del bucle

edad = 0
while edad <20:
    edad = edad + 1
    if edad % 2 == 0:
        continue
    print("felicidades, tienes"+str(edad))

#en esta ocacion hemos añadido un if que comprueba si la edad es par, en cuyo caso saltamos a la siguiente iteracion en lugar de imprimir el mensaje.
#quiere decir que con esta modificacion el programa solo imprimiria felicitaciones cuando la edad fuera impar.
