# -*- coding: utf-8 -*-

import random
import math
from distribuciones import *


def tiempoAtencion():
    """
    Calcula el tiempo en que es atendido un cliente
    """
    Ts = exponencial(4.2) # Tiempo de servicio de cada cliente

    return Ts


def servidor():
    T = 1 # Tiempo en horas
    clientes = 3 # Clientes en el sistema

    tiempos = [] # Lista de tiempo de atencion de clientes en el sistema

    # Agregamos los tiempos de atencion de los clientes en el sistema
    for _ in xrange(3):
        tiempos.append(tiempoAtencion())

    tiempos.sort() # Ordenamos los tiempos de atencion de los clientes

    tiempo_espera = sum(tiempos)
    
    while True:
        print "T =", T
        T += tiempos[0] # Menor tiempo de atencion
        tiempos.pop(0) # Cliente termino de ser atendido

        if clientes <= 3:
            tiempos.append(tiempoAtencion()) # Cliente nuevo
            tiempo_espera += tiempos[2]
            clientes += 1
        tiempos.sort()

        if T >= 8:
            break

    return tiempo_espera/float(clientes)


print servidor()