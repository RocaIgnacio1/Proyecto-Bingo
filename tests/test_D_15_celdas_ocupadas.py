from src import bingo

mi_carton = bingo.carton
def test_contar_celdas_ocupadas():
    assert bingo.contar_celdas_ocupadas(mi_carton)
