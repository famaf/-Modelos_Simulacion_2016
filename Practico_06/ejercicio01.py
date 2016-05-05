# -*- coding: utf-8 -*-

import random
import math


def raizGeneral(radicando, raiz):
    """
    Calcula la raiz N-esima de un numero.
    """
    return radicando**(1.0/raiz)


def exponencial(lamda):
    """
    Genera una v.a. X con distribucion Exponencial de parametro lamda.
    X ~ Exp(lamda).
    f(x) = lamda * e^(-lambda*x)
    F(x) = 1 - e**(-x) tq' lambda = 1
    E(x) = 1/lambda
    """
    u = random.random()
    x = -(1/float(lamda))*math.log(u)

    return x


def poisson(lamda):
    """
    Genera una v.a. X con distribucion Poisson de parametro lambda
    X ~ Poisson(lambda)
    Con Metodo de Transformada Inversa.
    """
    i = 0
    u = random.random()
    while u >= math.exp(-lamda):
        u *= random.random()
        i += 1

    x = i

    return x


def gamma(n, lamda):
    """
    Genera una v.a. X con distribucion Gamma de parametros (n, lamda)
    X ~ Gamma(n ,lamda)
    """
    u = 1 # Acumula la productoria de la uniformes.
    i = 0
    # Hago el producto de n uniformes
    while i < n:
        u *= random.random()
        i += 1

    x = -(1/float(lamda)) * math.log(u)

    return x


def normalEstandar1():
    """
    Genera una v.a. Z con distribucion Normal Estandar ==> Z ~ N(0, 1)
    Genera una v.a. X con distribucion Exponencial ==> X ~ Exp(1).
    """
    y1 = exponencial(1)
    y2 = exponencial(1)
    while y2 - ((y1 - 1)**2/2.0) <= 0:
        y1 = exponencial(1)
        y2 = exponencial(1)

    x = y2 - ((y1 - 1)**2/2.0)
    u = random.random()

    if u < 0.5:
        z = y1
    else:
        z = -y1

    return z
