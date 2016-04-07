# -*- coding: utf-8 -*-

import random
import math


def experimento(N):
    exito = 0
    for _ in xrange(N):
        u1 = random.random()  # Simulo u1
        u2 = random.random()  # Simulo u2

        # Si u1 es menor a 1/2
        if u1 < 0.5:
            # Me fijo si u2 es mayor a u1, si es asi entonces es un exito
            if u1 < u2:
                exito += 1
        # Si u1 es mayor a 1/2
        else:
            # Me fijo si u2 es menor a u1, si es asi entonces es un exito
            if u2 < u1:
                exito += 1

    F = float(exito)/N

    return F


for N in [100, 1000, 10000, 100000]:
    print "N =", N, "--> Ejercicio 5b =", experimento(N)
