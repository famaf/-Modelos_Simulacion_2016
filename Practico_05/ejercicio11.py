# -*- coding: utf-8 -*-

import random
import math
from distribuciones import intervalo, poisson


def procesoPoissonHomogeneo(lamda, tiempo):
    """
    Genera las primeras T (tiempo) unidades de tiempo de un
    Proceso de Poisson con parametro lambda del Ejercicio 11.
    """
    t = 0 # tiempo transcurrido
    i = 0 # N° colectivos
    s = [] # S[i]: tiempo del evento mas reciente
    
    aficionados = 0 # Cantidad total de aficionados
    j = 0

    while True:
        u = random.random()

        if t - (math.log(u)/float(lamda)) > tiempo:
            break
        else:
            t -= (math.log(u)/float(lamda))
            i += 1
            s.append(t)

    # Asigno a cada colectivo una capacidad {20...40}
    while j < i:
        aficionados += intervalo(20, 21) # Numero entre 20 y 40 -> aficionados
        j += 1

    return aficionados


def procesoPoissonMetodo1(lamda, tiempo):
    """
    Genera las primeras T (tiempo) unidades de tiempo de un
    Proceso de Poisson con parametro lambda del Ejercicio 11.
    """
    t = 0 # tiempo transcurrido
    i = 0 # N° colectivos
    s = [] # S[i]: tiempo del evento mas reciente
    
    aficionados = 0 # Cantidad total de aficionados
    j = 0

    while True:
        u = random.random()

        if t - (math.log(u)/float(lamda)) > tiempo:
            break
        else:
            t -= (math.log(u)/float(lamda))
            i += 1
            s.append(t)

    # Asigno a cada colectivo una capacidad {20...40}
    while j < i:
        aficionados += intervalo(20, 21) # Numero entre 20 y 40 -> aficionados
        j += 1

    return s


def procesoPoissonMetodo2(lamda, tiempo):
    s = []
    n = math.floor(poisson(lamda*tiempo))
    i = 0
    while i < n:
        u = random.random()
        s.append(tiempo*u)
        i += 1

    s.sort()

    return s



def esperanza(n):
    """
    Esperanza del Proceso de Poisson Homogeneo.
    """
    a = 0
    for _ in xrange(n):
        a += procesoPoissonHomogeneo(5, 1)

    return a/float(n)



for n in [100, 1000, 10000, 100000]:
    print "n =", n, "--> E(aficionados) =", esperanza(n)


print "Metodo 1"
print procesoPoissonMetodo1(5, 1)
print "----------------------------"
print "Metodo 2"
print procesoPoissonMetodo2(5, 1)
