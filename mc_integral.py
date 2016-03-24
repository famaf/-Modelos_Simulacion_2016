# -*- coding: utf-8 -*-

import random

def fa(x):
    """
    Funcion del ejercicio 3 a.
    """
    return (1 - x**2)**(float(3)/2)


def montecarlo(a, b, n):
    """
    Calcula la integral por medio del metodo de Monte Carlo.
    Donde:
        a = limite inferior.
        b = limite superior.
        n = cantidad de interaciones.
    """
    acumulador = 0

    for i in range(n):
        u = random.random()
        acumulador += fa(u*(b-a) + a)

    return ((b-a)/float(n))*acumulador

print montecarlo(0, 1, 10000)
