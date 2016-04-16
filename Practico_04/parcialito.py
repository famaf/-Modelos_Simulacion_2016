# -*- coding: utf-8 -*-

import random
import math

def parcialito(p):
    """
    Parcialito Nº 3.
    """
    N = 10000
    k = 10
    s = 0

    for _ in xrange(p):
        u = random.random()
        x = int(math.floor(N*u) + 1)

        s += math.cos((2*math.pi*x)/float(k))

    return (N*s)/float(p)

for p in [100, 1000, 10000, 100000]:
    print "p =", p, "--> Parcialito =", parcialito(p)
