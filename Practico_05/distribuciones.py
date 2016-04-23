# -*- coding: utf-8 -*-

import random
import math


def intervalo(inicio, longitud):
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



def normalEstadar1():
    """
    Genera una v.a. Z con distribucion Normal Estandar.
    Z ~ N(0, 1)
    """
    y = exponencial(1)
    u = random.random()
    while u >= math.exp((y - 1)**2/(-2.0)):
        y = exponencial(1)
        u = random.random()

    u = random.random()

    if u < 0.5:
        z = y
    else:
        z = -y

    return z


def normalEstadar2():
    """
    Genera una v.a. Z con distribucion Normal Estandar.
    Z ~ N(0, 1)
    """
    y1 = exponencial(1)
    y2 = exponencial(1)
    while y2 > ((y1 - 1)**2/2.0):
        y1 = exponencial(1)
        y2 = exponencial(1)

    u = random.random()

    if u < 0.5:
        z = y1
    else:
        z = -y1

    return z


def normalEstadar3():
    """
    Genera una v.a. Z con distribucion Normal Estandar ==> Z ~ N(0, 1)
    Genera una v.a. X con distribucion Exponencial ==> X ~ Exp(1).
    """
    y1 = exponencial(1)
    y2 = exponencial(1)
    while y2 - ((y1 - 1)**2/2.0) > 0:
        y1 = exponencial(1)
        y2 = exponencial(1)

    x = y2 - ((y1 - 1)**2/2.0)
    u = random.random()

    if u < 0.5:
        z = y1
    else:
        z = -y1

    return z


def normalPolar1():
    """
    Genera dos v.a. X, Y Normales Estadar Independientes, por medio del
    Metodo Polar.
    """
    u = random.random()
    r_cuadrado = exponencial(0.5)
    r = math.sqrt(r_cuadrado)
    theta = 2*math.pi*u

    x = r*math.cos(theta)
    y = r*math.sin(theta)

    return x, y


def normalPolar2():
    """
    Genera dos v.a. X, Y Normales Estadar Independientes, por medio del
    Metodo Polar haciendo uso de las Transformaciones de Box-Muller.
    """
    v1 = random.uniform(-1, 1)
    v2 = random.uniform(-1, 1)
    s = v1**2 + v2**2

    while s >= 1:
        v1 = random.uniform(-1, 1)
        v2 = random.uniform(-1, 1)
        s = v1**2 + v2**2

    x = math.sqrt((-2*math.log(s))/float(s)) * v1
    y = math.sqrt((-2*math.log(s))/float(s)) * v2

    return x, y


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
