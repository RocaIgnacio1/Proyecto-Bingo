from src import bingo

mi_carton = bingo.carton
def test_izquierda_derecha():
    assert bingo.izquierda_derecha(mi_carton)
