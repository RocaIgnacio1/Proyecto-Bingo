from src.bingo import carton

def test_no_puede_haber_una_fila_vacia():
    mi_carton = carton()
    contador = 0
    check = 0
    for fila in mi_carton:
        contador = 0
        for celda in fila:
            contador = contador + celda
            #Cuento la cantidad de celdas ocupadas
        if(contador >= 1):
            check = check + 1
    assert check == 3
