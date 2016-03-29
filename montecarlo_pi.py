# -*- coding: utf-8 -*-

from random import random
from math import sqrt

def montecarlo(t):
    """
    Calcula y devuelve el valor aproximado de pi usando el
    metodo de Montecarlo a partir de t puntos.
    """
    g = 0
    for i in range(t):
        x = random()
        y = random()
        d = sqrt(x**2 + y**2)

        if d < 1:
            g += 1
    return 4*g/float(t)

