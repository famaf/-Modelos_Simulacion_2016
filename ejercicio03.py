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
    a = 0
    for i in xrange(n):
        y = random.random()
        a += (1 - y**2)**(float(3)/2)

    return (a/float(n))

def ejercicio03b(n):
    pass

def fa(x):
    """
    Funcion del ejercicio 3 a.
    """
    return (1 - x**2)**(float(3)/2)


def fb(x):
    """
    Funcion del ejercicio 3 b.
    """
    return (x - x**2)*((1 - 2*x + 2*(y**2))**(-2))


print "n = 100 => Ejercicio 3a =", ejercicio03a(100)
