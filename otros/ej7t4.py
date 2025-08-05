def lcs_bits(A, B):
    """
    Calcula la subsecuencia común más larga (LCS) entre dos listas de bits.

    >>> lcs_bits([0,1,1,0,1,0,1,0], [1,0,1,0,0,1,0,0,1])
    (6, [0, 1, 1, 0, 0, 1])
    
    #También sirve [1, 1, 0, 1, 0, 0]

    >>> lcs_bits([], [])
    (0, [])

    >>> lcs_bits([], [1, 0, 1])
    (0, [])

    >>> lcs_bits([1, 0, 1], [])
    (0, [])

    >>> lcs_bits([1, 1, 1], [0, 0, 0])
    (0, [])

    >>> lcs_bits([1, 0, 1], [1, 0, 1])
    (3, [1, 0, 1])

    >>> lcs_bits([1, 0, 0, 1], [0, 1, 0, 1])
    (3, [1, 0, 1])
    
    #Otra posible LCS: [0, 0, 1]
    """
    m, n = len(A), len(B)
    
    # Crear tabla dp de tamaño (m+1)x(n+1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Llenar la tabla
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Longitud máxima
    longitud_maxima = dp[m][n]

    # Reconstrucción de la subsecuencia
    i, j = m, n
    subsecuencia = []

    while i > 0 and j > 0:
        if A[i - 1] == B[j - 1]:
            subsecuencia.append(A[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    subsecuencia.reverse()  # La reconstrucción es hacia atrás

    return longitud_maxima, subsecuencia


def lcs_bits_espacio_reducido(A, B):
    """
    Calcula la longitud de la LCS entre dos listas de bits usando espacio reducido.

    >>> lcs_bits_espacio_reducido([0,1,1,0,1,0,1,0], [1,0,1,0,0,1,0,0,1])
    6

    >>> lcs_bits_espacio_reducido([], [])
    0

    >>> lcs_bits_espacio_reducido([], [1, 0, 1])
    0

    >>> lcs_bits_espacio_reducido([1, 0, 1], [])
    0

    >>> lcs_bits_espacio_reducido([1, 1, 1], [0, 0, 0])
    0

    >>> lcs_bits_espacio_reducido([1, 0, 1], [1, 0, 1])
    3

    >>> lcs_bits_espacio_reducido([1, 0, 0, 1], [0, 1, 0, 1])
    3
    """
    m, n = len(A), len(B)

    # Usar solo dos filas
    prev = [0] * (n + 1)
    curr = [0] * (n + 1)

    # Llenar solo dos filas
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                curr[j] = prev[j - 1] + 1
            else:
                curr[j] = max(prev[j], curr[j - 1])
        # Intercambiar filas (evitar copiar)
        prev, curr = curr, prev

    # La longitud de la LCS está en la última fila usada
    return prev[n]  # ya que al final, prev es la última válida



if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)