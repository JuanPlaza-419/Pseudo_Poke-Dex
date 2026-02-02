import random

class Pokemon:
    def __init__(self, nombre, tipo, nivel):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel
        
        """Estadísticas aleatorias con los límites que definimos"""
        self.vida = random.randint(40, 100)
        self.fuerza = random.randint(5, 15)
        self.defensa = random.randint(5, 18)
        self.velocidad = random.randint(1, 100)

    def recibir_dano(self, dano):
        """Aplica el daño restándolo de la vida, asegurando que no sea negativo."""
        dano_final = max(0, dano)
        self.vida -= dano_final
        print(f"| {self.nombre} recibe {dano_final} de daño. Vida restante: {max(0, self.vida)}")

    def ejecutar_movimiento(self, mov, otro_pokemon):
        """Ejecuta un objeto Movimiento tras validar tipo y precisión."""
        
        """Validación de Tipo: Solo puede usar movimientos de su propio tipo"""
        if mov.tipo != self.tipo:
            raise ValueError(f"¡ERROR! {self.nombre} ({self.tipo}) no puede usar un movimiento de tipo {mov.tipo}.")

        print(f"\n>> {self.nombre} intenta usar {mov.nombre.upper()}...")
        
        """Lógica de Precisión: Tirada de probabilidad entre 1 y 100"""
        probabilidad = random.randint(1, 100)
        
        if probabilidad <= mov.precision:
            """Cálculo de daño: (Fuerza + Potencia) - Defensa del rival"""
            dano = (self.fuerza + mov.potencia) - otro_pokemon.defensa
            otro_pokemon.recibir_dano(dano)
        else:
            print(f"| ¡El ataque de {self.nombre} ha fallado!")