# -*- coding: utf-8 -*-

import random
import math

muestra = [5, 4, 9, 6, 21, 17, 11, 20, 7, 10, 21, 15, 13, 16, 8]
muestra2 = [1, 3]


def promedio(lista):
    suma = sum(lista)

    return suma/float(len(lista))


def varianza(lista):
    media = promedio(lista)

    a = 0
    for i in lista:
        a += (i - media)**2

    return a


def svar(muestra):
    s = varianza(muestra)/float(len(muestra) - 1)

    return (s - varianza(muestra)/float(len(muestra)))



print svar(muestra2)
