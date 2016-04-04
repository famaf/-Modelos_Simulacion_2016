# -*- coding: utf-8 -*-

import random

def ejercicio02c(n):
    """
    Ejericio 2c del Practico 3.
    """
    exitos = 0
    for _ in xrange(n):

       u = random.random() # Simula U
       
       # Simula X
       if u < 0.5:
           x = random.random() + random.random()
       else:
           x = random.random() + random.random() + random.random()

       # Actualiza la cuenta de casos de exito (evento (X>=1))
       if x >= 1.0:
           exitos += 1

    return float(exitos)/n



for n in [100, 1000, 10000, 100000]:
    print "n =", n, "--> P(X >= 1) =", ejercicio02c(n)
