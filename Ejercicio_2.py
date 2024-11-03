#Dada una lista de diccionarios que representan empleados (nombre, edad, salario), filtra a aquellos
#  empleados que son mayores de 30 años y ganan más de 5000. Luego,
# para aplicar un aumento de salario del 10% solo a ellos

empleados = [
    {"nombre": "Carlos", "edad": 25, "salario": 3000},
    {"nombre": "María", "edad": 35, "salario": 6000},
    {"nombre": "Ana", "edad": 45, "salario": 7000},
    {"nombre": "Juan", "edad": 40, "salario": 4000}
]

mayores_y_altos_salarios = list(filter(lambda e: e['edad'] > 30 and e['salario'] > 5000, empleados))
aumento = list(map(lambda e: {**e, "salario": e["salario"] * 1.1}, mayores_y_altos_salarios))

print(f"Empleados con aumento de salario: {aumento}")
