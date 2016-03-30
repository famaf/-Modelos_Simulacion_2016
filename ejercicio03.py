# -*- coding: utf-8 -*-

import random
import math

# Infinito en python: infinito = float("inf")

def montecarlo(funcion, a, b, n):
    """
    Calcula la integral por medio del metodo de Monte Carlo.
    Donde:
        funcion = funcion a la cual se quiere aproximar su integral.
        a = limite inferior != infinito.
        b = limite superior != infinito.
        n = cantidad de interaciones.
    """
    acumulador = 0

    for i in range(n):
        u = random.random()
        acumulador += funcion(u*(b-a) + a)

    return ((b-a)/float(n))*acumulador


def ejercicio03a(n):
    """
    Ejercicio 3a del Practico 3.
    """
    a = 0
    for i in xrange(n):
        y = random.random()
        a += (1 - y**2)**(float(3)/2)

    return (a/float(n))


def ejercicio03b(n):
    """
    Ejercicio 3b del Practico 3.
    """
    a = 0
    for i in xrange(n):
        y = random.random()
        a += (y**(-1) - 1) * (y**(-1) + 2*y - 2)**(-2)

    return (a/float(n))


def ejercicio03c(n):
    """
    Ejercicio 3c del Practico 3.
    """
    a = 0
    for i in xrange(n):
        y = random.random()
        a += math.e**(2*(y**(-1)) - y**(-2) - 1) * (y**(-2))
    a *= 2

    return (a/float(n))

# ESTE NO FUNCIONA BIEN
def ejercicio03d(n):
    """
    Ejercicio 3d del Practico 3.
    """
    a = 0
    for i in xrange(n):
        w = random.random()
        z = random.random()
        a += math.e**((w + z)**2)

    return (a/float(n))


L = [100, 1000, 10000, 100000, 1000000]

print "-------------------------------------------------------------"
for n in L:
    #print "n = {0} => Ejercicio 3a = {1}" .format(n, ejercicio03a(n))
    print "n = %d => Ejercicio 3a = %f" % (n, ejercicio03a(n))
print "-------------------------------------------------------------"

for n in L:
    print "n = {0} => Ejercicio 3b = {1}" .format(n, ejercicio03b(n))
print "-------------------------------------------------------------"

for n in L:
    print "n = {0} => Ejercicio 3c = {1}" .format(n, ejercicio03c(n))
print "-------------------------------------------------------------"

for n in L:
    print "n = {0} => Ejercicio 3d = {1}" .format(n, ejercicio03d(n))
print "-------------------------------------------------------------"
