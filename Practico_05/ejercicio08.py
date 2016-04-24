# -*- coding: utf-8 -*-

import random
import math
from distribuciones import *


def esperanza_exponeciales(n):
    """
    Esperanza de Normal Estandar con Metodo de Exponenciales.
    """
    a = 0
    for _ in xrange(n):
        a += normalEstandar2()

    return a/float(n)


def esperanza_polar(n):
    """
    Esperanza de Normal Estandar con Metodo Polar.
    """
    a = 0
    for _ in xrange(n):
        x, y = normalPolar1()
        a += x

    return a/float(n)



print "Esperanza de Normal con Metodo de Exponenciales"
for n in [100, 1000, 10000, 100000]:
    print "n =", n, "E(X) =", esperanza_exponeciales(n)

print "---------------------------------------"

print "Esperanza de Normal con Metodo Polar"
for n in [100, 1000, 10000, 100000]:
    print "n =", n, "E(X) =", esperanza_polar(n)

