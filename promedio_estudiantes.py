# notas de los estudiantes
notas_estudiantes = {
    'Juan': [3.2, 4.5, 5],
    'Maria': [4.2, 3.5, 4.3],
    'Pedro': [3.9, 2.5, 4.8]
}

# calcular el promedio de una lista de notas
def calcular_promedio(notas):
    total = sum(notas)
    promedio = total / len(notas)
    return promedio

# Calcular el promedio de cada estudiante-
for estudiante, notas in notas_estudiantes.items():
    promedio = calcular_promedio(notas)
    print(f'El promedio de {estudiante} es: {promedio:.2f}')