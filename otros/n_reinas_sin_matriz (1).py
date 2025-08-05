import random
def es_seguro(tablero: list[int], fila: int, columna: int) -> bool:
    seguro = True
    pos = 0
    while pos < fila and seguro:
        # Comprobamos la columna
        if tablero[pos] == columna:
            seguro = False
        # Comprobamos la diagonal principal
        elif tablero[pos] + fila == columna + pos:
            seguro = False
        # Comprobar la diagonal inversa
        elif tablero[pos] - fila == columna - pos:
            seguro = False
        pos += 1
    return seguro


def problema_n_reinas(tablero: list[int], soluciones: list[int], nivel: int = 0) -> None:
    """  """
    # Si hemos llegado al final guardamos la solución
    if nivel == N:
        soluciones.append(tablero[:])
        return
    # Generamos los nuevos hijos
    hijos = []
    for col in range(N):
        if es_seguro(tablero, nivel , col):
            hijos += [col]
    # Backtracking
    for col in hijos:
        tablero.append(col)
        problema_n_reinas(tablero, soluciones, nivel + 1)
        tablero.pop() # Backtrack
        

def problema_n_reinas_LV(N: int ):
    """  """
    # Generamos las posiciones iniciales de las reinas de forma aleatoria
    tablero = []
    validos = 0
    solución_válida = False
    for fila in range(N):
        posibles = []
        for col in range(N):
            if es_seguro(tablero, fila , col):
                posibles += [col]
        if not posibles:
            return soluciones,solución_válida
        
        col = random.choice(posibles)
        tablero.append(col)

    soluciones.append(tablero)
    solución_válida = True
    
        
    return soluciones,solución_válida
#        if es_seguro(tablero, fila, col):
#            hijos += [col]
    # Backtracking


N = 8
#tablero = [] # Posición de la reina en cada fila
soluciones = []
llamadas = []
#problema_n_reinas(tablero, soluciones)
for ejecución in range(100):
    solución_válida = False
    n_llamadas = 0
    while not solución_válida:
        n_llamadas += 1
        soluciones,solución_válida = problema_n_reinas_LV(N)
    llamadas.append(n_llamadas)

media_llamadas = sum(llamadas)/100
print('media de llamadas',media_llamadas)

solucion=soluciones[0]
print(solucion)
print("=" * N * 2)
for num in solucion:
    for j in range(N):
        if num == j:
            print("Q", end=" ")
        else:
            print(".", end=" ")
    print()
