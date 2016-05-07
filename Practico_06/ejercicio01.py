# -*- coding: utf-8 -*-

import random
import math
from distribuciones import *


def mediaMuestral(n, funcion):
    i = 1
    X = funcion
    F = X
    while i <= n:
        X = X + (funcion - X)/float(i+1)
        F += X
        i += 1

    return F


def varianzaMuestral(n, funcion):
    i = 1
    S = 0
    F = S
    while i <= n:
        S = (1 - 1/float(i)) * S + (i + 1) * (mediaMuestral(i+1, funcion) - mediaMuestral(i, funcion))**2
        F += S
        i += 1

    return F


def ejercicio(n):
    z = normalEstandar()
    a = z
    for i in xrange(1, n+1):
        if varianzaMuestral(i, z)/math.sqrt(n) < 0.1:
            z = normalEstandar()
            a += z
        else:
            break

    return a/float(n)

for n in [100, 1000, 10000, 100000]:
    print "n =", n, "--> E(X) =", ejercicio(n)
