diccionario = {"nombre": "Abel", "apellido": "Amarilla", "edad": 22}

# llamando a las claves
claves = diccionario.keys()

# obteniendo un elemento (si no encuentra nada el programa continua)
valor = diccionario.get("nombre")

# eliminando todos los datos
# diccionario.clear()

# eliminando un elemento del diccionario
diccionario.pop("nombre")

# obteniendo un elemento idct_items iterable
diccionario_iterable = diccionario.items()

print(diccionario_iterable)
