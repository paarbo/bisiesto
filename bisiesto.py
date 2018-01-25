def esbisiesto(anio):
    if anio%4==0 and anio%100!=0 or anio%400==0:
        print ("Bisiesto")
    else:
        print ("No es bisiesto")
print("Iniciando...")
esbisiesto(2100)
esbisiesto(2300)
esbisiesto(2020)
