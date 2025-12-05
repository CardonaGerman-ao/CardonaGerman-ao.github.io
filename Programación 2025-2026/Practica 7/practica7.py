# 1 - Imagina 4 pizzes que t’agradin, emmagatzema-les dins tipus llista i utilitza el bucle for per imprimir cadascun del nom d’aquestes pizzes.

pizzas = ["pepperoni", "cuatro quesos", "carbonara", "barbacoa"]
i = 0
while i < len(pizzas):
    print(pizzas[i])
    i += 1

# A - Modifica el bucle per tal de que en comptes de només imprimir el nom de la pizza, imprimeixi una oració com per exemple ‘M’agrada la pizza de pepperoni’.

i = 0
while i < len(pizzas):
    print(f"Me gusta la pizza de {pizzas[i]}")
    i += 1

# B - Afegeix una línia que imprimeixi ‘M’encanten les pizzes’ una vegada que surtis del bucle.

print("Me encantan las pizzas")

# 2 - Escriure un programa que demani a l'usuari un nombre enter positiu i mostri per pantalla tots els números imparells des d'1 fins a aquest nombre separats per comes.

num = int(input("Introduce un número entero positivo: "))
i = 1
impares = []

while i <= num:
    impares.append(str(i))
    i += 2

print(", ".join(impares))

# 3 - Escriure un algorisme en Python que imprimeixi els 10 primers números parells començant a 2 i imprimiu també els seus respectius cubs. Per exemple: 2 – 8; 4 – 64; 6 – 216 …

i = 2
contador = 0
while contador < 10:
    print(i, "-", i**3)
    i += 2
    contador += 1

# A - Modifica aquest programa perquè en comptes d’imprimir els 10 primers nombres parells, imprimeixi els primers n nombres parells on n es un enter positiu introduït per teclat.

n = int(input("¿Cuántos números pares quieres imprimir?: "))
i = 1
contador = 0
while contador < n:
    par = i * 2
    print(par, "-", par**3)
    i += 1
    contador += 1

# 4 - Realitza un programa que primer, llegeixi una frase per teclat i segón, que compti el nombre de paraules que té aquesta frase. 
# Recorda que hauràs d’utilitzar mètodes built-in de la classe String i de la clase List a més d’utilitzar el bucle for.

frase = input("Introduce una frase: ")
palabras = frase.split()
contador = 0
i = 0
while i < len(palabras):
    contador += 1
    i += 1

print("Número de palabras:", contador)

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

# A - Modifica aquest programa perquè a l’usuari se li demani per teclat el nombre de vegades que vol repetir la paraula i la repeteixi tantes vegades com les introduïdes per l’usuari.

palabra = input("Introduce una palabra: ")
veces = int(input("¿Cuántas veces quieres repetirla?: "))
i = 0
while i < veces:
    print(palabra)
    i += 1

# 7 - Fes un programa que llegeixi un nombre sencer per teclat i per pantalla imprimeixi tots els nombres primers des de l’1 fins al nombre introduït.
# Modifica aquest programa per a que comprovi si el nombre introduït sigui un nombre sencer, en cas contrari s’imprimirà per pantalla el missatge ‘El nombre introduït no és un nombre sencer’.

num = input("Introduce un número: ")
if not num.isdigit():
    print("El número introducido no es un número entero")
else:
    num = int(num)
    n = 2
    while n <= num:
        es_primo = True
        i = 2
        while i < n:
            if n % i == 0:
                es_primo = False
                break
            i += 1
        if es_primo:
            print(n)
        n += 1


# 8 - Es col·loca un capital C, a un interès I (que oscil·la entre 0 i 100), durant M anys i es vol saber quan s'hi haurà convertit aquest capital en “M” anys, 
# sabent que és acumulatiu (se refiere al interés, es decir, que cuando se calcule el interés en un año determinado, 
# se calculará respecto a la cantidad original más las cantidades de los intereses de los años anteriores). 
# Crea un programa utilitzant el bucle for que ens calculi l’interés acumulat d’aquest capital. El capital C i l'interès I s'hauran d’introduir per teclat.

C = float(input("Introduce el capital inicial: "))
I = float(input("Introduce el interés (%): "))
M = int(input("Introduce los años: "))
año = 0
while año < M:
    C += C * (I / 100)
    año += 1
print("Capital final:", C)

# 9 - Crea un programa que calculi la suma de tots els divisors (sencers) d’un nombre sencer introduït per teclat (recorda que els divisors poden ser com a molt grans fins a la meitat del nombre introduït).

num = int(input("Introduce un número entero: "))
i = 1
suma = 0
while i <= num // 2:
    if num % i == 0:
        suma += i
    i += 1
print("La suma de los divisores es:", suma)


# 10 - Crea un programa que demani un text per teclat i que la sortida sigui el text invertit. No podrás fer servir la sintaxi [::-1] Ç
# per invertir aquest texte sinó que hauràs de llegir-lo caràcter a caràcter i invertir-lo amb el bucle for.

texto = input("Introduce un texto: ")
invertido = ""
i = 0
while i < len(texto):
    invertido = texto[i] + invertido
    i += 1
print(invertido)


# 11 - Imprimeix el següent patró utilitzant el bucle for, les dimensions del patró dependran d’un nombre introduït per teclat, en el cas següent es mostra el patró si el nombre introduït és el 5:

n = int(input("Introduce un número: "))
i = 1
while i <= n:
    print("*" * i)
    i += 1
i = n - 1
while i > 0:
    print("*" * i)
    i -= 1

# 12 - Escriu un programa que donat un nombre sencer introduït per teclat imprimeixi tots els nombres primers des del número 1 fins a aquest nombre. 

num = int(input("Introduce un número: "))
n = 2
while n <= num:
    es_primo = True
    i = 2
    while i < n:
        if n % i == 0:
            es_primo = False
            break
        i += 1
    if es_primo:
        print(n)
    n += 1

# 13 - Crea un programa utilitzant el bucle for que compti el nombre de xifres que té un número sencer introduït per teclat.

num = input("Introduce un número entero: ")
contador = 0
i = 0
while i < len(num):
    if num[i].isdigit():
        contador += 1
    i += 1
print("Número de cifras:", contador)

# 14 - Escriu un programa que pregunti quants números s'introduiran, demaneu aquests números, i mostri un missatge cada vegada que un nombre no sigui més gran que el primer nombre introduït.

cantidad = int(input("¿Cuántos números introducirás?: "))
primero = int(input("Introduce el primer número: "))
i = 1
while i < cantidad:
    n = int(input("Introduce un número: "))
    if n <= primero:
        print("El número no es mayor que el primero.")
    i += 1

# 15 - Escriviu un programa que pregunti quants números s'introduiran, demaneu aquests números, i mostri un missatge cada vegada que un nombre no sigui més gran que l'anterior.

cantidad = int(input("¿Cuántos números introducirás?: "))
anterior = int(input("Introduce un número: "))
i = 1
while i < cantidad:
    n = int(input("Introduce un número: "))
    if n <= anterior:
        print("El número no es mayor que el anterior.")
    anterior = n
    i += 1