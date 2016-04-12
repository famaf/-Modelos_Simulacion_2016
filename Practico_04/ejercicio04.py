# -*- coding: utf-8 -*-

import random
import math


def ejercicio04():
    """
    Ejericicio 04 del Practico 4.
    """
    # Metodo de composicion
    u = random.random()
    if u < 0.5:
        # Metodo de la Transformada Inversa
        u = random.random()
        j = 1
        pj = 0.5**j
        while u >= pj:
            j += 1
            pj += 0.5**j
        x = j
    else:
        # Metodo de la Transformada Inversa
        u = random.random()
        j = 1
        pj = 0.5*((float(2)/3)**j)
        while u >= pj:
            j += 1
            pj += 0.5*((float(2)/3)**j)
        x = j

    return x


print ejercicio04()


# def ejercicio04(n):
#     """
#     Ejericicio 04 del Practico 4.
#     """
#     a = 0
#     for _ in xrange(n):
#         # Metodo de composicion
#         u = random.random()
#         if u < 0.5:
#             # Metodo de la Transformada Inversa
#             u = random.random()
#             j = 1
#             pj = 0.5**j
#             while u >= pj:
#                 j += 1
#                 pj += 0.5**j
#             x = j
#         else:
#             # Metodo de la Transformada Inversa
#             u = random.random()
#             j = 1
#             pj = 0.5*((float(2)/3)**j)
#             while u >= pj:
#                 j += 1
#                 pj += 0.5*((float(2)/3)**j)
#             x = j
#         a += x

#     return float(a)/n

# for n in [100, 1000, 10000, 100000]:
#     print "n =", n, "--> E(X) =", ejercicio04(n)
