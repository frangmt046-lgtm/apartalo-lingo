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

@pytest.mark.unitaria
def test_personas_fuera_del_rango_da_error():
    with pytest.raises(ValueError):
        total_compra(sueltas=0, grupales=1, personas=1, paquetes=0)

@pytest.mark.unitaria
@pytest.mark.regresion
def test_compra_combinada_suma_todo():
    assert total_compra(sueltas=2, grupales=2, personas=3, paquetes=1) == 4480

@pytest.mark.unitaria
def test_cantidades_negativas_dan_error():
    with pytest.raises(ValueError):
        total_compra(sueltas=-1, grupales=0, personas=0, paquetes=0)