# -*- coding: utf-8 -*-

import math
import random
from distribuciones import *

# T = sumatoria(1, k, (fo - fe)^2/fe)
# fo = Ni
# fe = n*pi

def estadisticoT(k, n, N, p):
    """
    Calcula el estadistico T.
    k = particiones (intervalos).
    n = tamaño de la muestra.
    N = vector de valores (Frecuencia Observada) de tamaño k.
    p = valores de valores (Frecuencia Esperada) de tamaño k
    """
    T = 0
    for i in xrange(k):
        T += ((N[i] - n*p[i])**2)/float(n*p[i])

    return T


def chiCuadrado():
    """
    Calcula el p-valor por medio de una aproximacion Chi-Cuadrada.
    """
    lanzamientos = 1000

    valor1 = 158
    valor2 = 172
    valor3 = 164
    valor4 = 181
    valor5 = 160
    valor6 = 165

    N = [valor1, valor2, valor3, valor4, valor5, valor6]
    p = [1/6.0 for _ in xrange(6)]

    t = estadisticoT(6, lanzamientos, N, p) # Valor observado

    grados_libertad = 5 # cantidad de intervalos - 1

    p_valor = pValor(grados_libertad, t)

    return p_valor


def simulacion01(r):
    """
    Algoritmo, para calcular el p-valor, que esta en el Libro de Simulacion.
    """
    n = 1000 # Tamaño de la muestra
    k = 6 # Cantidad de intevalos
    N = [158, 172, 164, 181, 160, 165] # Frecuencias observadas
    prob = [1/6.0 for _ in xrange(6)] # Probabilidades
    prob_acumuladas = [1/6.0, 1/3.0, 0.5, 2/3.0, 5/6.0, 1.0] # Probabilidades acumuladas
    t = estadisticoT(k, n, N, prob) # Valor observado

    exitos = 0 # Cantidad de veces que Ti >= t

    # Frecuencias Observadas
    fe = [n*prob[i] for i in xrange(len(prob))]

    # Hacemos r simulaciones
    for _ in xrange(r):
        # Frecuencias Observadas (son los N)
        fo = [0 for _ in xrange(k)]

        # Calculamos las Frecuencias Obsevadas en un experimento
        for _ in xrange(n):
            u = random.random()
            i = 0
            while u >= prob_acumuladas[i]:
                i += 1

            fo[i] += 1

        T = 0
        # Sumamos todos los estadisticos Ti
        for i in xrange(k):
            Ti = (fo[i] - fe[i])**2/float(fe[i]) # Calculamos los estadistios Ti
            T +=  Ti

        if T >= t:
            exitos += 1

    p_valor = exitos/float(r)

    return p_valor


def simulacion02(r):
    """
    Algoritmo, para calcular el p-valor, que esta en las Filminas.
    """
    n = 1000 # Tamaño de la muestra
    k = 6 # Cantidad de intevalos
    N = [158, 172, 164, 181, 160, 165] # Frecuencias observadas
    prob = [1/6.0 for _ in xrange(6)] # Probabilidades
    t = estadisticoT(k, n, N, prob) # Valor observado

    exitos = 0 # Cantidad de veces que Ti >= t

    for _ in xrange(r):
        Y = []
        N = []
        # Generamos los Y's
        # Tiene que tomar los valores 1...k con probabilidad pj
        # Todos tiene la misma probabilidad
        for _ in xrange(n):
            Y.append(random.randint(1, 6))

        # Generamos los Nj
        # Nj = {i | Yi = j}  j=1...k
        for j in xrange(1, k+1):
            N.append(Y.count(j))

        # Calculamos el estadistico T correspondiente
        T = estadisticoT(k, n, N, prob)

        if T >= t:
            exitos += 1

    p_valor = exitos/float(r)

    return p_valor


print("Chi-Cuadrado --> p-valor =", chiCuadrado())
print("Simulacion 1 --> p-valor =", simulacion01(10000))
print("Simulacion 2 --> p-valor =", simulacion02(10000))
