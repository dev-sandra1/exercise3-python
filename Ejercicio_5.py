#Dada una lista de números romanos, convierte cada uno a su equivalente entero, filtra aquellos que sean mayores de 50 y 
# luego agrúpalos en rangos (por ejemplo, de 50 a 100, de 100 a 200, etc.).

# Diccionario que mapea símbolos romanos a sus valores enteros
valores_romanos = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
}

# Función para convertir número romano a entero
def romano_a_entero(romano):
    total = 0
    prev_value = 0
    for char in reversed(romano):
        value = valores_romanos[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    return total

# Lista de números romanos
numeros_romanos = ['X', 'L', 'C', 'D', 'M', 'IV', 'XL', 'XC', 'CD', 'CM', 'LXXX', 'XCIX', 'MD']

# Convertir cada número romano a entero
numeros_enteros = list(map(romano_a_entero, numeros_romanos))

# Filtrar números mayores de 50
numeros_mayores_50 = list(filter(lambda x: x > 50, numeros_enteros))

# Función para agrupar números por rangos de 50 en 50
def agrupar_por_rango(numeros, intervalo=50):
    agrupados = {}
    for num in numeros:
        rango_min = (num // intervalo) * intervalo
        rango_max = rango_min + intervalo
        rango = f"{rango_min}-{rango_max}"
        if rango not in agrupados:
            agrupados[rango] = []
        agrupados[rango].append(num)
    return agrupados

# Agrupar los números filtrados por rango
numeros_agrupados = agrupar_por_rango(numeros_mayores_50)

# Mostrar los resultados
print(f"Números romanos convertidos y agrupados por rango: {numeros_agrupados}")
