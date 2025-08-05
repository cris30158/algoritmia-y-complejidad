
def min_pistas(reservas):
    """
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
    # Ordenamos las reservas por hora de inicio
    reservas.sort()
    print(reservas)

    pistas = []         # Guarda el fin de la última reserva de cada pista
    asignaciones = []   # Lista de listas: reservas por pista
    i = 0               # Índice de reserva actual
    p = 0               # Índice de pista actual (para recorrido lineal simulado)

    while i < len(reservas):
        inicio, fin = reservas[i]

        if p >= len(pistas):
            # No hay pista libre, se crea una nueva
            pistas.append(fin)
            asignaciones.append([(inicio, fin)])
            i += 1
            p = 0  # Reiniciamos el recorrido de pistas para la siguiente reserva
        elif pistas[p] <= inicio:
            # Pista disponible encontrada
            pistas[p] = fin
            asignaciones[p].append((inicio, fin))
            i += 1
            p = 0
        else:
            # Pista no disponible, seguimos buscando
            p += 1

    # Mostrar las pistas con sus reservas
    for idx, reservas_pista in enumerate(asignaciones):
        print(f"Pista {idx + 1}: {reservas_pista}")

    return len(pistas)


if __name__ == "__main__":
    import doctest
    doctest.testmod( verbose=True)