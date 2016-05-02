# -*- coding: utf-8 -*-

import random
import math


INFINITO = float("inf")


def exponencial(lamda):
    """
    Genera una v.a. X con distribucion Exponencial de parametro lamda.
    X ~ Exp(lamda).
    """
    u = random.random()
    x = -(1/float(lamda))*math.log(u)

    return x


def devolverLambda(esperanza):
    """
    Devuelve el lambda correspondiente segun la esperanza ingresada.
    """
    lamda = 1/float(esperanza)

    return lamda


def lavadero1(N, S, Tf, Tr):
    """
    N = Lavadoras en servicio
    S = Lavadoras de repuesto

    Tf = Tiempo medio hasta fallar
    Tr = Tiempo medio de reparacion
    """

    lamda_falla = devolverLambda(Tf)
    lamda_reparacion = devolverLambda(Tr)

    T = 0 # Tiempo en que falla
    t = 0 # Variable de tiempo
    r = 0 # Variable de estado del sistema (r: numero de maquina rotas en el instante t)

    t_estrella = INFINITO # Tiempo de maquinas en reparacion

    aleatorio = [] # Lista de variables aleatorias

    # Generamos N tiempos de falla (uno para cada maquina)
    for _ in xrange(N):
        F = exponencial(lamda_falla) # Tiempo hasta Fallar
        aleatorio.append(F)

    while True:
        aleatorio.append(t_estrella)
        aleatorio.sort() # Ordenamos la lista de variables aleatorias

        if t_estrella <= aleatorio[0]:
            t = t_estrella
            if r == 0:
                t_estrella = INFINITO
            if r > 0:
                Y = exponencial(lamda_reparacion)
                t_estrella = t + Y

        elif aleatorio[0] < t_estrella:
            t = aleatorio[0]
            if r == S:
                T = t
                break
            else:
                X = exponencial(lamda_falla)
                aleatorio[0] = t + X
                aleatorio.sort()

                if r == 0:
                    Y = exponencial(lamda_reparacion)
                    t_estrella = t + Y
                    r += 1
                else:
                    r += 1

    return T


def lavadero2(N, S, Tf, Tr):
    """
    N = Lavadoras en servicio
    S = Lavadoras de repuesto

    Tf = Tiempo medio hasta fallar
    Tr = Tiempo medio de reparacion
    """

    lamda_falla = devolverLambda(Tf)
    lamda_reparacion = devolverLambda(Tr)

    T = 0 # Tiempo en que falla
    t = 0 # Variable de tiempo
    r = 0 # Variable de estado del sistema (r: numero de maquina rotas en el instante t)

    t_estrella = INFINITO # Tiempo de maquinas en reparacion

    aleatorio = [] # Lista de variables aleatorias

    # Generamos N tiempos de falla (uno para cada maquina)
    for _ in xrange(N):
        F = exponencial(lamda_falla) # Tiempo hasta Fallar
        aleatorio.append(F)

    while True:
        if aleatorio[0] < t_estrella:
            t = aleatorio[0]
            r += 1
            # Si hay mas de S maquinas descompuestas (no hay repuestos)
            if r == S+1:
                T = t
                break
            elif r < S+1:
                X = exponencial(lamda_falla)
                aleatorio.pop(0)
                aleatorio.append(t+X)
                aleatorio.sort()
                if r == 1:
                    Y = exponencial(lamda_reparacion)
                    t_estrella = t + Y

        elif t_estrella <= aleatorio[0]:
            t = t_estrella
            r -= 1
            if r > 0:
                Y = exponencial(lamda_reparacion)
                t_estrella = t + Y
            if r == 0:
                t_estrella = INFINITO

    return T


def esperanza(n):
    """
    Esperanza con Metodo de Maximo de Uniformes.
    """
    a = 0
    for _ in xrange(n):
        a += lavadero2(5, 2, 1, 1/8.0)

    return a/float(n)


for n in [100, 1000, 10000, 100000]:
    print "n =", n, "--> E(X) =", esperanza(n)
