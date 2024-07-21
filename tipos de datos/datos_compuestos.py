# array de varios datos o conjunto de datos
# creando una lista, se pueden modificar
lista = ["Abel Amarilla", True, 1.70]

# creando una tupla, no se puede modificar
tupla = ("Abel Amarilla", True, 1.70)

# esto es valido
lista[2] = "maquina"

# esto no
# tupla[2] = "maquina"

# creando un conjunto (set)
# son elementos desordenados que pueden intercambiar posiciones
# no se pude acceder por indices
# en un conjunto no pueden haber datos duplicados
# para acceder dentro debemos utilizar un blucle
conjunto = {"Abel Amarilla", True, 1.70}

# creando un diccionario
# las tuplas no se pueden modificar
diccionario = {"nombre": "Abel Amarilla", "esta_emocionado": True, "altura": 1.70}
print(diccionario["altura"] + 2)
