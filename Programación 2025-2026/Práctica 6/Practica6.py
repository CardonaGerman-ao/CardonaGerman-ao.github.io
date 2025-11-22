# 1 - Crea un programa que determini si un número introduït des de teclat és positiu, negatiu o zero.

numero = float(input("Introduce un número: "))
if numero > 0:
    print("El número es positivo")
elif numero < 0:
    print("El número es negativo")
else:
    print("El número es cero")

# 2 - Escriu un programa que escrigui per pantalla si una fruita es "cítrica", "dolça", "fruit sec" o "altra" 
# utilitzant entrada per teclat (utiliza una llista per cada tipus de fruita, conjunt o tupla per la comprovació).

fruta = input("Introduce una fruta: ").lower()
citricas = ("naranja", "limón", "mandarina", "pomelo")
dulces = ("manzana", "pera", "fresa", "plátano", "uva")
frutos_secos = ("almendra", "nuez", "avellana", "pistacho")
if fruta in citricas:
    print("La fruta es cítrica")
elif fruta in dulces:
    print("La fruta es dulce")
elif fruta in frutos_secos:
    print("La fruta es un fruto seco")
else:
    print("Es otro tipo de fruta")

# 3 - Crea un programa que determini si una persona té menys de 18 anys (menor), té més o igual a 18 anys 
#(si té entre 18 y 30 -inclosos- és un adult jove, si te entre 31 y 65 anys és un adult, 
# si té més de 65 anys és un adult senior) i m’imprimeixi per pantalla el tipus de persona.

edad = int(input("Introduce tu edad: "))
if edad < 18:
    print("Eres menor de edad")
elif 18 <= edad <= 30:
    print("Eres un adulto joven")
elif 31 <= edad <= 65:
    print("Eres un adulto")
else:
    print("Eres un adulto senior")

# 4 - Creeu un programa que determini el dia de la setmana a partir d'un número de l'1 al 7 (1 Dilluns…i finalment 7 Diumenge).

numero = int(input("Introduce un número del 1 al 7: "))
if numero == 1:
    print("Lunes")
elif numero == 2:
    print("Martes")
elif numero == 3:
    print("Miércoles")
elif numero == 4:
    print("Jueves")
elif numero == 5:
    print("Viernes")
elif numero == 6:
    print("Sábado")
elif numero == 7:
    print("Domingo")
else:
    print("Número inválido")

# 5 - Escriu un programa que classifiqui un animal en "mamífer", "au", "rèptil" o "un altre" .

animal = input("Introduce un animal: ").lower()
mamiferos = ("perro", "gato", "vaca", "caballo", "ratón")
aves = ("pájaro", "águila", "paloma", "pollo", "pato")
reptiles = ("serpiente", "lagarto", "cocodrilo", "tortuga")
if animal in mamiferos:
    print("Es un mamífero")
elif animal in aves:
    print("Es un ave")
elif animal in reptiles:
    print("Es un reptil")
else:
    print("Es otro tipo de animal")
