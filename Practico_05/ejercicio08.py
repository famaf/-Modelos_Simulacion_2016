# -*- coding: utf-8 -*-

import random
import math
from distribuciones import *


def esperanza_exponeciales(n):
    """
    Esperanza de Normal Estandar con Metodo de Exponenciales.
    """
    a = 0
    for _ in xrange(n):
        a += normalEstadar1()

    return a/float(n)


def esperanza_polar(n):
    """
    Esperanza de Normal Estandar con Metodo Polar.
    """
    a = 0
    for _ in xrange(n):
        x, y = normalPolar1()
        a += x

    return a/float(n)



print esperanza_exponeciales(10000)
print esperanza_polar(10000)
