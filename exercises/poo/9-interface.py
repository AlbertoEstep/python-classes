"""
Crea una "interfaz" llamada Imprimible con un método imprimir(). 
Luego crea una clase Documento y otra Imagen que implementen esta interfaz.
Debe funcionar la siguinte prueba:

"""

# Prueba
items = [Documento(), Imagen()]
for item in items:
    item.imprimir()
