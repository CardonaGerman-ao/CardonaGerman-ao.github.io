

# 13 - Escriu un programa que pregunti quants números s'introduiran, demaneu aquests números, i mostri un missatge cada vegada 
# que un nombre no sigui més gran que el primer nombre introduït.

cantidad = int(input("¿Cuántos números vas a introducir?: "))
primer_numero = int(input("Introduce el primer número: "))
i = 1

while i < cantidad:
    numero = int(input("Introduce otro número: "))
    if numero <= primer_numero:
        print("El número", numero, "no es mayor que el primero")
    i += 1