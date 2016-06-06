Calculo recursivo Xbarra(n):
============================
Xbarra(1) = X1
Xbarra(j+1) = Xbarra(j) + (Xj+1 - Xbarra(j))/(j+1)


Calculo recursivo Scuadrado(n):
===============================
Scuadrado(1) = 0
Scuadrado(j+1) = (1 - 1/j)*Scuadrado(j) + (j+1)*(Xbarra(j+1) - Xbarra(j))^2



Algoritmo 1: Estimacion de la media M de X con error d
======================================================
Generar X
M = X # M = Xbarra(1) = X1
Scuadrado = 0 # Scuadrado = Scuadrado(1) = 0
J0 = 30 # Minimo simulaciones

for 2 <= j <= J0 do
    Generar X
    A = M
    M = M + (X - M)/j
    Scuadrado = (1 - 1/(j-1))*Scuadrado + j*(M-A)^2
end

j = J0

while sqrt(Scuadrado/j) > d do
    j = j + 1
    Generar X
    A = M
    M = M + (X - M)/j
    Scuadrado = (1 - 1/(j-1))*Scuadrado + j*(M-A)^2
end

return M


# Xbarra estima a p --> p = Xbarra
# Var(Xbarra) = (Xbarra * (1-Xbarra))/n
Algoritmo 2: Estimacion de la probabilidad p de X con error d
=============================================================
Generar X # X es 0 (con probabilidad 1-p) ó 1 (con probabilidad p) --> random()
p = X

for 1 < j <= 100 do
    Generar X
    p = p + (X - p)/j
end

j = 100

while sqrt( (p * (1-p))/j ) > d do
    j = j + 1
    Generar X
    p = p + (X - p)/j
end

return p



a = Xbarra - Z_alfa/2 * sqrt( (Xbarra * (1 - Xbarra))/n )
b = Xbarra + Z_alfa/2 * sqrt( (Xbarra * (1 - Xbarra))/n )
IC --> (a, b)
Longitud --> 2 * Z_alfa/2 * sqrt( (Xbarra * (1 - Xbarra))/n )
