a = float( input("a: "))
b = float( input("b: "))
c = float( input("c: "))
disc = b**2-4*a*c
if disc>0:
    x1 = ((-b)+disc**0.5)/2*a
    x2 = ((-b)-disc**0.5)/2*a
    print("x1:",x1)
    print("x2:",x2)
