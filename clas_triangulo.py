def clasificar_triangulo():
    a = float(input("Lado 1: "))
    b = float(input("Lado 2: "))
    c = float(input("Lado 3: "))

    if a + b <= c or a + c <= b or b + c <= a:
        print("No es un triangulo valido")
    elif a == b == c:
        print("Equilatero")
    elif a == b or a == c or b == c:
        print("Isosceles")
    else:
        print("Escaleno")

clasificar_triangulo()