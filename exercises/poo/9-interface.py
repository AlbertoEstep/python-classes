"""
Crea una "interfaz" llamada Imprimible con un método imprimir(). 
Luego crea una clase Documento y otra Imagen que implementen esta interfaz.
Debe funcionar la siguinte prueba:

"""

from abc import ABC, abstractmethod

# Interfaz
class Imprimible(ABC):
    @abstractmethod
    def imprimir(self):
        pass

class Documento(Imprimible):
    def imprimir(self):
        print("Imprimiendo documento...")

class Imagen(Imprimible):
    def imprimir(self):
        print("Imprimiendo imagen...")

# Prueba
items = [Documento(), Imagen()]
for item in items:
    item.imprimir()
