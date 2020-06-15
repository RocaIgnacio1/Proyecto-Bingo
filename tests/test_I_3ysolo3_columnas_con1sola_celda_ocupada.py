from src.bingo import carton

def test_sin_columnas_vacias():
    mi_carton = carton()
    check = 0
    confirmar = 0

    for columna in range(9):
        check = 0
        if mi_carton[0][columna] > 0:
            check = check + 1

        if mi_carton[1][columna] > 0:
            check = check + 1

        if mi_carton[2][columna] > 0:
            check = check + 1

        if check == 1:
            confirmar = confirmar + 1
    assert confirmar == 3
