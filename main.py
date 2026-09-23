# Nivel 1
# Parte 1: Preparación del proyecto

system_name = "catálogo de piezas coleccionables"
print("¡Bienvenido!")
print(f"Estás ingresando al {system_name}")

# Parte 2: Captura de piezas por terminal

cant = int(input("¿Cuántos items quieres añadir?"))
lista_de_items = []

#Test para cómo recoger/consultar datos diccionarios
"""
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