from pokemon import Pokemon
from movimiento import *

RODRIGO = Pokemon(1, "Rodrigo", 20, 110, 22, 25, 40)
RODRIGO.definir_tipos(["planta", "acero"])
MOVS_RODRIGO = [HOJA_AFILADA, GARRA_METAL, LATIGO_CEPA, CUERPO_PESADO]

ARTHUR = Pokemon(2, "Arthur", 20, 95, 28, 15, 65)
ARTHUR.definir_tipos(["fuego", "agua"])
MOVS_ARTHUR = [LANZALLAMAS, HIDROPULSO, RUEDA_FUEGO, BURBUJA]