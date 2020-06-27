from src import bingo

mi_carton = bingo.carton
def test_carton_9x3():
    assert bingo.carton_9x3(mi_carton)
