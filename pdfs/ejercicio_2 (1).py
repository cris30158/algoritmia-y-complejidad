"""
Repaso PEC1 - Ejercicio 2

Se tienen n esquiadoras de alturas H = [h_1, h_2, …, h_n] y n pares de esquíes de longitudes S = [s_1, s_2, …, s_n]. 
Diseñar un algoritmo que, usando un esquema voraz, asigne los esquíes a las esquiadoras de modo que el promedio de la 
diferencia (en valor absoluto) entre la altura de la esquiadora y la longitud de los esquíes asignados sea mínima.

"""

def asignar_esquis(alturas :list, longitudes: list) -> list:
    """ Asigna unos esquís de longitud x a una esquiadora de altura y de manera que su diferencia sea mínima """

    assert len(alturas) == len(longitudes), "Deben tener la misma longitud"

    solucion = [] # Tuplas (altura, longitud)

    # Ordenamos de menor a mayor las dos listas
    alturas = sorted(alturas)
    longitudes = sorted(longitudes)

    while len(alturas) > 0:
        # Escogemos los candidatos en orden
        pareja = (alturas[0], longitudes[0])
        # Eliminamos candidatos
        alturas = alturas[1:]
        longitudes = longitudes[1:]
        # Añadimos a la solución
        solucion += [pareja]

    return solucion


# Ejemplo
alturas = [1.52, 1.58, 1.85, 1.82, 1.84, 1.82, 1.51, 1.63, 1.9, 1.61]
longitudes = [1.35, 1.40, 1.50, 1.55, 1.60, 1.65, 1.70, 1.75, 1.80, 1.85]

# Asignamos los esquís
solucion = asignar_esquis(alturas, longitudes)

# Calculamos la diferencia
suma = 0
for altura, longitud in solucion:
    suma += abs(altura - longitud)
diferencia = suma / len(solucion)

print(f'Alturas: {alturas}')
print(f'Longitudes: {longitudes}')
print(f'Solución: {solucion}')
print(f'Diferencia: {diferencia:.3f}')
