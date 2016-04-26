# -*- coding: utf-8 -*-

import random
import math
from distribuciones import poisson


def transformadaInversa(k, lamda):
    """
    Ejercicio 5 con Metodo de Transformada Inversa.
    """
    pj = 0 # Acumula los sumandos del denominador
    j = 0 
    while j <= k:
        pj += (lamda**j/float(math.factorial(j)))
        j += 1

    divisor = pj # Divisor obtenido de la sumatoria

    # Algoritmo de generacion de una va Poisson P(lamda)
    u = random.random()
    i = 0
    pi = 1/float(divisor) # Primer elemento de la productoria
    f = pi

    while u >= f:
        pi = (lamda*pi)/float(i+1)
        f += pi
        i += 1

    x = i

    return x


# buscar q
# Encontrar maximo (m) de p ie pi > pi-1 y pi > pi+1
# Valuar: pm <= c*qm ====> Encuentro c

def aceptacionRechazo(k, lamda):
    """
    Ejercicio 5 con Metodo de Aceptacion y Rechazo.
    """
    x = poisson(lamda)
    while x >= k:
        x = poisson(lamda)

    return x


def esperanza1(k, lamda, n):
    """
    Esperanza con Metodo de Transformada Inversa.
    """
    a = 0
    for _ in xrange(n):
        a += transformadaInversa(k, lamda)

    return a/float(n)


def esperanza2(k, lamda, n):
    """
    Esperanza con Metodo de Aceptacion y Rechazo.
    """
    a = 0
    for _ in xrange(n):
        a += aceptacionRechazo(k, lamda)

    return a/float(n)


print "Metodo de Transformada Inversa"
for n in [100, 1000, 10000, 100000]:
    print "n =", n, "--> E(X) =", esperanza1(10, 2, n)

print "------------------------------"

print "Metodo de Aceptacion y Rechazo"
for n in [100, 1000, 10000, 100000]:
    print "n =", n, "--> E(X) =", esperanza2(10, 2, n)
