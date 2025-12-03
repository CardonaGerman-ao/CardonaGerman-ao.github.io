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

# 6 - Creeu un programa que calculi el cost d'enviament d’un paquet segons la distància: fins a 10 km, 10-50 km, o més de 50 km.

dist = float(input("Introduce la distancia en km: "))
if dist <= 10:
    print("Coste: 5€")
elif dist <= 50:
    print("Coste: 10€")
else:
    print("Coste: 20€")

# 7 - Crea un programa que assigni una qualificació a una nota numèrica (A, B, C, D o F) en funció d’una nota numérica donada per teclat
# (A = entre 9 i 10 -ambdós inclosos-, B = entre 7 i 9 -incloent el 7 però no el 9- , C = entre 5 i 7 -incloent el 5 però no el 7-, F = menys de 5).

nota = float(input("Introduce la nota: "))
if nota >= 9 and nota <= 10:
    print("A")
elif nota >= 7 and nota < 9:
    print("B")
elif nota >= 5 and nota < 7:
    print("C")
elif nota < 5 and nota >= 0:
    print("F")
else:
    print("Nota no válida")

# 8 - Escriu un programa que classifiqui un dia de la setmana a "laborable" o "cap de setmana".

dia = input("Introduce un día de la semana: ")
dia = dia.lower()
if dia == "lunes" or dia == "martes" or dia == "miércoles" or dia == "miercoles" or dia == "jueves" or dia == "viernes":
    print("Laborable")
elif dia == "sábado" or dia == "sabado" or dia == "domingo":
    print("Fin de semana")
else:
    print("Día no válido")

# 9 - Escriu un programa que emmagatzemi la cadena de caràcters contrasenya en una variable, pregunteu a l'usuari per la contrasenya 
# i imprimiu per pantalla si la contrasenya introduïda per l'usuari coincideix amb la desada a la variable sense tenir en compte majúscules i minúscules.

contrasena = "Manoloeldelbombo"
user = input("Introduce la contraseña: ")
if user.lower() == contrasena.lower():
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")

# 10 - Escriu un programa que demani a l'usuari dos números i en mostri per pantalla la divisió. Si el divisor és zero, el programa ha de mostrar un error.

a = float(input("Introduce el primer número: "))
b = float(input("Introduce el segundo número: "))
if b == 0:
    print("Error: no se puede dividir por cero")
else:
    print("Resultado:", a / b)

# 11 - Per tributar un determinat impost cal ser major de 16 anys i tenir uns ingressos iguals o superiors a 1000 € mensuals. 
# Escriure un programa que pregunti a l’usuari la seva edat i els seus ingressos mensuals i mostri per pantalla si l’usuari ha de tributar o no.

edad = int(input("Introduce tu edad: "))
ingresos = float(input("Introduce tus ingresos mensuales: "))
if edad > 16 and ingresos >= 1000:
    print("Debes tributar")
else:
    print("No debes tributar")

# 12 - Els alumnes d'un curs s’han dividit en dos grups A i B d’acord amb el sexe i el nom. El grup A està format per les dones amb un nom anterior a la M 
# i els homes amb un nom posterior a la N i el grup B per la resta. Escriu un programa que pregunti a l'usuari el nom i el sexe, i mostri per pantalla el grup que li correspon.

nombre = input("Introduce tu nombre: ").upper()
sexo = input("Introduce tu sexo (H/M): ").upper()
if (sexo == "M" and nombre < "M") or (sexo == "H" and nombre > "N"):
    print("Perteneces al grupo A")
else:
    print("Perteneces al grupo B")

# 13 - Escriu un programa que pregunti a l'usuari la renda anual i mostri per pantalla el tipus impositiu que li correspon.
# Els trams impositius per a la declaració de la renda en un país determinat són els següents:
# Renda Tipus impositiu
# Menys de 10000€ 		5%
# Entre 10000€ i 20000€ 	15%
# Entre 20000€ i 35000€ 	20%
# Entre 35000€ i 60000€ 	30%
# Més de 60000€ 		45%

renta = float(input("Introduce tu renta anual: "))
if renta < 10000:
    print("Impuesto: 5%")
elif renta < 20000:
    print("Impuesto: 15%")
elif renta < 35000:
    print("Impuesto: 20%")
elif renta < 60000:
    print("Impuesto: 30%")
else:
    print("Impuesto: 45%")

# Exercicis amb match

# 1 - Implementa un programa que verifiqui si una fruita és "poma", "plàtan" o "una altra" utilitzant match.

fruta = input("Introduce una fruta: ")
match fruta.lower():
    case "manzana":
        print("Es una manzana")
    case "plátano" | "platano":
        print("Es un plátano")
    case _:
        print("Es otra fruta")

# 2 - Implementa una funció que determini el dia de la setmana a partir d'un número de l'1 al 7 fent servir match.

num = int(input("Introduce un número (1-7): "))
match num:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miércoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sábado")
    case 7:
        print("Domingo")
    case _:
        print("Número no válido")

# 3 - Escriu un programa que rebi com a entrada (serà l'entrada per teclat) els codis: 200, 301, 302, 404, 500 i 503. El significat d'aquests codis és el següent: 
# '200' = 'Tot ok', '301' = 'Moviment permanent de la pàgina', '302' = 'Moviment temporal de la pàgina', '404' = 'Pàgina no trobada', '500' = 'Error intern del servidor', 
# '503' = 'Servidor no disponible '. El programa haurà de tornar el missatge corresponent al codi introduït. Si s'introdueix un codi no comprès entre aquests, 
# el programa ha de tornar per pantalla el missatge 'Missatge desconegut'. Tot això ho hauràs de ver fent servir match.

codi = int(input("Introduce un código HTTP: "))
match codi:
    case 200:
        print("Todo ok")
    case 301:
        print("Movimiento permanente de la página")
    case 302:
        print("Movimiento temporal de la página")
    case 404:
        print("Página no encontrada")
    case 500:
        print("Error interno del servidor")
    case 503:
        print("Servidor no disponible")
    case _:
        print("Mensaje desconocido")

