ALLOWED_STATUSES = ["disponible", "reservada", "vendida"]


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
        if value is None or str(value).strip() == "":
            raise ValueError(f"El campo '{field_name}' no puede estar vacío.")

    try:
        price = float(price)
    except (TypeError, ValueError):
        raise ValueError("El precio debe ser un valor numérico (ej: 12 o 19.99).")
    if price <= 0:
        raise ValueError("El precio debe ser mayor que cero.")

    status = str(status).strip().lower()
    if status not in ALLOWED_STATUSES:
        raise ValueError("El estado debe ser 'disponible', 'reservada' o 'vendida'.")

    description = str(description).strip()
    if "usada" not in description.lower() and "certificada" not in description.lower():
        raise ValueError("La descripción debe contener obligatoriamente la palabra 'usada' o 'certificada'.")

    return {
        "id": str(piece_id).strip(),
        "name": str(name).strip(),
        "category": str(category).strip(),
        "price": price,
        "status": status,
        "description": description
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
