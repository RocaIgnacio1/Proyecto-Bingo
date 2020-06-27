from src import bingo

mi_carton = bingo.carton
def test_sin_columnas_completamente_ocupadas():
    assert bingo.sin_columnas_completamente_ocupadas(mi_carton)
