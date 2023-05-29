import math

def f(x):
    return 5 * x ** 3 + 7 * x ** 2 - 4 * x + 4
    
def aproximacion_numerica(f, a, b, n):
    h = (b - a) / n

    integral = 0

    integral += f(a) + f(b)

    for i in range(1, n):
        x_i = a + i * h
        integral += 2 * f(x_i)

    integral = h / 2
    return integral

#Forward
def derivada_forward_mayor(f, x, h):
    return (-3 * f(x) + 4 * f(x + h) - f(x + 2 * h)) / (2 * h)

def derivada_forward_menor(f, x, h):
    return (f(x + h) - f(x)) / h

#Segunda Forward
def segunda_derivada_forward_mayor(f, x, h):
    return (2 * f(x) - 5 * f(x + h) + 4 * f(x + 2 * h) - f(x + 3 * h)) / (h * 2)

def segunda_derivada_forward_menor(f, x, h):
    return (f(x + 2 * h) - 2 * f(x + h) + f(x)) / (h * 2)

#Backward
def derivada_backward_mayor(f, x, h):
    return (3 * f(x) - 4 * f(x - h) + f(x - 2 * h)) / (2 * h)

def derivada_backward_menor(f, x, h):
    return (f(x) - f(x - h)) / h

#Segunda Backward
def segunda_derivada_backward_mayor(f, x, h):
    return (2 * f(x) - 5 * f(x - h) + 4 * f(x - 2 * h) - f(x - 3 * h)) / (h * 2)

def segunda_derivada_backward_menor(f, x, h):
    return (f(x) - 2 * f(x - h) + f(x - 2 * h)) / (h * 2)

#Center
def derivada_center(f, x0, h):
    return (f(x0 + h) - f(x0 - h)) / (2 * h)

def derivada_center_mayor(f, x0, h):
    return (-f(x0 + 2 * h) + 8 * f(x0 + h) - 8 * f(x0 - h) + f(x0 - 2 * h)) / (12 * h)

def derivada_center_menor(f, x0, h):
    return (f(x0 + h) - f(x0 - h)) / (4 * h)

#Segunda Center
def segunda_derivada_center(f, x0, h):
    return (f(x0 + h) - 2 * f(x0) + f(x0 - h)) / (h * 2)

def segunda_derivada_center_mayor(f, x0, h):
    return (-f(x0 + 2 * h) + 16 * f(x0 + h) - 30 * f(x0) + 16 * f(x0 - h) - f(x0 - 2 * h)) / (12 * (h * 2))

def segunda_derivada_center_menor(f, x0, h):
    return (-f(x0 + 2 * h) + 8 * f(x0 + h) - 8 * f(x0 - h) + f(x0 - 2 * h)) / (6 * (h ** 2))

print("Por favor seleccione una opción: ")
print("1. Calcular la aproximación numerica de una integral")
print("2. Calcular la aproximación de una derivada por metodo forward")
print("3. Calcular la aproximación de una derivada por metodo backward")
print("Calcular la aproximación de una derivada por metodo center")

opcion = int(input("Introduzca el número correspondiente a su selección: "))

if(opcion == 1):
    a = 0
    b = math.pi

    n = 10

    integral = aproximacion_numerica(f, a, b, n)
    print("Aproximación numerica: ", integral)

elif(opcion == 2):
    h = int(input("Introduzca el paso de diferenciación (h): "))
    x = int(input("Introduzca el punto de evualuación de la derivada (x): "))
    resultadoMayor = derivada_forward_mayor(f, x, h)
    resultadoMenor = derivada_forward_menor(f, x, h)
    resultadoMayor2 = segunda_derivada_forward_mayor(f, x, h)
    resultadoMenor2 = segunda_derivada_forward_menor(f, x, h)
    print("Derivada Forward Mayor: ", resultadoMayor)
    print("Derivada Forward Menor: ", resultadoMenor)
    print("Segunda Derivada Forward Mayor: ", resultadoMayor2)
    print("Segunda Derivada Forward Menor: ", resultadoMenor2)

elif(opcion == 3):
    h = int(input("Introduzca el paso de diferenciación (h): "))
    x = int(input("Introduzca el punto de evualuación de la derivada (x): "))
    resultadoMayor = derivada_backward_mayor(f, x, h)
    resultadoMenor = derivada_backward_menor(f, x, h)
    resultadoMayor2 = segunda_derivada_backward_mayor(f, x, h)
    resultadoMenor2 = segunda_derivada_backward_menor(f, x, h)
    print("Derivada Backward Mayor: ", resultadoMayor)
    print("Derivada Backward Menor: ", resultadoMenor)
    print("Segunda Derivada Backward Mayor: ", resultadoMayor2)
    print("Segunda Derivada Backward Menor: ", resultadoMenor2)

elif(opcion == 4):
    h = int(input("Introduzca el paso de diferenciación (h): "))
    x = int(input("Introduzca el punto de evualuación de la derivada (x): "))
    resultadoCentral = derivada_center(f, x, h)
    resultadoMayor = derivada_center_mayor(f, x, h)
    resultadoMenor = derivada_center_menor(f, x, h)
    resultadoCentral2 = segunda_derivada_center(f, x, h)
    resultadoMayor2 = segunda_derivada_center_mayor(f, x, h)
    resultadoMenor2 = segunda_derivada_center_menor(f, x, h)
    print("Derivada Center: ", resultadoCentral)
    print("Derivada Center Mayor: ", resultadoMayor)
    print("Derivada Center Menor: ", resultadoMenor)
    print("Segunda Derivada Center: ", resultadoCentral2)
    print("Segunda Derivada Center Mayor: ", resultadoMayor2)
    print("Segunda Derivada Center Menor: ", resultadoMenor2)

else:
    print("No hay ninguna opcion con este valor, porfavor intente de nuevo")


