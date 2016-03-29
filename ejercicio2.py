# -*- coding: utf-8 -*-

import random


n = int(raw_input("Ingrese la cantidad de iteraciones: "))

LISTA = [random.uniform(0,1) for i in range(n)]

counter_win = 0

for element in LISTA:
    acumulador = 0
    if element < 0.5:
        acumulador += random.random() + random.random()
    else:
        acumulador += random.random() + random.random() + random.random()

    if acumulador >= 1.0:
        # print "GANASTE"
        counter_win += 1

probabilidad = float(counter_win)/n

print probabilidad


# Codigo del profe XD
#import numpy as np

#def ej2c(n):
#    for _ in xrange(n):
 #       # simula u
 #       u = np.random.random()
 #       
 #       # simula x
 #       if u < 0.5:
 #           x = np.random.random() + np.random.random()
 #       else:
 #           x = np.random.random() + np.random.random() + np.random.random()
 #   
 #       # actualiza cuenta de casos de exito (evento (X>=1))
 #       if x >= 1.0:
 #           exito += 1
 #   
# v   return float(exitos)/n

#print "P(X>=1) = ", ej2c(100)

