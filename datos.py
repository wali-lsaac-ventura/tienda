import json, os
ARCHIVO = "productos.json"

def cargar():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO) as f:
            return json.load(f)
    return {"1": ["Arroz", 50], "2": ["Habichuela", 80]}

def guardar(p):
    with open(ARCHIVO, "w") as f:
        json.dump(p, f)
