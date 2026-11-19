from validations import ALLOWED_STATUSES, validate_not_empty, validate_price, validate_status, validate_description
from catalog import (add_piece, list_pieces, find_piece_by_id, find_pieces_by_field, remove_piece,
                     get_catalog_summary, get_unique_categories, get_pieces_by_category,
                     piece_exists, filter_by_status, filter_by_min_price,
                     get_average_price, get_catalog_metrics,
                     can_be_published, needs_review, get_unsold_pieces)

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


# Parte 1 y 2 (nivel I): Bienvenida y captura inicial de piezas

def show_welcome():
    system_name = "catálogo de piezas coleccionables"
    print("¡Bienvenido!")
    print(f"Estás ingresando al {system_name}")


def register_initial_pieces(catalog):
    while True:
        try:
            quantity = int(input("¿Cuántas piezas deseas añadir? "))
            if quantity < 0:
                raise ValueError
            break
        except ValueError:
            print("Error: La cantidad debe ser un número entero igual o mayor que cero.")

    for x in range(0, quantity):
        print(f"\nIntroduce los datos para la pieza número {x + 1}:")
        catalog.append(ask_piece_data(catalog))
    print("\nCatálogo registrado:")
    print(catalog)


# Opciones del menú principal

def add_new_piece(catalog):
    print("\n=== Registrar Pieza Validada ===")
    new_validated_piece = ask_piece_data(catalog)
    catalog.append(new_validated_piece)
    print("\nPieza validada añadida correctamente al catálogo:")
    print(new_validated_piece)
    print(f"Total actualizado de piezas en el catálogo: {len(catalog)}")


def show_all_pieces(catalog):
    print("\n--- Todas las piezas del catálogo ---")
    if not catalog:
        print("El catálogo está vacío actualmente.")
    else:
        for elem in catalog:
            print(f"ID: {elem['id']} | Nombre: {elem['name']} | Categoría: {elem['category']} | Precio: {elem['price']} | Estado: {elem['status']} | Descripción: {elem['description']}")
    print(f"\nCantidad total de piezas: {len(catalog)}")


def show_available_pieces(catalog):
    print("\n--- Piezas disponibles ---")
    available_pieces = filter_by_status(catalog, "disponible")
    for elem in available_pieces:
        print(f"ID: {elem['id']} | Nombre: {elem['name']} | Precio: {elem['price']} | Estado: {elem['status']}")
    if not available_pieces:
        print("No se encontraron piezas disponibles.")


def show_average_price(catalog):
    print("\n--- Precio promedio ---")
    avg_price = get_average_price(catalog)
    if not catalog:
        print(f"El catálogo está vacío. Precio promedio: {avg_price:.2f}")
    else:
        print(f"Precio promedio del catálogo: {avg_price:.2f}")


def search_piece(catalog):
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


def delete_piece(catalog):
    print("\n--- Eliminar una pieza ---")
    piece_id = input("Introduce el identificador de la pieza que deseas eliminar: ").strip()
    if remove_piece(catalog, piece_id):
        print(f"Pieza con id '{piece_id}' eliminada correctamente.")
    else:
        print(f"No se encontró ninguna pieza con id '{piece_id}'. No se eliminó nada.")


# Opciones adicionales (funcionalidades del nivel I)

def show_categories(catalog):
    categories = get_unique_categories(catalog)

    print("\n--- Categorías Únicas ---")
    print(f"Conjunto de categorías únicas: {categories}")
    print(f"Cantidad de categorías diferentes: {len(categories)}")

    print("\n--- Resumen: piezas por categoría ---")
    for category, count in get_catalog_summary(catalog).items():
        print(f"{category}: {count} pieza(s) -> {get_pieces_by_category(catalog, category)}")


def show_pieces_by_status(catalog):
    for target_status in ALLOWED_STATUSES:
        print(f"\n--- Piezas en estado '{target_status}' ---")
        status_pieces = filter_by_status(catalog, target_status)
        for elem in status_pieces:
            print(f"ID: {elem['id']} | Nombre: {elem['name']} | Categoría: {elem['category']} | Precio: {elem['price']} | Estado: {elem['status']}")
        if not status_pieces:
            print(f"No se encontraron piezas con el estado '{target_status}'.")


def show_pieces_by_min_price(catalog):
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


def show_business_rules(catalog):
    print("\n=== Regla de Publicación (Precio > 0 y Estado 'disponible') ===")
    for elem in catalog:
        if can_be_published(elem):
            print(f"Pieza '{elem['name']}' (ID: {elem['id']}): Puede publicarse.")
        else:
            print(f"Pieza '{elem['name']}' (ID: {elem['id']}): NO puede publicarse.")

    print("\n=== Regla de Revisión (Estado 'reservada' o 'vendida') ===")
    for elem in catalog:
        if needs_review(elem):
            print(f"Pieza '{elem['name']}' (ID: {elem['id']}): Requiere revisión.")
        else:
            print(f"Pieza '{elem['name']}' (ID: {elem['id']}): NO requiere revisión.")

    print("\n=== Piezas No Vendidas (Estado diferente a 'vendida') ===")
    unsold_pieces = get_unsold_pieces(catalog)
    for elem in unsold_pieces:
        print(f"ID: {elem['id']} | Nombre: {elem['name']} | Estado: {elem['status']} | Precio: {elem['price']}")
    if not unsold_pieces:
        print("No se encontraron piezas sin vender.")


def show_metrics(catalog):
    metrics = get_catalog_metrics(catalog)

    print("\n=== Métricas del Catálogo ===")
    print(f"1. Cantidad de piezas disponibles: {metrics['available']}")
    print(f"2. Cantidad de piezas reservadas: {metrics['reserved']}")
    print(f"3. Cantidad de piezas vendidas: {metrics['sold']}")
    print(f"4. Cantidad total de piezas: {metrics['total']}")
    print(f"5. Suma total de los precios: {metrics['sum_prices']:.2f}")
    print(f"6. Precio promedio del catálogo: {metrics['average_price']:.2f}")

    print("\n--- Piezas enumeradas ---")
    for index, piece_name in enumerate(list_pieces(catalog), start=1):
        print(f"{index}. {piece_name}")


def string_manipulation(catalog):
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


# Parte 12: Menú principal usando funciones

def show_menu():
    print("\n=== Menú Interactivo ===")
    print("1. Agregar una pieza")
    print("2. Mostrar todas las piezas")
    print("3. Mostrar piezas disponibles")
    print("4. Mostrar el precio promedio")
    print("5. Buscar una pieza (por identificador u otro campo)")
    print("6. Eliminar una pieza")
    print("7. Salir")
    print("--- Opciones adicionales ---")
    print("8. Categorías y resumen por categoría")
    print("9. Filtrar piezas por estado")
    print("10. Filtrar piezas por precio mínimo")
    print("11. Reglas de publicación y revisión")
    print("12. Métricas del catálogo")
    print("13. Manipulación de strings")


def main():
    catalog = []
    show_welcome()
    register_initial_pieces(catalog)

    menu_active = True
    while menu_active:
        show_menu()
        selected_option = input("Selecciona una opción (1-13): ").strip()

        try:
            if selected_option == "1":
                add_new_piece(catalog)
            elif selected_option == "2":
                show_all_pieces(catalog)
            elif selected_option == "3":
                show_available_pieces(catalog)
            elif selected_option == "4":
                show_average_price(catalog)
            elif selected_option == "5":
                search_piece(catalog)
            elif selected_option == "6":
                delete_piece(catalog)
            elif selected_option == "7":
                print("Saliendo del catálogo. ¡Hasta pronto!")
                menu_active = False
            elif selected_option == "8":
                show_categories(catalog)
            elif selected_option == "9":
                show_pieces_by_status(catalog)
            elif selected_option == "10":
                show_pieces_by_min_price(catalog)
            elif selected_option == "11":
                show_business_rules(catalog)
            elif selected_option == "12":
                show_metrics(catalog)
            elif selected_option == "13":
                string_manipulation(catalog)
            else:
                print("Opción no válida. Por favor, selecciona un número entre 1 y 13.")
        except (ValueError, TypeError) as error:
            print(f"Error: {error}")

    print("\nPrograma finalizado con éxito.")


if __name__ == "__main__":
    main()
