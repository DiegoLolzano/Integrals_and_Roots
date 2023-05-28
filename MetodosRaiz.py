import math



def f(x):
    return 3 * x ** 3 - 2 * x ** 2 + 5 * x - 10

#Determinación por Metodo de Bisección

def biseccion(f, xl, xu, tolerancia):
    iteraciones = 0
    xr = (xl + xu) / 2
    ea = 100

    while ea > tolerancia:
        xr_anterior = xr
        xr = (xl + xu) / 2

        if xr != 0:
            ea = abs((xr - xr_anterior) / xr) * 100
        elif f(xr) * f(xl) < 0:
            xu = xr
        else:
            break

        iteraciones += 1

    print(f"Raiz encontrada en xr = {xr:.4f} después de {iteraciones} iteracion(es) con un error de {ea:.5f}% por el metodo de Bisección")
    return xr

#Determinación por Regla Falsa (Regula Falsi)

def regula_falsi(f, xl, xu, tolerancia):
    iteraciones = 0
    xr = xu - ((f(xu) * (xl - xu)) / (f(xl) - f(xu)))
    ea = 100

    while ea > tolerancia:
        xr_anterior = xr
        xr = xu - ((f(xu) * (xl - xu)) / (f(xl) - f(xu)))

        if xr != 0:
            ea = abs((xr - xr_anterior) / xr ) * 100

        if f(xr) * f(xl) < 0:
            xu = xr
        elif f(xr) * f(xu) < 0:
            xl = xr
        else:
            break

        iteraciones += 1

    print(f"Raiz encontrada en xr = {xr:.4f} despues de {iteraciones} iteracion(es) con un error de {ea:.5f}% por el metodo de Regla Falsa")
    return xr

#Determinacion por Metodo de Newton

def newton(f, df, x0, tolerancia):
    iteraciones = 0
    ea = 100

    while ea > tolerancia:
        xr_nuevo = x0 - f(x0) / df(x0)

        if xr_nuevo != 0:
            ea = abs((xr_nuevo - x0) / xr_nuevo) * 100
        
        x0 = xr_nuevo
        iteraciones += 1
    
    print(f"Raiz encontrada en xr = {x0:.4f} despues de {iteraciones} iteracion(es) con un error de {ea:.5f}% por el metodo de Newton")
    return x0

print("Escoge el metodo para determinar la raiz de la funcion 3x³ - 2x² + 5x - 10:")
print("1. Bisección")
print("2. Regla Falsa")
print("3. Metodo de Newton")
metodo = int(input("Introduzca el número con la opcion que desea elegir: "))

if(metodo == 1):
    xl = float(input("Ingrese el limite inferior: "))
    xu = float(input("Ingrese el limite superior: "))
    tolerancia = float(input("Ingrese la tolerancia de error: "))
    biseccion(f, xl, xu, tolerancia)
elif(metodo == 2):
    xl = float(input("Ingrese el limite inferior: "))
    xu = float(input("Ingrese el limite superior: "))
    tolerancia = float(input("Ingrese la tolerancia de error: "))
    regula_falsi(f, xl, xu, tolerancia)
elif(metodo == 3):
    x0 = float(input("Ingrese la estimación inicial: "))
    tolerancia = float(input("Ingrese la tolerancia de error: "))
    df = lambda x: 9 * x ** 2 - 4 * x + 5
    newton(f, df, x0, tolerancia)
else:
    print("No hay ninguna opcion con este valor, porfavor intente de nuevo")
