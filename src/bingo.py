

def carton():
    carton = (
        (0,1,0,1,1,0,1,0,1),
        (1,0,1,1,0,1,0,1,1),
        (0,1,0,0,1,0,0,1,1)
    )
    return carton


def columnas(carton, numero_de_columna):
    columna = (carton[0][numero_de_columna], carton[1][numero_de_columna], carton[2][numero_de_columna])

    return columna
