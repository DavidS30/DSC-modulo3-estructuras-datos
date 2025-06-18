# 📚 Ejercicio: Esquema de datos para una Biblioteca usando Sets

---

## 📝 Descripción

Este ejercicio propone construir un esquema de datos para una biblioteca utilizando conjuntos (`set`) y sus métodos en Python. El objetivo es modelar la información de **libros**, **autores**, **usuarios** y **préstamos**, y aprovechar las operaciones de conjuntos para analizar y comparar los datos de manera eficiente.

---

## 🚀 Funcionalidades Principales

- **Registro interactivo de libros y autores**
  - Permite ingresar libros y sus autores mediante la consola.
- **Registro de usuarios**
  - Permite ingresar usuarios de la biblioteca.
- **Registro de préstamos**
  - Permite registrar préstamos de libros a usuarios, validando que tanto el libro como el usuario existan.
- **Visualización de datos**
  - Muestra los libros, autores, usuarios y préstamos registrados.
- **Operaciones con sets**
  - Libros prestados y no prestados.
  - Usuarios con y sin préstamos.
  - Comparaciones usando `issubset`, `issuperset` y `isdisjoint` para analizar relaciones entre los conjuntos.

---

## 🧩 Ejemplo de Uso de Métodos de Sets

- `issubset`: Verifica si todos los libros prestados pertenecen a la biblioteca.
- `issuperset`: Verifica si la biblioteca contiene todos los libros prestados.
- `isdisjoint`: Verifica si hay usuarios que también sean autores.

---

## ▶️ ¿Cómo Ejecutar el Script?

1. Abre una terminal en la carpeta del ejercicio.
2. Ejecuta el siguiente comando:

```bash
python ejercicio_biblioteca_sets.py
```

3. Sigue las instrucciones para ingresar los datos. Escribe `fin` cuando quieras terminar cada sección de ingreso.
