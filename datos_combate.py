from movimiento import Movimiento
from pokemon import Pokemon

"""Definición de los Pokémon base"""
JOSE_LUIS = Pokemon("Jose Luis", "Cuñao", 20)
PACO_PEPE = Pokemon("Paco Pepe", "Gitano", 20)

"""Listas de movimientos (4 movimientos cada uno)"""
MOVS_CUNAO = [
    Movimiento("Cerveza Fria", "Cuñao", 5, 100),
    Movimiento("Machismo", "Cuñao", 12, 80),
    Movimiento("Ajustar Huevo", "Cuñao", 15, 70),
    Movimiento("Pre-Jubilacion", "Cuñao", 20, 60)
]

MOVS_GITANO = [
    Movimiento("Llamar al Primo", "Gitano", 10, 90),
    Movimiento("Navaja Mariposa", "Gitano", 18, 75),
    Movimiento("Grito Sordo", "Gitano", 8, 95),
    Movimiento("Patada Huevillos", "Gitano", 25, 50)
]

"""Un 5º movimiento que pide sustitucion"""
nuevo_mov = Movimiento("Venta de Cobre", "Gitano", 30, 40)
MOVS_GITANO = PACO_PEPE.aprender_movimiento(MOVS_GITANO, nuevo_mov)

nuevo_mov = Movimiento("Dia de Pago", "Cuñao", 30, 40)
MOVS_CUNAO = JOSE_LUIS.aprender_movimiento(MOVS_CUNAO, nuevo_mov)