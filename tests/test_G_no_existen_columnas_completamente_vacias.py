from src.bingo import carton

def test_sin_columnas_vacias():
    mi_carton = carton()

    for columna in range(9):
        check = 1
        if mi_carton[0][columna] > 0 or mi_carton[1][columna] > 0 or mi_carton[2][columna] > 0:
            check = 0

        assert check == 0
