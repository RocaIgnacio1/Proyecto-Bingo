from src.bingo import carton

def test_izquierda_derecha():
    mi_carton = carton()
    for celda in range(9):
        for fila in range(2):
            if mi_carton[fila][celda]!=0 and mi_carton[fila+1][celda]!=0:
                assert mi_carton[fila][celda] < mi_carton[fila+1][celda]
