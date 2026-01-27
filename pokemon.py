import random

class Pokemon:
    def __init__(self, nombre, tipo, nivel, vida, fuerza, defensa, velocidad):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel
        self.vida = max(40, min(vida, 100))
        self.fuerza = min(fuerza, 15)
        self.defensa = min(defensa, 18)
        self.velocidad = min(velocidad, 100)
        self.movimientos = ["golpe normal", "golpe fuerte", "defender", "esquivar"]
        self.defendiendo = False
        self.esquivando = False

    def recibir_dano(self, dano, tipo_mov):
        if tipo_mov == "golpe normal" and self.defendiendo:
            dano = 0
        if tipo_mov == "golpe fuerte" and self.esquivando:
            dano = 0
        
        self.vida -= max(0, dano)

    def ejecutar_movimiento(self, otro_pokemon):
        self.defendiendo = False
        self.esquivando = False
        
        movimiento = random.choice(self.movimientos)
        
        if movimiento == "golpe normal":
            dano = self.fuerza - otro_pokemon.defensa
            otro_pokemon.recibir_dano(dano, "golpe normal")
        elif movimiento == "golpe fuerte":
            dano = (self.fuerza * 2) - otro_pokemon.defensa
            otro_pokemon.recibir_dano(dano, "golpe fuerte")
        elif movimiento == "defender":
            self.defendiendo = True
        elif movimiento == "esquivar":
            self.esquivando = True