"""
Crea una jerarquía de clases para representar electrodomésticos inteligentes.

La clase base Appliance debe tener:

    Un atributo model.

    Un método status() que será sobrescrito por las subclases.

La clase SmartAppliance debe heredar de Appliance y tener:

    Un atributo privado __wifi_signal que indica la intensidad de señal WiFi (0 a 100).

    Una propiedad wifi_signal que valida el valor al asignar.

    El método status() debe incluir el estado de la señal.

La clase SmartFridge debe heredar de SmartAppliance y sobrescribir el método status() para mostrar información del refrigerador y la señal WiFi.

Se debe usar polimorfismo con una función show_device_status(device).
"""