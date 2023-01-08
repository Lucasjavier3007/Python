# Day_9_of_30_With_Python 😁: Orientacion a Objetos

''' Orientacion a Objetos'''
#Para entender este paradigma primeros tenemos que comprender que es una Clase y que es un Objeto.

"""Un OBJETO es una entidad que agrupa un estado y una funcionalidad relacionadas, el estado del objeto se define
a traves de variables llamadas atributos, mientras que la funcionalidad se modela a traves de funciones
a la que se le conoce con el nombre de Metodos del objeto. 
Un ejemplo de objeto podria ser un auto, en el que tendriamos atributos como:
Marca
Numero de puertas
tipo de carburante
Metodo de arranque 
o bien cualquier otra combinacion de atributos y metodos segun lo que fuera relevante para nuestro programa"""


'''Una CLASE es una plantilla generica a partir de la cual instanciar los objetos; plantilla que es la que 
define  QUE atributos y metodos tendrian los objetos de esa clase'''

#sintaxis: 

class auto:
    """Abstraccion de los objetos auto."""
    def __init__(self, gasolina):  #__init__ este metodo se ejecuta justo despues de crear un objeto, a partir de la clase
        self.gasolina = gasolina   #este proceso se conoce como inicializacion
        print("Tenemos", "gasolina", "litros")
        
    def arrancar(self):
        if self.gasolina > 0:
            print("Arranca")
        else:
            print("No Arranca")
    def conducir(self):
        if self.gasolina >0:
            self.gasolina -= 1
            print("Quedan", self.gasolina, "litros")
        else:
            print ("No se mueve")
            
            
# HERENCIA
'''Hay tres conceptos que son basicos para cualquier lenguaje de programacion orientado a objetos: El Encapsulamiento, La Herencia y el Polimorfismo'''

"""
En un lenguaje orientado a objetos cuando hacemos que una clase (subclase) herede otra clase (Superclase) estamos haciendo que la 
subclase contenga todos los atributos y metodos que tenia la superclase.
No obstante al acto de heredar de una clase tambien se le llaman a menudo "Extender una clase" 
"""

'''Supongamos que queremos modelar los instrumentos musicales de una banda, tendremos entonces una clase "Guitarra", una clase "BAteria" 
una clase "BAjo", etc. Cada una de estas clases tendrauna serie de atributos y metodos, pero ocurre que, por el mero hecho de ser instrumentos
musicales, estas clases compartiran muchos de sus atributos y metodos; un ejemplo seria el metodo TOCAR
'''

# Para indicar que una 