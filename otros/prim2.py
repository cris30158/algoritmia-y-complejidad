def prim(graph):
    """
    Implementación del algoritmo de Prim utilizando una matriz de adyacencia 
    
    graph: Matriz de adyacencia (lista de listas) representando el grafo (comienza desde el nodo 0)
    return: Lista de aristas del Árbol de Expansión Mínima (MST).

    >>> graph = [
    ...     [0, 2, 0, 6, 0],
    ...     [2, 0, 3, 8, 5],
    ...     [0, 3, 0, 0, 7],
    ...     [6, 8, 0, 0, 9],
    ...     [0, 5, 7, 9, 0]
    ... ]
    >>> prim(graph)
    [(0, 1, 2), (1, 2, 3), (1, 4, 5), (0, 3, 6)]

    # Grafo diferente con conexiones distintas
    >>> graph2 = [
    ...     [0, 1, 4, 0, 0],
    ...     [1, 0, 2, 6, 0],
    ...     [4, 2, 0, 3, 5],
    ...     [0, 6, 3, 0, 7],
    ...     [0, 0, 5, 7, 0]
    ... ]
    >>> prim(graph2)
    [(0, 1, 1), (1, 2, 2), (2, 3, 3), (2, 4, 5)]

    # Grafo completamente conectado con pesos distintos
    >>> graph3 = [
    ...     [0, 10, 20, 30, 40],
    ...     [10, 0, 50, 60, 70],
    ...     [20, 50, 0, 80, 90],
    ...     [30, 60, 80, 0, 100],
    ...     [40, 70, 90, 100, 0]
    ... ]
    >>> prim(graph3)
    [(0, 1, 10), (0, 2, 20), (0, 3, 30), (0, 4, 40)]

    # Grafo con pesos iguales
    >>> graph4 = [
    ...     [0, 5, 5, 5, 5],
    ...     [5, 0, 5, 5, 5],
    ...     [5, 5, 0, 5, 5],
    ...     [5, 5, 5, 0, 5],
    ...     [5, 5, 5, 5, 0]
    ... ]
    >>> prim(graph4)
    [(0, 1, 5), (0, 2, 5), (0, 3, 5), (0, 4, 5)]

    # Grafo que ya es un MST (una línea)
    >>> graph5 = [
    ...     [0, 1, 0, 0, 0],
    ...     [1, 0, 2, 0, 0],
    ...     [0, 2, 0, 3, 0],
    ...     [0, 0, 3, 0, 4],
    ...     [0, 0, 0, 4, 0]
    ... ]
    >>> prim(graph5)
    [(0, 1, 1), (1, 2, 2), (2, 3, 3), (3, 4, 4)]

    # Grafo vacío
    >>> graph6 = []
    >>> prim(graph6)
    []

    # Grafo con solo un elemento
    >>> graph7 = [0]
    >>> prim(graph7)
    []


    """
    num_nodos = len(graph)  # Número de nodos en el grafo

    if num_nodos < 2: # Si es un grafo vacío o sólo hay un elemento, devuelve una lista vacía
        return []

    nodos_insertados = [False] * num_nodos  #Lista para marcar qué nodos han sido agregados al MST (True si ya está en el MST, False si no).
    aristas_insertadas = []  #  Lista donde guardaremos las aristas seleccionadas en el MST.
    
    dist = [float('inf')] * num_nodos  # Distancia mínima de cada nodo al MST
    parent = [-1] * num_nodos  # Para almacenar la conexión en el MST

    # Inicializamos el primer nodo en el MST
    dist[0] = 0  

    for i in range(num_nodos):
        # Buscar el nodo de menor distancia que aún no está en el MST
        min_dist = float('inf') #crea una lista llamada dist de tamaño num_nodos, donde cada posición se inicializa a infinito.
        u = -1
        for v in range(num_nodos):
            if not nodos_insertados[v] and dist[v] < min_dist:
                min_dist = dist[v]
                u = v

        if u == -1:
            break  # Si no encontramos un nodo válido, terminamos

        # Agregar el nodo al MST
        nodos_insertados[u] = True
        if parent[u] != -1:  # No agregamos la raíz inicial
            aristas_insertadas.append((parent[u], u, graph[parent[u]][u]))

        # Actualizar distancias de los vecinos de u
        for v in range(num_nodos):
            if not nodos_insertados[v] and 0 < graph[u][v] < dist[v]:
                dist[v] = graph[u][v]
                parent[v] = u  # Guardar la arista en el MST

    return aristas_insertadas



if __name__ == "__main__":
    import doctest
    doctest.testmod()
# Ejemplo de uso con una matriz de adyacencia
    graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
    ]

    mst = prim(graph)
    print(mst)
