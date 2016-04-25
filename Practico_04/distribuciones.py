# -*- coding: utf-8 -*-

import random
import math

def intervalo(longitud, inicio):
    """
    Devuelve un numero aleatorio entre [inicio, inicio+longitud-1].
    """
    u = random.random()

    return math.floor(longitud*u) + inicio


def permutacionAleatoria(lista):
    """
    Algoritmo de permutacion aleatoria.
    """
    k = len(lista) - 1

    while k > 0:
        u = random.random()
        i = int(math.floor(k*u))
        lista[k], lista[i] = lista[i], lista[k]
        k -= 1

    return lista


# P(X = i) = p * (1-p)**(i-1) tq' i>=1
# min{j : (1-p)**j < 1-U}
# ln es creciente y ln(1-p) < 0
# v = 1-u es U(0, 1)
# X = min{j : j > ln(1-u)/ln(1-p)} => X = piso( ln(1-u)/ln(1-p) ) + 1

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


# P(X = i) = (n!/i!*(n-i)!) * p**i * (1-p)**(n-i) tq' 0<=i<=n

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
