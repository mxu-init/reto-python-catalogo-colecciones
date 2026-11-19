ALLOWED_STATUSES = ["disponible", "reservada", "vendida"]


# Parte 11: Validaciones de una pieza
# Cada función lanza ValueError si la validación falla y no imprime nada:
# mostrar o manejar el error es responsabilidad de quien la llama.

def validate_not_empty(value, field_name):
    """Valida que el valor no esté vacío."""
    if value is None or str(value).strip() == "":
        raise ValueError(f"El campo '{field_name}' no puede estar vacío.")


def validate_price(price):
    """Valida que el precio sea numérico y mayor que cero. Retorna el precio como float."""
    try:
        price = float(price)
    except (TypeError, ValueError):
        raise ValueError("El precio debe ser un valor numérico (ej: 12 o 19.99).")
    if price <= 0:
        raise ValueError("El precio debe ser mayor que cero.")
    return price


def validate_status(status):
    """Valida que el estado esté entre los permitidos."""
    if str(status).strip().lower() not in ALLOWED_STATUSES:
        raise ValueError("El estado debe ser 'disponible', 'reservada' o 'vendida'.")


def validate_description(description):
    """Valida que la descripción contenga 'usada' o 'certificada'."""
    description = str(description).lower()
    if "usada" not in description and "certificada" not in description:
        raise ValueError("La descripción debe contener obligatoriamente la palabra 'usada' o 'certificada'.")
