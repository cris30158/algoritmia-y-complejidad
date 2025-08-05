

def trasponer_divide_venceras(m):
    """
    Transpone una matriz cuadrada utilizando el enfoque Divide y Vencerás.
    
    >>> trasponer_divide_venceras([[1]])
    [[1]]
    
    >>> trasponer_divide_venceras([[1, 2], [3, 4]])
    [[1, 3], [2, 4]]
    
    >>> trasponer_divide_venceras([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    
    >>> trasponer_divide_venceras([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
    [[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16]]

    >>> trasponer_divide_venceras([[0, 1, 0, 1],[0, 0, 1, 0],[1, 0, 0, 1],[0, 0, 0, 0]])
    [[0, 0, 1, 0], [1, 0, 0, 0], [0, 1, 0, 0], [1, 0, 1, 0]]

    >>> trasponer_divide_venceras([[1, 2, 3, 4, 5],[6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]])
    [[1, 6, 11, 16, 21], [2, 7, 12, 17, 22], [3, 8, 13, 18, 23], [4, 9, 14, 19, 24], [5, 10, 15, 20, 25]]


    """

    n = len(m)

    if n == 1:
        return [[m[0][0]]]  # Caso base, una matriz de 1x1 ya está traspuesta

    elif n % 2 == 1: #si la matriz es impar
        # Manejo especial para matrices impares: expandimos la matriz con una fila y columna extra para hacerla par
        #nueva_matriz = [fila + [0] for fila in m]  # Agregamos columna de ceros
        #nueva_matriz.append([0] * (n + 1))  # Agregamos fila de ceros
        nueva_matriz = []
        for fila in m:
            nueva_fila = fila + [0]  # Agregar columna de ceros
            nueva_matriz.append(nueva_fila)

        nueva_matriz.append([0] * (n + 1))  # Agregar fila de ceros



        # Aplicamos la transposición en la matriz extendida
        matriz_transpuesta = trasponer_divide_venceras(nueva_matriz)

        # Eliminamos la fila y columna extra del resultado, recortando la última fila y columna extra para obtener la matriz transpuesta original de tamaño nxn.
        #return [fila[:n] for fila in matriz_transpuesta[:n]]
        resultado = []
        for i in range(n):
            nueva_fila = []
            for j in range(n):
                nueva_fila.append(matriz_transpuesta[i][j])
            resultado.append(nueva_fila)
        return resultado
    
    else:
        mitad = n // 2
        # A11 = [fila[:mitad] for fila in m[:mitad]]  # Esquina superior izquierda
        # A12 = [fila[mitad:] for fila in m[:mitad]]  # Esquina superior derecha
        # A21 = [fila[:mitad] for fila in m[mitad:]]  # Esquina inferior izquierda
        # A22 = [fila[mitad:] for fila in m[mitad:]]  # Esquina inferior derecha

        A11,A12,A21,A22 = [],[],[],[]

        for i in range(mitad):
            fila_A11,fila_A12 = [],[]
            for j in range(mitad):
                fila_A11.append(m[i][j])  # Esquina superior izquierda
                fila_A12.append(m[i][j + mitad])  # Esquina superior derecha
            A11.append(fila_A11)
            A12.append(fila_A12)

        for i in range(mitad, n):
            fila_A21,fila_A22 = [],[]
            for j in range(mitad):
                fila_A21.append(m[i][j])  # Esquina inferior izquierda
                fila_A22.append(m[i][j + mitad])  # Esquina inferior derecha
            A21.append(fila_A21)
            A22.append(fila_A22)

    # Trasponer las submatrices recursivamente
        T11 = trasponer_divide_venceras(A11)
        T12 = trasponer_divide_venceras(A12)
        T21 = trasponer_divide_venceras(A21)
        T22 = trasponer_divide_venceras(A22)

    #Combina las submatrices en una sola matriz traspuesta, invirtiendo las T12->T21 y T21->T12
        return [T11[i] + T21[i] for i in range(len(T11))] + \
           [T12[i] + T22[i] for i in range(len(T12))]



if __name__ == "__main__":
    import doctest
    doctest.testmod()
    A = [[1,  2,  3,  4,  5,  6],
     [7,  8,  9, 10, 11, 12],
     [13,14, 15, 16, 17, 18],
     [19,20, 21, 22, 23, 24],
     [25,26, 27, 28, 29, 30],
     [31,32, 33, 34, 35, 36]]
    print(trasponer_divide_venceras(A))


    """A^T = 
       [[1,  7, 13, 19, 25, 31],
       [2,  8, 14, 20, 26, 32],
       [3,  9, 15, 21, 27, 33],
       [4, 10, 16, 22, 28, 34],
       [5, 11, 17, 23, 29, 35],
       [6, 12, 18, 24, 30, 36]]"""