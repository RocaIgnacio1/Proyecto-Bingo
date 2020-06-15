from src.bingo import carton


def test_aumentando_de_a_decenas():
    mi_carton = carton()
    contador = 0
    mayor = 0
    menor = -10
    for columna in range(9):
        mayor = mayor + 10
        menor = menor + 10
        for fila in range(3):
            if mi_carton[fila][columna] != 0:
                if columna==0:
                    assert mi_carton[fila][columna] >= 0 and mi_carton[fila][columna] < mayor
                elif columna==8:
                    assert mi_carton[fila][columna] >= menor and mi_carton[fila][columna] <= 90
                else:
                    assert mi_carton[fila][columna] >= menor and mi_carton[fila][columna] < mayor
