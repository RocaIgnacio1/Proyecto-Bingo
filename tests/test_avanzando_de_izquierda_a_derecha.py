from src.bingo import carton

def test_izquierda_derecha():
    mi_carton = carton()
    for fila in range(3):
        for celda in range(8):
            if mi_carton[fila][celda]!=0 and mi_carton[fila][celda+1]!=0:
                assert mi_carton[fila][celda] < mi_carton[fila][celda+1]
