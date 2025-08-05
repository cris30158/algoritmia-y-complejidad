"""
 Enunciado:
  - Se tienen dos jarras, una de 4 litros y otra de 3.
  - Ninguna de ellas tiene marcas de medición.
  - Se tiene una bomba que permite llenar jarras de agua.
  - Averiguar cómo se puede lograr tener exactamente 2 litros de agua
    en la jarra de 4 litros de capacidad.

 Representación de estados: x y con x en {0,1,2,3,4} e y en {0,1,2,3}
 Numero de estados: 20
 Estado inicial: (0 0)
 Estado final: (2 y)
 Operadores:
  - Llenar la jarra de 4 litros con la bomba.
  - Llenar la jarra de 3 litros con la bomba.
  - Vaciar la jarra de 4 litros en el suelo.
  - Vaciar la jarra de 3 litros en el suelo.
  - Echar el contenido de la jarra de 4 litros en la jarra de 3 litros.
  - Echar el contenido de la jarra de 3 litros en la jarra de 4 litros.
"""

def operaciones(estado: tuple) -> dict:
    """ Devuelve un diccionario con las operaciones disponibles aplicadas al estado actual """
    jarra_4, jarra_3 = estado
    return {
        "Llenar jarra de 4 litros": (4, jarra_3),
        "Llenar jarra de 3 litros": (jarra_4, 3),
        "Vaciar jarra de 4 litros": (0, jarra_3),
        "Vaciar jarra de 3 litros": (jarra_4, 0),
        "Verter de jarra de 4 a jarra de 3": (max(0, jarra_4 - (3 - jarra_3)), min(3, jarra_4 + jarra_3)),
        "Verter de jarra de 3 a jarra de 4": (min(4, jarra_4 + jarra_3), max(0, jarra_3 - (4 - jarra_4))),
    }

def generar_sucesores(estado: tuple, visitados: set) -> list:
    """ Devuelve la lista de sucesores del estado actual """
    sucesores = []
    for _, sucesor in operaciones(estado).items():
        if not sucesor in visitados:
            sucesores.append(sucesor)
    return sucesores

def busqueda_en_profundidad_recursivo(estado_actual: tuple, visitados: set) -> list:
    """ Devuelve el camino para encontrar la solución al problema de las jarras """
    # Extraemos la jarra de 4L para comprobar la solución
    jarra4, _ = estado_actual
    if jarra4 == 2:
        return [estado_actual]
    # Añadimos a visitados
    visitados.add(estado_actual)
    # Generar estados sucesores (hijos)
    sucesores = generar_sucesores(estado_actual, visitados)
    # Recorrer en profundidad
    for sucesor in sucesores:
        return [estado_actual] + busqueda_en_profundidad_recursivo(sucesor, visitados)
    # No hay solución
    return []

def busqueda_en_profundidad(estado_inicial: tuple) -> list:
    """ Devuelve el camino para encontrar la solución al problema de las jarras """
    visitados = set()
    # Estructura LIFO para recorrer el árbol
    pila = [(estado_inicial, [estado_inicial])]
    while pila:
        # Cogemos el último elemento (añadimos los hijos al final)
        estado_actual, camino = pila.pop()
        # Extraemos la jarra de 4L para comprobar la solución
        jarra4, _ = estado_actual
        if jarra4 == 2:
            return camino
        # Añadimos a visitados
        visitados.add(estado_actual)
        # Generar estados sucesores (hijos)
        sucesores = generar_sucesores(estado_actual, visitados)
        for sucesor in reversed(sucesores):
            pila.append((sucesor, camino + [sucesor]))
    # No hay solución
    return []

def busqueda_en_anchura(estado_inicial: tuple) -> list:
    """ Devuelve el camino para encontrar la solución al problema de las jarras """
    visitados = set()
    # Estructura FIFO para recorrer el árbol
    cola = [(estado_inicial, [estado_inicial])]
    while cola:
        # Cogemos el primer elemento (añadimos los hijos al final)
        estado_actual, camino = cola.pop(0)
        # Extraemos la jarra de 4L para comprobar la solución
        jarra4, _ = estado_actual
        if jarra4 == 2:
            return camino
        # Añadimos a visitados
        visitados.add(estado_actual)
        # Generar estados sucesores (hijos)
        sucesores = generar_sucesores(estado_actual, visitados)
        for sucesor in reversed(sucesores):
            cola.append((sucesor, camino + [sucesor]))
    # No hay solución
    return []

# Programa
estado_inicial = (0, 0)
solucion = busqueda_en_anchura(estado_inicial)
for paso in solucion:
    print(paso)
