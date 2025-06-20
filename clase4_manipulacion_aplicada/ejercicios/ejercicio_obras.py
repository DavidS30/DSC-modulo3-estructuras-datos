import json
from functools import reduce

with open("data_obras.json", "r") as archivo:
    obras_arte_crudo = json.load(archivo)


# Validación y limpieza

es_artista_valido = lambda obra: isinstance(obra.get("artista"), str) and len(obra.get("artista").strip()) > 0
es_precio_valido = lambda obra: isinstance(obra.get("precio_estimado"), (int, float)) and obra.get("precio_estimado") > 0
es_ano_valido = lambda obra: isinstance(obra.get("anio_creacion"), int) and (obra.get("anio_creacion") >= 2000 and obra.get("anio_creacion") <= 2025)
tiene_tags = lambda obra: isinstance(obra.get("tags"), list) and  len(obra['tags']) > 0
es_titulo_valido = lambda obra: isinstance(obra.get("titulo"), str) and len(obra["titulo"].strip()) > 0

limpiar_titulo = lambda titulo: titulo.strip() if isinstance(titulo, str) else ""

# filtración de obras
obras_validas = list(filter(
    lambda obra: es_artista_valido(obra) and es_precio_valido(obra) and es_ano_valido(obra)
                 and tiene_tags(obra) and es_titulo_valido(obra),
                 obras_arte_crudo
))

print("\n===* Obras validas despues de filtrar *===")

obras_para_exposicion = list(map(
    lambda obra: {
        "ID": obra["id"],
        "Titulo Limpio": limpiar_titulo(obra["titulo"]),
        "Artista": obra["artista"],
        "Año": obra["anio_creacion"],
        "Precio estimado": f"${obra["precio_estimado"]:.2f}"
    },
    obras_validas
))

for obra in obras_para_exposicion:
    print(obra)

# Analisis de obras
valor_total = reduce(lambda acumulado, obra: acumulado + obra["precio_estimado"], obras_validas,0)
print(f"\n El valor total estimado de la colección validada es: ${valor_total:.2f}")