
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

# Check if a threshold argument was provided
if len(sys.argv) < 2:
    print("Usage: python mayor_a.py <umbral>")
    sys.exit(1) # Exit the script with an error code

# Get the threshold from the command line arguments
try:
    umbral = int(sys.argv[1])
except ValueError:
    print("Error: El umbral debe ser un número entero.")
    sys.exit(1)

# Create an empty dictionary to store months exceeding the threshold
ventas_superiores_umbral = {}

# Iterate through the sales dictionary
for mes, valor in ventas.items():
    if valor > umbral:
        ventas_superiores_umbral[mes] = valor

# Print the resulting dictionary
print(ventas_superiores_umbral)