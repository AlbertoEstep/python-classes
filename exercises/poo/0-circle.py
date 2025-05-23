"""
Crea una clase Circulo que tenga un atributo: radio y métodos para calcular el área y el perímetro.
"""

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

# Using the class
my_circle = Circle(5)
print("Area:", my_circle.area())
print("Perimeter:", my_circle.perimeter())
