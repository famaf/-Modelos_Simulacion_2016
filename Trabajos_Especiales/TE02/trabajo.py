# -*- coding: utf-8 -*-

from pagerank import *
import matplotlib.pyplot as plt

# ejemplo2 = ((2,), (2, 3), (1, 3, 4), (4,), (5,), (4,))
# ejemplo = ((2,), (0, 2), (1,))

###############################################################################
############################ Funciones Auxiliares #############################
###############################################################################

def nodoAleatorio(n):
    """
    Devuelve un nodo aleatorio de una lista de vertices.
    n = Longitud de la lista de vertices
    """
    return random.randint(0, n-1)


def elegirVecino(nodo, P, length_grafo):
    """
    Elige un vecino del nodo ingresado, segun su Matriz de Transicion.
    """
    dist_vecinos = P[nodo]
    u = random.random()

    x = 0 # Vecino que sera elegido segun la acumulada
    F = dist_vecinos[x] # Distribucion acumulada

    # Mientras el aleatorio sea mayor que la acumulada, busco otro nodo
    while u >= F:
        x += 1
        F += dist_vecinos[x]

    return x


def redondearValores(lista, decimales):
    """
    Redondea los elementos de una lista de valores a una cierta cantidad de
    decimales.
    """
    result = [round(valor, decimales) for valor in lista]

    return result

###############################################################################
############################ Funciones Principales ############################
###############################################################################


##################################
########## Ejercicio 01 ##########
##################################

def distribucionEstacionaria01(length_grafo, matriz_trans, pasos, simulaciones):
    """
    Calcula la Distribucion Estacionaria por medio de simulacion.
    """
    apariciones = [0 for _ in xrange(length_grafo)]

    for _ in xrange(simulaciones):
        nodo = nodoAleatorio(length_grafo)

        for _ in xrange(pasos-1):
            vecino = elegirVecino(nodo, matriz_trans, length_grafo)
            nodo = vecino

        apariciones[nodo] += 1

    dist_est = [(valor/float(simulaciones)) for valor in apariciones]
    dist_est = redondearValores(dist_est, 3)

    return dist_est


def distribucionEstacionaria02(length_grafo, matriz_trans, pasos, simulaciones):
    """
    Calcula la Distribucion Estacionaria por medio de simulacion.
    """
    apariciones = [0 for _ in xrange(length_grafo)]

    for _ in xrange(simulaciones):
        nodo = nodoAleatorio(length_grafo)
        camino = [nodo]
        for _ in xrange(pasos-1):
            vecino = elegirVecino(nodo, matriz_trans, length_grafo)
            nodo = vecino
            camino.append(nodo)

        for i in xrange(length_grafo):
            apariciones[i] += camino.count(i)

    apariciones_promedio = [(valor/float(simulaciones)) for valor in apariciones]

    dist_est = [(valor/float(pasos)) for valor in apariciones_promedio]
    dist_est = redondearValores(dist_est, 3)

    return dist_est


def metodoPotencias(length_grafo, matriz_trans, pasos):
    """
    Calcula la Distribucion Estacionaria de un grafo segun su
    Matriz de Transicion en una cierta cantidad de pasos.
    """
    pi = np.ones(length_grafo) # Vector con todos sus elementos iguales a 1
    for _ in xrange(pasos):
        pi = power_iter_one_step(pi, matriz_trans)

    potencias = redondearValores(pi, 3) # Redondeamos los valores a 3 decimales

    return potencias


def ejercicio01(grafo, simulaciones):
    n = len(grafo) # Tamaño del grafo
    P = g2p(grafo) # Matriz de Transicion
    P_mod = g2p_pagerank(grafo, 0.85) # Matriz de Transicion PageRank

    dist_est1 = distribucionEstacionaria01(n, P, 100, simulaciones)
    dist_est2 = distribucionEstacionaria01(n, P_mod, 100, simulaciones)

    potencias1 = metodoPotencias(n, P, 100)
    potencias2 = metodoPotencias(n, P_mod, 100)

    return dist_est1, dist_est2, potencias1, potencias2

##################################
########## Ejercicio 02 ##########
##################################

def visitarNodo(nodo, matriz_trans, length_grafo, simulaciones):
    """
    Cantidad de pasos necesarios para volver a visitas un nodo dado.
    """
    t = 0
    for _ in xrange(simulaciones):
        nodo_inicial = nodo
        while True:
            vecino = elegirVecino(nodo_inicial, matriz_trans, length_grafo)
            t += 1

            if nodo == vecino:
                break

            nodo_inicial = vecino

    pasos = t/float(simulaciones)

    return pasos


def ejercicio02(grafo, simulaciones):
    """
    Ejercicio 2.
    """
    n = len(grafo) # Tamaño del grafo
    P = g2p(grafo) # Matriz de transicion
    P_mod = g2p_pagerank(grafo, 0.85) # Matriz de transicion
    tiempos1 = [] # Tiempos de visitas con P original
    tiempos2 = [] # Tiempos de visitas con P PageRank

    for nodo in xrange(n):
        tiempos1.append(visitarNodo(nodo, P, n, simulaciones))
        tiempos2.append(visitarNodo(nodo, P_mod, n, simulaciones))

    media1 = sum(tiempos1)/float(n)
    media2 = sum(tiempos2)/float(n)

    tiempos1 = redondearValores(tiempos1, 3)
    tiempos2 = redondearValores(tiempos2, 3)

    return tiempos1, tiempos2, media1, media2

##################################
########## Ejercicio 03 ##########
##################################

def tiempoCubrimiento(length_grafo, matriz_trans):
    """
    Cantidad de pasos de un caminante aleatorio para visitar todos los nodos
    de un grafo al menos una vez.
    """
    nodo = nodoAleatorio(length_grafo) # Elegimos un nodo aleatorio del grafo
    nodos_vistos = [nodo] # nodos por el caminante paso
    pasos = 1

    # Corremos el caminante aleatorio hasta ver todos los nodos
    while len(nodos_vistos) < length_grafo:
        # Elegimos un vecino al cual poder ir
        nodo = elegirVecino(nodo, matriz_trans, length_grafo)
        pasos += 1

        # Si el nodo en el estoy no lo recorri entonces lo agrego al ca
        if nodo not in nodos_vistos:
            nodos_vistos.append(nodo)

    return pasos


def ejercicio03(grafo, simulaciones):
    """
    Ejercicio 3.
    """
    n = len(grafo) # Tamaño del grafo
    alfas = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.85, 0.9, 0.99]
    P_s = [g2p_pagerank(grafo, alfa) for alfa in alfas] # Matrices de Transicion


    pasos1 = 0
    pasos2 = 0
    pasos3 = 0
    pasos4 = 0
    pasos5 = 0
    pasos6 = 0
    pasos7 = 0
    pasos8 = 0
    pasos9 = 0
    pasos10 = 0
    pasos11 = 0
    for _ in xrange(simulaciones):
        pasos1 += tiempoCubrimiento(n, P_s[0])
        pasos2 += tiempoCubrimiento(n, P_s[1])
        pasos3 += tiempoCubrimiento(n, P_s[2])
        pasos4 += tiempoCubrimiento(n, P_s[3])
        pasos5 += tiempoCubrimiento(n, P_s[4])
        pasos6 += tiempoCubrimiento(n, P_s[5])
        pasos7 += tiempoCubrimiento(n, P_s[6])
        pasos8 += tiempoCubrimiento(n, P_s[7])
        pasos9 += tiempoCubrimiento(n, P_s[8])
        pasos10 += tiempoCubrimiento(n, P_s[9])
        pasos11 += tiempoCubrimiento(n, P_s[10])

    tiempo1 = pasos1/float(simulaciones)
    tiempo2 = pasos2/float(simulaciones)
    tiempo3 = pasos3/float(simulaciones)
    tiempo4 = pasos4/float(simulaciones)
    tiempo5 = pasos5/float(simulaciones)
    tiempo6 = pasos6/float(simulaciones)
    tiempo7 = pasos7/float(simulaciones)
    tiempo8 = pasos8/float(simulaciones)
    tiempo9 = pasos9/float(simulaciones)
    tiempo10 = pasos10/float(simulaciones)
    tiempo11 = pasos11/float(simulaciones)

    tiempo = [tiempo1, tiempo2, tiempo3, tiempo4, tiempo5, tiempo6, tiempo7, tiempo8, tiempo9, tiempo10, tiempo11]

    return tiempo


def ejercicio03prima(grafo, simulaciones):
    """
    Ejercicio 3.
    """
    n = len(grafo) # Tamaño del grafo
    P_s = g2p_pagerank(grafo, 0.85) # Matrices de Transicion


    pasos = 0
    for _ in xrange(simulaciones):
        pasos += tiempoCubrimiento(n, P_s)

    tiempo = pasos/float(simulaciones)

    return tiempo


def testGrafo(grafo, simulaciones):
    n = len(grafo)
    P = g2p(grafo)
    pasos = 0
    for _ in xrange(simulaciones):
        pasos += tiempoCubrimiento(n, P)

    return pasos/float(simulaciones)

##################################
########## Ejercicio 04 ##########
##################################

def ejercicio04():
    """
    Ejercicio 4.
    """
    grafo1 = randg(5)
    grafo2 = randg(10)
    grafo3 = randg(30)
    grafo4 = randg(50)
    grafo5 = randg(75)
    grafo6 = randg(100)

    print("Nodo: 5 --> Tiempo de cubrimiento =", ejercicio03prima(grafo1, 1000))
    print("Nodo: 10 --> Tiempo de cubrimiento =", ejercicio03prima(grafo2, 1000))
    print("Nodo: 30 --> Tiempo de cubrimiento =", ejercicio03prima(grafo3, 1000))
    print("Nodo: 50 --> Tiempo de cubrimiento =", ejercicio03prima(grafo4, 1000))
    print("Nodo: 75 --> Tiempo de cubrimiento =", ejercicio03prima(grafo5, 1000))
    print("Nodo: 100 --> Tiempo de cubrimiento =", ejercicio03prima(grafo6, 1000))

##################################
########## Ejercicio 05 ##########
##################################

####################
### Estrategia A ###
####################

def agregarPagina(grafo, page_target=None):
    """
    Agrega nodos al grafo con vinculo a la pagina pasada como objetivo.
    """
    l = list(grafo) # Pasamos el grafo a una lista

    if page_target != None:
        l.append((page_target,))
    else:
        l.append(())

    t = tuple(l)

    return t


def paginasFictias(grafo, K):
    """
    Ejercicio 5a.
    K = Cantidad de paginas fictias que se agregan al grafo.
    """
    n = len(grafo) # Tamaño del grafo

    grafo = agregarPagina(grafo) # Agrego mi pagina S (vacia) a la web

    # Agrego K paginas a la web que apuntan a la pagina n+K
    for _ in xrange(0, K):
        grafo = agregarPagina(grafo, n)

    N = n + K + 1

    P_mod = g2p_pagerank(grafo, 0.85) # Matriz de transicion con PageRank

    dist_est = distribucionEstacionaria01(N, P_mod, 100, 1000)
    potencias = metodoPotencias(N, P_mod, 100)

    ranking1 = dist_est[n]
    ranking2 = potencias[n]

    return ranking1, ranking2

####################
### Estrategia B ###
####################

def modificarPagina(grafo, page, link):
    pass



def hackearPaginas(grafo, K):
    """
    Ejercicio 5b.
    """
    n = len(grafo)

    grafo = agregarPagina(grafo)
    grafo = list(grafo)

    hackeadas = []
    for _ in xrange(K):
        nodo = nodoAleatorio(n)
        
        while nodo in hackeadas:
            nodo = nodoAleatorio(n)

        hackeadas.append(nodo)

        grafo[nodo] = list(grafo[nodo])
        grafo[nodo].append(n)
        grafo[nodo] = tuple(grafo[nodo])

    grafo = tuple(grafo)

    N = n + 1

    P_mod = g2p_pagerank(grafo, 0.85) # Matriz de transicion con PageRank

    dist_est = distribucionEstacionaria01(N, P_mod, 100, 1000)
    potencias = metodoPotencias(N, P_mod, 100)

    ranking1 = dist_est[n]
    ranking2 = potencias[n]

    return ranking1, ranking2

###############################################################################
################################# Resultados ##################################
###############################################################################


def printEjercicio01():
    simulaciones = 1000
    dist_est1, dist_est2, potencias1, potencias2 = ejercicio01(G1, simulaciones)
    print("### Ejercicio 01 --> Sobre G1 ###")
    print("Simulaciones =", str(simulaciones))
    print("Caminante P-Original =", dist_est1)
    print("Potencias P-Original =", potencias1)
    print("Caminante P-Modificada =", dist_est2)
    print("Potencias P-Modificada =", potencias2)
    dist_est1, dist_est2, potencias1, potencias2 = ejercicio01(G2, simulaciones)
    print("### Ejercicio 01 --> Sobre G2 ###")
    print("Simulaciones =", str(simulaciones))
    print("Caminante P-Original =", dist_est1)
    print("Potencias P-Original =", potencias1)
    print("Caminante P-Modificada =", dist_est2)
    print("Potencias P-Modificada =", potencias2)


def printEjercicio02():
    simulaciones = 100
    tiempos1, tiempos2, media1, media2 = ejercicio02(G1, simulaciones)
    tiempos3, tiempos4, media3, media4 = ejercicio02(G2, simulaciones)
    print("### Ejercicio 02 ###")
    print("Simulaciones =", str(simulaciones))
    print("P-Original --> Distribucion de Tiempos G1 =", tiempos1)
    print("P-Original --> Media de Tiempos G1 =", media1)
    print("P-Modificada --> Distribucion de Tiempos G1 =", tiempos2)
    print("P-Modificada --> Media de Tiempos G1 =", media2)
    # print("Distribucion de Tiempos G2 =", tiempos2)
    print("P-Original --> Media de Tiempos G2 =", media3)
    print("P-Modificada --> Media de Tiempos G2 =", media4)


def printEjercicio03():
    simulaciones = 1000
    alfas = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.85, 0.9, 0.99]
    print("### Ejercicio 03 ###")
    print("Simulaciones =", str(simulaciones))
    print("Alfas =", alfas)
    print("Tiempo de cubrimiento G1 =", ejercicio03(G1, simulaciones))
    print("Tiempo de cubrimiento G2 =", ejercicio03(G2, simulaciones))
    print("Con P original")
    print("Tiempo de cubrimiento G1 =", testGrafo(G1, simulaciones))
    print("Tiempo de cubrimiento G2 =", testGrafo(G2, simulaciones))


# def printEjercicio05():
#     K = [10, 25, 50, 75, 100]
#     for k in K:
#         ranking1, ranking2 = paginasFictias(G2, k)
#         ranking3, ranking4 = hackearPaginas(G2, k)
#         print("### Ejercicio 05 --> Sobre G2 ###")
#         print("Simulaciones = 1000 ----- Pasos = 100")
#         print("########## Agregar", str(k), "Paginas ##########")
#         print("Dist Est --> Ranking Pagina S =", ranking1)
#         print("Met Pote --> Ranking Pagina S =", ranking2)
#         print("########## Hackear", str(k), "Paginas ##########")
#         print("Dist Est --> Ranking Pagina S =", ranking3)
#         print("Met Pote --> Ranking Pagina S =", ranking4)


def printEjercicio05():
    K = [1, 3, 5, 7, 10]
    print("### Ejercicio 05 --> Sobre G1 ###")
    print("Simulaciones = 1000 ----- Pasos = 100")
    for k in K:
        ranking1, a = paginasFictias(G1, k)
        ranking2, b = hackearPaginas(G1, k)
        print("########## Agregar", str(k), "Paginas ##########")
        print("Ranking Pagina S =", ranking1)
        print("########## Hackear", str(k), "Paginas ##########")
        print("Ranking Pagina S =", ranking2)


# print("")
# printEjercicio01()
# print("")
# printEjercicio02()
# print("")
# printEjercicio03()
# print("")
# ejercicio04()
# print("")
# printEjercicio05()
# print("")


###############################################################################
################################# Histogramas #################################
###############################################################################

def histograma01():
    dist_est1, dist_est2, potencias1, potencias2 = ejercicio01(G1, 10000)
    plt.title("Distribuciones Estacionarias sobre G1")
    plt.ylabel("Probabilidad")
    plt.xlabel("Numero de nodo")
    plt.grid(True)
    plt.plot(dist_est1, color="b", linestyle="-", label="Metodo 1 - MTO")
    plt.plot(potencias1, color="r", linestyle="--", label="Metodo 2 - MTO")
    plt.plot(dist_est2, color="y", linestyle="-", label="Metodo 1 - MTM")
    plt.plot(potencias2, color="g", linestyle="--", label="Metodo 2 - MTM")
    plt.legend()
    plt.show()


def histograma02_G1():
    tiemposO, tiemposM, mediaO, mediaM = ejercicio02(G1, 1000)

    plt.title("Tiempos de Cruce sobre G1")
    plt.xlabel("Numero de nodo")
    plt.ylabel("Tiempo de cruce [Pasos]")
    plt.grid(True)
    bins = np.linspace(0, max(tiemposO), 20)
    plt.text(2, 96, "Media de Tiempos con MTO = " + str(mediaO))
    plt.text(2, 88, "Media de Tiempos con MTM = " + str(mediaM))
    plt.ylim(0, 140)
    plt.plot(tiemposO, color="b", label="Matriz de Transicion Original")
    plt.plot(tiemposM, color="r", label="Matriz de Transicion Modificada")
    plt.legend()
    plt.show()


def histograma02_G2():
    tiemposO, tiemposM, mediaO, mediaM = ejercicio02(G2, 100)

    plt.title("Histograma de Tiempos de Cruce sobre G2")
    plt.xlabel("Tiempo de Cruce [Pasos]")
    plt.ylabel("Estimacion de Probabilidad")
    plt.grid(True)
    bins = np.linspace(0, max(tiemposO), 20)
    plt.hist([tiemposO, tiemposM], bins=bins, normed=True, color=["g", "r"], label=["Matriz de Transicion Original", "Matriz de Transicion Modificada"])
    plt.legend()
    plt.show()


def histograma03(number):
    alfas = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.85, 0.9, 0.99]
    datos1 = [30.085, 30.599, 31.345, 32.985, 35.268, 36.955, 41.33, 49.072, 55.559, 64.563, 101.207]
    datos2 = [523.399, 519.633, 522.228, 529.887, 522.984, 524.198, 535.352, 539.09, 543.288, 544.125, 548.871]

    if number == 1:
        plt.title("Tiempos de Cubrimiento sobre G1")
    elif number == 2:
        plt.title("Tiempos de Cubrimiento sobre G2")
    else:
        print("ERROR")
    plt.ylabel("Tiempo de Cubrimiento [Pasos]")
    plt.xlabel("Alfa")
    plt.grid(True)
    if number == 1:
        plt.ylim(0, 130)
        plt.plot(alfas, [107.641 for _ in xrange(len(datos1))], color="b", label="Tiempo de Cubrimiento con MTO")
        plt.plot(alfas, datos1, color="r", label="Tiempo de Cubrimiento con MTM")
    elif number == 2:
        plt.ylim(515, 560)
        plt.plot(alfas, [548.714 for _ in xrange(len(datos1))], color="b", label="Tiempo de Cubrimiento con MTO")
        plt.plot(alfas, datos2, color="r", label="Tiempo de Cubrimiento con MTM")
    else:
        print("ERROR")
    plt.legend()
    plt.show()


def histograma04():
    nodos = [5, 10, 30, 50, 75, 100]
    datos = [11.813, 31.742, 159.51, 250.54, 402.357, 558.348]

    plt.title("Tiempos de Cubrimiento para distintos Grafos")
    plt.ylabel("Tiempo de Cubrimiento [Pasos]")
    plt.xlabel("Cantidad de Nodos")
    plt.grid(True)
    plt.plot(nodos, datos)
    plt.show()


def histograma05():
    K = [1, 3, 5, 7, 10]
    rankingA = [0.023, 0.049, 0.072, 0.09, 0.112]
    rankingB = [0.036, 0.073, 0.12, 0.167, 0.205]

    plt.title("Estrategias A y B sobre G1")
    plt.xlabel("Paginas Agregadas")
    plt.ylabel("Probabilidad de Visita")
    plt.grid(True)
    plt.plot(K, rankingA, color="r", label="Estrategia A")
    plt.plot(K, rankingB, color="b", label="Estrategia B")
    plt.legend()
    plt.show()


def histograma06():
    K = [10, 25, 50, 75, 100]
    rankingA = [0.014, 0.031, 0.057, 0.08, 0.101]
    rankingB = [0.005, 0.008, 0.017, 0.021, 0.028]

    plt.title("Estrategias A y B sobre G2")
    plt.xlabel("Paginas Agregadas")
    plt.ylabel("Probabilidad de Visita")
    plt.grid(True)
    plt.plot(K, rankingA, color="r", label="Estrategia A")
    plt.plot(K, rankingB, color="b", label="Estrategia B")
    plt.legend()
    plt.show()

# histograma03(2)
# histograma05()
# histograma06()
# histograma05(27)
