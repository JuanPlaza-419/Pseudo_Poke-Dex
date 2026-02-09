from fastapi import FastAPI
from datos_combate import ROMPE_AIRE, SOLDADO_TECNO, MOVS_AIRE, MOVS_TECNO

app = FastAPI()

@app.get("/estado")
def ver_estado():
    return {
        ROMPE_AIRE.nombre: {"vida": ROMPE_AIRE.vida, "tipo": ROMPE_AIRE.tipo},
        SOLDADO_TECNO.nombre: {"vida": SOLDADO_TECNO.vida, "tipo": SOLDADO_TECNO.tipo}
    }

@app.post("/atacar")
def atacar(nombre_atacante: str, nombre_movimiento: str):
    if nombre_atacante == ROMPE_AIRE.nombre:
        atacante, defensor, movs = ROMPE_AIRE, SOLDADO_TECNO, MOVS_AIRE
    else:
        atacante, defensor, movs = SOLDADO_TECNO, ROMPE_AIRE, MOVS_TECNO

    mov = next((m for m in movs if m.nombre.lower() == nombre_movimiento.lower()), None)
    
    if mov:
        return atacante.ejecutar_movimiento(mov, defensor)
    
    return {"error": "Movimiento no encontrado"}