def mayor_y_menor():
    a = float(input("Numero 1: "))
    b = float(input("Numero 2: "))
    c = float(input("Numero 3: "))

    if a >= b and a >= c:
        mayor = a
    elif b >= a and b >= c:
        mayor = b
    else:
        mayor = c

    if a <= b and a <= c:
        menor = a
    elif b <= a and b <= c:
        menor = b
    else:
        menor = c

    print(f"El mayor es: {mayor}")
    print(f"El menor es: {menor}")

mayor_y_menor()
