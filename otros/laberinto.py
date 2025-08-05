import sys
import random
import matplotlib.pyplot as plt

def generar_laberinto(n: int) -> list[list]:
    """ Función para generar un laberinto utilizando DFS (similar a Backtracking) """
    # Función recursiva para generar el laberinto
    def generar_camino(x: int, y: int) -> None:
        direcciones = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(direcciones) # Selección aleatoria de direcciones
        for dx, dy in direcciones:
            nx, ny = x + dx * 2, y + dy * 2
            if 0 <= nx < n  and 0 <= ny < n and laberinto[nx][ny] == 1:
                laberinto[nx - dx][ny - dy] = 0  # Quita la pared intermedia
                laberinto[nx][ny] = 0  # Marca la nueva celda como camino
                generar_camino(nx, ny)
    # Inicializamos una matriz con paredes (1)
    laberinto = [[1 for _ in range(n)] for _ in range(n)]
    # Generamos los caminos
    generar_camino(1, 1)
    # Quitamos las paredes de la salida y de la meta
    laberinto[0][1] = 0
    laberinto[-1][-2] = 0
    return laberinto

def dibujar_laberinto(laberinto: list[list], camino: list[tuple] = None) -> None:
    """ Función para dibujar el laberinto y el camino resultante """
    # Creamos una imagen para representar el laberinto
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.imshow(laberinto, cmap='binary')
    # Si hay un camino, lo dibujamos en azul
    if camino:
        camino_x, camino_y = zip(*camino)
        ax.plot(camino_y, camino_x, color='blue', linewidth=2)
    # Dibujamos la gráfica
    plt.axis('off')
    plt.show()

def generar_sucesores(estado: tuple, visitados: list[list]) -> list:
    """ Devuelve la lista de sucesores del estado actual """
    sucesores = []
    x, y = estado
    movimientos = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dx, dy in movimientos:
        nx, ny = x + dx, y + dy
        sucesor = (nx, ny)
        if laberinto[nx][ny] != 1 and not visitados[nx][ny]:
            sucesores.append(sucesor)
    return sucesores

def resolver_laberinto(laberinto: list[list]) -> list[tuple]:
    """ Función para encontrar un camino utilizando búsqueda en profundidad (DFS) """
    n = len(laberinto)
    # Matriz de visitados (evita buscar en la lista)
    visitados = [[False for _ in range(n)] for _ in range(n)]
    estado_inicial = (0, 1)
    # Estructura LIFO para recorrer el árbol
    pila = [(estado_inicial, [estado_inicial])]
    while pila:
        # Cogemos el último elemento (añadimos los hijos al final)
        estado_actual, camino = pila.pop()
        # Comprobamos si hemos llegado a la meta (-1, -2)
        x, y = estado_actual
        if x == n - 1 and y == n - 2:
            return camino
        # Añadimos a visitados
        visitados[x][y] = True
        # Generar estados sucesores (hijos)
        sucesores = generar_sucesores(estado_actual, visitados)
        for sucesor in sucesores:
            pila.append((sucesor, camino + [sucesor]))
    # No hay solución
    return []

if __name__ == "__main__":
    # Aumentamos el límite de la recursión
    sys.setrecursionlimit(10**6)
    # Generamos un laberinto de tamaño NxN
    laberinto = generar_laberinto(101)
    # Resolvemos el laberinto
    camino = resolver_laberinto(laberinto)
    # Dibujamos el laberinto y el camino en azul
    dibujar_laberinto(laberinto, camino)

'''
def mejor_candidato(pila: list[tuple], laberinto: list[list]) -> tuple:
    """ Bonus: ¿Y si intentamos escoger el mejor? """
    n = len(laberinto)
    pos = 0
    menor = float("inf")
    for i in range(len(pila)):
        estado, camino = pila[i]
        x, y = estado
        f = (n - x) + (n - y) + len(camino) # heuristica -> h + g (A*)
        if f < menor:
            menor = f
            pos = i
    return pila.pop(pos)
'''
