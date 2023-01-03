# Day_4_of_30_With_Python 😁: Collections, List, Tuples and Dictionaries

#List: Are a type of ordered collection. 
"""
List can contain any type of data: numbers, strings, boolean, and also lists.
"""
#syntax
lst = ["aqui va el contenido de la lista"]
l = [22, True, "a list", [3, 4.3, False, "otra lista"]]
# We use len() to find the length of a list / Podemos usar len() para encontrar la longitud de una lista.

''' We can access each of the elements of the list by writing the name of the list and indicating the index of the element between squaer bracket. NOTE however taht the index of the first item in the list is 0, not 1.
Podemos acceder a cada uno de los elementos de la lista escribiendo el nombre de la lista e indicando el índice del elemento entre corchetes. TENGA EN CUENTA, sin embargo, que el índice del primer elemento de la lista es 0, no 1.
'''
print("La primer posicion de la lista es:", l[0])

# We can also modify an element of the list, if we place it in the left part of the assignment /
# Podemos tambien modificar un elemento de la lista, si lo colocamos en la parte izquierda de la asignacion

l[0] = [5, True]
print("Ahora el nuevo valor de la primer posicion de la lista es:",l[0])

"""
We can use a negative number as an index, the index starts its count from the end of the list.
Thus, to access the last element we would use [-1]
Podemos utilizar un numero negativo como indice, el indice comienza su conteo desde el final de la lista.
De este modo, para acceder al ultimo elemento usariamos [-1]    
"""

l = [3, 5.3, "four", True, 9, [7, 1, False], 90, "D", 2, "hola"]
print("El anteultimo elemento de nuestra lista es:",l[-2])

#Slicing o Partitioned
'''
Allows you to select portions of the list. If instead of a number we write two start and end numbers separated by colons
(start:end), Python will interpret that we want a list that goes from the position "start" to the position "end",
not including the latter. If we write three numbers (start:end:break) instead of two, the third is used to determine
every few positions add an element to the list. 
/
Permite seleccionar porciones de la lista. Si en lugar de un numero escribimos dos numeros inicio y fin separados por dos puntos
(inicio:fin), Python interpretara que queremos una lista que vaya desde la posicion "inicio" a la posicion "fin",
sin inlcuir este ultimo. Si escribimos tres numeros (inicio:fin:salto) en lugar de dos, el tercero se utiliza para deteerminar
cada cuantas posiciones añadir un elemento a la lista.
'''

print("El listado parcial es:",l[0:6])
print("El nuevo listado es:",l[0:8:2])

#We can also use negative numbers in a slicing/ Los numeros negativos tambien podemos usarlos en un slicing

#Tuplas: It differs from the lists in its way of defining it, in these, parentheses are used instead of brackets
# Se diferencia de las listas su forma de definirla, en estas se utilizan parentesis en lugar de corchetes

#Syntax

t = (1,3,False, "Python") 
print(t)
# for tuples with a single element we must place "," to differentiate it from an element between parentheses
# Para tuplas de un solo elemento debemos colocar "," para diferenciarlo de un elemento entre parentesis 

T=(2,)
print(t) 

#Para referirnos a un elemento de una tupla, utilizamos corchetes, al igual que en las listas []

mi_var = ("Hola MUndo")
print(mi_var[1])
print(mi_var[4:])

#Dictionaries
"""
Also called arrays, they are collections that relate a key and a value.
Tambien llamados matrices, son colecciones que relacionan una clave y un valor.    
"""
#Syntax
D = {"Key 1":"Value 1", "Key 2":"Value 2"}
print(D["Key 1"]) #print value 1.-

d = {"The Rolling Stones": "Mik Jagger", "The Beatles": "John Lennon"}
print(d["The Rolling Stones"]) # print Mik Jagger
print(d["The Beatles"]) #print John Lennon

'''
Dictionaries are mappings (associations, mapped), so we cannot use Slicing (since they are not sequenced data)
Los Diccionarios son mappings (asociaciones, mapeados), por lo cual no podemos utilizar Slicing (ya que no son datos en secuencia)
'''

