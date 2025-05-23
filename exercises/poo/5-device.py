"""
(Resuelto)
Crea una clase base llamada Device con un método turn_on() que sea sobrescrito por las clases hijas Smartphone y Laptop. Cada clase hija debe imprimir un mensaje diferente cuando se enciende el dispositivo.

Además, crea una función activate_device(device) que reciba cualquier objeto Device y llame a su método turn_on() (polimorfismo).
"""

class Device:
    def __init__(self, brand):
        self.brand = brand

    def turn_on(self):
        print("Turning on device...")

class Smartphone(Device):
    def turn_on(self):
        print(f"{self.brand} smartphone is booting up.")

class Laptop(Device):
    def turn_on(self):
        print(f"{self.brand} laptop is starting.")

def activate_device(device):
    device.turn_on()

# Example usage
phone = Smartphone("Samsung")
laptop = Laptop("Dell")
generic = Device("GenericBrand")

activate_device(phone)
activate_device(laptop)
activate_device(generic)
