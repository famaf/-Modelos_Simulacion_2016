# -*- coding: utf-8 -*-

import math
import random
from scipy.special import ndtr, ndtri # Normal
from scipy.special import chdtrc, chdtri # Chi-cuadrado


########################
##### Ejercicio 02 #####
########################

def sumaRangos(m1, m):
    """
    Calcula la suma de los rangos (R) de la 'muestra1' sobre la 'muestra'.
    """
    m.sort()
    rangos = []

    for valor in m1:
        cantidad_valor = m.count(valor)
        if cantidad_valor == 1:
            rangos.append(m.index(valor) + 1)
        else:
            indice1 = m.index(valor) + 1
            indice2 = indice1 + 1
            rangos.append((indice1+indice2)/float(cantidad_valor))

    R = sum(rangos)

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


def ej2d(alfa):
    """
    Ejercicio 02.
    """
    claustro1 = [35, 128, 20, 3, 41] # Primera muestra
    claustro2 = [12, 27, 9, 3, 11] # Segunda muestra

    muestra = claustro1 + claustro2 # Muestra general

    n = len(claustro1) # Tamaño de la primera muestra
    m = len(claustro2) # Tamaño de la segunda muestra

    R = sumaRangos(claustro1, muestra)

    p_valor = 2 * min(P(n, m, R), 1 - P(n, m, R-1))

    if p_valor < alfa:
        print("Chi-Cuadrado: Se rechaza H0 a un nivel", alfa, "--> p-valor =", p_valor)
    elif p_valor > alfa:
        print("Chi-Cuadrado: No se rechaza H0 a un nivel", alfa, "--> p-valor =", p_valor)


def ej2e(alfa, k):
    """
    Calculo del p-valor, mediante simulacion.
    """
    claustro1 = [35, 128, 20, 3, 41] # Primera muestra
    claustro2 = [12, 27, 9, 3, 11] # Segunda muestra

    muestra = claustro1 + claustro2 # Muestra general

    n = len(claustro1) # Tamaño de la primera muestra
    m = len(claustro2) # Tamaño de la segunda muestra

    r = sumaRangos(claustro1, muestra)

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
        if R <= r:
            R_min += 1

    # Calculo del p-valor
    p_valor = 2 * min(R_max/float(k), R_min/float(k))

    if p_valor < alfa:
        print("Simulacion: Se rechaza H0 a un nivel", alfa, "--> p-valor =", p_valor)
    elif p_valor > alfa:
        print("Simulacion: No se rechaza H0 a un nivel", alfa, "--> p-valor =", p_valor)


def printEj2d():
    ej2d(0.05)

def printEj2e():
    ej2e(0.05, 10000)

# printEj2d()
# printEj2e()

########################
##### Ejercicio 03 #####
########################

def calcularMedia(muestra):
    """
    Calcula la media (mu) de una muestra dada.
    """
    mu = sum(muestra)/float(len(muestra))

    return mu


def ej3(B):
    """
    Ejercicio 03.
    B = Numero de sorteos.
    """
    muestra = [0.615, 0.622, 0.631, 0.617, 0.617, 0.620, 0.621, 0.620, 0.627, 0.611]

    n = len(muestra) # Tamaño de la muestra --> n = 10

    exitos = 0 # Cantidad de veces que: -0.01 <= v < 0.01

    mu = calcularMedia(muestra) # Estimamos la media apartir de la muestra

    # Hacemos el sorteo para B muestras aleatorias
    for _ in xrange(B):
        # temporal = Lista que contiene elementos de la muestra aplicando Bootstrap

        # Seleccionamos de forma aleatoria 10 elementos de la muestra
        # (se puede repetir) para el calculo de la expresion correspondiente
        temporal = [muestra[random.randint(0, 9)] for _ in xrange(n)]

        v = calcularMedia(temporal) - mu # Calculamos la expresion

        # Si a < v < b ==> tenemos un exito
        if -0.01 <= v and v < 0.01:
            exitos += 1

    # La probabilidad esta dada las veces que se cumple la condicion sobre
    # las veces que se realizo
    probabilidad = exitos/float(B)

    return probabilidad


def printEj3():
    for B in [100, 1000, 10000]:
        print("B =", B, "--> probabilidad =", ej3(B))

# printEj3()

########################
##### Ejercicio 04 #####
########################

def binomial(n, p):
    """
    Genera una v.a. X con distribucion Binomial de parametro n, p.
    X ~ B(n, p).
    """
    u = random.random()
    i = 0
    c = p/float(1-p)
    Pr = (1 - p)**n
    F = Pr
    while u >= F:
        Pr = ((c*(n-i))/float(i+1)) * Pr
        F += Pr
        i += 1

    x = i

    return x


def estimacionMedia(muestra):
    """
    Estima la media de una lista de una muestra dada.
    """
    return sum(muestra)/float(len(muestra))


def estimacionDE(muestra):
    """
    Estima la Desviacion Estandar de una muestra dada.
    """
    media = estimacionMedia(muestra)

    suma = 0
    for valor in muestra:
        suma += (valor - media)**2

    return math.sqrt(suma/float(len(muestra)))


def fi(valor):
    """
    Devuelve el FI(valor) de la Normal Estadar.
    Es la acumulada de la Normal Estadar.
    """
    return ndtr(valor)


def pValor(r, n, d):
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


def ej4b(largo_muestra, alfa):
    """
    Ejercicio 04.
    Test de Kolmogorov-Smirnov.
    """
    # Generamos x v.a. binomiales de n=50 y p=0.7 y las ordenamos
    muestra = [binomial(50, 0.7) for _ in xrange(largo_muestra)]
    muestra.sort()

    # Estimacion de la media y desviacion estandar para una distribucion normal
    media = estimacionMedia(muestra)
    des_est = estimacionDE(muestra)

    n = len(muestra) # Tamaño de la muestra

    # Calculamos el estadistico D
    valoresD = [] # Contiene los elementos del conjunto D+ y D-
    j = 1
    for valor in muestra:
        F = fi((valor - media)/des_est)
        valoresD.append(j/float(n) - F)
        valoresD.append(F - (j-1)/float(n))
        j += 1

    d = max(valoresD) # Valor observado

    p_valor = pValor(10000, n, d)

    return p_valor


def generarMediaBinomial(largo_muestra):
    # Generamos x v.a. binomiales de n=50 y p=0.7 y las ordenamos
    muestra = [binomial(50, 0.7) for _ in xrange(largo_muestra)]
    muestra.sort()

    # Estimacion de la media para una distribucion normal
    media = estimacionMedia(muestra)

    return media


def ej4c(largo_muestra, error):
    n = 30 # Minimo numero de simulaciones
    N = n # Observaciones Realizadas
    X = generarMediaBinomial(largo_muestra)
    M = X # Media Muestral (valor inicial: M(1) = X1)
    S_cuadrado = 0 # Varianza Muestral (valor inicial: S_cuadrado(1) = 0)
    # Calculamos M(n) y  S_cuadrado(n)
    for j in xrange(2, n+1):
        X = generarMediaBinomial(largo_muestra)
        A = M
        M += (X - M)/float(j)
        S_cuadrado = (1 - 1.0/(j-1))*S_cuadrado + j*((M-A)**2)

    j = n
    # Iteramos hasta que el ancho de IC sea < error
    while 2 * 1.96 * math.sqrt(S_cuadrado/float(j)) >= error:
        N += 1
        j += 1
        X = generarMediaBinomial(largo_muestra)
        A = M
        M += (X - M)/float(j)
        S_cuadrado = (1 - 1.0/(j-1))*S_cuadrado + j*((M-A)**2)

    S = math.sqrt(S_cuadrado) # Desviacion Estandar Muestral

    IC = (M - 1.96*(S/math.sqrt(j)) , M + 1.96*(S/math.sqrt(j)))

    ancho_IC = IC[1] - IC[0] # Ancho del intervalo

    return IC, ancho_IC, N


def printEj4b():
    for largo in [10, 20, 100, 1000]:
        print("Tamaño de la muestra =", largo, "--> p_valor =", ej4b(largo, 0.05))


def printEj4c():
    for largo in [10, 20, 100, 1000]:
        IC, ancho_IC, N = ej4c(largo, 0.01)
        print("\nIntervalo de Confianza =", IC)
        print("Ancho de IC =", ancho_IC)
        print("Ejecuciones necesarias =", N)
        print("")


# printEj4b()
# printEj4c()


########################
##### Ejercicio 05 #####
########################

def pValorChi(v, T):
    return chdtrc(v, T)


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


def poisson(lamda):
    """
    Genera una v.a. X con distribucion Poisson de parametro lamda.
    X ~ P(lamda).
    E(X) = lamda
    V(X) = lamda
    """
    u = random.random()
    i = 0
    p = math.exp(-lamda)
    F = p
    while u >= F:
        p = (lamda*p)/float(i+1)
        F += p
        i += 1

    x = i

    return x


def probabilidadPoisson(lamda, i):
    return math.exp(-lamda) * ((lamda**i)/(math.factorial(i)))


def ej5b(alfa):
    """
    Distribucion Poisson con Chi-Cuadrado.
    """
    # Intervalos:
    # {0}
    # {1}
    # {2, 3, ...}

    n = 101 # Tamaño de la muestra

    muestra0 = [0 for _ in xrange(48)]
    muestra1 = [1 for _ in xrange(35)]
    muestra2 = [2 for _ in xrange(15)]
    muestra3 = [3, 3, 3]

    # Muestra obtenida
    muestra = muestra0 + muestra1 + muestra2 + muestra3

    N = [48, 35, 18] # Frecuencias observadas

    # Estimemos lambda
    lamda = sum(muestra)/float(n) # Media muestral

    k = 3 # Cantidad de intervalos

    # Probabilidades
    p0 = probabilidadPoisson(lamda, 0)
    p1 = probabilidadPoisson(lamda, 1)
    p2 = 1.0 - p0 - p1
    prob = [p0, p1, p2]

    t = estadisticoT(k, n, N, prob)

    m = 1 # Cantidad de parametros estimados

    grados_libertad = k - m - 1 # En este caso serian 4

    p_valor = pValorChi(grados_libertad, t)

    if p_valor < alfa:
        print("Chi-Cuadrado: Se rechaza H0 a un nivel", alfa, "--> p-valor =", p_valor)
    elif p_valor > alfa:
        print("Chi-Cuadrado: No se rechaza H0 a un nivel", alfa, "--> p-valor =", p_valor)

    return p_valor


def ej5c(alfa):
    for _ in xrange(101):
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        dado3 = random.randint(1, 6)

        N1 = 0
        N2 = 0
        N3 = 0

        if dado1 == 6 and dado2 == 6 and dado3 == 6:
            N1 += 1
        elif (dado1 == 6 and dado2 == 6) or (dado2 == 6 and dado3 == 6) or (dado1 == 6 and dado3 == 6):
        elif (dado1 == 6) or (dado2 == 6) or (dado3 == 6):
        else
         # FALTA TERMINAR



def printEj5b():
    ej5b(0.05)

# printEj5b()
