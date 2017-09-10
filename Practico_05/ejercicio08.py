# -*- coding: utf-8 -*-

import random
import math
from distribuciones import *


def esperanza_exponeciales(n):
    """
    Esperanza de Normal Estandar con Metodo de Exponenciales.
    """
    a = 0
    for _ in xrange(n):
        a += normalEstandar3()

    return a/float(n)


def varianza_exponeciales(n):
    """
    Varianza en base a la esperanza con Metodo de Exponenciales.
    """
    suma1 = 0
    suma2 = 0
    for _ in xrange(n):
        x = normalEstandar3()
        suma1 += x # x
        suma2 += x**2 # x**2

    varianza = suma2/float(n) - (suma1/float(n))**2 # V(x) = E(x^2) - E(x)^2

    return varianza


def esperanza_polar(n):
    """
    Esperanza de Normal Estandar con Metodo Polar.
    """
    a = 0
    for _ in xrange(n):
        x, y = normalPolar1()
        a += x

    return a/float(n)


def varianza_polar(n):
    """
    Varianza en base a la esperanza con Metodo Polar.
    """
    suma1 = 0
    suma2 = 0
    for _ in xrange(n):
        x, y = normalPolar1()
        suma1 += x # x
        suma2 += x**2 # x**2

    varianza = suma2/float(n) - (suma1/float(n))**2 # V(x) = E(x^2) - E(x)^2

    return varianza



print("Esperanza de Normal con Metodo de Exponenciales")
for n in [100, 1000, 10000, 100000]:
    print("n =", n, "--> E(X) =", esperanza_exponeciales(n))

print("Esperanza de Normal con Metodo Polar")
for n in [100, 1000, 10000, 100000]:
    print("n =", n, "--> E(X) =", esperanza_polar(n))

print("---------------------------------------")

print("\nVarianza de Normal con Metodo de Exponenciales")
for n in [100, 1000, 10000, 100000]:
    print("n =", n, "--> V(X) =", varianza_exponeciales(n))

print("\nVarianza de Normal con Metodo Polar")
for n in [100, 1000, 10000, 100000]:
    print("n =", n, "--> V(X) =", varianza_polar(n))
