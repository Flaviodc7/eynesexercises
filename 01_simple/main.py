import random


def generarlista():
    list = []
    menor = 0
    mayor = 100
    cantidad = 9
    for i in range(cantidad):
        list.append({'id': i, 'edad': random.randint(menor, mayor)})
    return list


def edad(e):
    return e['edad']


def ordenarlista(list):
    list.sort(key=edad)
    print("La persona más joven es: ", list[0])
    print("La persona más vieja es: ", list[-1])
    return list


lista = generarlista()
lista = ordenarlista(lista)
