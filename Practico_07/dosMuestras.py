# Programar para tomar promedio si hay datos repetidos

def sumaRangos(muestra1, muestra):
    """
    Calcula la suma de los rangos (R) de la 'muestra1' sobre la 'muestra'.
    """
    muestra.sort()

    rangos = []
    # Calculo los rangos de la muestra 1
    for valor in muestra1:
        cantidad = muestra.count(valor)
        if cantidad == 1:
            print "Cantidad =", cantidad
            print "    Sumar Indice =", muestra.index(valor) + 1
            rangos.append(muestra.index(valor) + 1)

        else:
            print "Cantidad =", cantidad
            indices = muestra.index(valor) + 1
            ultimo_indice = indices
            print "Indice inicial", indices 
            aux = cantidad
            restantes = aux - 1
            for i in xrange(restantes):
                indices += indices + 1
                ultimo_indice = indices + 1
            print "    Suma de indices =", indices, "| Cantidad =", cantidad
            print "    Sumar Indice =", indices/float(cantidad)
            rangos.append(indices/float(cantidad))

    R = sum(rangos) # Suma de los rangos

    return R

def rangoRBien(muestra1, nmMuestras):
    nmMuestras.sort()

    muestraCopy = list(muestra1)

    R = []
    j = 0
    while len(muestraCopy) != 0:
        valor = muestraCopy[0]
        cantValor = muestraCopy.count(valor)
        s = 0
        for i in xrange(cantValor):
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
# Falla con el segundo ejemplo
# R = (1+2+3)/3 + 4 + (5+6)/2 = 2 + 4 + 11/2 = 11.5
m = m1+m2


#R = sumaRangos(m1, m)
R = rangoRBien(m1, m)
print "R =", R
