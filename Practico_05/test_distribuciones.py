# -*- coding: utf-8 -*-

import random
import math


def ejercicio02(n):
    """
    Esperanza con Distribucion Weibull.
    """
    a = 0
    for _ in xrange(n):
        a += random.weibullvariate(1, 1)

    return a/float(n)


def ejercicio07(n):
    """
    Esperanza con Distribucion Gamma.
    """
    a = 0
    for _ in xrange(n):
        a += random.gammavariate(2, 1)

    return a/float(n)


def ejercicio08(n):
    """
    Esperanza con Distribucion Normal.
    """
    a = 0
    for _ in xrange(n):
        a += random.normalvariate(0, 1)

    return a/float(n)


def ejercicio08_V(n):
    """
    Varianza en base a la esperanza de Normal Estadar.
    """
    suma1 = 0
    suma2 = 0
    for _ in xrange(n):
        x = random.normalvariate(0, 1)
        suma1 += x # x
        suma2 += x**2 # x**2

    varianza = suma2/float(n) - (suma1/float(n))**2 # V(x) = E(x^2) - E(x)^2

    return varianza


print "Ejercicio 2"
for n in [100, 1000, 10000, 100000]:
    print "n =", n, "--> E(X) =", ejercicio02(n)

print "---------------------------------------------"

print "Ejercicio 7"
for n in [100, 1000, 10000, 100000]:
    print "n =", n, "--> E(X) =", ejercicio07(n)

print "---------------------------------------------"

print "Ejercicio 8"
for n in [100, 1000, 10000, 100000]:
    print "n =", n, "--> E(X) =", ejercicio08(n)

for n in [100, 1000, 10000, 100000]:
    print "n =", n, "--> V(X) =", ejercicio08_V(n)
