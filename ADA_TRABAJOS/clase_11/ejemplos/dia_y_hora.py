# Importar el módulo
import datetime

# Fecha actual
fecha_actual = datetime.date.today()
print(f'Fecha actual: {fecha_actual}')

# Hora actual
hora_actual = datetime.datetime.now().time()
print(f'Hora actual: {hora_actual}')

# Fecha y hora actual
fecha_hora_actual = datetime.datetime.now()
print(f'La fecha y hora actual es {fecha_hora_actual}')

# Crear una fecha y una hora específica
mi_fecha = datetime.date(2024, 8, 22)
mi_hora = datetime.time(14, 30, 0)

print(f'Fecha específica: {mi_fecha}')
print(f'Hora específica: {mi_hora}')

# Cálculos con fechas: sumar 10 dias a la fecha actual

diferencia = datetime.timedelta(days=10)

nueva_fechaa = fecha_actual + diferencia

print(f"Fecha despues de 10 dias: {nueva_fechaa}")