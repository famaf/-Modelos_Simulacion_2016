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
            print "    Suma de indices =", indices, "| Cantidad =", cantidad
            print "    Sumar Indice =", indices/float(cantidad)
            rangos.append(indices/float(cantidad))

    R = sum(rangos) # Suma de los rangos

    return R

m1 = [2, 3, 4]
m2 = [3, 5, 7]
m1 = [2, 3, 5]
m2 = [2, 2, 5, 7]
# Falla con el segundo ejemplo
m = m1+m2


R = sumaRangos(m1, m)
print "R =", R
