# Calcula el costo de entrada según el rango de edad ingresado.

def calcular_entrada():
    edad = int(input("Edad: "))

    if edad < 0:
        print("Edad no valida")
    elif edad < 12:
        print("El costo de la entrada es: $50")
    elif edad <= 17:
        print("El costo de la entrada es: $80")
    else:
        print("El costo de la entrada es: $120")

calcular_entrada()