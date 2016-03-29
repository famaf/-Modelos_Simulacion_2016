# -*- coding: utf-8 -*-

import random
import math

# Infinito en python: infinito = float('inf')

INFINITO = float("inf")

def fa(x):
    """
    Funcion del ejercicio 3 a.
    """
    return (1 - x**2)**(float(3)/2)


def fb(x):
    """
    Funcion del ejercicio 3 b.
    """
    return x*(1 + x**2)**(-2)


def fc(x):
    """
    Funcion del ejercicio 3 b.
    """
    return math.e**(-x**2)


def montecarlo(funcion, a, b, n):
    """
    Calcula la integral por medio del metodo de Monte Carlo.
    Donde:
        funcion = funcion a la cual se quiere aproximar su integral.
        a = limite inferior.
        b = limite superior.
        n = cantidad de interaciones.
    """
    acumulador = 0

    for i in range(n):
        u = random.random()
        acumulador += funcion(u*(b-a) + a)

    return ((b-a)/float(n))*acumulador

print montecarlo(fa, 0, 1, 20)

