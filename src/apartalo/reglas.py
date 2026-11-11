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
    if grupales > 0 and personas < 2 or personas > 4:
        raise ValueError("La cantidad de personas esta fuera del rango")
    if sueltas > 0:
        return(320 * sueltas)
    if grupales > 0:
        return(190 * personas)
    if paquetes >0:
        return(2700 * paquetes)
    return 320
