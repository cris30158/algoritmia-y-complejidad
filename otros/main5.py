import sys
import mylib5
import doctest

def main():
    """
    Programa principal para ejecutar funciones de mylib5 según argumentos recibidos.
    
    Uso:
    python main5.py <nombre_funcion> <parametros>

    Para correr los tests:
    python main5.py --test

    Ejemplos:
    python main5.py secuencia 1151451 4
    python main5.py sustituir acabada d
    """
    if '--test' in sys.argv:
        doctest.testmod(mylib5, verbose=True)
        return

    if len(sys.argv) < 3:
        print("Uso: python main5.py <nombre_funcion> <parametros>")
        return

    funcion = sys.argv[1]

    if funcion == "secuencia":
        if len(sys.argv) != 4:
            print("Uso: python main.py secuencia <dato> <N>")
            return
        dato = sys.argv[2]
        N = int(sys.argv[3])
        resultados = mylib5.secuencia(dato, N, 0, "", [])
        print(f"Secuencias de longitud {N} en '{dato}':")
        print(sorted(resultados))

    elif funcion == "sustituir":
        if len(sys.argv) != 4:
            print("Uso: python main.py sustituir <texto> <final>")
            return
        texto = sys.argv[2]
        final = sys.argv[3]

        # Tabla de sustitución de ejemplo, igual a la usada en mylib5
        M = {
            'a': {'a': 'b', 'b': 'b', 'c': 'a', 'd': 'd'},
            'b': {'a': 'c', 'b': 'a', 'c': 'd', 'd': 'a'},
            'c': {'a': 'b', 'b': 'a', 'c': 'c', 'd': 'c'},
            'd': {'a': 'd', 'b': 'c', 'c': 'd', 'd': 'b'}
        }

        exito, camino = mylib5.sustituir(texto, final, M)
        if exito:
            print("Ruta encontrada:")
            for paso in camino:
                print(paso)
        else:
            print("No es posible reducir al carácter final.")

    else:
        print(f"Error: función '{funcion}' no reconocida. Usa 'secuencia' o 'sustituir'.")

if __name__ == "__main__":
    main()