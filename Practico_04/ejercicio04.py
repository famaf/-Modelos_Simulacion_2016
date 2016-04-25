# -*- coding: utf-8 -*-

import random
import math
from distribuciones import geometrica


# Transformada Inversa
#     | x0 si U < F(x0)
#     | x1 si F(x0) <= U < F(x1)
# X = | :
#     | xj si F(xj-1) <= U < F(xj)
#     | :

# X <- x0 si U < p0 tq' p0 = F(x0)
# X <- xj si F(xj-1) <= U < F(xj)

# U ~ U(0,1)
# if U < p0 => X <- x0 y terminar
# if U < p0+p1 => X <- x1 y terminar
# :


# Composicion
# X1:{pj tq' j >= 0} y X2:{qj tq' j >= 0}
# P(X = j) = alfa*pj + (1-alfa)*qj
#     | X1 con probabilidad alfa
# X = |
#     | X2 con probabilidad 1-alfa


def composicionInversa():
    """
    Ejericicio 4 usando Metodo de Composicion y Transformada Inversa.
    """
    # Metodo de composicion
    u = random.random()
    if u < 0.5:
        # Metodo de la Transformada Inversa
        u = random.random()
        j = 1
        f = 0.5**j # f = p1
        # Mientras la acumulada sea menor a la U, sigo acumulando valores
        # hasta que la acumulada sea mayor a la U
        while u > f:
            j += 1
            f += 0.5**j # f = f + pj
        x = j
    else:
        # Metodo de la Transformada Inversa
        u = random.random()
        j = 1
        f = 0.5*((float(2)/3)**j) # f = p1
        # Mientras la acumulada sea menor a la U, sigo acumulando valores
        # hasta que la acumulada sea mayor a la U
        while u > f:
            j += 1
            f += 0.5*((float(2)/3)**j) # f = f + pj
        x = j

    return x


def composicionGeometrica():
    """
    Ejericicio 4 usando Metodo de Composicion y Geometrica.
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
        x = geometrica(1/float(3))

    return x


def esperanza1(n):
    """
    Esperanza con Metodo de Composicion y Transformada Inversa.
    """
    a = 0
    for _ in xrange(n):
        a += composicionInversa()

    return a/float(n)


def esperanza2(n):
    """
    Esperanza con Metodo de Composicion y Geometrica.
    """
    a = 0
    for _ in xrange(n):
        a += composicionGeometrica()

    return a/float(n)

print "Metodo de Composicion y Inversa"
for n in [100, 1000, 10000, 100000]:
    print "n =", n, "--> E(X) =", esperanza1(n)

print "------------------------------"

print "Metodo de Composicion y Geometrica"
for n in [100, 1000, 10000, 100000]:
    print "n =", n, "--> E(X) =", esperanza2(n)
