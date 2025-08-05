#Kruscal

def buscarraiz(padre, u):
    """
    Función que busca el representante del conjunto al que pertenece 'u'; devuelve la raíz del conjunto al que pertenece un nodo u.

    >>> padre = {'A': 'A', 'B': 'A', 'C': 'B', 'D': 'D'}
    >>> buscarraiz(padre, 'C')  # C está en el conjunto de B, que pertenece a A
    'A'
    >>> padre  # La compresión de ruta hace que C apunte directamente a A
    {'A': 'A', 'B': 'A', 'C': 'A', 'D': 'D'}
    """
    if padre[u] != u:
        padre[u] = buscarraiz(padre, padre[u])
    return padre[u]

def union(padre, u, v):
    """
    "Fusiona los conjuntos" de u y v para que el padre de v sea el de u.

    >>> padre = {'A': 'A', 'B': 'B', 'C': 'C'}
    >>> union(padre, 'A', 'B')
    >>> buscarraiz(padre, 'B')  # Ahora B pertenece al conjunto de A
    'A'
    >>> padre  # Se actualiza la estructura de conjuntos
    {'A': 'A', 'B': 'A', 'C': 'C'}
    """
    padre[buscarraiz(padre, v)] = buscarraiz(padre, u)

def kruskal(nodos, aristas):
    """
    Implementación del algoritmo de Kruskal para encontrar el Árbol de Recubrimiento Mínimo.
    Parámetros:
      -nodos: iterable con los nodos del grafo.
      -aristas: lista de tuplas (u, v, peso) representando cada arista con su longitud.
    
    Devuelve:
      -listafinal: lista de aristas que forman el árbol de recubrimiento mínimo.

    >>> nodos = ['A', 'B', 'C', 'D', 'E']
    >>> aristas = [('A', 'B', 1), ('A', 'C', 3), ('B', 'C', 1), ('B', 'D', 4), ('C', 'D', 1), ('C', 'E', 6), ('D', 'E', 2)]
    >>> kruskal(nodos, aristas)
    [('A', 'B', 1), ('B', 'C', 1), ('C', 'D', 1), ('D', 'E', 2)]
    """
    # Inicialización: cada nodo en su conjunto.
    padre = {nodo: nodo for nodo in nodos} # del tipo  padre = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D'}
    
    # Ordenar las aristas por longitudes crecientes.
    aristas.sort(key=obtener_peso)
    
    listafinal = []  # Conjunto de aristas del árbol de recubrimiento mínimo.
    n=len(nodos)
    # Bucle: recorrer las aristas desde la de menor peso hasta la de mayor.
    for u, v, peso in aristas:
        if buscarraiz(padre, u) != buscarraiz(padre, v): #si dos tienen el mismo padre significa que hay ciclos
            union(padre, u, v) #si no hay ciclos, modifico el padre de v
            listafinal.append((u, v, peso)) # y guardo la tupla en el resultado final
            n-=1
        if n==0:
            break  # Se ha obtenido el árbol de recubrimiento mínimo.
    
    return listafinal




def obtener_peso(tupla):
    return tupla[2]  # Devuelve el tercer elemento de la tupla

          






# Ejemplo de uso:
if __name__ == "__main__":
    # Definición de nodos y aristas: cada arista es (u, v, peso)
    import doctest
    doctest.testmod()
    nodos = ['A', 'B', 'C', 'D', 'E']
    aristas = [
        ('A', 'B', 1),
        ('A', 'C', 3),
        ('B', 'C', 1),
        ('B', 'D', 4),
        ('C', 'D', 1),
        ('C', 'E', 6),
        ('D', 'E', 2)
    ]
    
    mst = kruskal(nodos, aristas)
    print("Aristas del árbol de recubrimiento mínimo:")
    for arista in mst:
        print(arista)