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
        print(val)}