from validations import (ALLOWED_STATUSES, validate_not_empty, validate_price,
                         validate_status, validate_description)


def validate_catalog(catalog):
    """Lanza TypeError si el catálogo recibido no es una lista."""
    if not isinstance(catalog, list):
        raise TypeError("El catálogo debe ser una lista de piezas.")


# Parte 1: Agregar una pieza

def add_piece(piece_id, name, category, price, status, description):
    """Valida los datos recibidos y retorna el diccionario de la pieza.

    Lanza ValueError con un mensaje claro si alguna validación falla.
    """
    fields = {"id": piece_id, "name": name, "category": category,
              "price": price, "status": status, "description": description}
    for field_name, value in fields.items():
        validate_not_empty(value, field_name)
    price = validate_price(price)
    validate_status(status)
    validate_description(description)

    return {
        "id": str(piece_id).strip(),
        "name": str(name).strip(),
        "category": str(category).strip(),
        "price": price,
        "status": str(status).strip().lower(),
        "description": str(description).strip()
    }


# Parte 2: Listar piezas

def list_pieces(catalog):
    """Retorna una lista con los nombres de todas las piezas del catálogo.

    Lanza TypeError si el catálogo no es una lista.
    """
    validate_catalog(catalog)
    return [elem["name"] for elem in catalog]


# Parte 3: Buscar una pieza por identificador

def find_piece_by_id(catalog, piece_id):
    """Retorna la pieza cuyo id coincida, o None si no existe."""
    validate_catalog(catalog)
    for elem in catalog:
        if str(elem["id"]).lower() == str(piece_id).strip().lower():
            return elem
    return None


def find_pieces_by_field(catalog, search_field, search_value):
    """Retorna una lista con las piezas cuyo campo coincida con el valor buscado."""
    validate_catalog(catalog)
    return [elem for elem in catalog if str(elem.get(search_field)).lower() == str(search_value).strip().lower()]


# Parte 4: Quitar una pieza del catálogo

def remove_piece(catalog, piece_id):
    """Elimina la pieza con el id indicado.

    Retorna True si se eliminó, o False si no se encontró o el catálogo no es válido.
    """
    try:
        validate_catalog(catalog)
        piece = find_piece_by_id(catalog, piece_id)
        if piece is None:
            raise LookupError(f"No se encontró ninguna pieza con id '{piece_id}'.")
        catalog.remove(piece)
        return True
    except (TypeError, LookupError):
        return False


# Parte 5: Resumen del catálogo (diccionario)

def get_catalog_summary(catalog):
    """Retorna un diccionario con la cantidad de piezas por categoría."""
    validate_catalog(catalog)
    summary = {}
    for elem in catalog:
        category = elem["category"]
        summary[category] = summary.get(category, 0) + 1
    return summary


def get_unique_categories(catalog):
    """Retorna un set con las categorías únicas del catálogo."""
    validate_catalog(catalog)
    categories = set()
    for elem in catalog:
        categories.add(elem["category"])
    return categories


# Parte 6: Piezas por categoría (lista)

def get_pieces_by_category(catalog, category):
    """Retorna una lista con los nombres de las piezas de la categoría indicada."""
    validate_catalog(catalog)
    return [elem["name"] for elem in catalog if elem["category"].lower() == str(category).strip().lower()]


# Parte 7: Verificar existencia de una pieza (booleano)

def piece_exists(catalog, piece_id):
    """Retorna True si existe una pieza con ese id, o False en caso contrario."""
    validate_catalog(catalog)
    return find_piece_by_id(catalog, piece_id) is not None


# Parte 8: Filtrar por estado

def filter_by_status(catalog, status):
    """Retorna una lista con las piezas que tengan el estado indicado.

    Lanza ValueError si el estado no está entre los permitidos.
    """
    validate_catalog(catalog)
    validate_status(status)
    status = str(status).strip().lower()
    return [elem for elem in catalog if elem["status"].lower() == status]


# Parte 9: Filtrar por precio mínimo

def filter_by_min_price(catalog, min_price):
    """Retorna las piezas cuyo precio sea mayor que el precio mínimo indicado.

    Lanza ValueError si el precio mínimo no es numérico.
    """
    validate_catalog(catalog)
    try:
        min_price = float(min_price)
    except (TypeError, ValueError):
        raise ValueError("El precio mínimo debe ser un valor numérico.")
    return [elem for elem in catalog if float(elem["price"]) > min_price]


# Parte 10: Calcular el precio promedio

def get_average_price(catalog):
    """Retorna el precio promedio de las piezas, o 0 si el catálogo está vacío."""
    validate_catalog(catalog)
    try:
        if not catalog:
            raise ValueError("El catálogo está vacío, no se puede calcular el promedio.")
        total_sum = sum(float(elem["price"]) for elem in catalog)
        return total_sum / len(catalog)
    except ValueError:
        return 0


def get_catalog_metrics(catalog):
    """Retorna un diccionario con las métricas principales del catálogo."""
    validate_catalog(catalog)
    count_available = 0
    count_reserved = 0
    count_sold = 0
    sum_prices = 0.0

    for elem in catalog:
        status_lower = elem["status"].lower()
        if status_lower == "disponible":
            count_available += 1
        elif status_lower == "reservada":
            count_reserved += 1
        elif status_lower == "vendida":
            count_sold += 1
        sum_prices += float(elem["price"])

    return {
        "available": count_available,
        "reserved": count_reserved,
        "sold": count_sold,
        "total": len(catalog),
        "sum_prices": sum_prices,
        "average_price": get_average_price(catalog)
    }
