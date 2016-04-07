# -*- coding: utf-8 -*-

import random
import math

# L = range(1, 101) # Lista de 100 cartas

def permutacion(lista):
    k = len(lista) - 1
    while k >= 0:
        u = random.random()
        i = int(math.floor(k*u))
        lista[k], lista[i] = lista[i], lista[k]
        k -= 1
    return lista
    
L = range(1, 11)

print permutacion(L)
