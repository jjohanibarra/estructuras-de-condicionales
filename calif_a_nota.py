def convertir_calificacion():
    nota=float(input("Calificacion (0-100): "))

    if nota < 0 or nota > 100:
         print("Calificacion no valida")
    elif nota >= 90:
         print("A")
    elif nota >= 80:
         print("B")
    elif nota >= 70:
         print("C")
    elif nota >= 60:
         print("D")
    else:
         print("F")

convertir_calificacion()
