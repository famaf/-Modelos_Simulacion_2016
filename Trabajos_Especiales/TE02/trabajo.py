# -*- coding: utf-8 -*-

from pagerank import *

ejemplo2 = ((2,), (2, 3), (1, 3, 4), (4,), (5,), (4,))
ejemplo = ((2,), (0, 2), (1,))
# telefonica = ((0, 1), (1, 0))

############################
### Funciones Auxiliares ###
############################

def printCamino(lista):
    nueva_lista = []
    for valor in lista:
        nueva_lista.append(valor+1)

    return nueva_lista

def nodoAleatorio(grafo):
    n = len(grafo) # Tamaño del grafo

    nodo = random.randint(0, n-1) # Obtenemos un nodo aleatorio del grafo

    return nodo


# def gradoEntrada(matriz, nodo):
#     d_pos = sum(matriz[nodo])

#     return d_pos




#############################
### Funciones Principales ###
#############################

def caminanteAleatorio(grafo, pasos):
    """
    Ejercicio 1.
    """
    random.seed(4)
    n = len(grafo) # Tamaño del grafo

    # Obtenemos la Matriz de Transicion
    P = g2p(grafo)

    # Elegimos un nodo aleatorio del grafo
    nodo = nodoAleatorio(grafo)

    recorrido = [nodo]
    for _ in xrange(pasos-1):
        # Distribucion de probabilidad de los vecinos
        dis_prob = P[nodo]

        u = random.randint(0, n-1)

        # Busco un vecino a donde ir
        while dis_prob[u] == 0:
            u = random.randint(0, n-1)

        nodo = u
        recorrido.append(nodo)

    apariciones = []
    estacionaria = []

    for i in xrange(n):
        apariciones.append(recorrido.count(i))

    for valor in apariciones:
        estacionaria.append(valor/float(pasos))

    # print "Camino =", recorrido
    print "Camino =", printCamino(recorrido)
    print "Apariciones =", apariciones
    print "Dis Est =", estacionaria, sum(estacionaria)

    random.seed()




def tiempoCruce():
    """
    Ejercicio 2.
    """
    pass


def tiempoCubrimiento():
    """
    Ejercicio 3.
    """
    pass


def ejercicio04():
    """
    Ejercicio 4.
    """
    pass


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

caminanteAleatorio(G1, 100)