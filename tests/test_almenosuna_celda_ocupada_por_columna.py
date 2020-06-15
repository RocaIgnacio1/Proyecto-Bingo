from src.bingo import carton

def columnas(carton, numero_de_columna):
    columna = (carton[0][numero_de_columna], carton[1][numero_de_columna], carton[2][numero_de_columna])

    return columna

def test_al_menos_una_celda_ocupada_por_columna():
    mi_carton = carton()
    contador_columnas = 0
    contador = 0
    for contador_columnas in range(9):
        mi_columna = columnas(mi_carton,contador_columnas)
        if sum(mi_columna) >= 1:
            contador = contador + 1

    assert contador == 9
