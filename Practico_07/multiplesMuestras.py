# -*- coding: utf-8 -*-

from distribuciones import *


def sumaRangos(muestra1, muestra):
    muestra.sort()

    rangos = []

    for valor in muestra1:
        rangos.append(muestra.index(valor) + 1)

    R = sum(rangos)

    return R



muestra1 = [2, 7, 9]
muestra2 = [3, 5, 6]
muestra3 = [4, 8, 10]

m = 3

n1 = len(muestra1)
n2 = len(muestra2)
n3 = len(muestra3)

tamanos = [n1, n2, n3]


muestra = muestra1+muestra2+muestra3 # Muestra general

n = sum(tamanos) # Tamaño de la muestra general


R1 = sumaRangos(muestra1, muestra) # Rango de la muestra 1
R2 = sumaRangos(muestra2, muestra) # Rango de la muestra 1
R3 = sumaRangos(muestra3, muestra) # Rango de la muestra 1

Rs = [R1, R2, R3]

esp_R1 = n1 * (n + 1)/2.0 # Esperanza de la muestra 1

var_R1 = n1 * (n2+n3) * (n+1)/12.0 # Varianza de la muestra 1 --> nose si esta bien

# Estadistico
p1 = 12.0/(n*(n+1))
suma = 0
for i in xrange(m):
    suma += ((Rs[i] - (tamanos[i]*(n+1))/2.0)**2)/float(tamanos[i])
R = p1 * suma


y = R
grados_libertad = m - 1

p_valor = pValor(grados_libertad, y)


print "R =", R
print "p-valor =", p_valor
