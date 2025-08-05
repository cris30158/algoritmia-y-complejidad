"""
Repaso PEC1 - Ejercicio 1

Un camionero conduce desde Bilbao a Málaga siguiendo una ruta dada y llevando un camión que le permite, 
con el tanque de gasolina lleno, recorrer n kilómetros sin parar. El camionero dispone de un mapa de 
carreteras que le indica las distancias entre las gasolineras que hay en su ruta. Como va con prisa, 
el camionero desea pararse a repostar el menor número de veces posible.

Diseñar un algoritmo voraz para determinar en qué gasolineras tiene que parar.

"""

def paradas_camion(gasolineras :list) -> list:
    """ Devuelve las gasolineras en las que hay que parar a repostar """

    # Gasolineras en las que vamos a parar
    solucion = [] 

    posicion = 0
    distancia_recorrida = 0
    while posicion < len(gasolineras) - 1:
        # Si no llegamos a la siguiente gasolinera
        if gasolineras[posicion + 1] - distancia_recorrida > DISTANCIA_MAX:
            # Paramos a repostar (seleccionar candidato) ¿y si tampoco llega?
            solucion += [gasolineras[posicion]]
            distancia_recorrida += gasolineras[posicion]
        # Seguimos (eliminar candidato)
        posicion += 1

    return solucion



# Distancia que recorre el camión con el deposito lleno
DISTANCIA_MAX = 500
# Km en el que se encuentran las gasolineras de la ruta
gasolineras = [38, 131, 180, 226, 277, 288, 297, 315, 410, 511, 563, 595, 602, 683, 698, 760, 824, 906]

print(f'Gasolineras: {gasolineras}')
paradas = paradas_camion(gasolineras)
print(f'Paradas: {paradas}')
