# Day_8_of_30_With_Python 😁: funciones
"""
Sintaxis:

def my_funcion(param1, param2):   --> def es la palabra clave, seguido del nombre de la funcion y entre parentesis
    print (param1)                    los argumentos separados por comas.
    print (param2) 
"""

#al declarar la funcion lo que hacemos es asociar un nombre al fragmento del codigo que conforma la funcion

def varios(param1, param2, *otros):
    for val in otros:
        print(val)
        
        varios(1, 2)
        varios(1, 2, 3)
        varios(1, 2, 3, 4)

'''Esta sintaxis funciona creando una tupla ( de nombre otros) en la que se almacenan los valores de tdos los parametros
extra pasados como argumento. Para la primera llamada, varios (1, 2), la tupla otros estaria vacia dado que no se han pasado
mas parametros que los definidos por defecto, por lo tanto no se imprimira nada.
En la segunda llamada otros valdria (3, ), y en la tercera (3, 4).'''

#Tambien se puede acceder el nombre del ultimo parametros con **, en cuyo caso en lugar de una tupla utilizariamos un Diccionario.
#Las claves de este diccionario serian los nombres de los parametros indicados al llamar a la funcion y los valores del
#diccionario, los valores asociados a estos parametros.

def varios(val1, val2, **otros):
    for i in otros.items():
        print (i)
        
varios(1, 2, tercero = 3)


def sumar(x, y):
    return(x + y)

print (sumar(3, 2))


def f(x, y):
    return(x * 2, y * 2)

a, b = f(1, 2)