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
    muestra1 = [65.2, 67.1, 69.4, 78.4, 74, 80.3]
    muestra2 = [59.4, 72.1, 68, 66.2, 58.5]

    R = sumaRangos(muestra1, muestra2)

    print R


simulacion()
