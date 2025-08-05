"""
Repaso PEC1 - Ejercicio 5

En Acelandia el deporte nacional es el tenis... Diseñar un algoritmo
cuya función principal siga el esquema de divide y vencerás, que decida 
qué pareja de dobles debe competir en Acelandia.

"""

def elegir_pareja(jugadores :list) -> tuple:
    """ Escoge la mejor pareja de tenis """

    def _elegir_pareja(v :list, ini :int, fin :int) -> tuple: # (j1, j2)
        if ini >= fin:
            return 0, 0
        elif ini == fin - 1:
            return v[ini], v[fin]
        else:
            medio = (ini + fin) // 2
            r1 = v[medio], v[medio+1]
            r2 = _elegir_pareja(v, ini, medio)
            r3 = _elegir_pareja(v, medio + 1, fin)
            puntos = lambda tupla: tupla[0] + tupla[1]
            return max(r1, r2, r3, key=puntos)

    return _elegir_pareja(jugadores, 0, len(jugadores) - 1)

jugadores = [95, 79, 68, 68, 12, 43, 69, 97, 84, 83, 47]
print(f'Jugadores: {jugadores}')
pareja = elegir_pareja(jugadores)
print(f'Pareja: {pareja}')
