# -*- coding: utf-8 -*-

import random
import math
from distribuciones import *


def esperanza_exponeciales():
    """
    Esperanza de Normal Estandar con Metodo de Exponenciales.
    """
    a = 0
    for _ in xrange(10000):
        a += normalEstadar1()

    return a/float(10000)


def esperanza_polar():
    """
    Esperanza de Normal Estandar con Metodo Polar.
    """
    a = 0
    for _ in xrange(10000):
        x, y = normalPolar1()
        a += x

    return a/float(10000)



print esperanza_exponeciales()
print esperanza_polar()
