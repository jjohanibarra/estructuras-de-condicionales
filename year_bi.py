# Un año es bisiesto si es divisible entre 4 pero no entre 100 (para omitir la mayoría de los siglos)
# o si es divisible entre 400 (para rescatar los siglos bisiestos como el año 2000).
#Creo que si era asi por que no pude hacerlo con el datetime

def es_bisiesto():
    year = int(input("Año: "))

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Es bisiesto")
    else:
        print("No es bisiesto")

es_bisiesto()