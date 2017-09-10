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

    for _ in range(n):
        u = random.random()
        acumulador += funcion(u*(b-a) + a)

    return ((b-a) / float(n))*acumulador


def funcionA(n):
    """
    Ejercicio 3a.
    """
    a = 0
    for _ in xrange(n):
        y = random.random()
        a += (1 - y**2)**(float(3)/2)

    return (a / float(n))


def funcionB(n):
    """
    Ejercicio 3b.
    """
    a = 0
    for _ in xrange(n):
        y = random.random()
        a += (y**(-1) - 1) * (y**(-1) + 2*y - 2)**(-2)

    return (a / float(n))


def funcionC(n):
    """
    Ejercicio 3c.
    """
    a = 0
    for _ in xrange(n):
        y = random.random()
        a += math.exp(2*(y**(-1)) - y**(-2) - 1) * (y**(-2))
    a *= 2

    return (a / float(n))


def funcionD(n):
    """
    Ejercicio 3d.
    """
    a = 0
    for _ in xrange(n):
        w = random.random()
        z = random.random()
        a += math.exp((w + z)**2)

    return (a / float(n))


def funcionE(n):
    """
    Ejercicio 3e.
    """
    a = 0
    for _ in xrange(n):
        w = random.random()
        z = random.random()

        if z > w:
            a += w**(-2) * z**(-2) * math.exp(2 - z**(-1) - w**(-1))

    return (a / float(n))


L = [100, 1000, 10000, 100000, 1000000]

for n in L:
    print("n =", n, "--> Funcion A =", funcionA(n))

print("-------------------------------------------------------------")

for n in L:
    print("n =", n, "--> Funcion B =", funcionB(n))

print("-------------------------------------------------------------")

for n in L:
    print("n =", n, "--> Funcion C =", funcionC(n))

print("-------------------------------------------------------------")

for n in L:
    print("n =", n, "--> Funcion D =", funcionD(n))

print("-------------------------------------------------------------")

for n in L:
    print("n =", n, "--> Funcion E =", funcionE(n))
