"""
Alí Babá ha conseguido entrar en la cueva de los ciento un mil ladrones, y ha llevado
consigo su camello junto con dos grandes alforjas; el problema es que se
encuentra con tanto tesoro que no sabe ni qué llevarse. Los tesoros son joyas
talladas, obras de arte, cerámica… es decir, son objetos únicos que no pueden
partirse ya que entonces su valor se reduciría a cero.
Afortunadamente los ladrones tienen todo muy bien organizado y se encuentra con
una lista de todos los tesoros que hay en la cueva, donde se refleja el peso de cada
pieza y su valor en el mercado de Damasco. Por su parte, Alí sabe la capacidad de
peso que tiene cada una de las alforjas.
Diseñar un algoritmo de Programación Dinámica que, teniendo como datos los
pesos y valor de las piezas, y la capacidad de las dos alforjas, permita obtener el
máximo beneficio que podrá sacar Alí Babá de la cueva de las maravillas.

Para 1 limite de peso. para 2 se puede hacer 2 veces y sumar, pero objetos !=...
m [i,j]=max(m[i-1,j], m [i-1,j-pi] + vi)
"""


def mochila():
    mochila1=10 #capacidad m1
    mochila2=5 #capacidad m2
    tesoros=[(1,3),(5,20),(2,9),(4,10),(6,1),(3,2),(9,10)] #peso-valor de los tesoros
    n=7 #len tesoros

    
    result = [[[0] * (mochila2 + 1) for _ in range(mochila1 + 1)] for _ in range(n + 1)]
    

    for i in range(1, n + 1):
        pi=tesoros[i-1][0]
        vi=tesoros[i-1][1]
        for j in range(mochila1+1):
            for k in range(mochila2+1):
                
                result[i][j][k]=result[i-1][j][k] #para empezar, no añadimos
                # Si no incluimos el objeto i en ninguna mochila, entonces el valor máximo será el mismo que el valor máximo con los primeros i−1 objetos y las mismas capacidades de las mochilas
                
                if(pi<=j): #si se puede añadir a la mochila 1:
                    añadir=result[i-1][j-pi][k]+vi #solucion sin añadir + el valor del objeto actual, quitandole el peso del objeto a la capacidad de la mochila donde se añada
                    result[i][j][k]=max(result[i][j][k], añadir) #max entre valor actual, sin añadir, o añadiendo

                if(pi<=k): #si se puede añadir a la mochila 1:
                    añadir=result[i-1][j][k-pi]+vi
                    result[i][j][k]=max(result[i][j][k], añadir)
                
        


    print("Matriz result:")
    for a in range(n + 1):
        for c1 in range(mochila1 + 1):
            for c2 in range(mochila2 + 1):
                print(f"result[{a}][{c1}][{c2}] = {result[a][c1][c2]}", end="\t")
            print()

            
    return result[n][mochila1][mochila2]


mochila()
















