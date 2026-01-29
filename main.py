from pokemon import Pokemon
from movimiento import Movimiento
import random

"""Crear los Pokémon"""
p1 = Pokemon("Jose Luis", "Cuñao", 20)
p2 = Pokemon("Paco Pepe", "Gitano", 20)

"""Movimientos de Jose Luis"""
movs_p1 = [
    Movimiento("Cerveza Fria", "Salud", 5, 100),
    Movimiento("Machismo", "Psicologico", 12, 80),
    Movimiento("Golpe de CruzCampo", "Fisico", 15, 70),
    Movimiento("Pre-Jubilacion", "Especial", 20, 60)
]

"""Movimientos de Paco Pepe"""
movs_p2 = [
    Movimiento("Llamar al Primo", "Social", 10, 90),
    Movimiento("Navaja Mariposa", "Corte", 18, 75),
    Movimiento("Grito sin Proposito", "Sonoro", 8, 95),
    Movimiento("Patada en los Cocos", "Fisico", 25, 50)
]

print("¡COMIENZA EL COMBATE!")
print(f"{p1.nombre} vs {p2.nombre}\n")

"""Determinar orden por velocidad"""
if p1.velocidad >= p2.velocidad:
    atacante, movs_atq = p1, movs_p1
    defensor, movs_def = p2, movs_p2
else:
    atacante, movs_atq = p2, movs_p2
    defensor, movs_def = p1, movs_p1

print(f"{atacante.nombre} es más rápido.")

"""Bucle de combate"""
turno = 1
combate_activo = True

while combate_activo:
    print(f"\n--- TURNO {turno} ---")

    """Ataque del primer Pokémon"""
    m1 = random.choice(movs_atq)
    atacante.ejecutar_movimiento(m1, defensor)

    if defensor.vida <= 0:
        combate_activo = False
    else:
        """Ataque del segundo Pokémon"""
        m2 = random.choice(movs_def)
        defensor.ejecutar_movimiento(m2, atacante)
        
        if atacante.vida <= 0:
            combate_activo = False
    
    turno += 1

print("\n--- FIN DEL COMBATE ---")

"""Resultado final"""
if p1.vida <= 0:
    print(f"{p1.nombre} ha sido derrotado. ¡{p2.nombre} gana!")
else:
    print(f"{p2.nombre} ha sido derrotado. ¡{p1.nombre} gana!")