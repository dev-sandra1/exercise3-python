#Dada una lista de eventos con fechas de inicio y fin,
# para encontrar eventos cuya duración sea mayor de 5 días. Luego, agrupa los eventos por mes de inicio.

from datetime import datetime
from itertools import groupby

# Lista de eventos con fechas de inicio y fin
eventos = [
    {"nombre": "Evento A", "inicio": "2024-01-10", "fin": "2024-01-17"},
    {"nombre": "Evento B", "inicio": "2024-01-20", "fin": "2024-01-22"},
    {"nombre": "Evento C", "inicio": "2024-02-01", "fin": "2024-02-10"},
    {"nombre": "Evento D", "inicio": "2024-03-15", "fin": "2024-03-20"},
    {"nombre": "Evento E", "inicio": "2024-03-05", "fin": "2024-03-11"}
]

# Función para calcular la duración de un evento en días
def duracion_dias(evento):
    inicio = datetime.strptime(evento["inicio"], "%Y-%m-%d")
    fin = datetime.strptime(evento["fin"], "%Y-%m-%d")
    return (fin - inicio).days

# Filtrar eventos cuya duración sea mayor de 5 días
eventos_largos = list(filter(lambda evento: duracion_dias(evento) > 5, eventos))

# Ordenar eventos por mes de inicio
eventos_largos.sort(key=lambda x: datetime.strptime(x["inicio"], "%Y-%m-%d").month)

# Agrupar eventos por el mes en que inician
agrupados_por_mes = {k: list(g) for k, g in groupby(eventos_largos, key=lambda x: datetime.strptime(x["inicio"], "%Y-%m-%d").month)}

# Mostrar los resultados
print(f"Eventos largos agrupados por mes: {agrupados_por_mes}")
