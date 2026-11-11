import pytest
from apartalo.reglas import cambio_de_sesion

@pytest.mark.unitaria
def test_cambio_con_24_horas_o_mas_se_reprograma_sin_costo():
    assert cambio_de_sesion(horas_anticipacion=30) == ("reprograma", 0)

@pytest.mark.unitaria
def test_cambio_entre_4_y_24_horas_cobra_80():
    assert cambio_de_sesion(horas_anticipacion=10) == ("reprograma", 80)

@pytest.mark.unitaria
def test_menos_de_4_horas_la_sesion_se_pierde():
    assert cambio_de_sesion(horas_anticipacion=2) == ("pierde", 0)

@pytest.mark.unitaria
def test_horas_negativas_lanzan_error():
    with pytest.raises(ValueError):
        cambio_de_sesion(horas_anticipacion=-5)