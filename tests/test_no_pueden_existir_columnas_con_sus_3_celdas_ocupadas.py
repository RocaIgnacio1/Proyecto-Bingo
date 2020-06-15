from src.bingo import carton

def test_sin_columnas_vacias():
    mi_carton = carton()
    check = 0

    for columna in range(9):
        if mi_carton[0][columna] > 0 and mi_carton[1][columna] > 0 and mi_carton[2][columna] > 0:
            check = 1

        assert check == 0
