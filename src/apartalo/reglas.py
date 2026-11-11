def cambio_de_sesion(horas_anticipacion):
    """R2: decide qué pasa si el alumno cambia o cancela una sesión.

    Regresa una tupla (resultado, cargo):
    - 24 horas o más: ("reprograma", 0)
    - 4 horas o más, pero menos de 24: ("reprograma", 80)
    - menos de 4 horas: ("pierde", 0)
    Lanza ValueError si las horas son negativas.
    """
    if horas_anticipacion < 0:
        raise ValueError("Las horas de anticipación no pueden ser negativas")
    if horas_anticipacion >= 24:
        return ("reprograma", 0)
    if horas_anticipacion < 4:
        return ("pierde", 0)
    return ("reprograma", 80)

def total_compra(sueltas, grupales, personas, paquetes):
    """R1: total de una compra en Lingo.

    total = sueltas × 320 + grupales × 190 × personas + paquetes × 2700
    Lanza ValueError si hay cantidades negativas o si una sesión
    grupal no tiene de 2 a 4 personas.
    """
    if sueltas < 0 or grupales < 0 or paquetes < 0:
        raise ValueError("Las cantidades no pueden ser negativas")
    if grupales > 0:
        if personas < 2 or personas > 4:
            raise ValueError("Una sesión grupal debe tener de 2 a 4 personas")
    return 320 * sueltas + 190 * grupales * personas + 2700 * paquetes