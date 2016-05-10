# -*- coding: utf-8 -*-

import random
import math

def geometrica(p):
    """
    Genera una v.a. X con distribucion Geometrica de parametro p.
    X ~ Geom(p).
    """
    u = random.random()
    x = math.floor(math.log(u)/math.log(1-p)) + 1

    return x


# P(X = i) = e**(-lambda) * (lambda**i/i!) tq' i>=0

def poisson(lamda):
    """
    Genera una v.a. X con distribucion Poisson de parametro lamda.
    X ~ P(lamda).
    E(X) = lamda
    V(X) = lamda
    """
    u = random.random()
    i = 0
    p = math.exp(-lamda)
    F = p
    while u >= F:
        p = (lamda*p)/float(i+1)
        F += p
        i += 1

    x = i

    return x


def binomial(n, p):
    """
    Genera una v.a. X con distribucion Binomial de parametro n, p.
    X ~ B(n, p).
    """
    u = random.random()
    i = 0
    c = p/float(1-p)
    Pr = (1 - p)**n
    F = Pr
    while u >= F:
        Pr = ((c*(n-i))/float(i+1)) * Pr
        F += Pr
        i += 1

    x = i

    return x


def intervalo(inicio, longitud):
    """
    Devuelve un numero aleatorio entre [inicio, inicio+longitud-1].
    """
    u = random.random()

    return math.floor(longitud*u) + inicio


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


def poisson2(lamda):
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


def normalEstandar():
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


def normal(mu, sigma):
    """
    Genera una v.a. Z con distribucion Normal ==> Z ~ N(mu, sigma)
    """
    z = normalEstandar3()

    return (mu + sigma*z)
