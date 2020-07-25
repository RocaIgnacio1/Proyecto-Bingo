import random
import math

#Esta funcion genera un carton.
def intentoCarton():
    contador = 0
    carton = (
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
    )
    numerosCarton = 0

    while (numerosCarton < 15):

      contador = contador + 1
      if (contador == 50):
        return intentoCarton()

      numero = random.randint(1,90)
      columna = math.floor(numero / 10)

      if (columna == 9):
          columna = 8

      huecos = 0

      for i in range(3):
        if (carton[i][columna] == 0):
          huecos = huecos + 1
        if (carton[i][columna] == numero):
          huecos = 0
          break

      if (huecos < 2):
        continue

      fila = 0

      for j in range(3):
        huecos = 0
        for i in range(9):
          if (carton[fila][i] == 0):
              huecos = huecos + 1
        if (huecos < 5 or carton[fila][columna] != 0):
          fila = fila + 1
        else:
          break

      if (fila == 3):
        continue

      carton[fila][columna] = numero
      numerosCarton = numerosCarton + 1
      contador = 0

    for x in range(9):
      huecos = 0
      for y in range(3):
        if (carton[y][x] == 0):
            huecos = huecos + 1
      if (huecos == 3):
        return intentoCarton()

    return carton

#Esta funcion imprime un carton.
def imprimirCarton(mi_carton):
    if generar_carton_valido(mi_carton):
        for columna in range(3):
            for fila in range(9):
                print(carton[columna][fila], end = " ")
            print('\n')
        return 1
    else:
        return 0;

#Esta funcion verifica que los números del carton se encuentran en el rango 1 a 90.
def numeros_del_1_al_90(mi_carton):
	for fila in mi_carton:
		for celda in fila:
			if celda < 0 or celda > 90:
				return False
	return True

#Esta funcion verifica que cada columna de un carton (contando de izquierda a derecha) contiene numeros que van del 1 al 9, 10 al 19, 20 al 29 ..., 70 al 79 y 80 al 90.
def aumentando_de_a_decenas(mi_carton):
    menor = 1
    mayor = 9
    for columna in range(9):
        for fila in range(3):
            if mi_carton[fila][columna] != 0:
                if mi_carton[fila][columna] < menor or mi_carton[fila][columna] > mayor:
                        return False;
        menor = mayor + 1
        mayor = mayor + 10
    return True;

#Esta funcion verifica que cada fila de un carton tiene exactamente 5 celdas ocupadas.
def exactamente_5_celdas_por_fila(mi_carton):
    for fila in range(3):
        check = 0
        for columna in range(9):
            if mi_carton[fila][columna] > 0:
                check = check + 1
    return check == 5

#Esta funcion verifica que cada carton tiene 15 celdas ocupadas.
def contar_celdas_ocupadas(mi_carton):
    contador = 0
    for fila in mi_carton:
        for celda in fila:
            if celda > 0:
                contador = contador + 1
    return contador == 15

#Esta funcion verifica que los números de las columnas izquierdas son menores que los de las columnas a la derecha.
def izquierda_derecha(mi_carton):
    auxiliar=0
    for fila in range(3):
        for celda in range(8):
            if mi_carton[fila][celda]!=0:
                if auxiliar != 0:
                    if mi_carton[fila][celda] <= auxiliar:
                        return False
                auxiliar=mi_carton[fila][celda]
        auxiliar = 0
    return True

#Esta funcion verifica que para una misma columna, sus números están ordenados de menor a mayor de arriba hacia abajo.
def arriba_abajo(mi_carton):
    for celda in range(9):
        auxiliar=0
        for fila in range(3):
            if mi_carton[fila][celda]!=0:
                if mi_carton[fila][celda] <= auxiliar:
                    return False
                auxiliar=mi_carton[fila][celda]
    return True

#Esta funcion verifica que no pueden existir columnas vacias.
def sin_columnas_vacias(mi_carton):
    for columna in range(9):
        check = 1
        if mi_carton[0][columna] > 0 or mi_carton[1][columna] > 0 or mi_carton[2][columna] > 0:
            check = 0
    return check == 0

#Esta funcion verifica que no pueden existir columnas con sus tres celdas ocupadas.
def sin_columnas_completamente_ocupadas(mi_carton):
    for columna in range(9):
        check = 1
        if mi_carton[0][columna] == 0 or mi_carton[1][columna] == 0 or mi_carton[2][columna] == 0:
            check = 0
    return check == 0

#Esta funcion verifica que cada carton debe tener 3 y solo 3 columas con solo una celda ocupada.
def tres_columnas_con_una_sola_fila_ocupada(mi_carton):
    check = 0
    confirmar = 0
    for columna in range(9):
        check = 0
        if mi_carton[0][columna] > 0:
            check = check + 1

        if mi_carton[1][columna] > 0:
            check = check + 1

        if mi_carton[2][columna] > 0:
            check = check + 1

        if check == 1:
            confirmar = confirmar + 1
    return confirmar == 3

#Esta funcion verifica que en una fila no existen más de dos celdas vacías consecutivas.
def en_una_fila_no_existen_masde2_celdas_vacias_consecutivas(mi_carton):
    for fila in range(3):
        for columna in range(7):
            check = 0
            if mi_carton[fila][columna] == 0 and mi_carton[fila][columna+1] == 0 and mi_carton[fila][columna+2] == 0:
                check = check + 1
            if check == 1:
                return False
    return True

#Esta funcion verifica que n una fila no existen más de dos celdas ocupadas consecutivas.
def en_una_fila_no_existen_masde2_celdas_ocupadas_consecutivas(mi_carton):
    for fila in range(3):
        for columna in range(7):
            check = 0
            if mi_carton[fila][columna] > 0 and mi_carton[fila][columna+1] > 0 and mi_carton[fila][columna+2] > 0:
                check = check + 1
            if check == 1:
                return False
    return True

#Esta funcion verifica que no puede haber una fila completamente vacia.
def no_puede_haber_una_fila_vacia(mi_carton):
    contador = 0
    check = 0
    for fila in mi_carton:
        contador = 0
        for celda in fila:
            contador = contador + celda
            #Cuento la cantidad de celdas ocupadas
        if(contador >= 1):
            check = check + 1
            # Check es un contador de filas aceptadas
    return check == 3

#Esta funcion verifica que cada carton es una matrix de 9 x 3.
def carton_9x3(mi_carton):
    cantidad_filas = 0
    cantidad_columnas = 0
    check = True
    for columnas in mi_carton:
        cantidad_filas = 0
        for filas in columnas:
            cantidad_filas = cantidad_filas + 1
        if cantidad_filas != 9:
            check = False
        cantidad_columnas = cantidad_columnas + 1
    if cantidad_columnas != 3:
        check = False
    return check

def generar_carton_valido():
    r=0
    while(r==0):
        mi_carton = intentoCarton()
        if (numeros_del_1_al_90(mi_carton) == True
        and
        aumentando_de_a_decenas(mi_carton) == True
        and
        exactamente_5_celdas_por_fila(mi_carton) == True
        and
        contar_celdas_ocupadas(mi_carton) == True
        and
        izquierda_derecha(mi_carton) == True
        and
        arriba_abajo(mi_carton) == True
        and
        sin_columnas_vacias(mi_carton) == True
        and
        sin_columnas_completamente_ocupadas(mi_carton) == True
        and
        tres_columnas_con_una_sola_fila_ocupada(mi_carton) == True
        and
        en_una_fila_no_existen_masde2_celdas_vacias_consecutivas(mi_carton) == True
        and
        en_una_fila_no_existen_masde2_celdas_ocupadas_consecutivas(mi_carton) == True
        and
        no_puede_haber_una_fila_vacia(mi_carton) == True
        and
        carton_9x3(mi_carton) == True):
                r=1
    return mi_carton
carton = generar_carton_valido()
