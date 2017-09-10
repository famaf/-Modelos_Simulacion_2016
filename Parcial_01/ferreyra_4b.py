# -*- coding: utf-8 -*-

import random
import math


def experimento(N):
    acumulador = 0
    for _ in xrange(N):
        u = random.random()
        v = random.random()
        acumulador += math.exp(-((u**(-1) + v - 1)**2)) * (u**(-2))

    return acumulador / float(N)


for N in [100, 1000, 10000, 100000]:
    print("N =", N, "--> Intergral 4b =", experimento(N))
