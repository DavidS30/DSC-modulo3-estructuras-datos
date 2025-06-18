# Ejercicio Práctico: Curador Digital de Arte 🎨

Este ejercicio te desafía a procesar un conjunto de datos JSON simulando una colección de obras de arte. Deberás aplicar los principios de la programación funcional en Python utilizando funciones lambda junto con map, filter, y reduce para lograr lo siguiente:

## Validación y Limpieza de Datos:

- Cargar el JSON en una estructura de Python.
- Filtrar obras que cumplan criterios específicos de validez (artista no vacío, precio positivo, año de creación numérico y dentro de un rango digital razonable, título no vacío y al menos un "tag").
- Limpiar y estandarizar datos como el título (eliminando espacios extra) y el año (asegurando que sea un número entero).

## Transformación para Presentación:

- Convertir las obras válidas en un formato simplificado para exhibición, incluyendo campos como "ID", "Título Limpio", "Artista", "Año", y "Precio Estimado" (este último formateado con símbolo de moneda).

## Análisis de Colección:

- Calcular el valor total estimado de toda la colección de obras válidas.
- Identificar el año de creación más reciente entre las obras.
- Contar el número de obras de un artista específico y de aquellas que tienen un "tag" particular.
