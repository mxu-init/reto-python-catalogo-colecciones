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

