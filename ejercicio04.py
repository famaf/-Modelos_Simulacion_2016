# -*- coding: utf-8 -*-

import random
import math


def ejercicio04a(n):
    a = 0
    last_factorial = 1
    for i in xrange(1, n+1):
        a += 1.0/(last_factorial*i)
        last_factorial = last_factorial*i

    return a+1


L = [100, 1000, 10000, 100000, 1000000]

print ejercicio04a(170) # si n > 170 da error: overflow

#print math.e
# for n in L:
#     print "e =", ejercicio04a(n)



# def factorial(n):
#     last_factorial = 1
#     for i in range(1, n+1):
#         last_factorial *= i

#     return last_factorial

# print factorial(6)