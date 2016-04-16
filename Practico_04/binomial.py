# Generacion de una va Binomial B(n, p)

import math
import random

def binomial(n, p):
    u = random.random()
    i = 0
    c = float(p)/(1-p)
    Pr = (1-p)**n
    F = Pr
    while u >= F:
        Pr = math.floor((c*(n-i))/float(i+1)) * Pr
        F += Pr
        i += 1

    x = i


