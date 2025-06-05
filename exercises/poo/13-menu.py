"""

Haz un programa que:

- Use clases abstractas, interfaces, sobrecarga de operadores, etc.
- Ofrezca un menú con las siguientes opciones:
    - Agregar producto (Libro o Electrónico)
    - Ver todos los productos
    - Aplicar descuento a todos
    - Calcular precio total
    - Salir
"""

import json
import os
from abc import ABC, abstractmethod

# Interfaz Descontable
class Descontable(ABC):
    @abstractmethod
    def aplicar_descuento(self, porcentaje):
        pass

# Clase abstracta Producto
class Producto(Descontable):
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor:
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = valor

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if valor < 0:
            raise ValueError("El precio no puede ser negativo.")
        self._precio = valor

    @abstractmethod
    def descripcion(self):
        pass

    def __str__(self):
        return f"{self.nombre} - {self.descripcion()} - Precio: ${self.precio:.2f}"

    def __add__(self, other):
        if isinstance(other, Producto):
            return self.precio + other.precio
        return NotImplemented

    @abstractmethod
    def to_dict(self):
        pass

# Clase Libro
class Libro(Producto):
    def __init__(self, nombre, autor, precio):
        super().__init__(nombre, precio)
        self.autor = autor

    def descripcion(self):
        return f"Libro de {self.autor}"

    def aplicar_descuento(self, porcentaje):
        self.precio -= self.precio * (porcentaje / 100)

    def to_dict(self):
        return {"tipo": "Libro", "nombre": self.nombre, "precio": self.precio, "autor": self.autor}

# Clase Electronico
class Electronico(Producto):
    def __init__(self, nombre, marca, precio):
        super().__init__(nombre, precio)
        self.marca = marca

    def descripcion(self):
        return f"Electrónico marca {self.marca}"

    def aplicar_descuento(self, porcentaje):
        self.precio -= self.precio * (porcentaje / 100)

    def to_dict(self):
        return {"tipo": "Electronico", "nombre": self.nombre, "precio": self.precio, "marca": self.marca}

# Función para cargar productos desde un archivo JSON
def cargar_productos(archivo):
    productos = []
    if os.path.exists(archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            datos = json.load(f)
            for item in datos:
                if item["tipo"] == "Libro":
                    productos.append(Libro(item["nombre"], item["autor"], item["precio"]))
                elif item["tipo"] == "Electronico":
                    productos.append(Electronico(item["nombre"], item["marca"], item["precio"]))
    return productos

# Función para guardar productos a JSON
def guardar_productos(productos, archivo):
    datos = [p.to_dict() for p in productos]
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4)

# Clase para manejar la aplicación y el menú
class Aplicacion:
    def __init__(self, archivo="productos.json"):
        self.archivo = archivo
        self.productos = cargar_productos(archivo)

    def agregar_producto(self):
        tipo = input("¿Qué desea agregar? (1) Libro (2) Electrónico: ")
        nombre = input("Nombre del producto: ")
        try:
            precio = float(input("Precio: "))
        except ValueError:
            print("Precio no válido.")
            return

        if tipo == "1":
            autor = input("Autor: ")
            producto = Libro(nombre, autor, precio)
        elif tipo == "2":
            marca = input("Marca: ")
            producto = Electronico(nombre, marca, precio)
        else:
            print("Opción no válida.")
            return

        self.productos.append(producto)
        guardar_productos(self.productos, self.archivo)
        print("Producto agregado y guardado.")

    def ver_productos(self):
        if not self.productos:
            print("No hay productos.")
        for i, p in enumerate(self.productos, 1):
            print(f"{i}. {p}")

    def aplicar_descuento_a_todos(self):
        try:
            porcentaje = float(input("Porcentaje de descuento: "))
        except ValueError:
            print("Porcentaje no válido.")
            return
        for p in self.productos:
            p.aplicar_descuento(porcentaje)
        guardar_productos(self.productos, self.archivo)
        print("Descuento aplicado y productos actualizados.")

    def calcular_precio_total(self):
        if not self.productos:
            print("No hay productos.")
            return
        total = self.productos[0]
        for p in self.productos[1:]:
            total += p
        print(f"Precio total de todos los productos: ${total:.2f}")

    def ejecutar(self):
        while True:
            print("\nMenú:")
            print("1. Agregar producto")
            print("2. Ver todos los productos")
            print("3. Aplicar descuento a todos")
            print("4. Calcular precio total")
            print("5. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.agregar_producto()
            elif opcion == "2":
                self.ver_productos()
            elif opcion == "3":
                self.aplicar_descuento_a_todos()
            elif opcion == "4":
                self.calcular_precio_total()
            elif opcion == "5":
                print("Saliendo del programa...")
                break
            else:
                print("Opción inválida.")

# Ejecutar la aplicación
if __name__ == "__main__":
    app = Aplicacion()
    app.ejecutar()
