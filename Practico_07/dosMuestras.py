# Programar para tomar promedio si hay datos repetidos

def sumaRangos(muestra1, muestra2):
    muestra = muestra1 + muestra2
    muestra.sort()

    rangos = []
    # Calculo los rangos de la muestra 1
    for valor in muestra1:
        rangos.append(muestra.index(valor) + 1)

    R = sum(rangos) # Suma de los rangos

    return R

m1 = [342, 448, 504, 361, 453]
m2 = [186, 220, 225, 456, 276, 199, 371, 426, 242, 311]

m1 = [2, 3, 4]
m2 = [3, 5, 7]

n = len(m1)
m = len(m2)

R = sumaRangos(m1, m2)
print "R =", R
