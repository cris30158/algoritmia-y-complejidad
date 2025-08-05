def permutar(A, act, usado):
    if len(act) == len(A):
        print(act)  # o print(''.join(act)) si A es una lista de caracteres
        return
    
    for i in range(len(A)):
        if not usado[i]:
            usado[i] = True
            act.append(A[i])
            permutar(A, act, usado)
            act.pop()         # quitar el último elemento (backtrack)
            usado[i] = False   # marcar como no usado nuevamente
#complejidad=N*N!; N cuesta el bucle for y hay N! permutaciones (seria igual si tenemos en cuenta quitar duplicados, ya que en el caso todas son distintas, y nlogn de ordenar es menor) 

def conmutar(A, act, N): #N es de cuanta longitud quiero las combinaciones
    if len(act) == N:
        print(act)  # o print(''.join(act)) si A es una lista de caracteres
        return
    
    for i in range(len(A)):
            act.append(A[i])
            conmutar(A[i+1:], act,N)
            act.pop()         # quitar el último elemento (backtrack)


# Ejemplo de uso
A = ['a', 'b', 'c']  # puede ser también A = [1, 2, 3]
usado = [False] * len(A)
act = []

#permutar(A, act, usado)
conmutar(A, act, 2)


"""
Se dispone de un tablero M de tamaño FxC (F es la cantidad de filas y C la
cantidad de columnas) y se pone en una casilla inicial (posx, posy) un caballo de
ajedrez. El objetivo es encontrar, si es posible, la forma en la que el caballo debe
moverse para recorrer todo el tablero de manera que cada casilla se utilice una
única vez en el recorrido (el tablero 8x8 siempre tiene solución
independientemente de dónde comience el caballo). El caballo puede terminar
en cualquier posición del tablero.
Un caballo tiene ocho posibles movimientos (suponiendo, claro está, que no se
sale del tablero). Un movimiento entre las casillas Mij y Mpq es válido solamente
si:
• (|p–i|=1)&&(|q–j|=2), o bien si
• (|p–i|=2)&&(|q–j|=1),
es decir, una coordenada cambia dos unidades y la otra una única unidad.

"""

def knight_tour(F, C, start_x, start_y):
    tablero = [[-1 for _ in range(C)] for _ in range(F)] #tamaño fxc
    movimientos = [(2, 1), (1, 2), (-1, 2), (-2, 1),
                   (-2, -1), (-1, -2), (1, -2), (2, -1)]

    def es_valido(x, y):
        return 0 <= x < F and 0 <= y < C and tablero[x][y] == -1 #si no se sale del tablero y si no se ha pisado aun, es valida

    def backtrack(x, y, paso):
        if paso == F * C:
            return True

        for dx, dy in movimientos:
            nx, ny = x + dx, y + dy
            if es_valido(nx, ny):
                tablero[nx][ny] = paso
                if backtrack(nx, ny, paso + 1):
                    return True
                tablero[nx][ny] = -1  # backtrack

        return False

    tablero[start_x][start_y] = 0
    if backtrack(start_x, start_y, 1):
        for fila in tablero:
            print(fila)
    else:
        print("No hay solución")

# Ejemplo de uso para tablero 8x8 desde posición (0, 0)
#knight_tour(8, 8, 0, 0)


def encontrar_caminos(laberinto, x, y, camino, visitado, soluciones):
    filas, cols = len(laberinto), len(laberinto[0])

    # Si está fuera del laberinto o en una pared o ya visitada
    if not (0 <= x < filas and 0 <= y < cols) or laberinto[x][y] or visitado[x][y]:
        return

    # Si está en una casilla de borde y no es pared → es la salida
    if (x == 0 or x == filas - 1 or y == 0 or y == cols - 1) and not laberinto[x][y]:
        soluciones.append(camino + [(x, y)])
        return

    visitado[x][y] = True
    camino.append((x, y))

    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]: #moverse hacia delante,detras,izq,der
        encontrar_caminos(laberinto, x + dx, y + dy, camino, visitado, soluciones)

    # Backtrack
    camino.pop()
    visitado[x][y] = False

n, m = 5, 5
laberinto = [
    [True,  True,  True,  True,  True],
    [True, False, False, False, True],
    [True, False, True,  False, True],
    [True, False, False, False, False],  # ← salida en (3, 4)
    [True,  True,  True,  True,  True]
]

inicio_x, inicio_y = 1, 1
visitado = [[False]*m for _ in range(n)]
soluciones = []

#encontrar_caminos(laberinto, inicio_x, inicio_y, [], visitado, soluciones)

#print(f"Se encontraron {len(soluciones)} caminos:")
#for camino in soluciones:
#    print(camino)




def mejor_camino(laberinto, x, y, camino, visitado, mejor):
    filas, cols = len(laberinto), len(laberinto[0])

    if not (0 <= x < filas and 0 <= y < cols) or laberinto[x][y] or visitado[x][y]:
        return

    if (x == 0 or x == filas - 1 or y == 0 or y == cols - 1) and not laberinto[x][y]:
        camino_actual = camino + [(x, y)]
        if mejor[0] is None or len(camino_actual) < len(mejor[0]): #cambio para guardar el camino mas corto
            mejor[0] = camino_actual
        return

    visitado[x][y] = True
    camino.append((x, y))

    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        mejor_camino(laberinto, x + dx, y + dy, camino, visitado, mejor)

    camino.pop()
    visitado[x][y] = False
    
mejor = [None]
visitado = [[False]*m for _ in range(n)]
#mejor_camino(laberinto, inicio_x, inicio_y, [], visitado, mejor)

#print("Mejor camino encontrado:")
#print(mejor[0])




 #hacer palabra moviendome a celdas arriba abajo izq der
def hacerpalabra(tablero, x, y, palabra, act, visitado):
    if len(act) == len(palabra):
        return ''.join(act) == palabra

    filas, columnas = len(tablero), len(tablero[0])

    for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < filas and 0 <= ny < columnas:# and not visitado[nx][ny]:
            act.append(tablero[nx][ny])
            #visitado[nx][ny] = True
            if hacerpalabra(tablero, nx, ny, palabra, act, visitado):
                return True
            act.pop()
            #visitado[nx][ny] = False

    return False

def funcionhacerpalabra(tablero, palabra):
    filas, columnas = len(tablero), len(tablero[0])
    visitado = [[False]*columnas for _ in range(filas)]
    for i in range(filas):
        for j in range(columnas):
            if hacerpalabra(tablero, i, j, palabra,[],visitado):
                return True

    return False

tablero = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]
palabra = "ABCCED"

print(funcionhacerpalabra(tablero, palabra))  # True

"""
Dado un array de enteros positivos nums y un número k, 
¿es posible dividir los elementos de nums en k subconjuntos disjuntos 
cuya suma total sea la misma?

ej:
nums = [4, 3, 2, 3, 5, 2, 1]
k = 4
Suma total = 20
Suma por subconjunto = 20 / 4 = 5
Es posible: [5], [1,4], [2,3], [2,3]
"""

def puede_partirse_en_k(nums, k):
    if (sum(nums) % k != 0):
        return False

    target = sum(nums) // k
    #nums.sort(reverse=True)  # ayuda a podar más rápido
    buckets = [0] * k

    return buscarsubconjuntos(nums, 0, buckets, target)

def buscarsubconjuntos(nums, index, buckets, objetivo):
    if index == len(nums):
        return all(b == objetivo for b in buckets)

    num = nums[index]
    for i in range(len(buckets)): #busco el num a ver si me cabe en algun bucket
        if buckets[i] + num <= objetivo:
            buckets[i] += num
            if buscarsubconjuntos(nums, index + 1, buckets, objetivo):
                return True
            buckets[i] -= num  # backtrack

        # optimización: no pruebes el mismo valor en otro bucket vacío
        if buckets[i] == 0:
            break

    return False


nums = [4, 3, 2, 3, 5, 2, 1]
k = 4
resultado = puede_partirse_en_k(nums, k)
print("¿Se puede partir en", k, "subconjuntos iguales?:", resultado)