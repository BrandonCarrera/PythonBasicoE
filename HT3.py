#Ejercicio 1

contraseña = input('Ingrese una contraseña:')
confirmarcontraseña = input('Confirme su contraseña:')
if contraseña == confirmarcontraseña:
    print('La contraseña coincide')
else:
    print('La contraseña no coincide')


#Ejercicio 2

nombre = input('Ingresa tu nombre:')
sexo = input('Ingresa tu sexo (M o F):')
if sexo == 'F' and nombre.lower() < 'm' :
    print('Perteneces al grupo A')
elif sexo == 'M' and nombre.lower() < 'n' :
    print('Perteneces al grupo A')
else:
    print('Perteneces al grupo B')
