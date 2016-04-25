# -*- coding: utf-8 -*-

import random
import math
from distribuciones import adelgazamiento, procesoPoissonHomogeneo, raizGeneral

# lamda = 7 porque se tiene que cumplir que lamda_t(t) <= lamda para todo t<=T

#################
# EJERCICIO 12a #
#################
def lamda_t(t):
    """
    Funcion Lambda t (funcion de intensidad).
    """
    return 3 + (4/float(t+1))


def esperanza(n):
    """
    Esperanza del Proceso de Poisson No Homogeneo del Ejercicio 12a.
    """
    a = 0
    for _ in xrange(n):
        i, s = adelgazamiento(7, lamda_t, 10) # Lambda = 7
        a += i

    return a/float(n)



for n in [100, 1000, 10000, 100000]:
    print "n =", n, "--> E(X) =", esperanza(n)


#################
# EJERCICIO 12c #
#################
def transformadaInversa(tiempo):
    """
    Metodo de Transformada Inversa, durante un tiempo T (tiempo).
    """
    i = 0
    s = []
    s.append(0)
    while True:
        u = random.random()
        if ((s[i]+1)/raizGeneral(1-u, 4)) - (s[i] + 1) > tiempo:
            break
        else:
            i += 1
            s[i] = ((s[i-1]+1)/raizGeneral(1-u, 4)) - (s[i-1] + 1)

    return i, s


def ejercicio12c(tiempo):
    """
    Ejericicio 12c con Mezcla de Proceso de Poisson Homogeneo y Metodo de
    Transformada Inversa.
    """
    i_homogeneo, s_homogeneo = procesoPoissonHomogeneo(3, tiempo)
    i_inversa, s_inversa = transformadaInversa(tiempo)

    s = s_homogeneo ++ s_inversa
    i = i_homogeneo + i_inversa

    return i, s


# i, s = ejercicio12c(10)
# print "i =", i, "len(s) =", len(s)
