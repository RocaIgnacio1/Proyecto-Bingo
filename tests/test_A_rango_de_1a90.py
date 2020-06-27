from src import bingo

mi_carton = bingo.carton
def test_numeros_del_1_al_90():
    assert bingo.numeros_del_1_al_90(mi_carton)
