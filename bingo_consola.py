from src import bingo
from jinja2 import Template

carton = bingo.generar_carton_valido()
bingo.imprimirCarton(carton)
