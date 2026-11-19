from validations import validate_not_empty, validate_price, validate_status, validate_description
from catalog import (add_piece, list_pieces, find_piece_by_id, find_pieces_by_field,
                     get_catalog_summary, get_unique_categories, get_pieces_by_category,
                     piece_exists, filter_by_status, filter_by_min_price,
                     get_average_price, get_catalog_metrics, ALLOWED_STATUSES)

# Nivel 1
# Parte 1: Preparación del proyecto

system_name = "catálogo de piezas coleccionables"
print("¡Bienvenido!")
print(f"Estás ingresando al {system_name}")

# Parte 2: Captura de piezas por terminal

#Test para cómo recoger/consultar datos diccionarios. Consultar una sola clave individual
#Ejemplo: solo consultar el nombre objeto 1, no todo el objeto
"""
cant = int(input("¿Cuántos items quieres añadir?"))
lista_de_items = []

for x in range (0, cant):
  nombre = input("Introduce el nombre del item:")
  categoria = input ("Introduce la categoría del item: ")

  item = {"nombre": nombre, "categoria": categoria}
  lista_de_items.append(item)

for x in lista_de_items:
  print(f"{x['nombre']} - {x['categoria']}")

numero_item = int(input("¿Qué item quieres consultar?"))
consulta= input("¿Qué quieres consultar?").strip().lower()

print(lista_de_items[numero_item][consulta])

"""

piece_prompts = {
    "id": "Introduce el identificador de la pieza: ",
    "name": "Introduce el nombre de la pieza: ",
    "category": "Introduce la categoría de la pieza: ",
    "price": "Introduce el precio de la pieza: ",
    "status": "Introduce el estado (disponible, reservada, vendida): ",
    "description": "Introduce la descripción (debe contener obligatoriamente 'usada' o 'certificada'): "
}


def validate_piece_field(catalog, key, value):
    """Valida un campo de la pieza usando las funciones de validations.py."""
    validate_not_empty(value, key)
    if key == "id" and piece_exists(catalog, value):
        raise ValueError("Ya existe una pieza con ese ID. Por favor, introduce uno diferente.")
    elif key == "price":
        validate_price(value)
    elif key == "status":
        validate_status(value)
    elif key == "description":
        validate_description(value)


def ask_piece_data(catalog):
    """Pide por terminal cada campo (repitiendo si no es válido) y retorna la pieza creada."""
    piece = {}
    for key, prompt in piece_prompts.items():
        while True:
            value = input(prompt).strip()
            try:
                validate_piece_field(catalog, key, value)
                piece[key] = value
                break
            except ValueError as error:
                print(f"Error de validación: {error}")
    return add_piece(piece["id"], piece["name"], piece["category"],
                     piece["price"], piece["status"], piece["description"])


catalog = []
quantity = int(input("¿Cuántas piezas deseas añadir? "))
for x in range(0, quantity):
    print(f"\nIntroduce los datos para la pieza número {x + 1}:")
    catalog.append(ask_piece_data(catalog))
print("\nCatálogo registrado:")
print(catalog)

# Parte 3: Almacenamiento de la información | Acceso a los valores de cada pieza

print("\n--- Búsqueda de pieza por campo y valor ---")
search_field = input("¿Por qué campo deseas buscar? (id, name, category, price, status, description): ").strip().lower()
search_value = input(f"Introduce el valor de '{search_field}' que deseas encontrar: ").strip()

if search_field == "id":
    found_piece = find_piece_by_id(catalog, search_value)
    found_pieces = [found_piece] if found_piece is not None else []
else:
    found_pieces = find_pieces_by_field(catalog, search_field, search_value)

if not found_pieces:
    print(f"No se encontró ninguna pieza con {search_field} = '{search_value}'.")
else:
    print(f"Se encontraron {len(found_pieces)} pieza(s):")
    for elem in found_pieces:
        print(elem)

# Parte 4: Información adicional del catálogo

categories = get_unique_categories(catalog)

print("\n--- Categorías Únicas ---")
print(f"Conjunto de categorías únicas: {categories}")
print(f"Cantidad de categorías diferentes: {len(categories)}")

print("\n--- Resumen: piezas por categoría ---")
for category, count in get_catalog_summary(catalog).items():
    print(f"{category}: {count} pieza(s) -> {get_pieces_by_category(catalog, category)}")

# Parte 5: Mostrar el catálogo

print("\n=== Catálogo Completo de Piezas ===")
for elem in catalog:
    print(f"Identificador: {elem['id']} | Nombre: {elem['name']} | Categoría: {elem['category']} | Precio: {elem['price']} | Estado: {elem['status']} | Descripción: {elem['description']}")

print(f"\nCantidad total de piezas: {len(catalog)}")
print(f"Categorías únicas: {categories}")
print(f"Cantidad de categorías diferentes: {len(categories)}")

# Nivel 2
# Parte 6: Filtrar piezas por estado

for target_status in ALLOWED_STATUSES:
    print(f"\n--- Piezas en estado '{target_status}' ---")
    status_pieces = filter_by_status(catalog, target_status)
    for elem in status_pieces:
        print(f"ID: {elem['id']} | Nombre: {elem['name']} | Categoría: {elem['category']} | Precio: {elem['price']} | Estado: {elem['status']}")
    if not status_pieces:
        print(f"No se encontraron piezas con el estado '{target_status}'.")

# Parte 7: Filtrar piezas por precio

min_price_input = input("\nIntroduce un precio mínimo para filtrar: ").strip()
while True:
    try:
        price_pieces = filter_by_min_price(catalog, min_price_input)
        break
    except ValueError as error:
        print(f"Precio no válido. {error}")
        min_price_input = input("Introduce un precio mínimo para filtrar: ").strip()

min_price = float(min_price_input)
print(f"\n--- Piezas con precio superior a {min_price} ---")
for elem in price_pieces:
    print(f"ID: {elem['id']} | Nombre: {elem['name']} | Precio: {elem['price']}")

if not price_pieces:
    print(f"No se encontraron piezas con precio superior a {min_price}.")

# Parte 8: Aplicar operadores lógicos

print("\n=== Regla de Publicación (Precio > 0 y Estado 'disponible') ===")
for elem in catalog:
    can_publish = float(elem["price"]) > 0 and elem["status"].lower() == "disponible"
    if can_publish:
        print(f"Pieza '{elem['name']}' (ID: {elem['id']}): Puede publicarse.")
    else:
        print(f"Pieza '{elem['name']}' (ID: {elem['id']}): NO puede publicarse.")

print("\n=== Regla de Revisión (Estado 'reservada' o 'vendida') ===")
for elem in catalog:
    needs_review = elem["status"].lower() == "reservada" or elem["status"].lower() == "vendida"
    if needs_review:
        print(f"Pieza '{elem['name']}' (ID: {elem['id']}): Requiere revisión.")
    else:
        print(f"Pieza '{elem['name']}' (ID: {elem['id']}): NO requiere revisión.")

print("\n=== Piezas No Vendidas (Estado diferente a 'vendida') ===")
unsold_found = False
for elem in catalog:
    if elem["status"].lower() != "vendida":
        print(f"ID: {elem['id']} | Nombre: {elem['name']} | Estado: {elem['status']} | Precio: {elem['price']}")
        unsold_found = True
if not unsold_found:
    print("No se encontraron piezas sin vender.")

# Parte 9: Manipulación de strings

print("\n=== Manipulación de Cadenas de Texto ===")
if len(catalog) > 0:
    first_piece = catalog[0]
    concatenation_output = "ID Pieza: " + str(first_piece["id"]) + " - Nombre: " + first_piece["name"] + " - Categoría: " + first_piece["category"] + " - Precio: " + str(first_piece["price"])
    print("Concatenación:\n" + concatenation_output)

    interpolation_output = f"ID Pieza: {first_piece['id']} - Nombre: {first_piece['name']} - Categoría: {first_piece['category']} - Precio: {first_piece['price']}"
    print(f"Interpolación:\n{interpolation_output}")

    modified_description = first_piece["description"].replace("usada", "certificada")
    print(f"Descripción original: {first_piece['description']}")
    print(f"Descripción con 'usada' reemplazada por 'certificada': {modified_description}")

    normalized_piece_name = first_piece["name"].strip().title()
    print(f"Nombre de la pieza normalizado: '{normalized_piece_name}'")

tags_string = input("\nIntroduce etiquetas separadas por comas (ej. retro,anime,limited): ")
separated_tags = tags_string.split(",")
clean_tags = [tag.strip() for tag in separated_tags]
print(f"Lista de etiquetas separadas: {clean_tags}")

terminal_username = input("\nIntroduce un nombre de usuario: ")
clean_username = terminal_username.strip()
print(f"Sin espacios al inicio o al final: '{clean_username}'")
print(f"En minúsculas: {clean_username.lower()}")
print(f"En mayúsculas: {clean_username.upper()}")
print(f"En formato título: {clean_username.title()}")

# Nivel 3 (Opcional)
# Parte 10: Crear un menú interactivo

menu_active = True
while menu_active:
    print("\n=== Menú Interactivo ===")
    print("1. Mostrar todas las piezas")
    print("2. Mostrar solo las piezas disponibles")
    print("3. Mostrar el precio promedio")
    print("4. Salir")
    selected_option = input("Selecciona una opción (1-4): ").strip()

    if selected_option == "1":
        print("\n--- Todas las piezas del catálogo ---")
        if not catalog:
            print("El catálogo está vacío actualmente.")
        else:
            for elem in catalog:
                print(f"ID: {elem['id']} | Nombre: {elem['name']} | Categoría: {elem['category']} | Precio: {elem['price']} | Estado: {elem['status']} | Descripción: {elem['description']}")
    elif selected_option == "2":
        print("\n--- Piezas disponibles ---")
        available_pieces = filter_by_status(catalog, "disponible")
        for elem in available_pieces:
            print(f"ID: {elem['id']} | Nombre: {elem['name']} | Precio: {elem['price']} | Estado: {elem['status']}")
        if not available_pieces:
            print("No se encontraron piezas disponibles.")
    elif selected_option == "3":
        print("\n--- Precio promedio ---")
        avg_price = get_average_price(catalog)
        if not catalog:
            print(f"El catálogo está vacío. Precio promedio: {avg_price:.2f}")
        else:
            print(f"Precio promedio del catálogo: {avg_price:.2f}")
    elif selected_option == "4":
        print("Saliendo del menú interactivo. Continuando con métricas y validaciones...")
        menu_active = False
    else:
        print("Opción no válida. Por favor, selecciona un número entre 1 y 4.")

# Parte 11: Calcular métricas del catálogo

metrics = get_catalog_metrics(catalog)

print("\n=== Métricas del Catálogo ===")
print(f"1. Cantidad de piezas disponibles: {metrics['available']}")
print(f"2. Cantidad de piezas reservadas: {metrics['reserved']}")
print(f"3. Cantidad de piezas vendidas: {metrics['sold']}")
print(f"4. Cantidad total de piezas: {metrics['total']}")
print(f"5. Suma total de los precios: {metrics['sum_prices']:.2f}")
print(f"6. Precio promedio del catálogo: {metrics['average_price']:.2f}")

print("\n--- Piezas enumeradas ---")
try:
    for index, piece_name in enumerate(list_pieces(catalog), start=1):
        print(f"{index}. {piece_name}")
except TypeError as error:
    print(f"Error: {error}")

# Parte 12: Validaciones básicas

print("\n=== Validaciones Básicas: Registrar Pieza Validada ===")
new_validated_piece = ask_piece_data(catalog)
catalog.append(new_validated_piece)
print("\nPieza validada añadida correctamente al catálogo:")
print(new_validated_piece)
print(f"Total actualizado de piezas en el catálogo: {len(catalog)}")
print("\nPrograma finalizado con éxito.")



