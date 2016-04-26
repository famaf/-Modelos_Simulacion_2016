# -*- coding: utf-8 -*-

import random
import math

# METODOS AUXILIARES

def lamda_t(t):
    """
    Funcion Lambda t (funcion de intensidad).
    """
    return 1 + (1/float(1 + t))


def adelgazamiento(lamda, lamda_t, tiempo):
    """
    Generacion de eventos en el intervalo usando Algoritmo de Adelgazamiento
    para Proceso de Poisson no Homogeneo.
    """
    t = 0
    i = 0 # N° de eventos
    s = [] # s[1], s[2], ... ==> tiempos de eventos
    while True:
        u = random.random()

        if t - (math.log(u)/float(lamda)) > tiempo:
            break
        else:
            t -= (math.log(u)/float(lamda))
            v = random.random()

            if v < (lamda_t(t)/float(lamda)):
                i += 1
                s.append(t)

    return i, s


def procesoPoissonHomogeneo(lamda, tiempo):
    """
    Genera las primeras T (tiempo) unidades de tiempo de un
    Proceso de Poisson Homogeneo con parametro lambda.
    """
    t = 0 # tiempo transcurrido
    i = 0 # N° de eventos ocurridos hasta t
    s = [] # S[i]: tiempo del evento mas reciente
    while True:
        u = random.random()

        if t - (math.log(u)/float(lamda)) > tiempo:
            break
        else:
            t -= (math.log(u)/float(lamda))
            i += 1
            s.append(t)

    return i, s


def transformadaInversa(tiempo):
    """
    Metodo de Transformada Inversa, durante un tiempo T (tiempo).
    """
    i = 0
    s = []
    s.append(0)
    while True:
        u = random.random()
        if (1+s[i]/float(1-u)) - 1 > tiempo:
            break
        else:
            i += 1
            s.append((1+s[i-1]/float(1-u)) - 1)

    return i, s


def exponencial(lamda):
    """
    Genera una v.a. X con distribucion Exponencial de parametro lamda.
    X ~ Exp(lamda).
    """
    u = random.random()
    x = -(1/float(lamda))*math.log(u)

    return x


# EJERCICIOS DEL PARCIAL

def ej2(n, p):
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


def ej3a():
    """
    Algoritmo de Adelgazamiento.
    """
    i, s = adelgazamiento(2, lamda_t, 1)

    return i, s


def ej3c():
    """
    Ejericicio 3c con Mezcla de Proceso de Poisson Homogeneo y Metodo de
    Transformada Inversa.
    """
    i_homogeneo, s_homogeneo = procesoPoissonHomogeneo(1, 1)
    i_inversa, s_inversa = transformadaInversa(1)

    s = s_homogeneo + s_inversa
    i = i_homogeneo + i_inversa

    return i, s


def ej4(k):
    """
    Genera un v.a. con el Metodo de Aceptacion y Rechazo con la siguiente
    funcion de densidad:
       f(x) = k * x**(1/3) * e**(-2*x) siendo k una constante de normalizacion.
    """
    numero = (2/float(3))**(4/float(3))
    y = exponencial(1.5)
    u = random.random()
    while u >= (y**(1/3.0) * math.exp(-0.5*y + (1/3.0))) / ((2/3.0)**(1/3.0)):
        y = exponencial(1.5)
        u = random.random()
    
    x = y
    
    return x
