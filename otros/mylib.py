


# Función para ordenar: primero por hora, luego por tipo (-1 antes que 1)
def ordenar_eventos(evento):
    hora, tipo = evento
    return (hora, tipo)  # como tipo es -1 o +1, -1 se ordena antes si hay empate
    
def opcion2(reservas):
    """
    Calcula el número mínimo de pistas necesarias para alojar todas las reservas sin solapamientos.

    >>> opcion2([(10, 12), (9, 11), (11, 13), (15, 16)])
    2

    >>> opcion2([(9, 10), (10, 11), (11, 12)])
    1


    >>> opcion2([(9, 12), (10, 13), (11, 14), (12, 15)])
    3

    >>> opcion2([(9, 12), (10, 11), (11, 14), (12, 13), (13, 15), (14, 16)])
    2

    >>> opcion2([])
    0
    """
    if not reservas: return 0
    
    lista = []
    for inicio, fin in reservas:
        lista.append((inicio, 1))   # +1 por inicio
        lista.append((fin, -1))     # -1 por fin

    lista.sort(key=ordenar_eventos)

    ocupadas = 0 #pistas ocupadas actualmente
    max_pistas = 0  #número máximo de "ocupadas" a la vez

    for hora, tipo in lista:
        ocupadas += tipo #sumo o resto uno a las pistas ocupadas
        if ocupadas > max_pistas: #compruebo si el valor actual es el máximo de momento
            max_pistas = ocupadas

    return max_pistas #el máximo número de pistas encontrado será el número mínimo de pistas totales necesarias



if __name__ == "__main__":
    import doctest
    doctest.testmod( verbose=True)