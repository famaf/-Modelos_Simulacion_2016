# -*- coding: utf-8 -*-

import random
import math


def calculoPromedio(lista):
    return sum(lista)/float(len(lista))


def bootstrap(B, muestra):
    """
    Ejericicio 6 b.
    B = Numero de sorteos.
    muestra = Lista con los datos de la muestra.
    """
    a, b = -5, 5 # Limites

    n = len(muestra) # Tamaño de la muestra

    exitos = 0 # Cantidad de veces que: a < v < b

    media_muestral = sum(muestra)/float(n) # Media muestral de la muestra dada (X barra)

    # Hacemos el sorteo para B muestras aleatorias
    for _ in xrange(B):
        # temporal = Lista que contiene elementos de la muestra aplicando Bootstrap

        # Seleccionamos de forma aleatoria 10 elementos de la muestra
        # (se puede repetir) para el calculo de la expresion correspondiente
        temporal = [muestra[random.randint(0, 9)] for _ in xrange(n)]

        v = calculoPromedio(temporal) - media_muestral # Calculamos la expresion

        # Si a < v < b ==> tenemos un exito
        if v > a and v < b:
            exitos += 1

    # La probabilidad esta dada las veces que se cumple la condicion sobre
    # las veces que se realizo
    p = exitos/float(B)

    return p


muestra = [56, 101, 78, 67, 93, 87, 64, 72, 80, 69] # Valores de la muetra obtenida

for B in [100, 1000, 10000, 100000]:
    # Si B = 1000000 ---> p = 0.761043
    print("B =", B, "---> p =", bootstrap(B, muestra))
