a =int(input("Ingrese el primer lado "))
b =int(input("Ingrese el segundo lado "))
c =int(input("Ingrese el tercer lado "))

if a == b == c:
    print("El triangulo es quilatero ")

elif a == b != c or a == c != b or c == b != a:
    print("El triangulo es isoceles ")

elif a != b != c:
    print("El triangulo es escaleno ")

