# -*- coding: utf-8 -*-

import random
import math
from distribuciones import procesoPoissonHomogeneo, poisson


def procesoPoissonMetodo1(lamda, tiempo):
    """
    Metodo 1 de generacion de un Proceso de Poisson Homogeneo.
    """
    return procesoPoissonHomogeneo(lamda, tiempo)


def procesoPoissonMetodo2(lamda, tiempo):
    """
    Metodo 2 de generacion de un Proceso de Poisson Homogeneo.
    """
    s = []
    n = math.floor(poisson(lamda*tiempo))
    i = 0
    while i < n:
        u = random.random()
        s.append(tiempo*u)
        i += 1

    s.sort()

    return s
