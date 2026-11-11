"""Reglas de negocio de mi variante (Ejercicio 6).

Aquí van las funciones de R1 y R2. Escríbelas con TDD:
primero una prueba que falle (ROJO), luego el código mínimo para que pase (VERDE),
y después mejora el código sin romper las pruebas (REFACTOR).

Si una entrada no tiene sentido (horas negativas, un servicio que no existe, etc.),
la función debe lanzar ValueError.
"""

def cambio_de_sesion(horas_anticipacion):
    if horas_anticipacion < 0:
            raise ValueError("Las horas de anticipación no pueden ser negativas")
    if horas_anticipacion >= 24:
        return ("reprograma", 0)
    if horas_anticipacion < 4:
        return ("pierde", 0)
    return ("reprograma", 80)