# -*- coding: utf-8 -*-

import random
import math

# 15 observaciones
# Pesos
# p(21) = 2/15
# p = 1/15 para el resto de los datos
muestra = [5, 4, 9, 6, 21, 17, 11, 20, 7, 10, 21, 15, 13, 16, 8]


def calcularPeso(muestra):
    pesos = [(muestra.count(valor)/float(len(muestra))) for valor in muestra]

    return pesos

def mediaMuestral(lista):
    """
    Xbarra(n) = (x1+...+x2)/n
    """
    return sum(lista)/float(len(lista))


def varianzaMuestral(lista):
    """
    Scuadrado(n) = sumatoria(1, n, (xi - Xbarra(n))^2)/(n-1)
    """
    media_muestral = mediaMuestral(lista)

    return sum([(x - media_muestral)**2 for x in lista]) / float(len(lista) - 1)


def mediaFe(lista):
    """
    mu_Fe = (x1+...+x2)/n = E_Fe[Xbarra]
    """
    return sum(lista)/float(len(lista))


def varianzaFe(lista):
    """
    sigma^2_Fe = sumatoria(1, n, (xi - mu_Fe)^2)/n = E_Fe[Scuadrado]
    """
    media = mediaFe(lista)

    return sum([(x - media)**2 for x in lista]) / float(len(lista))


def bootstrap(B, muestra):
    """
    B = Numero de sorteos.
    muestra = Lista con los datos de la muestra.
    """
    media_muestral = mediaMuestral(muestra) # 12.2
    varianza_muestral = varianzaMuestral(muestra) # 34.3142

    media_Fe = mediaFe(muestra) # 12.2
    varianza_Fe = varianzaFe(muestra) # 32.03

    acumulador = 0
    # Hacemos el sorteo para B muestras aleatorias
    for _ in xrange(B):
        # temporal = Lista que contiene elementos de la muestra aplicando Bootstrap

        # Seleccionamos de forma aleatoria 15 elementos de la muestra
        # (se puede repetir) para el calculo de la expresion correspondiente
        temporal = [muestra[random.randint(0, 14)] for _ in xrange(15)]

        acumulador += (varianzaMuestral(temporal) - varianza_Fe)**2

    # Sacamos el promedio de los B terminos obtenidos
    var_Scuadrado = acumulador/float(B)

    return var_Scuadrado

# Generar U ~ U(0, 1)
# I = piso(n*U)+1
# X = X[I]

for B in [100, 1000, 10000, 100000, 1000000]:
    print("B =", B, "--> Var(S^2) =", bootstrap(B, muestra))
