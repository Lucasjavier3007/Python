# Day_5_of_30_With_Python 馃榿: Flow Control / Control de Flujo
"""
conditionals: if, elif, else / Condicionales   

If a program were nothing more than a list of commands to be executed sequentially, one by one,
it wouldn't be very useful. Conditionals allow us to check conditions and make our program behave in
one way or another, to execute one piece of code or another, depending on this condition. 
 
 Si un programa no fuera m谩s que una lista de 贸rdenes a ejecutar de forma secuencial, una por una,no tendr铆a mucha utilidad.
 Los condicionales nos permiten comprobar condiciones y hacer que nuestro programa
 se comporte de una forma u otra, que ejecute un fragmento de c贸digo u otro, dependiendo de esta condici贸n.
"""
# This is where the Boolean type and the logical and relational operators come into importance.
# Aqu铆 es donde cobran importancia el tipo booleano y los operadores l贸gicos y relacionales

'''
if
The simplest form of a conditional statement is an if followed by the condition to be evaluated, 
a colon (:) and on the next line, indented, the code to be executed if said condition is met.

La forma m谩s simple de un estamento condicional es un if (del ingl茅s si) seguido de la condici贸n a evaluar,
dos puntos (:) y en la siguiente l铆nea e indentado, el c贸digo a ejecutar en caso de que se cumpla dicha condici贸n.
'''
day = "Lunes"
if day == "Lunes" :
    print ("Comienza la semana con Tutti") #Si colocamos 2 ordenes de print, python sabe que nuestra intencion es que los dos print se ejecuten
    print("G贸") #solo en caso de que se cumpla la condicion.

# if else
'''
Lo utilizamos cuando queramos que se ejecutara otra orden en caso de que la primer condicion no se cumpla
'''

day = "Monday"
if day == "Friday":
    print("Llego el lunes!!")
    print("Vamos de nuevo!")
else:
    print("Ohhh raaaaiiiiooooossss! Aun no termino la semana")

# if ...elif..elif...else

numero = 6               # ELIF es una contraccion de else IF, Primero evalua la condicion de IF, si es cierta se ejecuta 
if numero < 0:           # el codigo y se continua ejecutando el codigo posterior al condicional; si no se cumple, se evalua
    print("Negativo")    # y hay mas de un ELIF se continua con el siguiente en orden de aparicion.
elif numero >0:          # Si no se cumple la condicion del IF ni de ninguno de los ELIF, se ejecuta el codigo de ELSE
    print("Positivo")
else:
    print("Zero")



    
