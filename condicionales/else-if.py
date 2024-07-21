ingreso_mensual = 11000
gasto_mensual = 12000

# If anidados, son if adentro de otros if
if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual >= 3000:
        print("Ahora si estas bien")
    elif ingreso_mensual - gasto_mensual < 0:
        print("Estas gastando demas")
    else:
        print("Tenes que ahorrar mas")
elif ingreso_mensual > 1000:
    print("Estas bien economicamente en latinoamerica")
elif ingreso_mensual > 500:
    print("Estas bien en Argentina")
elif ingreso_mensual > 200:
    print("Estas bien en Venezuela")
else:
    print("Sos Pobre")
