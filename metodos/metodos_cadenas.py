cadena1 = "a,e,i,o,u"
cadena2 = "Bienvenido"


# DIR devuelve la lista de atruibutos validos del objeto pasado
resultado = dir(cadena1)

# UPPER convierte todo a mayusculas
mayusc = cadena1.upper()

# LOWER convierte todo a minusculas
minusc = cadena1.lower()

# CAPITALIZE convierte la primera letra en mayuscula
primer_letra_mayusc = cadena1.capitalize()

# LOS SIGTES METODOS BUSCAN UN VALOR
# FIND buscamos una cadena en otra cadena
busqueda_find = cadena1.find("a")

# INDEX devuelve el primer valor, sino devuelve una excepcion
busqueda_index = cadena1.index("a")

# LOS SIGTES METODOS CONSULTAN UN VALOR
# IS_NUMERIC devuelve TRUE si el valor es numerico
is_numeric = cadena1.isnumeric()

# ISALPHA devuelve TRUE si el valor es alfa numerico
is_alpha = cadena1.isalpha()

# COUNT devuelve la canidad de veces que coincida ina letra o palabra
contar_coincidencias = cadena1.count("hola")

# LEN cuenta los caracteres de una cadena
contar_caracteres = len(cadena1)

# Verificamos si una cadena empieza con otra cadena dada, si es asi devuelve True
empieza_con = cadena1.startswith("ho")

# Verificamos si una cadena termina con otra cadena dada, si es asi devuelve True
termina_con = cadena1.endswith("hola")

# Reemplaza un pedazo de la cadena dada , por otra
# si el valor 1, se encuentra en la cadena original, reemplaza el valor 1 por la misma,
# por el valor 2
cadena_nueva = cadena1.replace(",", " ")
cadena_nueva2 = cadena_nueva.capitalize()

# Separa cadenas con la cadena que le pasemos
cadena_separada = cadena1.split(" ")
print(cadena_separada)
