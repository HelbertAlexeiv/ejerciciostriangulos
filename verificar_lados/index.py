# Datos de entrada
a = int(input("Ingresa un valor para el lado a: "))
b = int(input("Ingresa un valor para el lado b: "))
c = int(input("Ingresa un valor para el lado c: "))

if a+b >= c:
    if b+c >= a:
        if c+a >= b:
            print("Se puede formar un triangulo con los lados: ", a, ", ", b, " y ", c, sep="")
        else:
            print("La suma de los lados ", c, " y ", a, " es menor a ", b, " por lo que no se puede formar el triangulo", sep="")
    else:
        print("La suma de los lados ", b, " y ", c, " es menor a ", a, " por lo que no se puede formar el triangulo", sep="")
else:
    print("La suma de los lados ", a, " y ", b, " es menor a ", c, " por lo que no se puede formar el triangulo", sep="")
