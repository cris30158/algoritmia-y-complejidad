import random

def ponerTapones(botellas, corchos):
    """
    Algoritmo por Divide y Vencerás para emparejar botellas y corchos correctamente.
    - botellas: lista con los tamaños de las botellas.
    - corchos: lista con los tamaños de los corchos.
    
    >>> ponerTapones([5, 3, 8, 2, 7], [3, 5, 2, 8, 7])
    [(2, 2), (3, 3), (5, 5), (7, 7), (8, 8)]
    
    >>> ponerTapones([1, 4, 6], [6, 4, 1])
    [(1, 1), (4, 4), (6, 6)]
    
    >>> ponerTapones([], [])
    []
    
    >>> ponerTapones([10, 20, 30], [30, 10, 20])
    [(10, 10), (20, 20), (30, 30)]
    
    >>> ponerTapones([15, 5, 25, 10], [10, 5, 25, 15])
    [(5, 5), (10, 10), (15, 15), (25, 25)]
    
    >>> ponerTapones([100], [100])
    [(100, 100)]

    >>> ponerTapones([15, 5, 25], [10, 5, 25, 15])
    Traceback (most recent call last):
        ...
    ValueError: Hay distinta cantidad de tapones y botellas

    """ 
    if len(botellas)!=len(corchos): raise ValueError("Hay distinta cantidad de tapones y botellas")

    # Casos base, una única botella con su corcho o lista vacía
    elif len(botellas) < 1:
        return []  
    elif len(botellas) == 1:
        return [(botellas[0],corchos[0])]

    else: # Caso recursivo
    # Seleccionar un pivote al azar
        pos = random.randint(0, len(botellas) - 1)
        pivote_botella = botellas[pos]
    # Particionar las botellas y corchos en menores, iguales y mayores
        botellas_menores, botellas_mayores = [], []
        corchos_menores, corchos_mayores = [], []

    # Encontrar el corcho correcto para la botella pivote
        for corcho in corchos:
            if corcho == pivote_botella:  # Corcho correcto encontrado
                corcho_pivote = corcho
            elif corcho < pivote_botella:
                corchos_menores.append(corcho)
            else:
                corchos_mayores.append(corcho)
    
        for botella in botellas[:pos]+botellas[pos+1:]:
            if corcho_pivote > botella :
                botellas_menores.append(botella)
            else:
                botellas_mayores.append(botella)
    
    # Llamadas recursivas
        emparejamientos_menores = ponerTapones(botellas_menores, corchos_menores)
        emparejamientos_mayores = ponerTapones(botellas_mayores, corchos_mayores)
    
        return emparejamientos_menores + [(pivote_botella, corcho_pivote)] + emparejamientos_mayores



if __name__ == "__main__":
    import doctest
    doctest.testmod( verbose=True)
