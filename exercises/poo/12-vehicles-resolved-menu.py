"""
Desarrolla un sistema que administre Vehículos. Debe incluir:

- Una clase abstracta Vehiculo con método calcular_precio_final().
- Subclases Auto y Moto que implementen ese método.
- Una interfaz Descontable para aplicar descuentos.
- Sobrecarga del método constructor para permitir crear vehículos con o sin descuento inicial.
- Sobrecarga del operador + para sumar precios de vehículos.
- Un menú de usuario con opciones para:
    - Agregar vehículo
    - Mostrar todos los vehículos
    - Aplicar descuento
    - Calcular precio total
    - Salir
"""


from abc import ABC, abstractmethod

class Descontable(ABC):
    @abstractmethod
    def aplicar_descuento(self, porcentaje):
        pass

class Vehiculo(ABC):
    def __init__(self, marca, precio):
        self.marca = marca
        self.precio = precio

    @abstractmethod
    def calcular_precio_final(self):
        pass

    def __str__(self):
        return f"{self.descripcion()} - ${self.calcular_precio_final():.2f}"

    def __add__(self, otro):
        return self.calcular_precio_final() + otro.calcular_precio_final()

class Auto(Vehiculo, Descontable):
    def __init__(self, marca, precio, puertas=4):
        super().__init__(marca, precio)
        self.puertas = puertas

    def descripcion(self):
        return f"Auto {self.marca} ({self.puertas} puertas)"

    def calcular_precio_final(self):
        return self.precio

    def aplicar_descuento(self, porcentaje):
        self.precio -= self.precio * (porcentaje / 100)

class Moto(Vehiculo, Descontable):
    def __init__(self, marca, precio, tipo="urbana"):
        super().__init__(marca, precio)
        self.tipo = tipo

    def descripcion(self):
        return f"Moto {self.marca} ({self.tipo})"

    def calcular_precio_final(self):
        return self.precio

    def aplicar_descuento(self, porcentaje):
        self.precio -= self.precio * (porcentaje / 100)

# Menú
vehiculos = []

def menu():
    while True:
        print("\n=== GESTIÓN DE VEHÍCULOS ===")
        print("1. Agregar vehículo")
        print("2. Ver todos los vehículos")
        print("3. Aplicar descuento a todos")
        print("4. Calcular precio total")
        print("5. Salir")
        
        op = input("Opción: ")
        if op == "1":
            tipo = input("¿Auto o Moto? ").strip().lower()
            marca = input("Marca: ")
            precio = float(input("Precio: "))

            if tipo == "auto":
                puertas = int(input("¿Cuántas puertas? (default 4): ") or 4)
                vehiculos.append(Auto(marca, precio, puertas))
            elif tipo == "moto":
                tipo_moto = input("Tipo de moto (urbana/deportiva): ").strip()
                vehiculos.append(Moto(marca, precio, tipo_moto))
            else:
                print("Tipo no válido.")
        elif op == "2":
            if not vehiculos:
                print("No hay vehículos.")
            for v in vehiculos:
                print(v)
        elif op == "3":
            porc = float(input("Porcentaje de descuento: "))
            for v in vehiculos:
                v.aplicar_descuento(porc)
            print("Descuentos aplicados.")
        elif op == "4":
            total = sum(v.calcular_precio_final() for v in vehiculos)
            print(f"Precio total: ${total:.2f}")
        elif op == "5":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

# Descomenta para ejecutar el menú:
menu()
