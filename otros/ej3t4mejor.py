from math import inf

def cambio_dinero_con_capacidad(v, c, D):
    """
    Determina si es posible formar la cantidad D usando billetes con valores y cantidades dadas.

    Args:
        v (list[int]): valores de los billetes (por ejemplo, [1, 2])
        c (list[int]): cantidad máxima disponible por tipo (por ejemplo, [2, 1])
        D (int): cantidad total que se quiere formar

    Returns:
        tuple:
            - bool: True si se puede formar D, False si no
            - list[int] o None: cuántos billetes de cada tipo se usaron si es posible, o None

        >>> cambio_dinero_con_capacidad([1, 2], [2, 1], 3)
        (True, [1, 1])

        >>> cambio_dinero_con_capacidad([2, 5], [1, 1], 3)
        (False, None)

        >>> cambio_dinero_con_capacidad([1], [10], 7)
        (True, [7])

        >>> cambio_dinero_con_capacidad([1, 3], [3, 2], 6)
        (True, [0, 2])

        >>> cambio_dinero_con_capacidad([1, 2, 5], [1, 2, 1], 8)
        (True, [1, 1, 1])

        >>> cambio_dinero_con_capacidad([3, 6], [10, 10], 5)
        (False, None)

        >>> cambio_dinero_con_capacidad([1, 2, 5, 10, 20, 50, 100], [5, 3, 6, 2, 1, 3, 2], 0)
        (True, [0, 0, 0, 0, 0, 0, 0])

        >>> cambio_dinero_con_capacidad([1, 2, 5, 10, 20, 50, 100], [5, 3, 6, 2, 1, 3, 2], 127)
        (True, [0, 1, 1, 0, 1, 0, 1])
    """
    N = len(v)
    dp = [inf] * (D + 1) # dp[d] = mínimo número de billetes necesarios para alcanzar exactamente d euros
    dp[0] = 0  # Para alcanzar 0 euros no se necesita ningún billete

    # pre[d] guarda un par (i, k): el tipo de billete y la cantidad usada para llegar a d
    pre = [(-1, 0)] * (D + 1)

    # Recorremos todos los tipos de billetes
    for i in range(N):
        # Recorremos las cantidades posibles en orden descendente
        # para no reutilizar el mismo billete varias veces en una misma iteración
        for d in range(D, -1, -1):
            # Intentamos usar de 1 a c[i] billetes del tipo i
            for k in range(1, c[i] + 1):
                # Calculamos desde qué cantidad previa d - k*v[i] podríamos llegar a d
                if d - k * v[i] < 0:
                    break  # Si se sale del rango, no tiene sentido seguir probando más k

                # Verificamos si podemos mejorar la forma de alcanzar d
                # Es decir, si usar k billetes de tipo i desde d - k*v[i] reduce la cantidad total
                if dp[d - k * v[i]] + k < dp[d]:
                    dp[d] = dp[d - k * v[i]] + k  # Actualizamos con la nueva mejor solución
                    pre[d] = (i, k)  # Guardamos cómo se alcanzó esta cantidad

    # Si dp[D] sigue siendo infinito, no hay combinación válida que sume exactamente D
    if dp[D] == inf:
        return False, None

    # Si se puede alcanzar D, reconstruimos cuántos billetes de cada tipo se usaron
    usado = [0] * N  # usado[i] = cantidad de billetes del tipo i utilizados
    d = D
    while d > 0:
        i, k = pre[d]          # Obtenemos el tipo y número de billetes usados en este paso
        usado[i] += k          # Acumulamos en el resultado final
        d -= k * v[i]          # Retrocedemos a la cantidad anterior

    return True, usado  # Devolvemos éxito y la distribución de billetes usada
    




"""
# Ejemplo:
v = [1, 2, 5, 10, 20, 50, 100]  # Valores de billetes
c = [5, 3, 6, 2, 1, 3, 2]       # Cantidad disponible de cada billete
D = 127                        # Cantidad a pagar

es_posible, billetes = cambio_dinero_con_capacidad(v, c, D)

if es_posible:
    print(f"Es posible pagar {D}€. Billetes usados:")
    for i in range(len(v)):
        print(f"{billetes[i]} billetes de {v[i]}€")
else:
    print(f"No es posible pagar exactamente {D}€ con los billetes disponibles.")
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)