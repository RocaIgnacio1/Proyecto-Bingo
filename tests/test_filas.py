from src.bingo import carton

def test_no_puede_haber_una_fila_vacia():
    mi_carton = carton()
    contador = 0
    check = 0
    for fila in mi_carton:
        contador = 0
        for celda in fila:
            contador = contador + celda
        if(contador >= 1):
            check = check + 1
            # Check es un contador de filas aceptadas
    assert check == 3
