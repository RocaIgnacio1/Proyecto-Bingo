from src.bingo import carton
from src.bingo import columnas

def test_contar_celdas_ocupadas():
    mi_carton = carton()
    contador = 0
    for fila in mi_carton:
        for celda in fila:
            contador = contador + celda
# Esperamos encontrar 15 celdas ocupadas
    assert contador == 15


def test_al_menos_una_celda_ocupada_por_columna():
    mi_carton = carton()
    contador_columnas = 0
    contador = 0
    for contador_columnas in range(9):
        mi_columna = columnas(mi_carton,contador_columnas)
        if sum(mi_columna) >= 1:
            contador = contador + 1

    assert contador == 9
