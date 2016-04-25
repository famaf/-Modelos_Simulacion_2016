# -*- coding: utf-8 -*-

import random
import math
from distribuciones import exponencial


def aceptacionRechazo():
    """
    Ejercicio 7 con Metodo de Aceptacion y Rechazo.
    X ~ Gamma(alfa, beta) = ((beta^alfa)/Gamma(alfa)) * e^(-beta*x) * x^(alfa-1)
    E(X) = alfa/beta
    """
    y = exponencial(0.5)
    u = random.random()

    while u >= ((y * math.exp(1 - 0.5*y))/2.0):
        y = exponencial(0.5)
        u = random.random()

    x = y

    return x


def esperanza(n):
    """
    Esperanza con Metodo de Aceptacion y Rechazo.
    """
    a = 0
    for _ in xrange(n):
        a += aceptacionRechazo()

    return a/float(n)


for n in [100, 1000, 10000, 100000]:
    print "n =", n, "--> E(X) =", esperanza(n)
