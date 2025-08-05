"""
Se tiene un sistema de billetes de distintos valores y ordenados de menor a mayor
(por ejemplo 1, 2, 5, 10, 20, 50 y 100 euros), que se representan mediante los
valores vi , con i ∈ {1, … , N} (en el caso anterior, N = 7) de manera que de cada
billete se tiene una cantidad finita, mayor o igual a cero, que se guarda en ci
(siguiendo con el ejemplo, c3 = 6 representaría que hay 6 billetes de 5 euros).
Se quiere pagar exactamente una cierta cantidad de dinero D, utilizando para ello
la menor cantidad de billetes posible. Se sabe que D ≤ ∑(de i=1 a n) ci*vi, 
pero puede que la cantidad exacta D no sea obtenible mediante los billetes disponibles.
Diseñar un algoritmo de Programación Dinámica que determine, teniendo como
datos los valores ci, vi y D:
- Si la cantidad D puede devolverse exactamente o no.
- En caso afirmativo, cuantos billetes de cada tipo forman la descomposición óptima



"""

def contarmonedas(m):
    lista = []  # Lista para almacenar las tuplas (moneda, cantidad)
    
    for moneda in m:
        # Verificamos si la moneda ya está en la lista
        for i in range(len(lista)):
            if lista[i][0] == moneda:
                lista[i] = (lista[i][0], lista[i][1] + 1)  # Incrementamos el contador de esa moneda
                break
        else:
            lista.append((moneda, 1))  # Si la moneda no está, la añadimos con contador 1
    return lista

def esta(m,v):
    r=0
    x=contarmonedas(m)
    if len(x)>0:
        for i in range (len(x)):
            print(len(x),x[i][0], "", x[i][1],"" ,v)
            if x[i][0]==v:
                r=x[i][1]
                break
    return r


def billetes(v,ctd,D):
    n=len(v)
    result = [[float('inf')] * (D + 1) for _ in range(n + 1)] 
    monedas_usadas = [[[] for _ in range(D + 1)] for _ in range(n + 1)]
    result[0][0] = 0  # 0 cambio se necesita para 0 monto
    

    for i in range(1, n + 1):
        for j in range(D + 1):
            if (j < v[i - 1] ):
                result[i][j] = result[i - 1][j]   # No se puede usar el billete i-1. dinero a conseguir<valor de la moneda actual
                monedas_usadas[i][j]=monedas_usadas[i - 1][j]
            else:             
                result[i][j] = result[i - 1][j]   # empezamos como si no fueramos a añadir ninguna moneda nueva, y en cada iteracion de ctd veremos si mejora el numero o no
                monedas_usadas[i][j]=monedas_usadas[i - 1][j]
                for k in range(1, ctd[i - 1] + 1): #para cada ctd posible de la moneda actual
                    if(j>=k*v[i-1] and ((ctd[i - 1] - esta(monedas_usadas[i][j - k*v[i - 1]], v[i-1]) )>=1)):
                        print(f"result[{i}][{j}]{ ctd[i - 1]}{esta(monedas_usadas[i][j - k*v[i - 1]], v[i-1]) }")
                        if (result[i][j]  > result[i][j - k*v[i - 1]] + k) : #si con una moneda mas (en vez del +1 de antes, +k monedas nuevas) es mejor que lo que tenemos actualmente...
                            # (ctd[i - 1]- esta(monedas_usadas[i][j - k*v[i - 1]], v[i-1]) )>0 para comprobar que no se utilicen monedas de mas al haberlas ya utilizado en el result[i][j-k*v...], y como se reutiliza ese resultado, se añaden monedas de mas
                            result[i][j]= k + result[i][j - k*v[i - 1]]
                            monedas_usadas[i][j]=monedas_usadas[i][j - k*v[i - 1]] + [v[i-1]]*k
                    else: break
                            
                            
                        

#prints de debug ########################
    for a in range(n + 1):
        for c1 in range(D + 1):
            print(f"result[{a}][{c1}] = {result[a][c1]}", end="\t")
            #print()
        print()
    print()
    print()
    print()
    for a in range(n + 1):
        for c1 in range(D + 1):
            print(f"monedas[{a}][{c1}] = {monedas_usadas[a][c1]}", end="\t")
            
        print()
###################################

    if result[n][D] == float('inf'):
        return -1, []  # No es posible hacer el cambio
    
    
    lista=contarmonedas(monedas_usadas[n][D])
    for l in lista: print(l)
    return result[n][D], monedas_usadas[n][D]  # Devuelve el número mínimo de monedas y la lista de monedas utilizadas







vi=[1,4,6]  #[1,2,5,10,20,50,100]    #ordenado!
ci=[2,2,8]  #[5,2,6,3, 4,  2, 1]
D=8
billetes(vi,ci,D)