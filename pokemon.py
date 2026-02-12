import random

class Pokemon:
    def __init__(self, id_pokemon, nombre, nivel, vida, fuerza, defensa, velocidad):
        self.id_pokemon = id_pokemon
        self.nombre = nombre
        self.nivel = nivel
        self.vida_max = vida
        self.vida = vida
        self.fuerza = fuerza
        self.defensa = defensa
        self.velocidad = velocidad
        self.tipos = []  
        self.movimientos = []

    def datos_a_JSON(self):
        return {
            "id": self.id_pokemon,
            "nombre": self.nombre,
            "nivel": self.nivel,
            "vida": self.vida,
            "vida_max": self.vida_max,
            "fuerza": self.fuerza,
            "defensa": self.defensa,
            "velocidad": self.velocidad,
            "tipos": self.tipos,
            "movimientos": self.movimientos
        }

    def obtener_multiplicador(self, tipo_atq):
        mult = 1.0
        for t in self.tipos:
            mult *= self._tabla(t, tipo_atq)
        return mult

    def _tabla(self, mi_tipo, tipo_atq):
        debilidades = {
            "fuego": {"agua": 2.0, "planta": 0.5, "acero": 0.5},
            "agua": {"planta": 2.0, "fuego": 0.5},
            "planta": {"fuego": 2.0, "agua": 0.5, "volador": 2.0},
            "volador": {"acero": 2.0, "planta": 0.5},
            "acero": {"fuego": 2.0, "volador": 0.5}
        }
        return debilidades.get(mi_tipo, {}).get(tipo_atq, 1.0)

    def recibir_dano(self, dano):
        self.vida -= max(0, dano)
        return dano

"""--- Clases Hijas (Tipos) ---"""

class Fuego(Pokemon):
    def __init__(self, id_pokemon, nombre, nivel, vida, fuerza, defensa, velocidad):
        super().__init__(id_pokemon, nombre, nivel, vida, fuerza, defensa, velocidad)
        self.tipos = ["fuego"]

class Agua(Pokemon):
    def __init__(self, id_pokemon, nombre, nivel, vida, fuerza, defensa, velocidad):
        super().__init__(id_pokemon, nombre, nivel, vida, fuerza, defensa, velocidad)
        self.tipos = ["agua"]

class Planta(Pokemon):
    def __init__(self, id_pokemon, nombre, nivel, vida, fuerza, defensa, velocidad):
        super().__init__(id_pokemon, nombre, nivel, vida, fuerza, defensa, velocidad)
        self.tipos = ["planta"]

class Volador(Pokemon):
    def __init__(self, id_pokemon, nombre, nivel, vida, fuerza, defensa, velocidad):
        super().__init__(id_pokemon, nombre, nivel, vida, fuerza, defensa, velocidad)
        self.tipos = ["volador"]

class Acero(Pokemon):
    def __init__(self, id_pokemon, nombre, nivel, vida, fuerza, defensa, velocidad):
        super().__init__(id_pokemon, nombre, nivel, vida, fuerza, defensa, velocidad)
        self.tipos = ["acero"]