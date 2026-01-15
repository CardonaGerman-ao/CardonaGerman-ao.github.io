# 1 - Imagina 4 pizzes que t’agradin, emmagatzema-les dins tipus llista i utilitza el bucle for per imprimir cadascun del nom d’aquestes pizzes.

pizzas = ["pepperoni", "cuatro quesos", "carbonara", "barbacoa"]
i = 0
while i < len(pizzas):
    print(pizzas[i])
    i += 1

# A - Modifica el bucle per tal de que en comptes de només imprimir el nom de la pizza, imprimeixi una oració com per exemple 
# ‘M’agrada la pizza de pepperoni’.

i = 0
while i < len(pizzas):
    print(f"Me gusta la pizza de {pizzas[i]}")
    i += 1

# B - Afegeix una línia que imprimeixi ‘M’encanten les pizzes’ una vegada que surtis del bucle.

print("Me gustan las pizzas")

# 2 - Escriure un programa que demani a l'usuari un nombre enter positiu i mostri per pantalla tots els números imparells 
# des d'1 fins a aquest nombre separats per comes.

num = int(input("Introduce un número entero positivo: "))
i = 1
impares = []

while i <= num:
    impares.append(str(i))
    i += 2

print(", ".join(impares))

# 3 - Escriure un algorisme en Python que imprimeixi els 10 primers números parells començant a 2 i imprimiu també els seus respectius cubs. 
# Per exemple: 2 – 8; 4 – 64; 6 – 216 …



# A - Modifica aquest programa perquè en comptes d’imprimir els 10 primers nombres parells, imprimeixi els primers n nombres parells 
# on n es un enter positiu introduït per teclat.



# 4 - Realitza un programa que primer, llegeixi una frase per teclat i segón, que compti el nombre de paraules que té aquesta frase. 
# Recorda que hauràs d’utilitzar mètodes built-in de la classe String i de la clase List a més d’utilitzar el bucle for.


# 5 - Escriure un programa que demani a l'usuari un número sencer i mostri per pantalla un triangle rectangle com el de més avall, 
# d'alçada el número introduït. La imatge següent mostra l’exemple de la sortida del programa si introduïm el número 5.

num = int(input("Introduce un número entero: "))
i = 1
while i <= num:
    print("*" * i)
    i += 1

# 6 - Escriure un programa que demani a l’usuari una paraula i la mostri per pantalla 10 vegades.

palabra = input("Introduce una palabra: ")
i = 0
while i < 10:
    print(palabra)
    i += 1

# A - Modifica aquest programa perquè a l’usuari se li demani per teclat el nombre de vegades que vol repetir la paraula 
# i la repeteixi tantes vegades com les introduïdes per l’usuari.

palabra = input("Introduce una palabra: ")
veces = int(input("¿Cuántas veces quieres repetirla?: "))
i = 0
while i < veces:
    print(palabra)
    i += 1

# 7 - Fes un programa que llegeixi un nombre sencer per teclat i per pantalla imprimeixi tots els nombres primers 
# des de l’1 fins al nombre introduït.

entero = input("Introduce un número entero: ")

# A - Modifica aquest programa per a que comprovi si el nombre introduït sigui un nombre sencer, 
# en cas contrari s’imprimirà per pantalla el missatge 
# ‘El nombre introduït no és un nombre sencer’.



# 8 - Es col·loca un capital C, a un interès I (que oscil·la entre 0 i 100), durant M anys i es vol saber quan s'hi haurà convertit 
# aquest capital en “M” anys, sabent que és acumulatiu (se refiere al interés, es decir, que cuando se calcule el interés en un año determinado, 
# se calculará respecto a la cantidad original más las cantidades de los intereses de los años anteriores). 
# Crea un programa utilitzant el bucle for que ens calculi l’interés acumulat d’aquest capital. El capital C i l'interès I 
# s'hauran d’introduir per teclat.



# 9 - Crea un programa que calculi la suma de tots els divisors (sencers) d’un nombre sencer introduït per teclat 
# (recorda que els divisors poden ser com a molt grans fins a la meitat del nombre introduït).
