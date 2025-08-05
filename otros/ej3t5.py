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

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)