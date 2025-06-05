"""
Crea una clase Vector3D que represente un vector en 3D (x,y,z) y sobrecarga los operadores +, - y ==.

"""
class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __eq__(self, other):
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

# Prueba
v1 = Vector3D(1, 2, 3)
v2 = Vector3D(4, 5, 6)
v3 = v1 + v2
v4 = v2 - v1
v5 = Vector3D(1, 2, 3)

print("v1 + v2 =", v3)
print("v2 - v1 =", v4)
print("v1 == v5:", v1 == v5)
