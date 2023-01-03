# Day 3 of 30 with Python 😁: Operators
'''
Los operadores son simbolos especiales que representan calculos, como la suma o la multiplicacion.
Los valores a los cuales se aplican esos operadores reciben el nombre de operandos
'''
suma = (2+3)
resta = (5-2)
division = (100/10)
multiplicacion = (5*2)
modulo = (100%10)
exponenciacion = (2**3)
divisionEntera = (40//2)

"""
Jerarquia:
cuando se presentan muchas operaciones aritmeticas, la jerarquia determina
el orden con el que deben realizarse esas operaciones
"""

'''
Orden de operacion:
Parentesis- Exponenciacion- Multiplicacion, division- suma y resta

'''

#Boolean
"""    
A boolean data type represents one of the two values: True or False. 
The use of these data types will be clear once we start using the comparison operator. The first letter T for True and F for False should be capital unlike JavaScript. Example: Boolean Valu
"""
print(True)
print(False)

# Operators: Assignment Operators
#Los utilizamos para asignarles valores a las variables
'''
And: Nos devuelve True if both statements are true(si ambas son verdaderas). Ej: x<5 and x <10
or: returns True if one of the statements is True. Ej: x<5 or x<4
not: reverse the result, returns false if the result is True. Ej: not (x<5 and x<10)
'''

print(3>2 and 4>3) #True, because both statements are true
print(3>2 and 4<3) # False, because the second statement is false
print('True and True:', True and True)
print(3>2 and 4>3) #True
print(3>2 and 4==3) #False

# exercise Day 3

# 1) Declare your age as integer variable / Declarar tu edad como una variable entera
age = int(input("Ingrese su edad:"))
print("Tienes:",age,"años")
# 2) Declare your height as a float variable / Declarar tu Altura como una variable float
height = float(input("Ingresa tu altura, en cm:"))
print("Tu altura es:",height)
"""
if height <150
print("Eres bajito")
else height >160 and <170
print("Tienes estatura normal")
if else height >170{
print("Eres alto")
]
"""
# 3) Declare a variable that store a complex number / Declarar una variable que almacene un numero complejo
real = int(input("Ingresa un numero del 1 al 9:"))
img = int(input("Ingresa otro numero del 1 al 9:"))                 
letter = str(input("Elige: i, j o k :")) 
#print ("Felicitaciones, creaste el numero complejo:",real,"+",img,letter)
print ("Felicitaciones, creaste un numero complejo:","(",real,"+",img,letter,")")
# 4) Write a script that prompts the user to enter base and height of the triangle / escriba un script que solicite al ususario q ingrese base y altura del triangulo
# and calculate an area of this triangle (area = 0.5 x b x h) / Calcular el area de este triangulo
b = int(input("Ingresa la base del Triangulo :"))
print(b)
h = int(input("Ingresa la altura del Triangulo :"))
print(h)
area = (0.5*b*h)
print("El area del Triangulo formado es:",area)

# 5) Write a script that prompts the user to enter side a, side b, and side c of the triangle. 
# Calculate the perimeter of the triangle (perimeter = a + b + c).
A = int(input("Ingrese el lado a:"))
print(A)
B = int(input("Ingrese el lado b:"))
print(B)
C = int(input("Ingrese el aldo c:"))
print(C)
perimeter= (A+B+C)
print("El perimetro del triangulo ingresado es:",perimeter)

# 6) Get length and width of a rectangle using prompt. / Obtener la longitud y el ancho de un rectangulo usando el indicador.
# Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = int(input("Ingresa longitud:"))
width = int(input("Ingresa ancho :"))
area = length * width
print(length)
print(width)
print("El area del rectangulo es:",area)

Perimeter = 2 * (length+width)
print("El perimetro del rectangulo es:",Perimeter)

# Comparison Operators
"""
Operator       Name               Example
==           Equal               x == y
!=         Not equal             x != y
>        Greater than            x > y
<        Less than               x < y
>=    Greater than or equal to   x >= y
<=    Less than or equal to      x <= y

"""


# In addition to the above comparison operator Python uses:
"""
is: Returns TRUE if both variables are the same object(x is y) / Devuelve True si AMBAS variables son el mismo Objeto.
is not: Returns true if both variables are not the same object(x is not y) / Devuelve True sin ambas variables no son el mismo objeto.
in: Returns True if the queried list contains a certain item(x in y)/ Devuelve True sio la lista consultada contiene un determinado elemento (x en y).
not in: Returns True if the queried list doesn't have a certain item(x in y) / Devuelve True si la lista consultada no contiene un determinado elemento ( x en y).

"""
print('1 is 1', 1 is 1)                   # True - because the data values are the same
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - A found in the string
print('B in Asabeneh', 'B' in 'Asabeneh') # False - there is no uppercase B
print('coding' in 'coding for all') # True - because coding for all has the word coding
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

# Logical Operators
"""
Python uses keywords AND, OR and NOT for logical operators. Logical operators are used to combine conditional statements:

Operator      Description                                       Example
and   Returns True if both statements are true                  x<5 and x<10
or    Returns True if one of the statements is true             x<5 or x<4
not  Reverse the result, returns False if the result is True    not(x<5 and x<10)        
"""
#Examples:
print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statements is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print('True or False:', True or False)
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False

# Exercises:
# a) Get radius of a circle using prompt. Calculate the area 
# (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
r = int(input("Ingresa un radio"))
print(r)
pi = 3.14
area = pi * r**2
print("El area del circulo es:",area)

#Circumference
c = 2* pi * r
print("La circunsferencia creada es de:",c)


# b)  Calculate the slope, x-intercept and y-intercept of y = 2x -2 
#  Calcular la pendiente x, la interseccion y 

'''
Ejercicios:
1) Escribir un programa que realice la siguiente operacion aritmetica:
((3+2)/(2*5))**2
'''
a= 3+2
b=2*5
c= a/b
d= c**2
ejercicio = (a/b)**2

'''
Ejercicio 2)
Una jugueteria tiene mucho exito en dos de sus productos:
payasos y muñecas. Suele hacer venta por correo y la empresa de logistica
les cobra por peso de cada paquete, asi que deben calcular el peso de los 
payasos y muñecas que saldrian en cada paquete a demanda. Cada payaso pesa 112g y cada muñeca
75g. Un cliente frecuente pide la cantidad de 23 payasos y 54 muñecas, realiza un programa
que muestre el peso total de toda la venta'''

payasos = 112
muñecas = 75
pesoTotalVenta = ((23*payasos)+(54*muñecas))
print(pesoTotalVenta)


"""
pow = es una variable que podemos utilizar para la exponenciacion
sintaxis:
calculo= pow(5,2) en esta oportunidad vamos a elevar al cuadrado el n 5    
    
"""
