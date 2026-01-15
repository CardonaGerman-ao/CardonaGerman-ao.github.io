# Exercici del 7 del Gener de 2026
# Es demanar a l'usuari que introdueixi una cadena de caràcters per teclat y el bucle for haurà de processar aquesta cadena
# i crear-ne una de nova amb les lletres minúscules y majúscules alternades.
# Exemple:
# Si l'usuari introdueix la cadena "MaduroMArica"
# La sortida haurà de ser: "MaDuRoMaRiCa"

cadena = input('Introdueix una cadena qualsevol: ')
cadenaltern = ''
ismayus = True
for char in cadena:
    if ismayus:
        cadenaltern += char.upper()
    else:
        cadenaltern  += char.lower()
    ismayus = not ismayus

print(f'La cadena resultante de {cadena} es: {cadenaltern}')

# Versió de l'exercici utilitzant while en comptes de for:
print()
cadena = input('Introdueix una cadena qualsevol: ')
index = 0
cadIter = ''
ismayus = True
while index < len(cadena):
    if ismayus:
        cadIter += cadena[index].upper()
    else:
        cadIter  +=  cadena[index].lower()
    ismayus = not ismayus
    index += 1
print(f'La cadena resultante de {cadena} es: {cadIter}')

# Exercici 2 de la pràctica 7 de la col·lecció d'exercicis:
# Escriure un programa que demani a l'usuari un nombre enter positiu i mostri per pantalla 
# tots els números imparells des d'1 fins a aquest nombre separats per comes.
print()
num = int(input('Introdueix un número enter positiu: '))
index = 1
impares = []
while index <= num:
    if not (index%2 == 0):
        impares.append(str(index))
    index += 1

print(','.join(impares))

impares = []
index = 1
while index <= num:
    print(f'{index},', end='')
    index += 2
print()

# Pel pròxim dia realitzar els exercicis 7, 8 i 9 de la pràctica 7. Ànim, no utilitzeu el chatGPT.