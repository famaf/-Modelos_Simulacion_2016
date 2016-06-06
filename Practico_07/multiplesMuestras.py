from distribuciones import *

def sumaRangos(muestra1, muestra):
    muestra.sort()

    rangos = []

    for valor in muestra1:
        rangos.append(muestra.index(valor) + 1)

    R = sum(rangos)

    return R


m1 = [2, 7, 9]
m2 = [3, 5, 6]
m3 = [4, 8, 10]

cantidad_muestras = 3

m = m1+m2+m3 # Muetra general

tamanos = [len(m1), len(m2), len(m3)]

n = sum(tamanos) # Tamano de la muestra general


R1 = sumaRangos(m1, m) # Rango de la muestra 1
R2 = sumaRangos(m2, m) # Rango de la muestra 1
R3 = sumaRangos(m3, m) # Rango de la muestra 1

Rs = [R1, R2, R3]

esp_R1 = len(m1) * (n + 1)/2.0 # Esperanza de la muestra 1

var_R1 = len(m1) * (len(m2)+len(m3)) * (n+1)/12.0 # Varianza de la muestra 1

# Estadistico
p1 = 12.0/(n*(n+1))
suma = 0
for i in xrange(cantidad_muestras):
    suma += ((Rs[i] - (tamanos[i]*(n+1))/2.0)**2)/float(tamanos[i])

R = p1 * suma
print "R =", R

y = R
grados_libertad = cantidad_muestras - 1

p_valor = pValor(grados_libertad, y)

print "p-valor =", p_valor
