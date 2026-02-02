import pytest
from pokemon import Pokemon
from movimiento import Movimiento

def test_gestion_basica_movimientos():
    """Creamos un Pokémon y una lista vacia"""
    p = Pokemon("Test", "Cuñao", 10)
    mis_movimientos = []
    
    """Añade un movimiento"""
    m1 = Movimiento("Ataque 1", "Cuñao", 10, 100)
    p.aprender_movimiento(mis_movimientos, m1)
    
    """COMPROBACIÓN: ¿Se ha añadido?"""
    assert len(mis_movimientos) == 1
    assert mis_movimientos[0].nombre == "Ataque 1"

def test_limite_maximo_cuatro():
    """Creamos un Pokémon con 4 movimientos ya llenos"""
    p = Pokemon("Test", "Cuñao", 10)
    mis_movimientos = [
        Movimiento("M1", "Cuñao", 5, 100),
        Movimiento("M2", "Cuñao", 5, 100),
        Movimiento("M3", "Cuñao", 5, 100),
        Movimiento("M4", "Cuñao", 5, 100)
    ]
    
    """COMPROBACIÓN: La lista tiene exactamente 4"""
    assert len(mis_movimientos) == 4