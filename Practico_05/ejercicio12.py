# -*- coding: utf-8 -*-

import random
import math
from distribuciones import adelgazamiento

# lamda = 7 porque se tiene que cumplir que lamda_t(t) <= lamda para todo t<=T

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
        a += adelgazamiento(7, lamda_t, 10)

    return a/float(n)



for n in [100, 1000, 10000, 100000]:
    print "n =", n, "--> E(X) =", esperanza(n)
