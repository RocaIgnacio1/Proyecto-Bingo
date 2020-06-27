from src import bingo

mi_carton = bingo.carton
def test_en_una_fila_no_existen_masde2_celdas_ocupadas_consecutivas():
    assert bingo.en_una_fila_no_existen_masde2_celdas_ocupadas_consecutivas(mi_carton)
