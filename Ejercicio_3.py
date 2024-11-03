#Dada una lista de productos con diferentes categorías y precios, para agrupar los productos por categoría,
#y luego filtra las categorías que tengan productos cuyo precio promedio sea mayor a 50.

from itertools import groupby # Importamos la función groupby de itertools

productos = [
    {"nombre": "Laptop", "categoria": "Tecnología", "precio": 1200},
    {"nombre": "Celular", "categoria": "Tecnología", "precio": 800},
    {"nombre": "Mouse", "categoria": "Tecnología", "precio": 25},
    {"nombre": "Mesa", "categoria": "Muebles", "precio": 300},
    {"nombre": "Silla", "categoria": "Muebles", "precio": 75},
    {"nombre": "Lámpara", "categoria": "Muebles", "precio": 20}, 
]

# Ordenar por categoría para usar groupby
productos.sort(key=lambda x: x["categoria"])

# Agrupar por categoría
agrupados = {key: list(group) for key, group in groupby(productos, key=lambda x: x["categoria"])}

# Filtrar categorías cuyo promedio de precios sea mayor a 50
categorias_filtradas = {categoria: productos for categoria, productos in agrupados.items() if sum(p["precio"] for p in productos) / len(productos) > 50}

print(f"Categorías con precio promedio mayor a 50: {categorias_filtradas}") # Mostramos el resultado
