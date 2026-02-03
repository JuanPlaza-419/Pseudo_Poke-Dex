import random

"""Tabla de efectividades: [Atacante][Defensor]"""
TABLA_TIPOS = {
    "espadachín": {"hachero": 1.5, "lancero": 0.5, "espadachín": 1.0, "mago": 1.5},
    "hachero":    {"lancero": 1.5, "espadachín": 0.5, "hachero": 1.0, "mago": 1.5},
    "lancero":    {"espadachín": 1.5, "hachero": 0.5, "lancero": 1.0, "mago": 1.5},
    "mago":       {"espadachín": 1.5, "hachero": 1.5, "lancero": 1.5, "mago": 1.0}
}

class Pokemon:
    def __init__(self, nombre, nivel):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = None 
        
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
            """Cálculo de efectividad: Consulta la tabla según los tipos de ambos combatientes"""
            multiplicador = TABLA_TIPOS[self.tipo][otro_pokemon.tipo]
            
            """Cálculo de daño: (Fuerza + Potencia) - Defensa del rival"""
            dano_base = (self.fuerza + mov.potencia) - otro_pokemon.defensa
            
            """Aplicar el multiplicador de tipo al daño final (redondeado a entero)"""
            dano_final = int(dano_base * multiplicador)
            
            if multiplicador > 1.0:
                print("¡Es súper efectivo!")
            elif multiplicador < 1.0:
                print("No es muy efectivo...")
                
            otro_pokemon.recibir_dano(dano_final)
        else:
            print(f"| ¡El ataque de {self.nombre} ha fallado!")
            
    def aprender_movimiento(self, lista_movimientos, nuevo_mov):
        """Añade un movimiento o gestiona la sustitución si ya hay 4."""
        if len(lista_movimientos) < 4:
            lista_movimientos.append(nuevo_mov)
            print(f"¡{self.nombre} ha aprendido {nuevo_mov.nombre}!")
        else:
            print(f"\n--- {self.nombre} quiere aprender {nuevo_mov.nombre} ---")
            print("Pero ya conoce 4 movimientos. Elige uno para olvidar:")
            
            seleccion_realizada = False
            while not seleccion_realizada:
                for i, m in enumerate(lista_movimientos):
                    print(f"{i + 1}. {m.nombre}")
                
                opcion = input("Elige el número del movimiento a olvidar (1-4): ")
                
                if opcion in ["1", "2", "3", "4"]:
                    indice = int(opcion) - 1
                    olvidado = lista_movimientos[indice].nombre
                    lista_movimientos[indice] = nuevo_mov
                    print(f"¡Puf! {self.nombre} olvidó {olvidado} y aprendió {nuevo_mov.nombre}.")
                    seleccion_realizada = True
                else:
                    print("Por favor, selecciona un número válido del 1 al 4.")
        
        return lista_movimientos

"""--- CLASES ESPECIALIZADAS (Herencia) ---"""



class Espadachin(Pokemon):
    def __init__(self, nombre, nivel):
        super().__init__(nombre, nivel)
        self.tipo = "espadachín"

class Mago(Pokemon):
    def __init__(self, nombre, nivel):
        super().__init__(nombre, nivel)
        self.tipo = "mago"

class Lancero(Pokemon):
    def __init__(self, nombre, nivel):
        super().__init__(nombre, nivel)
        self.tipo = "lancero"

class Hachero(Pokemon):
    def __init__(self, nombre, nivel):
        super().__init__(nombre, nivel)
        self.tipo = "hachero"