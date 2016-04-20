# -*- coding: utf-8 -*-

import random
import math


def intervalo(longitud, inicio):
    """
    Devuelve un numero aleatorio entre [inicio, inicio+longitud-1].
    """
    u = random.random()

    return math.floor(longitud*u) + inicio


def raizGeneral(raiz, radicando):
    """
    Calcula la raiz N-esima de un numero.
    """
    return radicando**(1.0/raiz)


def exponencial(lamda):
    """
    Genera una v.a. X con distribucion Exponencial de parametro lamda.
    X ~ Exp(lamda).
    """
    u = random.random()
    x = -(1/float(lamda))*math.log(u)

    return x


def maxUniformes(n):
    """
    Calcula el maximo de n Uniformes en (0, 1).
    """
    maximo = 0
    for _ in xrange(n):
        u = random.random()
        maximo = max(maximo, u)

    return maximo


def minUniformes(n):
    """
    Calcula el minimo de n Uniformes en (0, 1).
    """
    minimo = 1
    for _ in xrange(n):
        u = random.random()
        minimo = min(minimo, u)

    return minimo


def procesoPoissonH(lamda, tiempo):
    """
    Genera las primeras T (tiempo) unidades de tiempo de un
    Proceso de Poisson Homogeneo con parametro lambda.
    """
    t = 0 # tiempo transcurrido
    i = 0 # N° de eventos ocurridos hasta t
    s = [] # S[i]: tiempo del evento mas reciente
    while True:
        u = random.random()

        if t - (math.log(u)/float(lamda)) > tiempo:
            break
        else:
            t -= (math.log(u)/float(lamda))
            i += 1
            s.append(t)

    return i


def adelgazamiento(lamda, lamda_t, tiempo):
    """
    Generacion de eventos en el intervalo usando Algoritmo de Adelgazamiento
    para Proceso de Poisson no Homogeneo.
    """
    t = 0
    i = 0 # N° de eventos
    s = [] # s[1], s[2], ... ==> tiempos de eventos
    while True:
        u = random.random()

        if t - (math.log(u)/float(lamda)) > tiempo:
            break
        else:
            t -= (math.log(u)/float(lamda))
            v = random.random()

            if v < (lamda_t(t)/float(lamda)):
                i += 1
                s.append(t)

    return i