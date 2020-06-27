from src import bingo

mi_carton = bingo.carton
def test_exactamente_5_celdas_por_fila():
    assert bingo.exactamente_5_celdas_por_fila(mi_carton)
