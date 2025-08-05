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