"""
¡Llega el torneo de EscobaBall, y más salvaje que nunca! Este año, en el Colegio de
Magia y Hechicería han decidido que los cuatro equipos (Grifos, Serpientes,
Cuervos y Tejones) jueguen en cada partido todos contra todos, y como siempre
que ningún partido termine en empate. El torneo acabará cuando un mismo equipo
haya ganado un total de N partidos (no necesariamente consecutivos).
El aprendiz de mago Javi Potter quiere apostar algo de dinero por su equipo, los
Grifos, así que se dirige a la casa de apuestas de los gnomos para ver cuánto le
darían si gana su equipo: sus ganancias serían iguales a la cantidad de dinero
apostado dividido por la probabilidad de que el equipo gane el campeonato (por
ejemplo, si los Grifos tuviesen un 50% de ganar el campeonato y Javi apuesta 10
monedas de oro, sus posibles ganancias serían 10 ∕ 0.5 = 20 monedas de oro; si
tuviesen un 20% de ganar, el beneficio posible sería de 10 ∕ 0.2 = 50 monedas de
oro (una mayor recompensa al ser más difícil de conseguir).
Para obtener esta probabilidad, la casa de apuestas tiene un Valor de Calidad
asignado a cada equipo (que mide la habilidad de los jugadores, su motivación,
etc., y que es un valor fijo para el equipo e independiente del partido que esté
jugando) de manera que cuanto mayor es el VC de un equipo, más probabilidades
tiene de ganar un partido. Por ejemplo, si los cuatro equipos tuviesen igual VC todos
tendrían un 25% de ganar un partido. Si tres equipos tuviesen el mismo VC y el
cuarto equipo tuviese el doble de esa cantidad, los primeros tendrían un 20% y el
último un 40%. Como los partidos no pueden terminar en empate, la suma de las
probabilidades siempre es el 100%.
Teniendo como datos los Valores de Calidad de los equipos, la cantidad de partidos
N que debe ganar un equipo para conseguir ganar el torneo, y el dinero D apostado
por Javi Potter, obtener cuáles serían las ganancias si ganasen los Grifos
"""

def P (i,j):  #formato base
    p=0.6
    q=1-p
    if (i==0):
        return 1
    elif (j==0): 
        return 0
    else:
        return p*P(i-1,j)+q*P(i,j-1)
    
print(P(10,10))

def torneo(N, g, s, c, t, probG, probS, probC, probT, memo):
    if g == N:
        return 1
    if s == N or c == N or t == N:
        return 0
    if (g, s, c, t) in memo:
        return memo[(g, s, c, t)]
    
    res = (
        probG * torneo(N, g + 1, s, c, t, probG, probS, probC, probT, memo) +
        probS * torneo(N, g, s + 1, c, t, probG, probS, probC, probT, memo) +
        probC * torneo(N, g, s, c + 1, t, probG, probS, probC, probT, memo) +
        probT * torneo(N, g, s, c, t + 1, probG, probS, probC, probT, memo)
    )
    memo[(g, s, c, t)] = res
    return res

def apuestas(vcg, vcs, vcc, vct):
    suma = vcg + vcs + vcc + vct
    return vcg/suma, vcs/suma, vcc/suma, vct/suma

def resultado(dineroApostado, vcg, vcs, vcc, vct, N):
    probG, probS, probC, probT = apuestas(vcg, vcs, vcc, vct)
    memo = dict()
    probFinalG = torneo(N, 0, 0, 0, 0, probG, probS, probC, probT, memo)
    gananciasG = dineroApostado / probFinalG if probFinalG > 0 else float('inf')
    print("Probabilidad de que ganen los Grifos:", probFinalG)
    print("Ganancia si ganan (con", dineroApostado, "monedas):", gananciasG)
    return probFinalG, gananciasG

# vc_grifos = 2
# vc_serpientes = 1
# vc_cuervos = 1
# vc_tejones = 1
# N = 3  # Número de victorias necesarias
# dineroApostado = 10  # Dinero apostado

# vc_grifos = 2   # Grifos
# vc_serpientes = 1   # Serpientes
# vc_cuervos = 1   # Cuervos
# vc_tejones = 1   # Tejones
# N = 1     # Solo 1 victoria necesaria
# dineroApostado = 10
#resultado final: 0.4    0.2    0.2    0.2    ganancias:  25.0  monedas    prob final:  0.4

# vc_grifos = 1
# vc_serpientes = 1
# vc_cuervos = 1
# vc_tejones = 1
# N = 2
# dineroApostado = 10
#ahora la prob es aprox. porque N>1, puede ganar de varias formas

vc_grifos = 1
vc_serpientes = 2
vc_cuervos = 2
vc_tejones = 1
N = 2
dineroApostado = 10

resultado(dineroApostado, vc_grifos, vc_serpientes, vc_cuervos, vc_tejones, N)


