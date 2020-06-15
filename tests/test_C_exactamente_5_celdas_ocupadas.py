from src.bingo import carton

def test_exactamente_5_celdas_por_fila():
    mi_carton = carton()
    for fila in range(3):
        check = 0
        for columna in range(9):
            if mi_carton[fila][columna] > 0:
                check = check + 1
        assert check == 5
