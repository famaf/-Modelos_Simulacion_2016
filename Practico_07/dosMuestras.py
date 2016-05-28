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

N = len(m1)
M = len(m2)

R = sumaRangos(m1, m2)
print R

P = [[[0 for k in xrange(R+1)] for j in xrange(M)] for i in xrange(N)]

for i in xrange(1, N):
    k = i * (i+1)/2.0
    for k in xrange(1, R):
        P[i][0][k] = 1

for k in xrange(1, R+1):
    for j in xrange(1, M):
        P[0][j][k-1] = 1


for i in xrange(1, N):
    for j in xrange(1, M):
        for k in xrange(1 ,R):
            if k < (i+j):
                P[i][j][k] = (j/float(i+j)) * P[i][j-1][k]
            else:
                P[i][j][k] = (i/float(i+j)) * P[i-1][j][k-i-j] + (j/float(i+j)) * P[i][j-1][k]

if P[N-1][M-1][R-1] < 1 - P[N-1][M-1][R-2]:
    V = P[N-1][M-1][R-1]
else:
    V = 1 - P[N-1][M-1][R-2]

print 2*V
