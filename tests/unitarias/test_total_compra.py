import pytest
from apartalo.reglas import total_compra

@pytest.mark.unitaria
def test_una_sesion_suelta_cuesta_320():
    assert total_compra(sueltas=1, grupales=0, personas=0, paquetes=0) == 320

@pytest.mark.unitaria
def test_tres_sueltas_cuestan_960():
    assert total_compra(sueltas=3, grupales=0, personas=0, paquetes=0) == 960

@pytest.mark.unitaria
def test_un_grupal_con_tres_personas_cuesta_570():
    assert total_compra(sueltas=0, grupales=1, personas=3, paquetes=0) == 570

@pytest.mark.unitaria
def test_un_paquete_cuesta_2700():
    assert total_compra(sueltas=0, grupales=0, personas=0, paquetes=1) == 2700