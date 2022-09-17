a = int(input("Ingrese un lado: "))
b = int(input("Ingrese un lado: "))
c = int(input("Ingrese un lado mayor a los otros dos: "))
print(c**2 == (a**2) + (b**2))
if (c**2) == ((a**2) + (b**2)):
    print("El triangulo es rectangulo")
elif c**2 < a**2 + b**2:
    print("El triangulo es agudo")

elif c**2 > a**2 + b**2:
    print("El triangulo es obtuso")



