# Day_9_of_30_With_Python 😁:

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