def min_pistas(reservas):
    """
    usando búsqueda binaria en lugar del for sobre pistas (el anidado)

    Calcula el número mínimo de pistas necesarias para alojar todas las reservas sin solapamientos.

    >>> min_pistas([(10, 12), (9, 11), (11, 13), (15, 16)])
    [(9, 11), (10, 12), (11, 13), (15, 16)]
    Pista 1: [(9, 11), (11, 13), (15, 16)]
    Pista 2: [(10, 12)]
    2

    >>> min_pistas([(9, 10), (10, 11), (11, 12)])
    [(9, 10), (10, 11), (11, 12)]
    Pista 1: [(9, 10), (10, 11), (11, 12)]
    1

    >>> min_pistas([(9, 12), (10, 13), (11, 14), (12, 15)])
    [(9, 12), (10, 13), (11, 14), (12, 15)]
    Pista 1: [(9, 12), (12, 15)]
    Pista 2: [(10, 13)]
    Pista 3: [(11, 14)]
    3

    >>> min_pistas([(9, 12), (10, 11), (11, 14), (12, 13), (13, 15), (14, 16)])
    [(9, 12), (10, 11), (11, 14), (12, 13), (13, 15), (14, 16)]
    Pista 1: [(9, 12), (12, 13), (13, 15)]
    Pista 2: [(10, 11), (11, 14), (14, 16)]
    2

    >>> min_pistas([])
    []
    0
    """

    # Paso 1: Ordenamos las reservas por hora de inicio
    reservas.sort()
    print(reservas)

    # Lista para almacenar las horas de finalización de las reservas en cada pista
    pistas = []

    # Diccionario para almacenar las reservas asignadas a cada pista
    asignaciones = {}

    for inicio, fin in reservas:
        # Paso 2: Encontrar la primera pista disponible usando búsqueda binaria manual
        izquierda, derecha = 0, len(pistas)
        while izquierda < derecha:
            mid = (izquierda + derecha) // 2
            if pistas[mid] <= inicio:
                derecha = mid  # Buscar en la mitad izquierda
            else:
                izquierda = mid + 1  # Buscar en la mitad derecha

        # Paso 3: Asignar la reserva a la pista encontrada
        if izquierda < len(pistas):
            # Reutilizar pista existente
            pistas[izquierda] = fin
            asignaciones[izquierda].append((inicio, fin))
        else:
            # Agregar nueva pista
            pistas.append(fin)
            asignaciones[len(pistas) - 1] = [(inicio, fin)]

    # Mostrar las pistas con sus reservas
    for pista, reservas in asignaciones.items():
        print(f"Pista {pista + 1}: {reservas}")

    # El número de pistas utilizadas es el tamaño de la lista de pistas
    return len(pistas)


if __name__ == "__main__":
    import doctest
    doctest.testmod( verbose=True)
