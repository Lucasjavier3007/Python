# Day_7_of_30_With_Python 😁: for in
secuencia = ["uno", "dos", "tres", "cuatro", "cinco"]
for elemento in secuencia:
    print(elemento)

#En python "for" se utiliza como una forma generica de iterar sobre una secuencia

for x in range(0,98):
    print("El numero de x es:",x)
#la funcion "range" permite generar una lista que va desde el primer numero que le indiquemos al segundo.

for i in range(15):
    print("Repeticion n°:",i)
#si colocamos un solo valor en la funcion, crea una lista de esa cantidad de elementos

m = int(input("Ingrese un numero:"))
for nu in range(m):
    print("El numero de repeticion es:",nu)


for x in "Argentina":
    print(x)
#podemos crear un listado con una cadena de caracteres.

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "junio", "Julio"]
for x in meses:
    print(x)

#tambien podemos establecer un formato de como imprimir nuestra lista, la tercer variable es la que nos indica el salto de linea

for x in range (0,50,3):
    print("Esta es la linea: ",x)