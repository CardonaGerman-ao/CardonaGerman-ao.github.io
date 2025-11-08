# Para el próximo día me váis a investigar qué hacen los siguientes métodos e las listas.

# list.append()
# Agrega un elemento al final de la lista.

frutas = ["manzana", "pera"]
frutas.append("plátano")
print(frutas)

# list.clear()
# Elimina los elementos de la lista (la deja vacía).

frutas = ["manzana", "pera"]
frutas.clear()
print(frutas)

# list.count()
# Cuenta cuantas veces aparece un elemento en la lista.

numeros = [1, 2, 2, 3, 2]
print(numeros.count(2))

# list.extend()
# Agrega los elementos de otra lista al final de la lista.

frutas = ["manzana", "pera"]
mas_frutas = ["uva", "melón"]
frutas.extend(mas_frutas)
print(frutas)

# list.insert()
# Inserta un elemento en una posición específica.

frutas = ["manzana", "pera"]
frutas.insert(1, "plátano")
print(frutas)

# list.remove()
# Elimina la primera aparición del elemento indicado.

numeros = [1, 2, 3, 2]
numeros.remove(2)
print(numeros)

# list.reverse()
# Invierte el orden de los elementos en la lista.

numeros = [1, 2, 3, 4]
numeros.reverse()
print(numeros)

# Ayudaos del bocadillo contextual de Python.