
import sys

ventas = {
    "Enero": 15000,
    "Febrero": 22000,
    "Marzo": 12000,
    "Abril": 17000,
    "Mayo": 81000,
    "Junio": 13000,
    "Julio": 21000,
    "Agosto": 41200,
    "Septiembre": 25000,
    "Octubre": 21500,
    "Noviembre": 91000,
    "Diciembre": 21000,
}


try:
    umbral = int(sys.argv[1])
except ValueError:
    print("Error: El umbral debe ser un número entero.")
    sys.exit(1)

mayor_umbral = {}

for mes, valor in ventas.items():
    if valor > umbral: # valor mayor que umbral
        mayor_umbral[mes] = valor # añade mes y valor al dicc.


print(mayor_umbral)

