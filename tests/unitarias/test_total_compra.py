import pytest
from apartalo.reglas import total_compra

@pytest.mark.unitaria
def test_una_sesion_suelta_cuesta_320():
    assert total_compra(sueltas=1, grupales=0, personas=0, paquetes=0) == 320

@pytest.mark.unitaria
def test_tres_sueltas_cuestan_960():
    assert total_compra(sueltas=3, grupales=0, personas=0, paquetes=0) == 960