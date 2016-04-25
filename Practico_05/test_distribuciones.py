# -*- coding: utf-8 -*-

import random
import math


def ejercicio02():
    """
    Esperanza con Distribucion Weibull.
    """
    a = 0
    for _ in xrange(n):
        a += random.weibullvariate(1, 1)

    return a/float(n)


def ejercicio07():
    """
    Esperanza con Distribucion Weibull.
    """
    a = 0
    for _ in xrange(n):
        a += random.gammavariate(2, 1)

    return a/float(n)


def ejercicio08():
    """
    Esperanza con Distribucion Weibull.
    """
    a = 0
    for _ in xrange(n):
        a += random.normalvariate(0, 1)

    return a/float(n)



print "Ejercicio 2"
for n in [100, 1000, 10000, 100000]:
    print "n =", n, "--> E(X) =", ejercicio02()

print "-----------------------------"

print "Ejercicio 7"
for n in [100, 1000, 10000, 100000]:
    print "n =", n, "--> E(X) =", ejercicio07()

print "-----------------------------"

print "Ejercicio 8"
for n in [100, 1000, 10000, 100000]:
    print "n =", n, "--> E(X) =", ejercicio08()
