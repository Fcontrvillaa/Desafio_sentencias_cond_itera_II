
import string
import getpass


password_oculta = getpass.getpass("Ingrese la contraseña: ")

intentos = 0

password_lower = password_oculta.lower()

for caracter_password in password_lower:
    
    for caracter in string.ascii_lowercase:
        intentos += 1  # Cuenta cada intento 
        
        if caracter_password == caracter:
            break  # Si la letra coincide, pasamos a la siguiente letra de la contraseña

print(f"La contraseña fue forzada en {intentos} intentos")
