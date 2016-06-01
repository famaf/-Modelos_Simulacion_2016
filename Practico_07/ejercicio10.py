# -*- coding: utf-8 -*-

import math
import random
from distribuciones import *


def sumaRangos(muestra1, muestra2):
    """
    Calcula la suma de los rangos (R) de la muestra 1.
    """
    muestra = muestra1 + muestra2
    muestra.sort()

    rangos = []
    # Calculo los rangos de la muestra 1
    for valor in muestra1:
        rangos.append(muestra.index(valor) + 1)

    R = sum(rangos) # Suma de los rangos

    return R


def P(n, m, k):
    """
    Calcula la probabilidad P (dado n, m) de k.
    """
    # Casos base 1: n = 1 y m = 0
    if n == 1 and m == 0:
        if k <= 0:
            result = 0
        else:
            result = 1
    # Casos base 2: n = 0 y m = 1
    elif n == 0 and m == 1:
        if k < 0:
            result = 0
        else:
            result = 1
    # Casos Recursivos: n >= 1 y m >= 1
    else:
        # Caso especial 1: n = 0 y m >= 2
        if n == 0:
            result = (m/float(m+n)) * P(n, m-1, k)
        # Caso especial 2: n >= 2 y m >= 0
        elif m == 0:
            result = (n/float(n+m)) * P(n-1, m, k-n-m)
        # Caso general
        else:
            result = (n/float(n+m)) * P(n-1, m, k-n-m) + (m/float(m+n)) * P(n, m-1, k)

    return result


def valorExacto():
    """
    Calculo exacto del p-valor.
    """
    muestra1 = [19, 31, 39, 45, 47, 66, 75]
    muestra2 = [28, 36, 44, 49, 52, 72, 72]

    n = len(muestra1) # Tamaño de la primera muestra
    m = len(muestra2) # Tamaño de la segunda muestra

    R = sumaRangos(muestra1, muestra2)

    # Calculo de p-valor por recursion

    p_valor = 2 * min(P(n, m, R), 1 - P(n, m, R-1))

    return p_valor


def aproximacionNormal():
    """
    Calculo del p-valor, con una aproximacion normal.
    """
    muestra1 = [19, 31, 39, 45, 47, 66, 75]
    muestra2 = [28, 36, 44, 49, 52, 72, 72]

    n = len(muestra1) # Tamaño de la primera muestra
    m = len(muestra2) # Tamaño de la segunda muestra

    N = n + m # Tamaño de la suma de las muestras

    R = sumaRangos(muestra1, muestra2)

    esp_R = n * (N+1)/2.0 # Esperanza de R
    var_R = n * m * (N+1)/12.0 # Varianza de R

    z = (R - esp_R)/math.sqrt(var_R) # Normalizacion a una N(0, 1)

    # Calculo del p-valor
    if R <= esp_R:
        p_valor = 2 * fi(z)
    else:
        p_valor = 2 * (1 - fi(z))

    return p_valor


def simulacion(k):
    """
    Calculo del p-valor, con una simulacion
    """
    muestra1 = [19, 31, 39, 45, 47, 66, 75]
    muestra2 = [28, 36, 44, 49, 52, 72, 72]

    n = len(muestra1) # Tamaño de la primera muestra
    m = len(muestra2) # Tamaño de la segunda muestra

    N = n + m # Tamaño de la suma de las muestras

    r = sumaRangos(muestra1, muestra2)

    # Lista con las dos muestras ordenadas
    muestra = muestra1 + muestra2
    muestra.sort()

    R_mayor = 0 # Cantidad de veces que R >= r
    R_menor = 0 # Cantidad de veces que R <= r

    # Ejecutamos k veces la simulacion
    for _ in xrange(k):
        sub_muestra = [] # Contendra la submuestra
        while len(sub_muestra) < n:
            valor = muestra[random.randint(0, N-1)] # 
            
            # Si el valor no esta en la submuestra, lo agrego
            if valor not in sub_muestra:
                sub_muestra.append(valor)

        R = sumaRangos(sub_muestra, muestra2) # Generamos el R correspondiente

        if R >= r:
            R_mayor += 1
        elif R <= r:
            R_menor += 1

    pro_R_mayor = R_mayor/float(k)
    pro_R_menor = R_menor/float(k)

    # Calculo del p-valor
    p_valor = 2 * min(pro_R_menor, pro_R_mayor)

    return p_valor



print "Valor Exacto =", valorExacto()
print "Aprocimacion Normal =", aproximacionNormal()
print "Simulacion =", simulacion(100000)
