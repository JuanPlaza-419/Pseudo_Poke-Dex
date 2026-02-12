class Movimiento:
    def __init__(self, nombre, tipo, potencia, precision):
        self.nombre = nombre
        self.tipo = tipo.lower()
        self.potencia = potencia
        self.precision = precision

HOJA_AFILADA = Movimiento("Hoja Afilada", "planta", 15, 95)
GARRA_METAL = Movimiento("Garra Metal", "acero", 18, 90)
LATIGO_CEPA = Movimiento("Latigo Cepa", "planta", 10, 100)
CUERPO_PESADO = Movimiento("Cuerpo Pesado", "acero", 25, 70)

LANZALLAMAS = Movimiento("Lanzallamas", "fuego", 20, 100)
HIDROPULSO = Movimiento("Hidropulso", "agua", 18, 95)
RUEDA_FUEGO = Movimiento("Rueda Fuego", "fuego", 15, 100)
BURBUJA = Movimiento("Burbuja", "agua", 10, 100)