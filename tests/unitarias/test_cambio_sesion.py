import pytest
from apartalo.reglas import cambio_de_sesion

@pytest.mark.unitaria
def test_cambio_con_24_horas_o_mas_se_reprograma_sin_costo():
    assert cambio_de_sesion(horas_anticipacion=30) == ("reprograma", 0)