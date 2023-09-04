precio = float( input("Ingrese el precio: "))
marca = input(("Ingrese la marca: "))
if precio>=2000:
    precio=precio*0.90
if marca=="NOSY":
    precio=precio*0.95
precio=precio*1.20
print("El precio a pagar es de: ", precio)