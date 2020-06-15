from src.bingo import carton

def test_en_una_fila_no_existen_masde2_celdas_vacias_consecutivas():
    mi_carton = carton()
    for fila in range(3):
        for columna in range(7):
            check = 0
            if mi_carton[fila][columna] > 0 and mi_carton[fila][columna+1] > 0 and mi_carton[fila][columna+2] > 0:
                check = check + 1
            assert check == 0
