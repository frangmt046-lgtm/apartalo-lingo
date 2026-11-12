import pytest
from apartalo.reglas import total_compra


@pytest.mark.aceptacion
@pytest.mark.parametrize("sueltas, grupales, personas, paquetes, total", [
    (1, 0, 0, 0, 320),
    (0, 1, 2, 0, 380),
    (0, 1, 4, 0, 760),
    (0, 0, 0, 1, 2700),
    (1, 1, 2, 1, 3400),
])

def test_total_de_la_compra(sueltas, grupales, personas, paquetes, total):
    # Dado que un alumno compra <sueltas> sesiones sueltas, <grupales> sesiones grupales de <personas> personas y <paquetes> paquetes
    # (los datos ya vienen de la tabla)
    # Cuando paga su compra
    obtenido = total_compra(sueltas, grupales, personas, paquetes)
    # Entonces el total es de <total> pesos
    assert obtenido == total