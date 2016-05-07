# -*- coding: utf-8 -*-

import random
import math
import matplotlib.pyplot as plt


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


def lavadero01(N, S, Tf, Tr):
    """
    N = Lavadoras en servicio
    S = Lavadoras de repuesto

    Tf = Tiempo medio hasta fallar
    Tr = Tiempo medio de reparacion
    """

    lamda_falla = devolverLambda(Tf) # Lambda de los tiempos de falla
    lamda_reparacion = devolverLambda(Tr) # Lambda de los tiempos de reparacion

    T = 0 # Tiempo en que falla el sistema
    t = 0 # Variable de tiempo
    r = 0 # Numero de Lavadoras rotas en el instante t

    t_estrella = INFINITO # Tiempo en el que la Lavadora en reparacion vuelve a funcionar

    lavadoras = [] # Lista de tiempos de falla de las Lavadoras

    # Generamos N tiempos de falla (uno para cada maquina)
    for _ in xrange(N):
        F = exponencial(lamda_falla) # Tiempo hasta Fallar
        lavadoras.append(F)

    lavadoras.sort() # Ordenamos los tiempos

    while True:
        # Lavadora falla antes de que se repare alguna
        if lavadoras[0] < t_estrella:
            t = lavadoras[0]
            r += 1 # Se rompio una Lavadora
            # Si hay mas de S Lavadoras descompuestas (no hay repuestos)
            if r == S+1:
                T = t
                break
            # Se agrega la Lavadora de repuesto, ya que fallo alguna
            if r < S+1:
                X = exponencial(lamda_falla) # Tiempo hasta fallar de la lavadora de repuesto
                lavadoras.pop(0) # Quitamos la Lavadora que fallo
                lavadoras.append(t+X) # Agregamos la nueva Lavadora al sistema (tiempo actual + tiempo de falla)
                lavadoras.sort() # Ordenamos los tiempos en que fallan las Lavadoras
            # La Lavadora rota es la unica descompuesta, entonces se comienza a reparar
            if r == 1:
                Y = exponencial(lamda_reparacion) # Lavadora entra en reparacion
                t_estrella = t + Y
        
        # Lavadora que estaba en reparacion, esta disponible
        elif lavadoras[0] >= t_estrella:
            t = t_estrella
            r -= 1
            # Hay maquinas para Reparar
            if r > 0:
                Y = exponencial(lamda_reparacion) # Tiempo de reparacion de la Lavadora para reparar
                t_estrella = t + Y
            # No hay maquinas que Reparar
            if r == 0:
                t_estrella = INFINITO

    return T


def lavadero02(N, S, Tf, Tr):
    """
    N = Lavadoras en servicio
    S = Lavadoras de repuesto

    Tf = Tiempo medio hasta fallar
    Tr = Tiempo medio de reparacion
    """

    lamda_falla = devolverLambda(Tf) # Lambda de los tiempos de falla
    lamda_reparacion = devolverLambda(Tr) # Lambda de los tiempos de reparacion

    T = 0 # Tiempo en que falla el sistema
    t = 0 # Variable de tiempo
    r = 0 # Numero de Lavadoras rotas en el instante t

    t_estrella = [INFINITO, INFINITO] # Tiempo en el que las Lavadoras en reparacion vuelve a funcionar

    lavadoras = [] # Lista de tiempos de falla de las Lavadoras

    # Generamos N tiempos de falla (uno para cada maquina)
    for _ in xrange(N):
        F = exponencial(lamda_falla) # Tiempo hasta Fallar
        lavadoras.append(F)

    lavadoras.sort() # Ordenamos los tiempos

    while True:
        # Lavadora falla antes de que se repare alguna
        t_min = min(t_estrella)
        if lavadoras[0] < t_min:
            t = lavadoras[0]
            r += 1 # Se rompio una Lavadora
            # Si hay mas de S Lavadoras descompuestas (no hay repuestos)
            if r == S+1:
                T = t
                break
            # Se agrega la Lavadora de repuesto, ya que fallo alguna
            if r < S+1:
                X = exponencial(lamda_falla) # Tiempo hasta fallar de la lavadora de repuesto
                lavadoras.pop(0) # Quitamos la Lavadora que fallo
                lavadoras.append(t+X) # Agregamos la nueva Lavadora al sistema (tiempo actual + tiempo de falla)
                lavadoras.sort() # Ordenamos los tiempos en que fallan las Lavadoras
            # Primera Lavadora rota es la unica descompuesta, entonces se comienza a reparar
            if r == 1 or r == 2:
                if t_estrella[0] == INFINITO:
                    Y = exponencial(lamda_reparacion) # Primera Lavadora entra en reparacion
                    t_estrella[0] = t + Y
                elif t_estrella[1] == INFINITO:
                    Y = exponencial(lamda_reparacion) # Primera Lavadora entra en reparacion
                    t_estrella[1] = t + Y
        
        # Lavadora que estaba en reparacion, esta disponible
        elif lavadoras[0] >= t_min:
            t = t_min
            r -= 1 # Se reparo una maquina
            # Hay por lo menos una maquina para reparar
            if r > 1:
                Y = exponencial(lamda_reparacion) # Tiempo de reparacion de la Lavadora para reparar
                t_estrella[t_estrella.index(t_min)] = t + Y
            # No hay maquinas que Reparar
            if r <= 1:
                t_estrella[t_estrella.index(t_min)] = INFINITO


    return T


def esperanzaYVarianza(lavadero, N, S, Tf, Tr):
    """
    Esperanza y Varianza del Tiempo de Fallo del Sistema del Lavadero.
    N = Lavadoras en servicio
    S = Lavadoras de repuesto

    Tf = Tiempo medio hasta fallar
    Tr = Tiempo medio de reparacion
    """
    n = 100000 # Simulaciones
    suma1 = 0
    suma2 = 0

    for _ in xrange(n):
        exito = lavadero(N, S, Tf, Tr)
        
        suma1 += exito # x
        suma2 += exito**2 # x^2

    esperanza = suma1/float(n)
    varianza = suma2/float(n) - esperanza**2 # V(x) = E(x^2) - E(x)^2
    
    return esperanza, varianza


def printEV():
    # print "\n### Lavadero con 2 Repuestos y 1 Tecnico ###"
    # esperanza, varianza = esperanzaYVarianza(lavadero01, 5, 2, 1, 1/8.0)
    # print "E(X) =", esperanza, ", V(X) =", varianza

    # print "----------------------------------------------------------------------"

    # print "### Lavadero con 3 Repuestos y 1 Tecnico ###"
    # esperanza, varianza = esperanzaYVarianza(lavadero01, 5, 3, 1, 1/8.0)
    # print "E(X) =", esperanza, ", V(X) =", varianza

    # print "----------------------------------------------------------------------"

    print "### Lavadero con 2 Repuestos y 2 Tecnico ###"
    # (2.61, 2.76)
    esperanza, varianza = esperanzaYVarianza(lavadero02, 5, 2, 1, 1/8.0)
    print "E(X) =", esperanza, ", V(X) =", varianza
    print ""


def plot():
    """
    Ploteo en Histogramas
    """
    v1 = [lavadero01(5, 2, 1, 1/8.0) for _ in xrange(10000)] # S = 2 y Tecnicos = 1
    v2 = [lavadero01(5, 3, 1, 1/8.0) for _ in xrange(10000)] # S = 3 y Tecnicos = 1
    v3 = [lavadero02(5, 2, 1, 1/8.0) for _ in xrange(10000)] # S = 2 y Tecnicos = 2
    #plt.figure(1)
    plt.title("Histograma Lavadero")
    plt.ylabel("Mario")
    plt.xlabel("Manda")
    plt.hist(v1, bins=100, color="r")
    #plt.figure(2)
    # plt.hist(v2, bins=100, color="g")
    # #plt.figure(3)
    # plt.hist(v3, bins=100, color="b")
    plt.show()


printEV()
#plot()
