# -*- coding: utf-8 -*-

import random
import math


INFINITO = float("inf") # Constante Infinito


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

    lavadoras = [] # Lista de variables aleatorias

    # Generamos N tiempos de falla (uno para cada maquina)
    for _ in xrange(N):
        F = exponencial(lamda_falla) # Tiempo hasta Fallar
        lavadoras.append(F)

    while True:
        lavadoras.append(t_estrella)
        lavadoras.sort() # Ordenamos la lista de variables aleatorias

        if t_estrella <= lavadoras[0]:
            t = t_estrella
            if r == 0:
                t_estrella = INFINITO
            if r > 0:
                Y = exponencial(lamda_reparacion)
                t_estrella = t + Y

        elif lavadoras[0] < t_estrella:
            t = lavadoras[0]
            if r == S:
                T = t
                break
            else:
                X = exponencial(lamda_falla)
                lavadoras[0] = t + X
                lavadoras.sort()

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

    lamda_falla = devolverLambda(Tf) # Lambda de los tiempos de falla
    lamda_reparacion = devolverLambda(Tr) # Lambda de los tiempos de reparacion

    T = 0 # Tiempo en que falla
    t = 0 # Variable de tiempo
    r = 0 # Variable de estado del sistema (r: numero de maquina rotas en el instante t)

    t_estrella = INFINITO # Tiempo en el que la Lavadora en reparacion vuelve a funcionar

    lavadoras = [] # Lista de tiempos de falla de las Lavadoras

    # Generamos N tiempos de falla (uno para cada maquina)
    for _ in xrange(N):
        F = exponencial(lamda_falla) # Tiempo hasta Fallar
        lavadoras.append(F)

    while True:
        # Lavadora falla antes de que se repare alguna
        if lavadoras[0] < t_estrella:
            t = lavadoras[0]
            r += 1 # Se rompio una Lavadora
            # Si hay mas de S Lavadoras descompuestas (no hay repuestos)
            if r == S+1:
                T = t
                break
            elif r < S+1:
                X = exponencial(lamda_falla) # Tiempo hasta fallar de la lavadora de repuesto
                lavadoras.pop(0)
                lavadoras.append(t+X)
            elif r == 1:
                Y = exponencial(lamda_reparacion) # Lavadora entra en reparacion
                t_estrella = t + Y
        
        # Lavadora que estaba en reparacion esta disponible
        elif t_estrella <= lavadoras[0]:
            t = t_estrella
            r -= 1
            # Hay maquinas para Reparar
            if r > 0:
                Y = exponencial(lamda_reparacion) # Tiempo de reparacion de la Lavadora para reparar
                t_estrella = t + Y
            # No hay maquinas que Reparar
            elif r == 0:
                t_estrella = INFINITO # Tiempo de

    return T


def esperanzaYVarianza(n):
    """
    Esperanza y Varianza del Tiempo de Fallo del Sistema del Lavadero.
    """
    suma1 = 0
    suma2 = 0

    for _ in xrange(n):
        exito = lavadero2(5, 2, 1, 0.125) # N=5, S=2, Tf=1, Tr=1/8
        
        suma1 += exito # x
        suma2 += exito**2 # x^2

    esperanza = suma1/float(n)
    varianza = suma2/float(n) - esperanza**2 # V(x) = E(x^2) - E(x)^2
    
    return esperanza, varianza


for n in [100, 1000, 10000, 100000]:
    esperanza, varianza = esperanzaYVarianza(n)
    print "n =", n, "--> E(X) =", esperanza, ", V(X) =", varianza
