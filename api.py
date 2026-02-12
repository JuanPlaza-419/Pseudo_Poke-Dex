from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import json
import os

from pokemon import Fuego, Agua, Planta, Volador, Acero, Pokemon
from movimiento import LANZALLAMAS, HIDROPULSO, HOJA_AFILADA, GARRA_METAL

app = FastAPI()
DB_PATH = "pokedex.json"

class PokemonSchema(BaseModel):
    id: int
    nombre: str
    nivel: int
    vida: int
    fuerza: int
    defensa: int
    velocidad: int
    tipos: List[str] # Ejemplo: ["fuego", "agua"]

class MovimientoRequest(BaseModel):
    id_pokemon: int
    nombre_movimiento: str

def cargar_json():
    if not os.path.exists(DB_PATH): return {}
    with open(DB_PATH, "r") as f: return json.load(f)

def guardar_json(datos):
    with open(DB_PATH, "w") as f: json.dump(datos, f, indent=4)

MOV_DB = {
    "lanzallamas": LANZALLAMAS,
    "hidropulso": HIDROPULSO,
    "hoja afilada": HOJA_AFILADA,
    "garra metal": GARRA_METAL
}

@app.post("/pokemon/crear")
def crear_pokemon(data: PokemonSchema):
    pokedex = cargar_json()
    if str(data.id) in pokedex:
        raise HTTPException(status_code=400, detail="El ID ya existe")
    
    pokedex[str(data.id)] = data.dict()
    pokedex[str(data.id)]["movimientos"] = []
    
    guardar_json(pokedex)
    return {"mensaje": f"Pokemon {data.nombre} guardado correctamente"}

@app.post("/pokemon/añadir-movimiento")
def añadir_movimiento(req: MovimientoRequest):
    pokedex = cargar_json()
    id_s = str(req.id_pokemon)
    
    if id_s not in pokedex:
        raise HTTPException(status_code=404, detail="Pokemon no encontrado")
    
    mov_nombre = req.nombre_movimiento.lower()
    if mov_nombre not in MOV_DB:
        raise HTTPException(status_code=404, detail="Movimiento no existe en el sistema")
    
    if len(pokedex[id_s]["movimientos"]) >= 4:
        raise HTTPException(status_code=400, detail="El Pokemon ya conoce 4 movimientos")
    
    pokedex[id_s]["movimientos"].append(MOV_DB[mov_nombre].nombre)
    
    guardar_json(pokedex)
    return {"mensaje": f"¡{pokedex[id_s]['nombre']} aprendió {mov_nombre}!"}