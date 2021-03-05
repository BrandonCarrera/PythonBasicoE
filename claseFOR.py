#Ciclos For.

notas = [61, 59, 20, 45, 80, 100, 62, 75]

for nota in notas:
    if nota == 100:
        print("Hay un 100")
        break   #Detiene el ciclo
    if nota >= 61:
        print("You win")
    else:
        print("It's not enough to pass")

print('------')

    #También en strings

for letter in "Hello":
    print(letter)

print('------')

productos = ['manzana', 'pera', 'fresa', 'banana', 'kiwi']
for producto in productos:
    if producto == 'banana':
        print('Comprar')
    print('No necesario')