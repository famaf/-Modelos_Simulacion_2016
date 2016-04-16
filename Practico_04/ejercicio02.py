# -*- coding: utf-8 -*-

import random
import math

def ejercicio02(n):
    """
    Ejericicio 02 del Practico 4.
    """
    N = 10000
    s = 0

    for _ in xrange(n):
        u = random.random()
        x = int(math.floor(N*u) + 1)

        s += math.exp(x/float(N))

    return (N*s)/float(n)


for n in [100, 1000, 10000, 100000]:
    print "n =", n, "--> Ejericicio 02 =", ejercicio02(n)
