from src import bingo

mi_carton = bingo.carton
def test_tres_columnas_con_una_sola_fila_ocupada():
    assert bingo.tres_columnas_con_una_sola_fila_ocupada(mi_carton)
