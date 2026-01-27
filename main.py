from pokemon import Pokemon

p1 = Pokemon("Jose Luis", "Cuñao", 20)
p2 = Pokemon("Paco Pepe", "Gitano", 20)

print("¡COMIENZA EL COMBATE!")
print(f"{p1.nombre} (Vida: {p1.vida}, Fuerza: {p1.fuerza}) vs {p2.nombre} (Vida: {p2.vida}, Fuerza: {p2.fuerza})\n")

if p1.velocidad >= p2.velocidad:
    atacante, defensor = p1, p2
else:
    atacante, defensor = p2, p1

print(f"{atacante.nombre} ataca primero por ser más rápido.\n")

turno = 1
combate_activo = True

while combate_activo:
    print(f"\n--- TURNO {turno} ---")

    atacante.ejecutar_movimiento(defensor)

    if defensor.vida <= 0:
        combate_activo = False
    else:
        defensor.ejecutar_movimiento(atacante)

        if atacante.vida <= 0:
            combate_activo = False
    
    turno += 1

print("\n--- FIN DEL COMBATE ---")

if p1.vida <= 0:
    print(f"{p1.nombre} ha sido derrotado. ¡{p2.nombre} gana!")
else:
    print(f"{p2.nombre} ha sido derrotado. ¡{p1.nombre} gana!")