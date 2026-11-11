import pytest
from apartalo.reglas import total_compra

@pytest.mark.unitaria
def test_una_sesion_suelta_cuesta_320():
    assert total_compra(sueltas=1, grupales=0, personas=0, paquetes=0) == 320