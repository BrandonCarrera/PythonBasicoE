peso = float(input("Ingrese su peso en kg"))
estatura = float(input("Ingrese su estatura en metros"))

IMC = peso/estatura**2

print("Tu índice de masa corporal es " + str(round(IMC,2)))
