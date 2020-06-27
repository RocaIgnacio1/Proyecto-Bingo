[![Build Status](https://travis-ci.com/RocaIgnacio1/Proyecto-Bingo.svg?branch=master)](https://travis-ci.com/RocaIgnacio1/Proyecto-Bingo)





# Bingo

Proyecto hecho en python3 que genera un carton de bingo, a partir de algunas reglas.
Escrito por: Ignacio Roca. Con la ayuda de Mariano Dagostino.
2020


# Reglas que hacen que un cartón sea considerado válido:

- Los números del carton se encuentran en el rango 1 a 90.
- Cada columna de un carton (contando de izquierda a derecha) contiene numeros que van del 1 al 9, 10 al 19, 20 al 29 ..., 70 al 79 y 80 al 90.
- Cada fila de un carton tiene exactamente 5 celdas ocupadas.
- Cada carton es una matrix de 3 x 9.
- Cada carton tiene 15 celdas ocupadas.
- Los números de las columnas izquierdas son menores que los de las columnas a la derecha.
- Para una misma columna, sus números están ordenados de menor a mayor de arriba hacia abajo.
- No pueden existir columnas vacias.
- No pueden existir columnas con sus tres celdas ocupadas.
- Cada carton debe tener 3 y solo 3 columas con solo una celda ocupada.
- En una fila no existen más de dos celdas vacías consecutivas.
- En una fila no existen más de dos celdas ocupadas consecutivas.

# Uso del Proyecto

Para clonarlo:
git clone https://github.com/RocaIgnacio1/Proyecto-Bingo

Una vez clonado, ejecute:
python src/bingo.py
