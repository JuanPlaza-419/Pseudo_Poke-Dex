import pytest
from pokemon import Pokemon
from movimiento import Movimiento

def test_validacion_tipos():
    """Crea un Pokémon tipo 'Cuñao'"""
    p = Pokemon("Jose", "Cuñao", 20)
    
    """Crea un movimiento de tipo 'Gitano' (Incorrecto)"""
    mov_malo = Movimiento("Navaja", "Gitano", 10, 100)

    """VERIFICACIÓN: "Espero que esto lance un ValueError""""
    with pytest.raises(ValueError):
        p.ejecutar_movimiento(mov_malo, p)

def test_funciona_bien():
    """Comprobar que si el tipo coincide, NO da error"""
    p = Pokemon("Paco", "Gitano", 20)
    mov_bueno = Movimiento("Patada", "Gitano", 10, 100)
    
    """Si esto NO da error, el test pasa"""
    p.ejecutar_movimiento(mov_bueno, p)