#PL5


#Ejercicio 3
def secuencia(dato, N, index, act,resultados):
    """
    Genera todas las secuencias posibles de longitud N a partir de los dígitos de la cadena 'dato',
    respetando el orden relativo de los dígitos. No se permiten duplicados en el resultado.

    Args:
    - dato (str): cadena de dígitos.
    - N (int): longitud de las secuencias a generar.
    - index (int): posición actual en la cadena.
    - act (str): secuencia parcial en construcción.
    - resultados (list): lista donde se almacenan las soluciones únicas.

    Returns:
    - list: lista de secuencias válidas sin duplicados.

    
    >>> secuencia("", 3, 0, "", [])
    []

    >>> secuencia("123", 0, 0, "", [])
    []

    >>> r = secuencia("123", 2, 0, "", [])
    >>> sorted(r)
    ['12', '13', '23']

    >>> r = secuencia("115", 2, 0, "", [])
    >>> sorted(r)
    ['11', '15']

    >>> r = secuencia("1234", 3, 0, "", [])
    >>> sorted(r)
    ['123', '124', '134', '234']

    >>> r = secuencia("111", 2, 0, "", [])
    >>> sorted(r)
    ['11']

    >>> r = secuencia("1151451", 4, 0, "", [])
    >>> sorted(r)
    ['1111', '1114', '1115', '1141', '1145', '1151', '1154', '1155', '1451', '1511', '1514', '1515', '1541', '1545', '1551', '5141', '5145', '5151', '5451']
    """
    if N <= 0: # Si se solicita una longitud 0 o negativa, no se puede formar ningún número válido.
        return resultados
    
    if len(act) == N and (act not in resultados):
        resultados.append(act) # Si ya se ha construido una secuencia de longitud N y no está duplicada, se añade a los resultados.
        return resultados # Se termina esta rama de exploración.
    
    if index >= len(dato):
        # Si se ha llegado al final de la cadena y no se ha alcanzado longitud N, no se puede continuar.
        return resultados

    for i in range(index, len(dato)):
        # En cada posición desde el índice actual hasta el final:
        # Se incluye el dígito actual al camino y se continúa desde el siguiente índice.
        secuencia(dato, N, i + 1, act + dato[i], resultados)

    return resultados # Se devuelve la lista de resultados una vez finalizada la exploración.


"""
# Ejemplo de uso:
dato = "1151451"
N = 4
act=''
resultados=[]
resultados = secuencia(dato, N, 0, act,resultados)

# Convertir a enteros y mostrar ordenados
numeros = sorted(int(num) for num in resultados)
print(numeros)
"""


#Ejercicio 6

def sustituir(texto, final, M, camino=None):
    """
    Intenta reducir la cadena 'texto' a un solo carácter que coincida con 'final'
    utilizando la tabla de sustitución M.

    Args:
    - texto (str): cadena actual en proceso de reducción.
    - final (str): carácter objetivo al que queremos llegar.
    - M (dict): tabla de sustitución, representada como diccionario de diccionarios.
    - camino (list): lista que guarda los estados intermedios del texto en la ruta actual.

    Returns:
    - Una tupla (True, camino) si se logra reducir a 'final',
    - o (False, []) si no es posible hacerlo.

    >>> M = {
    ...     'a': {'a': 'b', 'b': 'b', 'c': 'a', 'd': 'd'},
    ...     'b': {'a': 'c', 'b': 'a', 'c': 'd', 'd': 'a'},
    ...     'c': {'a': 'b', 'b': 'a', 'c': 'c', 'd': 'c'},
    ...     'd': {'a': 'd', 'b': 'c', 'c': 'd', 'd': 'b'}
    ... }

    >>> sustituir("acabada", "d", M)
    (True, ['acabada', 'aabada', 'bbada', 'aada', 'ada', 'da', 'd'])

    >>> sustituir("acabada", "z", M)
    (False, [])

    >>> sustituir("a", "a", M)
    (True, ['a'])

    >>> sustituir("a", "b", M)
    (False, [])

    >>> sustituir("aa", "b", M)
    (True, ['aa', 'b'])

    >>> sustituir("ab", "b", M)
    (True, ['ab', 'b'])

    >>> sustituir("ab", "c", M)
    (False, [])

    >>> sustituir("ab", "z", M)
    (False, [])

    >>> sustituir("abcd", "x", M)
    (False, [])


    """

    # Si no se ha proporcionado camino, se inicializa con el texto original como primer paso
    if camino is None:
        camino = [texto]

    # CASO BASE: Si el texto se ha reducido a un solo carácter
    if len(texto) == 1:
        if texto == final:
            # Si el único carácter coincide con el objetivo, hemos terminado
            return True, camino
        else:
            # Si no coincide, esta rama no lleva a una solución
            return False, []

    # CASO RECURSIVO: intentamos sustituir todos los pares consecutivos posibles
    for i in range(len(texto) - 1):
        a, b = texto[i], texto[i + 1]  # tomamos el par de caracteres consecutivos

        # Verificamos si existe una sustitución válida en la tabla
        if a in M and b in M[a]:
            nuevo_caracter = M[a][b]  # obtenemos el resultado de la sustitución

            # Construimos la nueva cadena con la sustitución aplicada
            nueva_cadena = texto[:i] + nuevo_caracter + texto[i + 2:]

            # Añadimos la nueva cadena al camino para registrar el paso
            camino.append(nueva_cadena)

            # Llamada recursiva para continuar el proceso con la nueva cadena
            exito, resultado = sustituir(nueva_cadena, final, M, camino)

            if exito:
                # Si la rama lleva a una solución, devolvemos el camino completo
                return True, resultado

            # Si no funcionó, hacemos "backtrack": quitamos el último paso del camino
            camino.pop()

    # Si se han probado todas las sustituciones posibles y ninguna funcionó
    return False, []



"""
#Ejemplo de ejecución:

# Tabla de sustitución (ejemplo). Se asume que la tabla es completa y está definida de la siguiente forma:
# Por ejemplo, M['c']['a'] = 'b' indica que la secuencia "ca" se sustituye por "b"
M = {
    'a': {'a': 'b', 'b': 'b', 'c': 'a', 'd': 'd'},
    'b': {'a': 'c', 'b': 'a', 'c': 'd', 'd': 'a'},
    'c': {'a': 'b', 'b': 'a', 'c': 'c', 'd': 'c'},
    'd': {'a': 'd', 'b': 'c', 'c': 'd', 'd': 'b'}
}

texto = "acabada"
final = "d"

exito, camino = sustituir(texto, final, M)
if exito:
    print("Ruta encontrada:")
    for paso in camino:
        print(paso)
else:
    print("No es posible reducir al carácter final.")
    """


# Ejemplo de uso:
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)