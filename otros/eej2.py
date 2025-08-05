def obtener_razon(fichero):
    """
    Calcula la razón longitud/peticiones de un fichero.
    Parámetros:
        fichero: Tupla (longitud, peticiones)
    Devuelve:
        Razón longitud/peticiones
    """
    longitud, peticiones = fichero
    return longitud / peticiones


def algVoraz(fichero_original):
    """
    Calcula el tiempo medio de carga para el orden dado.
    
    >>> algVoraz([(30, 5), (20, 2), (10, 10), (40, 1)])
    [(10, 10), (30, 5), (20, 2), (40, 1)]
    520
    28.8889

    >>> algVoraz([(8,2), (2,1), (5,8), (9,20), (1,18), (3,1)])
    [(1, 18), (9, 20), (5, 8), (2, 1), (3, 1), (8, 2)]
    431
    8.62

    >>> algVoraz([(100, 50), (200, 100), (50, 25)])
    [(100, 50), (200, 100), (50, 25)]
    43750
    250.0

    >>> algVoraz([(5, 5), (10, 10), (20, 20), (40, 40)])
    [(5, 5), (10, 10), (20, 20), (40, 40)]
    3875
    51.6667

    >>> algVoraz([])
    0.0
    
    Parámetros:
        -ficheros_ordenados: Lista ordenada de tuplas (longitud, peticiones)
    Devuelve:
        -Tiempo medio de carga
    """
    if not fichero_original: # Para evitar error de 0/0 con listas vacias
        return 0.0
    
    ficheros=sorted(fichero_original, key=obtener_razon)
    print(ficheros)
    lenlista=len(ficheros)
    texe=0
    sumalx=0
    sumapx=0
    for i in range (lenlista): #Recorrer la lista por su longitud, de i=0 a i=lenlista-1
        sumalx+=ficheros[i][0]
        texe+=sumalx*ficheros[i][1]
        sumapx+=ficheros[i][1]

    print(texe)
    # Solución redondeada con 4 decimales para que sea más sencillo de probar
    return round(texe/sumapx,4)
    
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()

 # Ejemplo de uso
    # ficheros = [(30, 5), (10, 10), (20, 2), (40, 1)]  # (longitud, peticiones)
    # ordenados = ordenar(ficheros)
    # tiempo_medio = algVoraz(ordenados)

    # print("Orden óptimo de ficheros:", ordenados)
    # print("Tiempo medio de carga:", tiempo_medio)
