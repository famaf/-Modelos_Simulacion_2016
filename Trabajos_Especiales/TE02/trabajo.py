# -*- coding: utf-8 -*-

from pagerank import *

ejemplo2 = ((2,), (2, 3), (1, 3, 4), (4,), (5,), (4,))
ejemplo = ((2,), (0, 2), (1,))

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
    dist_prob = P[nodo] # Distribucion de probabilidad de los vecinos
    vecino = random.randint(0, length_grafo-1) # Vecino elegido al azar

    # Buscamos un vecino al cual podamos ir
    while dist_prob[vecino] == 0:
        vecino = random.randint(0, length_grafo-1)

    return vecino


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

def distribucionEstacionaria(length_grafo, matriz_trans, pasos, simulaciones):
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


def metodoPotencias(length_grafo, P, pasos):
    """
    Calcula la Distribucion Estacionaria de un grafo segun su
    Matriz de Transicion en una cierta cantidad de pasos.
    """
    pi = np.ones(length_grafo) # Vector con todos sus elementos iguales a 1
    for _ in xrange(pasos):
        pi = power_iter_one_step(pi, P)

    potencias = redondearValores(pi, 3) # Redondeamos los valores a 3 decimales

    return potencias


def ejercicio01(grafo, simulaciones):
    n = len(grafo) # Tamaño del grafo
    P = g2p(grafo) # Matriz de Transicion
    P_mod = g2p_pagerank(grafo, 0.85) # Matriz de Transicion PageRank

    dist_est = distribucionEstacionaria(n, P, 100, simulaciones)

    potencias1 = metodoPotencias(n, P, 100)
    potencias2 = metodoPotencias(n, P_mod, 100)

    return dist_est, potencias1, potencias2

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
    tiempos = [] # Tiempos de visitas

    for nodo in xrange(n):
        tiempos.append(visitarNodo(nodo, P, n, simulaciones))

    media = sum(tiempos)/float(n)

    return tiempos, media

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
    P = g2p(grafo) # Matriz de Transicion

    pasos = 0
    for _ in xrange(simulaciones):
        pasos += tiempoCubrimiento(n, P)

    tiempo = pasos/float(simulaciones)

    return tiempo

##################################
########## Ejercicio 04 ##########
##################################

def ejercicio04():
    """
    Ejercicio 4.
    """
    grafo1 = randg(10)
    grafo2 = randg(20)
    grafo3 = randg(50)
    grafo4 = randg(100)

    print "Tiempo de cubrimiento 1 =", ejercicio03(grafo1, 1000)
    print "Tiempo de cubrimiento 2 =", ejercicio03(grafo2, 1000)
    print "Tiempo de cubrimiento 3 =", ejercicio03(grafo3, 1000)
    print "Tiempo de cubrimiento 4 =", ejercicio03(grafo4, 1000)

##################################
########## Ejercicio 05 ##########
##################################

def paginasFictias():
    """
    Ejercicio 5a.
    """
    pass


def hackearPagina():
    """
    Ejercicio 5b.
    """
    pass

###############################################################################
################################# Resultados ##################################
###############################################################################

def printEjercicio01():
    dist_est, potencias1, potencias2 = ejercicio01(G1, 10000)
    print "DE =", dist_est
    print "POT P =", potencias1
    print "POT PR =", potencias2


def printEjercicio02():
    tiempos, media = ejercicio02(G1, 1000)
    print "Distribucion de Tiempos =", tiempos
    print "Media de Tiempos =", media


def printEjercicio03():
    print "Tiempo de cubrimiento =", ejercicio03(G1, 10000)

# ejercicio04()


printEjercicio03()
