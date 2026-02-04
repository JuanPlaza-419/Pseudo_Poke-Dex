from movimiento import Movimiento
from pokemon import Volador, Acero

"""Definición de los Combatientes Activos usando Herencia"""
ROMPE_AIRE = Volador("Rompe-Aire", 20)

SOLDADO_TECNO = Acero("Soldado del Tecno", 20)

"""Listas de movimientos exclusivos"""

MOVS_AIRE = [
    Movimiento("Tornado", "volador", 15, 95),
    Movimiento("Ala de Acero", "volador", 12, 100),
    Movimiento("Picotazo", "volador", 10, 100),
    Movimiento("Ataque Aéreo", "volador", 25, 60)
]

MOVS_TECNO = [
    Movimiento("Puño Bala", "acero", 12, 100),
    Movimiento("Garra Metal", "acero", 18, 90),
    Movimiento("Cuerpo Pesado", "acero", 22, 80),
    Movimiento("Cabeza Hierro", "acero", 20, 100)
]

"""Gestión de aprendizaje (5º movimiento)"""

nuevo_mov_aire = Movimiento("Vendaval", "volador", 30, 70)
MOVS_AIRE = ROMPE_AIRE.aprender_movimiento(MOVS_AIRE, nuevo_mov_aire)

nuevo_mov_tecno = Movimiento("Giga Impacto", "acero", 35, 50)
MOVS_TECNO = SOLDADO_TECNO.aprender_movimiento(MOVS_TECNO, nuevo_mov_tecno)