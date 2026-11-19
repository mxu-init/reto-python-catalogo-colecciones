# Catálogo de Piezas Coleccionables (Collectible Pieces Catalog System)

Programa de consola en Python para gestionar, consultar, filtrar, validar y analizar un catálogo de piezas coleccionables.

> **Nivel II:** el código del nivel I (un único flujo de ejecución) se ha refactorizado en **funciones con parámetros y `return`**, con **manejo de errores (`try` / `except`)**, **lanzamiento de excepciones (`raise`)**, **validaciones tempranas** y **organización en módulos**.

---

## Objetivo del programa

Construir un programa por consola que permita gestionar un catálogo básico de piezas coleccionables:
1. Registrar piezas con sus atributos (`id`, `name`, `category`, `price`, `status`, `description`).
2. Consultar el catálogo: listar, buscar por identificador (u otro campo) y eliminar piezas.
3. Aplicar filtros por estado y por precio mínimo.
4. Calcular métricas: precio promedio, piezas por categoría y por estado.
5. Validar los datos introducidos por el usuario, mostrando mensajes de error claros.

---

## Contexto del catálogo

El catálogo modela un entorno de compra, venta y tasación de artículos coleccionables (figuras de acción, cartas coleccionables, monedas antiguas, cómics, etc.).

Cada pieza es un diccionario con esta forma:

```python
{
    "id": "P001",
    "name": "Dragon Figure",
    "category": "Figuras",
    "price": 25.5,
    "status": "disponible",
    "description": "Figura usada en buen estado"
}
```

| Campo | Tipo de dato | Descripción |
|---|---|---|
| `id` | Texto (`str`) | Identificador único de la pieza |
| `name` | Texto (`str`) | Nombre de la pieza |
| `category` | Texto (`str`) | Categoría a la que pertenece |
| `price` | Número decimal (`float`) | Precio, numérico y mayor que cero |
| `status` | Texto (`str`) | Estado actual: `disponible`, `reservada` o `vendida` |
| `description` | Texto (`str`) | Debe contener obligatoriamente `usada` o `certificada` |

### Reglas de negocio
- **Estados permitidos:** `disponible`, `reservada`, `vendida`.
- **Descripción:** debe incluir obligatoriamente el término `usada` o `certificada`.
- **Identificador:** no puede repetirse dentro del catálogo.
- **Regla de publicación:** una pieza es publicable si su precio es mayor que 0 y su estado es `disponible`.
- **Regla de revisión:** requiere revisión si su estado es `reservada` o `vendida`.

---

## Estructura del proyecto

```
Python-Colecciones/
├── catalog.py        -> Funciones del catálogo (agregar, listar, buscar, quitar, filtrar, métricas)
├── validations.py    -> Funciones de validación de los datos de una pieza
├── main.py           -> Programa principal: menú y flujo de ejecución
└── README.md
```

- `main.py` importa las funciones de `catalog.py` y `validations.py`.
- `catalog.py` importa las validaciones de `validations.py`, de modo que la lógica de validación no se repite en ningún otro archivo.

---

## Funcionalidades implementadas

### `catalog.py`
| Parte | Función | Descripción |
|---|---|---|
| 1 | `add_piece(piece_id, name, category, price, status, description)` | Valida los datos y retorna el diccionario de la pieza. Lanza `ValueError` si algún dato no es válido. |
| 2 | `list_pieces(catalog)` | Retorna la lista de nombres de las piezas. |
| 3 | `find_piece_by_id(catalog, piece_id)` | Retorna la pieza con ese id, o `None` si no existe. |
| 3 | `find_pieces_by_field(catalog, field, value)` | Búsqueda por cualquier otro campo (`name`, `category`...). |
| 4 | `remove_piece(catalog, piece_id)` | Elimina la pieza. Retorna `True` si se eliminó o `False` si no se encontró. |
| 5 | `get_catalog_summary(catalog)` | Retorna un diccionario con la cantidad de piezas por categoría. |
| 6 | `get_pieces_by_category(catalog, category)` | Retorna los nombres de las piezas de una categoría. |
| 7 | `piece_exists(catalog, piece_id)` | Retorna `True` o `False` según exista la pieza. |
| 8 | `filter_by_status(catalog, status)` | Retorna las piezas con ese estado. Lanza `ValueError` si el estado no es válido. |
| 9 | `filter_by_min_price(catalog, min_price)` | Retorna las piezas con precio mayor al indicado. Lanza `ValueError` si no es numérico. |
| 10 | `get_average_price(catalog)` | Retorna el precio promedio, o `0` si el catálogo está vacío. |

Todas las funciones que reciben el catálogo comprueban primero que sea una lista (`validate_catalog`) y, si no lo es, lanzan `TypeError`.

Además se conservan como funciones las funcionalidades del nivel I: `get_unique_categories` (set de categorías), `get_catalog_metrics` (conteo por estado, suma y promedio), `can_be_published`, `needs_review` y `get_unsold_pieces` (reglas con operadores lógicos).

### `validations.py` (Parte 11)
- `validate_not_empty(value, field_name)`: el valor no puede estar vacío.
- `validate_price(price)`: el precio debe ser numérico y mayor que cero.
- `validate_status(status)`: el estado debe estar entre los permitidos.
- `validate_description(description)`: la descripción debe contener `usada` o `certificada`.

Cada función lanza `ValueError` con un mensaje claro y no imprime nada: mostrar el error es responsabilidad de quien la llama.

### `main.py` (Parte 12)
Al iniciar, el programa da la bienvenida y permite registrar varias piezas. Después muestra un menú que se repite hasta que el usuario elige salir. Cada opción llama a una función, y los errores se capturan y se muestran con un mensaje claro.

1. Agregar una pieza
2. Mostrar todas las piezas
3. Mostrar piezas disponibles
4. Mostrar el precio promedio
5. Buscar una pieza (por identificador u otro campo)
6. Eliminar una pieza
7. Salir

Opciones adicionales (funcionalidades del nivel I):

8. Categorías y resumen por categoría
9. Filtrar piezas por estado
10. Filtrar piezas por precio mínimo
11. Reglas de publicación y revisión
12. Métricas del catálogo
13. Manipulación de strings

Al introducir los datos de una pieza, cada campo se valida en el momento: si un dato no es válido, se muestra el motivo y se vuelve a pedir solo ese campo.

---

## Ejemplo de interacción con el programa

```text
¡Bienvenido!
Estás ingresando al catálogo de piezas coleccionables
¿Cuántas piezas deseas añadir? 1

Introduce los datos para la pieza número 1:
Introduce el identificador de la pieza: P001
Introduce el nombre de la pieza: Dragon Figure
Introduce la categoría de la pieza: Figuras
Introduce el precio de la pieza: -5
Error de validación: El precio debe ser mayor que cero.
Introduce el precio de la pieza: 25.5
Introduce el estado (disponible, reservada, vendida): nueva
Error de validación: El estado debe ser 'disponible', 'reservada' o 'vendida'.
Introduce el estado (disponible, reservada, vendida): disponible
Introduce la descripción (debe contener obligatoriamente 'usada' o 'certificada'): Figura usada en buen estado

Catálogo registrado:
[{'id': 'P001', 'name': 'Dragon Figure', 'category': 'Figuras', 'price': 25.5, 'status': 'disponible', 'description': 'Figura usada en buen estado'}]

=== Menú Interactivo ===
1. Agregar una pieza
2. Mostrar todas las piezas
3. Mostrar piezas disponibles
4. Mostrar el precio promedio
5. Buscar una pieza (por identificador u otro campo)
6. Eliminar una pieza
7. Salir
--- Opciones adicionales ---
...
Selecciona una opción (1-13): 5

--- Búsqueda de pieza por campo y valor ---
¿Por qué campo deseas buscar? (id, name, category, price, status, description): id
Introduce el valor de 'id' que deseas encontrar: P001
Se encontraron 1 pieza(s):
{'id': 'P001', 'name': 'Dragon Figure', 'category': 'Figuras', 'price': 25.5, 'status': 'disponible', 'description': 'Figura usada en buen estado'}

Selecciona una opción (1-13): 6

--- Eliminar una pieza ---
Introduce el identificador de la pieza que deseas eliminar: P999
No se encontró ninguna pieza con id 'P999'. No se eliminó nada.

Selecciona una opción (1-13): 4

--- Precio promedio ---
Precio promedio del catálogo: 25.50

Selecciona una opción (1-13): 7
Saliendo del catálogo. ¡Hasta pronto!

Programa finalizado con éxito.
```

---

## Tecnologías utilizadas

- **Python 3:** lenguaje y entorno de ejecución.
- **Módulos propios:** `catalog.py`, `validations.py` y `main.py`, conectados con `import`.
- **Funciones:** definición con parámetros, `return` y docstrings.
- **Manejo de errores:** `try` / `except`, `raise` y las excepciones `ValueError`, `TypeError` y `LookupError`.
- **Estructuras de datos nativas:** `list` (catálogo y resultados), `dict` (piezas, resumen y métricas) y `set` (categorías únicas).
- **Control de flujo:** bucles `for` y `while` y condicionales `if` / `elif` / `else`.
- **Métodos de `str` y conversión de tipos:** `int()`, `float()`, `str()`, `.strip()`, `.split()`, `.replace()`, `.lower()`, `.upper()`, `.title()`, `enumerate()` e `isinstance()`.

---

## Cómo ejecutar el programa

### 1. Requisitos previos
Tener instalado Python 3.8 o superior. Puedes comprobarlo con:

```bash
python --version
```

### 2. Ubicarse en el directorio del proyecto

```bash
cd "ruta/hacia/Python-Colecciones"
```

### 3. Ejecutar el programa principal

```bash
python main.py
```

Sigue las instrucciones de la terminal para registrar piezas y usar el menú. Para salir, elige la opción `7`.
