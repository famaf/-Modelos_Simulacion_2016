# -*- coding: utf-8 -*-

import random
import math


def raizGeneral(raiz, radicando):
    return radicando**(1.0/raiz)

def ejercicio02(alfa, beta):
    u = random.random()
    x = raizGeneral(beta, -(math.log(1-u)/float(alfa)))

    return x



def esperanza(n):
    a = 0
    for _ in xrange(n):
        a += ejercicio02(1, 1)

    return a/float(n)


for n in [100, 1000, 10000, 100000]:
    print "n =", n, "--> E(X) =", esperanza(n)
