#Ejercicio 1

numero = input('Ingresar un número entero:')
for x in range(int(numero) + 1):
    c = '*'
    print(c * x)


#Ejercicio 2

n = int(input('Ingrese un número entero positivo:'))

while n >= 0:
    print(str(n) + ", ", end="")
    n -= 1


#Ejercicio 3

np = int(input('Ingrese un número entero:'))

for w in range(2, np):
    if np % w == 0:
        print('No es un número primo')
        break
else:
    print('Es un número primo')
