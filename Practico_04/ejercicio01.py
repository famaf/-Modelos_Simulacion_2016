# -*- coding: utf-8 -*-

import random
import math


def permutacion(lista):
    k = len(lista) - 1
    while k >= 0:
        u = random.random()
        i = int(math.floor(k*u))
        lista[k], lista[i] = lista[i], lista[k]
        k -= 1
    return lista


def esperanza(n):
    exito = 0
    for _ in xrange(n):
        mazo = range(1, 101) # Lista de 100 cartas
        random.shuffle(mazo) # Desordena el mazo
        exito += sum([mazo[i-1]==i for i in xrange(1, 101)])
    return float(exito)/n


def varianza(n):
    exito1 = 0
    exito2 = 0
    for _ in xrange(n):
        mazo = range(1, 101) # Lista de 100 cartas
        random.shuffle(mazo) # Desordena el mazo
        evento = sum([mazo[i-1]==i for i in xrange(1, 101)])
        
        exito1 += evento
        exito2 += evento**2
    
    esperanza = exito1/float(n)
    varianza = exito2/float(n) - esperanza**2
    
    return varianza



print "E(X) =", esperanza(10000)
print "V(X) =", varianza(10000)

