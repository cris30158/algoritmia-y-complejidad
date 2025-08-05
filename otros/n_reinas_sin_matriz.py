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
        if es_seguro(tablero, nivel, col):
            hijos += [col]
    # Backtracking
    for col in hijos:
        tablero.append(col)
        problema_n_reinas(tablero, soluciones, nivel + 1)
        tablero.pop() # Backtrack

N = 8
tablero = [] # Posición de la reina en cada fila
soluciones = []
problema_n_reinas(tablero, soluciones)
for solucion in soluciones:
    print("=" * N * 2)
    for num in solucion:
        for j in range(N):
            if num == j:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
