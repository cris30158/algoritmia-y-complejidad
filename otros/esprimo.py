

# def esprimo1(n):
#     esprimo=True
#     if n<2:
#         esprimo=False
#     else:
#         for i in range(2,n): #2....n-1
#             if (n%i)==0: esprimo=False

#     return (esprimo)




def esprimo2(n):
    """
    Determina si un número es primo.

    >>> esprimo2(2)
    True
    >>> esprimo2(3)
    True
    >>> esprimo2(4)
    False
    >>> esprimo2(5)
    True
    >>> esprimo2(11)
    True
    >>> esprimo2(15)
    False
    >>> esprimo2(1)
    False
    >>> esprimo2(0)
    False
    >>> esprimo2(-7)
    False
    """
    esprimo=True
    if (n<2): 
        esprimo=False
    else:
        for i in range(2,int(n**0.5)+1): #2....(raiz de n)
            if (n%i)==0: esprimo=False
    return esprimo


if __name__ == "__main__":
    import doctest
    doctest.testmod( verbose=True)