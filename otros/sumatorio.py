

def sumatorio(n):
    """
    Calcula el sumatorio de un número entero positivo n.
    
    >>> sumatorio(0)
    0
    >>> sumatorio(1)
    1
    >>> sumatorio(2)
    3
    >>> sumatorio(3)
    6
    >>> sumatorio(5)
    15
    >>> sumatorio(10)
    55
    >>> sumatorio(-5)
    Traceback (most recent call last):
        ...
    ValueError: El número debe ser un entero no negativo
    """
     
    if n < 0:
        raise ValueError("El número debe ser un entero no negativo") # Manejo de error para negativos
    elif n == 0:
        return 0
    else:
        return n + sumatorio(n - 1)


if __name__ == "__main__":
    import doctest
    doctest.testmod( verbose=True)