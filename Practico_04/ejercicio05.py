# -*- coding: utf-8 -*-

import random
import math


def poisson(n, lamb):
    pn = math.exp(-lamb)
    i = 1
    while i <= n:
        pn *= (lamb/float(i))
        i += 1
   
    return pn


def ejercicio05(k, l):
    pn = 1
    j = 1
    while j <= k:
        pn += (l/float(i))
        j += 1
    
    denominador = math.exp(-l)*pn
    
    u = random.random()
    u *= denominador
    
    i = 0
    
    pi = 1
    
    while u >= math.exp(-l)*pi:
        i += 1
        pi += 

print ejercicio05(2, 1)
