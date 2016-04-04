# -*- coding: utf-8 -*-(

import random
import math


def ejercicio05a(n):
    """
    Ejercicio 5a del Practico 3.
    """
    a = 0 # Acumulador de la suma de N's tq' max{ N : Pn >= e^(-3) }
    for i in xrange(n):
        N = 0 # max { N : Pn > 1}
        p = 1 # Pn

        # Si Pn >= 1 entonces multiplicamos otro numero aleatorio
        # y aumentamos el N
        while p >= math.exp(-3):
            p *= random.random()
            N += 1
        
        a += (N - 1)

    return float(a)/n


def ejercicio05b(i):
    """
    Ejercicio 5b del Practico 3.
    """
    exitos = 0
    cota = math.exp(-3)
    for _ in xrange(1000000):
        u = 1 # Empezamos con la Pi = 1, Pi : Productoria de i numeros

        # Multiplicamos i numeros aleatorios
        for _ in xrange(i):
            u *= random.random()

        # Si Pi >= e^(-3)
        if u >= cota:
            u *= random.random()
            # Me fijo que Pi+1 < e^(-3)
            if u < cota:
                exitos += 1

    return float(exitos)/1000000



for n in [100, 1000, 10000, 100000, 1000000]:
    print "n =", n, "--> E(N) =", ejercicio05a(n)

print "--------------------------------"

for i in xrange(7):
    print "P(N = %d)" % i, "=", ejercicio05b(i)
