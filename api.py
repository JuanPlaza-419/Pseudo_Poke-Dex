import json
import os
from fastapi import FastAPI, HTTPException
from pokemon import Pokemon
from movimiento import * 

app = FastAPI()
DB_PATH = "pokedex.json"

def cargar_datos():
    if not os.path.exists(DB_PATH):
        return {}
    with open(DB_PATH, "r") as f:
        return json.load(f)

def guardar_datos(datos):
    with open(DB_PATH, "w") as f:
        json.dump(datos, f, indent=4)

MOVIMIENTOS_DISPONIBLES = {
    "lanzallamas": LANZALLAMAS, 
    "hidropulso": HIDROPULSO,
    "hoja afilada": HOJA_AFILADA, 
    "garra metal": GARRA_METAL
}

@app.get("/pokemon")
def listar():
    return cargar_datos()

@app.post("/pokemon/crear")
def crear(id: int, nombre: str, nivel: int, vida: int, fuerza: int, defensa: int, velocidad: int, tipos: str):
    datos = cargar_datos()
    if str(id) in datos:
        raise HTTPException(status_code=400, detail="ID ya ocupado")
    
    nuevo_p = Pokemon(id, nombre, nivel, vida, fuerza, defensa, velocidad)
    nuevo_p.definir_tipos(tipos.split(","))
    
    datos[str(id)] = nuevo_p.datos_a_JSON()
    guardar_datos(datos)
    return {"mensaje": "Guardado en JSON", "pokemon": nombre}

@app.post("/pokemon/añadir-movimiento")
def añadir_movimiento(id_pokemon: int, nombre_mov: str):
    datos = cargar_datos()
    id_str = str(id_pokemon)
    
    if id_str not in datos:
        raise HTTPException(status_code=404, detail="Pokemon no encontrado")
    
    mov_key = nombre_mov.lower()
    if mov_key not in MOVIMIENTOS_DISPONIBLES:
        raise HTTPException(status_code=404, detail="El movimiento no existe en movimiento.py")
    
    mov_obj = MOVIMIENTOS_DISPONIBLES[mov_key]
    if mov_obj.tipo not in datos[id_str]["tipos"]:
         raise HTTPException(status_code=400, detail="Tipo de movimiento incompatible")

    if len(datos[id_str]["movimientos"]) >= 4:
        raise HTTPException(status_code=400, detail="Ya tiene 4 movimientos")

    datos[id_str]["movimientos"].append(mov_obj.nombre)
    guardar_datos(datos)
    return {"mensaje": f"{mov_obj.nombre} aprendido por {datos[id_str]['nombre']}"}

@app.delete("/pokemon/eliminar/{id}")
def eliminar(id: int):
    datos = cargar_datos()
    if str(id) in datos:
        del datos[str(id)]
        guardar_datos(datos)
        return {"mensaje": "Eliminado del JSON"}
    raise HTTPException(status_code=404, detail="No existe")