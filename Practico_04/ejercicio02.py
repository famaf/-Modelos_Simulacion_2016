# -*- coding: utf-8 -*-

import random
import math

# abrir imagen con "eog"


def aproximacion(n):
    """
    Ejericicio 2, usando la Ley de los Grandes Numeros.
    """
    N = 10000
    s = 0

    for _ in xrange(n):
        u = random.random()
        x = int(math.floor(N*u) + 1)

        s += math.exp(x/float(N))

    return (N*s)/float(n)


for n in [100, 1000, 10000, 100000]:
    print "n =", n, "--> Aproximacion =", aproximacion(n)
