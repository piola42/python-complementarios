dia = int( input("Ingrese el dia: "))
mes = int( input("Ingrese el mes: "))
año = int( input("Ingrese el año: "))
if dia<30:
    print(dia+1)
    print(mes)
    print(año)
else:
    if mes<12:
        print("1")
        print(mes+1)
        print(año)
    else:
        print("1")
        print("1")
        print(año+1)