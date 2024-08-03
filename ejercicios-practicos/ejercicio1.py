#a) Diferencia en porcentaje entre el curso actual y:
#   el mas rapido de otros cursos
#   el mas lento de otros cursos
#   el promedio de los cursos

curso_actual = 90
otros_cursos_rapidos = 150
otros_cursos_lentos = 420
pro_cursos = 240

diferencia = 100 - ((curso_actual / otros_cursos_rapidos)*100) 
diferencia_Clento = 100 - ((curso_actual / otros_cursos_lentos)*100)
prom = 100 - ((curso_actual / pro_cursos)*100)
print(f"""La diferencia entre el porcentaje actual y el mas rapido de otros cursos es: {diferencia}%
      La diferencia entre el porcentaje actual y el mas lento de otros cursos es: {diferencia_Clento:.3f}%
      La diferencia entre el porcentaje actual y el promedio es: {prom}%""")
#b) Porcentaje de material inservible que se reduce en:
#   el promedio de los cursos
#   el curso actual(este curso)

crudo_actual = 3.5
promedio_actual = 1.5
crudo_otros = 5
promedio_otros = 4

prom_actual = 100 - ((promedio_actual / crudo_actual)*100) 
promedio_cursos = 100 - ((promedio_otros / crudo_otros)*100) 

print(f"""El porcentaje de material inservible que se reduce en:
      El promedio de los cursos: {promedio_cursos}% y
      El curso actual: {prom_actual:.3f}%""")

#c) Ver 10 horas de este curso, a cuantos de otros cursos equivale?
#   ¿y alreves?

horas = 10
curso = 1.5
otros = 7
este_curso = ((curso / horas)*100)-otros
cursos_otros = ((otros / horas)*100)-curso

print(este_curso)
print(cursos_otros)