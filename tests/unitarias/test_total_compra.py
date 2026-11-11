import pytest
from apartalo.reglas import total_compra

@pytest.mark.unitaria
def test_una_sesion_suelta_cuesta_320():
    assert total_compra(sueltas=___, grupales=___, personas=___, paquetes=___) == ___