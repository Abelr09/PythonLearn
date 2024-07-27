# creando una lista con list
lista = list([22, True, False])
cadena = "hola"

# devuelve la cantidad de elementos a la lista
cantidad_element = len(lista)

# agregando un elemento a la lista
lista.append(True)

# agregando un elemento a la lista en un indice especifico
lista.insert(2, 5)

# agregando varios elementos a la lista
lista.extend([2, 20])

# eliminando un elemento de la lista por indice
lista.pop()

# removiendo un elemento a la lista por su valor
lista.remove(2)

# eliminando todos los elementos de la lista
# lista.clear()
# ordenando los elementos de forma ascendente
# con reverse=True lo ordena en reversa de forma descendente
lista.sort(reverse=True)

# Invertimos los elementos de una lista
lista.reverse()

# verificamos si in elemento se encuentra en una lista
elemento_encontrado = lista.index(22)

print(elemento_encontrado)
