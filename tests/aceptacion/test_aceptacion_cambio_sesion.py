import pytest
from apartalo.reglas import cambio_de_sesion

@pytest.mark.aceptacion
@pytest.mark.parametrize("horas, resultado, cargo", [
    (24, "reprograma", 0),   # ← una tupla por cada fila de tu tabla
    (23, "reprograma", 80),
    (4, "reprograma", 80),
    (3, "pierde", 0),
])
def test_cambio_de_sesion_segun_anticipacion(horas, resultado, cargo):
    # Dado que un alumno avisa con <horas> horas de anticipación
    anticipacion = horas
    # Cuando pide cambiar su sesión
    obtenido = cambio_de_sesion(anticipacion)
    # Entonces el resultado es <resultado> con un cargo de <cargo> pesos
    assert obtenido == (resultado, cargo)