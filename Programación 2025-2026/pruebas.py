cadena = input('Introduce una cadena de caracteres: ')
resultado = ""
mayuscula = True
i = 0

while i < len(cadena):
    letra = cadena[i]

    if mayuscula:
        resultado += letra.upper()

    else:
        resultado += letra.lower()
    
    mayuscula = not mayuscula

    i += 1

print(f'El resultado es: {resultado}')