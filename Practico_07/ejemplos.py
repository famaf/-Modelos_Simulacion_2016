# -*- coding: utf-8 -*-

import math
import random
from distribuciones import *


#################################
# Bondad de ajuste - Practico 7 #
#################################


def estadisticoT(k, n, N, p):
    """
    Calcula el estadistico T.
    k = particiones (intervalos).
    n = tamaño de la muestra.
    N = vector de valores (Frecuencia Observada) de tamaño k.
    p = valores de valores (Frecuencia Esperada) de tamaño k
    """
    T = 0
    for i in xrange(k):
        T += ((N[i] - n*p[i])**2)/float(n*p[i])

    return T


def acumuladaExponencial(x, lamda):
    """
    Funcion de distribucion acumulada de una exponencial.
    """
    return 1 - math.exp(-lamda*x)


def ejemplo01():
    """
    Distribucion exponencial con Chi-Cuadrado.
    """
    lamda = 0.399
    n = 219 # Tamaño de la muestra
    k = 10 # Cantidad de intervalos
    N = [19, 28, 26, 12, 25, 14, 22, 29, 20, 24]
    prob = [0.1 for _ in xrange(k)]
    t = estadisticoT(k, n, N, prob) # Valor observado

    grados_libertad = k - 1 # En este caso son 9

    p_valor = pValor(grados_libertad, t)

    return p_valor


def probabilidadGeometrica(p, i):
    return p * ((1-p)**(i-1))


def ejemplo02():
    """
    Distribucion Geometrica con Chi-Cuadrado.
    """
    # Intervalos:
    # {1}
    # {2, 3}
    # {4, 5, ...}
    p = 0.346
    n = 159 # Tamaño de la muestra
    k = 3 # Cantidad de intervalos
    N = [59, 50, 47]

    p1 = probabilidadGeometrica(p, 1)
    p2 = probabilidadGeometrica(p, 2) + probabilidadGeometrica(p, 3)
    p3 = 1.0 - p1 - p2
    prob = [p1, p2, p3]

    t = estadisticoT(k, n, N, prob) # Valor observado

    grados_libertad = k - 1 # En este caso son 2

    p_valor = pValor(grados_libertad, t)

    return p_valor


def ejemplo03():
    n = 50 # Tamaño de la muestra
    k = 5 # Cantidad de intervalos
    N = [12, 5, 19, 7, 7]
    prob = [0.2 for _ in xrange(k)]
    t = estadisticoT(k, n, N, prob) # Valor observado

    grados_libertad = k - 1 # En este caso son 9

    p_valor = pValor(grados_libertad, t)

    return p_valor


def pValorKS(r, n, d):
    """
    r = Numero de simulaciones
    n = Tamaño de la muestra
    d = Valor observado
    """
    uniformes = []
    valoresD = []
    exitos = 0 # Cantidad de veces que se cumple que D >= d

    for _ in xrange(r):
        # Generamos n U ~ U(0, 1) y las ordenamos
        uniformes = [random.random() for _ in xrange(n)]
        uniformes.sort()

        # Calculamos el estadistico D correspondiente
        j = 1
        for U in uniformes:
            valoresD.append(j/float(n) - U)
            valoresD.append(U - (j-1)/float(n))
            j += 1

        D = max(valoresD)

        # Si D >= d --> es un exito
        if D >= d:
            exitos += 1

        # Vaciamos las listas: uniformes y valoresD
        uniformes = []
        valoresD = []

    p_valor = exitos/float(r)

    return p_valor


def ejemplo04(alfa):
    """
    Distribucion exponencial con KS.
    """
    lamda = 1/100.0
    valores = [66, 72, 81, 94, 112, 116, 124, 140, 145, 155]
    valores.sort()

    n = len(valores) # Tamaño de la muestra

    # Calculamos el estadistico D
    valoresD = [] # Contendra los elementos del conjunto D+ y D-
    j = 1
    for valor in valores:
        F = acumuladaExponencial(valor, lamda)
        valoresD.append(j/float(n) - F)
        valoresD.append(F - (j-1)/float(n))
        j += 1

    d = max(valoresD) # Valor observado

    p_valor = pValorKS(10000, n, d)

    if p_valor < alfa:
        return "Se rechaza H0 --> p-valor = " + str(p_valor)
    elif p_valor > alfa:
        return "No se rechaza H0 --> p-valor = " + str(p_valor)


def probabilidadPoisson(lamda, i):
    return math.exp(-lamda) * ((lamda**i)/(math.factorial(i)))


def ejemplo05():
    """
    Distribucion Poisson con Chi-Cuadrado.
    """
    # Intervalos:
    # {0}
    # {1}
    # {2}
    # {3}
    # {4}
    # {5, 6, ...}
    n = 30
    datos = [0, 0, 0, 0, 0, 0, 1, 1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 8]
    N = [6, 2, 1, 9, 7, 5] # Frecuencias observadas

    # Estimemos lambda
    lamda = sum(datos)/float(n) # Media muestral

    k = 6 # Cantidad de intervalos

    # Probabilidades
    p0 = probabilidadPoisson(lamda, 0)
    p1 = probabilidadPoisson(lamda, 1)
    p2 = probabilidadPoisson(lamda, 2)
    p3 = probabilidadPoisson(lamda, 3)
    p4 = probabilidadPoisson(lamda, 4)
    p5 = 1.0 - p0 - p1 - p2 - p3 - p4
    prob = [p0, p1, p2, p3, p4, p5]

    t = estadisticoT(k, n, N, prob)

    m = 1 # Cantidad de parametros estimados

    grados_libertad = k - m - 1 # En este caso serian 4

    p_valor = pValor(grados_libertad, t)

    return p_valor


def ejemplo05Prima(r):
    """
    Distribucion Poisson con Simulacion.
    TERMINAR PARTE DE LOS Nj
    """
    # Intervalos:
    # {0}
    # {1}
    # {2}
    # {3}
    # {4}
    # {5, 6, ...}
    n = 30
    datos = [0, 0, 0, 0, 0, 0, 1, 1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 8]
    N = [6, 2, 1, 9, 7, 5] # Frecuencias observadas

    k = 6 # Cantidad de intervalos

    # Estimamos lambda
    lamda = sum(datos)/float(n) # Media muestral

    # Probabilidades
    p0 = probabilidadPoisson(lamda, 0)
    p1 = probabilidadPoisson(lamda, 1)
    p2 = probabilidadPoisson(lamda, 2)
    p3 = probabilidadPoisson(lamda, 3)
    p4 = probabilidadPoisson(lamda, 4)
    p5 = 1.0 - p0 - p1 - p2 - p3 - p4
    prob = [p0, p1, p2, p3, p4, p5]

    t = estadisticoT(k, n, N, prob)

    exitos = 0 # Cantidad de veces que T >= t

    for _ in xrange(r):
        Y = []
        # Generamos 30 va Poisson con media lambda 2.9
        for _ in xrange(n):
            Y.append(poisson(lamda))

        # Generamos los N
        N0 = 0
        N1 = 0
        N2 = 0
        N3 = 0
        N4 = 0
        N5 = 0
        for j in xrange(n):
            if Y[j] == 0:
                N0 += 1
            elif Y[j] == 1:
                N1 += 1
            elif Y[j] == 2:
                N2 += 1
            elif Y[j] == 3:
                N3 += 1
            elif Y[j] == 4:
                N4 += 1
            elif Y[j] >= 5:
                N5 += 1
        N = [N0,N1,N2,N3,N4,N5]

        # Estimamos lambda segun la nueva muestra
        lamda_sim = sum(Y)/float(n)

        # Generamos las nuevas Probabilidades
        p0 = probabilidadPoisson(lamda_sim, 0)
        p1 = probabilidadPoisson(lamda_sim, 1)
        p2 = probabilidadPoisson(lamda_sim, 2)
        p3 = probabilidadPoisson(lamda_sim, 3)
        p4 = probabilidadPoisson(lamda_sim, 4)
        p5 = 1.0 - p0 - p1 - p2 - p3 - p4
        prob = [p0, p1, p2, p3, p4, p5]

        T = estadisticoT(k, n, N, prob)

        if T >= t:
            exitos += 1

    p_valor = exitos/float(r)

    return p_valor

print "########## Test de Bondad ##########"
print "Ejemplo 1 --> p-valor =", ejemplo01()
print "Ejemplo 2 --> p-valor =", ejemplo02()
print "Ejemplo 3 --> p-valor =", ejemplo03()
print "Ejemplo 4 -->", ejemplo04(0.05)
print "Ejemplo 5 --> p-valor =", ejemplo05()
print "Ejemplo 5 Prima --> p-valor =", ejemplo05Prima(10000)




###############################
# Suma de Rangos - Practico 7 #
###############################

##########################################
# Caso de datos repetidos, ejemplo:
# m1 = [2, 3, 4]
# m2 = [3, 5, 7]
# m = [2, 3, 3, 4, 5, 7]
# R = sumaRangos(m1, m) "promedio de los rangos"
# ==> R = 1 + 2.5 + 4 = 7.5
##########################################


def sumaRangos(muestra1, muestra):
    """
    Calcula la suma de los rangos (R) de la 'muestra1' sobre la 'muestra'.
    """
    muestra.sort()

    rangos = []
    # Calculo los rangos de la muestra 1
    for valor in muestra1:
        rangos.append(muestra.index(valor) + 1)

    R = sum(rangos) # Suma de los rangos

    return R


def P(n, m, k):
    """
    Calcula la probabilidad P (dado n, m) de k.
    """
    # Casos base 1: n = 1 y m = 0
    if n == 1 and m == 0:
        if k <= 0:
            result = 0
        else:
            result = 1
    # Casos base 2: n = 0 y m = 1
    elif n == 0 and m == 1:
        if k < 0:
            result = 0
        else:
            result = 1
    # Casos Recursivos: n >= 1 y m >= 1
    else:
        # Caso especial 1: n = 0 y m >= 2
        if n == 0:
            result = (m/float(m+n)) * P(n, m-1, k)
        # Caso especial 2: n >= 2 y m >= 0
        elif m == 0:
            result = (n/float(n+m)) * P(n-1, m, k-n-m)
        # Caso general
        else:
            result = (n/float(n+m)) * P(n-1, m, k-n-m) + (m/float(m+n)) * P(n, m-1, k)

    return result


def ejemplo06():
    """
    Calcula la suma de rangos.
    """
    m1 = [1, 7, 5, 4]
    m2 = [3, 2, 9]

    m = m1+m2

    R = sumaRangos(m1, m)

    return R


def ejemplo07():
    """
    Calcula la suma de rangos.
    """
    m1 = [342, 448, 504, 361, 453]
    m2 = [186, 220, 225, 456, 276, 199, 371, 426, 242, 311]

    m = m1+m2

    R = sumaRangos(m1, m)

    return R


def ejemplo08Exacto():
    """
    Calculo exacto del p-valor.
    """
    muestra1 = [132, 104, 162, 171, 129]
    muestra2 = [107, 94, 136, 99, 114, 122, 108, 130, 106, 88]
    muestra = muestra1 + muestra2

    n = len(muestra1) # Tamaño de la primera muestra
    m = len(muestra2) # Tamaño de la segunda muestra

    R = sumaRangos(muestra1, muestra)

    # Calculo de p-valor por recursion
    p_valor = 2 * min(P(n, m, R), 1 - P(n, m, R-1))

    return p_valor


def ejemplo08Normal():
    """
    Calculo del p-valor, con una aproximacion normal.
    """
    muestra1 = [132, 104, 162, 171, 129]
    muestra2 = [107, 94, 136, 99, 114, 122, 108, 130, 106, 88]
    muestra = muestra1 + muestra2

    n = len(muestra1) # Tamaño de la primera muestra
    m = len(muestra2) # Tamaño de la segunda muestra
    N = n + m # Tamaño de la suma de las muestras

    R = sumaRangos(muestra1, muestra)

    esp_R = n * (N+1)/2.0 # Esperanza de R
    var_R = n * m * (N+1)/12.0 # Varianza de R

    z = (R - esp_R)/math.sqrt(var_R) # Normalizacion a una N(0, 1)

    # Calculo del p-valor
    if R <= esp_R:
        p_valor = 2 * fi(z)
    else:
        p_valor = 2 * (1 - fi(z))

    return p_valor


def ejemplo08Simulado(k):
    """
    Calculo del p-valor, mediante simulacion.
    """
    muestra1 = [132, 104, 162, 171, 129]
    muestra2 = [107, 94, 136, 99, 114, 122, 108, 130, 106, 88]
    muestra = muestra1 + muestra2

    n = len(muestra1) # Tamaño de la primera muestra
    m = len(muestra2) # Tamaño de la segunda muestra

    r = sumaRangos(muestra1, muestra)

    R_max = 0 # Cantidad de veces que R >= r
    R_min = 0 # Cantidad de veces que R <= r

    # Ejecutamos k veces la simulacion
    for _ in xrange(k):
        # Calculamos la submuestra
        random.shuffle(muestra) # Desordenamos la muestra

        # Obtenemos la submuestra
        sub_muestra = muestra[0:n] # Nos quedamos con los primeros 'n' elementos

        R = sumaRangos(sub_muestra, muestra) # Generamos el R correspondiente

        if R >= r:
            R_max += 1
        elif R < r:
            R_min += 1

    # Calculo del p-valor
    p_valor = 2 * min(R_max/float(k), R_min/float(k))

    return p_valor


print "\n########## Suma de rangos ###########"
print "Ejemplo 6 --> R =", ejemplo06()
print "Ejemplo 7 --> R =", ejemplo07()
print "Ejemplo 8 Exacto --> p-valor =", ejemplo08Exacto()
print "Ejemplo 8 Normal --> p-valor =", ejemplo08Normal()
print "Ejemplo 8 Simulado --> p-valor =", ejemplo08Simulado(10000)
