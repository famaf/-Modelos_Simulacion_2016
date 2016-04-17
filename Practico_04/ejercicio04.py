# -*- coding: utf-8 -*-

import random
import math
from distribuciones import geometrica


def ejercicio04_composicionInversa1():
    """
    Ejericicio 04 del Practico 4, sin Geometrica.
    """
    # Metodo de composicion
    u = random.random()
    if u < 0.5:
        # Metodo de la Transformada Inversa
        u = random.random()
        j = 1
        pj = 0.5**j
        # Mientras la acumulada sea menor a la U, sigo acumulando valores
        # hasta que la acumulada sea mayor a la U
        while u >= pj:
            j += 1
            pj += 0.5**j
        x = j
    else:
        # Metodo de la Transformada Inversa
        u = random.random()
        j = 1
        pj = 0.5*((float(2)/3)**j)
        # Mientras la acumulada sea menor a la U, sigo acumulando valores
        # hasta que la acumulada sea mayor a la U
        while u >= pj:
            j += 1
            pj += 0.5*((float(2)/3)**j)
        x = j

    return x


def ejercicio04_composicionGeometrica():
    """
    Ejericicio 04 del Practico 4 usando Geometrica.
    """
    # Metodo de composicion
    u = random.random()
    if u < 0.5:
        # Metodo de la Transformada Inversa
        u = random.random()
        x = geometrica(0.5)
    else:
        # Metodo de la Transformada Inversa
        u = random.random()
        x = geometrica(2/float(3))

    return x


def esperanza1(n):
    """
    Esperanza con Metodo de Transformada Inversa.
    """
    a = 0
    for _ in xrange(n):
        a += ejercicio04_composicionInversa1()

    return a/float(n)


def esperanza2(n):
    """
    Esperanza con Metodo de Transformada Inversa usando Geometrica.
    """
    a = 0
    for _ in xrange(n):
        a += ejercicio04_composicionGeometrica()

    return a/float(n)


for n in [100, 1000, 10000, 100000]:
    print "n =", n, "--> E(X) =", esperanza1(n)

print "------------------------------"

for n in [100, 1000, 10000, 100000]:
    print "n =", n, "--> E(X) =", esperanza2(n)
