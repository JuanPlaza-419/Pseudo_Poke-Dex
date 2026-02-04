import random

class Pokemon:
    def __init__(self, nombre, nivel):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = "Normal"
        self.vida = random.randint(40, 100)
        self.fuerza = random.randint(5, 15)
        self.defensa = random.randint(5, 18)
        self.velocidad = random.randint(1, 100)

    def obtener_multiplicador(self, tipo_atq):
        return 1.0

    def recibir_dano(self, dano):
        dano_final = max(0, dano)
        self.vida -= dano_final
        print(f"| {self.nombre} recibe {dano_final} de daño. Vida restante: {max(0, self.vida)}")

    def ejecutar_movimiento(self, mov, otro_pokemon):
        if mov.tipo != self.tipo:
            raise ValueError(f"¡ERROR! {self.nombre} no puede usar {mov.tipo}.")
        print(f"\n>> {self.nombre} usa {mov.nombre.upper()}...")
        if random.randint(1, 100) <= mov.precision:
            mult = otro_pokemon.obtener_multiplicador(self.tipo)
            dano = int(((self.fuerza + mov.potencia) - otro_pokemon.defensa) * mult)
            if mult > 1.0: print("¡Es súper efectivo!")
            elif mult < 1.0: print("No es muy efectivo...")
            otro_pokemon.recibir_dano(dano)
        else:
            print(f"| ¡El ataque ha fallado!")

    def aprender_movimiento(self, lista_movimientos, nuevo_mov):
        """Añade o sustituye un movimiento y devuelve la lista actualizada"""
        if len(lista_movimientos) < 4:
            lista_movimientos.append(nuevo_mov)
        else:
            print(f"\n--- {self.nombre} quiere aprender {nuevo_mov.nombre} ---")
            for i, m in enumerate(lista_movimientos):
                print(f"{i + 1}. {m.nombre}")
            opcion = input("Elige el número del movimiento a olvidar (1-4): ")
            indice = int(opcion) - 1
            lista_movimientos[indice] = nuevo_mov
        
        return lista_movimientos

"""--- Clases Hijas ---"""

class Volador(Pokemon):
    def __init__(self, nombre, nivel):
        super().__init__(nombre, nivel)
        self.tipo = "volador"
    def obtener_multiplicador(self, tipo_atq):
        if tipo_atq == "acero": return 2.0
        return 1.0

class Acero(Pokemon):
    def __init__(self, nombre, nivel):
        super().__init__(nombre, nivel)
        self.tipo = "acero"
    def obtener_multiplicador(self, tipo_atq):
        if tipo_atq == "fuego": return 2.0
        if tipo_atq == "volador": return 0.5
        return 1.0