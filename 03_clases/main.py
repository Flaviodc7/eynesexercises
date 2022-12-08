class Circulo:
    pi = 3.14

    def __init__(self, radio):
        self._radio = radio

    def area(self):
        return f'El area del circulo es: {self.pi * pow(self._radio, 2)}'

    def perimetro(self):
        return f'El perimetro del circulo es: {2 * self.pi * self._radio}'
