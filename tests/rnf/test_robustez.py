import pytest
from apartalo.reglas import cambio_de_sesion, total_compra


@pytest.mark.rnf
@pytest.mark.parametrize("horas", [-1, -24])
def test_horas_invalidas_se_rechazan(horas):
    with pytest.raises(ValueError):
        cambio_de_sesion(horas_anticipacion=horas)


@pytest.mark.rnf
@pytest.mark.parametrize("sueltas, grupales, personas, paquetes", [
    (-1, 0, 0, 0),
    (0, 1, 1, 0),
    (0, 1, 5, 0),
    (0, 0, 0, -2)
])
def test_compras_invalidas_se_rechazan(sueltas, grupales, personas, paquetes):
    with pytest.raises(ValueError):
        total_compra(sueltas, grupales, personas, paquetes)