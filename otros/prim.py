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

    if num_nodos<2: # Si es un grafo vacío o sólo hay un elemento, devuelve una lista vacía
        return []
    
    nodos_insertados = [False] * num_nodos  #Lista para marcar qué nodos han sido agregados al MST (True si ya está en el MST, False si no).
    aristas_insertadas = []  #  Lista donde guardaremos las aristas seleccionadas en el MST.

    # Inicialización: Seleccionar un nodo arbitrario
    nodos_insertados[0] = True  # Seleccionamos el nodo 0 como el nodo inicial 
    candidatas = []  # Lista de aristas candidatas

    # Añadir todas las aristas desde el nodo inicial
    for j in range(num_nodos): #Recorremos los nodos vecinos del nodo 0
        if graph[0][j] > 0: #Si hay una conexión, agregamos la arista (peso, nodo_u, nodo_v)  a la lista de candidatas
            candidatas.append((graph[0][j], 0, j)) 

    # Ordenar aristas por peso (O(a log a))
    candidatas.sort()

    # Proceso Voraz
    for i in range(num_nodos - 1): #n-1 iteraciones máximo, ya que si hay n nodos, el MST tendrá exactamente n-1 aristas
        # Seleccionar la mejor arista (O(1) ya que candidatas está ordenado)
        while candidatas:
            min_weight, u, v = candidatas.pop(0)  # Extraer la mejor arista (menor peso)
            if not nodos_insertados[v]:  # Si el nodo aún no está en el MST, lo añadimos
                break
        else:
            continue  # En caso de que no haya más aristas válidas

        # Agregar la arista al MST
        aristas_insertadas.append((u, v, min_weight)) #en el resultado final se guardarán tuplas de la forma (u,v,peso)
        nodos_insertados[v] = True  # Marcar el nodo como visitado

        # Añadir nuevas aristas del nodo `v` 
        for j in range(num_nodos):
            if not nodos_insertados[j] and graph[v][j] > 0:
                candidatas.append((graph[v][j], v, j))

        # Ordenar de nuevo las candidatas
        candidatas.sort()
    

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

