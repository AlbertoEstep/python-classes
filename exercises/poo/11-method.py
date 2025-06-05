"""
Crea una clase Persona que permita crear objetos de dos formas distintas:

Solo con nombre.

Con nombre y edad.

Si no se pasa edad, debe establecerse a None.

Crea el método __str__ que muestre todos los atributos y úsalo para mostrar el resultado de las dos personas
"""


class Persona:
    def __init__(self, nombre, edad=None):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"

# Prueba
persona1 = Persona("Ana")
persona2 = Persona("Carlos", 30)

print(persona1)
print(persona2)
