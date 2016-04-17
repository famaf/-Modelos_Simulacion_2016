# -*- coding: utf-8 -*-

import random
import math

def intervalo(longitud, inicio):
    """
    Devuelve un numero aleatorio entre [inicio, inicio+longitud-1].
    """
    u = random.random()

    return math.floor(longitud*u) + inicio


def raizGeneral(raiz, radicando):
    """
    Calcula la raiz N-esima de un numero.
    """
    return radicando**(1.0/raiz)


def exponencial(lamda):
    """
    Genera una v.a. X con distribucion Exponencial de parametro lamda.
    X ~ Exp(lamda).
    """
    u = random.random()
    x = -(1/float(lamda))*math.log(u)

    return x

