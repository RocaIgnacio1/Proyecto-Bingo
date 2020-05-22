# Los 0 indican que la celda esta vacia
# Los 1 indican que la celda esta ocupada
def carton():
    carton = (
                (2,  0,  0, 35, 41, 51,  0, 70, 85),
                (0, 14, 27, 38,  0, 52, 63,  0, 87),
                (0, 18,  0,  0, 49,  0,  0, 79,  0)
    )
    return carton


def columnas(carton, numero_de_columna):
    columna = (carton[0][numero_de_columna], carton[1][numero_de_columna], carton[2][numero_de_columna])

    return columna
