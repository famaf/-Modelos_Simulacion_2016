# -*- coding: utf-8 -*-

import random


n = int(raw_input("Ingrese la cantidad de iteraciones: "))

LISTA = [random.uniform(0,1) for i in range(n)]

counter_win = 0

for element in LISTA:
    acumulador = 0
    if element < 0.5:
        acumulador += random.random() + random.random()
        if acumulador >= 1.0:
            # print "GANASTE"
            counter_win += 1
    else:
        acumulador += random.random() + random.random() + random.random()
        if acumulador >= 1.0:
            # print "GANASTE"
            counter_win += 1
            
probabilidad = float(counter_win)/n

print probabilidad

