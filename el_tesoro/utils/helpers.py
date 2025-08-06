import json

def cargar_json(ruta):
    with open(ruta, 'r', encoding='utf-8') as f:
        return json.load(f)

def cargar_txt(ruta):
    with open(ruta, 'r', encoding='utf-8') as f:
        return f.readlines()
