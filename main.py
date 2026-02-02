import time
import random
from pokemon import Pokemon
from movimiento import Movimiento

"""Definición de Movimientos (El tipo debe ser IGUAL al del Pokémon)"""

"""Movimientos para Jose Luis (Tipo: Cuñao)"""
movs_cuñao = [
    Movimiento("Cerveza Fria", "Cuñao", 5, 100),
    Movimiento("Machismo", "Cuñao", 12, 80),
    Movimiento("Ajustar Huevo Ajeno", "Cuñao", 15, 70),
    Movimiento("Pre-Jubilacion", "Cuñao", 20, 60)
]

"""Movimientos para Paco Pepe (Tipo: Gitano)"""
movs_gitano = [
    Movimiento("Llamar al Primo", "Gitano", 10, 90),
    Movimiento("Navaja Mariposa", "Gitano", 18, 75),
    Movimiento("Grito sin Proposito", "Gitano", 8, 95),
    Movimiento("Patada en Huevillos", "Gitano", 25, 50)
]

"""Creación de los contrincantes"""
p1 = Pokemon("Jose Luis", "Cuñao", 20)
p2 = Pokemon("Paco Pepe", "Gitano", 20)

print("¡COMIENZA EL COMBATE!")
print(f"{p1.nombre} ({p1.tipo}) vs {p2.nombre} ({p2.tipo})\n")
time.sleep(1)

"""Determinar quién empieza por velocidad"""
if p1.velocidad >= p2.velocidad:
    atacante, movs_atq = p1, movs_cuñao
    defensor, movs_def = p2, movs_gitano
else:
    atacante, movs_atq = p2, movs_gitano
    defensor, movs_def = p1, movs_cuñao

print(f"{atacante.nombre} ataca primero por su velocidad ({atacante.velocidad})\n")

"""Bucle de combate"""
turno = 1
combate_activo = True

while combate_activo:
    print(f"--- TURNO {turno} ---")
    
    """Ataque del primer Pokémon"""
    m_actual = random.choice(movs_atq)
    atacante.ejecutar_movimiento(m_actual, defensor)
    time.sleep(1.5)

    if defensor.vida <= 0:
        combate_activo = False
    else:
        """Ataque del segundo Pokémon (si el primero no lo ha debilitado)"""
        m_actual_def = random.choice(movs_def)
        defensor.ejecutar_movimiento(m_actual_def, atacante)
        time.sleep(1.5)
        
        if atacante.vida <= 0:
            combate_activo = False
    
    turno += 1

"""Resultado final"""
print("\n" + "="*20)
print(" FIN DEL COMBATE ")
print("="*20)

if p1.vida <= 0:
    print(f"{p1.nombre} ha sido derrotado. ¡{p2.nombre} gana!")
else:
    print(f"{p2.nombre} ha sido derrotado. ¡{p1.nombre} gana!")