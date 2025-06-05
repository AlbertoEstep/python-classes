"""
Crea una clase abstracta Empleado con un método abstracto calcular_sueldo().
Luego, crea dos clases: EmpleadoPorHora y EmpleadoAsalariado.
Cada una debe implementar el cálculo de sueldo de forma diferente (por hora: precio/hora por horas trabajadas; asalariado con su salario mensual mas pluses).
"""

from abc import ABC, abstractmethod

# Clase abstracta
class Empleado(ABC):
    @abstractmethod
    def calcular_sueldo(self):
        pass

# Empleado por hora
class EmpleadoPorHora(Empleado):
    def __init__(self, precio_hora, horas_trabajadas):
        self.precio_hora = precio_hora
        self.horas_trabajadas = horas_trabajadas

    def calcular_sueldo(self):
        return self.precio_hora * self.horas_trabajadas

# Empleado asalariado
class EmpleadoAsalariado(Empleado):
    def __init__(self, salario_mensual, pluses=0):
        self.salario_mensual = salario_mensual
        self.pluses = pluses

    def calcular_sueldo(self):
        return self.salario_mensual + self.pluses

# Ejemplo de uso
if __name__ == "__main__":
    empleado1 = EmpleadoPorHora(precio_hora=15, horas_trabajadas=160)
    empleado2 = EmpleadoAsalariado(salario_mensual=2000, pluses=300)

    print("Sueldo empleado por hora:", empleado1.calcular_sueldo())
    print("Sueldo empleado asalariado:", empleado2.calcular_sueldo())
