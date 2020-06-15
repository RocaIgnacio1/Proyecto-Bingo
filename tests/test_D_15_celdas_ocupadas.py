from src.bingo import carton


def test_contar_celdas_ocupadas():
    mi_carton = carton()
    contador = 0
    for fila in mi_carton:
        for celda in fila:
            if celda > 0:
                contador = contador + 1

    assert contador == 15
