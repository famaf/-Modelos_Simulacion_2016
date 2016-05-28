# -*- coding: utf-8 -*-

import math
import random
from distribuciones import *


def sumaRangos(muestra1, muestra2):
    muestra = muestra1 + muestra2
    muestra.sort()

    rangos = []
    # Calculo los rangos de la muestra 1
    for valor in muestra1:
        rangos.append(muestra.index(valor) + 1)

    R = sum(rangos) # Suma de los rangos

    return R


def simulacion():
    muestra1 = [19, 31, 39, 45, 47, 66, 75]
    muestra2 = [28, 36, 44, 49, 52, 72, 72]

    R = sumaRangos(muestra1, muestra2)

    print R


simulacion()
