from src import bingo

mi_carton = bingo.carton
def test_no_puede_haber_una_fila_vacia():
    assert bingo.no_puede_haber_una_fila_vacia(mi_carton)
