import time


class Circulo:
    pi = 3.14

    def __init__(self, radio):
        self._radio = radio

    def area(self):
        return f'El area del circulo es: {self.pi * pow(self._radio, 2)}\n'

    def perimetro(self):
        return f'El perimetro del circulo es: {2 * self.pi * self._radio}\n'


radio = 0
ingresoerroneo = 0

while radio <= 0:
    if ingresoerroneo:
        print("\nUsted ha ingresado un número menor o igual a 0")
    radio = int(input("Por favor, ingrese un radio para el circulo mayor a cero: "))
    if radio <= 0:
        ingresoerroneo = 1
        radio = 0
    else:
        circulo = Circulo(radio)
        time.sleep(3)
        print(f"Excelente, estos son los datos del circulo:\n"
              f"{circulo.area()}"
              f"{circulo.perimetro()}")
        opcion = 1
        time.sleep(5)
        while opcion != 3:
            opcion = int(input("Por favor, elija una opción a continuacion: \n"
                               "1 - Modificar el radio del circulo\n"
                               "2 - Multiplicar el radio del circulo\n"
                               "3 - Salir\n"))
