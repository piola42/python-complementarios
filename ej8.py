print("1: Area de un triangulo")
print("2: Area de un circulo")
oper = int( input())
if oper==1:
    lado = int( input("Ingrese el lado del triangulo: "))
    area = ((3**0.5)/4)*lado**2
    print("El area del triangulo es de:", area)
else:
    if oper==2:
        radio = int( input("Ingrese el radio del circulo: "))
        area = 3.1416*radio**2
        print("El area del circulo es de:", area)
    else:
        print("Error")