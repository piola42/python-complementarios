print("Ingrese la operacion a realizar")
print("1 multiplicacion")
print("2 potencia")
print("3 division")
oper = int( input())
num = float( input("Ingrese el numero: "))
funciones = {
    1: 100*num,
    2: 100**num,
    3: 100/num
}
print(funciones.get(oper, 0))
