import time
import random
from datos_combate import *

p1 = ALEISTER
p2 = SEIGEN

"""Asignar movimientos según velocidad"""
if p1.velocidad >= p2.velocidad:
    atacante, movs_atq = p1, MOVS_ALEISTER
    defensor, movs_def = p2, MOVS_SEIGEN
else:
    atacante, movs_atq = p2, MOVS_SEIGEN
    defensor, movs_def = p1, MOVS_ALEISTER

print("¡COMIENZA EL COMBATE!")
print(f"{p1.nombre} ({p1.tipo}) vs {p2.nombre} ({p2.tipo})\n")
time.sleep(1)

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