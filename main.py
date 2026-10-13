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

keys = ["id", "name", "category", "price", "status", "description"]

piece = {}
catalog = []
quantity = int(input("¿Cuántas piezas deseas añadir? "))
for x in range(0, quantity):
    print(f"\nIntroduce los datos para la pieza número {x + 1}:")
    for key in keys:
        if key == "id":
            while True:
                try:
                    id_num = int(input(f"Introduce el valor para {key}: "))
                    existing_ids = [elem["id"] for elem in catalog]
                    if id_num in existing_ids:
                        print("Ya existe una pieza con ese ID. Por favor, introduce uno diferente.")
                    else:
                        piece[key] = id_num
                        break
                except ValueError:
                    print("Error: El ID debe ser un número entero.")

        elif key == "price":
            while True:
                try:
                    price_val = float(input(f"Introduce el valor para {key}: "))
                    piece[key] = price_val
                    break
                except ValueError:
                    print("Error: El precio debe ser un número válido (ej: 12 o 19.99).")

        else:
            value = input(f"Introduce el valor para {key}: ")
            piece[key] = value
    catalog.append(piece)
    piece = {}
print("\nCatálogo registrado:")
print(catalog)

# Parte 3: Almacenamiento de la información | Acceso a los valores de cada pieza

print("\n--- Búsqueda de pieza por campo y valor ---")
search_field = input("¿Por qué campo deseas buscar? (id, name, category, price, status, description): ").strip().lower()
search_value = input(f"Introduce el valor de '{search_field}' que deseas encontrar: ").strip()

found_pieces = [elem for elem in catalog if str(elem.get(search_field)).lower() == search_value.lower()]

if not found_pieces:
    print(f"No se encontró ninguna pieza con {search_field} = '{search_value}'.")
else:
    print(f"Se encontraron {len(found_pieces)} pieza(s):")
    for elem in found_pieces:
        print(elem)

# Parte 4: Información adicional del catálogo

categories = set()
for elem in catalog:
    categories.add(elem["category"])

print("\n--- Categorías Únicas ---")
print(f"Conjunto de categorías únicas: {categories}")
print(f"Cantidad de categorías diferentes: {len(categories)}")

# Parte 5: Mostrar el catálogo

print("\n=== Catálogo Completo de Piezas ===")
for elem in catalog:
    print(f"Identificador: {elem['id']} | Nombre: {elem['name']} | Categoría: {elem['category']} | Precio: {elem['price']} | Estado: {elem['status']} | Descripción: {elem['description']}")

print(f"\nCantidad total de piezas: {len(catalog)}")
print(f"Categorías únicas: {categories}")
print(f"Cantidad de categorías diferentes: {len(categories)}")

# Nivel 2
# Parte 6: Filtrar piezas por estado

for target_status in ["disponible", "reservada", "vendida"]:
    print(f"\n--- Piezas en estado '{target_status}' ---")
    status_found = False
    for elem in catalog:
        if elem["status"].lower() == target_status:
            print(f"ID: {elem['id']} | Nombre: {elem['name']} | Categoría: {elem['category']} | Precio: {elem['price']} | Estado: {elem['status']}")
            status_found = True
    if not status_found:
        print(f"No se encontraron piezas con el estado '{target_status}'.")

# Parte 7: Filtrar piezas por precio

min_price_input = input("\nIntroduce un precio mínimo para filtrar: ").strip()
while not min_price_input.replace(".", "", 1).isdigit():
    print("Precio no válido. Por favor, introduce un valor numérico.")
    min_price_input = input("Introduce un precio mínimo para filtrar: ").strip()

min_price = float(min_price_input)
price_found = False
print(f"\n--- Piezas con precio superior a {min_price} ---")
for elem in catalog:
    if float(elem["price"]) > min_price:
        print(f"ID: {elem['id']} | Nombre: {elem['name']} | Precio: {elem['price']}")
        price_found = True

if not price_found:
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
        available_found = False
        for elem in catalog:
            if elem["status"].lower() == "disponible":
                print(f"ID: {elem['id']} | Nombre: {elem['name']} | Precio: {elem['price']} | Estado: {elem['status']}")
                available_found = True
        if not available_found:
            print("No se encontraron piezas disponibles.")
    elif selected_option == "3":
        print("\n--- Precio promedio ---")
        if not catalog:
            print("El catálogo está vacío. Precio promedio: 0.00")
        else:
            total_sum = sum(float(elem["price"]) for elem in catalog)
            avg_price = total_sum / len(catalog)
            print(f"Precio promedio del catálogo: {avg_price:.2f}")
    elif selected_option == "4":
        print("Saliendo del menú interactivo. Continuando con métricas y validaciones...")
        menu_active = False
    else:
        print("Opción no válida. Por favor, selecciona un número entre 1 y 4.")


