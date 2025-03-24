# Nombre del estudiante: Luis Navarro Masson
# Grupo: 81
# Número y Texto del programa: Problema 1 - Matrices Bidimensionales - Clasificación de atletas
# Código Fuente: autoría propia

import numpy as np

# Nombres de los corredores
corredores = ["Juan", "Carlos", "Pedro", "Roberto", "Raúl", "David"]

# Matriz de tiempos (6 atletas x 6 carreras)
# Valores simulados entre 10.1 y 10.5 segundos
tiempos = np.array([
    [10.2, 10.3, 10.1, 10.4, 10.3, 10.2],  # Juan (válido)
    [10.5, 10.4, 10.3, 10.2, 10.1, 10.4],  # Carlos (inválido, tiene un 10.5)
    [10.3, 10.3, 10.3, 10.3, 10.3, 10.3],  # Pedro (válido)
    [10.4, 10.4, 10.4, 10.4, 10.4, 10.4],  # Roberto (válido)
    [10.1, 10.2, 10.5, 10.3, 10.4, 10.2],  # Raúl (inválido)
    [10.2, 10.1, 10.2, 10.3, 10.4, 10.1],  # David (válido)
])

# Listas para guardar promedios y mejores tiempos válidos
promedios_validos = []
mejores_tiempos = []

# Evaluar cada corredor
for i in range(len(corredores)):
    tiempos_atleta = tiempos[i]
    if np.all(tiempos_atleta <= 10.4):  # Solo si todos sus tiempos son válidos
        promedio = np.mean(tiempos_atleta)
        mejor_tiempo = np.min(tiempos_atleta)
        promedios_validos.append((promedio, corredores[i]))
        mejores_tiempos.append((mejor_tiempo, corredores[i]))

# Selección por mejor tiempo
if mejores_tiempos:
    mejor_por_tiempo = min(mejores_tiempos, key=lambda x: x[0])
else:
    mejor_por_tiempo = ("N/A", "Ninguno clasifica")

# Selección por mejor promedio
if promedios_validos:
    mejor_por_promedio = min(promedios_validos, key=lambda x: x[0])
else:
    mejor_por_promedio = ("N/A", "Ninguno clasifica")

# Mostrar resultados
print("Matriz de Tiempos (6 atletas x 6 carreras):\n")
for i in range(len(corredores)):
    print(f"{corredores[i]:<8}: {', '.join(f'{t:.1f}' for t in tiempos[i])}")

print("\n🏅 Clasificados:")
print(f"- Por Mejor Tiempo   -> {mejor_por_tiempo[1]} con {mejor_por_tiempo[0]:.2f} s")
print(f"- Por Mejor Promedio -> {mejor_por_promedio[1]} con {mejor_por_promedio[0]:.3f} s")
