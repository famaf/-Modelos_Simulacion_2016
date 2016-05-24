# -*- coding: utf-8 -*-

import random
import math
from scipy.special import ndtr, ndtri # Normal
from scipy.special import chdtrc, chdtri # Chi-cuadrado


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


# Variables Aleatorias: Discretas


def geometrica(p):
    """
    Genera una v.a. X con distribucion Geometrica de parametro p.
    X ~ Geom(p).
    """
    u = random.random()
    x = math.floor(math.log(u)/math.log(1-p)) + 1

    return x


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


# Variables Aleatorias: Continuas


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


# Calculos de Φ y la inversa de Φ con la Normal Estadar

def fi(valor):
    """
    Devuelve el FI(valor) de la Normal Estadar.
    """
    return ndtr(valor)


def fi_inversa(resultado):
    """
    Devuelve el "valor" tq' FI(valor) = resultado.
    """
    return ndtri(resultado)


def calculoZalfasobre2(confianza):
    """
    Devuelve el valor Z_alfa/2 segun la confianza ingresada.
    """
    alfa = 1 - confianza/100.0
    beta = alfa/2.0
    result = ndtri(1 - beta) # FI(Z_alfa/2) = 1 - alfa/2

    return result


def calculoConfianza(z_alfaSobre2):
    """
    Devuelve la confianza segun el z_alfaSobre2.
    """
    result = ndtr(z_alfaSobre2)
    beta = 1 - result
    alfa = 2*beta
    confianza = 1 -alfa # Confianza sin porcentual

    return confianza*100


# Calculos Chi-cuadrado

def pValor(v, T):
    """
    Calculo de alfa?????
    v = Grados de libertad.
    T = Estadistico.

    T ... infinito
    """
    return chdtrc(v, T)


def calculoT(v, p):
    """
    v = Grados de libertad.
    p = Probabilidad. (¿ alfa ?)
    """
    return chdtri(v, p)
