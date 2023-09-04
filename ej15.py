num1 = int( input("Ingrese un numero entre 0 y 10"))
if num1>10 or num1<0:
    print("El numero es mayor que 10 o menor que 0")
else:
    if num1%2==0:
        print("Numero par")
    else:
        print("Numero impar")