# Day_2 _of _30_with_python 😎: Variables_building_functions

# Variables, Building Functions (Funciones integradas)
#Las funciones integradas esta disponibles para su uso, no hace falta configurarlas
print("Hello World") # its prints the text value: Hello World
len("Hello World!") #it counts the number of characters inscluding space
type("Hello World!") # it the checks the data type
str(10) #it converts number to string
int("10") #it converts to number
float(10) # it converts integer to decimal
input("Enter your name:") # it takes user input
help("keywords") #print all python reserved words
help(str) # give information about string
dir(str) # give information about string
# No usamos las palabras reservadas para declarar variables o funciones.- OjO
"""
    Ahora vamos a practicar un poco
"""
min(30, 31, 43, 66, 77, 88) # Muestra el minimo valor (gives the minimum value)
max(13, 42, 45, 56,77, 87, 98) # Muestra el maximo valor (gives the maximum value)
min([12, 23, 45, 56, 67, 87, 91, 102]) # it takes list as an argument and return min (Toma List como argumento y devuelve el valor min)
max([0, 1,12,34,56,75,86,90,125,304, 665]) # it takes list as an argument and return max(Toma List como argumento y devuelve el valor max)
sum([1,3,5,31,42,55,67,76,78,99,121])# it takes only list as an argument and return the sum

"""
Python Variable Name Rules

A variable name must start with a letter or the underscore character (Comienza con una letra o con un caracter subrayado)
A variable name cannot start with a number (No puede comenzar con un numero)
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and_) (Solo puede contener caracteres alfanumericos y _)
Variables names are case-sensitive (firstname, Firstname, FirstName and FIRSTNAME) are different variables. (Los nombres de las variables son case-sensitive)
"""

#Invalid variables names:
#first-name/ first@name/ first$name/ num-1/ 1num

#Las variables si tienen un nombre largo se declaran_asi
#Ejemplo

first_name = "Javier"
last_name = "Oviedo"
country = "Argentina"
city = "La Rioja"
age = 37
is_married = True
skills = ["HTML", "CSS", "SQL","Python", "Swift", "Xcode"]
person_info = {
    'first_name' : "Javier",
    'last_name' : "Oviedo",
    'country' : "Argentina",
    'city' : 'La Rioja'    
}
# Obtener la entrada de datos del usuario usando la funcion "input()". Getting user input using the input() buit-in function
First_name = input("Whats is your name?:")
Age = input("how old are you?:")
print(First_name)
print(Age)

# Data Types
type("Javier")
type(23)
type(4.67)
type([2, "SUN", 3.34])
type({"Name":"Javier", "age":36, "is_married":23})
type((2, 4, 5))
type(zip([2,4],[5,7]))

#Exercise
"""
A) Declare 5 as num_one and 4 as num_two 
1) Add num_one and num_two and assign the value to a variable total / Sumar y asignar el total en una nueva variable
2) Subtract num_two from num_one and assign the value to a variable diff / restar variable 2 con 1 y asignar nueva variable
3) Multiply num_two and num_one and assign the value to a variable product / Multiplicar y asignar nueva variable
4) Divide num_one by num_two and assign the value to a variable division / Dividir num1 en 2, asignar nuevo valor
5) Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
6) Calculate num_one to the power of num_two and assign the value to a variable exp
7) Find floor division of num_one by num_two and assign the value to a variable floor_division
    
"""
#Respuestas
#A)
num_one = 5
num_two = 4

# 1)
total = (num_one+num_two)
print(total)

# 2)
substraction = (num_two-num_one)
print(substraction)

# 3)
Multiplication= (num_two*num_one)
print(Multiplication)

# 4)
division = (num_one/num_two)
print(division)

# 5)
modulus = (num_two%num_one)
print(modulus)

# 6)
exponential = (num_one**num_two)
print(exponential)

# 7)
floor_division = (num_one//num_two)
print(floor_division)

#Exercise B) The radius of a circle is 30 meters.
"""
1) Calculate the area of a circle and assign the value to a variable name of area_of_circle / calcular el area de un circulo y asignar el nombre de su variable como area_of_circle
2) Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle / calcular la circunsferencia de un circulo y asignar el valor a una variable de nombre: circum_of_circle
3) Take radius as user input and calculate the area / Tomar el radio que el usuario ingreso y calcular el area  
"""
# Respuestas B)
# 1)
r = 30
π = 3.14
area_of_circle = ( π *(r**2))
print(area_of_circle)

# 2)
radio = 30
diametro = (2*radio)
circum_of_circle = (π*diametro)
print(circum_of_circle)

# 3)

radius= input("Cual es el radio de su circulo?:")
Area_Of_Circulo = [π *(radius**2)]
print(Area_Of_Circulo)

#Exercise C
"""
Use the built-in input function to get first name, last name, / Usanr la funcion input para obtener los datos
country and age from a user and store the value to their corresponding variable names /
""" 

#Respuesta C
first_name = input("What is your name?:")
last_name = input ("What is your Last Name?:")
country = input ("Where are you from?:")
age = input ("how old are you?:")
print(first_name)
print(last_name)
print(country)
print(age)

# Exercise D
"""
    Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
"""
#Respuesta
'''
help ("keywords")
'''