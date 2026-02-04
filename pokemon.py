import random

class Pokemon:
    def __init__(self, nombre, nivel):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = "Normal" # Se sobreescribe en los hijos
        
        """Estadísticas aleatorias base"""
        self.vida = random.randint(40, 100)
        self.fuerza = random.randint(5, 15)
        self.defensa = random.randint(5, 18)
        self.velocidad = random.randint(1, 100)

    def obtener_multiplicador(self, tipo_atacante):
        """Este método define las debilidades. Retorna 2.0 si es débil, 0.5 si es fuerte."""
        return 1.0

    def recibir_dano(self, dano):
        """Aplica el daño restándolo de la vida"""
        dano_final = max(0, dano)
        self.vida -= dano_final
        print(f"| {self.nombre} recibe {dano_final} de daño. Vida restante: {max(0, self.vida)}")

    def ejecutar_movimiento(self, mov, otro_pokemon):
        """Lógica de combate con ventajas de tipo integradas"""
        if mov.tipo != self.tipo:
            raise ValueError(f"¡ERROR! {self.nombre} no puede usar movimientos de tipo {mov.tipo}.")

        print(f"\n>> {self.nombre} usa {mov.nombre.upper()}...")
        
        if random.randint(1, 100) <= mov.precision:
            
            """Pregunta al rival cuánto daño recibe de nuestro tipo"""
            multiplicador = otro_pokemon.obtener_multiplicador(self.tipo)
            
            dano_base = (self.fuerza + mov.potencia) - otro_pokemon.defensa
            dano_final = int(dano_base * multiplicador)
            
            if multiplicador > 1.0: print("¡Es súper efectivo! (x2.0)")
            elif multiplicador < 1.0: print("No es muy efectivo... (x0.5)")
                
            otro_pokemon.recibir_dano(dano_final)
        else:
            print(f"| ¡El ataque de {self.nombre} ha fallado!")

"""--- SUBCLASES POR TIPO ---"""

class Fuego(Pokemon):
    def __init__(self, nombre, nivel):
        super().__init__(nombre, nivel)
        self.tipo = "fuego"

    def obtener_multiplicador(self, tipo_atq):
        if tipo_atq == "agua": return 2.0
        if tipo_atq in ["planta", "acero"]: return 0.5
        return 1.0

class Agua(Pokemon):
    def __init__(self, nombre, nivel):
        super().__init__(nombre, nivel)
        self.tipo = "agua"

    def obtener_multiplicador(self, tipo_atq):
        if tipo_atq == "planta": return 2.0
        if tipo_atq == "fuego": return 0.5
        return 1.0

class Planta(Pokemon):
    def __init__(self, nombre, nivel):
        super().__init__(nombre, nivel)
        self.tipo = "planta"

    def obtener_multiplicador(self, tipo_atq):
        if tipo_atq in ["fuego", "volador"]: return 2.0
        if tipo_atq == "agua": return 0.5
        return 1.0

class Volador(Pokemon):
    def __init__(self, nombre, nivel):
        super().__init__(nombre, nivel)
        self.tipo = "volador"

    def obtener_multiplicador(self, tipo_atq):
        if tipo_atq == "acero": return 2.0
        if tipo_atq == "planta": return 0.5
        return 1.0

class Acero(Pokemon):
    def __init__(self, nombre, nivel):
        super().__init__(nombre, nivel)
        self.tipo = "acero"

    def obtener_multiplicador(self, tipo_atq):
        if tipo_atq == "fuego": return 2.0
        if tipo_atq == "volador": return 0.5
        return 1.0