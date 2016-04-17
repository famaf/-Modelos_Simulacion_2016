# -*- coding: utf-8 -*-

import random
import math


def ejercicio01():
    u = random.random()
    if u < 0.25:
        x = 2 + 2*math.sqrt(u)
    else:
        x = 6 - 6*math.sqrt((1-u)/3.0)

    return x


def esperanza(n):
    a = 0
    for _ in xrange(n):
        a += ejercicio01()

    return a/float(n)


for n in [100, 1000, 10000, 100000]:
    print "n =", n, "--> E(X) =", esperanza(n)
