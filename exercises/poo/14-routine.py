"""Sistema de Seguimiento de Actividades Diarias

Objetivo:
Llevar un registro de actividades cotidianas: ejercicio, lectura, ocio, trabajo, etc.

Especificaciones técnicas

Clases:
* Actividad (abstracta):
    * Atributos: nombre, duracion (en minutos), fecha
    * Métodos abstractos: tipo() y detalle()
* Subclases:
    * Ejercicio: tiene también tipo_ejercicio (correr, nadar, etc.)
    * Lectura: incluye titulo_libro
    * Trabajo: incluye proyecto
    * Ocio: incluye descripcion_ocio

Interfaz:
* Registrable: con método to_dict().

Funcionalidades:
* Agregar actividad
* Ver actividades
* Filtrar por tipo (Ejercicio, Lectura, etc.)
* Ver total de tiempo invertido
* Guardar/Cargar en archivo JSON


"""

