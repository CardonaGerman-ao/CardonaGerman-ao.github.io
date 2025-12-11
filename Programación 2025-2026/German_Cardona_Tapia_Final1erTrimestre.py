#-INSTRUCCIONS:
# 1 - Respon totes les preguntes en un arxiu amb el format “Nom_llinatge1_llinatge2_Final1erTrimestrel.py”
# 2 - Copia l’enunciat de cada exercici en aquest document i posa’l com a comentari.

# Exercicis de teoria:
# 1 - Explica els diferents tipus de contenidors de dades i les seves característiques i, per tant, les seves diferències. 1 punt



# 2 - Digues quin tipus de dades natius de Python hem vist a classe i explica’ls. 0.75 punts.

''' Tenemos el print para mostrar información por pantalla.
El float para valores númericos.
El int con el que podemos realizar un casting de string a float.
El str (string) es una cadena de caracteres.
'''

# Exercicis de condicionals:
# 3 - Crea un petit programa que demani que l’usuari introdueixi per teclat una  opció de l’1 al 5 
# (pot ser processat com a enter o com a caràcter) i que imprimeixi per pantalla “Has introduït l'opció -nombre introduït-” o, 
# en el cas de no introduir una opció correcte imprimeixi “No has introduït una opció vàlida”. 1’75 punts

numero = (print('Introduce un número del 1-5: '))
if numero == 1:
    print(f'El número introducido es: {numero}')
if numero == 2:
    print(f'El número introducido es: {numero}')
if numero == 3:
    print(f'El número introducido es: {numero}')
if numero == 4:
    print(f'El número introducido es: {numero}')
if numero == 5:
    print(f'El número introducido es: {numero}')
else:
    print('No has introducido una opción válida')

# 4 - (Exercici amb condicionals). Escriu un programa que llegeixi una lletra per teclat i digui si es tracta d’una vocal. 
# Haureu de tenir en compte les majúscules també, no serà necessari tenir en compte les vocals amb accent o altres. 
# Una altra cosa que haurà de fer el programa serà la d’imprimir un missatge d’error “Has introduït més d’una lletra” si 
# l’usuari introdueix 2 o més lletres com a missatge d’entrada. 1’75 punt



# 5 - (Exercici amb condicionals). Crea una calculadora per donar-te un impost d’IRPF total a pagar en funció d’un salari 
# introduït per l’usuari. Una vegada que l’usuari introdueixi el seu salari (haurà de ser transformat en ‘float’) 
# la calculadora fará el següent:
# Si el salari és inferior o igual a 15000€ anuals, l’usuari no haurà de pagarà res.
# Si el salari és troba entre els 15000€ i els 30000€ (aquest darrer inclòs) l’usuari haurà de pagar el 17% d’aquest 
# en IRPF (multiplica el salari per 0.17 i ja tens la quantitat).
# Si el salari es troba entre els 35000€ i els 45000€ (aquest darrer inclòs) l’usuari haurà de pagar el 23% d’aquest 
# en IRPF (multiplica el salari per 0.23 i ja tens la quantitat).
# Si el salari és superior a 45000€ l’usuari haurà de pagar el 37% d’aquest salari en IRPF 
# (multiplica el salari per 0.37 i ja tens la quantitat). 2 punts

if salario >= 15000:
    print('No tienes que pagar nada')
if salario :
    print('Tienes que pagar:')

# Exercicis de bucles:
# 6 - Crea un menú ‘infinit’ del qual només es pugui sortir quan l’usuari introdueix per teclat el número 3. 
# Aquest menú haurà de tenir 3 opcions: 1.5 punts.
# 1a opció: ‘Introdueix el número 1 per saludar-te’, i si l’usuari introueix aquest número el programa 
# haurà de contestar: ‘Hola que tal Pascual’.
# 2a opció: ‘Introdueix el número 2 per fer una suma’, llavors, demanará dos números per teclat i 
# imprimirà per pantalla: “La suma del ‘num1’+ ‘num2’ és: ‘resultat de la suma’”.
# 3a opció: ‘Introdueix el número 3 per sortir d’aquest menú’, si el usuari introdueix el número 3, 
# haurà d’imprimir ‘Adeu Mateu.’ i haurà de finalitzar.

while True:


# 7 - Realitza un programa que demani a l’usuari un nombre i un caràcter d’entrada i a partir d’aquests realitzi 
# el següent patró (exemple per a nombre = 4 y per a caràcter = #) :
# “””
1#
2##2##
3###3###3###
4####4####4####4####
# 1.25 punts.

