# -*- coding: utf-8 -*-

import random

def ejercicio02c(n):

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


print "n = 100 => P(X>=1) =", ejercicio02c(100)
print "n = 1000 => P(X>=1) =", ejercicio02c(1000)
print "n = 10000 => P(X>=1) =", ejercicio02c(10000)
print "n = 100000 => P(X>=1) =", ejercicio02c(100000)
