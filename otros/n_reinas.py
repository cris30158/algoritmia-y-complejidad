import copy

def es_seguro(tablero: list[int], fila: int, columna: int) -> bool:
    # Comprueba columnas a la izquierda
    for i in range(fila):
        if tablero[i][columna] == 1:
            return False
    # Comprueba diagonal principal a la izquierda
    for i, j in zip(range(fila, -1, -1), range(columna, -1, -1)):
        if tablero[i][j] == 1:
            return False
    # Comprueba diagonal secundaria a la izquierda
    for i, j in zip(range(fila, -1, -1), range(columna, N, 1)):
        if tablero[i][j] == 1:
            return False
    return True

def problema_n_reinas(tablero: list[int], soluciones: list[int], nivel: int = 0) -> None:
    """  """
    # Si hemos llegado al final guardamos la solución
    if nivel == N:
        soluciones.append(copy.deepcopy(tablero))
    # Generamos los nuevos hijos
    hijos = []
    for col in range(N):
        if es_seguro(tablero, nivel, col):
            hijos += [col]
    # Backtracking
    for col in hijos:
        tablero[nivel][col] = 1
        problema_n_reinas(tablero, soluciones, nivel + 1)
        tablero[nivel][col] = 0 # Backtrack

N = 8
tablero = [[0] * N for _ in range(N)]
soluciones = []
problema_n_reinas(tablero, soluciones)
for solucion in soluciones:
    print("=" * N * 2)
    for row in solucion:
        for col in row:
            if col == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
