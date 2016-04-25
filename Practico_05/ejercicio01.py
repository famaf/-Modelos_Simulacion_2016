# -*- coding: utf-8 -*-

import random
import math


# Transformada Inversa
# F distribucion continua e inversible y U ~ U(0,1)
# ==> X = F^(-1)(U) v.a. con distribucion F
# P(X<=a) = P(F^(-1)(U)<=a) = P(F(F^(-1)(U))<=F(a)) = P(U<=F(a)) = F(a)

def transformadaInversa():
    """
    Ejercicio 1 con Metodo de Transformada Inversa.
    """
    u = random.random()
    if u < 0.25:
        x = 2 + 2*math.sqrt(u)
    else:
        x = 6 - 6*math.sqrt((1-u)/3.0)

    return x


def esperanza(n):
    """
    Esperanza con Metodo de Transformada Inversa.
    """
    a = 0
    for _ in xrange(n):
        a += transformadaInversa()

    return a/float(n)


for n in [100, 1000, 10000, 100000]:
    print "n =", n, "--> E(X) =", esperanza(n)
