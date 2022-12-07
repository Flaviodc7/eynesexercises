import random


def generarlista():
    list = []
    menor = 0
    mayor = 100
    cantidad = 9
    for i in range(cantidad):
        list.append({'id': i, 'edad': random.randint(menor, mayor)})
    return list


lista = generarlista()
