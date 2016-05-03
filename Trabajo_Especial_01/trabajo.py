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
    r = 0 # Variable de estado del sistema (r: numero de lavadoras rotas en el instante t)

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
                lavadoras.pop(0)
                lavadoras.append(t+X)
                lavadoras.sort()
            # La Lavadora rota es la unica descompuesta, entonces se comienza a reparar
            if r == 1:
                Y = exponencial(lamda_reparacion) # Lavadora entra en reparacion
                t_estrella = t + Y
        
        # Lavadora que estaba en reparacion, esta disponible
        elif t_estrella <= lavadoras[0]:
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
    r = 0 # Variable de estado del sistema (r: numero de lavadoras rotas en el instante t)

    t_estrella = [INFINITO, INFINITO] # Tiempo en el que las Lavadoras en reparacion vuelve a funcionar

    lavadoras = [] # Lista de tiempos de falla de las Lavadoras

    tecnicos_libres = 2

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
                lavadoras.pop(0)
                lavadoras.append(t+X)
                lavadoras.sort()
            # Primera Lavadora rota es la unica descompuesta, entonces se comienza a reparar
            if r == 1:
                Y = exponencial(lamda_reparacion) # Lavadora entra en reparacion
                tecnicos_libres -= 1
                t_estrella[0] = t + Y
            # Segunda Lavadora rota es la unica descompuesta, entonces se comienza a reparar
            if r == 2:
                Y = exponencial(lamda_reparacion) # Lavadora entra en reparacion
                tecnicos_libres -= 1
                t_estrella[1] = t + Y
        
        # Lavadora que estaba en reparacion, esta disponible
        elif t_estrella <= lavadoras[0]:
            t = t_estrella
            r -= 1 # Se reparo una maquina
            tecnicos_libres += 1
            # Hay maquinas para Reparar
            if r - tecnicos_libres > 0:
                Y = exponencial(lamda_reparacion) # Tiempo de reparacion de la Lavadora para reparar
                t_estrella = t + Y
            # No hay maquinas que Reparar
            if r == 0:
                t_estrella = INFINITO

    return T


def esperanzaYVarianza01(n):
    """
    Esperanza y Varianza del Tiempo de Fallo del Sistema del Lavadero 1.
    """
    suma1 = 0
    suma2 = 0

    for _ in xrange(n):
        exito = lavadero01(5, 3, 1, 1/8.0) # N=5, S=2, Tf=1, Tr=1/8
        
        suma1 += exito # x
        suma2 += exito**2 # x^2

    esperanza = suma1/float(n)
    varianza = suma2/float(n) - esperanza**2 # V(x) = E(x^2) - E(x)^2
    
    return esperanza, varianza


def esperanzaYVarianza02(n):
    """
    Esperanza y Varianza del Tiempo de Fallo del Sistema del Lavadero 2.
    """
    suma1 = 0
    suma2 = 0

    for _ in xrange(n):
        exito = lavadero02(5, 2, 1, 1/8.0) # N=5, S=2, Tf=1, Tr=1/8
        
        suma1 += exito # x
        suma2 += exito**2 # x^2

    esperanza = suma1/float(n)
    varianza = suma2/float(n) - esperanza**2 # V(x) = E(x^2) - E(x)^2
    
    return esperanza, varianza


print "Lavadero con 3 Repuestos y 1 Tecnico"
for n in [100, 1000, 10000, 100000]:
    esperanza, varianza = esperanzaYVarianza01(n)
    print "n =", n, "--> E(X) =", esperanza, ", V(X) =", varianza

print "----------------------------------------------------------------------"

print "Lavadero con 2 Repuestos y 2 Tecnico"
for n in [100, 1000, 10000, 100000]:
    esperanza, varianza = esperanzaYVarianza02(n)
    print "n =", n, "--> E(X) =", esperanza, ", V(X) =", varianza
