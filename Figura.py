from math import pi

class Figura():

    def __init__(self):
        self.area = 0
        self.perimetro= 0
    
    #def __str__(self):
    #    return "area {}, {} perimetro".format(self.area, self.perimetro)


class Cuadrado(Figura):

    def __init__(self, lado):
        super().__init__()
        self.lado = lado

    def calcularArea(self):
        self.area = self.lado * self.lado
        return self.area

    def calcularPerimetro(self):
        self.perimetro = self.lado * 4
        return self.perimetro


class Rectangulo(Figura):
    def __init__(self, base, altura):
        super().__init__()
        self.base=base
        self.altura=altura

    def calcularArea(self):
        self.area = self.base * self.altura
        return self.area
    
    def calcularPerimetro(self):
        self.perimetro= (self.base * 2) + (self.altura * 2)
        return self.perimetro

class Triangulo(Figura):
    def __init__(self, base, altura, l1, l2, l3):
        super().__init__()
        self.base=base
        self.altura=altura
        self.lado1 = l1
        self.lado2 = l2
        self.lado3 = l3

    def calcularArea(self):
        self.area = (self.base * self.altura) / 2
        return self.area
    
    def calcularPerimetro(self):
        self.perimetro= self.lado1 + self.lado2 +self.lado3
        return self.perimetro

class Circulo(Figura):
    def __init__(self, radio):
        super().__init__()
        self.radio=radio

    def calcularArea(self):
        self.area = self.radio * self.radio * pi
        return self.area
    
    def calcularPerimetro(self):
        self.perimetro= pi * 2 * self.radio
        return self.perimetro




