import random

class Pokemon:
    def __init__(self, nombre, tipo, nivel):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel
        self.vida = random.randint(40, 100)
        self.fuerza = random.randint(5, 15)
        self.defensa = random.randint(5, 18)
        self.velocidad = random.randint(1, 100)
        
        self.movimientos = ["golpe normal", "golpe fuerte", "defender", "esquivar"]
        self.defendiendo = False
        self.esquivando = False

    def recibir_dano(self, dano, tipo_mov):
        if tipo_mov == "golpe normal" and self.defendiendo:
            print(f"¡{self.nombre} bloqueó el golpe!")
            dano = 0
        if tipo_mov == "golpe fuerte" and self.esquivando:
            print(f"¡{self.nombre} esquivó el golpe!")
            dano = 0
        
        dano_final = max(0, dano)
        self.vida -= dano_final
        print(f"{self.nombre} pierde {dano_final} de vida. Vida restante: {max(0, self.vida)}")

    def ejecutar_movimiento(self, otro_pokemon):
        self.defendiendo = False
        self.esquivando = False
        mov = random.choice(self.movimientos)
        print(f"{self.nombre} usa {mov.upper()}")

        if mov == "golpe normal":
            dano = self.fuerza - otro_pokemon.defensa
            otro_pokemon.recibir_dano(dano, "golpe normal")
        elif mov == "golpe fuerte":
            dano = (self.fuerza * 2) - otro_pokemon.defensa
            otro_pokemon.recibir_dano(dano, "golpe fuerte")
        elif mov == "defender":
            self.defendiendo = True
        elif mov == "esquivar":
            self.esquivando = True