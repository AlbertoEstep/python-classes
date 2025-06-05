"""

Crea un sistema que tenga:

- Una clase abstracta Producto con un método descripcion() y __str__().

- Clases derivadas Libro y Electronico que sobrecargan estos métodos.

- Una interfaz Descontable con un método aplicar_descuento(porcentaje).

- Sobrecarga del operador + para sumar precios de productos.

"""

from abc import ABC, abstractmethod

# Interfaz Descontable
class Descontable(ABC):
    @abstractmethod
    def aplicar_descuento(self, porcentaje):
        pass

# Clase abstracta Producto
class Producto(ABC, Descontable):
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    @abstractmethod
    def descripcion(self):
        pass

    def __str__(self):
        return f"{self.nombre} - {self.descripcion()} - Precio: ${self.precio:.2f}"

    def __add__(self, other):
        if isinstance(other, Producto):
            return self.precio + other.precio
        return NotImplemented

# Clase Libro
class Libro(Producto):
    def __init__(self, nombre, autor, precio):
        super().__init__(nombre, precio)
        self.autor = autor

    def descripcion(self):
        return f"Libro de {self.autor}"

    def aplicar_descuento(self, porcentaje):
        self.precio -= self.precio * (porcentaje / 100)

# Clase Electronico
class Electronico(Producto):
    def __init__(self, nombre, marca, precio):
        super().__init__(nombre, precio)
        self.marca = marca

    def descripcion(self):
        return f"Electrónico marca {self.marca}"

    def aplicar_descuento(self, porcentaje):
        self.precio -= self.precio * (porcentaje / 100)

# Lista para almacenar productos
productos = []

# Funciones del menú
def agregar_producto():
    tipo = input("¿Qué desea agregar? (1) Libro (2) Electrónico: ")
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio: "))
    if tipo == "1":
        autor = input("Autor: ")
        producto = Libro(nombre, autor, precio)
    elif tipo == "2":
        marca = input("Marca: ")
        producto = Electronico(nombre, marca, precio)
    else:
        print("Opción no válida.")
        return
    productos.append(producto)
    print("Producto agregado.")

def ver_productos():
    if not productos:
        print("No hay productos.")
        return
    for i, p in enumerate(productos, 1):
        print(f"{i}. {p}")

def aplicar_descuento_a_todos():
    try:
        porcentaje = float(input("Porcentaje de descuento: "))
    except ValueError:
        print("Porcentaje no válido.")
        return
    for p in productos:
        p.aplicar_descuento(porcentaje)
    print("Descuento aplicado.")

def calcular_precio_total():
    if not productos:
        print("No hay productos.")
        return
    total = productos[0]
    for p in productos[1:]:
        total += p
    print(f"Precio total de todos los productos: ${total:.2f}")

# Menú principal
def menu():
    while True:
        print("\nMenú:")
        print("1. Agregar producto")
        print("2. Ver todos los productos")
        print("3. Aplicar descuento a todos")
        print("4. Calcular precio total")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            ver_productos()
        elif opcion == "3":
            aplicar_descuento_a_todos()
        elif opcion == "4":
            calcular_precio_total()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()
