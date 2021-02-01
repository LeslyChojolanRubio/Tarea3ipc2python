# Aca realizamos las importaciones
from Figura import Figura
from Figura import Cuadrado
from Figura import Rectangulo
from Figura import Triangulo
from Figura import Circulo


def solicitarDatos(lista): 
    print("Bienvenido al programa")
    
    print('ingrese el numero de figuras:')
    cantidad = int(input("Cantidad: "))
    contador=1

    while contador <= cantidad:
        tipo= input("Seleccione el numero del tipo de figura 1. Cuadrado, 2. Rectangulo, 3. Triangulo, 4. Circulo")
        tipo= int(tipo)
        if(tipo== 1):#cuadrado, esto es para llenar la lista que enviaré a catalogar
            unLado= int(input('ingrese longitud de 1 lado del cuadrado: '))
            unCuadrado = Cuadrado(unLado)
            unCuadrado.calcularArea()
            unCuadrado.calcularPerimetro()
            lista.append(unCuadrado)
            contador += 1
        elif tipo== 2:
            base= int(input('ingrese longitud de base rectangulo: '))
            altura= int(input('ingrese longitud de altura rectangulo: '))
            unRectangulo = Rectangulo(base, altura)
            unRectangulo.calcularArea()
            unRectangulo.calcularPerimetro()
            lista.append(unRectangulo)
            contador += 1
        elif tipo== 3:
            base= int(input('ingrese base del triangulo: '))
            altura= int(input('ingrese altura del triangulo: '))
            lado1= int(input('ingrese lado 1: '))
            lado2= int(input('ingrese lado 2: '))
            lado3= int(input('ingrese lado 3: '))
            unTriangulo = Triangulo(base, altura, lado1, lado2, lado3)
            unTriangulo.calcularArea()
            unTriangulo.calcularPerimetro()
            lista.append(unTriangulo)
            contador += 1
        elif tipo== 4:
            radio= int(input('ingrese el radio del circulo'))
            unCirculo = Circulo(radio)
            unCirculo.calcularArea()
            unCirculo.calcularPerimetro()
            lista.append(unCirculo)
            contador += 1
        else:
            print('opcion no valida')

#ese fue el menu del funcionamiento del programa ahora la segunda parte
# una vez ingresadas todas las figuras, se muestra el nombre, area y perimetro de cada figura para        
#  ello se define una funcion para recorrer el vector de figuras y mostrar sus datos calculados



def catalogar(figuras):#recibe una lista ya llena

    # Primera pasada, mostrar areas y perimetros
    contadorAreas = 0
    contadorPerimetros=0
    if len(figuras) != 0:
        
        for v in figuras: 
            contadorAreas += v.area
            contadorPerimetros += v.perimetro
        print("\nResultados: {} area total {} perimetro total:".format(contadorAreas, contadorPerimetros))

    # Segnda pasada, mostrar figuras
    for v in figuras:
        if len(figuras) != 0:
            print(type(v).__name__)
            print("area: "+ str(v.area) + " perimetro: "+ str(v.perimetro))
        else:
            print("hubo un error")


#aqui ya no se definen funciones sino que se implementan en orden logico
lista = []


solicitarDatos(lista)
print(" ver resultados de areas y perimetros")
catalogar(lista)
print("Fin del programa")