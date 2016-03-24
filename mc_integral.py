# -*- coding: utf-8 -*-

import random

# Iteraciones
n = 10000

# Limites
a = 0
b = 1

def f(x):
    """
    Funcion a integrar.
    """
    return (1 - x**2)**(float(3)/2)


acumulador = 0

for i in range(n):
    u = random.random()
    acumulador += f(u*(b-a) + a)

print ((b-a)/float(n))*acumulador
