import time


class Circulo:
    pi = 3.14

    def __init__(self, radio):
        self._radio = radio

    def area(self):
        return f'El area del circulo es: {self.pi * pow(self._radio, 2)}\n'

    def perimetro(self):
        return f'El perimetro del circulo es: {2 * self.pi * self._radio}\n'

    def multiplicar(self, mult):
        self._radio *= mult

    def mostrarradio(self):
        return self._radio


radio = 0


def chequearradio(rad):
    ingresoerroneo = 0
    while rad <= 0:
        if ingresoerroneo:
            print("\nUsted ha ingresado un número menor o igual a 0")
        rad = int(input("Por favor, ingrese un radio para el circulo mayor a cero: "))
        if rad <= 0:
            ingresoerroneo = 1
            rad = 0
        else:
            circ = Circulo(rad)
            time.sleep(3)
            print(f"\nExcelente, estos son los datos del circulo:\n{circ.area()}{circ.perimetro()}")
            return circ


def multiplicarradio(circ):
    multiplicador = 0
    while multiplicador <= 0:
        multiplicador = int(input("Por favor, ingrese por cuanto quiere multiplicar el radio,"
                                  "recuerde que el número debe ser mayor a cero: "))
        if multiplicador <= 0:
            print("\nUsted ha ingresado un número menor o igual a 0")
        else:
            circ.multiplicar(multiplicador)
            time.sleep(2)
            print(f"\nEl nuevo radio del circulo es de: {circ.mostrarradio()}")
            print(f"\nEstos son los nuevos datos del circulo:\n{circ.area()}{circ.perimetro()}")
            return circ


circulo = chequearradio(radio)
opcion = 0
while opcion != 3:
    time.sleep(4)
    opcion = int(input("Por favor, elija una opción a continuacion: \n"
                       "1 - Modificar el radio del circulo\n"
                       "2 - Multiplicar el radio del circulo\n"
                       "3 - Salir\n"))
    if opcion == 1:
        chequearradio(radio)
    elif opcion == 2:
        circulo = multiplicarradio(circulo)
    else:
        print("Usted ha ingresado una opción incorrecta")