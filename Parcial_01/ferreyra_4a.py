# -*- coding: utf-8 -*-

import random
import math


def experimento(N):
    acumulador = 0
    for _ in xrange(N):
        y = random.random()
        acumulador += math.exp(y) + (math.exp(1 - y**(-1)) * y**(-2))

    return acumulador / float(N)


for N in [100, 1000, 10000, 100000]:
    print("N =", N, "--> Intergral 4a =", experimento(N))
