anio=int(input("Escribe un anio: "))

if anio%4==0 and anio%100!=0 or anio%400==0:
    print ("Bisiesto")
else:
    print ("No es")
