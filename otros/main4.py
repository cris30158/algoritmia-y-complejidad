import sys
import mylib4
import doctest
import ast  # Para convertir strings de listas a listas reales

def main():
    """
    Programa principal para ejecutar funciones de mylib4 desde línea de comandos.

    Uso:
    python main4.py <función> <parámetros>

    Para ejecutar los tests:
    python main4.py --test

    Ejemplos:
    python main4.py cambio_dinero_con_capacidad [1,2,5] [2,1,1] 8
    python main4.py lcs_bits [1,0,1] [0,1,0,1]
    python main4.py lcs_bits_espacio_reducido [1,0,1] [0,1,0,1]
    """
    if '--test' in sys.argv:
        doctest.testmod(mylib4, verbose=True)
        return

    if len(sys.argv) < 3:
        print("Uso: python main4.py <función> <parámetros>")
        return

    funcion = sys.argv[1]

    if funcion == "cambio_dinero_con_capacidad":
        if len(sys.argv) != 5:
            print("Uso: python main.py cambio_dinero_con_capacidad <valores> <cantidades> <D>")
            return
        v = ast.literal_eval(sys.argv[2])
        c = ast.literal_eval(sys.argv[3])
        D = int(sys.argv[4])
        exito, resultado = mylib4.cambio_dinero_con_capacidad(v, c, D)
        if exito:
            print("Es posible formar la cantidad. Billetes usados:", resultado)
        else:
            print("No es posible formar la cantidad.")

    elif funcion == "lcs_bits":
        if len(sys.argv) != 4:
            print("Uso: python main.py lcs_bits <listaA> <listaB>")
            return
        A = ast.literal_eval(sys.argv[2])
        B = ast.literal_eval(sys.argv[3])
        longitud, secuencia = mylib4.lcs_bits(A, B)
        print(f"LCS longitud = {longitud}, subsecuencia = {secuencia}")

    elif funcion == "lcs_bits_espacio_reducido":
        if len(sys.argv) != 4:
            print("Uso: python main.py lcs_bits_espacio_reducido <listaA> <listaB>")
            return
        A = ast.literal_eval(sys.argv[2])
        B = ast.literal_eval(sys.argv[3])
        longitud = mylib4.lcs_bits_espacio_reducido(A, B)
        print(f"LCS longitud = {longitud}")

    else:
        print(f"Error: función '{funcion}' no reconocida.")

if __name__ == "__main__":
    main()
