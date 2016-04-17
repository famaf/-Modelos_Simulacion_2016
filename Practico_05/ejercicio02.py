# -*- coding: utf-8 -*-

import random
import math
from distribuciones import raizGeneral


def ejercicio02(alfa, beta):
    """
    Ejercicio 2 del Practico 5 con Metodo de Transformada Inversa.
    """
    u = random.random()
    x = raizGeneral(beta, -(math.log(1-u)/float(alfa)))

    return x


def esperanza(n):
    """
    Esperanza con Metodo de Transformada Inversa.
    """
    a = 0
    for _ in xrange(n):
        a += ejercicio02(1, 1)

    return a/float(n)


for n in [100, 1000, 10000, 100000]:
    print "n =", n, "--> E(X) =", esperanza(n)
