listaejemplo = [15,12,34,56,12,12,3,4,6,5,7,8]

# 1 - Imprimer por pantalla cuantas veces aparece el número 12.
# ej de impresión: "El número 12 aparece x veces"

print("El número de veces que aparece 12 es:", listaejemplo.count(12))

# 2 - Inserta un número leído por teclado en la posición 4 de la lista.

listaejemplo.insert(3, int(input("Introduce un número")))
print(listaejemplo)

# 3 - Imprime la lista con los elementos invertidos de posición.

listaejemplo.reverse()
print(listaejemplo)

# 4 - Tienes otra lista: [1,2,3]. Añadela como único elemento al final de lista ejemplo.

listaejemplo2 = [1,2,3]
listaejemplo.append(listaejemplo2)
print(listaejemplo)


# 5 - Extiende la lista ejemplo con los elementos de la lista del punto anterior.

listaejemplo.extend(listaejemplo2)
print(listaejemplo)

# 6 - Extrae el elemnto 12 de la lista (una vez) y imprime como queda la lista al extraerlo.

listaejemplo.remove(12)
print(listaejemplo)


# Ejercicio rápido:
# Crea una lista que tenga 3 dimensiones en la que cada sublista contenga al menos 3 elementos.
# Quiero que imprimais el 3er elemento de la lista que está dentro del 3er elemento de la lista
# que se encuentre en la 3a posición de la lista principal "listatri"

listatri = [[[1,2,3], [4,5,6], [7,8,9]], [[1,2,3], [4,5,6], [7,8,9]], [[1,2,3], [4,5,6], [7,8,9]]]
print(f"El tercer elemento de la lista que está dentro del tercer elemento de la lista que se encuentra en la tercera posicion de la lista principal es: {listatri[2][2][2]}")