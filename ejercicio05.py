# -*- coding: utf-8 -*-

import random
import math


def ejercicio05a(n):
    """
    Ejercicio 5a del Practico 3.
    """
    a = 0
    for i in xrange(n):
        N = 0
        p = 1

        while p >= math.e**(-3):
            p *= random.random()
            N += 1
        
        a += N

    return float(a)/n


def ejercicio05b(i):
    """
    Ejercicio 5b del Practico 3.
    """
    exitos = 0
    limite = math.e**(-3)
    for _ in xrange(1000000):
        if i == 0:
            pass
        if i == 1:
            u = random.random()
            if u < limite:
                exitos += 1
        if i == 2:
            u = random.random()
            if u >= limite:
                u *= random.random()
                if u < limite:
                    exitos += 1
        if i == 3:
            u = random.random() + random.random()
            if u >= limite:
                u *= random.random()
                if u < limite:
                    exitos +=1
        if i == 4:
            u = random.random() + random.random() + random.random()
            if u >= limite:
                u *= random.random()
                if u < limite:
                    exitos +=1
        if i == 5:
            u = random.random() + random.random() + random.random() + random.random()
            if u >= limite:
                u *= random.random()
                if u < limite:
                    exitos +=1
        if i == 6:
            u = random.random() + random.random() + random.random() + random.random() + random.random()
            if u >= limite:
                u *= random.random()
                if u < limite:
                    exitos +=1

    return float(exitos)/1000000


for n in [100, 1000, 10000, 100000, 1000000]:
    print "E(N) =", ejercicio05a(n)

print "----------------------"

for i in xrange(7):
    print "P(N = %d)" % i, "=", ejercicio05b(i)
