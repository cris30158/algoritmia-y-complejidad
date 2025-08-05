import math
def encontrar_punto_mas_bajo(f, inicio, fin, epsilon):
    """
    Encuentra el punto x donde la función f(x) alcanza su mínimo en el intervalo [inicio, fin]
    utilizando búsqueda ternaria.
    
    :param f: Función que devuelve la altura en un punto x del puente.
    :param inicio: Extremo izquierdo del intervalo de búsqueda.
    :param fin: Extremo derecho del intervalo de búsqueda.
    :param epsilon: Precisión aceptada para detener la búsqueda.
    :return: Punto x donde la función alcanza su mínimo con precisión epsilon.
    """
    while (fin - inicio) > epsilon:
        m1 = inicio + (fin - inicio) / 3
        m2 = fin - (fin - inicio) / 3
        
        if f(m1) < f(m2):
            fin = m2  # El mínimo está en la parte izquierda
        else:
            inicio = m1  # El mínimo está en la parte derecha

    return (inicio + fin) / 2  # Devolvemos el punto medio del intervalo final






def altura_1(x):
    return (x - 50) ** 2 + 10  # Valle con mínimo en x = 50

def altura_2(x):
    return (x - 30) ** 2 + 5  # Valle con mínimo en x = 30


def altura_3(x):
    return math.sin(x / 10) * 50 + (x - 70) ** 2  # Valle con mínimo alrededor de x = 70

def altura_4(x):
    return math.exp((x - 40) / 10) + (x - 40) ** 2  # Valle con mínimo en x = 40

# Parámetros de búsqueda
longitud_puente = 100  # Longitud del puente en metros
epsilon = 0.01  # Precisión de 0.01 metros

# Aplicar el algoritmo a distintas funciones
punto_minimo_1 = encontrar_punto_mas_bajo(altura_1, 0, longitud_puente, epsilon)
punto_minimo_2 = encontrar_punto_mas_bajo(altura_2, 0, longitud_puente, epsilon)
punto_minimo_3 = encontrar_punto_mas_bajo(altura_3, 0, longitud_puente, epsilon)
punto_minimo_4 = encontrar_punto_mas_bajo(altura_4, 0, longitud_puente, epsilon)

print(punto_minimo_1, punto_minimo_2, punto_minimo_3, punto_minimo_4)