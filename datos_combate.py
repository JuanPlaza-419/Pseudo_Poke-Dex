from movimiento import Movimiento
from pokemon import Mago, Espadachin 

"""Definición de los Combatientes Activos usando Herencia"""
ALEISTER = Mago("Aleister Crowley", 20)
SEIGEN = Espadachin("Toda Seigen", 20)

"""Listas de movimientos exclusivos"""

MOVS_ALEISTER = [
    Movimiento("Abramelin", "mago", 15, 90),
    Movimiento("Estrella de Plata", "mago", 12, 100),
    Movimiento("Telema", "mago", 20, 70),
    Movimiento("Ritual Menor", "mago", 10, 95)
]

MOVS_SEIGEN = [
    Movimiento("Kodachi Iai", "espadachín", 15, 95),
    Movimiento("Corte de Grulla", "espadachín", 12, 100),
    Movimiento("Tajo Cruzado", "espadachín", 18, 80),
    Movimiento("Estilo Chujo-ryu", "espadachín", 22, 60)
]

"""Gestión de aprendizaje"""

nuevo_mov_seigen = Movimiento("Corte de Luna", "espadachín", 25, 75)
MOVS_SEIGEN = SEIGEN.aprender_movimiento(MOVS_SEIGEN, nuevo_mov_seigen)

nuevo_mov_aleister = Movimiento("Clave Mayor", "mago", 30, 50)
MOVS_ALEISTER = ALEISTER.aprender_movimiento(MOVS_ALEISTER, nuevo_mov_aleister)