
from src.bingo import generar_carton_valido
from jinja2 import Template

template = Template(open('src/plantilla.j2').read())
file = open("bingo.html", "w")
file.write(template.render(tabla = generar_carton_valido()))
file.close()
