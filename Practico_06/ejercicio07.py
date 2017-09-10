# -*- coding: utf-8 -*-

import random
import math

# 2 observaciones
muestra = [1, 3]

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


def bootstrap(muestra):
    """
    muestra = Lista con los datos de la muestra.
    """
    # Xbarra y Scuadrado
    media_muestral = mediaMuestral(muestra)
    varianza_muestral = varianzaMuestral(muestra)

    # mu_Fe y sigma^2_Fe
    media_Fe = mediaFe(muestra)
    varianza_Fe = varianzaFe(muestra)

    # Acumulan los resultados de la sumatoria
    acumulador1 = 0
    acumulador2 = 0

    # Las 4 posibilidades
    temporal1 = [1, 1]
    temporal2 = [1, 3]
    temporal3 = [3, 1]
    temporal4 = [3, 3]

    temporal = [temporal1, temporal2, temporal3, temporal4]

    for fila in temporal:
        acumulador1 += (mediaMuestral(fila) - media_Fe)**2
        acumulador2 += (varianzaMuestral(fila) - varianza_Fe)**2

    # Calculamos Var(Xbarra) y Var(S^2)
    var_Xbarra = acumulador1/4.0
    var_Scuadrado = acumulador2/4.0

    return var_Xbarra, var_Scuadrado


var_Xbarra, var_Scuadrado = bootstrap(muestra)
print("Var(Xbarra) =",var_Xbarra)
print("Var(S^2) =", var_Scuadrado)
print(calcularPeso(muestra))
