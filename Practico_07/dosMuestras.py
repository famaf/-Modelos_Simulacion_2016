# Programar para tomar promedio si hay datos repetidos


def sumaRangos(muestra1, muestra):
    """
    Calcula la suma de los rangos (R) de la 'muestra1' sobre la 'muestra'.
    """
    muestra.sort()

    rangos = []
    # Calculo los rangos de la muestra 1
    for valor in muestra1:
        indice = muestra.index(valor) + 1
        cantidad_valor = muestra.count(valor)
        print("Cantidad '", valor, "' =", cantidad_valor)
        print("Indice = ", indice)
        for i in xrange(cantidad_valor):
            indice += i
            print("\t INDICES =", indice)

        result = indice/float(cantidad_valor)
        print("\tIndice final =", indice)
        print("\tResult =", result)

        rangos.append(indice/float(cantidad_valor))

    R = sum(rangos) # Suma de los rangos

    return R


# Rango de Joni --> Funciona

def rangoRBien(muestra1, nmMuestras):
    nmMuestras.sort()

    muestraCopy = list(muestra1)
    muestraCopy.sort()

    R = []
    j = 0
    while len(muestraCopy) != 0:
        valor = muestraCopy[0]
        cantValor = muestraCopy.count(valor)
        s = 0
        for j in xrange(cantValor):
            for i in xrange(nmMuestras.count(valor)):
                s += nmMuestras.index(valor) + (i + 1)
            muestraCopy.pop(0)

        s = s / float(nmMuestras.count(valor))
        R.append(s)

    return sum(R)


m1 = [2, 3, 4]
m2 = [3, 5, 7]

m1 = [2, 3, 5]
m2 = [2, 2, 5, 7]
# Falla con el segundo ejemplo con mi rango, el de joni anda bien
# R = (1+2+3)/3 + 4 + (5+6)/2 = 2 + 4 + 11/2 = 11.5
m1 = [2, 3, 4, 4, 4]
m2 = [2, 3, 4, 5]

m = m1 + m2

# R = sumaRangos(m1, m)
R = rangoRBien(m2, m)
print("R =", R)
