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
        value = input(f"Introduce el valor para {key}: ")
        if key == "price":
            piece[key] = float(value)
        else:
            piece[key] = value
    catalog.append(piece)
    piece = {}
print("\nCatálogo registrado:")
print(catalog)

# Parte 3: Almacenamiento de la información

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