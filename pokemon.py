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

    def recibir_dano(self, dano):
        dano_final = max(0, dano)
        self.vida -= dano_final
        print(f"{self.nombre} recibe {dano_final} de daño. Vida restante: {max(0, self.vida)}")

    def ejecutar_movimiento(self, movimiento_obj, otro_pokemon):
        print(f"\n{self.nombre} usa {movimiento_obj.nombre.upper()}")
        
        """El daño se basa en: Fuerza del Pokemon + Potencia del Movimiento - Defensa del Rival"""
        dano = (self.fuerza + movimiento_obj.potencia) - otro_pokemon.defensa
        otro_pokemon.recibir_dano(dano)