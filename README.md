# Catálogo de Piezas Coleccionables (Collectible Pieces Catalog System)

Programa de consola en Python para gestionar, consultar, filtrar, validar y analizar un catálogo de piezas coleccionables.

---

## Objetivo del programa

El objetivo principal de esta aplicación es proporcionar una herramienta interactiva por terminal que permita:
1. Registrar piezas coleccionables con sus atributos clave (`id`, `name`, `category`, `price`, `status`, `description`).
2. Almacenar la información en colecciones nativas (`list`, `dict`, `set`) para su consulta y recorrido.
3. Aplicar filtros dinámicos por estado y rango de precio.
4. Evaluar reglas de negocio mediante operadores lógicos y relacionales.
5. Transformar y normalizar texto mediante métodos de manipulación de cadenas.
6. Presentar métricas consolidadas del catálogo y un menú interactivo con validaciones de entrada robustas.

---

## Contexto del catálogo

El catálogo modela un entorno de compra, venta y tasación de artículos coleccionables (como figuras de acción, cartas coleccionables, monedas antiguas, cómics, etc.). 

Cada artículo del catálogo contiene los siguientes campos:

| Campo | Tipo de dato | Descripción |
|---|---|---|
| `id` | Texto (`str`) | Identificador único de la pieza |
| `name` | Texto (`str`) | Nombre de la pieza |
| `category` | Texto (`str`) | Categoría a la que pertenece |
| `price` | Número decimal (`float`) | Precio de venta o valor de referencia |
| `status` | Texto (`str`) | Estado actual: `disponible`, `reservada` o `vendida` |
| `description` | Texto (`str`) | Descripción obligatoria con `usada` o `certificada` |

### Reglas de negocio:
- **Estados permitidos:**
  - `disponible`: La pieza puede venderse o intercambiarse.
  - `reservada`: Apartada temporalmente para un comprador.
  - `vendida`: Ya fue adquirida y no está disponible.
- **Descripción:** Debe incluir obligatoriamente el término `usada` o `certificada`.
- **Regla de publicación:** Una pieza solo es publicable si su precio es mayor que 0 y su estado es `disponible`.
- **Regla de revisión:** Requiere revisión si su estado es `reservada` o `vendida`.

---

## Funcionalidades implementadas

El proyecto cubre todos los niveles y partes especificados en la guía técnica:

### Nivel 1 – Registro de piezas y estructuras base
- **Parte 1 (Preparación del proyecto):** Definición del nombre del sistema y despliegue del mensaje de bienvenida al catálogo.
- **Parte 2 (Captura de piezas por terminal):** Captura dinámica de piezas utilizando la estructura de la Opción A (recorrido de claves, construcción de diccionarios y almacenamiento en la lista principal `catalog`).
- **Parte 3 (Almacenamiento de la información):** Búsqueda dinámica y consulta individual de piezas filtrando por cualquier campo (`id`, `name`, `category`, `price`, `status`, `description`).
- **Parte 4 (Información adicional del catálogo):** Creación y cálculo de un `set` con las categorías únicas para eliminar duplicados y conocer la cantidad de categorías distintas.
- **Parte 5 (Mostrar el catálogo):** Recorrido completo imprimiendo el detalle de cada pieza, el total de piezas y las categorías únicas.

### Nivel 2 – Filtros, operadores y strings
- **Parte 6 (Filtrar piezas por estado):** Visualización segmentada para piezas `disponible`, `reservada` y `vendida` con control de resultados vacíos.
- **Parte 7 (Filtrar piezas por precio):** Filtrado por precio mínimo con validación numérica interactiva.
- **Parte 8 (Aplicar operadores lógicos):** Evaluación de condiciones booleanas compuestas (`and`, `or`, `not`) para publicación, revisión y piezas no vendidas.
- **Parte 9 (Manipulación de strings):** Demostración de concatenación (`+`), interpolación con f-strings, reemplazo con `.replace()`, división de etiquetas con `.split()`, limpieza con `.strip()` y conversiones de caso (`.lower()`, `.upper()`, `.title()`).

### Nivel 3 (Opcional) – Bucles, menú y métricas
- **Parte 10 (Crear un menú interactivo):** Menú en bucle `while` con opciones para listar todas las piezas, listar disponibles, consultar precio promedio y salir, gestionando opciones inválidas.
- **Parte 11 (Calcular métricas del catálogo):** Cálculo de totales acumulados, conteo por cada estado, precio promedio general y listado enumerado de piezas (`1. Nombre`).
- **Parte 12 (Validaciones básicas):** Validación estricta paso a paso (precio numérico > 0, nombre no vacío, estado permitido, descripción con palabra clave requerida) impidiendo el avance con datos incorrectos y re-solicitando la entrada.

---

## Ejemplo de interacción con el programa

```text
========================================
¡Bienvenido al Catálogo de Piezas Coleccionables!
Estás ingresando al catálogo de piezas coleccionables.
========================================

¿Cuántas piezas deseas añadir? 2

Introduce los datos para la pieza número 1:
Introduce el valor para id: P001
Introduce el valor para name: Dragon Figure
Introduce el valor para category: Figures
Introduce el valor para price: 25.5
Introduce el valor para status: disponible
Introduce el valor para description: Figura usada en buen estado

Introduce los datos para la pieza número 2:
Introduce el valor para id: P002
Introduce el valor para name: Silver Coin
Introduce el valor para category: Coins
Introduce el valor para price: 120.0
Introduce el valor para status: reservada
Introduce el valor para description: Moneda certificada por experto

--- Búsqueda de pieza por campo y valor ---
¿Por qué campo deseas buscar? (id, name, category, price, status, description): id
Introduce el valor de 'id' que deseas encontrar: P001
Se encontraron 1 pieza(s):
{'id': 'P001', 'name': 'Dragon Figure', 'category': 'Figures', 'price': 25.5, 'status': 'disponible', 'description': 'Figura usada en buen estado'}

=== Menú Interactivo ===
1. Mostrar todas las piezas
2. Mostrar solo las piezas disponibles
3. Mostrar el precio promedio
4. Salir
Selecciona una opción (1-4): 2

--- Piezas disponibles ---
ID: P001 | Nombre: Dragon Figure | Precio: 25.5 | Estado: disponible

=== Métricas del Catálogo ===
1. Cantidad de piezas disponibles: 1
2. Cantidad de piezas reservadas: 1
3. Cantidad de piezas vendidas: 0
4. Cantidad total de piezas: 2
5. Suma total de los precios: 145.50
6. Precio promedio del catálogo: 72.75

--- Piezas enumeradas ---
1. Dragon Figure
2. Silver Coin
```

---

## Tecnologías utilizadas

- **Python 3:** Entorno de ejecución y sintaxis moderna.
- **Estructuras de datos nativas:**
  - `list`: Colección ordenada para el catálogo de piezas (`catalog`) y resultados de búsqueda.
  - `dict`: Mapeo clave-valor para representar cada pieza con sus atributos.
  - `set`: Conjunto para el almacenamiento de categorías únicas sin duplicados.
- **Control de flujo:** Bucles `for` y `while`, condicionales `if`, `elif`, `else`.
- **Métodos nativos de `str` y conversión de tipos:** `int()`, `float()`, `str()`, `.strip()`, `.split()`, `.replace()`, `.lower()`, `.upper()`, `.title()`, `enumerate()`.

---

## Cómo ejecutar el programa

### 1. Requisitos previos
Tener instalado Python 3.8 o superior en el sistema. Puedes comprobarlo ejecutando:

```bash
python --version
```

### 2. Ubicarse en el directorio del proyecto
Abre una terminal o consola y dirígete a la carpeta raíz del proyecto:

```bash
cd "ruta/hacia/Python-Colecciones-ref"
```

### 3. Ejecutar el script principal
Ejecuta el archivo `main.py`:

```bash
python main.py
```

Sigue las instrucciones que aparecerán en la terminal para ingresar piezas, realizar búsquedas, interactuar con el menú y visualizar las métricas del catálogo.
