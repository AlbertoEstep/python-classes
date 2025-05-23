"""
Crea una jerarquía de clases para representar dispositivos inteligentes con batería.

La clase base SmartDevice debe tener:

    Un atributo brand.

    Un método status() que será sobrescrito por las subclases.

La clase BatteryDevice debe heredar de SmartDevice y:

    Tener un atributo privado __battery_level.

    Usar una propiedad battery_level para obtener y modificar la batería (validando que esté entre 0 y 100).

    Sobrescribir el método status() para incluir el nivel de batería.

La clase Smartphone debe heredar de BatteryDevice y sobrescribir status() para incluir marca y batería.

Usa polimorfismo con una función print_status(device) que acepte cualquier tipo de dispositivo.
"""

class SmartDevice:
    def __init__(self, brand):
        self.brand = brand

    def status(self):
        return "Generic smart device status."


class BatteryDevice(SmartDevice):
    def __init__(self, brand, battery_level):
        super().__init__(brand)
        self.__battery_level = None
        self.battery_level = battery_level

    @property
    def battery_level(self):
        return self.__battery_level

    @battery_level.setter
    def battery_level(self, value):
        if 0 <= value <= 100:
            self.__battery_level = value
        else:
            print("Battery level must be between 0 and 100.")

    def status(self):
        return f"{self.brand} device with battery at {self.battery_level}%."


class Smartphone(BatteryDevice):
    def status(self):
        return f"{self.brand} smartphone — Battery: {self.battery_level}%"


# Polymorphic function
def print_status(device):
    print(device.status())


# Example usage
generic = SmartDevice("GenericBrand")
device = BatteryDevice("Anker", 75)
phone = Smartphone("iPhone", 50)

print_status(generic)
print_status(device)
print_status(phone)

# Trying to set invalid battery level
phone.battery_level = 150  # Should show warning
print_status(phone)
