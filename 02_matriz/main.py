import numpy.random as nprandom


def crearmatriz():
    matriz = nprandom.randint(10, size=(5, 5))
    print(matriz)
    return matriz


crearmatriz()
