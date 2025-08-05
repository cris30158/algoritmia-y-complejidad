"""
Repaso PEC1 - Ejercicio 3

Hay M farolas en las posiciones y_1, y_2, …, y_M de una recta y N puntos x_1, x_2, …, x_N.
Cada farola tiene un radio de iluminación r_i, tal que la i-ésima farola ilumina puntos en 
el intervalo [y_i-r_i, y_i+r_i]. 
Se quiere encender el mínimo número de farolas tales que cada uno de los N puntos x_1, x_2, …, x_N
esté iluminado por al menos una farola. Encuentra este mínimo número.

"""

def enciende_farolas(farolas :list, puntos: list) -> list:
    """ Devuelve una lista con la posición de las farolas encendidas """

    solucion = [] # Posición de las farolas encendidas

    # Ordenamos de menor a mayor las farolas y los puntos
    farolas = sorted(farolas)
    puntos = sorted(puntos)

    while len(farolas) > 0 and len(puntos) > 0:
               
        # Si la primera farola no ilumina el primer punto no hay solución
        assert farolas[0] - R <= puntos[0], "El punto no se puede iluminar"

        # Si la siguiente farola ilumina el primer punto descartamos la primera
        if len(farolas) > 1 and farolas[1] - R <= puntos[0]:
            farolas = farolas[1:]
        else:
            # Metemos la primera farola en la solución y quitamos todos los puntos que ilumina
            solucion += [farolas[0]]
            pos = 0
            while pos < len(puntos) and puntos[pos] <= farolas[0] + R:
                pos += 1
            puntos = puntos[pos:]
            
    return solucion



R = 10
farolas = [10, 20, 30, 40, 50, 60, 70, 80, 90]
puntos = [2, 11, 48, 72, 80]

encendidas = enciende_farolas(farolas, puntos)

print(encendidas)
print(len(encendidas))
